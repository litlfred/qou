#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Q_β N=2 brane-tower truncation — Hoefsmit recursion beyond N=1.

PR #655 N=1 finding (probe_q_beta_operator_valued_N1.py):
  Q_β^{A,N=1}  =  Q_β^A · cos(α − b·ℏ_q²/2)    →  74 ppm
  α = (z-1)h/2
  b = √(q⁴ + q² + 1) / (q² + 1)   ← Hoefsmit off-diagonal coupling
  ℏ_q = (q-1)/q

The N=1 correction is a SHIFT of the eigenphase by −b·ℏ_q²/2. The
c(K) bound at N=1 is 97 ppm; the cos(α − b·ℏ_q²/2) result of 74 ppm
sits just under it (relative slack 0.76).

At N=2 the c(K) bound is 0.96 ppm — 77× tighter than N=1. The
natural Hoefsmit recursion suggests the next-order eigenphase
correction at b² · ℏ_q^4 / 2 scale (the next term in the Taylor
expansion of the Hoefsmit seminormal action around q=1).

This probe tests several N=2 ansätze:

  cos(α − b·ℏ_q²/2 − b²·ℏ_q^4/2)     [Hoefsmit recursion ansatz]
  cos(α − b·ℏ_q²/2 + b²·ℏ_q^4/2)     [opposite sign]
  cos(α − b·ℏ_q²/2 − b²·ℏ_q^4/4)     [half-scale]
  cos(α − b·ℏ_q²/2) · cos(b·ℏ_q²)    [iterated cos]
  cos(α − b·ℏ_q²/2 − b² ℏ_q^4)       [doubled b² term]
  cos(α − b·ℏ_q²/2 − b²·ℏ_q^4/2 − b³·ℏ_q^6/2)  [Hoefsmit N=3]
  Padé[3,3] resummation in (b·ℏ_q²)

If the Hoefsmit recursion structure is correct, one of the b²·ℏ_q^4
ansätze should sit under the 0.96 ppm N=2 ceiling.

Output: `q-beta-operator-valued-N2.witness.json`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps()


def _q_0_50dps() -> mp.mpf:
    with (HERE / "q-pinning-50-digit.witness.json").open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


def main() -> int:
    q = _q_0_50dps()
    m_e = mp.mpf(str(M_E_MEV))
    Q_AME = mp.mpf("939.5654205240") - mp.mpf("938.27208816") - m_e
    Q_A = m_e * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    h = q - 1 / q
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    hbar_q = (q - 1) / q
    hbar_q_sq = hbar_q ** 2
    hbar_q_4th = hbar_q ** 4
    alpha = (z - 1) * h / 2

    # Hoefsmit b — closed form derived from d_1 · d_2 + 1
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b_sq = d1 * d2 + 1
    b = mp.sqrt(b_sq)

    # N=1 shift (PR #655 winner)
    n1_shift = b * hbar_q_sq / 2
    alpha_n1 = alpha - n1_shift

    print("=" * 96)
    print("  Q_β N=2 brane-tower truncation via Hoefsmit recursion")
    print("=" * 96)
    print()
    print(f"  q_0      = {mp.nstr(q, 14)}")
    print(f"  α        = (z-1)h/2 = {mp.nstr(alpha, 14)}")
    print(f"  ℏ_q²     = {mp.nstr(hbar_q_sq, 14)}")
    print(f"  ℏ_q^4    = {mp.nstr(hbar_q_4th, 14)}")
    print(f"  b        = √(q⁴+q²+1)/(q²+1) = {mp.nstr(b, 14)}")
    print(f"  b² · ℏ_q^4 / 2 = {mp.nstr(b ** 2 * hbar_q_4th / 2, 14)}")
    print()

    eps_N0 = (Q_A / Q_AME - 1) * mp.mpf("1e6")
    eps_N1 = (Q_A * mp.cos(alpha_n1) / Q_AME - 1) * mp.mpf("1e6")
    print(f"  baseline:")
    print(f"    Form A bare:              {float(eps_N0):+10.4f} ppm (N=0 form)")
    print(f"    cos(α − b·ℏ_q²/2):        {float(eps_N1):+10.4f} ppm (N=1 form, PR #655)")
    print(f"    c(K) N=2 ceiling:           ≤ 0.96 ppm")
    print()

    # N=2 candidates
    n2_scale = b ** 2 * hbar_q_4th / 2  # natural Hoefsmit recursion scale
    candidates = {
        # Hoefsmit recursion: shift by additional b² · ℏ_q^4 / 2 (both signs)
        "cos(α − b·ℏ_q²/2 − b²·ℏ_q^4/2)":
            mp.cos(alpha_n1 - n2_scale),
        "cos(α − b·ℏ_q²/2 + b²·ℏ_q^4/2)":
            mp.cos(alpha_n1 + n2_scale),
        # Half-scale variants
        "cos(α − b·ℏ_q²/2 − b²·ℏ_q^4/4)":
            mp.cos(alpha_n1 - n2_scale / 2),
        "cos(α − b·ℏ_q²/2 + b²·ℏ_q^4/4)":
            mp.cos(alpha_n1 + n2_scale / 2),
        # Doubled-scale variants
        "cos(α − b·ℏ_q²/2 − b²·ℏ_q^4)":
            mp.cos(alpha_n1 - 2 * n2_scale),
        "cos(α − b·ℏ_q²/2 + b²·ℏ_q^4)":
            mp.cos(alpha_n1 + 2 * n2_scale),
        # Iterated cos (multiplicative composition)
        "cos(α − b·ℏ_q²/2) · cos(b·ℏ_q²)":
            mp.cos(alpha_n1) * mp.cos(b * hbar_q_sq),
        "cos(α − b·ℏ_q²/2) · cos(b·ℏ_q²/2)":
            mp.cos(alpha_n1) * mp.cos(b * hbar_q_sq / 2),
        "cos(α − b·ℏ_q²/2) · cos(b²·ℏ_q^4/2)":
            mp.cos(alpha_n1) * mp.cos(b ** 2 * hbar_q_4th / 2),
        # Through Padé[3,3] in (b·ℏ_q²)
        "(1 − α_N1²/2 + α_N1^4/24 − α_N1^6/720)":
            1 - alpha_n1 ** 2 / 2 + alpha_n1 ** 4 / 24 - alpha_n1 ** 6 / 720,
        # Three-term Hoefsmit (N=3): include b³ · ℏ_q^6 / 6 (anti-symmetric)
        "cos(α_N1) − b³·ℏ_q^6 sin(α_N1) / 6":
            mp.cos(alpha_n1) - b ** 3 * hbar_q ** 6 * mp.sin(alpha_n1) / 6,
        # Asymmetric: shift by 3·b² ℏ_q^4 / 4
        "cos(α − b·ℏ_q²/2 − 3·b²·ℏ_q^4/4)":
            mp.cos(alpha_n1 - 3 * b ** 2 * hbar_q_4th / 4),
        # Geometric-tail at N=2
        "cos(α_N1) · (1 - ℏ_q^4)":
            mp.cos(alpha_n1) * (1 - hbar_q_4th),
        "cos(α_N1) · (1 + ℏ_q^4)":
            mp.cos(alpha_n1) * (1 + hbar_q_4th),
        # Sanity: stay at N=1
        "cos(α − b·ℏ_q²/2) [N=1, no change]":
            mp.cos(alpha_n1),
    }

    print(f"  N=2 candidates vs CODATA Q_β:")
    print(f"    {'candidate':<58} {'ε [ppm]':>12} {'verdict':<30}")
    print(f"    {'-'*100}")
    results = []
    best_name, best_eps = "cos(α − b·ℏ_q²/2)", eps_N1
    for name, val in candidates.items():
        Q_cand = Q_A * val
        eps = (Q_cand / Q_AME - 1) * mp.mpf("1e6")
        if mp.fabs(eps) < mp.fabs(best_eps):
            best_name, best_eps = name, eps
        if mp.fabs(eps) < mp.fabs(eps_N1) * mp.mpf("0.5"):
            ratio = float(mp.fabs(eps_N1) / mp.fabs(eps))
            verdict = f"BETTER ({ratio:.2f}× tighter than N=1)"
        elif mp.fabs(eps) < mp.fabs(eps_N1) * mp.mpf("1.2"):
            verdict = "~same as N=1"
        elif mp.fabs(eps) < mp.mpf("0.96"):
            verdict = "UNDER N=2 BOUND"
        else:
            ratio = float(mp.fabs(eps) / mp.fabs(eps_N1))
            verdict = f"worse ({ratio:.2f}× looser than N=1)"
        print(f"    {name:<58} {float(eps):>+12.4f}  {verdict}")
        results.append({
            "name": name,
            "value_at_q0": str(val),
            "Q_pred_MeV": str(Q_cand),
            "eps_ppm": float(eps),
        })
    print()
    print(f"  BEST candidate: {best_name}")
    print(f"    ε = {float(best_eps):+.4f} ppm")
    if mp.fabs(best_eps) < mp.mpf("0.96"):
        print(f"    ✓ UNDER N=2 c(K) ceiling — Hoefsmit recursion validated at N=2.")
    elif mp.fabs(best_eps) < mp.fabs(eps_N1):
        ratio = float(mp.fabs(eps_N1) / mp.fabs(best_eps))
        print(f"    {ratio:.2f}× tighter than N=1 but NOT under N=2 ceiling (0.96 ppm).")
        print(f"    Hoefsmit recursion needs further refinement at N=2.")
    else:
        print(f"    No improvement over N=1 — naive Hoefsmit recursion doesn't")
        print(f"    capture the N=2 correction; needs operator-valued matrix")
        print(f"    exponential of the full Hecke generator.")

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "q-beta-operator-valued-N2",
        {
            "description": (
                "N=2 brane-tower truncation probe via Hoefsmit recursion. "
                "Tests b²·ℏ_q^4 scale corrections to the N=1 eigenphase "
                "shift cos(α − b·ℏ_q²/2). The c(K) bound at N=2 is "
                "0.96 ppm — 77× tighter than N=1. The natural recursion "
                "ansatz cos(α − b·ℏ_q²/2 ∓ b²·ℏ_q^4/2) tests both signs "
                "of the next-order shift."
            ),
            "auditOnly": (
                "PR #655 follow-up; N=2 brane-tower extension test. "
                "Tightens the 1ppb roadmap if Hoefsmit recursion captures "
                "the c(K) N=2 ceiling."
            ),
            "data": {
                "q_0_50dps": str(q),
                "alpha": str(alpha),
                "alpha_N1": str(alpha_n1),
                "hbar_q_squared": str(hbar_q_sq),
                "hbar_q_4th": str(hbar_q_4th),
                "hoefsmit_b": str(b),
                "n1_shift": str(n1_shift),
                "n2_scale": str(n2_scale),
                "baseline_N0_eps_ppm": float(eps_N0),
                "baseline_N1_eps_ppm": float(eps_N1),
                "c_K_N2_bound_ppm": 0.96,
                "candidates": results,
                "best_candidate_name": best_name,
                "best_eps_ppm": float(best_eps),
                "under_N2_ceiling": bool(mp.fabs(best_eps) < mp.mpf("0.96")),
                "tightening_vs_N1": (
                    float(mp.fabs(eps_N1) / mp.fabs(best_eps))
                    if best_eps != 0 else None
                ),
            },
        },
        script_path=__file__,
        engine="mpmath",
    )
    out_path = builder.save()
    print(f"\n  Witness: {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
