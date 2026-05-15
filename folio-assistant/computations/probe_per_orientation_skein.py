#!/usr/bin/env python3
"""Probe: per-orientation Skein S(p), S(n) via Jones polynomial of typed B_3.

The Vol-form mass formula
  m(B) / m_e = Vol(ℬ_3) / ℏ_q² · λ_scale  +  S(B)
introduces a per-orientation Skein correction S(B) for each Borromean
baryon orientation partition (k positive, 3-k negative). The DIFFERENCE
ΔS(n - p) = S(n) - S(p) has been derived from CAL-1+CAL-2 alone via

  ΔS = (Q_β + m_e) / m_e / (Vol(ℬ_3)/ℏ_q²) ≈ 0.003391
                                              (1015 ppm vs target;
                                               algebraically locked to
                                               Q_β closed-form residual)

This probe computes the individual S(p), S(n) via the Jones polynomial
of the canonical 11-crossing typed B_3 braids:

  proton  (uud): atomic_braid_to_crossings(Z=1, N=0, include_inter=False)
                 {σ:6, σ⁻¹:3, averaged:2}
  neutron (udd): atomic_braid_to_crossings(Z=0, N=1, include_inter=False)
                 {σ:5, σ⁻¹:4, averaged:2}

For each typed braid β at q_0:
  - Compute Wenzl-bridge Markov trace τ_M(β) at q_0
  - Compute its difference τ_M(β_n) - τ_M(β_p)
  - Compare against ΔS_derived (Q_β-form)

The empirical S-targets are obtained by inverting the Vol-form mass
formula and using λ_scale_p_target, λ_scale_n_target from
`derive_m_baryon_volume_form.py`. Since λ_scale is currently open,
S(p) and S(n) individually are also open — the consistency check is
ONLY on the difference.

Output: `per-orientation-skein.witness.json`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from codata_constants import M_E_MEV, M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402

mp.mp.dps = 50

VOL_BORROMEAN = mp.mpf("7.32772475587766148235147121870981010907842498879866")


def _q_0_50dps() -> mp.mpf:
    with (HERE / "q-pinning-50-digit.witness.json").open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


def _direct_tau_M_at_q0(Z: int, N: int) -> mp.mpf:
    """τ_M(T_w(Z,N)) at q_0 via canonical_braid_to_crossings + Wenzl y_λ.

    Uses the typed atomic braid recipe with include_inter=False (free
    nucleon: 11-crossing typed B_3). The "averaged" crossings expand as
    σ_i - (q-q⁻¹)/2 · 1 in the operator-valued interface."""
    from hecke_character_symbolic import (
        atomic_braid_to_crossings, q_character_on_braid_word, partitions_of,
    )
    sys.path.insert(0, str(HERE / "from_scratch"))
    from wedderburn_markov import wenzl_y_lambda

    q = sp.Symbol("q", positive=True, real=True)
    # Carry the 50-dp value of q_0 into sympy via mp.nstr (full precision)
    # rather than float() which truncates to ~17 digits.
    q0 = sp.Rational(mp.nstr(_q_0_50dps(), 50))

    crossings = atomic_braid_to_crossings(Z, N, include_inter=False)
    total = sp.Integer(0)
    per_lam = []
    for lam in partitions_of(3):
        chi = q_character_on_braid_word(lam, crossings, q)
        y = wenzl_y_lambda(lam)
        chi_at_q0_50 = sp.cancel(chi).subs(q, q0).evalf(50)
        y_at_q0_50   = y.subs(q, q0).evalf(50)
        total = total + y * chi
        per_lam.append({
            "partition": list(lam),
            "chi_at_q0":         str(chi_at_q0_50),
            "y_lambda_at_q0":    str(y_at_q0_50),
            "contrib_at_q0":     str(chi_at_q0_50 * y_at_q0_50),
        })
    total_at_q0_50 = sp.cancel(total).subs(q, q0).evalf(50)
    return mp.mpf(mp.nstr(total_at_q0_50, 50)), per_lam


def main() -> int:
    q = _q_0_50dps()
    hbar_q = (q - 1) / q
    hbar_q2 = hbar_q ** 2
    V = VOL_BORROMEAN / hbar_q2

    m_e = mp.mpf(str(M_E_MEV))
    m_p = mp.mpf(str(M_P_MEV_VALIDATION))
    m_n = mp.mpf(str(M_N_MEV_VALIDATION))

    print("=" * 78)
    print("  Per-orientation Skein corrections S(p), S(n) via τ_M(typed B_3)")
    print("=" * 78)
    print()
    print(f"  q_0 = {mp.nstr(q, 14)}")
    print(f"  Vol(ℬ_3)/ℏ_q² = {mp.nstr(V, 14)}")
    print()

    print(f"  Computing τ_M for typed B_3 (Wenzl-bridge × q-character)...")
    tau_M_p, p_breakdown = _direct_tau_M_at_q0(Z=1, N=0)
    tau_M_n, n_breakdown = _direct_tau_M_at_q0(Z=0, N=1)
    print(f"    τ_M(β_p, 11-cross typed B_3) at q_0 = {mp.nstr(tau_M_p, 14)}")
    print(f"    τ_M(β_n, 11-cross typed B_3) at q_0 = {mp.nstr(tau_M_n, 14)}")
    print()
    print(f"  Per-partition χ × y_λ breakdown:")
    print(f"    {'λ':<12} {'χ(β_p)':>12} {'χ(β_n)':>12} {'y_λ':>14} {'contrib_p':>12} {'contrib_n':>12}")
    for bp, bn in zip(p_breakdown, n_breakdown):
        print(f"    {str(bp['partition']):<12} {float(bp['chi_at_q0']):>+12.6f} "
              f"{float(bn['chi_at_q0']):>+12.6f} {float(bp['y_lambda_at_q0']):>+14.10f} "
              f"{float(bp['contrib_at_q0']):>+12.6f} {float(bn['contrib_at_q0']):>+12.6f}")
    print()

    delta_tau_M = tau_M_n - tau_M_p
    print(f"  Δτ_M(n − p) = {mp.nstr(delta_tau_M, 14)}")

    # Empirical Skein difference target
    delta_S_target = (m_n - m_p) / m_e / V
    print(f"  ΔS empirical (m_n - m_p)/m_e / V = {mp.nstr(delta_S_target, 14)}")
    print()

    # Direct comparison: does Δτ_M match ΔS_target?
    rel_err_direct = (delta_tau_M - delta_S_target) / delta_S_target
    print(f"  Δτ_M / ΔS_target − 1 = {mp.nstr(rel_err_direct, 8)} "
          f"({mp.nstr(rel_err_direct * 100, 6)} %)")
    if mp.fabs(rel_err_direct) < mp.mpf("0.01"):
        print(f"  ✓ Δτ_M and ΔS_target agree at <1%.")
    else:
        print(f"  ✗ Δτ_M and ΔS_target differ by {float(rel_err_direct * 100):.2f}%; "
              f"raw τ_M is NOT directly the Skein S.")
    print()

    # Try a normalisation: scaled τ_M (dimensionless candidates)
    candidates = {
        "tau_M":                  (tau_M_n - tau_M_p),
        "tau_M / hbar_q":         (tau_M_n - tau_M_p) / hbar_q,
        "tau_M * hbar_q":         (tau_M_n - tau_M_p) * hbar_q,
        "tau_M / V":              (tau_M_n - tau_M_p) / V,
        "tau_M * hbar_q^2":       (tau_M_n - tau_M_p) * hbar_q2,
        "tau_M * hbar_q^2 / V":   (tau_M_n - tau_M_p) * hbar_q2 / V,
        "tau_M / (m_e/m_e_unit)": (tau_M_n - tau_M_p),  # already dimensionless
    }
    print(f"  Normalization candidates for ΔS = (n − p):")
    print(f"    {'candidate':<30} {'value':>16} {'target':>16} {'rel.err':>14}")
    print(f"    {'-'*78}")
    for name, val in candidates.items():
        rel = (val - delta_S_target) / delta_S_target
        print(f"    {name:<30} {mp.nstr(val, 10):>16} "
              f"{mp.nstr(delta_S_target, 10):>16} "
              f"{mp.nstr(rel, 6):>14}")
    print()

    # Even simpler: what's the multiplicative factor that maps Δτ_M → ΔS_target?
    if delta_tau_M != 0:
        normalisation_to_ΔS = delta_S_target / delta_tau_M
        print(f"  Multiplicative factor from Δτ_M to ΔS_target:")
        print(f"    f = ΔS_target / Δτ_M = {mp.nstr(normalisation_to_ΔS, 14)}")
        # Check if f matches obvious substrate quantities
        substrate_candidates = {
            "1":               mp.mpf(1),
            "ℏ_q":             hbar_q,
            "ℏ_q²":            hbar_q2,
            "1/V":             1 / V,
            "ℏ_q² / V":        hbar_q2 / V,
            "ℏ_q / V":         hbar_q / V,
            "ℏ_q · V":         hbar_q * V,
            "(q-1)":           q - 1,
            "(q-1)²":          (q - 1) ** 2,
            "1/V/m_e":         1 / V / m_e,
        }
        print(f"    Substrate candidates for f:")
        print(f"      {'candidate':<20} {'value':>16} {'f-ratio':>14}")
        for name, val in substrate_candidates.items():
            ratio = val / normalisation_to_ΔS
            marker = "  ←" if mp.fabs(ratio - 1) < mp.mpf("0.05") else ""
            print(f"      {name:<20} {mp.nstr(val, 10):>16} "
                  f"{mp.nstr(ratio, 6):>14}{marker}")
    print()

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "per-orientation-skein",
        {
            "description": (
                "Probe of per-orientation Skein corrections S(p), S(n) via "
                "the Jones / Wenzl-bridge Markov trace τ_M of the canonical "
                "11-crossing typed B_3 braids. Verifies whether the "
                "difference τ_M(β_n) - τ_M(β_p) matches the substrate-"
                "derived ΔS(n-p) = (Q_β + m_e)/m_e / (Vol(ℬ_3)/ℏ_q²). "
                "If yes (within ε): τ_M IS the Skein correction; ΔS chain "
                "validated by independent symbolic path. If no: the Skein "
                "correction is a different functional of the typed braid."
            ),
            "data": {
                "q_0_50dps": str(q),
                "Vol_Borromean_over_hbar_q_squared": str(V),
                "tau_M_proton_typed_B3_at_q0":  str(tau_M_p),
                "tau_M_neutron_typed_B3_at_q0": str(tau_M_n),
                "delta_tau_M_n_minus_p":        str(delta_tau_M),
                "delta_S_target":               str(delta_S_target),
                "rel_err_delta_tau_M_vs_target": str(rel_err_direct),
                "normalization_factor_target_over_tau_M": (
                    str(delta_S_target / delta_tau_M) if delta_tau_M != 0 else None
                ),
                "proton_per_lambda":  p_breakdown,
                "neutron_per_lambda": n_breakdown,
            },
        },
        script_path=__file__,
        engine="sympy+mpmath",
    )
    out_path = builder.save()
    print(f"  Witness: {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
