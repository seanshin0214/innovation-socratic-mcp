"""
Socratic Thinking MCP - Knowledge Base Upload Script
지식 파일을 Supabase에 벡터화하여 업로드

사용법:
    # 환경변수 설정 후 실행
    export SUPABASE_URL="your-project-url"
    export SUPABASE_KEY="your-service-key"
    export OPENAI_API_KEY="your-openai-key"

    python supabase/upload_knowledge.py

    # 또는 특정 파일만 업로드
    python supabase/upload_knowledge.py --file 01-Question-Storming.md
"""

import os
import sys
import json
import re
import yaml
from pathlib import Path
from typing import Optional
import argparse

# Dependencies
try:
    from supabase import create_client, Client
    from openai import OpenAI
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install supabase openai pyyaml")
    sys.exit(1)


def get_project_root() -> Path:
    """프로젝트 루트 경로 반환"""
    return Path(__file__).parent.parent


def parse_markdown_file(file_path: Path) -> dict:
    """마크다운 파일에서 YAML frontmatter와 본문 분리"""
    content = file_path.read_text(encoding='utf-8')

    # YAML frontmatter 추출
    yaml_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)

    if yaml_match:
        yaml_content = yaml_match.group(1)
        body_content = yaml_match.group(2).strip()

        try:
            metadata = yaml.safe_load(yaml_content)
        except yaml.YAMLError as e:
            print(f"YAML parse error in {file_path.name}: {e}")
            metadata = {}
    else:
        metadata = {}
        body_content = content

    return {
        'metadata': metadata,
        'content': body_content,
        'filename': file_path.stem
    }


def generate_embedding(client: OpenAI, text: str) -> list[float]:
    """OpenAI API로 텍스트 임베딩 생성"""
    # 텍스트 길이 제한 (8191 토큰 제한)
    max_chars = 8000 * 4  # 대략적인 토큰-문자 비율
    if len(text) > max_chars:
        text = text[:max_chars]

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


def prepare_document(parsed: dict) -> dict:
    """업로드용 문서 데이터 준비"""
    meta = parsed['metadata']

    # ID 생성 (파일명 기반)
    doc_id = meta.get('id', parsed['filename'].lower().replace(' ', '-'))

    # 검색용 텍스트 생성 (제목 + 키워드 + 본문)
    search_text_parts = [
        meta.get('title', ''),
        ' '.join(meta.get('keywords', [])),
        parsed['content'][:4000]  # 본문 앞부분
    ]
    search_text = '\n'.join(filter(None, search_text_parts))

    return {
        'id': doc_id,
        'title': meta.get('title', parsed['filename']),
        'title_kr': meta.get('title', '').split('(')[-1].rstrip(')') if '(' in meta.get('title', '') else None,
        'category': meta.get('category', 'uncategorized'),
        'category_kr': meta.get('category_kr', ''),
        'difficulty': meta.get('difficulty', 'intermediate'),
        'time_required': meta.get('time_required', ''),
        'group_size': meta.get('group_size', ''),
        'origin': meta.get('origin', ''),
        'content': parsed['content'],
        'keywords': json.dumps(meta.get('keywords', []), ensure_ascii=False),
        'use_cases': json.dumps(meta.get('use_cases', []), ensure_ascii=False),
        'related_methods': json.dumps(meta.get('related_methods', []), ensure_ascii=False),
        'complementary_methods': json.dumps(meta.get('complementary_methods', []), ensure_ascii=False),
        'search_text': search_text
    }


def upload_document(
    supabase: Client,
    openai_client: OpenAI,
    doc: dict,
    dry_run: bool = False
) -> bool:
    """문서를 Supabase에 업로드"""
    try:
        # dry_run이면 파싱 정보만 출력
        if dry_run:
            print(f"  [DRY RUN] Would upload: {doc['id']}")
            print(f"    Title: {doc['title']}")
            print(f"    Category: {doc['category']}")
            return True

        # 임베딩 생성
        embedding = generate_embedding(openai_client, doc['search_text'])

        # 업로드 데이터 준비
        upload_data = {
            'id': doc['id'],
            'title': doc['title'],
            'title_kr': doc['title_kr'],
            'category': doc['category'],
            'category_kr': doc['category_kr'],
            'difficulty': doc['difficulty'],
            'time_required': doc['time_required'],
            'group_size': doc['group_size'],
            'origin': doc['origin'],
            'content': doc['content'],
            'keywords': doc['keywords'],
            'use_cases': doc['use_cases'],
            'related_methods': doc['related_methods'],
            'complementary_methods': doc['complementary_methods'],
            'embedding': embedding
        }

        # Upsert (있으면 업데이트, 없으면 삽입)
        result = supabase.table('thinking_tools').upsert(upload_data).execute()

        if result.data:
            print(f"  Uploaded: {doc['id']}")
            return True
        else:
            print(f"  Failed: {doc['id']}")
            return False

    except Exception as e:
        print(f"  Error uploading {doc['id']}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Upload knowledge files to Supabase')
    parser.add_argument('--file', type=str, help='Upload specific file only')
    parser.add_argument('--dry-run', action='store_true', help='Parse files without uploading')
    parser.add_argument('--skip-existing', action='store_true', help='Skip files already in database')
    args = parser.parse_args()

    # 환경변수 확인
    supabase_url = os.environ.get('SUPABASE_URL')
    supabase_key = os.environ.get('SUPABASE_KEY')
    openai_key = os.environ.get('OPENAI_API_KEY')

    # dry-run이 아닐 때만 환경변수 필수
    if not args.dry_run and not all([supabase_url, supabase_key, openai_key]):
        print("Error: Missing environment variables")
        print("Required: SUPABASE_URL, SUPABASE_KEY, OPENAI_API_KEY")
        sys.exit(1)

    # 클라이언트 초기화 (dry-run이면 None)
    supabase = None
    openai_client = None
    if not args.dry_run:
        supabase = create_client(supabase_url, supabase_key)
        openai_client = OpenAI(api_key=openai_key)

    # Knowledge 폴더 경로
    knowledge_dir = get_project_root() / "knowledge"

    if not knowledge_dir.exists():
        print(f"Error: Knowledge directory not found: {knowledge_dir}")
        sys.exit(1)

    # 파일 목록 수집
    if args.file:
        files = [knowledge_dir / args.file]
        if not files[0].exists():
            print(f"Error: File not found: {args.file}")
            sys.exit(1)
    else:
        files = sorted(knowledge_dir.glob("[0-9]*.md"))

    print(f"Found {len(files)} knowledge files")

    # 기존 문서 ID 조회 (skip-existing 옵션용)
    existing_ids = set()
    if args.skip_existing:
        try:
            result = supabase.table('thinking_tools').select('id').execute()
            existing_ids = {row['id'] for row in result.data}
            print(f"Found {len(existing_ids)} existing documents in database")
        except Exception as e:
            print(f"Warning: Could not fetch existing documents: {e}")

    # 업로드 실행
    success_count = 0
    skip_count = 0
    fail_count = 0

    for file_path in files:
        print(f"\nProcessing: {file_path.name}")

        # 파일 파싱
        parsed = parse_markdown_file(file_path)
        doc = prepare_document(parsed)

        # Skip 체크
        if args.skip_existing and doc['id'] in existing_ids:
            print(f"  Skipped (exists): {doc['id']}")
            skip_count += 1
            continue

        # 업로드
        if upload_document(supabase, openai_client, doc, dry_run=args.dry_run):
            success_count += 1
        else:
            fail_count += 1

    # 결과 출력
    print(f"\n{'='*50}")
    print(f"Upload complete!")
    print(f"  Success: {success_count}")
    print(f"  Skipped: {skip_count}")
    print(f"  Failed:  {fail_count}")
    print(f"  Total:   {len(files)}")


if __name__ == "__main__":
    main()
