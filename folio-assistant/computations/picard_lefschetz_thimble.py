#!/usr/bin/env python3
"""
Picard-Lefschetz thimble decomposition for the color-tube cubic.

Implements the 6-step plan from docs/picard-lefschetz-plan.md:
  1. Critical points of the SW action S = ∫ λ_SW on E_q  (z_c known)
  2. Hessian ∂²S/∂z² at each z_c → thimble directions
  3. Parametrize thimbles as steepest-descent paths from z_c
  4. Numerically integrate λ_SW along each thimble
  5. Intersection numbers with the real axis
  6. Assemble the period ratio m_p/m_e

The color-tube cubic:
  F(z,c) = c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1) = 0

Its discriminant Δ(z) vanishes at 6 complex roots (3 conjugate pairs).
At each z_c, two color sheets merge and the prolonged SW differential
λ_SW^(1) = dc/dz has a pole.  The Picard-Lefschetz thimble J_{z_c}
is the steepest-descent contour of Re(S) from z_c.

Usage:
    python3 folio-assistant/computations/picard_lefschetz_thimble.py
"""

import sys
import math
import cmath
import numpy as np
from scipy import integrate
from scipy.optimize import fsolve
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HBAR_Q, HBAR_Q_SQ
from experimental_constants import M_E_MEV, M_P_MEV, VOL_BORROMEAN

s0 = math.sqrt(q0)
z0 = s0 - 1.0 / s0   # physical spacetime ratio


# ══════════════════════════════════════════════════════════════
# §1  COLOR-TUBE CUBIC AND DISCRIMINANT
# ══════════════════════════════════════════════════════════════

def F_cubic(z, c):
    """Color-tube cubic F(z, c)."""
    return c**3 + (4*z+1)*c**2 + (6*z**2+3*z+1)*c + (4*z**3+3*z**2+2*z+1)

def dF_dc(z, c):
    """∂F/∂c — vanishes at discriminant locus (repeated root)."""
    return 3*c**2 + 2*(4*z+1)*c + (6*z**2+3*z+1)

def dF_dz(z, c):
    """∂F/∂z — used in implicit differentiation dc/dz = -dF/dz / dF/dc."""
    return 4*c**2 + (12*z+3)*c + (12*z**2+6*z+2)

def cubic_roots(z):
    """Roots of the color-tube cubic at complex z."""
    coeffs = [1, 4*z+1, 6*z**2+3*z+1, 4*z**3+3*z**2+2*z+1]
    return np.roots(coeffs)

def cubic_discriminant_complex(z):
    """Discriminant Δ(z) of the color-tube cubic at complex z."""
    a = 1
    b = 4*z + 1
    c = 6*z**2 + 3*z + 1
    d = 4*z**3 + 3*z**2 + 2*z + 1
    return 18*a*b*c*d - 4*b**3*d + b**2*c**2 - 4*a*c**3 - 27*a**2*d**2


# ══════════════════════════════════════════════════════════════
# §2  CRITICAL POINTS OF THE SW ACTION
# ══════════════════════════════════════════════════════════════

def find_discriminant_roots():
    """
    Find all 6 complex roots of Δ(z) = 0.

    The discriminant is a degree-6 polynomial in z. We construct it
    explicitly and find roots via numpy.
    """
    # Δ(z) = 18abcd - 4b³d + b²c² - 4ac³ - 27a²d²
    # with a=1, b=4z+1, c=6z²+3z+1, d=4z³+3z²+2z+1
    #
    # Build as numpy polynomial coefficients.
    # We use a dense grid + Newton polishing approach.
    from numpy.polynomial import polynomial as P

    # Represent a, b, c, d as polynomial coefficients (ascending powers)
    a_p = np.array([1.0])                    # 1
    b_p = np.array([1.0, 4.0])              # 1 + 4z
    c_p = np.array([1.0, 3.0, 6.0])         # 1 + 3z + 6z²
    d_p = np.array([1.0, 2.0, 3.0, 4.0])    # 1 + 2z + 3z² + 4z³

    # Compute each term of Δ using polynomial multiplication
    # Term 1: 18*a*b*c*d
    t1 = 18 * P.polymul(P.polymul(P.polymul(a_p, b_p), c_p), d_p)
    # Term 2: -4*b³*d
    b3 = P.polymul(P.polymul(b_p, b_p), b_p)
    t2 = -4 * P.polymul(b3, d_p)
    # Term 3: +b²*c²
    b2 = P.polymul(b_p, b_p)
    c2 = P.polymul(c_p, c_p)
    t3 = P.polymul(b2, c2)
    # Term 4: -4*a*c³
    c3 = P.polymul(P.polymul(c_p, c_p), c_p)
    t4 = -4 * P.polymul(a_p, c3)
    # Term 5: -27*a²*d²
    d2 = P.polymul(d_p, d_p)
    t5 = -27 * P.polymul(P.polymul(a_p, a_p), d2)

    # Sum all terms — pad to same length
    max_len = max(len(t) for t in [t1, t2, t3, t4, t5])
    delta_coeffs = np.zeros(max_len)
    for t in [t1, t2, t3, t4, t5]:
        delta_coeffs[:len(t)] += t

    # Find roots (ascending power convention for numpy.polynomial)
    roots = P.polyroots(delta_coeffs)
    return roots, delta_coeffs


# ══════════════════════════════════════════════════════════════
# §3  SW INTEGRAND AND ACTION
# ══════════════════════════════════════════════════════════════

def sw_integrand_degree1(z):
    """
    λ_SW^(1)(z) = dc/dz = -dF/dz / dF/dc

    Returns the prolonged SW differential at complex z,
    evaluated on the real root (or the root closest to real).
    """
    roots = cubic_roots(z)
    # Select the root with smallest imaginary part
    idx = np.argmin(np.abs(roots.imag))
    c = roots[idx]

    denom = dF_dc(z, c)
    if abs(denom) < 1e-30:
        return complex(0, 0)
    numer = dF_dz(z, c)
    return -numer / denom


def sw_action(z, z_ref=0.0):
    """
    S(z) = ∫_{z_ref}^{z} λ_SW^(1)(z') dz'

    Computed via adaptive quadrature along a straight-line path
    from z_ref to z in the complex plane.
    """
    def integrand_real(t):
        """Parametrize path: z(t) = z_ref + t*(z - z_ref), t ∈ [0,1]."""
        zt = z_ref + t * (z - z_ref)
        dz_dt = z - z_ref
        val = sw_integrand_degree1(zt)
        return complex(val) * complex(dz_dt)

    def real_part(t):
        return integrand_real(t).real

    def imag_part(t):
        return integrand_real(t).imag

    re_val, _ = integrate.quad(real_part, 0, 1, limit=200)
    im_val, _ = integrate.quad(imag_part, 0, 1, limit=200)
    return complex(re_val, im_val)


# ══════════════════════════════════════════════════════════════
# §4  HESSIAN AT CRITICAL POINTS
# ══════════════════════════════════════════════════════════════

def hessian_at_critical_point(z_c, h=1e-5):
    """
    Compute H(z_c) = ∂²S/∂z² at z_c via finite differences.

    Since S = ∫ λ_SW^(1) dz, we have dS/dz = λ_SW^(1) and
    d²S/dz² = dλ_SW^(1)/dz.

    We compute this via central finite differences on the integrand.
    """
    f_plus = sw_integrand_degree1(z_c + h)
    f_minus = sw_integrand_degree1(z_c - h)
    f_center = sw_integrand_degree1(z_c)

    # Central difference for second derivative
    hessian = (f_plus - 2*f_center + f_minus) / h**2
    return complex(hessian)


def thimble_direction(z_c):
    """
    Compute the initial thimble direction at z_c.

    The thimble J_{z_c} departs from z_c along direction e^{iθ}
    where θ = -½ arg(H(z_c)).
    """
    H = hessian_at_critical_point(z_c)
    theta = -0.5 * cmath.phase(H)
    return cmath.exp(1j * theta)


# ══════════════════════════════════════════════════════════════
# §5  THIMBLE PARAMETRIZATION (STEEPEST DESCENT)
# ══════════════════════════════════════════════════════════════

def trace_thimble(z_c, direction, n_steps=500, dt=0.005):
    """
    Trace the Picard-Lefschetz thimble from z_c in the given direction.

    The thimble satisfies dz/dt = -conj(∇S(z)), which in 1D means
    dz/dt = -conj(dS/dz) = -conj(λ_SW^(1)(z)).

    We integrate this ODE starting near z_c along the initial direction.

    Returns array of complex points along the thimble.
    """
    # Start slightly displaced from z_c along the thimble direction
    z_start = z_c + 1e-4 * direction

    path = [z_c, z_start]
    z = z_start

    for _ in range(n_steps):
        # Gradient flow: dz/dt = -conj(dS/dz)
        grad_S = sw_integrand_degree1(z)
        if abs(grad_S) < 1e-30:
            break

        dz = -np.conj(complex(grad_S)) * dt

        # Adaptive step size: reduce if gradient is large
        if abs(dz) > 0.1:
            dz = dz * 0.1 / abs(dz)

        z_new = z + dz

        # Stop if we've gone too far from origin
        if abs(z_new) > 10:
            break

        path.append(z_new)
        z = z_new

    return np.array(path)


def trace_anti_thimble(z_c, direction, n_steps=500, dt=0.005):
    """
    Trace the anti-thimble (steepest ascent) from z_c.
    Direction rotated by π/2 from thimble direction.
    """
    anti_dir = direction * 1j
    return trace_thimble(z_c, anti_dir, n_steps, dt)


# ══════════════════════════════════════════════════════════════
# §6  INTERSECTION NUMBERS
# ══════════════════════════════════════════════════════════════

def intersection_with_real_axis(anti_thimble_path):
    """
    Count signed intersections of the anti-thimble path with the real axis.

    n_σ = #(K_σ ∩ γ) where γ = ℝ.
    A crossing from Im>0 to Im<0 counts as +1, reverse as -1.
    """
    n = 0
    for i in range(len(anti_thimble_path) - 1):
        im1 = anti_thimble_path[i].imag
        im2 = anti_thimble_path[i+1].imag
        if im1 * im2 < 0:  # sign change
            # Interpolate real part at crossing
            t = im1 / (im1 - im2)
            re_cross = anti_thimble_path[i].real + t * (anti_thimble_path[i+1].real - anti_thimble_path[i].real)
            # Sign: positive if crossing downward (Im: + → -)
            n += 1 if im1 > 0 else -1
    return n


# ══════════════════════════════════════════════════════════════
# §7  PERIOD INTEGRALS ALONG THIMBLES
# ══════════════════════════════════════════════════════════════

def integrate_along_thimble(thimble_path, degree=0):
    """
    Integrate λ_SW^(k) along a thimble path.

    degree 0: ∮ (c+z) dz  (electron)
    degree 1: ∮ dc/dz dz   (muon)
    degree 2: ∮ d²c/dz² dz (baryon)
    """
    total = complex(0, 0)

    for i in range(len(thimble_path) - 1):
        z = 0.5 * (thimble_path[i] + thimble_path[i+1])
        dz = thimble_path[i+1] - thimble_path[i]

        roots = cubic_roots(z)
        idx = np.argmin(np.abs(roots.imag))
        c = roots[idx]

        if degree == 0:
            integrand = c + z
        elif degree == 1:
            denom = dF_dc(z, c)
            if abs(denom) < 1e-30:
                continue
            integrand = -dF_dz(z, c) / denom
        elif degree == 2:
            # Finite difference of degree 1
            h = 1e-5
            f_plus = sw_integrand_degree1(z + h)
            f_minus = sw_integrand_degree1(z - h)
            integrand = (f_plus - f_minus) / (2*h)
        else:
            integrand = 0

        total += complex(integrand) * complex(dz)

    return total


# ══════════════════════════════════════════════════════════════
# §8  MAIN COMPUTATION
# ══════════════════════════════════════════════════════════════

def main():
    print("=" * 100)
    print("PICARD-LEFSCHETZ THIMBLE DECOMPOSITION")
    print(f"q₀ = {q0:.10f}   z₀ = √q - 1/√q = {z0:.10f}")
    print("=" * 100)
    print()

    # ── Step 1: Find critical points ──────────────────────────
    print("STEP 1: Critical points of S (discriminant locus Δ(z) = 0)")
    print()

    disc_roots, disc_coeffs = find_discriminant_roots()
    print(f"  Discriminant polynomial degree: {len(disc_coeffs)-1}")
    print(f"  Number of roots: {len(disc_roots)}")
    print()

    # Sort by distance to z₀
    distances = [abs(r - z0) for r in disc_roots]
    sorted_idx = np.argsort(distances)

    print(f"  {'Root':>5}  {'z_c':>35}  {'|z_c - z₀|':>12}  {'Δ(z_c)':>15}")
    print(f"  {'─'*5}  {'─'*35}  {'─'*12}  {'─'*15}")
    for i, idx in enumerate(sorted_idx):
        zc = disc_roots[idx]
        delta_check = cubic_discriminant_complex(zc)
        print(f"  {i+1:>5}  {zc.real:>16.10f} {'+' if zc.imag >= 0 else '-'} {abs(zc.imag):.10f}i"
              f"  {distances[idx]:>12.6f}  {abs(delta_check):>15.2e}")
    print()

    # Focus on the closest conjugate pair
    zc_nearest = disc_roots[sorted_idx[0]]
    if zc_nearest.imag < 0:
        zc_nearest = np.conj(zc_nearest)
    zc_conj = np.conj(zc_nearest)

    print(f"  Closest pair to z₀:")
    print(f"    z_c⁺ = {zc_nearest.real:.10f} + {zc_nearest.imag:.10f}i")
    print(f"    z_c⁻ = {zc_conj.real:.10f} + {zc_conj.imag:.10f}i")
    print()

    # ── Step 2: Hessian at critical points ────────────────────
    print("STEP 2: Hessian H(z_c) = ∂²S/∂z² and thimble directions")
    print()

    for label, zc in [("z_c⁺", zc_nearest), ("z_c⁻", zc_conj)]:
        H = hessian_at_critical_point(zc)
        direction = thimble_direction(zc)

        print(f"  {label} = {zc:.6f}")
        print(f"    H(z_c) = {H.real:.6f} + {H.imag:.6f}i")
        print(f"    |H| = {abs(H):.6f}")
        print(f"    arg(H) = {cmath.phase(H):.6f} rad = {cmath.phase(H)*180/math.pi:.2f}°")
        print(f"    Thimble direction: e^{{iθ}} = {direction:.6f}")
        print(f"    θ = {cmath.phase(direction)*180/math.pi:.2f}°")
        print()

    # ── Step 3: Trace thimbles ────────────────────────────────
    print("STEP 3: Parametrize thimbles (steepest descent from z_c)")
    print()

    thimble_plus = trace_thimble(zc_nearest, thimble_direction(zc_nearest),
                                  n_steps=2000, dt=0.002)
    thimble_minus = trace_thimble(zc_conj, thimble_direction(zc_conj),
                                   n_steps=2000, dt=0.002)

    print(f"  Thimble J⁺: {len(thimble_plus)} points")
    print(f"    Start: {thimble_plus[0]:.6f}")
    print(f"    End:   {thimble_plus[-1]:.6f}")
    print(f"    Re range: [{min(p.real for p in thimble_plus):.4f}, {max(p.real for p in thimble_plus):.4f}]")
    print(f"    Im range: [{min(p.imag for p in thimble_plus):.4f}, {max(p.imag for p in thimble_plus):.4f}]")
    print()

    print(f"  Thimble J⁻: {len(thimble_minus)} points")
    print(f"    Start: {thimble_minus[0]:.6f}")
    print(f"    End:   {thimble_minus[-1]:.6f}")
    print(f"    Re range: [{min(p.real for p in thimble_minus):.4f}, {max(p.real for p in thimble_minus):.4f}]")
    print(f"    Im range: [{min(p.imag for p in thimble_minus):.4f}, {max(p.imag for p in thimble_minus):.4f}]")
    print()

    # ── Step 4: Anti-thimbles and intersection numbers ────────
    print("STEP 4–5: Anti-thimbles and intersection numbers with ℝ")
    print()

    anti_plus = trace_anti_thimble(zc_nearest, thimble_direction(zc_nearest),
                                    n_steps=2000, dt=0.002)
    anti_minus = trace_anti_thimble(zc_conj, thimble_direction(zc_conj),
                                     n_steps=2000, dt=0.002)

    n_plus = intersection_with_real_axis(anti_plus)
    n_minus = intersection_with_real_axis(anti_minus)

    print(f"  Anti-thimble K⁺: {len(anti_plus)} points")
    print(f"    Intersection number n⁺ = ⟨K⁺, ℝ⟩ = {n_plus}")
    print()
    print(f"  Anti-thimble K⁻: {len(anti_minus)} points")
    print(f"    Intersection number n⁻ = ⟨K⁻, ℝ⟩ = {n_minus}")
    print()

    # ── Step 6: Period integrals along thimbles ───────────────
    print("STEP 6: Period integrals along thimbles")
    print()

    for label, thimble in [("J⁺", thimble_plus), ("J⁻", thimble_minus)]:
        print(f"  Thimble {label}:")
        for deg in [0, 1, 2]:
            period = integrate_along_thimble(thimble, degree=deg)
            print(f"    ∮_{{label}} λ_SW^({deg}) dz = {period.real:.10f} + {period.imag:.10f}i")
            print(f"      |period| = {abs(period):.10f}")
            print(f"      |period|/ℏ_q² = {abs(period)/HBAR_Q_SQ:.6f}")
        print()

    # ── Assemble period ratios ────────────────────────────────
    print("─" * 100)
    print("PERIOD RATIOS AND MASS PREDICTIONS")
    print()

    pi_0_plus = integrate_along_thimble(thimble_plus, degree=0)
    pi_0_minus = integrate_along_thimble(thimble_minus, degree=0)
    pi_1_plus = integrate_along_thimble(thimble_plus, degree=1)
    pi_1_minus = integrate_along_thimble(thimble_minus, degree=1)
    pi_2_plus = integrate_along_thimble(thimble_plus, degree=2)
    pi_2_minus = integrate_along_thimble(thimble_minus, degree=2)

    # Combined periods with intersection numbers
    Pi_0 = n_plus * pi_0_plus + n_minus * pi_0_minus
    Pi_1 = n_plus * pi_1_plus + n_minus * pi_1_minus
    Pi_2 = n_plus * pi_2_plus + n_minus * pi_2_minus

    print(f"  Combined periods (Π^(k) = Σ n_σ ∮_{{J_σ}} λ_SW^(k)):")
    print(f"    Π^(0) = {Pi_0:.10f}   |Π^(0)| = {abs(Pi_0):.10f}")
    print(f"    Π^(1) = {Pi_1:.10f}   |Π^(1)| = {abs(Pi_1):.10f}")
    print(f"    Π^(2) = {Pi_2:.10f}   |Π^(2)| = {abs(Pi_2):.10f}")
    print()

    if abs(Pi_0) > 1e-15:
        r10 = abs(Pi_1) / abs(Pi_0)
        r20 = abs(Pi_2) / abs(Pi_0)
        print(f"  |Π^(1)/Π^(0)| = {r10:.6f}   (target: m_μ/m_e = 206.768)")
        print(f"  |Π^(2)/Π^(0)| = {r20:.6f}   (target: m_p/m_e = {M_P_MEV/M_E_MEV:.4f})")
    else:
        print("  WARNING: Π^(0) is effectively zero — contour may not capture electron period")
        print("  Individual thimble periods:")
        for label, p0, p1, p2 in [("J⁺", pi_0_plus, pi_1_plus, pi_2_plus),
                                    ("J⁻", pi_0_minus, pi_1_minus, pi_2_minus)]:
            if abs(p0) > 1e-15:
                print(f"    {label}: |Π^(1)/Π^(0)| = {abs(p1)/abs(p0):.6f}  "
                      f"|Π^(2)/Π^(0)| = {abs(p2)/abs(p0):.6f}")
    print()

    # ── Color-tube amplification factor ───────────────────────
    print("─" * 100)
    print("COLOR-TUBE AMPLIFICATION FACTOR")
    print()

    target_ratio = M_P_MEV / M_E_MEV
    borromean_factor = VOL_BORROMEAN / HBAR_Q_SQ
    amplification_needed = target_ratio / borromean_factor
    print(f"  m_p/m_e = {target_ratio:.4f}")
    print(f"  Vol(𝔅₃)/ℏ_q² = {borromean_factor:.6f}")
    print(f"  Amplification factor needed: A(q₀) = {amplification_needed:.6f}")
    print(f"    i.e., m_p = Vol(𝔅₃)/ℏ_q² × A(q₀) × m_e")
    print(f"    with A(q₀) ≈ {amplification_needed:.4f}")
    print()

    # ── Summary of all 6 critical points ──────────────────────
    print("─" * 100)
    print("ALL CRITICAL POINT SUMMARY")
    print()

    all_thimble_data = []
    for i, idx in enumerate(sorted_idx):
        zc = disc_roots[idx]
        H = hessian_at_critical_point(zc)
        direction = thimble_direction(zc)

        # Quick thimble trace
        thimble = trace_thimble(zc, direction, n_steps=500, dt=0.005)
        anti = trace_anti_thimble(zc, direction, n_steps=500, dt=0.005)
        n_int = intersection_with_real_axis(anti)

        p0 = integrate_along_thimble(thimble, degree=0)
        p1 = integrate_along_thimble(thimble, degree=1)
        p2 = integrate_along_thimble(thimble, degree=2)

        all_thimble_data.append({
            "z_c": zc,
            "hessian": H,
            "direction": direction,
            "intersection": n_int,
            "period_0": p0,
            "period_1": p1,
            "period_2": p2,
        })

        print(f"  Root {i+1}: z_c = {zc.real:+.8f} {'+' if zc.imag >= 0 else '-'} {abs(zc.imag):.8f}i")
        print(f"    |H| = {abs(H):.4f}  dir = {cmath.phase(direction)*180/math.pi:.1f}°"
              f"  n = {n_int}")
        print(f"    |Π⁰| = {abs(p0):.8f}  |Π¹| = {abs(p1):.8f}  |Π²| = {abs(p2):.8f}")
        if abs(p0) > 1e-15:
            print(f"    |Π¹/Π⁰| = {abs(p1)/abs(p0):.4f}  |Π²/Π⁰| = {abs(p2)/abs(p0):.4f}")
        print()

    # ── Write witness ─────────────────────────────────────────
    from witness_base import WitnessBuilder
    w = WitnessBuilder("picard-lefschetz-thimble", engine="scipy")
    w.set_description(
        "Picard-Lefschetz thimble decomposition for the color-tube cubic. "
        "Computes critical points, Hessians, thimble directions, "
        "intersection numbers, and SW period integrals."
    )
    w.set_content_block("def:picard-lefschetz-thimble")
    w.add_parameter("q0", str(q0))
    w.add_parameter("z0", str(z0))
    w.add_parameter("hbar_q_sq", str(HBAR_Q_SQ))

    # Record critical points
    crit_data = []
    for td in all_thimble_data:
        crit_data.append({
            "z_c_real": float(td["z_c"].real),
            "z_c_imag": float(td["z_c"].imag),
            "hessian_abs": float(abs(td["hessian"])),
            "hessian_arg_deg": float(cmath.phase(td["hessian"]) * 180 / math.pi),
            "intersection_number": int(td["intersection"]),
            "period_0_abs": float(abs(td["period_0"])),
            "period_1_abs": float(abs(td["period_1"])),
            "period_2_abs": float(abs(td["period_2"])),
        })
    w.add_data("critical_points", crit_data)
    w.add_data("amplification_factor_needed", float(amplification_needed))

    w.add_caveat(
        "Thimble tracing uses simple Euler integration of the gradient flow ODE. "
        "Higher-order integrators (RK4) and adaptive step sizes may improve accuracy."
    )
    w.add_caveat(
        "Intersection numbers depend on the length and accuracy of anti-thimble paths. "
        "Results should be verified with finer step sizes."
    )
    w.add_caveat(
        "The period ratios do not yet reproduce the target m_p/m_e = 1836. "
        "The baryon period may require a different contour prescription "
        "(e.g. integration over all three color roots simultaneously, or "
        "a product formula rather than individual root tracking)."
    )

    w.save()
    print()
    print("=" * 100)
    print("COMPUTATION COMPLETE")
    print("=" * 100)


if __name__ == "__main__":
    main()
