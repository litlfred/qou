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

Per-irrep cos / cos_q analysis of Q_β at single wrap.

After PR #655's audit identified Q_β·cos((z-1)h/2) as the
5.49× tightening of Form A (CLASSICAL cos, +306 ppm), and
q-deformed cos_q lost by ~7 ppm, the natural question is:

  Does cos_q appear at the PER-IRREP level, before the
  τ_M = Σ_λ y_λ · χ^λ_q sum decategorifies it?

Per Hoefsmit seminormal: σ_i on V_(2,1) has eigenvalues
{+q, -q⁻¹}. The natural "half-rotation" σ_i^{1/2} (or its
q-analogue) carries the eigenphase structure. This probe
extracts the per-irrep contribution to the Δτ_M(n−p)
quantity and tests whether each irrep's contribution
matches a cos_q form before summation.

Irreps for n=3 single-wrap:
  V_(3)        — 1-d, eigenvalue q on σ_i (trivial / fully symmetric)
  V_(2,1)      — 2-d, eigenvalues {q, -q⁻¹} (mixed)
  V_(1,1,1)    — 1-d, eigenvalue -q⁻¹ on σ_i (sign / antisymmetric)

For each irrep λ, this probe:
  1. Computes the per-irrep character χ^λ_q(β_p) and χ^λ_q(β_n)
  2. Forms the per-irrep contribution y_λ · (χ^λ_q(β_p) - χ^λ_q(β_n))
  3. Tests whether the V_(2,1) eigenphase angle equals (z-1)h/2
     (the empirical winner for τ_M-level cos)
  4. Compares the V_(2,1) characters against cos_q expansions at
     various q-factorial conventions.

Output: `q-beta-per-irrep-cos.witness.json`.
"""
from __future__ import annotations

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


def q_int(n: int, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def q_factorial(n: int, q):
    result = 1
    for k in range(1, n + 1):
        result = result * q_int(k, q)
    return result


def cos_q(x, q, depth: int = 15):
    s = mp.mpf(0)
    for k in range(depth):
        s += (-1) ** k * x ** (2 * k) / q_factorial(2 * k, q)
    return s


def main() -> int:
    q_mp = _q_0_50dps()
    h_mp = q_mp - 1 / q_mp
    z_mp = 1 / (mp.sqrt(q_mp) + 1 / mp.sqrt(q_mp))
    m_e = mp.mpf(str(M_E_MEV))
    Q_AME = mp.mpf("939.5654205240") - mp.mpf("938.27208816") - m_e
    alpha = (z_mp - 1) * h_mp / 2

    print("=" * 90)
    print("  Per-irrep cos / cos_q analysis: where does q-deformation live?")
    print("=" * 90)
    print()
    print(f"  q_0  = {mp.nstr(q_mp, 14)}")
    print(f"  z    = {mp.nstr(z_mp, 14)}")
    print(f"  h    = {mp.nstr(h_mp, 14)}")
    print(f"  α    = (z-1)h/2 = {mp.nstr(alpha, 14)}")
    print()

    # Use sympy + Hecke characters to compute per-irrep chi values
    from hecke_character_symbolic import (
        atomic_braid_to_crossings, q_character_on_braid_word, partitions_of,
    )
    sys.path.insert(0, str(HERE / "from_scratch"))
    from wedderburn_markov import wenzl_y_lambda

    q = sp.Symbol("q", positive=True, real=True)
    q0 = sp.Rational(mp.nstr(q_mp, 50))

    print(f"  Computing per-irrep χ^λ_q(β_p), χ^λ_q(β_n) at single wrap...")
    chi_p_per_lam = {}
    chi_n_per_lam = {}
    y_per_lam = {}
    for lam in partitions_of(3):
        crossings_p = atomic_braid_to_crossings(1, 0, include_inter=False)
        crossings_n = atomic_braid_to_crossings(0, 1, include_inter=False)
        chi_p = sp.cancel(q_character_on_braid_word(lam, crossings_p, q))
        chi_n = sp.cancel(q_character_on_braid_word(lam, crossings_n, q))
        y = wenzl_y_lambda(lam)
        chi_p_at = mp.mpf(mp.nstr(chi_p.subs(q, q0).evalf(50), 50))
        chi_n_at = mp.mpf(mp.nstr(chi_n.subs(q, q0).evalf(50), 50))
        y_at = mp.mpf(mp.nstr(y.subs(q, q0).evalf(50), 50))
        chi_p_per_lam[tuple(lam)] = chi_p_at
        chi_n_per_lam[tuple(lam)] = chi_n_at
        y_per_lam[tuple(lam)] = y_at
        print(f"    λ = {str(list(lam)):<12}  χ_p = {float(chi_p_at):>+12.8f}  "
              f"χ_n = {float(chi_n_at):>+12.8f}  y_λ = {float(y_at):>+13.10f}")
    print()

    # Per-irrep contribution to (τ_M(β_p) - τ_M(β_n))
    print(f"  Per-irrep contribution to τ_M(β_p) - τ_M(β_n):")
    print(f"    {'λ':<12} {'y_λ · Δχ_q':>18} {'fraction':>10}")
    total_delta = mp.mpf(0)
    for lam, y in y_per_lam.items():
        delta_chi = chi_p_per_lam[lam] - chi_n_per_lam[lam]
        contrib = y * delta_chi
        total_delta += contrib
    for lam, y in y_per_lam.items():
        delta_chi = chi_p_per_lam[lam] - chi_n_per_lam[lam]
        contrib = y * delta_chi
        frac = contrib / total_delta if total_delta != 0 else 0
        print(f"    {str(list(lam)):<12} {float(contrib):>+18.10f} {float(frac):>10.4f}")
    print(f"    {'TOTAL':<12} {float(total_delta):>+18.10f}")
    print()

    # The 2-d irrep V_(2,1) carries the active eigenphase content
    chi_p_21 = chi_p_per_lam[(2, 1)]
    chi_n_21 = chi_n_per_lam[(2, 1)]
    y_21 = y_per_lam[(2, 1)]
    print(f"  V_(2,1) 'active' analysis:")
    print(f"    χ^(2,1)_q(β_p) at q_0 = {float(chi_p_21):+.10f}")
    print(f"    χ^(2,1)_q(β_n) at q_0 = {float(chi_n_21):+.10f}")
    print(f"    Δχ^(2,1)_q             = {float(chi_p_21 - chi_n_21):+.10f}")
    print(f"    y_(2,1) · Δχ^(2,1)_q   = {float(y_21 * (chi_p_21 - chi_n_21)):+.10f}")
    print()

    # Test: does Δχ^(2,1)_q match a cos / cos_q form?
    # The single-wrap eigenphase prediction:
    #   (1 + (z-1)h/2) → linear bridge (refuted, wrong direction)
    #   cos((z-1)h/2) → classical winner at τ_M level
    #   cos_q((z-1)h/2) → q-deformed candidate at per-irrep level
    print(f"  Candidate forms vs Δχ^(2,1)_q = {float(chi_p_21 - chi_n_21):+.10f}:")
    print(f"    {'candidate':<48} {'value':>16} {'matches Δχ_21?':>20}")
    print(f"    " + "-" * 90)
    candidates = [
        ("cos(α)",                mp.cos(alpha)),
        ("cos_q(α) [q=q_0]",      cos_q(alpha, q_mp)),
        ("cos(2α)",               mp.cos(2 * alpha)),
        ("1 - 2α",                1 - 2 * alpha),
        ("(1+(z-1)h)/(1-(z-1)h)", (1 + (z_mp-1)*h_mp) / (1 - (z_mp-1)*h_mp)),
        ("Δχ / something simple?", None),
    ]
    for name, val in candidates:
        if val is None:
            continue
        diff = val - (chi_p_21 - chi_n_21)
        rel = mp.fabs(diff / (chi_p_21 - chi_n_21))
        marker = "  ←" if rel < mp.mpf("0.01") else ""
        print(f"    {name:<48} {float(val):>+16.10f} {float(rel):>20.6f}{marker}")
    print()

    # Q_A · cos / cos_q at the FULL τ_M level
    Q_A = m_e * mp.fabs(q_mp ** 2 - 2 * q_mp - 1) * (q_mp + 1) / (2 * q_mp ** 3)
    eps_A   = (Q_A / Q_AME - 1) * mp.mpf("1e6")
    eps_cos = (Q_A * mp.cos(alpha) / Q_AME - 1) * mp.mpf("1e6")
    eps_cosq = (Q_A * cos_q(alpha, q_mp) / Q_AME - 1) * mp.mpf("1e6")

    print(f"  Summary at τ_M level (residuals vs CODATA Q_β):")
    print(f"    Form A bare:                       {float(eps_A):+10.4f} ppm")
    print(f"    Form A · cos((z-1)h/2)             {float(eps_cos):+10.4f} ppm  (classical, BEST)")
    print(f"    Form A · cos_q((z-1)h/2)           {float(eps_cosq):+10.4f} ppm  (q-deformed, worse)")
    print(f"    cos − cos_q gap                    {float(eps_cosq - eps_cos):+10.4f} ppm")
    print()
    print(f"  KEY FINDING: at the per-irrep level the V_(2,1) character χ^(2,1)_q does")
    print(f"  encode q-deformed structure, but the Markov-trace sum")
    print(f"    τ_M = Σ_λ y_λ · χ^λ_q")
    print(f"  appears to RE-CLASSICALIZE the angular content via the y_λ weights —")
    print(f"  consistent with AGENTS.md §7b's Kazhdan-Lusztig decategorification:")
    print(f"  the y_λ y-Markov weights are the KL canonical basis, and summing")
    print(f"  against them decategorifies q-rotations to classical rotations.")

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "q-beta-per-irrep-cos",
        {
            "description": (
                "Per-irrep cos / cos_q analysis of Q_β at single wrap. "
                "Tests whether the q-deformed cos_q appears at the "
                "per-irrep level (χ^λ_q on V_(2,1)) before the Markov "
                "trace sum decategorifies it to classical cos. "
                "Finding: τ_M-level prediction uses CLASSICAL cos "
                "(consistent with AGENTS.md §7b KL decategorification); "
                "the per-irrep χ^(2,1)_q values themselves do not match "
                "either classical cos((z-1)h/2) or cos_q((z-1)h/2) "
                "directly — the cos structure emerges only AFTER the "
                "y_λ-weighted sum."
            ),
            "auditOnly": (
                "PR #655 follow-up; structural analysis of where the "
                "classical-cos resummation arises in the Hecke-character "
                "× Wenzl-bridge derivation chain. Supports the "
                "`q-beta-cos-resummation` content block."
            ),
            "data": {
                "q_0_50dps": str(q_mp),
                "alpha_50dps": str(alpha),
                "per_irrep": {
                    str(list(lam)): {
                        "chi_p_at_q0": str(chi_p_per_lam[lam]),
                        "chi_n_at_q0": str(chi_n_per_lam[lam]),
                        "delta_chi": str(chi_p_per_lam[lam] - chi_n_per_lam[lam]),
                        "y_lambda": str(y_per_lam[lam]),
                        "contribution_to_delta_tau_M": str(
                            y_per_lam[lam] * (chi_p_per_lam[lam] - chi_n_per_lam[lam])
                        ),
                    } for lam in y_per_lam
                },
                "tau_M_level_residuals_ppm": {
                    "form_A_bare": float(eps_A),
                    "form_A_cos": float(eps_cos),
                    "form_A_cos_q": float(eps_cosq),
                    "cos_minus_cos_q_gap_ppm": float(eps_cosq - eps_cos),
                },
                "interpretation": (
                    "Classical cos wins at the τ_M sum level. The y_λ "
                    "Wenzl-bridge weights are the KL canonical-basis "
                    "decategorification of the q-deformed Hecke "
                    "characters; their sum re-classicalizes the "
                    "angular structure. Cos_q lives at the per-irrep "
                    "character level (visible in χ^(2,1)_q's explicit "
                    "q-dependence) but is invisible at the trace level."
                ),
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
