#!/usr/bin/env python3
"""Proof Step 4 of conj:lambda-scale-substrate-form — O(h⁴) remainder.

Step 4 of the proof strategy claims:

> The next-order correction τ^(4) in the q-expansion
>   τ_q = τ_1 + h²·τ^(2) + h^4·τ^(4) + O(h^6)
> on H_4 is bounded by a finite Wedderburn-block computation.

The probe found c_4 ≈ +0.00691 (numerical residual after subtracting
5/2 - h²·G from the CODATA λ_p target). To upgrade Step 4 to a
proved closure, c_4 must come from a substrate-derivable expression.

This script does three things:

1. **Refine c_4 to higher precision** by computing
   λ_p_target = (m_p/m_e) · ℏ_q² / Vol(B_3) at mpmath 100 dps and
   isolating the h^4 coefficient.

2. **Test candidate substrate forms** for c_4: rational multiples of
   q-integer products, G^2 forms, [n]_q ratios, etc.

3. **Connect to the H_4 Wedderburn-block character expansion**
   at q = 1: the leading h² correction is the *trace* of the
   second-derivative of the q-deformation on the half-symmetric
   partition combination; h^4 should be the *trace of the
   fourth-derivative*, computable in closed form.

## What's derivable

The Wedderburn-block characters at q=1 are classical (Schur
characters). Their q-deformation has well-known h-expansion:
  [n]_q = n + n(n²-1)/6 · h² + n(n²-1)(3n²-7)/360 · h^4 + O(h^6)
(at q = 1 + h/2 + O(h²) — careful with conventions).

For the (2,2) self-conjugate partition (dimension 2), the
half-contribution at q=1 is 1/2 · χ_{(2,2)}(1) = 1/2 · 2 = 1.
The 2 conjugate pairs contribute 1 each at q=1.

Total leading: 2·1 + 1 = 3? But we claimed 5/2... so the
"half-symmetric count" is a different rational than a simple
trace count at q=1. The structural identification is subtler.

## Status

This probe surfaces multiple unresolved questions:
- What's the precise "half-symmetric trace" formula at q=1?
- Does c_4 admit a closed form?
- Does the formula extend to higher A?

The probe emits all numerical candidates + a clear next-step list.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 100

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402 — canonical q_0 source
from experimental_constants import (  # noqa: E402 — CODATA single source
    M_E_MEV, M_P_MEV, Q_NEUTRON_MEV,
)

# Substrate
Q = Q_MP
H = Q - mp.mpf(1) / Q
HBAR_Q = (Q - mp.mpf(1)) / Q
G = mp.catalan
VOL_B3 = 8 * mp.catalan  # = Vol(Borromean rings complement), 8·G via Adams 1985

# CODATA (single source — experimental_constants); m_n derived via 3-input scheme
M_E = mp.mpf(M_E_MEV)
M_P = mp.mpf(M_P_MEV)
M_N = M_P + mp.mpf(Q_NEUTRON_MEV) + M_E

LAM_P_TARGET = (M_P / M_E) * HBAR_Q**2 / VOL_B3


def qint(n):
    return (Q**n - Q**(-n)) / (Q - 1/Q)


def main() -> int:
    w = WitnessBuilder("lambda-scale-proof-step4-h4-remainder", engine="mpmath")
    w.set_description(
        "Proof Step 4 of conj:lambda-scale-substrate-form — "
        "investigate the O(h^4) remainder coefficient c_4 in "
        "λ_p = 5/2 − h²·G − h^4·c_4 + O(h^6). Refines c_4 to "
        "high precision and tests candidate substrate forms."
    )
    w.set_content_block("conj:lambda-scale-substrate-form")
    w.add_parameter("dps", 100)
    w.add_parameter("q_0", mp.nstr(Q, 30))
    w.add_parameter("h", mp.nstr(H, 30))
    w.add_parameter("G_catalan", mp.nstr(G, 30))

    # Solve for c_4 at high precision:
    #   λ_p_target = 5/2 - h²·G - h^4·c_4
    #   c_4 = (5/2 - h²·G - λ_p_target) / h^4
    c4 = (mp.mpf(5)/2 - H**2 * G - LAM_P_TARGET) / H**4
    w.add_data("c4_solved", mp.nstr(c4, 30))
    w.add_data("c4_solved_30dps", mp.nstr(c4, 30))
    print(f"c_4 solved (h^4 coefficient) at 100 dps:")
    print(f"  c_4 = {mp.nstr(c4, 25)}")
    print()

    # Test simple rational candidates
    candidates_rational = {
        "G^2": G**2,
        "G^2/2": G**2 / 2,
        "1/(8·G)": 1/(8*G),
        "G/h": G/H,
        "h·G": H*G,
        "[2]_q · h": qint(2) * H,
        "1/[2]_q": 1/qint(2),
        "1/(2·[3]_q)": 1/(2*qint(3)),
        "1/([4]_q)": 1/qint(4),
        "h/(8·G)": H/(8*G),
        "h/2": H/2,
        "1/24": mp.mpf(1)/24,
        "G^2 · 5/2": G**2 * mp.mpf(5)/2,
        "h^2/3": H**2 / 3,
    }
    cand_results = {}
    for name, val in candidates_rational.items():
        diff = float(val - c4)
        ratio = float(val / c4) if c4 != 0 else float('nan')
        cand_results[name] = {
            "value": mp.nstr(val, 12),
            "abs_diff_from_c4": diff,
            "ratio_to_c4": ratio,
        }
    w.add_data("simple_substrate_candidates", cand_results)

    # Print closest
    sorted_c = sorted(cand_results.items(),
                      key=lambda kv: abs(kv[1]["abs_diff_from_c4"]))
    print("Top 5 candidates for c_4 (sorted by absolute diff):")
    for name, info in sorted_c[:5]:
        print(f"  {name:24s}: {info['value']:>22s}  (Δ to c_4 = {info['abs_diff_from_c4']:+.5e})")
    print()

    # Try: c_4 = some specific rational times h to test
    # if it's really an h-series coefficient
    c4_over_h = c4 / H
    c4_over_h2 = c4 / H**2
    print(f"c_4/h  = {mp.nstr(c4_over_h, 15)}")
    print(f"c_4/h² = {mp.nstr(c4_over_h2, 15)}")
    w.add_data("c4_normalised", {
        "c4_over_h": mp.nstr(c4_over_h, 20),
        "c4_over_h_squared": mp.nstr(c4_over_h2, 20),
        "comment": (
            "If c_4 is itself O(h), the formula simplifies to "
            "λ_p = 5/2 − h²·G − h^5·(c_4/h) + O(h^7). "
            "c_4/h ≈ 0.033 — small but non-zero, suggests a "
            "fundamental h^5 contribution."
        ),
    })

    # Connect to FSC pattern: 1/α_EM has corrections at h^6, h^8
    # of similarly small magnitudes. The c_4 here might be the
    # analog of that for the baryon sector.
    w.add_data("FSC_analogy", {
        "FSC_bare_form": "1/α_EM = q · [9]_q · [10]_q (CODATA to 6.7e-9)",
        "baryon_bare_form": "λ_p = 5/2 - h²·G + O(h^4)",
        "FSC_correction_scale": "8e-9 relative",
        "baryon_correction_scale": f"{float(abs(H**4 * c4 / LAM_P_TARGET)):.3e} relative (c_4·h^4/λ_p)",
        "interpretation": (
            "The baryon-sector h^4 correction is ~5 ppm of λ_scale "
            "(consistent with the 5.4 ppm proton residual). "
            "FSC-style PSLQ uniqueness in a sufficiently large q-integer "
            "basis at 100+ dps might pin c_4's closed form."
        ),
    })

    # Caveat — open R&D
    w.add_caveat(
        "Step 4 is OPEN R&D. The probe surfaces c_4 ≈ 0.00691 but "
        "no simple substrate form matches. Closed-form derivation "
        "requires either (a) a sufficiently extended PSLQ basis "
        "search, or (b) a direct categorical derivation from the "
        "H_4 Wedderburn-block characters' h^4 expansion. Both are "
        "concrete next steps."
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
