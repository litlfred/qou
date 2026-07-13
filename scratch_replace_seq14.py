import sys

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-surreals-archimedean_seq1.md", "r") as f:
    text = f.read()

replacements = [
    (
        "## Conjecture\n\nThe birthday trajectory discriminates algebraic from transcendental:",
        "## Conjecture\n\n**Conjecture (Algebraic-transcendental discrimination via birthday trajectory).**\nThe birthday trajectory discriminates algebraic from transcendental numbers:"
    )
]

for orig, new in replacements:
    if orig not in text:
        print(f"FAILED: {orig[:100]}")
    text = text.replace(orig, new)

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-surreals-archimedean_seq1.md", "w") as f:
    f.write(text)

