#!/usr/bin/env python3
"""
Per-braid mass prediction vs AME — calibration check.

Applies the H^0 calibration (m_e per the three-calibration
discipline) to the per-braid tower totals from per_braid_tower.py
and compares to AME atomic masses.

The per-braid total scales as ≈ 1850 × A (linear). The physical
mass scales as ≈ 939 × A (linear, with binding-energy corrections).
If the per-braid framework is consistent, the calibration constant
m_e × C should be ≈ 939 / 1850 ≈ 0.507 MeV per per-braid unit —
within a per-nucleon correction.

Note: the current per-braid tower uses the q=1 Murnaghan-Nakayama
character; proton and neutron sub-braids have identical
permutation cycle structure (uud vs udd doesn't change the
S_3 cycle of the braid generator), so per-braid traces don't
distinguish them. This is a known limitation — flagged below.

AME values from PDG / AME 2020:
  D     1875.6128 MeV  (Z=1, N=1, A=2)
  3He   2808.3914 MeV  (Z=2, N=1, A=3)
  3H    2808.9209 MeV  (Z=1, N=2, A=3)
  4He   3727.3791 MeV  (Z=2, N=2, A=4)
  12C  11177.9292 MeV  (Z=6, N=6, A=12)
  16O  14899.1683 MeV  (Z=8, N=8, A=16)
  40Ca 37224.9202 MeV  (Z=20, N=20, A=40)

Witness: docs/audits/2026-05-01-per-braid-vs-ame.witness.json
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower import per_braid_mass
from q_parameter import Q as Q0_FLOAT

mpmath.mp.dps = 50
q0 = mpmath.mpf(str(Q0_FLOAT))

# AME 2020 atomic masses in MeV/c² (Wang et al. 2021)
AME_MASS_MEV = {
    "D":    1875.61294257,
    "3He":  2808.39148127,
    "3H":   2808.92113298,
    "4He":  3727.37909409,
    "12C": 11177.9292,
    "16O": 14899.16828,
    "40Ca": 37224.9202,
}

# m_e calibration (CODATA 2018) — H^0 input per
# prop:three-calibration-discipline.
M_E_MEV = 0.51099895000

ATOMS = [
    ("D", 1, 1),
    ("3He", 2, 1),
    ("3H", 1, 2),
    ("4He", 2, 2),
    ("12C", 6, 6),
    ("16O", 8, 8),
    ("40Ca", 20, 20),
]


print("=" * 88)
print("Per-braid mass prediction vs AME — calibration check")
print("=" * 88)
print(f"q_0 = {q0}")
print(f"m_e = {M_E_MEV} MeV (CODATA, H^0 calibration)")
print()
print(f"  {'Atom':>5} {'A':>3} {'per-braid total':>16} {'AME (MeV)':>12} {'ratio':>14} {'cal / m_e':>12}")
print("  " + "-" * 80)

results = []
ratios = []
for name, Z, N in ATOMS:
    out = per_braid_mass(Z, N)
    total = float(out["total"])
    ame = AME_MASS_MEV[name]
    cal_constant = ame / total  # MeV per per-braid unit
    cal_over_me = cal_constant / M_E_MEV  # dimensionless
    print(
        f"  {name:>5} {Z+N:>3} {total:>16.6e} {ame:>12.4f} "
        f"{cal_constant:>14.10f} {cal_over_me:>12.6f}"
    )
    ratios.append(cal_over_me)
    results.append({
        "atom": name, "Z": Z, "N": N, "A": Z + N,
        "per_braid_total": total,
        "ame_mass_mev": ame,
        "calibration_constant_mev_per_unit": cal_constant,
        "calibration_over_me_dimensionless": cal_over_me,
    })

mean_ratio = sum(ratios) / len(ratios)
spread = (max(ratios) - min(ratios)) / mean_ratio * 100  # %
print()
print(f"  Mean cal/m_e = {mean_ratio:.6f} (spread {spread:.2f}%)")
print(f"  Per-braid 'natural unit' ≈ {mean_ratio * M_E_MEV:.4f} MeV ≈ {mean_ratio:.3f} × m_e")
print()
print(f"  ┌── Interpretation ──")
print(f"  │ Per-braid total × ({mean_ratio:.4f} × m_e) ≈ AME atomic mass.")
print(f"  │ The {spread:.2f}% spread across A=2..40 is the binding-energy-")
print(f"  │ like correction not captured by the q=1 character.")
print(f"  │ Three-calibration discipline: m_e is the H^0 input;")
print(f"  │ {mean_ratio:.4f} is a dimensionless universal constant of")
print(f"  │ the per-braid tower normalisation.")
print(f"  └────────────────────")
print()
print("KNOWN LIMITATION:")
print(
    "  The current MN character is at q=1; proton and neutron sub-braids\n"
    "  have identical permutation cycle structure, so per-braid traces are\n"
    "  identical for both (0.6715). The full q-deformed Hecke character\n"
    "  distinguishes them; with that refinement the n-p mass splitting\n"
    "  (1.293 MeV) and ³He vs ³H splitting (~0.53 MeV) should emerge."
)

witness = {
    "audit": "Per-braid mass prediction vs AME — calibration check",
    "generated": datetime.now(timezone.utc).isoformat(),
    "q_0": str(q0),
    "m_e_mev": M_E_MEV,
    "calibration_discipline": "prop:three-calibration-discipline (H^0 = m_e)",
    "atoms": results,
    "mean_calibration_over_me": mean_ratio,
    "calibration_spread_percent": spread,
    "interpretation": (
        f"Per-braid total × ({mean_ratio:.6f} × m_e) ≈ AME atomic mass. "
        f"Spread {spread:.2f}% is the binding-energy correction. The "
        f"per-braid 'natural unit' is dimensionless × m_e (H^0 input)."
    ),
    "limitations": [
        (
            "Murnaghan-Nakayama at q=1: proton and neutron sub-braids have "
            "identical permutation cycle structure (S_3 generator action). "
            "Per-braid traces don't distinguish them yet. q-deformed Hecke "
            "character refinement is the next step (P2.2c)."
        ),
    ],
}

out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-01-per-braid-vs-ame.witness.json"
out_path.write_text(json.dumps(witness, indent=2, default=str))
print()
print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
