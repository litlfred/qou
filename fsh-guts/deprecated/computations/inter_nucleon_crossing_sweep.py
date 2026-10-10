#!/usr/bin/env python3
"""
Sweep inter-nucleon crossings_per_pair to find the ILP-stable count.

For each candidate m ∈ {1, 2, ..., 12}:
  1. Compute exact tower binding for D, T, 3He, 4He, 12C, 16O, 20Ne.
  2. Report ratio B_pred / B_AME and overall fit metric.

The CORRECT inter-nucleon crossing count m is the one where:
  - Binding scales correctly across A
  - The fit metric (mean abs ratio - 1) is minimised

Per the proton derivation in mass-endomorphism-tower.md, the gluon
count (2 crossings) is the unique integer optimum closing the
Frobenius positivity LP.  We're testing whether the inter-nucleon
analog has a similar unique integer count.
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from pyhecke.gram import atom_per_generator_volumes
from mass_endomorphism import (
    q0, mass_from_tower, additive_wedderburn_volumes, proton_cross,
)

_proton_vols = additive_wedderburn_volumes(3, proton_cross)
_, _, _, M_PROTON_TOWER = mass_from_tower(_proton_vols)
E_0_TOWER_MEV = 938.272 / M_PROTON_TOWER


def binding(Z, N, m):
    vols_atom = atom_per_generator_volumes(Z, N, include_inter=True,
                                           crossings_per_pair=m)
    vols_free = atom_per_generator_volumes(Z, N, include_inter=False)
    if not vols_atom:
        return None
    _, _, _, m_atom = mass_from_tower(vols_atom)
    _, _, _, m_free = mass_from_tower(vols_free)
    return E_0_TOWER_MEV * (m_free - m_atom)


ATOMS = [
    ("D",    1,  1,   2.22),
    ("T",    1,  2,   8.48),
    ("3He",  2,  1,   7.72),
    ("4He",  2,  2,  28.30),
    ("6Li",  3,  3,  32.00),
    ("12C",  6,  6,  92.16),
    ("16O",  8,  8, 127.62),
    ("20Ne", 10, 10, 160.65),
]

print("INTER-NUCLEON CROSSING COUNT SWEEP")
print("=" * 88)
print(f"E_0_tower = {E_0_TOWER_MEV:.4e} MeV/cat.unit")
print()
header = f"  {'m':>3}"
for atom, _, _, _ in ATOMS:
    header += f" {atom:>8}"
header += f" {'fit':>10}"
print(header)
header2 = f"  {'  ':>3}"
for _, _, _, B_AME in ATOMS:
    header2 += f" {B_AME:>8.2f}"
header2 += f" {'AME':>10}"
print(header2)
print("  " + "-" * 80)

results = []
for m in range(1, 13):
    row = f"  {m:>3}"
    ratios = []
    row_data = {"crossings_per_pair": m, "atoms": []}
    for atom, Z, N, B_AME in ATOMS:
        try:
            B = binding(Z, N, m)
            if B is None or B_AME <= 0:
                row += f" {'—':>8}"
                continue
            ratio = B / B_AME
            ratios.append(ratio)
            row += f" {ratio:>8.3f}"
            row_data["atoms"].append({"atom": atom, "B_pred": B,
                                       "B_AME": B_AME, "ratio": ratio})
        except Exception as e:
            row += f" {'ERR':>8}"
    # Filter out negative ratios (atom heavier than free → wrong sign)
    pos_ratios = [r for r in ratios if r > 0]
    if pos_ratios and len(pos_ratios) == len(ratios):
        # Geometric mean of |log(ratio)| as fit metric
        fit = math.exp(sum(abs(math.log(r)) for r in pos_ratios)
                       / len(pos_ratios))
        row += f" {fit:>10.4f}"
        row_data["fit_metric"] = fit
    else:
        n_neg = len(ratios) - len(pos_ratios)
        row += f"  WRONG-SIGN×{n_neg}"
        row_data["fit_metric"] = None
        row_data["wrong_sign_count"] = n_neg
    print(row)
    results.append(row_data)

print()
print("Best fit (minimum fit metric among rows without wrong-sign):")
valid = [r for r in results if r.get("fit_metric") is not None]
if valid:
    best = min(valid, key=lambda r: r["fit_metric"])
    print(f"  m = {best['crossings_per_pair']}, fit = {best['fit_metric']:.4f}")
else:
    best = {"crossings_per_pair": None, "fit_metric": None}
    print(f"  All m have wrong-sign atoms — no positive-binding regime found.")

# Save witness
witness = {
    "computation": "inter-nucleon-crossing-sweep",
    "description": (
        "Sweep crossings_per_pair m in {1..12} for inter-nucleon coupling. "
        "Reports B_pred/B_AME for D-20Ne. "
        "Fit metric = geometric mean of exp(|log(ratio)|), minimum at "
        "categorically-correct m."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "parameters": {"q": q0, "E_0_tower_MeV": E_0_TOWER_MEV},
    "sweep": results,
    "best_m": best["crossings_per_pair"],
    "best_fit": best.get("fit_metric"),
}
out = Path(__file__).parent / "inter-nucleon-crossing-sweep.witness.json"
out.write_text(json.dumps(witness, indent=2, default=str))
print(f"\nWitness: {out}")
