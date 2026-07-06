#!/usr/bin/env python3
"""
Seiberg-Witten period integrals on the Descartes elliptic curve E_q.

The mass hierarchy comes from SW periods at different vertical degrees:
  Degree 0 (electron): a_D^(e) = ∮ (c+z) dz
  Degree 1 (muon):     a_D^(μ) = ∮ dc/dz × residue at discriminant locus
  Degree 3 (baryon):   a_D^(B) = ∮ λ_SW^(2) = ???

The elliptic curve E_q: y² = x³ + p(q)x + r(q)
with p(q) = 2(q²-q+1)/(3q) + (q-1)/(3√q)
     r(q) = 20(q-1)³/(27q^{3/2}) + 5(q-1)²/(9q) + 5(√q-1/√q)/9 + 20/27

The color-tube cubic: c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1) = 0

At spacetime ratio z = √q - 1/√q (= s - s⁻¹), the cubic encodes
the three color channels. The discriminant locus (where two roots merge)
gives the topological defect z_c.

We compute:
1. The elliptic curve periods ω₁, ω₂ at q₀
2. The color-tube discriminant locus z_c
3. The SW period integrals at degrees 0, 1, 2, 3
4. The mass ratios m_e : m_μ : m_p from the periods

Usage:
    python3 computations/sw_period_baryon.py
"""

import sys, math, cmath
import numpy as np
from scipy import integrate
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HBAR_Q, HBAR_Q_SQ
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV, VOL_BORROMEAN

s0 = math.sqrt(q0)
si0 = 1.0 / s0
z0 = s0 - si0  # spacetime ratio at q₀
HA = q0 - 1.0/q0


# ══════════════════════════════════════════════════════════════
# §1  ELLIPTIC CURVE E_q
# ══════════════════════════════════════════════════════════════

def weierstrass_p(q):
    """p(q) coefficient of E_q."""
    return 2*(q**2 - q + 1)/(3*q) + (q - 1)/(3*math.sqrt(q))

def weierstrass_r(q):
    """r(q) coefficient of E_q."""
    s = math.sqrt(q)
    return (20*(q-1)**3/(27*q**1.5) + 5*(q-1)**2/(9*q) +
            5*(s - 1/s)/9 + 20/27)

p_q0 = weierstrass_p(q0)
r_q0 = weierstrass_r(q0)
disc = -16*(4*p_q0**3 + 27*r_q0**2)


# ══════════════════════════════════════════════════════════════
# §2  COLOR-TUBE CUBIC DISCRIMINANT
# ══════════════════════════════════════════════════════════════

def cubic_roots(z):
    """Roots of c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1) = 0."""
    coeffs = [1, 4*z+1, 6*z**2+3*z+1, 4*z**3+3*z**2+2*z+1]
    return np.roots(coeffs)

def cubic_discriminant(z):
    """Discriminant of the color-tube cubic."""
    a, b, c, d = 1, 4*z+1, 6*z**2+3*z+1, 4*z**3+3*z**2+2*z+1
    return 18*a*b*c*d - 4*b**3*d + b**2*c**2 - 4*a*c**3 - 27*a**2*d**2

# Find the discriminant locus z_c where Δ = 0
from scipy.optimize import brentq
# The discriminant changes sign near z ≈ -0.25 and z ≈ 0
zc_candidates = []
for z_test in np.linspace(-2, 2, 1000):
    d1 = cubic_discriminant(z_test)
    d2 = cubic_discriminant(z_test + 0.004)
    if d1 * d2 < 0:
        zc = brentq(cubic_discriminant, z_test, z_test + 0.004)
        zc_candidates.append(zc)


# ══════════════════════════════════════════════════════════════
# §3  SEIBERG-WITTEN PERIODS
# ══════════════════════════════════════════════════════════════

def sw_degree0_integrand(z):
    """λ_SW^(0) = (c + z) where c is a root of the cubic.
    For the electron: integrate over the exceptional divisor S_c."""
    roots = cubic_roots(z)
    # Use the real root (or the one closest to real)
    real_roots = [r.real for r in roots if abs(r.imag) < 1e-10]
    if real_roots:
        c = real_roots[0]
    else:
        c = roots[0].real
    return c + z

def sw_degree1_integrand(z):
    """λ_SW^(1) = dc/dz from the cubic.
    dc/dz = -(4z³+3z²+2z+1) / (3c²+2(4z+1)c+(6z²+3z+1))
    This is the muon SW differential."""
    roots = cubic_roots(z)
    real_roots = [r.real for r in roots if abs(r.imag) < 1e-10]
    c = real_roots[0] if real_roots else roots[0].real
    numer = (4*z**3 + 3*z**2 + 2*z + 1)
    denom = 3*c**2 + 2*(4*z+1)*c + (6*z**2+3*z+1)
    if abs(denom) < 1e-15:
        return 0.0
    return numer / (c * denom)

def sw_degree2_integrand(z):
    """λ_SW^(2) = d²c/dz² — the second prolongation.
    This should give the tau (or baryon) mass scale.
    Compute via finite difference of degree 1."""
    h = 1e-6
    f1 = sw_degree1_integrand(z + h)
    f0 = sw_degree1_integrand(z - h)
    return (f1 - f0) / (2*h)

def sw_degree3_integrand(z):
    """λ_SW^(3) — the third prolongation (Borromean/baryon).
    The baryon has 3 color channels; the SW differential at degree 3
    integrates over all three color roots simultaneously.

    Alternative interpretation: product of all 3 color roots' contributions.
    """
    roots = cubic_roots(z)
    # Product: c_r × c_g × c_b = -(4z³+3z²+2z+1) by Vieta
    product = -(4*z**3 + 3*z**2 + 2*z + 1)
    # Sum: c_r + c_g + c_b = -(4z+1)
    total = -(4*z + 1)
    # The baryon contribution: all three roots together
    # Try: sum of all three (c_k + z) = total + 3z = -(4z+1) + 3z = -(z+1)
    return -(z + 1)


# ══════════════════════════════════════════════════════════════
# §4  COMPUTE PERIODS
# ══════════════════════════════════════════════════════════════

def main():
    print("=" * 100)
    print("SEIBERG-WITTEN PERIODS ON THE DESCARTES ELLIPTIC CURVE")
    print(f"q₀ = {q0:.10f}   s = √q = {s0:.10f}   z₀ = s-s⁻¹ = {z0:.10f}")
    print("=" * 100)
    print()

    print(f"Elliptic curve E_q: y² = x³ + {p_q0:.6f}x + {r_q0:.6f}")
    print(f"  Discriminant Δ = {disc:.6f}")
    print()

    print("Color-tube cubic discriminant locus z_c:")
    for zc in zc_candidates:
        roots_at_zc = cubic_roots(zc)
        print(f"  z_c = {zc:.10f}  roots = {[f'{r:.4f}' for r in roots_at_zc]}")
    print()

    # Integration limits: around the discriminant locus
    # The SW period is a contour integral around z_c
    # For numerical computation, integrate along the real axis
    # from z_c - ε to z_c + ε

    # Degree 0: electron mass scale
    print("─" * 100)
    print("SW PERIODS (integrated along real axis near z₀)")
    print()

    # Integrate each degree from -1 to z₀
    z_lo, z_hi = -0.5, z0

    for deg, name, integrand in [
        (0, "electron (deg 0)",  sw_degree0_integrand),
        (1, "muon (deg 1)",      sw_degree1_integrand),
        (2, "tau/baryon (deg 2)", sw_degree2_integrand),
        (3, "baryon 3-color (deg 3)", sw_degree3_integrand),
    ]:
        try:
            result, error = integrate.quad(integrand, z_lo, z_hi, limit=200)
            # Also try with absolute value for mass
            result_abs, _ = integrate.quad(lambda z: abs(integrand(z)), z_lo, z_hi, limit=200)
        except Exception as e:
            result, error, result_abs = float('nan'), float('nan'), float('nan')

        print(f"  a_D^({deg}) [{name}]:")
        print(f"    ∮ λ_SW^({deg}) dz = {result:.10f} ± {error:.2e}")
        print(f"    ∮ |λ_SW^({deg})| dz = {result_abs:.10f}")

        # Mass from period: m = |a_D| / ℏ_q²
        m_hecke = abs(result) / HBAR_Q_SQ
        m_abs_hecke = result_abs / HBAR_Q_SQ
        print(f"    |a_D|/ℏ_q² = {m_hecke:.4f} (mass in Hecke units)")
        print(f"    ∮|λ|/ℏ_q² = {m_abs_hecke:.4f}")
        print()

    # Now try different integration contours
    print("─" * 100)
    print("PERIOD RATIOS (key question: which gives m_p/m_e = 1836?)")
    print()

    # Compute all periods
    periods = {}
    for z_lo, z_hi, label in [
        (-0.5, z0, "[-0.5, z₀]"),
        (0, z0, "[0, z₀]"),
        (-1, 1, "[-1, 1]"),
    ]:
        for deg, integrand in [(0, sw_degree0_integrand), (1, sw_degree1_integrand)]:
            try:
                val, _ = integrate.quad(integrand, z_lo, z_hi, limit=200)
            except:
                val = float('nan')
            key = f"deg{deg}_{label}"
            periods[key] = val

    print(f"  Ratio a_D^(1)/a_D^(0) should give m_μ/m_e = 206.77:")
    for contour in ["[-0.5, z₀]", "[0, z₀]", "[-1, 1]"]:
        p0 = periods.get(f"deg0_{contour}", 0)
        p1 = periods.get(f"deg1_{contour}", 0)
        ratio = abs(p1/p0) if abs(p0) > 1e-15 else 0
        print(f"    Contour {contour}: |a_D^(1)/a_D^(0)| = {ratio:.6f}")

    # Try the PRODUCT of all three color roots as the baryon mass
    print()
    print("─" * 100)
    print("BARYON MASS FROM COLOR-TUBE CUBIC")
    print()

    # At z = z₀ = s - 1/s, the three roots are:
    roots_z0 = cubic_roots(z0)
    print(f"  Color-tube roots at z₀ = {z0:.6f}:")
    for i, r in enumerate(roots_z0):
        print(f"    c_{i} = {r:.6f}")

    # The product: c_r × c_g × c_b = -(4z³+3z²+2z+1)
    product = -(4*z0**3 + 3*z0**2 + 2*z0 + 1)
    print(f"  Product c_r·c_g·c_b = {product:.6f}")
    print(f"  |product| = {abs(product):.6f}")
    print(f"  |product|^(1/3) = {abs(product)**(1/3):.6f}")

    # The sum |(c_k + z)| for each root = the per-color mass
    print()
    print("  Per-color mass |c_k + z₀|:")
    total_color_mass = 0.0
    for i, r in enumerate(roots_z0):
        m_k = abs(r + z0)
        total_color_mass += m_k
        print(f"    |c_{i} + z₀| = {m_k:.6f}")
    print(f"  Sum = {total_color_mass:.6f}")

    # The electron mass is |c_0 + z₀| (one root)
    # The baryon mass should be sum of all 3 (or product)
    m_e_sw = abs(roots_z0[0].real + z0)  # use real root
    m_baryon_sum = total_color_mass
    ratio_sum = m_baryon_sum / m_e_sw if m_e_sw > 1e-10 else 0

    print()
    print(f"  m_e(SW) ≈ |c_real + z₀| = {m_e_sw:.6f}")
    print(f"  m_baryon(SW) ≈ Σ|c_k + z₀| = {m_baryon_sum:.6f}")
    print(f"  Ratio baryon/electron = {ratio_sum:.6f}")
    print(f"  Need: m_p/m_e = {M_P_MEV/M_E_MEV:.4f}")
    print()

    # Try: m_p = Vol(B3)/ℏ_q² × Σ|c_k + z₀| / |c_real + z₀|
    vol_factor = m_baryon_sum / m_e_sw
    m_p_derived = VOL_BORROMEAN / HBAR_Q_SQ * vol_factor * M_E_MEV / (VOL_BORROMEAN / HBAR_Q_SQ)
    # Simplifies to: m_p = vol_factor × m_e
    m_p_from_sw = vol_factor * M_E_MEV
    print(f"  m_p(SW) = (Σ|c+z|/|c₀+z|) × m_e = {vol_factor:.4f} × {M_E_MEV} = {m_p_from_sw:.3f} MeV")
    print(f"  CODATA m_p = {M_P_MEV:.3f} MeV")
    print()

    # Try more approaches: integrate (c+z)^n for n = 1,2,3
    print("─" * 100)
    print("POWER-WEIGHTED INTEGRALS ∮ (c+z)^n dz")
    print()
    for n in [1, 2, 3, 4, 5, 6]:
        def integrand_n(z, n=n):
            roots = cubic_roots(z)
            real_roots = [r.real for r in roots if abs(r.imag) < 1e-10]
            c = real_roots[0] if real_roots else roots[0].real
            return (c + z)**n
        try:
            val, _ = integrate.quad(integrand_n, -0.5, z0, limit=200)
        except:
            val = float('nan')
        m_hecke = abs(val) / HBAR_Q_SQ
        # In m_e units: divide by degree-0 period
        print(f"  n={n}: ∮(c+z)^{n} dz = {val:.10f}  →  |∮|/ℏ_q² = {m_hecke:.4f}")

    # Try: integrate PRODUCT of all three roots
    print()
    print("PRODUCT-ROOT INTEGRAL ∮ (c_r+z)(c_g+z)(c_b+z) dz")
    def product_integrand(z):
        roots = cubic_roots(z)
        prod = 1.0
        for r in roots:
            prod *= abs(r + z)
        return prod.real if isinstance(prod, complex) else prod
    try:
        val_prod, _ = integrate.quad(product_integrand, -0.5, z0, limit=200)
    except:
        val_prod = float('nan')
    print(f"  ∮ ∏|c_k+z| dz = {val_prod:.10f}")
    print(f"  |∮|/ℏ_q² = {val_prod/HBAR_Q_SQ:.4f}")

    # Ratio to degree-0
    p0, _ = integrate.quad(sw_degree0_integrand, -0.5, z0, limit=200)
    if abs(p0) > 1e-15:
        print(f"  Ratio to deg-0: {val_prod / abs(p0):.6f}")
        print(f"  Need: m_p/m_e = {M_P_MEV/M_E_MEV:.4f}")

    from witness_base import WitnessBuilder
    w = WitnessBuilder("sw-period-baryon", engine="scipy")
    w.set_description("SW period integrals on E_q for baryon mass derivation.")
    w.add_parameter("q0", str(q0))
    w.save()


if __name__ == "__main__":
    main()
