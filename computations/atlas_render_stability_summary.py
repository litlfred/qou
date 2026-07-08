import re
import json
import glob
from pathlib import Path

ATLAS_MD = Path("content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas.md")

with open(ATLAS_MD) as f:
    text = f.read()

begin_marker = "<!-- AUTO:stability-summary BEGIN -->"
end_marker = "<!-- AUTO:stability-summary END -->"

if begin_marker not in text or end_marker not in text:
    print("Markers not found")
    exit(1)

pre, rest = text.split(begin_marker)
table_text, post = rest.split(end_marker)

# Extract existing data: Z, N -> Element, N_pred, Delta, k_alpha, annotations
metadata = {}
lines = table_text.strip().split("\n")
for line in lines:
    if line.startswith("| ") and " | " in line and not line.startswith("|---"):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) > 10 and parts[1].isdigit():
            z = int(parts[3])
            n = int(parts[4])
            element = parts[2]
            n_pred = parts[5]
            delta = parts[6]
            k_alpha = parts[7]
            metadata[z] = {
                "element": element,
                "n": n,
                "n_pred": n_pred,
                "delta": delta,
                "k_alpha": k_alpha
            }

# Load witnesses for M_pred, M_AME, B/A
witnesses = {}
for file in glob.glob("computations/canonical-isotope-witness-Z*.witness.json"):
    with open(file) as f:
        data = json.load(f)
        for row in data['data']['rows']:
            if row.get("composite_mass") and row["composite_mass"].get("M_pred_MeV") is not None:
                witnesses[(row["Z"], row["N"])] = row

new_table = [
    r"| $\#$ | Element | $Z$ | $N$ | $N_{\mathrm{pred}}$ | $\Delta$ | $k_\alpha$ | $M_q$ (MeV) | $M_o$ (MeV) | $B/A$ |",
    "|---:|------|---:|---:|---:|---:|---:|---:|---:|---:|"
]

for z in sorted(metadata.keys()):
    meta = metadata[z]
    n = meta["n"]
    if (z, n) in witnesses:
        row = witnesses[(z, n)]
        comp = row["composite_mass"]
        m_pred = comp["M_pred_MeV"]
        m_ame = comp["M_AME_MeV"]
        # calculate B/A
        if z == 1 and n == 0:
            b_over_a = 0.0
        else:
            b_over_a = row["reference_MeV_50dps"] / row["A"] if isinstance(row.get("reference_MeV_50dps"), (int, float)) else 0.0
        
        m_pred_str = f"${m_pred:.4f}$"
        m_ame_str = f"${m_ame:.4f}$"
        b_a_str = f"${b_over_a:.4f}$"
    else:
        m_pred_str = "—"
        m_ame_str = "—"
        b_a_str = "—"

    new_table.append(f"| {z} | {meta['element']} | {z} | {n} | {meta['n_pred']} | {meta['delta']} | {meta['k_alpha']} | {m_pred_str} | {m_ame_str} | {b_a_str} |")

new_table_str = "\n" + "\n".join(new_table) + "\n"
new_text = pre + begin_marker + new_table_str + end_marker + post

with open(ATLAS_MD, "w") as f:
    f.write(new_text)

print("Updated table via python")
