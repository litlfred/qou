#!/usr/bin/env python3
"""
Refine higher-A (A ≥ 5) binding predictions.

Current state (from bw_chirality_isotopes.py):
  - Paper sets a_K = 1 for A ≥ 5 ("many crossings → cancel")
  - Errors 5-20% on ⁶Li through ¹⁶O

New derivation (chirality-dual-space-derivation):
  a_K = ∏_{pn crossings} (1 + sign·h)

For A ≥ 5 atomic braids, count net pn crossings and apply.

Hypothesis: paper's "a_K = 1" is wrong for A ≥ 5; the per-crossing
factorization should continue.

Witness: higher-a-binding-refinement.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from bw_chirality_isotopes import (
    B_bulk, B_Zdep, B_shell, pairing_sign, f_Zdep_scale, h, Q0,
    f_chiral_plus, f_chiral_minus, f_amphi, f_borromean,
)
from hecke_character_symbolic import atomic_braid_to_crossings


def count_pn_crossings(Z, N):
    """Count net pn crossings in atomic braid (sign-aware).
    Inter-nucleon crossings between p and n have specific signs based
    on (c, d) values: (1, -h/2) is averaged (sign 0), but the structural
    intent is one positive + one negative compound."""
    crossings = atomic_braid_to_crossings(Z, N, include_inter=True)
    pn_pos = 0   # inter-nucleon σ
    pn_neg = 0   # inter-nucleon σ⁻¹
    pn_avg = 0   # inter-nucleon averaged
    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    # Inter-nucleon crossings are at generators 3k+2 for k=0..A-2
    inter_idx = [(3 * k + 2, k) for k in range(A - 1)]
    for gen_idx, ct in crossings:
        # Find if this is an inter-nucleon crossing
        for inter_g, k in inter_idx:
            if gen_idx == inter_g:
                pair = (nucleon_types[k], nucleon_types[k + 1])
                if pair[0] != pair[1]:  # pn (or np)
                    if ct == "sigma":
                        pn_pos += 1
                    elif ct == "sigma_inv":
                        pn_neg += 1
                    else:
                        pn_avg += 1
                break
    return pn_pos, pn_neg, pn_avg


def chirality_per_crossing(Z, N):
    """a_K = ∏ (1 + sign·h) over pn crossings.
    Averaged crossings: their contribution is the AVERAGE of (1+h) and (1-h):
      ((1+h) + (1-h))/2 = 1, contributing factor 1 (neutral).
    Net effect: averaged crossings DON'T contribute to chirality.

    For ALTERNATIVE: averaged could contribute multiplicatively as
    sqrt((1+h)(1-h)) = sqrt(1-h²) — geometric mean."""
    pn_pos, pn_neg, pn_avg = count_pn_crossings(Z, N)
    h_val = float(h)
    a_K = (1 + h_val) ** pn_pos * (1 - h_val) ** pn_neg
    # Averaged crossings: arithmetic-mean factor (= 1)
    # Could try geometric: ((1-h²))^{pn_avg/2}
    a_K_geo = a_K * ((1 - h_val ** 2) ** (pn_avg / 2))
    return a_K, a_K_geo, pn_pos, pn_neg, pn_avg


def predict_with_chirality(Z, N, a_K_value, include_shell=True):
    """Paper's formula B = a_K · B_bulk + h·[2]·B_Zdep + B_shell."""
    A = Z + N
    sign = pairing_sign(Z, N)
    bulk = B_bulk(A, Z, N, sign)
    zdep = B_Zdep(A, Z, N)
    shell = B_shell(A, Z, N) if include_shell and A >= 4 else mp.mpf(0)
    a_K_mp = mp.mpf(str(a_K_value))
    return float(a_K_mp * bulk + f_Zdep_scale * zdep + shell)


if __name__ == "__main__":
    print("HIGHER-A BINDING REFINEMENT — A ≥ 5 isotopes")
    print("=" * 96)
    print(f"q_0 = {Q0}")
    print(f"h = q - q⁻¹ = {float(h):.6f}")
    print()

    ISOTOPES = [
        ("D",   1, 1,  2.22457),
        ("T",   1, 2,  8.48180),
        ("3He", 2, 1,  7.71806),
        ("4He", 2, 2, 28.29569),
        ("6Li", 3, 3, 31.99405),
        ("7Li", 3, 4, 39.24452),
        ("9Be", 4, 5, 58.16505),
        ("10B", 5, 5, 64.75080),
        ("11B", 5, 6, 76.20546),
        ("12C", 6, 6, 92.16175),
        ("14N", 7, 7,104.65864),
        ("16O", 8, 8,127.61931),
    ]

    print(f"{'iso':>5} {'A':>3} {'pn+':>4} {'pn-':>4} {'pn_a':>5} "
          f"{'a_K (per-cr)':>14} {'paper a_K':>10} "
          f"{'B_per-cr':>10} {'B_paper':>10} {'B_AME':>9} "
          f"{'err_per':>9} {'err_paper':>10}")
    print('-' * 110)

    rows = []
    for iso, Z, N, B_AME in ISOTOPES:
        A = Z + N
        a_K_per, a_K_geo, pn_p, pn_n, pn_a = chirality_per_crossing(Z, N)

        # Paper's a_K (matches for A ≤ 4, set to 1 for A ≥ 5)
        if A == 2:
            a_K_paper = float(f_chiral_plus)
        elif A == 3:
            a_K_paper = float(f_amphi)
        elif A == 4:
            a_K_paper = float(f_borromean)
        else:
            a_K_paper = 1.0

        B_per = predict_with_chirality(Z, N, a_K_per, include_shell=A >= 4)
        B_paper = predict_with_chirality(Z, N, a_K_paper, include_shell=A >= 4)

        err_per = (B_per - B_AME) / B_AME * 100
        err_paper = (B_paper - B_AME) / B_AME * 100

        print(f"{iso:>5} {A:>3} {pn_p:>4} {pn_n:>4} {pn_a:>5} "
              f"{a_K_per:>14.4f} {a_K_paper:>10.4f} "
              f"{B_per:>10.3f} {B_paper:>10.3f} {B_AME:>9.3f} "
              f"{err_per:>+8.2f}% {err_paper:>+9.2f}%")
        rows.append({
            "isotope": iso, "Z": Z, "N": N, "A": A,
            "pn_pos": pn_p, "pn_neg": pn_n, "pn_avg": pn_a,
            "a_K_per_crossing": a_K_per,
            "a_K_paper": a_K_paper,
            "B_pred_per_crossing": B_per,
            "B_pred_paper": B_paper,
            "B_AME": B_AME,
            "err_pct_per_crossing": err_per,
            "err_pct_paper": err_paper,
        })

    # Summary
    print()
    light = [r for r in rows if r["A"] <= 4]
    heavy = [r for r in rows if r["A"] >= 5]
    print(f"A ≤ 4 isotopes (n={len(light)}):")
    print(f"  per-cr   max |err|: {max(abs(r['err_pct_per_crossing']) for r in light):.2f}%")
    print(f"  paper    max |err|: {max(abs(r['err_pct_paper']) for r in light):.2f}%")
    print()
    print(f"A ≥ 5 isotopes (n={len(heavy)}):")
    print(f"  per-cr   max |err|: {max(abs(r['err_pct_per_crossing']) for r in heavy):.2f}%")
    print(f"  paper    max |err|: {max(abs(r['err_pct_paper']) for r in heavy):.2f}%")
    print(f"  per-cr   mean |err|: {sum(abs(r['err_pct_per_crossing']) for r in heavy)/len(heavy):.2f}%")
    print(f"  paper    mean |err|: {sum(abs(r['err_pct_paper']) for r in heavy)/len(heavy):.2f}%")

    witness = {
        "computation": "higher-a-binding-refinement",
        "description": (
            "Tests whether the per-crossing chirality factor "
            "a_K = ∏_{pn} (1 + sign·h) (derived in "
            "prop:chirality-dual-space-derivation) improves higher-A "
            "binding predictions vs paper's a_K = 1 default at A ≥ 5."
        ),
        "reference_blocks": [
            "prop:chirality-dual-space-derivation",
            "prop:figure-eight-bw-coefficients",
            "thm:six-term-mass-formula-complete",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q_0": float(Q0), "h": float(h)},
        "rows": rows,
    }
    out = Path(__file__).parent / "higher-a-binding-refinement.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
