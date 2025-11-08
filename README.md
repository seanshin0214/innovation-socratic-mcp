# 🤔 Socratic Thinking MCP

> **AI that asks, not answers** | 질문하는 AI, 소크라테스처럼

[![MCP](https://img.shields.io/badge/MCP-Model_Context_Protocol-blue)](https://modelcontextprotocol.io)
[![Python](https://img.shields.io/badge/Python-3.10+-green)](https://www.python.org)
[![Methodologies](https://img.shields.io/badge/Methodologies-78+-orange)](knowledge/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 💡 Why This Exists

Most AI tools **give you answers**.
This MCP **asks you questions** instead.

Like Socrates, it guides you to discover insights through structured questioning - using **78+ proven methodologies** from business strategy, creative thinking, and critical analysis.

## ✨ What Makes This Different

| Traditional AI | Socratic Thinking MCP |
|---------------|---------------------|
| ✅ Gives instant answers | ❓ Asks guiding questions |
| 🤖 AI does the thinking | 🧠 You do the thinking |
| 📝 Provides conclusions | 🎯 Helps you reach conclusions |
| ⚡ Fast but shallow | 🔍 Slower but deeper |

## 🎯 Core Philosophy

**"I cannot teach anybody anything. I can only make them think." - Socrates**

This MCP implements 78+ structured thinking methodologies as **question frameworks**:

- **Strategic Decision-Making** (30 methods): Decision Tree, SWOT, BCG Matrix, Business Model Canvas, Lean Canvas, Stakeholder Mapping...
- **Creative Problem-Solving** (30 methods): SCAMPER, Question Storming, TRIZ, Design Thinking, Jobs To Be Done, Liberating Structures...
- **Critical Thinking** (18 methods): 5 Whys, Cynefin Framework, Socratic Questioning, Systems Thinking, Theory of Constraints...

## 📚 Knowledge Base (RAG-Ready)

**[20 Advanced Methodology Files](knowledge/)** - Detailed methodologies with:
- Category classification
- Question sequences
- Academic sources
- Best practices
- Expected outcomes

Perfect for RAG (Retrieval-Augmented Generation) integration!

## 🚀 Quick Start

### Installation

1. **Install dependencies**:
```bash
cd socratic-thinking-mcp
pip install -r requirements.txt
```

2. **Add to Claude Desktop config** (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "socratic-thinking": {
      "command": "python",
      "args": ["-m", "src.server"],
      "cwd": "C:\\\\Users\\\\YourName\\\\Documents\\\\socratic-thinking-mcp",
      "env": {
        "PYTHONPATH": "C:\\\\Users\\\\YourName\\\\Documents\\\\socratic-thinking-mcp"
      }
    }
  }
}
```

3. **Restart Claude Desktop**

### Usage

Just ask Claude naturally - the MCP activates automatically:

```
You: "Should I pursue an MBA or start a business?"

Claude: [Activates Socratic Thinking MCP]

🎯 Problem analyzed
Category: Strategic decision-making

📋 Recommended methodologies:
1. DECISION TREE - Complex decisions (5 steps)
2. REGRET MINIMIZATION - Life decisions (3 steps)
3. LEAN CANVAS - Business model validation (9 steps)

Which method? (1/2/3)

You: 1

[Method: DECISION TREE - STRATEGIC]
Question 1/5: What is the core decision you need to make?

You: Whether MBA or entrepreneurship is better for my career

[Method: DECISION TREE - STRATEGIC]
Question 2/5: What are your options? (at least 2)

...
```

### Trigger Keywords

The MCP activates when you use:
- **English**: "thinking tools", "Socratic method", "help me think", "guide my thinking"
- **Korean**: "씽킹툴", "소크라테스", "생각 정리", "사고 도구"
- **Context**: Decision-making, strategy, brainstorming, problem-solving

## 📚 78+ Methodologies

### 🎯 Strategic & Decision-Making (30)

**Business Strategy (8 core + 3 advanced)**:
- SWOT Analysis, BCG Matrix, Porter's Five Forces
- PESTEL, Ansoff Matrix, Blue Ocean Strategy
- Value Chain Analysis, OKR
- **+ Business Model Canvas, Value Proposition Canvas, Lean Canvas** *(knowledge/)*

**Decision-Making (7 core + 3 advanced)**:
- Decision Tree, Decision Matrix, Cost-Benefit Analysis
- Pros-Cons-Fixes, Regret Minimization, Opportunity Cost
- Eisenhower Matrix
- **+ Impact-Effort Matrix, Critical Success Factors, Balanced Scorecard** *(knowledge/)*

**Risk & Scenarios (3)**:
- Pre-Mortem, Scenario Planning, Second-Order Thinking

**Systems & Analysis (4 + 2 advanced)**:
- Systems Thinking, Mental Models Check, Inversion, Fishbone
- **+ Stakeholder Mapping, Appreciative Inquiry** *(knowledge/)*

### 🧠 Critical & Systems Thinking (18)

**Root Cause (3)**:
- 5 Whys, Phoenix Checklist, Force-Field Analysis

**Perspective (2 + 1 advanced)**:
- Six Thinking Hats, Lateral Thinking
- **+ Socratic Questioning (6 types)** *(knowledge/)*

**Analysis (7 + 5 advanced)**:
- Attribute Listing, Morphological Analysis, Fractionation
- Mind Mapping, Reversal, Lotus Blossom, Future Scenarios
- **+ Kipling Method (5W1H), Assumption Testing, Cynefin Framework**
- **+ Theory of Constraints, Causal Loop Diagrams** *(knowledge/)*

### 🎨 Creative & Innovation (30)

**Linear Creative (3 + 1 advanced)**:
- SCAMPER, Design Thinking, TRIZ
- **+ TRIZ Contradiction Matrix** *(knowledge/)*

**Intuitive (6 + 3 advanced)**:
- Random Stimulation, Analogies, Fantasy Questions
- Paradox, Forced Connection, Dreamscape
- **+ Question Storming, Jobs To Be Done, Thought Experiments** *(knowledge/)*

**Perspective Shift (10 + 2 advanced)**:
- Intuition, Three B's, Relaxation, Talk to Stranger
- Pattern Language, Drawing, Hypnagogic Imagery
- Guided Imagery, Psychosynthesis, Hieroglyphics
- **+ Liberating Structures (1-2-4-All), Worst Possible Idea** *(knowledge/)*

**Feedback (2)**:
- Murder Board, Brainstorming

**Additional (3)**:
- Circle of Opportunity, Idea Grid, Airline Method

## 🎬 Real-World Examples

### Example 1: Career Decision
```
User: "Should I do a Babson DBA in Entrepreneurship?"

MCP recommends: Decision Tree, Regret Minimization, Cost-Benefit
User selects: Decision Tree

Q1: What's the core decision?
A1: Whether Babson DBA adds value to my career

Q2: What are your options?
A2: 1) Do DBA now, 2) Wait 2 years, 3) Do executive program instead

Q3: Expected outcomes?
A3: DBA = deep research skills + network ($120K, 4 years)
    Executive = quick network ($15K, 2 weeks)

Q4: Probability and value?
A4: Success 80% but opportunity cost is high (already have EdD + 2 PhDs in progress)

Q5: Best choice and why?
A5: Executive program - achieves 70% of goal in 5% of time/cost
```

### Example 2: Product Innovation
```
User: "How can we improve our mobile app?"

MCP recommends: SCAMPER, Question Storming, Jobs To Be Done
User selects: Question Storming

Q1: WHAT IS? - What's the current situation?
A1: Users drop off after 3 days, engagement is low

Q2: WHAT CAUSED? - Root factors?
A2: Onboarding is confusing, value prop unclear

Q3: WHAT IF? - No constraints?
A3: Personalized AI coach for each user

... (7 total questions)

Final insight: 50+ questions reframing the problem from multiple angles
```

## 🏗️ Architecture

```
socratic-thinking-mcp/
├── src/
│   ├── server.py              # MCP server (tool registration)
│   ├── classifier.py          # Problem categorization
│   ├── question_engine.py     # Question generation
│   ├── session.py             # Conversation state management
│   └── methods/
│       └── templates.py       # 58 core methodology templates
├── knowledge/                 # 20 advanced methodologies (RAG-ready)
│   ├── README.md
│   ├── 01-Question-Storming.md
│   ├── 02-Kipling-Method.md
│   └── ... (18 more)
├── data/
│   └── user_sessions/         # Session storage (compressed JSON)
├── README.md                  # This file
└── requirements.txt           # Python dependencies
```

## 🎯 Design Principles

1. **Token Efficiency** - Compressed templates, one question at a time (97% token reduction)
2. **Submarine Mode** - Silent until triggered, no token waste
3. **Methodology Transparency** - Always shows which method is being used
4. **Progressive Disclosure** - Questions revealed step-by-step
5. **User Agency** - User chooses methodology, not imposed
6. **RAG-Ready** - Knowledge base optimized for retrieval

## 📊 Comparison with Other Tools

| Feature | Socratic Thinking MCP | Sequential Thinking | ChatGPT |
|---------|---------------------|-------------------|---------| 
| Question-based | ✅ 78+ structured frameworks | ✅ General reasoning | ❌ Answer-based |
| Business Strategy | ✅ SWOT, BCG, Porter, Canvas | ❌ | ⚠️ Limited |
| Decision Trees | ✅ Structured 5-step | ❌ | ⚠️ Ad-hoc |
| Creative Thinking | ✅ SCAMPER, TRIZ, Question Storming | ❌ | ⚠️ General |
| Methodology Choice | ✅ User selects | ❌ AI-driven | ❌ N/A |
| Token Efficiency | ✅ 97% compressed | ⚠️ Medium | ❌ Verbose |
| RAG Integration | ✅ 20 knowledge files | ❌ | ❌ |

## 🔗 Related Projects

- **[Socratic Thinking GPT](https://github.com/seanshin0214/socratic-thinking-gpt)** - ChatGPT GPT version (no coding required)
- **[QualAI MCP](https://github.com/seanshin0214/qualai-mcp)** - Qualitative research analysis

## 🤝 Contributing

We welcome contributions! Areas of interest:
- Additional methodologies (please include academic/practitioner sources)
- Improved question templates
- Multi-language support
- RAG optimization

## 📖 Academic Background

This MCP implements methodologies from:
- **Business Strategy**: Porter (1979), Ansoff (1957), Henderson (BCG, 1970), Osterwalder (Business Model Canvas, 2010)
- **Creative Thinking**: Osborn (SCAMPER, 1953), de Bono (Lateral Thinking, 1967), Michalko (ThinkerToys, 1991), Gregersen (Question Storming, 2018)
- **Critical Thinking**: Altshuller (TRIZ, 1946), Senge (Systems Thinking, 1990), Snowden (Cynefin, 1999)
- **Decision Science**: Kahneman & Tversky (Biases, 1974), Bezos (Regret Minimization, 1994), Maurya (Lean Canvas, 2012)

## 📝 License

MIT License

## 🙏 Acknowledgments

- Michael Michalko - *ThinkerToys* (Creative methodologies)
- Edward de Bono - *Six Thinking Hats*, *Lateral Thinking*
- Genrich Altshuller - TRIZ methodology
- Hal Gregersen - Question Storming (Harvard)
- Clayton Christensen - Jobs To Be Done
- Alex Osterwalder - Business Model Canvas
- Dave Snowden - Cynefin Framework
- Jeff Bezos - Regret Minimization Framework
- Model Context Protocol team at Anthropic

---

**Built with ❤️ for deeper thinking**

*"The unexamined life is not worth living." - Socrates*
