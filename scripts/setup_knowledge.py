"""
Socratic Thinking MCP - Knowledge Setup Script
지식 파일 자동 설치 스크립트

사용법:
    python scripts/setup_knowledge.py

GitHub에서 최신 지식 파일을 다운로드하거나,
로컬에서 지식 파일을 생성합니다.
"""

import os
import sys
import urllib.request
import zipfile
from pathlib import Path

# 설정 - 실제 GitHub repo로 변경 필요
GITHUB_REPO = "your-username/innovation-socratic-mcp"
RELEASE_TAG = "latest"
KNOWLEDGE_ZIP_URL = f"https://github.com/{GITHUB_REPO}/releases/download/{RELEASE_TAG}/knowledge.zip"

def get_project_root():
    return Path(__file__).parent.parent

def check_knowledge_exists():
    knowledge_dir = get_project_root() / "knowledge"
    if knowledge_dir.exists():
        md_files = list(knowledge_dir.glob("[0-9]*.md"))
        return len(md_files) >= 70
    return False

def download_from_release():
    print(f"Downloading from {KNOWLEDGE_ZIP_URL}...")
    try:
        knowledge_dir = get_project_root() / "knowledge"
        zip_path = get_project_root() / "knowledge.zip"
        urllib.request.urlretrieve(KNOWLEDGE_ZIP_URL, zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(get_project_root())
        zip_path.unlink()
        print(f"Installed to {knowledge_dir}")
        return True
    except Exception as e:
        print(f"Download failed: {e}")
        return False

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Setup knowledge files')
    parser.add_argument('--download', action='store_true', help='Force download')
    parser.add_argument('--check', action='store_true', help='Check existence')
    args = parser.parse_args()
    
    if args.check:
        exists = check_knowledge_exists()
        print("Installed" if exists else "Not installed")
        return 0 if exists else 1
    
    if check_knowledge_exists() and not args.download:
        print("Knowledge files exist. Use --download to reinstall.")
        return 0
    
    download_from_release()
    return 0

if __name__ == "__main__":
    sys.exit(main())
