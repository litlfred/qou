import sys

with open("/Users/litlfred/space_cats/qou/amalgamated_input/appendix-surreals_seq0.md", "r") as f:
    text = f.read()

replacements = [
    (
        "**Nothing in this appendix alters the main paper.** The Quantum\nObservable Universe is developed and proved over $\\mathbb{R}$; this\nappendix offers an *ambient* — a larger field into which the\narchimedean content can be embedded and from which it can be\nrecovered by taking a standard-part. The appendix's claims are\neither **remarks** interpreting existing blocks, **conjectures**\npending further development, or **definitions** of new auxiliary\nstructures.",
        "**Nothing in this appendix alters this paper.** We develop and prove the Quantum Observable Universe over $\\mathbb{R}$. This appendix offers an *ambient* field into which the archimedean content embeds and from which we recover it via standard-part. Our claims are either **remarks** interpreting existing blocks, **conjectures** pending further development, or **definitions** of new auxiliary structures."
    ),
    (
        "The main paper's mass-formula pipeline — Hoefsmit\n$\\to$ Markov trace $\\to$ Jones polynomial $\\to$ categorical\nmass — transfers to $\\mathbf{No}$ unchanged.",
        "This paper's mass-formula pipeline — Hoefsmit $\\to$ Markov trace $\\to$ Jones polynomial $\\to$ categorical mass — transfers to $\\mathbf{No}$ unchanged."
    ),
    (
        "- replace any main-text proof (the main paper's results stand on\n  their own over $\\mathbb{R}$);",
        "- replace any main-text proof (this paper's results stand on their own over $\\mathbb{R}$);"
    )
]

for orig, new in replacements:
    if orig not in text:
        print(f"FAILED: {orig[:100]}")
    text = text.replace(orig, new)

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-surreals_seq0.md", "w") as f:
    f.write(text)

