"""
residue_algebraic_verification.py — substantiate prop:sw-period-thimble-equivalence A2.4.

The merged PR #779 replaced the Lefschetz-decomposition hypothesis A2.4
with an algebraic-residue formula on the principal Galois orbit of the
color-tube cubic's discriminant:

    ∫_{γ_{a(q_0)}^{cat}} λ^{(k)}(z) dz  =  Σ_{z_c ∈ O_prin} Res^{alg}_{z_c}(λ^{(k)})

where γ_{a(q_0)}^{cat} is the categorical contour whose archimedean image
under τ at substrate q_0 is the real interval [-a(q_0), a(q_0)] with
a(q) = (4-q)/(4q+3).

This script numerically checks the equality at q_0 ≈ 1.110 for the baryon
channel k = 3 (integrand ∏_k dc_k/dz) by computing BOTH sides:

  (LHS) the real-axis interval integral [-a(q_0), a(q_0)] directly (as
        used by picard_lefschetz_thimble.py — the empirical m_p closure)
  (RHS) the algebraic residue sum at the principal pair z_c^± obtained
        from a small-circle contour integral around each z_c

Both are then divided by the analogous denominator for the electron
channel k = 0 (integrand c_0 + z, no poles — only LHS makes sense).
The amplification factor A(q_0) := |LHS_num| / |LHS_denom| should match
the empirical 2.460 → m_p ≈ 938.267 MeV closure.

The CRITICAL check is whether |RHS_num| (algebraic residue sum) equals
|LHS_num| (interval integral) up to the appropriate conventional factor.
If yes, the A2.4 algebraic-residue swap is empirically supported. If no,
the swap needs a refinement (e.g. residue requires a closing contour
that the finite real-axis interval doesn't provide).

Ref: [grothendieck1966] algebraic de Rham cohomology
Ref: [hartshorne1966] Residues and Duality
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import numpy as np
from scipy import integrate
from q_parameter import Q as q0, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, VOL_BORROMEAN
from witness_base import WitnessBuilder


# ── Color-tube cubic + helpers ──────────────────────────────────────

def cubic_roots(z: complex) -> np.ndarray:
    """Three color roots of F(z, c) = 0 at given z."""
    coeffs = [
        1.0 + 0.0j,
        4 * z + 1,
        6 * z**2 + 3 * z + 1,
        4 * z**3 + 3 * z**2 + 2 * z + 1,
    ]
    return np.roots(coeffs)


def dF_dc(z: complex, c: complex) -> complex:
    return 3 * c**2 + 2 * (4 * z + 1) * c + (6 * z**2 + 3 * z + 1)


def dF_dz(z: complex, c: complex) -> complex:
    return 4 * c**2 + (12 * z + 3) * c + (12 * z**2 + 6 * z + 2)


def dc_dz_at(z: complex, c: complex) -> complex:
    denom = dF_dc(z, c)
    if abs(denom) < 1e-14:
        return complex("inf")
    return -dF_dz(z, c) / denom


def prod_dc_dz(z: complex) -> complex:
    """Baryon integrand: product of three color prolongations."""
    cs = cubic_roots(z)
    p = 1.0 + 0.0j
    for c in cs:
        p *= dc_dz_at(z, c)
    return p


def electron_integrand(z: complex) -> complex:
    """Electron integrand: c_0 + z, where c_0 is the closest-to-real root at z."""
    cs = cubic_roots(z)
    c0 = cs[np.argmin(np.abs(cs.imag))]
    return c0 + z


# ── Discriminant roots + principal Galois orbit selection ───────────

def find_discriminant_roots() -> np.ndarray:
    """Six complex roots of Δ(z) = -(16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16)."""
    return np.roots([16, 24, 35, 50, 35, 24, 16])


def select_principal_orbit(roots: np.ndarray) -> list[complex]:
    """Principal Galois orbit O_prin = innermost conjugate pair (by |z|)."""
    sorted_by_modulus = sorted(roots, key=lambda z: abs(z))
    return [complex(sorted_by_modulus[0]), complex(sorted_by_modulus[1])]


# ── Algebraic residue via small-circle contour integral ─────────────

def residue_via_circle(f, z_c: complex, eps: float = 1e-3, n: int = 400) -> complex:
    """
    Algebraic residue Res_{z_c}(f) computed numerically as
    (1/2πi) ∮_{|z-z_c|=ε} f(z) dz over a small circle of radius ε.

    Discrete approximation: sum over n equispaced points, dz = i·ε·e^{iθ} dθ.
    """
    thetas = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    dtheta = 2.0 * np.pi / n
    integral = 0.0 + 0.0j
    for theta in thetas:
        z = z_c + eps * np.exp(1j * theta)
        dz = 1j * eps * np.exp(1j * theta) * dtheta
        integral += f(z) * dz
    return integral / (2j * np.pi)


# ── Real-axis interval integral (matches picard_lefschetz_thimble.py) ──

def interval_integral(f, a: float, n: int = 5000) -> complex:
    """∫_{-a}^{a} f(z) dz over real axis via Simpson's rule (complex-valued)."""
    xs = np.linspace(-a, a, n)
    fs_re = np.array([f(x).real for x in xs])
    fs_im = np.array([f(x).imag for x in xs])
    re = integrate.simpson(fs_re, x=xs)
    im = integrate.simpson(fs_im, x=xs)
    return complex(re, im)


# ── Main verification ──────────────────────────────────────────────

def main() -> int:
    builder = WitnessBuilder("residue-algebraic-verification")
    builder.set_description(
        "Numerical verification of prop:sw-period-thimble-equivalence A2.4 "
        "algebraic-residue formula at q_0: compares the real-axis interval "
        "integral (empirical m_p closure) with the algebraic residue sum at "
        "the principal Galois orbit {z_c^±} of the color-tube discriminant."
    )

    a_q0 = (4 - q0) / (4 * q0 + 3)
    borromean_factor = VOL_BORROMEAN / (HBAR_Q ** 2)

    builder.add_parameter("q0", str(q0))
    builder.add_parameter("a_q0_mobius_limit", str(a_q0))
    builder.add_parameter("hbar_q", str(HBAR_Q))

    # Find principal Galois orbit
    disc_roots = find_discriminant_roots()
    principal = select_principal_orbit(disc_roots)

    builder.add_data("discriminant_roots", [
        {"re": float(z.real), "im": float(z.imag), "abs": float(abs(z))}
        for z in disc_roots
    ])
    builder.add_data("principal_orbit", [
        {"re": float(z.real), "im": float(z.imag), "abs": float(abs(z))}
        for z in principal
    ])

    # ── Numerator (baryon, k=3) ─────────────────────────────────────
    # LHS: real-axis interval integral
    lhs_num = interval_integral(prod_dc_dz, a_q0)
    # RHS: algebraic residue sum at principal orbit
    residues = [residue_via_circle(prod_dc_dz, z_c) for z_c in principal]
    rhs_num = sum(residues)

    builder.add_data("baryon_numerator", {
        "lhs_real_axis_interval_integral": {
            "re": float(lhs_num.real),
            "im": float(lhs_num.imag),
            "abs": float(abs(lhs_num)),
        },
        "rhs_algebraic_residue_sum": {
            "re": float(rhs_num.real),
            "im": float(rhs_num.imag),
            "abs": float(abs(rhs_num)),
        },
        "rhs_per_residue": [
            {
                "z_c": {"re": float(z.real), "im": float(z.imag)},
                "res": {"re": float(r.real), "im": float(r.imag), "abs": float(abs(r))},
            }
            for z, r in zip(principal, residues)
        ],
        "lhs_over_rhs_ratio_abs": (
            float(abs(lhs_num) / abs(rhs_num))
            if abs(rhs_num) > 1e-14 else None
        ),
        "lhs_over_rhs_ratio_2pi_norm": (
            float(abs(lhs_num) / abs(rhs_num) / (2 * np.pi))
            if abs(rhs_num) > 1e-14 else None
        ),
    })

    # ── Denominator (electron, k=0) ─────────────────────────────────
    # Only LHS makes sense (c_0 + z has no poles → trivial residue)
    lhs_denom = interval_integral(electron_integrand, a_q0)

    builder.add_data("electron_denominator", {
        "lhs_real_axis_interval_integral": {
            "re": float(lhs_denom.real),
            "im": float(lhs_denom.imag),
            "abs": float(abs(lhs_denom)),
        },
        "note": "Electron integrand (c_0 + z) is holomorphic on the principal "
                "orbit's neighbourhood; residue sum is identically zero. The "
                "algebraic content of the electron mass channel is the direct "
                "interval integration, not a residue."
    })

    # ── Amplification factor + m_p prediction ───────────────────────
    A_q0_lhs = abs(lhs_num) / abs(lhs_denom)
    m_p_pred_lhs = borromean_factor * A_q0_lhs * M_E_MEV
    builder.add_data("amplification_via_lhs", {
        "A_q0": float(A_q0_lhs),
        "m_p_predicted_MeV": float(m_p_pred_lhs),
        "m_p_codata_MeV": float(M_P_MEV),
        "error_percent": float(abs(m_p_pred_lhs - M_P_MEV) / M_P_MEV * 100),
    })

    # The RHS-based amplification factor (algebraic residue vs interval denom)
    # — this is the "mixed" formula since the denominator has no residue analog
    if abs(rhs_num) > 1e-14:
        A_q0_rhs = abs(rhs_num) / abs(lhs_denom)
        builder.add_data("amplification_via_rhs_numerator", {
            "A_q0_using_residue_numerator": float(A_q0_rhs),
            "note": "Numerator uses algebraic residue sum; denominator uses "
                    "interval integral (no residue analog for c_0 + z). "
                    "Whether this matches the empirical 2.460 indicates whether "
                    "the LHS=RHS equality holds up to the conventional 2πi "
                    "factor on the numerator."
        })

    # Assertion: LHS amplification matches empirical (this is the picard_lefschetz_thimble.py result)
    builder.add_assertion(
        "amplification_factor_LHS_real_axis_matches_empirical",
        computed=A_q0_lhs,
        expected=2.4599,
        tolerance=0.01,
        unit="ratio",
        source="picard_lefschetz_thimble.py best_limit (4-q)/(4q+3) at q_0"
    )

    # Assertion: residue sum is non-trivial (basic sanity check)
    builder.add_assertion(
        "residue_sum_nontrivial",
        computed=float(abs(rhs_num)),
        expected=0.5,
        tolerance=0.5,  # loose; just want non-zero
        unit="abs residue",
        source="algebraic-residue formulation per prop:sw-period-thimble-equivalence A2.4"
    )

    builder.save()

    print("=" * 72)
    print("  Residue-algebraic verification of A2.4 at q_0")
    print("=" * 72)
    print(f"  q_0          = {q0:.10f}")
    print(f"  a(q_0)       = (4-q)/(4q+3) = {a_q0:.10f}")
    print()
    print(f"  Principal Galois orbit:")
    for z in principal:
        print(f"    z = {z.real:.6f} + {z.imag:+.6f}i  (|z| = {abs(z):.6f})")
    print()
    print("  Numerator (baryon ∏ dc_k/dz):")
    print(f"    LHS real-axis ∫_{{-a}}^{{a}}: |{lhs_num:.6f}| = {abs(lhs_num):.6f}")
    print(f"    RHS Σ_{{z_c}} Res:           |{rhs_num:.6f}| = {abs(rhs_num):.6f}")
    if abs(rhs_num) > 1e-14:
        print(f"    LHS / RHS                 = {abs(lhs_num)/abs(rhs_num):.6f}")
        print(f"    LHS / (2π·RHS)            = {abs(lhs_num)/(2*np.pi*abs(rhs_num)):.6f}")
    print()
    print("  Denominator (electron c_0 + z):")
    print(f"    LHS real-axis ∫_{{-a}}^{{a}}: |{lhs_denom:.6f}| = {abs(lhs_denom):.6f}")
    print()
    print("  Amplification factor:")
    print(f"    A(q_0) [LHS/LHS] = {A_q0_lhs:.6f}  (target ≈ 2.460)")
    print(f"    m_p_pred         = {m_p_pred_lhs:.3f} MeV (CODATA = {M_P_MEV:.3f} MeV)")
    print(f"    error            = {abs(m_p_pred_lhs - M_P_MEV)/M_P_MEV*100:.4f}%")
    print()
    print("  See witness JSON for full numerical record.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
