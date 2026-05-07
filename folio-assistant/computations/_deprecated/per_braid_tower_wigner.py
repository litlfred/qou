#!/usr/bin/env python3
"""
Per-braid + q-Hecke Coulomb + Wigner asymmetry probe.

Adds the SEMF Asymmetry term (per `prop:wigner-np-pairing`) on top
of the principled Coulomb-corrected hybrid. The Wigner formula
([wigner-np-pairing.md](../../content/quantum-observable-universe/braids-and-knots/wigner-np-pairing.md))
is

    ΔB_Wigner = -m_e · H_q((2,2)) · min(Z, N) / A
              = -m_e · [3]_q · [2]_q² · min(Z, N) / A
              ≈ -6.29 MeV · min(Z, N) / A   (at q_0)

negative sign because Wigner is BINDING (reduces mass).

We also probe Pairing (Term 5 of SEMF):
    ΔB_pairing = ±m_e · H_q((1,1)) / A^(1/2)  (sign: +even-even, -odd-odd, 0 odd-A)
where H_q((1,1)) = [2]_q (smallest self-conjugate hook product)
gives ~0.21 MeV — too small. Try alternative scales.

Witness: docs/audits/2026-05-02-per-braid-wigner.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import (
    per_braid_mass_hybrid, q0, qi0, z_mark, M_E_MEV, AME_MASS_MEV
)


def q_int(k):
    return (q0 ** k - qi0 ** k) / (q0 - qi0) if k else mpmath.mpf(0)


# Wigner unit (Term 4, asymmetry/np-pairing): m_e · H_q((2,2)) = m_e · [3]_q · [2]_q²
delta_W_unit_MeV = M_E_MEV * float(q_int(3)) * float(q_int(2)) ** 2

# Pairing unit (Term 5): scale TBD; try m_e · [2]_q (smallest self-conj hook product)
# This is too small at ~0.21 MeV. SEMF a_P ≈ 11.18 MeV. Real categorical
# scale likely involves higher hook products / shell-correction terms.
delta_pair_unit_MeV = M_E_MEV * float(q_int(2))


def wigner_correction_MeV(Z: int, N: int) -> float:
    """Wigner T=0 isoscalar np-pairing BONUS at near-N=Z (binding).

    Per prop:wigner-np-pairing: -m_e · H_q((2,2)) · min(Z, N) / A.
    """
    A = Z + N
    if A < 2 or Z < 1 or N < 1:
        return 0.0
    return -delta_W_unit_MeV * min(Z, N) / A


# Categorical scales derived from q_0 only (no SEMF empirical coefficients).
#
# For asymmetry: candidate scale is m_e · H_q((3,1)) = m_e · [4]_q · [2]_q · [1]_q · [1]_q
#   = m_e · [4]_q · [2]_q  (the q-hook product of the self-conjugate
#   partition (3,1) ⊢ 4, also the next 4-cell partition after (2,2)).
delta_asym_unit_MeV = M_E_MEV * float(q_int(4) * q_int(2))

# For pairing: candidate scale is m_e · H_q((1,1)) = m_e · [2]_q · [1]_q = m_e · [2]_q
#   (smallest self-conjugate 2-cell partition; algebraic minimum).
delta_pairing_unit_MeV = M_E_MEV * float(q_int(2))


def asymmetry_correction_MeV(Z: int, N: int) -> float:
    """Asymmetry penalty using CATEGORICAL hook-product scale (not SEMF).

    Form: m_e · H_q((3,1)) · (N-Z)² / A
    Scale derivation: (3,1) is the next self-conjugate-after-(2,2)
    partition of 4; its hook product gives the natural categorical
    quadratic-asymmetry scale. SEMF a_A is empirically 23.69 MeV;
    this categorical version yields ~m_e · [4]_q · [2]_q ≈ 4.5 MeV
    — an order of magnitude smaller, suggesting either (a) a different
    categorical partition is right, or (b) (N-Z)²/A is missing a
    multiplicative q-factor from the per-A normalisation.
    """
    A = Z + N
    if A < 1:
        return 0.0
    return delta_asym_unit_MeV * (N - Z) ** 2 / A


def pairing_correction_MeV(Z: int, N: int) -> float:
    """Pairing using CATEGORICAL hook-product scale (not SEMF).

    Form: ±m_e · [2]_q / √A
    Sign: -ee (binding bonus), +oo (penalty), 0 oa.
    Categorical [2]_q ≈ 2.011 → unit ≈ 1.03 MeV — empirically smaller
    than SEMF a_P ≈ 11.18 MeV, suggesting the right categorical
    scale uses a larger hook product or a different self-conjugate
    partition.
    """
    A = Z + N
    if A < 2:
        return 0.0
    if Z % 2 == 0 and N % 2 == 0:
        return -delta_pairing_unit_MeV / mpmath.sqrt(A)
    if Z % 2 == 1 and N % 2 == 1:
        return +delta_pairing_unit_MeV / mpmath.sqrt(A)
    return 0.0


if __name__ == "__main__":
    print("=" * 100)
    print("Per-braid + q-Hecke Coulomb + Wigner asymmetry + Pairing probe")
    print("=" * 100)
    print(f"q_0   = {q0}")
    print(f"m_e   = {M_E_MEV} MeV")
    print(f"H_q((2,2)) = [3]_q · [2]_q² = {float(q_int(3) * q_int(2)**2):.4f}")
    print(f"Wigner unit  = m_e · H_q((2,2)) = {delta_W_unit_MeV:.4f} MeV")
    print(f"Pairing unit = m_e · [2]_q     = {delta_pair_unit_MeV:.4f} MeV")
    print()

    ATOMS = [
        ("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2),
        ("6Li", 3, 3), ("7Li", 3, 4), ("9Be", 4, 5),
        ("12C", 6, 6), ("16O", 8, 8), ("40Ca", 20, 20),
    ]

    print(f"  {'atom':>5} {'A':>3} {'pred (H)':>10} "
          f"{'ΔW':>7} {'Δasym':>7} {'Δpair':>7} "
          f"{'cal bare':>10} {'cal +W':>9} {'cal +W+A':>10} {'cal full':>10}")
    print("  " + "-" * 100)
    rows = []
    bare, with_W, with_WA, with_full = [], [], [], []
    for name, Z, N in ATOMS:
        out = per_braid_mass_hybrid(Z, N)
        pred = float(out["total"])  # Hecke units
        ame = AME_MASS_MEV[name]

        cal_bare = (ame / pred) / M_E_MEV
        bare.append(cal_bare)

        dW = wigner_correction_MeV(Z, N)
        pred_eff_W = pred + dW / M_E_MEV
        cal_W = (ame / pred_eff_W) / M_E_MEV
        with_W.append(cal_W)

        dA = asymmetry_correction_MeV(Z, N)
        pred_eff_WA = pred_eff_W + dA / M_E_MEV
        cal_WA = (ame / pred_eff_WA) / M_E_MEV
        with_WA.append(cal_WA)

        dP = float(pairing_correction_MeV(Z, N))
        pred_eff_full = pred_eff_WA + dP / M_E_MEV
        cal_full = (ame / pred_eff_full) / M_E_MEV
        with_full.append(cal_full)

        print(f"  {name:>5} {Z+N:>3} {pred:>10.2f} "
              f"{dW:>+7.3f} {dA:>+7.3f} {dP:>+7.3f} "
              f"{cal_bare:>10.6f} {cal_W:>9.6f} {cal_WA:>10.6f} {cal_full:>10.6f}")
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": Z + N,
            "pred_hecke": pred,
            "delta_wigner_mev": dW,
            "delta_asymmetry_mev": dA,
            "delta_pairing_mev": dP,
            "cal_over_me_bare": cal_bare,
            "cal_over_me_W": cal_W,
            "cal_over_me_WA": cal_WA,
            "cal_over_me_full": cal_full,
        })

    def stats(name, ratios):
        m = sum(ratios) / len(ratios)
        s = (max(ratios) - min(ratios)) / m * 100
        return name, m, s

    name1, m1, s1 = stats("Bare (Coulomb hybrid)", bare)
    name2, m2, s2 = stats("+ Wigner",                with_W)
    name3, m3, s3 = stats("+ Wigner + Asymmetry",    with_WA)
    name4, m4, s4 = stats("+ W + A + Pairing (full)", with_full)
    print()
    for n, m, s in [(name1, m1, s1), (name2, m2, s2), (name3, m3, s3), (name4, m4, s4)]:
        print(f"  {n:<28}  mean = {m:.6f}  spread = {s:.4f}%")
    print()
    print(f"  Δ spread (W vs bare):       {s2 - s1:+.4f}%")
    print(f"  Δ spread (W+A vs bare):     {s3 - s1:+.4f}%")
    print(f"  Δ spread (full vs bare):    {s4 - s1:+.4f}%")

    out_path = (Path(__file__).parent.parent.parent
                / "docs/audits/2026-05-02-per-braid-wigner.witness.json")
    out_path.write_text(json.dumps({
        "audit": "Per-braid + Coulomb + Wigner asymmetry + Pairing probe",
        "generated": datetime.now(timezone.utc).isoformat(),
        "q_0": str(q0),
        "m_e_mev": M_E_MEV,
        "wigner_unit_mev": delta_W_unit_MeV,
        "pairing_unit_mev": delta_pair_unit_MeV,
        "atoms": rows,
        "stats": {
            "bare":    {"mean": m1, "spread_pct": s1},
            "wigner":  {"mean": m2, "spread_pct": s2},
            "wigner_asymmetry": {"mean": m3, "spread_pct": s3},
            "full_W_A_P": {"mean": m4, "spread_pct": s4},
        },
        "interpretation": (
            "Wigner uses prop:wigner-np-pairing formula: ΔB = -m_e · "
            "H_q((2,2)) · min(Z,N)/A ≈ -6.29 MeV · min/A (binding). "
            "Pairing uses ±m_e · [2]_q / √A with sign from Z/N parity."
        ),
    }, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
