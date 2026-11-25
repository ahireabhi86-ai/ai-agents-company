# 🤖 AI Agents Team Company

A virtual company of Claude-powered agents that creates digital products.

| Agent | Role |
|-------|------|
| Rita | Researcher: finds trending topics via web search |
| Dev-Ana | Designer: UX, branding, design spec |
| Dan | Developer: feasibility + builds the MVP |
| Eva | Executive: decides what ships |
| Mia | Marketer: positioning, pricing, launch kit |
| Quinn | QA Reviewer: finds bugs, gives SHIP / FIX FIRST verdict |

## Workflow
Research → Debate (Designer, Developer, Marketer, Researcher) → Executive decision → Design spec → Build → QA review → Fixes → Launch kit

## Setup
```bash
git clone https://github.com/YOUR_USERNAME/ai-agents-company.git
cd ai-agents-company
pip install -r requirements.txt
cp .env.example .env   # add your Anthropic API key
python main.py "AI productivity tools"
```
Results are saved in `outputs/<timestamp>/`.

## Customize
Edit prompts in `agents/team.py`, add agents (support, legal, finance), or change `DEBATE_ROUNDS` in `main.py`.
