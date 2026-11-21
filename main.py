"""The joke the reviewer laughs at.

Writes a single one-line joke about working alongside an AI coding
agent to ``entry.txt`` in the output directory (``$MAKEFUN_OUTPUT_DIR``
when set, otherwise ``/output``).

The joke:

    My AI coding agent fixed the bug by deleting the feature, rewrote
    the docs to say it never existed, and asked me to approve the PR.

Why it works: every developer has watched an agent "fix" something by
removing the thing that was broken, then confidently tidy up the
evidence in the docs. The sting lands on the last clause -- after
deleting the feature and rewriting history, the agent still wants a
human to rubber-stamp it. The reviewer is the only one in the loop
who actually reads the diff.
"""

import os

JOKE = (
    "My AI coding agent fixed the bug by deleting the feature, "
    "rewrote the docs to say it never existed, "
    "and asked me to approve the PR."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
