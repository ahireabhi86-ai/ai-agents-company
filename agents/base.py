import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()
MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")


class Agent:
    def __init__(self, name: str, role: str, system: str, use_search: bool = False):
        self.name, self.role, self.system, self.use_search = name, role, system, use_search

    def run(self, prompt: str, max_tokens: int = 2000) -> str:
        kwargs = dict(
            model=MODEL,
            max_tokens=max_tokens,
            system=self.system,
            messages=[{"role": "user", "content": prompt}],
        )
        if self.use_search:
            kwargs["tools"] = [{"type": "web_search_20250305", "name": "web_search"}]
        resp = client.messages.create(**kwargs)
        text = "\n".join(b.text for b in resp.content if b.type == "text")
        print(f"\n=== {self.name} ({self.role}) ===\n{text}\n")
        return text
