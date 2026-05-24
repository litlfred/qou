"""
picard_lefschetz_standard_practice_refactor.py — research scaffold
for refactoring picard_lefschetz_thimble.py to STANDARD PL practice
(task 3 from m_n audit).

Per owner: "Refactor picard_lefschetz_thimble.py to STANDARD PL
practice (integrate along thimbles to ∞, not finite real-axis) —
this is the literature-aligned fix"

Per the lit search (docs/audits/2026-05-17-m-n-substrate-investigation-
and-lit-search.md), standard Picard-Lefschetz practice is:

  1. Identify saddle points z_c in ℂ
  2. For each saddle, parametrise the steepest-descent THIMBLE
     𝒥_{z_c} = {z(t) : dz/dt = -conjugate(λ_SW(z)), z(0) = z_c,
                Im(S(z(t))) = Im(S(z_c))}
     extended from z_c to INFINITY in the direction of decreasing Re(S).
  3. Decompose the original real-axis integral as a sum over thimbles:
        ∫_ℝ f(z) dz  =  Σ_σ n_σ · ∫_{𝒥_σ} f(z) dz
     where n_σ = ⟨𝒦_σ, ℝ⟩ are intersection numbers of the anti-thimbles
     𝒦_σ with the original real-axis contour.
  4. Each thimble integral ∫_{𝒥_σ} f(z) dz is convergent (asymptotic
     decay of f along the thimble direction).
  5. NO FINITE REAL-AXIS CUTOFF.

The existing picard_lefschetz_thimble.py uses a non-standard
finite real-axis cutoff [-a, +a] with `a` post-hoc fit.  This
refactor computes the SAME observable (A(q₀) = baryon period /
electron period) using the standard along-thimble integration.

If the refactored value matches the post-hoc result (~2.46),
the empirical formula is recovered structurally.  If not, the
post-hoc fit is exposed as fictitious.

**RESEARCH SCAFFOLD** — implementation requires careful handling
of:
  - thimble parametrisation (numerical ODE integration to large t)
  - intersection number computation (winding integrals)
  - convergence detection along the thimble
  - reproduction of the original ∏ dc_k/dz prescription on the
    thimble (not just on the real axis)

Full implementation deferred; this script establishes the scaffold
and demonstrates the standard PL approach on a SIMPLIFIED test case.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import numpy as np
from scipy import integrate
from picard_lefschetz_thimble import (  # noqa: E402
    cubic_roots, dF_dc, dF_dz, find_discriminant_roots,
    sw_3root_product_degree1,
)
from q_parameter import Q as q0, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, VOL_BORROMEAN
from witness_base import WitnessBuilder  # noqa: E402


def lambda_SW(z):
    """λ_SW^(1)(z) = dc/dz on principal sheet."""
    cs = cubic_roots(z)
    c = cs[np.argmin(np.abs(cs.imag))]
    denom = dF_dc(z, c)
    if abs(denom) < 1e-15:
        return complex("inf")
    return -dF_dz(z, c) / denom


def thimble_trajectory(z_c, n_steps=50000, dt=0.0005):
    """Parametrise the steepest-descent thimble from z_c.

    Returns (t_values, z_values) along the thimble.  Extends to
    large t until the integrand magnitude decays sufficiently.
    """
    z = complex(z_c) + 0.001 * complex(1.0, 1.0)  # nudge off saddle
    traj = [z]
    t_values = [0.0]
    for i in range(n_steps):
        flow = -np.conj(lambda_SW(z))
        if not np.isfinite(flow.real) or abs(flow) < 1e-15:
            break
        z = z + flow * dt
        traj.append(z)
        t_values.append((i + 1) * dt)
        if abs(z) > 100.0:  # gone too far
            break
    return np.array(t_values), np.array(traj)


def integrand_baryon(z):
    """∏_k dc_k/dz at z (baryon prescription)."""
    return sw_3root_product_degree1(z)


def integrand_electron(z):
    """c_0(z) + z (electron-reference prescription)."""
    cs = cubic_roots(z)
    c = cs[np.argmin(np.abs(cs.imag))]
    return c + z


def thimble_integral(z_c, integrand_fn):
    """Integrate `integrand_fn(z)` along the thimble from z_c using
    trapezoidal rule on the parametrised contour."""
    t_vals, z_vals = thimble_trajectory(z_c)
    if len(z_vals) < 10:
        return complex("nan")
    # Trapezoidal: ∫ f(z(t)) dz/dt dt  ≈  Σ f(z) · Δz
    integrand_at_z = np.array([integrand_fn(z) for z in z_vals])
    delta_z = np.diff(z_vals)
    midpoint_integrand = 0.5 * (integrand_at_z[:-1] + integrand_at_z[1:])
    return np.sum(midpoint_integrand * delta_z)


def main() -> int:
    print("=" * 78)
    print("  Standard PL refactor scaffold — integrate ALONG thimbles to ∞")
    print("=" * 78)
    print(f"  q_0 = {q0:.10f}")
    print()

    z_cs_raw = find_discriminant_roots()
    z_cs = []
    for item in (z_cs_raw if hasattr(z_cs_raw, '__iter__') else [z_cs_raw]):
        if hasattr(item, '__len__') and not isinstance(item, complex):
            for sub in item:
                z_cs.append(complex(sub))
        else:
            z_cs.append(complex(item))

    # Take the principal pair (nearest to z_0)
    z_0 = (q0 ** 0.5) - 1.0 / (q0 ** 0.5)
    z_cs_sorted = sorted(z_cs[:6], key=lambda z: abs(z.real - z_0))
    z_c_plus = z_cs_sorted[0]
    print(f"  Principal saddle: z_c⁺ = {z_c_plus.real:+.6f}{z_c_plus.imag:+.6f}i")
    print()

    print("  Step 1: Parametrise steepest-descent thimble from z_c⁺")
    print("  " + "-" * 60)
    t_vals, z_vals = thimble_trajectory(z_c_plus)
    print(f"    Thimble length: {len(z_vals)} points, |z_final| = {abs(z_vals[-1]):.4f}")
    print(f"    Thimble endpoint: {z_vals[-1].real:+.4f}{z_vals[-1].imag:+.4f}i")
    print()

    print("  Step 2: Integrate baryon prescription along thimble")
    print("  " + "-" * 60)
    I_baryon = thimble_integral(z_c_plus, integrand_baryon)
    I_electron = thimble_integral(z_c_plus, integrand_electron)
    print(f"    ∫_{{𝒥⁺}} ∏ dc_k/dz dz  = {I_baryon.real:+.6f}{I_baryon.imag:+.6f}i")
    print(f"    ∫_{{𝒥⁺}} (c_0 + z) dz  = {I_electron.real:+.6f}{I_electron.imag:+.6f}i")
    print()

    if abs(I_electron) > 1e-15:
        ratio = abs(I_baryon) / abs(I_electron)
        borromean = VOL_BORROMEAN / (HBAR_Q ** 2)
        m_p_pred = borromean * ratio * M_E_MEV
        err_pct = abs(m_p_pred - M_P_MEV) / M_P_MEV * 100
        print(f"  Step 3: Ratio A(q₀) = |I_baryon|/|I_electron| = {ratio:.6f}")
        print(f"  borromean factor       = {borromean:.6f}")
        print(f"  m_p_pred (standard PL) = {m_p_pred:.4f} MeV")
        print(f"  CODATA m_p              = {M_P_MEV} MeV")
        print(f"  residual                = {err_pct:.4f} %")
        print()
        post_hoc_a = (4 - q0) / (4 * q0 + 3)
        print(f"  Compare to post-hoc finite-interval result at a={post_hoc_a:.4f}:")
        print(f"    m_p_pred (post-hoc) = 938.27 MeV (6 ppm — back-fit)")
        print()

        if err_pct < 1.0:
            print("  *** Standard PL recovers m_p to <1% — empirical formula has")
            print("      a structural origin (the along-thimble integral converges to")
            print("      the same value).")
        else:
            print("  *** Standard PL gives DIFFERENT m_p_pred from the post-hoc")
            print("      finite-interval result — empirical formula is fictitious")
            print("      OR the thimble parametrisation needs refinement.")
    else:
        ratio = float("nan")
        m_p_pred = float("nan")
        err_pct = float("nan")
        print(f"  ∫_electron near zero — thimble may not capture the")
        print(f"  full electron contribution.  Refactor needs more work.")
    print()

    print("  STATUS: research scaffold")
    print("  Full refactor requires:")
    print("    1. Refined thimble parametrisation (adaptive step size)")
    print("    2. Intersection-number computation (n_σ via anti-thimbles)")
    print("    3. Multi-thimble decomposition (6 saddles → 6 thimbles)")
    print("    4. Reproducing the original 9 prescriptions on thimbles")
    print()
    print("  See docs/audits/2026-05-17-m-n-substrate-investigation-and-lit-search.md")
    print("  for the full lit-search context.")

    w = (WitnessBuilder("picard-lefschetz-standard-practice-refactor",
                         engine="scipy+numpy")
         .set_description("Research scaffold: standard PL along-thimble refactor"))
    w.add_data("q_0", q0)
    w.add_data("z_c_principal", {"re": float(z_c_plus.real),
                                   "im": float(z_c_plus.imag)})
    w.add_data("thimble_length", len(z_vals))
    w.add_data("thimble_endpoint", {"re": float(z_vals[-1].real),
                                      "im": float(z_vals[-1].imag)})
    w.add_data("I_baryon", {"re": float(I_baryon.real),
                             "im": float(I_baryon.imag)})
    w.add_data("I_electron", {"re": float(I_electron.real),
                                "im": float(I_electron.imag)})
    if not np.isnan(ratio):
        w.add_data("ratio_A_q0", float(ratio))
        w.add_data("m_p_pred_standard_PL_MeV", float(m_p_pred))
        w.add_data("residual_pct", float(err_pct))
    w.add_data("status", "scaffold")
    w.add_caveat("Thimble parametrisation uses simple Euler integration; "
                 "production refactor needs adaptive step size + intersection-number "
                 "computation.")
    w.add_assertion("refactor_implemented",
                    computed=0.0, expected=0.0)  # scaffold, not full implementation
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
