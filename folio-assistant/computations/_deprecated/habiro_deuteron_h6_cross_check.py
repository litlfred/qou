#!/usr/bin/env python3
"""Habiro correction tower for the DEUTERON at H_6 (n=6, p(6)=11).

Cross-checks whether the proton pattern
    S = hab_sum / (tr_M × Plancherel × Vol/ℏ²) ≈ (1+ℏ²)(1−ℏ²/p(n))
is universal — i.e. whether the deuteron at H_6 uses p(6)=11 the
same way the proton at H_9 uses p(9)=30.

The proton's S ≈ 1.009 — near 1 — so ℏ² corrections close the gap.
This script tests whether the same normalization brings the deuteron
near 1, and whether the Pochhammer bridge ratio hab_A/hab_B has a
parallel correction structure.
"""
from __future__ import annotations
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402
except ImportError:
    from qou_substrate.constants import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402


def q_factorial(n, q):
    """[n]_q! = prod_{k=1}^{n} [k]_q."""
    result = mp.mpf(1)
    for k in range(1, n + 1):
        result *= (q**k - q**(-k)) / (q - 1/q)
    return result


def q_integer(k, q):
    """[k]_q = (q^k - q^{-k}) / (q - q^{-1})."""
    return (q**k - q**(-k)) / (q - 1/q)


def poch_qq(m, q):
    """(q;q)_m = prod_{k=1}^{m} (1 - q^k)."""
    p = mp.mpf(1)
    for k in range(1, m + 1):
        p *= (1 - q**k)
    return p


def poch_uu(m, u):
    """(u;u)_m = prod_{k=1}^{m} (1 - u^k)."""
    p = mp.mpf(1)
    for k in range(1, m + 1):
        p *= (1 - u**k)
    return p


def eval_poly_u(expr_str, u_val):
    """Evaluate a polynomial expression string in u at u_val."""
    ns = {"u": u_val, "__builtins__": {}}
    return mp.mpf(eval(expr_str, ns))  # noqa: S307


def main():
    _t0 = time.perf_counter()
    set_compute_dps()

    q = mp.mpf(Q_50_DIGIT_STR)
    u = mp.sqrt(q)
    hbar_q = (q - 1) / q
    eps = hbar_q**2

    n_deut = 6       # Hecke level for deuteron
    p_deut = 11      # p(6) = number of partitions of 6
    n_prot = 9       # Hecke level for proton
    p_prot = 30      # p(9) = number of partitions of 9

    vol = vol_4_1_at(mp.mp.dps)
    vol_over_hsq = vol / eps

    # ------------------------------------------------------------------
    # 1. Load coefficients
    # ------------------------------------------------------------------
    with open(HERE / "habiro-coefficients-atomic.witness.json") as f:
        witness_data = json.load(f)
    deut = witness_data["results"]["D (deuteron, A=2)"]
    prot = witness_data["results"]["p (proton, A=1)"]

    print("=" * 70)
    print("  Deuteron Habiro correction tower -- H_6 cross-check")
    print("=" * 70)
    print()
    print(f"  q_0  = {mp.nstr(q, 15)}")
    print(f"  u_0  = sqrt(q_0) = {mp.nstr(u, 15)}")
    print(f"  h^2  = {mp.nstr(eps, 15)}")
    print()

    # ------------------------------------------------------------------
    # 2. Compute hab_A (q;q) and hab_B (u;u) for BOTH species
    # ------------------------------------------------------------------
    def compute_hab(species_data):
        coeffs = species_data["habiro_coefficients"]
        hA = mp.mpf(0)
        hB = mp.mpf(0)
        for entry in coeffs:
            m = entry["m"]
            a_val = eval_poly_u(entry["a_m"], u)
            hA += a_val * poch_qq(m, q)
            hB += a_val * poch_uu(m, u)
        denom_val = eval_poly_u(species_data["denom_in_u"], u)
        trM = hB / denom_val
        return hA, hB, denom_val, trM

    hab_A_d, hab_B_d, denom_d, tr_M_d = compute_hab(deut)
    hab_A_p, hab_B_p, denom_p, tr_M_p = compute_hab(prot)

    # ------------------------------------------------------------------
    # Print deuteron coefficient table
    # ------------------------------------------------------------------
    print(f"  Deuteron coefficients (n={n_deut}, p(n)={p_deut}):")
    print(f"  {'m':>2s}  {'a_m(u_0)':>14s}  {'(q;q)_m':>14s}  {'(u;u)_m':>14s}")
    print(f"  {'--':>2s}  {'-'*14}  {'-'*14}  {'-'*14}")
    for entry in deut["habiro_coefficients"]:
        m = entry["m"]
        a_val = eval_poly_u(entry["a_m"], u)
        print(f"  {m:>2d}  {float(a_val):>14.2f}  {float(poch_qq(m, q)):>14.6e}"
              f"  {float(poch_uu(m, u)):>14.6e}")
    print()

    # ------------------------------------------------------------------
    # 3. Bridge and S for both species
    # ------------------------------------------------------------------
    bridge_d = hab_A_d * denom_d / hab_B_d
    bridge_p = hab_A_p * denom_p / hab_B_p
    poch_ratio_d = hab_A_d / hab_B_d
    poch_ratio_p = hab_A_p / hab_B_p

    planck_d = mp.factorial(n_deut) / q_factorial(n_deut, q)
    planck_p = mp.factorial(n_prot) / q_factorial(n_prot, q)

    S_d = hab_A_d / (tr_M_d * planck_d * vol_over_hsq)
    S_p = hab_A_p / (tr_M_p * planck_p * vol_over_hsq)

    print("-" * 70)
    print("  Side-by-side: proton vs deuteron")
    print("-" * 70)
    print()
    print(f"  {'Quantity':<35s} {'Proton (H_9)':>18s} {'Deuteron (H_6)':>18s}")
    print(f"  {'-'*35} {'-'*18} {'-'*18}")
    print(f"  {'hab_A (q;q convention)':<35s} {float(hab_A_p):>18.4f} {float(hab_A_d):>18.4f}")
    print(f"  {'hab_B (u;u convention)':<35s} {float(hab_B_p):>18.4f} {float(hab_B_d):>18.4f}")
    print(f"  {'denom_in_u':<35s} {float(denom_p):>18.4f} {float(denom_d):>18.4f}")
    print(f"  {'tr_M = hab_B / denom':<35s} {float(tr_M_p):>18.6f} {float(tr_M_d):>18.6f}")
    print(f"  {'Pochhammer ratio hab_A/hab_B':<35s} {float(poch_ratio_p):>18.6f} {float(poch_ratio_d):>18.6f}")
    print(f"  {'bridge = hab_A * denom / hab_B':<35s} {float(bridge_p):>18.4f} {float(bridge_d):>18.4f}")
    print(f"  {'Plancherel n!/[n]_q!':<35s} {float(planck_p):>18.6f} {float(planck_d):>18.6f}")
    print(f"  {'S = hab_A / (tr_M*Planck*Vol/h^2)':<35s} {float(S_p):>18.6f} {float(S_d):>18.6f}")
    print()

    correction_p = (1 + eps) * (1 - eps / p_prot)
    residual_p = float(S_p / correction_p - 1) * 1e6

    print(f"  Proton:   S = {mp.nstr(S_p, 12)} ~ 1 + O(h^2)")
    print(f"            (1+h^2)(1-h^2/30) residual: {residual_p:.1f} ppm")
    print()
    print(f"  Deuteron: S = {mp.nstr(S_d, 12)} >> 1")
    print(f"            The normalization tr_M * Plancherel * Vol/h^2 does NOT")
    print(f"            bring the deuteron near 1.  The (1+h^2)(1-h^2/p(n))")
    print(f"            tower is inapplicable at this normalization.")
    print()

    # ------------------------------------------------------------------
    # 4. Pochhammer bridge analysis (convention-independent)
    # ------------------------------------------------------------------
    # For both species: hab_A/hab_B = <prod(1+u^k)>_Habiro
    # This is the pure Pochhammer convention ratio.
    # For proton: 5.616; for deuteron: 27.234
    # Can we express these as a (1+eps) tower?

    print("-" * 70)
    print("  Pochhammer bridge ratio analysis")
    print("-" * 70)
    print()
    print(f"  hab_A/hab_B = <prod(1+u^k)>_Habiro  (weighted avg over coefficients)")
    print()

    # Compute the raw product prod_{k=1}^{M}(1+u^k) for max coefficient order
    max_m_d = max(c["m"] for c in deut["habiro_coefficients"])
    max_m_p = max(c["m"] for c in prot["habiro_coefficients"])

    prod_1_plus_uk_d = mp.mpf(1)
    for k in range(1, max_m_d + 1):
        prod_1_plus_uk_d *= (1 + u**k)

    prod_1_plus_uk_p = mp.mpf(1)
    for k in range(1, max_m_p + 1):
        prod_1_plus_uk_p *= (1 + u**k)

    print(f"  Proton:   prod(1+u^k, k=1..{max_m_p}) = {mp.nstr(prod_1_plus_uk_p, 12)}")
    print(f"            hab_A/hab_B                 = {mp.nstr(poch_ratio_p, 12)}")
    print(f"  Deuteron: prod(1+u^k, k=1..{max_m_d}) = {mp.nstr(prod_1_plus_uk_d, 12)}")
    print(f"            hab_A/hab_B                 = {mp.nstr(poch_ratio_d, 12)}")
    print()

    # The weighted average differs from the raw product because higher-m
    # terms have larger products but smaller weights (a_m * (u;u)_m).

    # ------------------------------------------------------------------
    # 5. Test (1+h^2)(1-h^2/p(n)) on the Pochhammer ratio
    # ------------------------------------------------------------------
    # For the proton:  poch_ratio = 5.616, log2(poch_ratio) ~ 2.49
    # For the deuteron: poch_ratio = 27.234
    # These are not near 1, so the additive tower doesn't apply either.
    # But the RATIO of poch_ratios might be interesting.

    print("-" * 70)
    print("  Ratio of Pochhammer bridges: deuteron / proton")
    print("-" * 70)
    print()

    cross_ratio = poch_ratio_d / poch_ratio_p
    print(f"  (hab_A/hab_B)_D / (hab_A/hab_B)_p = {mp.nstr(cross_ratio, 15)}")
    print()

    # Test if this is near a power of (1+u^k) factors
    # Since deut has m up to 12 and proton has m up to max_m_p,
    # the ratio might reflect the extra (1+u^k) factors.
    prod_extra = mp.mpf(1)
    for k in range(max_m_p + 1, max_m_d + 1):
        prod_extra *= (1 + u**k)
    print(f"  Extra (1+u^k) factors for k={max_m_p+1}..{max_m_d}: {mp.nstr(prod_extra, 12)}")
    print(f"  (This does not explain the ratio since max_m_d <= max_m_p.)")
    print()

    # ------------------------------------------------------------------
    # 6. Direct correction tower on S_deut (how far from 1?)
    # ------------------------------------------------------------------
    print("-" * 70)
    print("  Direct tower analysis for deuteron S")
    print("-" * 70)
    print()

    # S_d = 371.75. What integer N satisfies S_d ~ N?
    S_d_int = int(round(float(S_d)))
    frac_part = S_d - S_d_int
    print(f"  S_deut = {mp.nstr(S_d, 15)}")
    print(f"  Nearest integer: {S_d_int}")
    print(f"  Fractional part: {mp.nstr(frac_part, 12)}")
    print(f"  S_deut / S_proton = {mp.nstr(S_d / S_p, 12)}")
    print()

    # What if S_d = S_p * (denom_d/denom_p) * (planck_p/planck_d)?
    # S_d/S_p = (hab_A_d * tr_M_p * planck_p) / (hab_A_p * tr_M_d * planck_d)
    ratio_S = S_d / S_p
    expected_ratio = (denom_d / denom_p) * (planck_p / planck_d) * (poch_ratio_d / poch_ratio_p)
    print(f"  S_d/S_p = {mp.nstr(ratio_S, 12)}")
    print(f"  = (denom_d/denom_p) * (Planck_p/Planck_d) * (poch_d/poch_p)")
    print(f"  = {mp.nstr(denom_d/denom_p, 8)} * {mp.nstr(planck_p/planck_d, 8)} "
          f"* {mp.nstr(poch_ratio_d/poch_ratio_p, 8)}")
    print(f"  = {mp.nstr(expected_ratio, 12)}")
    print()

    # ------------------------------------------------------------------
    # 7. Search: is there an A-dependent normalization that brings S ~ 1?
    # ------------------------------------------------------------------
    print("-" * 70)
    print("  Normalization search: what factor brings S_deut near 1?")
    print("-" * 70)
    print()

    # S_d ~ 372. We need an extra factor of ~372 in the denominator.
    # Candidates: a0_d = 32, denom_d/denom_p, A-factorials, etc.
    a0_d = eval_poly_u(deut["habiro_coefficients"][0]["a_m"], u)
    a0_p = eval_poly_u(prot["habiro_coefficients"][0]["a_m"], u)

    norm_candidates = [
        ("a0_d / a0_p = 32/4 = 8", a0_d / a0_p),
        ("denom_d / denom_p", denom_d / denom_p),
        ("S_d (exact)", S_d),
        ("poch_ratio_d / poch_ratio_p", poch_ratio_d / poch_ratio_p),
        ("S_d / S_p", S_d / S_p),
    ]

    print(f"  {'Factor':<40s} {'Value':>14s} {'S_d/factor':>14s}")
    print(f"  {'-'*40} {'-'*14} {'-'*14}")
    for name, val in norm_candidates:
        print(f"  {name:<40s} {float(val):>14.4f} {float(S_d/val):>14.6f}")
    print()

    # ------------------------------------------------------------------
    # 8. Conclusion
    # ------------------------------------------------------------------
    print("=" * 70)
    print("  CONCLUSION: p(n) UNIVERSALITY")
    print("=" * 70)
    print()
    print("  The proton correction tower works because")
    print(f"    S_p = hab_A / (tr_M * Planck_9 * Vol/h^2) = {mp.nstr(S_p, 10)}")
    print("  is within O(h^2) of 1, enabling the product expansion")
    print("    S ~ (1+h^2)(1-h^2/30)(1+h^2/1260)")
    print()
    print("  For the deuteron:")
    print(f"    S_d = hab_A / (tr_M * Planck_6 * Vol/h^2) = {mp.nstr(S_d, 10)}")
    print("  is ~372, not near 1.")
    print()
    print("  The normalization tr_M * Plancherel * Vol/h^2 is proton-specific.")
    print("  The (1+h^2)(1-h^2/p(n)) correction tower is NOT directly")
    print("  universal across isotopes at the same normalization.")
    print()
    print("  The Pochhammer bridge (hab_A/hab_B) is structurally present")
    print(f"  for both species (proton: {mp.nstr(poch_ratio_p, 8)}, "
          f"deuteron: {mp.nstr(poch_ratio_d, 8)}),")
    print("  but the overall scale requires an A-dependent normalization")
    print("  factor to bring S near 1 before the tower can be tested.")
    print()

    # ------------------------------------------------------------------
    # Witness
    # ------------------------------------------------------------------
    w = WitnessBuilder("habiro-deuteron-h6-cross-check", engine="mpmath", start_time=_t0)
    w.set_description(
        f"Deuteron Habiro correction tower at H_{n_deut} (n={n_deut}, p({n_deut})={p_deut}). "
        f"The proton normalization tr_M*Plancherel*Vol/h^2 gives S_p={mp.nstr(S_p, 6)} ~ 1, "
        f"but S_d={mp.nstr(S_d, 6)} >> 1. The (1+h^2)(1-h^2/p(n)) tower is proton-specific "
        f"at this normalization. Pochhammer bridge ratio present for both species "
        f"(proton: {mp.nstr(poch_ratio_p, 6)}, deuteron: {mp.nstr(poch_ratio_d, 6)}), "
        f"but A-dependent normalization needed to bring deuteron near 1."
    )
    w.add_data("isotope", "deuteron")
    w.add_data("hecke_level_deuteron", n_deut)
    w.add_data("hecke_level_proton", n_prot)
    w.add_data("partition_number_deuteron", p_deut)
    w.add_data("partition_number_proton", p_prot)
    w.add_data("hab_A_qq_deuteron", str(mp.nstr(hab_A_d, 20)))
    w.add_data("hab_B_uu_deuteron", str(mp.nstr(hab_B_d, 20)))
    w.add_data("hab_A_qq_proton", str(mp.nstr(hab_A_p, 20)))
    w.add_data("hab_B_uu_proton", str(mp.nstr(hab_B_p, 20)))
    w.add_data("denom_deuteron", str(mp.nstr(denom_d, 15)))
    w.add_data("denom_proton", str(mp.nstr(denom_p, 15)))
    w.add_data("tr_M_deuteron", str(mp.nstr(tr_M_d, 15)))
    w.add_data("tr_M_proton", str(mp.nstr(tr_M_p, 15)))
    w.add_data("pochhammer_ratio_deuteron", str(mp.nstr(poch_ratio_d, 15)))
    w.add_data("pochhammer_ratio_proton", str(mp.nstr(poch_ratio_p, 15)))
    w.add_data("bridge_deuteron", str(mp.nstr(bridge_d, 15)))
    w.add_data("bridge_proton", str(mp.nstr(bridge_p, 15)))
    w.add_data("S_deuteron", str(mp.nstr(S_d, 15)))
    w.add_data("S_proton", str(mp.nstr(S_p, 15)))
    w.add_data("S_deuteron_over_S_proton", str(mp.nstr(S_d / S_p, 12)))
    w.add_data("proton_correction_residual_ppm", residual_p)
    w.add_data("universality_result",
               "NEGATIVE: (1+h^2)(1-h^2/p(n)) tower is proton-specific at "
               "tr_M*Plancherel*Vol/h^2 normalization. Deuteron S >> 1.")

    # The key finding: S_d >> 1 means the tower is inapplicable
    w.add_assertion("proton_S_near_1",
                    computed=float(abs(S_p - 1) < 0.02),
                    expected=1, tolerance=0,
                    source="Proton S is within 2% of 1 (tower applicable)")
    w.add_assertion("deuteron_S_not_near_1",
                    computed=float(abs(S_d - 1) > 1),
                    expected=1, tolerance=0,
                    source="Deuteron S is far from 1 (tower inapplicable)")
    w.add_assertion("pochhammer_bridge_structural",
                    computed=float(poch_ratio_d > 1 and poch_ratio_p > 1),
                    expected=1, tolerance=0,
                    source="Pochhammer bridge hab_A/hab_B > 1 for both species")

    witness_path = w.save()
    print(f"  Witness: {witness_path}")


if __name__ == "__main__":
    main()
