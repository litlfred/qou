#!/usr/bin/env python3
"""
GB DEPTH = WORD LENGTH interpretation: each hyperbolic knot K
lives in the J^{c_K} filtration ideal where c_K is the (minimal)
crossing/word length of its braid representative.

Damping factor at depth ℓ:
  D₁(ℓ) := 1 / [ℓ]_q!         (q-factorial damping; Habiro)
  D₂(ℓ) := (q; q)_ℓ            (q-Pochhammer)
  D₃(ℓ) := 1 / dim_q V_(ℓ,1,...,1) = 1 / [ℓ]_q  (column-partition damping)

For each hyperbolic knot, multiply Vol(K) by the damping factor at
its GB depth.  Look for a clean correlation with paper-relevant
quantities (e.g., m_e units, the np splitting, A=2 binding).
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = mp.mpf(str(Q0_FLOAT)); QI = mp.mpf(1)/Q0
hbar_q = 1 - QI
hbar_q_sq = hbar_q * hbar_q
me = mp.mpf(str(M_E_MEV))


def q_int(n):
    return (Q0**n - QI**n) / (Q0 - QI)


def q_factorial(n):
    out = mp.mpf(1)
    for k in range(2, n+1):
        out *= q_int(k)
    return out


def q_pochhammer(n):
    """(q;q)_n = ∏_{k=1}^{n} (1 - q^k)."""
    out = mp.mpf(1)
    for k in range(1, n+1):
        out *= (1 - Q0**k)
    return out


# Hyperbolic knots: (name, braid word, n_strands, crossing number, Vol)
HYPERBOLIC_KNOTS = [
    ("4_1",  [1, -2, 1, -2],                    3, 4, 2.0298832),
    ("5_2",  [1, 1, 1, -2, 1, -2],              3, 6, 2.8281220),
    ("6_1",  [1, 1, -2, 1, -2, -2],             3, 6, 3.1639633),
    ("6_2",  [1, 1, 1, -2, 1, -2, -2],          3, 7, 4.4015175),
    ("6_3",  [1, 1, -2, 1, -2, 1, -2],          3, 7, 5.6927297),
    ("7_2",  [1, 1, 1, 1, 1, -2, 1, -2],        3, 8, 3.3317442),
    ("7_3",  [1, 1, 1, 1, -2, 1, 1, -2],        3, 8, 4.5921326),
    ("7_4",  [1, 1, -2, 1, -2, -2, -2],         3, 7, 5.0136959),
    ("7_5",  [1, 1, 1, 1, -2, 1, 1, 1, -2],     3, 9, 6.4439185),
    ("7_6",  [1, 1, 1, -2, 1, -2, -2, -2],      3, 8, 7.0846178),
    ("7_7",  [1, 1, -2, 1, -2, 1, -2, -2],      3, 8, 7.6433568),
]


def main():
    print("=" * 100)
    print("GB DEPTH (word length) → DAMPING FACTOR for hyperbolic knots")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}, ℏ_q² = {float(hbar_q_sq):.6f}")
    print()

    print(f"  {'knot':<6} {'word_len':>8} {'Vol':>10} {'1/[ℓ]_q!':>10} "
          f"{'(q;q)_ℓ':>12} {'1/[ℓ]_q':>10} {'Vol/[ℓ]_q!':>12} {'Vol·(q;q)_ℓ':>14}")

    rows = []
    for name, word, n_str, c_num, vol in HYPERBOLIC_KNOTS:
        ell = len(word)
        D1 = float(1 / q_factorial(ell))
        D2_complex = q_pochhammer(ell)  # may be complex for q > 1
        D2 = float(mp.fabs(D2_complex))
        D3 = float(1 / q_int(ell))
        v_d1 = vol * D1
        v_d2 = vol * D2
        v_d3 = vol * D3
        print(f"  {name:<6} {ell:>8} {vol:>10.4f} {D1:>10.4e} "
              f"{D2:>12.4e} {D3:>10.4f} {v_d1:>12.4e} {v_d2:>14.4e}")
        rows.append({
            'knot': name, 'word_length': ell, 'volume': vol,
            'D1_qfac_inv': D1, 'D2_qpoch': D2, 'D3_qint_inv': D3,
            'vol_x_D1': v_d1, 'vol_x_D2': v_d2, 'vol_x_D3': v_d3,
        })

    # Check whether `Vol · (q;q)_ℓ` or `Vol/[ℓ]_q!` correlates with
    # paper-relevant masses.
    print()
    print("=" * 100)
    print("  Compare to paper quantities")
    print("=" * 100)
    print(f"  m_e = {float(me):.6f} MeV")
    print(f"  m_e · 8G = {float(me * 8 * mp.catalan):.6f} MeV (binding scale α)")
    print(f"  Q_β(n) = {M_N_MEV - M_P_MEV - float(me):.6f} MeV")
    print(f"  Δm_{{n-p}} = {M_N_MEV - M_P_MEV:.6f} MeV")
    print(f"  m_e · Σ_3 = {float(me * (2 + 1/(Q0+QI))):.6f} MeV")
    print()

    # Sum Vol · damping over all knots (analog of "knot tower")
    print(f"  Σ Vol · D for the 11 hyperbolic knots:")
    sum_v_d1 = sum(r['vol_x_D1'] for r in rows)
    sum_v_d2 = sum(r['vol_x_D2'] for r in rows)
    sum_v_d3 = sum(r['vol_x_D3'] for r in rows)
    print(f"    Σ Vol · 1/[ℓ]_q!  = {sum_v_d1:.6e}")
    print(f"    Σ Vol · (q;q)_ℓ   = {sum_v_d2:.6e}")
    print(f"    Σ Vol · 1/[ℓ]_q   = {sum_v_d3:.6f}")
    print(f"    in m_e units:")
    print(f"      D1 sum / m_e   = {sum_v_d1 / float(me):.6e}")
    print(f"      D2 sum / m_e   = {sum_v_d2 / float(me):.6e}")
    print(f"      D3 sum / m_e   = {sum_v_d3 / float(me):.6f}")

    witness = {
        'computation': 'gb-knot-word-depth-damping',
        'description': (
            'Map hyperbolic knots to GB filtration depth = braid word length.  '
            'Compute three damping factor candidates: 1/[ℓ]_q! (q-factorial), '
            '(q;q)_ℓ (q-Pochhammer), 1/[ℓ]_q.  Tests user hypothesis that '
            'GB level provides the scaling/dampening for each knot contribution.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'knots': rows,
        'sum_vol_D1': sum_v_d1,
        'sum_vol_D2': sum_v_d2,
        'sum_vol_D3': sum_v_d3,
    }
    out = Path(__file__).parent / "gb-knot-word-depth-damping.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
