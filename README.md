# 🤔 Socratic Thinking MCP

> **AI that asks, not answers** | 질문하는 AI, 소크라테스처럼

[![MCP](https://img.shields.io/badge/MCP-Model_Context_Protocol-blue)](https://modelcontextprotocol.io)
[![Python](https://img.shields.io/badge/Python-3.10+-green)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 💡 Why This Exists

Most AI tools **give you answers**.
This MCP **asks you questions** instead.

Like Socrates, it guides you to discover insights through structured questioning - using 58 proven methodologies from business strategy, creative thinking, and critical analysis.

## ✨ What Makes This Different

| Traditional AI | Socratic Thinking MCP |
|---------------|---------------------|
| ✅ Gives instant answers | ❓ Asks guiding questions |
| 🤖 AI does the thinking | 🧠 You do the thinking |
| 📝 Provides conclusions | 🎯 Helps you reach conclusions |
| ⚡ Fast but shallow | 🔍 Slower but deeper |

## 🎯 Core Philosophy

**"I cannot teach anybody anything. I can only make them think." - Socrates**

This MCP implements 58 structured thinking methodologies as **question frameworks**:

- **Strategic Decision-Making** (22 methods): Decision Tree, SWOT, BCG Matrix, Porter's Five Forces, Cost-Benefit, Pre-Mortem, Scenario Planning...
- **Creative Problem-Solving** (24 methods): SCAMPER, 5 Whys, Six Thinking Hats, TRIZ, Design Thinking...
- **Critical Thinking** (12 methods): Mental Models Check, Systems Thinking, Second-Order Thinking, Fishbone, Inversion...

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
      "cwd": "C:\\Users\\YourName\\Documents\\socratic-thinking-mcp",
      "env": {
        "PYTHONPATH": "C:\\Users\\YourName\\Documents\\socratic-thinking-mcp"
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
3. COST-BENEFIT ANALYSIS - Investment decisions (4 steps)

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

## 📚 58 Methodologies

### 🎯 Strategic & Decision-Making (22)

**Business Strategy**:
- SWOT Analysis - Strengths/Weaknesses/Opportunities/Threats
- BCG Matrix - Portfolio analysis (Star/Cash Cow/Question Mark/Dog)
- Porter's Five Forces - Industry competition analysis
- PESTEL - Macro environment (Political/Economic/Social/Tech/Environmental/Legal)
- Ansoff Matrix - Growth strategies
- Blue Ocean Strategy - Create uncontested market space
- Value Chain Analysis - Competitive advantage identification
- OKR - Objectives & Key Results

**Decision-Making**:
- Decision Tree - Complex decision mapping
- Decision Matrix - Weighted scoring
- Cost-Benefit Analysis - Investment evaluation
- Pros-Cons-Fixes - Enhanced pros/cons with solutions
- Regret Minimization (Jeff Bezos) - Long-term life decisions
- Opportunity Cost - Resource allocation optimization
- Eisenhower Matrix - Prioritization (Urgent-Important)

**Risk & Scenarios**:
- Pre-Mortem - Prospective hindsight for risk prevention
- Scenario Planning - Best/Worst/Most Likely futures
- Second-Order Thinking - Long-term consequences

### 🧠 Critical & Systems Thinking (12)

**Causal Analysis**:
- 5 Whys - Root cause analysis
- Fishbone Diagram (Ishikawa) - Man/Method/Machine/Material
- Systems Thinking - Causal loops and leverage points

**Cognitive Debiasing**:
- Mental Models Check - Overcome confirmation bias, sunk cost, availability bias
- Inversion - Backwards thinking to avoid failure

**Analytical**:
- Phoenix Checklist - Comprehensive problem examination
- Force-Field Analysis (Tug-of-War) - Driving vs restraining forces

### 🎨 Creative & Innovation (24)

**Linear Creative Tools**:
- SCAMPER - Substitute/Combine/Adapt/Modify/Put to other use/Eliminate/Reverse
- Attribute Listing (Slice & Dice) - Break down and recombine
- Morphological Analysis (Idea Box) - Systematic combinations
- Mind Mapping - Visual connections
- Lotus Blossom - Idea expansion

**Intuitive Tools**:
- Random Stimulation (BruteThink) - Random word associations
- Analogies - Cross-domain thinking
- Fantasy Questions (Stone Soup) - "What if" scenarios
- Dreamscape - Dream analysis for insights

**Perspective Shifts**:
- Six Thinking Hats - White/Red/Black/Yellow/Green/Blue perspectives
- TRIZ - Inventive problem-solving (40 principles)
- Design Thinking - Empathize/Define/Ideate/Prototype/Test
- Lateral Thinking - Break patterns

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

MCP recommends: SCAMPER, Design Thinking, Value Chain
User selects: SCAMPER

Q1: SUBSTITUTE - What can be replaced?
A1: Replace manual input with AI auto-fill

Q2: COMBINE - What can be merged?
A2: Combine calendar + task manager

Q3: ADAPT - What can be adapted from elsewhere?
A3: Gaming mechanics for engagement (from Duolingo)

... (7 total questions)

Final insight: 15 concrete improvement ideas across 7 dimensions
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
│       └── templates.py       # 58 methodology templates
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

## 📊 Comparison with Other Tools

| Feature | Socratic Thinking MCP | Sequential Thinking | ChatGPT |
|---------|---------------------|-------------------|---------|
| Question-based | ✅ 58 structured frameworks | ✅ General reasoning | ❌ Answer-based |
| Business Strategy | ✅ SWOT, BCG, Porter, etc. | ❌ | ⚠️ Limited |
| Decision Trees | ✅ Structured 5-step | ❌ | ⚠️ Ad-hoc |
| Creative Thinking | ✅ SCAMPER, TRIZ, etc. | ❌ | ⚠️ General |
| Methodology Choice | ✅ User selects | ❌ AI-driven | ❌ N/A |
| Token Efficiency | ✅ 97% compressed | ⚠️ Medium | ❌ Verbose |

## 🤝 Contributing

We welcome contributions! Areas of interest:
- Additional methodologies (please include academic/practitioner sources)
- Improved question templates
- Multi-language support

## 📖 Academic Background

This MCP implements methodologies from:
- **Business Strategy**: Porter (1979), Ansoff (1957), Henderson (BCG, 1970)
- **Creative Thinking**: Osborn (SCAMPER, 1953), de Bono (Lateral Thinking, 1967), Michalko (ThinkerToys, 1991)
- **Critical Thinking**: Altshuller (TRIZ, 1946), Senge (Systems Thinking, 1990)
- **Decision Science**: Kahneman & Tversky (Biases, 1974), Bezos (Regret Minimization, 1994)

## 📝 License

MIT License

## 🙏 Acknowledgments

- Michael Michalko - *ThinkerToys* (Creative methodologies)
- Edward de Bono - *Six Thinking Hats*, *Lateral Thinking*
- Genrich Altshuller - TRIZ methodology
- Jeff Bezos - Regret Minimization Framework
- Model Context Protocol team at Anthropic

---

**Built with ❤️ for deeper thinking**

*"The unexamined life is not worth living." - Socrates*
