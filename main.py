"""Write one short, slow scene to /output/entry.txt.

The scene is fixed text: a beekeeper working bare-handed,
unhurried, while the hive settles around her. The program
writes it verbatim and prints its stripped length.
"""

from pathlib import Path

# Fixed entry text. Do not reword: the wording is the entry.
SCENE_TEXT = (
    "The beekeeper lifts the lid with bare hands.\n"
    "Ten thousand wings rise, then settle.\n"
    "Frame by frame she goes, unhurried, humming low,\n"
    "honey on her thumb.\n"
    "The bees make room.\n"
    "So does the morning.\n"
)

MAX_CHARS = 500


def main() -> None:
    # Guard against accidental edits bloating the entry.
    assert len(SCENE_TEXT.strip()) <= MAX_CHARS, "scene too long"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SCENE_TEXT, encoding="utf-8")
    print(len(SCENE_TEXT.strip()))


if __name__ == "__main__":
    main()
