"""AI Agents Team Company:
research -> debate -> executive decision -> design -> build -> QA -> fix -> marketing."""
import sys, datetime, pathlib
from agents.team import researcher, designer, developer, executive, marketer, qa

DEBATE_ROUNDS = 2
DEBATERS = (designer, developer, marketer, researcher)


def save(out, name, text):
    (out / name).write_text(text)


def main(niche: str = "AI and technology"):
    out = pathlib.Path("outputs") / datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out.mkdir(parents=True, exist_ok=True)

    # 1. Research
    research = researcher.run(f"Find trending topics now in: {niche}. Suggest digital product ideas.")
    save(out, "1_research.md", research)

    # 2. Debate
    transcript = f"RESEARCH:\n{research}\n"
    for r in range(1, DEBATE_ROUNDS + 1):
        for agent in DEBATERS:
            reply = agent.run(
                f"Debate round {r}. Decide which idea is best to build.\n\n{transcript}\n"
                f"Give your view as {agent.role}. Respond to others' points.",
                max_tokens=700,
            )
            transcript += f"\n[{agent.role} R{r}]: {reply}\n"
    save(out, "2_debate.md", transcript)

    # 3. Executive decision
    decision = executive.run(f"Research and debate:\n\n{transcript}\n\nMake the final decision.")
    save(out, "3_decision.md", decision)

    # 4. Design + build
    design_spec = designer.run(f"Create a design spec (colors, fonts, layout, copy) for:\n{decision}")
    save(out, "4_design_spec.md", design_spec)
    build = developer.run(
        f"Build the MVP.\n\nDECISION:\n{decision}\n\nDESIGN:\n{design_spec}", max_tokens=4000
    )
    save(out, "5_build.md", build)

    # 5. QA review + developer fixes
    review = qa.run(f"Review this build:\n\n{build}", max_tokens=1500)
    save(out, "6_qa_review.md", review)
    fixed = developer.run(
        f"Fix the issues from QA and output the final complete files.\n\nBUILD:\n{build}\n\nQA:\n{review}",
        max_tokens=4000,
    )
    save(out, "7_final_build.md", fixed)

    # 6. Marketing
    launch = marketer.run(f"Write the launch kit for this product:\n{decision}", max_tokens=2000)
    save(out, "8_launch_kit.md", launch)

    print(f"\nDone. Results saved in {out}/")


if __name__ == "__main__":
    main(" ".join(sys.argv[1:]) or "AI and technology")
