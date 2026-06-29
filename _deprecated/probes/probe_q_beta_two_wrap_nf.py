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

Q_β 2-wrap NF counit extension probe.

PR #655's cos-resummation hit a 305 ppm floor at single wrap. The
remaining gap should live at 2-wrap (next brane-tower depth N=1).
This probe computes the NF counit AT 2-wrap (β² for both nucleons)
and tests whether the resulting Q_β prediction tightens further.

Single-wrap typed B_3 (from `prop:neutron-qvalue-symbolic`):
  proton:   σ_0 · (σ_1 - h/2·1)              net = 1 - h/2
  neutron:  (σ_0 - h/2·1) · (σ_1 - h·1)       net = 1 - 3h/2 + h²/2

2-wrap NF counit: apply the typed braid TWICE, then take the
counit (project to the H_3 identity component). Each square
involves Hecke-quadratic reductions σ_i² = (q - q⁻¹)σ_i + 1.

Strategy: use the symbolic q-character framework to compute
τ_M(β²) directly via χ^λ_q(β²) on each irrep, then form the
Markov-trace difference τ_M(β²_n) - τ_M(β²_p) and the
corresponding Q_β prediction.

Output: `q-beta-two-wrap-nf.witness.json`.
"""
from __future__ import annotations
from computations.substrate.codata_constants import M_N_MEV_VALIDATION, M_P_MEV_VALIDATION

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "from_scratch"))


from _precision import set_compute_dps, fmt  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps()


def _q_0_50dps() -> mp.mpf:
    with (HERE / "q-pinning-50-digit.witness.json").open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


def main() -> int:
    q0_mp = _q_0_50dps()
    m_e = mp.mpf(str(M_E_MEV))
    Q_AME = M_N_MEV_VALIDATION - M_P_MEV_VALIDATION - m_e

    h0 = q0_mp - 1 / q0_mp
    z0 = 1 / (mp.sqrt(q0_mp) + 1 / mp.sqrt(q0_mp))
    alpha = (z0 - 1) * h0 / 2

    print("=" * 96)
    print("  Q_β 2-wrap NF counit extension")
    print("=" * 96)
    print()
    print(f"  q_0  = {mp.nstr(q0_mp, 14)}")
    print(f"  h    = {mp.nstr(h0, 14)}")
    print(f"  z    = {mp.nstr(z0, 14)}")
    print(f"  α    = (z-1)h/2 = {mp.nstr(alpha, 14)}")
    print()

    # Compute single-wrap τ_M difference via canonical Hecke-character path
    from hecke_character_symbolic import (
        atomic_braid_to_crossings, q_character_on_braid_word, partitions_of,
    )
    from wedderburn_markov import wenzl_y_lambda

    q = sp.Symbol("q", positive=True, real=True)
    q0 = sp.Rational(mp.nstr(q0_mp, 50))

    # Single wrap (N=0)
    crossings_p_1 = atomic_braid_to_crossings(1, 0, include_inter=False)
    crossings_n_1 = atomic_braid_to_crossings(0, 1, include_inter=False)
    print(f"  Single-wrap braid lengths:")
    print(f"    β_p: {len(crossings_p_1)} crossings")
    print(f"    β_n: {len(crossings_n_1)} crossings")

    # 2-wrap (N=1): concatenate the braid word with itself
    crossings_p_2 = crossings_p_1 + crossings_p_1
    crossings_n_2 = crossings_n_1 + crossings_n_1
    print(f"  2-wrap braid lengths:")
    print(f"    β_p²: {len(crossings_p_2)} crossings")
    print(f"    β_n²: {len(crossings_n_2)} crossings")
    print()

    print(f"  Computing per-irrep χ^λ_q(β_k^n) at q_0...")
    results_by_wrap = {}
    for wrap_idx, (cp, cn) in [
        (1, (crossings_p_1, crossings_n_1)),
        (2, (crossings_p_2, crossings_n_2)),
    ]:
        chi_p, chi_n, y_lam = {}, {}, {}
        for lam in partitions_of(3):
            chi_p[tuple(lam)] = mp.mpf(mp.nstr(
                sp.cancel(q_character_on_braid_word(lam, cp, q)).subs(q, q0).evalf(50), 50))
            chi_n[tuple(lam)] = mp.mpf(mp.nstr(
                sp.cancel(q_character_on_braid_word(lam, cn, q)).subs(q, q0).evalf(50), 50))
            y_lam[tuple(lam)] = mp.mpf(mp.nstr(
                wenzl_y_lambda(lam).subs(q, q0).evalf(50), 50))

        tau_p = sum(y_lam[lam] * chi_p[lam] for lam in y_lam)
        tau_n = sum(y_lam[lam] * chi_n[lam] for lam in y_lam)
        delta_tau = tau_n - tau_p

        results_by_wrap[wrap_idx] = {
            "tau_M_proton": tau_p,
            "tau_M_neutron": tau_n,
            "delta_tau": delta_tau,
            "per_irrep": {
                str(list(lam)): {
                    "chi_p": str(chi_p[lam]),
                    "chi_n": str(chi_n[lam]),
                    "delta_chi": str(chi_p[lam] - chi_n[lam]),
                } for lam in y_lam
            },
        }
        print(f"  Wrap N={wrap_idx-1}:")
        print(f"    τ_M(β_p) = {float(tau_p):+.10f}")
        print(f"    τ_M(β_n) = {float(tau_n):+.10f}")
        print(f"    Δτ_M(n-p) = {float(delta_tau):+.10f}")
        print()

    # Tower-truncation: if the brane-tower expansion is
    #   τ_M^exact = Σ_N c_N τ_M^(N)
    # then the relationship between τ_M at N=0 and N=1 tells us about
    # the convergence rate. Specifically, the ratio
    #   Δτ_M(N=1) / Δτ_M(N=0)
    # should match the per-N decay ℏ_q² ≈ 0.0098 if the tower is a
    # simple geometric series, or some other structure otherwise.
    d_tau_0 = results_by_wrap[1]["delta_tau"]
    d_tau_1 = results_by_wrap[2]["delta_tau"]
    ratio_1_over_0 = d_tau_1 / d_tau_0 if d_tau_0 != 0 else None
    hbar_q = (q0_mp - 1) / q0_mp
    hbar_q_sq = hbar_q ** 2

    print(f"  Tower-truncation analysis:")
    print(f"    Δτ_M(N=0) = {float(d_tau_0):+.10f}")
    print(f"    Δτ_M(N=1) = {float(d_tau_1):+.10f}")
    if ratio_1_over_0 is not None:
        print(f"    Δτ_M(N=1) / Δτ_M(N=0) = {float(ratio_1_over_0):+.10f}")
        print(f"    ℏ_q² (geometric series rate) = {float(hbar_q_sq):+.10f}")
        deviation = mp.fabs(ratio_1_over_0 / hbar_q_sq - 1)
        print(f"    |ratio / ℏ_q² − 1| = {float(deviation):+.4f} → "
              f"{'NEAR geometric' if deviation < 0.05 else 'NOT geometric'}")
    print()

    # Q_β prediction: bridge identity gives Q_β = Form A · cos(α) at single wrap
    # At 2-wrap: try the natural ansatz Form A · cos(α) · (1 + correction term
    # from the 2-wrap Δτ_M)
    Q_A_single = m_e * mp.fabs(q0_mp ** 2 - 2 * q0_mp - 1) * (q0_mp + 1) / (2 * q0_mp ** 3)

    # Approach: derive the 2-wrap analogue of cos(α) by treating the
    # 2-wrap Δτ_M as encoding the next-order correction
    # Form A_2wrap = Form A · |Δτ_M(N=1) / Δτ_M(N=0)| ???
    # Or: derive via the bridge at 2-wrap

    # Direct test: 2-wrap Δτ_M ratio as direct correction factor
    candidates = {
        "Form A bare":                              Q_A_single,
        "Form A · cos((z-1)h/2)":                   Q_A_single * mp.cos(alpha),
        "Form A · cos(α) · (1 + Δτ_M(N=1)/2)":     Q_A_single * mp.cos(alpha) * (1 + d_tau_1 / 2),
        "Form A · cos(α) · (1 - Δτ_M(N=1)/2)":     Q_A_single * mp.cos(alpha) * (1 - d_tau_1 / 2),
        "Form A · cos(α + Δτ_M(N=1)/2)":           Q_A_single * mp.cos(alpha + d_tau_1 / 2),
        "Form A · cos(α - Δτ_M(N=1)/2)":           Q_A_single * mp.cos(alpha - d_tau_1 / 2),
        # The "deeper" expansion: cos at 2-wrap may involve cos(2α)
        "Form A · cos(2α)":                         Q_A_single * mp.cos(2 * alpha),
        "Form A · (cos(α) + ℏ_q² · cos(2α))":      Q_A_single * (mp.cos(alpha) + hbar_q_sq * mp.cos(2 * alpha)),
        "Form A · cos(α) · (1 + ℏ_q² · Δτ_M(N=1)/Δτ_M(N=0))":
            Q_A_single * mp.cos(alpha) * (1 + hbar_q_sq * (ratio_1_over_0 if ratio_1_over_0 else 0)),
        # Geometric resummation
        "Form A · cos(α) / (1 - ℏ_q² · cos(α))":   Q_A_single * mp.cos(alpha) / (1 - hbar_q_sq * mp.cos(alpha)),
    }

    print(f"  Residuals vs CODATA Q_β:")
    print(f"    {'candidate':<60} {'Q_β [MeV]':>14} {'ε [ppm]':>12}")
    print(f"    {'-'*92}")
    for name, val in candidates.items():
        eps = (val / Q_AME - 1) * mp.mpf("1e6")
        marker = " ←" if mp.fabs(eps) < 300 else ""
        print(f"    {name:<60} {float(val):>14.10f} {float(eps):>+12.4f}{marker}")
    print()

    print(f"  KEY FINDING:")
    print(f"    The 2-wrap Δτ_M differs from N=0 by factor {float(ratio_1_over_0):.4f}")
    print(f"    (if geometric, should equal ℏ_q² = {float(hbar_q_sq):.4f}).")
    print(f"    {'GEOMETRIC' if mp.fabs(ratio_1_over_0/hbar_q_sq - 1) < 0.05 else 'NOT GEOMETRIC'}")
    print(f"    — informs whether tower-truncation closed forms apply directly.")

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "q-beta-two-wrap-nf",
        {
            "description": (
                "Q_β 2-wrap (N=1 brane-tower depth) NF counit probe. "
                "Computes τ_M(β²_p) and τ_M(β²_n) at q_0 and tests "
                "whether the 2-wrap correction tightens Q_β beyond the "
                "single-wrap cos((z-1)h/2) form (PR #655's 306 ppm "
                "result). Per the c(K) bound at N=1: residual ceiling "
                "is 97 ppm — substantial room beyond cos resummation."
            ),
            "auditOnly": (
                "PR #655 follow-up. The 305 ppm cos-resummed residual "
                "must live at N≥1 brane-tower depth; this probe is the "
                "first direct compute at N=1."
            ),
            "data": {
                "q_0_50dps": str(q0_mp),
                "alpha_50dps": str(alpha),
                "hbar_q_squared": str(hbar_q_sq),
                "wrap_results": {
                    str(N): {k: str(v) if not isinstance(v, dict) else v
                            for k, v in r.items()}
                    for N, r in results_by_wrap.items()
                },
                "delta_tau_N1_over_N0": str(ratio_1_over_0) if ratio_1_over_0 else None,
                "is_geometric_with_hbar_q_sq": (
                    bool(mp.fabs(ratio_1_over_0 / hbar_q_sq - 1) < mp.mpf("0.05"))
                    if ratio_1_over_0 else None
                ),
                "candidates_residuals_ppm": {
                    name: float((val / Q_AME - 1) * mp.mpf("1e6"))
                    for name, val in candidates.items()
                },
            },
        },
        script_path=__file__,
        engine="sympy+mpmath",
    )
    out_path = builder.save()
    print(f"\n  Witness: {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
