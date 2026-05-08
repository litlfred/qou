#!/usr/bin/env python3
"""
Term6 binding-formula scaling probe — heavy nuclei.

The Term6/A³ + magic-correction formula was fit on D...16O.
This probe tests whether the same SHAPE holds at heavy nuclei
(A = 24, 28, 32, 40, 48, 56, ...) where:

  - The triple-stratum count grows as A³ → tighter constraint on α
  - Magic atoms appear at Z=20 (40Ca), Z=28 (56Ni), Z=50 (Sn),
    Z=82 (Pb)
  - More atoms reduces fit uncertainty on α and β

Strategy: compute Term6 for each atom, fit B/A ≈ α·T6/A³ + β,
report:
  - α and β with confidence interval
  - Per-atom residuals (magic enhancement should appear at
    20Ca, 28Ni, 50Sn, 82Pb)
  - Whether the SHAPE holds across the full nuclear range

Cost note: Term6 requires Markov traces of 9-strand sub-braids
ppp / ppn / pnn / nnn. These are O(1) per atom (sub-braid traces
are atom-independent — already cached). Per-atom binding-fit
calculation is cheap.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0, _safe_phi, z_mark
from schur_weyl_mpmath import markov_trace_mpmath


# AME 2020 atomic masses (MeV) for selected nuclei across the full range.
# Source: AME 2020 (https://www-nds.iaea.org/amdc/).
AME_PANEL = {
    "D":     ("D",     1, 1,  1875.61294257),
    "3He":   ("3He",   2, 1,  2808.39148127),
    "3H":    ("3H",    1, 2,  2808.92113298),
    "4He":   ("4He",   2, 2,  3727.37909409),
    "6Li":   ("6Li",   3, 3,  5603.05182),
    "7Li":   ("7Li",   3, 4,  6535.36573),
    "9Be":   ("9Be",   4, 5,  8392.74912),
    "12C":   ("12C",   6, 6, 11177.92924),
    "16O":   ("16O",   8, 8, 14899.16828),
    "20Ne":  ("20Ne", 10, 10, 18617.7286),
    "24Mg":  ("24Mg", 12, 12, 22335.7917),
    "28Si":  ("28Si", 14, 14, 26060.3401),
    "32S":   ("32S",  16, 16, 29781.6324),
    "40Ca":  ("40Ca", 20, 20, 37224.9202),  # doubly-magic
    "48Ca":  ("48Ca", 20, 28, 44657.2802),  # neutron-magic
    "56Ni":  ("56Ni", 28, 28, 52109.5418),  # doubly-magic
    "58Ni":  ("58Ni", 28, 30, 53972.4076),
}

# pre-compute the per-triple-pair sub-braid traces (atom-independent,
# only 4 distinct values: ppp, ppn, pnn, nnn at H_9(q))
_SUB_BRAID_CACHE = {}


def cached_subbraid(Z_sub: int, N_sub: int) -> mpmath.mpf:
    """|tr_M(Z_sub-proton, N_sub-neutron sub-braid)| via H_{3(Z_sub+N_sub)}."""
    key = (Z_sub, N_sub)
    if key not in _SUB_BRAID_CACHE:
        v, _, _ = markov_trace_mpmath(Z_sub, N_sub, q_val=q0,
                                        include_inter=True)
        _SUB_BRAID_CACHE[key] = abs(v)
    return _SUB_BRAID_CACHE[key]


def term6(Z: int, N: int) -> float:
    A = Z + N
    if A < 3:
        return 0.0
    n_ppp = Z * (Z - 1) * (Z - 2) // 6 if Z >= 3 else 0
    n_nnn = N * (N - 1) * (N - 2) // 6 if N >= 3 else 0
    n_ppn = (Z * (Z - 1) // 2) * N if Z >= 2 and N >= 1 else 0
    n_pnn = Z * (N * (N - 1) // 2) if Z >= 1 and N >= 2 else 0

    total = mpmath.mpf(0)
    if n_ppp > 0:
        v = cached_subbraid(3, 0)
        if v > 0:
            total += n_ppp * _safe_phi(v)
    if n_nnn > 0:
        v = cached_subbraid(0, 3)
        if v > 0:
            total += n_nnn * _safe_phi(v)
    if n_ppn > 0:
        v = cached_subbraid(2, 1)
        if v > 0:
            total += n_ppn * _safe_phi(v)
    if n_pnn > 0:
        v = cached_subbraid(1, 2)
        if v > 0:
            total += n_pnn * _safe_phi(v)
    return float(total * z_mark ** 3)


MAGIC = (2, 8, 20, 28, 50, 82, 126)


def is_magic_pair(Z: int, N: int) -> int:
    return 1 if (Z in MAGIC and N in MAGIC) else 0


def main():
    print("=" * 92)
    print("Term6 binding-formula scaling probe — heavy nuclei")
    print("=" * 92)
    print()

    M_P_MEV = 938.272
    rows = []
    for label, (name, Z, N, ame) in AME_PANEL.items():
        A = Z + N
        T6 = term6(Z, N)
        bn = M_P_MEV - ame / A
        norm = T6 / A ** 3 if A > 0 else 0
        rows.append({"atom": name, "Z": Z, "N": N, "A": A,
                     "term6": T6, "term6_over_A3": norm,
                     "binding_per_nucleon": bn,
                     "is_magic_pair": is_magic_pair(Z, N)})

    print(f"  {'atom':>6} {'A':>3} {'magic?':>7} {'Term6':>14} "
          f"{'T6/A³':>10} {'B/A AME':>10}")
    print("  " + "-" * 60)
    for r in rows:
        magic_marker = "★" if r["is_magic_pair"] else " "
        print(f"  {r['atom']:>6} {r['A']:>3} {magic_marker:>7} "
              f"{r['term6']:>14.4e} {r['term6_over_A3']:>10.4e} "
              f"{r['binding_per_nucleon']:>10.4f}")

    # Fit on the full panel
    A_arr = np.array([r["A"] for r in rows])
    T6_norm = np.array([r["term6_over_A3"] for r in rows])
    bn_arr = np.array([r["binding_per_nucleon"] for r in rows])

    valid = T6_norm > 0
    T6n = T6_norm[valid]
    bn_v = bn_arr[valid]
    coef = np.polyfit(T6n, bn_v, 1)
    pred = np.polyval(coef, T6n)
    resid = bn_v - pred
    R = np.corrcoef(T6n, bn_v)[0, 1]
    print()
    print(f"  ── Full-panel fit (n = {len(T6n)} atoms) ──")
    print(f"  α = {coef[0]:.4f}, β = {coef[1]:.4f}, R² = {R ** 2:.4f}")
    print(f"  residual σ = {resid.std():.4f} MeV, max |resid| = {np.max(np.abs(resid)):.4f}")
    print()
    print(f"  ── Compare to D...16O fit (7 atoms) ──")
    print(f"  α = 342.5, β = 1.20, R² = 0.70")

    # Per-atom residuals + magic indicator
    print()
    print(f"  {'atom':>6} {'A':>3} {'B/A':>9} {'pred':>9} {'resid':>9} {'magic?':>7}")
    print("  " + "-" * 55)
    j = 0
    for r in rows:
        if r["term6_over_A3"] == 0:
            continue
        rsd = bn_v[j] - pred[j]
        m = "★" if r["is_magic_pair"] else " "
        print(f"  {r['atom']:>6} {r['A']:>3} {bn_v[j]:>9.3f} "
              f"{pred[j]:>9.3f} {rsd:>+9.3f} {m:>7}")
        j += 1

    # Magic-residual correlation
    if len(T6n) > 2:
        valid_rows = [r for r in rows if r["term6_over_A3"] > 0]
        magic_arr = np.array([r["is_magic_pair"] for r in valid_rows])
        if magic_arr.std() > 0:
            corr = np.corrcoef(magic_arr, resid)[0, 1]
            print(f"\n  Magic-pair correlation w/ residual: {corr:+.4f}")

    out = {
        "computation": "Term6-scaling-heavy-nuclei",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "panel_atoms": [r["atom"] for r in rows],
        "n_atoms_in_fit": int(valid.sum()),
        "fit": {"alpha_MeV": float(coef[0]), "beta_MeV": float(coef[1]),
                 "R_sq": float(R ** 2),
                 "residual_std_MeV": float(resid.std()),
                 "max_abs_resid_MeV": float(np.max(np.abs(resid)))},
        "atoms": rows,
        "interpretation": (
            "Tests Term6/A³ binding formula scaling beyond A=16. The "
            "panel includes doubly-magic 40Ca, 56Ni and the larger "
            "stable nuclei 20Ne/24Mg/28Si/32S. Whether α stays near "
            "342.5 MeV or drifts indicates whether the formula is "
            "structurally consistent at heavy nuclei or only holds "
            "for the light-atom test panel."
        ),
    }
    p_out = (Path(__file__).parent.parent.parent
             / "docs/audits/2026-05-02-Term6-scaling-heavy.witness.json")
    p_out.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {p_out.relative_to(Path(__file__).parent.parent.parent)}")


if __name__ == "__main__":
    main()
