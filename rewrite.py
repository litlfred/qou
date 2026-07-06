import re

with open("content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas.md", "r") as f:
    text = f.read()

# 1. Update intro text
text = text.replace("Each entry occupies **two rows**: the first gives the braid word\nin normal form (NF, shortlex Gröbner–Shirshov); the second gives\nthe prediction and AME residual.", "Each entry provides the canonical braid word\nin normal form (NF, shortlex Gröbner–Shirshov) and its Markov closure topology.")

text = text.replace("Each entry occupies **two rows**: the first gives the braid word\nin normal form (NF, shortlex Gröbner–Shirshov); the second gives\nthe prediction and AME residual.", "Each entry provides the canonical braid word\nin normal form (NF, shortlex Gröbner–Shirshov) and its Markov closure topology.")

# Replace Methodology table
old_table_start = text.find("| Tag | Definition | Examples |")
old_table_end = text.find("The principled pipeline computes", old_table_start)

new_table = """| Tag | Definition | Examples |
|---|---|---|
| `principled-derivation` | Knot is the closure of an explicit $\\sigma$-braid word in $H_{n_0}(q_0)$ from [`def:confined-particle`](#def:confined-particle). | electron $\\sigma_1^3 \\to 3_1$, proton/neutron $(\\sigma_1 \\sigma_2^{-1})^3 \\to \\mathcal{B}_3$. |
| `principled-gb-nf` | Trivial-NF entries: a single strand (unknot $0_1$) or the pure identity $\\mathbf{1}$. | neutrino ($0_1$), quark; the bare photon. |

"""

text = text[:old_table_start] + new_table + text[old_table_end:]

# Strip Prediction rows
text = re.sub(r'\|\s*Prediction\s*\|.*?\|\n', '', text)

with open("content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas.md", "w") as f:
    f.write(text)
