# Entry for make-the-ai-judge-feel-brave-20261121-0302:
# one still scene, left to do its own quiet work.
from pathlib import Path

ENTRY = (
    "The kettle clicked off a minute ago. Steam still rises from the cup, "
    "slow in the window light. Nothing is being asked of anyone yet. "
    "The chair, the table, the quiet room — all of it holds, steady, "
    "ready for whatever comes next."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
