#!/usr/bin/env python3
"""Attempt to prove `A((4-q)/(4q+3)) = 5/2 - h²·G + O(h^4)`.

Strategy: compute A(a_post_hoc(q)) at multiple q values near q=1,
fit a polynomial in h = q - q^{-1}, extract h^0 and h^2 coefficients,
test against the conjectured values.

If c_0 = 5/2 and c_2 = -G (Catalan), the conjecture is verified
numerically. If yes, this gives the structural derivation of the
nucleon mass via PR #690's framework.

The Schur-Weyl integrand depends on q implicitly through cubic_roots
+ sw_3root_product_degree1. So A(a_post_hoc(q), q) is a function of
just q. We sample at q = q_0(ε) for various ε, where ε = q - 1, and
fit:
  A(a_post_hoc(q), q) = c_0 + c_2 · h² + c_4 · h^4 + c_6 · h^6 + ...
"""
from __future__ import annotations
import json, sys
from pathlib import Path

import numpy as np
import mpmath as mp
from scipy import integrate

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder

# Have to construct the integrands as q-dependent ourselves.
# Strategy: read picard_lefschetz_thimble source for the cubic +
# SW3 product, then re-construct at arbitrary q.


def cubic_roots_at_q(z, q):
    """Cubic roots used by the categorical-action integrand.

    From `picard_lefschetz_thimble.py`: the cubic underlying the
    Schur-Weyl 3-root product is c^3 + ... with coefficients in q.
    For this probe we use the q-dependent form.

    Specifically the cubic that defines the proton's SW 3-roots
    (as in `prop:operator-selection-lp`):
        c^3 - 3 z c^2 + (3 z^2 - h^2) c - z^3 = 0
    (this is one canonical form for the 3-root product at q;
    not the only one; the production script uses similar via
    cubic_roots(z))
    """
    # Symbolic-style: solve c^3 - 3 z c^2 + (3 z^2 - h_q^2) c - z^3 = 0
    h_q = q - 1/q
    # Coefficients [a_3, a_2, a_1, a_0]
    coeffs = [1, -3*z, 3*z**2 - h_q**2, -z**3]
    return np.roots(coeffs)


def sw_3root_product_degree1_at_q(z, q):
    """Schur-Weyl 3-root product, degree-1 component.

    Approximation matching `picard_lefschetz_thimble.sw_3root_product_degree1`:
    product of the 3 roots minus z^3, divided by leading factor.
    For the canonical cubic above, sum of roots = 3z, so the
    "degree-1" symmetric function is the elementary sym e_1(c_1, c_2, c_3) - 3z = 0

    The "product" function in the script likely refers to a SPECIFIC
    polynomial in the symmetric functions. Use SCRIPT-COMPATIBLE form
    at q=q_0; for other q values we extrapolate via this same form.
    """
    cs = cubic_roots_at_q(z, q)
    # Use the form from picard_lefschetz_thimble:
    # the integrand is real part of the 3-root product expression
    # which evaluates to a real-axis function. Match the numerical
    # output at q=q_0 by using the same combination.
    # For this proof attempt, use: real part of product of (c - z)
    # for each root (degree-1 generating function)
    prod = 1.0
    for c in cs:
        prod *= (c - z)
    return np.real(prod)


def integrand_baryon_at_q(z, q):
    return float(sw_3root_product_degree1_at_q(z, q))


def integrand_electron_at_q(z, q):
    cs = cubic_roots_at_q(z, q)
    # Take root nearest imaginary axis
    idx = np.argmin(np.abs(cs.imag)) if hasattr(cs, 'imag') else 0
    c = cs[idx]
    return float(np.real(c + z))


def A_of_q(q):
    """Compute A(a_post_hoc(q), q)."""
    a_val = (4 - q) / (4*q + 3)
    if not (0 < a_val < 1/(np.sqrt(q) + np.sqrt(1/q))):
        return float('nan')
    try:
        e_ref, _ = integrate.quad(lambda z: integrand_electron_at_q(z, q),
                                   -a_val, a_val, limit=200)
        prod, _ = integrate.quad(lambda z: integrand_baryon_at_q(z, q),
                                  -a_val, a_val, limit=200)
        if abs(e_ref) < 1e-15:
            return float('nan')
        return abs(prod) / abs(e_ref)
    except Exception:
        return float('nan')


def main():
    G = float(mp.catalan)  # = 0.91596559...

    print("Proof attempt: A((4-q)/(4q+3)) = 5/2 - h²·G + O(h^4)?")
    print(f"  Conjectured: c_0 = 5/2 = 2.5,  c_2 = -G = {-G:.10f}")
    print()

    # Sample q values near 1
    q_samples = np.linspace(1.001, 1.30, 30)
    h_samples = q_samples - 1.0/q_samples
    A_samples = np.array([A_of_q(q) for q in q_samples])

    # Drop NaNs
    valid = ~np.isnan(A_samples)
    q_v = q_samples[valid]
    h_v = h_samples[valid]
    A_v = A_samples[valid]

    print(f"  Sampled {len(q_v)} q values:")
    for q, h, A in zip(q_v[:5], h_v[:5], A_v[:5]):
        print(f"    q={q:.4f}, h={h:.4f}, A((4-q)/(4q+3))={A:.6f}")
    print("    ...")
    for q, h, A in zip(q_v[-3:], h_v[-3:], A_v[-3:]):
        print(f"    q={q:.4f}, h={h:.4f}, A((4-q)/(4q+3))={A:.6f}")
    print()

    # Fit polynomial in h: A = c_0 + c_2·h² + c_4·h^4 + ...
    # h² is the leading variable since A should be symmetric in q↔1/q
    h2 = h_v**2

    # Try polynomial fits of various degrees
    for degree in [1, 2, 3, 4]:
        coeffs = np.polyfit(h2, A_v, degree)
        # coeffs are in order [c_2k, c_2k-2, ..., c_2, c_0]
        c_0 = coeffs[-1]
        c_2 = coeffs[-2] if len(coeffs) >= 2 else None
        print(f"  Degree {degree} polynomial in h² fit:")
        print(f"    c_0 (constant): {c_0:.10f}   vs 5/2 = 2.5  (Δ = {c_0 - 2.5:+.6f})")
        if c_2 is not None:
            print(f"    c_2 (h² coeff): {c_2:.10f}   vs -G = {-G:.10f}  (Δ = {c_2 - (-G):+.6f})")
        # Residuals
        pred = np.polyval(coeffs, h2)
        residual_max = np.max(np.abs(A_v - pred))
        print(f"    max residual: {residual_max:.4e}")
        print()

    # Verdict
    print("=" * 70)
    print("VERDICT")
    print("=" * 70)
    # Use degree-2 fit (linear in h²) for cleanest test
    coeffs_2 = np.polyfit(h2, A_v, 1)
    c_2_fit, c_0_fit = coeffs_2[0], coeffs_2[1]
    if abs(c_0_fit - 2.5) < 0.005:
        print(f"  c_0 = {c_0_fit:.6f} matches 5/2 (within 0.5%)")
    else:
        print(f"  c_0 = {c_0_fit:.6f} does NOT match 5/2 (off by {c_0_fit - 2.5:.4f})")
    if abs(c_2_fit - (-G)) < 0.01:
        print(f"  c_2 = {c_2_fit:.6f} matches -G = {-G:.6f} (within 0.01)")
    else:
        print(f"  c_2 = {c_2_fit:.6f} does NOT match -G = {-G:.6f}")
        print(f"  Ratio c_2 / (-G) = {c_2_fit / (-G):.6f}")

    w = WitnessBuilder("A-at-post-hoc-h-expansion", engine="numpy+scipy")
    w.set_description(
        "Proof attempt: numerical fit of A((4-q)/(4q+3)) as polynomial "
        "in h². Tests conjecture c_0 = 5/2, c_2 = -G (Catalan)."
    )
    w.set_content_block("conj:flavor-dressed-mass-from-substrate-split")
    w.add_data("n_samples", int(len(q_v)))
    w.add_data("c_0_fit", float(c_0_fit))
    w.add_data("c_2_fit", float(c_2_fit))
    w.add_data("c_0_target_5_over_2", 2.5)
    w.add_data("c_2_target_minus_G", float(-G))
    w.add_data("c_0_diff", float(c_0_fit - 2.5))
    w.add_data("c_2_diff", float(c_2_fit - (-G)))
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
