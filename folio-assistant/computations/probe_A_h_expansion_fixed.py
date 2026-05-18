#!/usr/bin/env python3
"""Test the claim: A((4-q)/(4q+3)) = 5/2 - h²·G + O(h^4).

CRITICAL INSIGHT: the production `cubic_roots(z)` and
`sw_3root_product_degree1(z)` have coefficients depending ONLY on z,
not on q. So A(a) is a q-INDEPENDENT function of a.

The h-expansion comes ENTIRELY from how a_post_hoc(q) = (4-q)/(4q+3)
varies with q. We can expand:

  A(a_post_hoc(q)) = A(a_*) + (a_post_hoc(q) - a_*) · A'(a_*) + ...
                   = A(3/7) + Δa · A'(3/7) + (Δa)²/2 · A''(3/7) + ...

where a_* = a_post_hoc(q=1) = 3/7. So:

  c_0 = A(3/7)
  c_2 = ? (computed from chain-rule expansion of Δa in h²)

If A(3/7) = 5/2, this would PROVE the leading term.
If A(3/7) ≠ 5/2, the entire conjecture fails at the leading order.

Cleanest test: compute A(3/7) numerically.
"""
import sys
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy import integrate

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from picard_lefschetz_thimble import cubic_roots, sw_3root_product_degree1
from witness_base import WitnessBuilder


def integrand_baryon(z):
    return float(np.real(sw_3root_product_degree1(z)))


def integrand_electron(z):
    cs = cubic_roots(z)
    c = cs[np.argmin(np.abs(cs.imag))]
    return float(np.real(c + z))


def A_of(a_val):
    e_ref, _ = integrate.quad(integrand_electron, -a_val, a_val, limit=200)
    prod, _ = integrate.quad(integrand_baryon, -a_val, a_val, limit=200)
    return abs(prod) / abs(e_ref) if abs(e_ref) > 1e-15 else float("nan")


def main():
    G = float(mp.catalan)

    print("Test: A(a_post_hoc(q=1)) = 5/2 ?")
    print()

    # At q = 1: h = 0, so a_post_hoc(1) = (4-1)/(4+3) = 3/7
    a_at_q1 = 3.0 / 7.0
    A_at_q1 = A_of(a_at_q1)
    print(f"  a_post_hoc(q=1) = 3/7 = {a_at_q1:.10f}")
    print(f"  A(3/7) = {A_at_q1:.10f}")
    print(f"  5/2 = 2.5")
    print(f"  diff: {A_at_q1 - 2.5:+.6f}  ({(A_at_q1-2.5)/2.5*100:+.3f}%)")
    print()

    if abs(A_at_q1 - 2.5) > 0.01:
        print(f"  ❌ A(3/7) ≠ 5/2 — conjecture FAILS at leading order")
        print(f"     The h^0 coefficient is {A_at_q1:.4f}, not 5/2.")
    else:
        print(f"  ✓ A(3/7) ≈ 5/2 — leading-order match!")
    print()

    # Sample at various q to get the full h-expansion
    print("Sample A(a_post_hoc(q)) at multiple q values:")
    q_vals = np.array([1.0001, 1.001, 1.005, 1.01, 1.02, 1.05, 1.08,
                       1.1099785956, 1.15, 1.2])
    h_vals = q_vals - 1.0/q_vals
    print(f"  {'q':>10s}  {'h':>10s}  {'a_post_hoc':>12s}  {'A':>12s}")
    A_vals = []
    for q in q_vals:
        a_phoc = (4 - q) / (4*q + 3)
        if not (0 < a_phoc < 1/(np.sqrt(q) + np.sqrt(1/q))):
            print(f"  {q:>10.4f}  {q-1/q:>10.5f}  {a_phoc:>12.6f}  out of range")
            A_vals.append(float('nan'))
            continue
        A = A_of(a_phoc)
        A_vals.append(A)
        print(f"  {q:>10.4f}  {q-1/q:>10.5f}  {a_phoc:>12.6f}  {A:>12.6f}")
    print()
    A_vals = np.array(A_vals)
    h_vals_arr = q_vals - 1.0/q_vals
    h2 = h_vals_arr**2

    # Fit polynomial in h² (excluding NaN)
    valid = ~np.isnan(A_vals)
    if valid.sum() >= 3:
        for degree in [1, 2, 3]:
            coeffs = np.polyfit(h2[valid], A_vals[valid], degree)
            c_0 = coeffs[-1]
            c_2 = coeffs[-2] if len(coeffs) >= 2 else None
            c_4 = coeffs[-3] if len(coeffs) >= 3 else None
            print(f"Degree {degree} polynomial in h² fit:")
            print(f"  c_0 = {c_0:.10f}  (target 5/2 = 2.5, Δ = {c_0 - 2.5:+.6f})")
            if c_2 is not None:
                print(f"  c_2 = {c_2:.10f}  (target -G = {-G:.6f}, Δ = {c_2 - (-G):+.6f})")
            if c_4 is not None:
                print(f"  c_4 = {c_4:.10f}")
            print()

    print("=" * 70)
    print("VERDICT")
    print("=" * 70)
    # If c_0 ≈ 5/2 and c_2 ≈ -G, the claim is verified
    coeffs_lin = np.polyfit(h2[valid], A_vals[valid], 1)
    c_2_fit, c_0_fit = coeffs_lin[0], coeffs_lin[1]
    print(f"Linear h² fit:")
    print(f"  c_0 = {c_0_fit:.8f}")
    print(f"  c_2 = {c_2_fit:.8f}")
    print(f"  conjecture: c_0 = 5/2 = 2.5,  c_2 = -G = {-G:.6f}")
    print()
    leading_match = abs(c_0_fit - 2.5) < 0.005
    h2_match = abs(c_2_fit - (-G)) < 0.01
    print(f"  Leading 5/2: {'✓ MATCH' if leading_match else '✗ FAIL'} (Δ {c_0_fit - 2.5:+.5f})")
    print(f"  h² = -G:     {'✓ MATCH' if h2_match else '✗ FAIL'} (Δ {c_2_fit + G:+.5f})")
    if leading_match and h2_match:
        print()
        print(f"  → A((4-q)/(4q+3)) = 5/2 - h²·G + O(h^4) VERIFIED numerically!")
    elif leading_match:
        print()
        print(f"  → Leading verified; h² coefficient is {c_2_fit:.5f}, NOT -G.")

    # Persist the proof-attempt result as a witness (Copilot review on PR #751).
    w = WitnessBuilder("probe-A-h-expansion-fixed", engine="numpy+scipy")
    w.set_description(
        "Numerical proof-attempt: A((4-q)/(4q+3)) = 5/2 - h²·G + O(h^4). "
        "Computes A(3/7) (the q=1 leading term) and fits A(a_post_hoc(q)) "
        "to a polynomial in h² over a small q-grid. Records c_0, c_2, c_4 "
        "fit coefficients and the leading/h² match flags."
    )
    w.set_content_block("conj:flavor-dressed-mass-from-substrate-split")
    w.add_data("A_at_q1_3over7", A_at_q1)
    w.add_data("leading_target", 2.5)
    w.add_data("leading_match", bool(leading_match))
    w.add_data("c_0_fit", float(c_0_fit))
    w.add_data("c_2_fit", float(c_2_fit))
    w.add_data("h2_match_minus_G", bool(h2_match))
    w.add_data("target_h2_minus_G", -G)
    w.add_data("q_samples", q_vals.tolist())
    w.add_data("A_samples_at_a_post_hoc", [None if np.isnan(v) else float(v) for v in A_vals.tolist()])
    out = w.save()
    print(f"\nWitness emitted: {out.name}")


if __name__ == "__main__":
    main()
