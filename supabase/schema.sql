-- Socratic Thinking MCP - Supabase Schema
-- pgvector extension for semantic search

-- Enable pgvector extension
create extension if not exists vector;

-- Main knowledge documents table
create table if not exists thinking_tools (
    id text primary key,
    title text not null,
    title_kr text,
    category text not null,
    category_kr text,
    difficulty text check (difficulty in ('beginner', 'intermediate', 'advanced', 'expert')),
    time_required text,
    group_size text,
    origin text,

    -- Full content
    content text not null,

    -- Metadata arrays (stored as JSONB)
    keywords jsonb default '[]'::jsonb,
    use_cases jsonb default '[]'::jsonb,
    related_methods jsonb default '[]'::jsonb,
    complementary_methods jsonb default '[]'::jsonb,

    -- Vector embedding (OpenAI text-embedding-3-small: 1536 dimensions)
    embedding vector(1536),

    -- Timestamps
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);

-- Categories reference table
create table if not exists categories (
    id text primary key,
    name_kr text not null,
    description text,
    tool_count integer default 0
);

-- Clusters reference table
create table if not exists clusters (
    id serial primary key,
    name text not null,
    name_kr text,
    core_tool text references thinking_tools(id),
    members jsonb default '[]'::jsonb
);

-- Workflows reference table
create table if not exists workflows (
    id text primary key,
    name_kr text,
    description text,
    steps jsonb default '[]'::jsonb
);

-- Insert categories
insert into categories (id, name_kr, description) values
    ('question_inquiry', '질문/탐구', '문제를 질문을 통해 탐구하고 정의하는 도구'),
    ('creative_divergent', '창의적 발산', '새로운 아이디어를 창출하고 발산하는 도구'),
    ('analysis_convergent', '분석/수렴', '정보를 분석하고 수렴하여 결론을 도출하는 도구'),
    ('strategy_planning', '전략/계획', '전략을 수립하고 계획을 세우는 도구'),
    ('problem_solving', '문제해결', '복잡한 문제를 체계적으로 해결하는 도구'),
    ('innovation_design', '혁신/디자인', '혁신적 제품/서비스를 설계하는 도구'),
    ('visualization', '시각화', '아이디어와 관계를 시각적으로 표현하는 도구'),
    ('decision_making', '의사결정', '대안을 평가하고 결정을 내리는 도구'),
    ('intuitive_creative', '직관적 사고', '직관과 무의식을 활용한 창의적 도구'),
    ('group_collaboration', '그룹/협업', '그룹이 함께 사고하고 협업하는 도구'),
    ('structured_thinking', '구조화 사고', '정보를 체계적으로 구조화하는 도구'),
    ('root_cause', '근본원인 분석', '문제의 근본 원인을 분석하는 도구')
on conflict (id) do nothing;

-- Create indexes for fast search
create index if not exists idx_thinking_tools_category on thinking_tools(category);
create index if not exists idx_thinking_tools_difficulty on thinking_tools(difficulty);
create index if not exists idx_thinking_tools_keywords on thinking_tools using gin(keywords);
create index if not exists idx_thinking_tools_use_cases on thinking_tools using gin(use_cases);

-- Vector similarity search index (IVFFlat for large datasets)
create index if not exists idx_thinking_tools_embedding on thinking_tools
using ivfflat (embedding vector_cosine_ops) with (lists = 10);

-- Function: Hybrid search (vector + metadata)
create or replace function search_thinking_tools(
    query_embedding vector(1536),
    match_threshold float default 0.7,
    match_count int default 5,
    filter_category text default null,
    filter_difficulty text default null
)
returns table (
    id text,
    title text,
    category text,
    difficulty text,
    content text,
    similarity float,
    related_methods jsonb,
    complementary_methods jsonb
)
language plpgsql
as $$
begin
    return query
    select
        t.id,
        t.title,
        t.category,
        t.difficulty,
        t.content,
        1 - (t.embedding <=> query_embedding) as similarity,
        t.related_methods,
        t.complementary_methods
    from thinking_tools t
    where
        1 - (t.embedding <=> query_embedding) > match_threshold
        and (filter_category is null or t.category = filter_category)
        and (filter_difficulty is null or t.difficulty = filter_difficulty)
    order by t.embedding <=> query_embedding
    limit match_count;
end;
$$;

-- Function: Get related tools
create or replace function get_related_tools(tool_id text)
returns table (
    id text,
    title text,
    category text,
    relation_type text
)
language plpgsql
as $$
declare
    related jsonb;
    complementary jsonb;
begin
    select t.related_methods, t.complementary_methods
    into related, complementary
    from thinking_tools t
    where t.id = tool_id;

    -- Return related methods
    return query
    select
        t.id,
        t.title,
        t.category,
        'related'::text as relation_type
    from thinking_tools t
    where t.id = any(select jsonb_array_elements_text(related));

    -- Return complementary methods
    return query
    select
        t.id,
        t.title,
        t.category,
        'complementary'::text as relation_type
    from thinking_tools t
    where t.id = any(select jsonb_array_elements_text(complementary));
end;
$$;

-- Function: Search by use case
create or replace function search_by_use_case(use_case text)
returns table (
    id text,
    title text,
    category text,
    difficulty text
)
language sql
as $$
    select t.id, t.title, t.category, t.difficulty
    from thinking_tools t
    where t.use_cases ? use_case
    order by t.title;
$$;

-- Update timestamp trigger
create or replace function update_updated_at()
returns trigger as $$
begin
    new.updated_at = now();
    return new;
end;
$$ language plpgsql;

create trigger thinking_tools_updated_at
    before update on thinking_tools
    for each row
    execute function update_updated_at();
