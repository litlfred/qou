#!/usr/bin/env python3
"""
Compute the Legendre lambda-invariant of the Descartes elliptic curve
E_q at the substrate parameter q_0, and compare to the shape parameter
z = e^{i pi/3} of the regular ideal tetrahedron (figure-8 knot).

This pins down whether the "universal shape parameter" ansatz
(every crossing carries z_c = lambda(q)) aligns with the Thurston
volume of key atomic links.

Inputs:
    q_0 from q_parameter.py (pinned via Vol(4_1) / (m_mu/m_e))

Outputs:
    lambda-descartes-q0.witness.json

Numerical pipeline:
    q       -> p(q), r(q) via Weierstrass form y^2 = x^3 + p x + r
    p, r    -> j = 6912 p^3 / (4 p^3 + 27 r^2)
    j       -> u root of  256 u^3 = j (1 - u)^2,  u = lambda^2 - lambda + 1
    u       -> lambda = (1 +/- sqrt(1 - 4(1 - u))) / 2  (pair of roots)
    lambda  -> D(lambda) via Bloch-Wigner dilogarithm
    compare to D(e^{i pi/3}) = v_3  (Lobachevsky constant)

Refs:
    prop:descartes-elliptic-curve in content/quantum-observable-universe/
    prop:thurston-volume-additivity (this branch)
"""
from __future__ import annotations

import cmath
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, HBAR_Q, HBAR_Q_SQ


# ── Descartes Weierstrass coefficients p(q), r(q) ─────────────────
# From prop:descartes-elliptic-curve:
#   p(z) = (2/3) z^2 + (1/3) z + (2/3)
#   r(z) = (20/27) z^3 + (5/9) z^2 + (5/9) z + (20/27)
#   z    = s - 1/s   with s = sqrt(q)

def weierstrass_pr(q: float) -> tuple[float, float]:
    s = math.sqrt(q)
    z = s - 1.0 / s
    p = (2.0 / 3.0) * z * z + (1.0 / 3.0) * z + (2.0 / 3.0)
    r = (20.0 / 27.0) * z ** 3 + (5.0 / 9.0) * z * z + (5.0 / 9.0) * z + (20.0 / 27.0)
    return p, r


def j_invariant(p: float, r: float) -> float:
    # y^2 = x^3 + p x + r   =>   j = 6912 p^3 / (4 p^3 + 27 r^2)
    num = 6912.0 * p ** 3
    den = 4.0 * p ** 3 + 27.0 * r ** 2
    return num / den


# ── Legendre lambda via j-invariant ───────────────────────────────
# j(E) = 256 (1 - lambda + lambda^2)^3 / (lambda^2 (1 - lambda)^2)
# Set u = lambda^2 - lambda + 1.  Then
# lambda(1 - lambda) = 1 - u, so lambda^2 (1 - lambda)^2 = (1 - u)^2.
# Hence j = 256 u^3 / (1 - u)^2.

def _f(u: float, j: float) -> float:
    return 256.0 * u ** 3 - j * (1.0 - u) ** 2


def _bisect_u(j: float, lo: float = 1e-6, hi: float = 1.0 - 1e-6,
              tol: float = 1e-14, max_iter: int = 200) -> float:
    """Bisection fallback when Newton's derivative vanishes.

    f(u) = 256 u^3 - j (1-u)^2 is increasing on (0, 1) for j > 0,
    so a sign change exists between (lo, hi) for any physically
    valid j.
    """
    flo, fhi = _f(lo, j), _f(hi, j)
    if flo * fhi > 0:
        # No sign change in [lo, hi] — return midpoint as least-bad guess.
        return 0.5 * (lo + hi)
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        fm = _f(mid, j)
        if abs(fm) < tol or (hi - lo) < tol:
            return mid
        if fm * flo < 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def u_from_j(j: float, tol: float = 1e-12, max_iter: int = 200) -> float:
    # Newton on f(u) = 256 u^3 - j (1 - u)^2, with bisection fallback
    # if the derivative vanishes (rare but possible near u = 2j/(3·256+2j)).
    u = 0.5
    for _ in range(max_iter):
        f = _f(u, j)
        fp = 3 * 256.0 * u ** 2 + 2 * j * (1.0 - u)
        if abs(fp) < 1e-14:
            return _bisect_u(j, tol=tol, max_iter=max_iter)
        step = f / fp
        u -= step
        if abs(step) < tol:
            break
    return u


def lambdas_from_u(u: complex) -> list[complex]:
    # u := λ² - λ + 1  ⇒  λ² - λ = u - 1  ⇒  λ² - λ + (1 - u) = 0
    # Quadratic formula: λ = (1 ± √(1 - 4(1-u))) / 2 = (1 ± √(4u - 3)) / 2
    disc = 4.0 * u - 3.0
    root = cmath.sqrt(complex(disc))
    return [(1 + root) / 2, (1 - root) / 2]


def bloch_wigner(z: complex, n_terms: int = 2000) -> float:
    """D(z) = Im(Li_2(z)) + arg(1-z) * log|z|  (Bloch-Wigner dilogarithm).

    Primary path: direct series Li_2(z) = sum z^n / n^2 for |z| <= 1,
    with inversion for |z| > 1.  For |z| ≈ 1 the series converges
    slowly; we delegate to mpmath.polylog (arbitrary precision) when
    available, falling back to the series otherwise.
    """
    if z == 0:
        return 0.0
    # For |z| close to 1, prefer mpmath.polylog (handles boundary robustly).
    if abs(abs(z) - 1.0) < 1e-3:
        try:
            import mpmath as _mp
            Li2 = complex(_mp.polylog(2, complex(z)))
            one_minus_z = 1.0 - z
            arg_1mz = cmath.phase(one_minus_z) if one_minus_z != 0 else 0.0
            log_abs_z = math.log(abs(z)) if abs(z) > 0 else 0.0
            return Li2.imag + arg_1mz * log_abs_z
        except ImportError:
            pass  # fall through to series
    if abs(z) > 1:
        # Bloch-Wigner functional equation D(z) = -D(1/z) — avoids
        # complex-log branch cuts of the full Li_2 inversion.
        return -bloch_wigner(1.0 / z, n_terms)
    Li2 = _li2_series(z, n_terms)
    one_minus_z = 1.0 - z
    arg_1mz = cmath.phase(one_minus_z) if one_minus_z != 0 else 0.0
    log_abs_z = math.log(abs(z)) if abs(z) > 0 else 0.0
    return Li2.imag + arg_1mz * log_abs_z


def _li2_series(z: complex, n_terms: int) -> complex:
    s = 0 + 0j
    zn = 1 + 0j
    for n in range(1, n_terms + 1):
        zn *= z
        s += zn / (n * n)
    return s


# ── Main ──────────────────────────────────────────────────────────

def main() -> int:
    p, r = weierstrass_pr(Q0)
    j = j_invariant(p, r)

    u = u_from_j(j)
    lam_pair = lambdas_from_u(complex(u))

    # Full S_3 orbit: lambda, 1 - lambda, 1/lambda, ...
    s3_orbit = []
    for lam in lam_pair:
        orbit = [
            lam,
            1.0 - lam,
            1.0 / lam,
            1.0 / (1.0 - lam),
            (lam - 1.0) / lam,
            lam / (lam - 1.0),
        ]
        s3_orbit.append(orbit)

    # Bloch-Wigner at each lambda root and at the regular tetrahedron
    regular = cmath.exp(1j * math.pi / 3.0)
    D_regular = bloch_wigner(regular)  # ≈ 1.01494 = v_3

    D_values = []
    for lam in lam_pair:
        D_values.append({
            "lambda": {"re": lam.real, "im": lam.imag},
            "abs": abs(lam),
            "arg": cmath.phase(lam),
            "D": bloch_wigner(lam),
        })

    # Compare to other key knot/link shapes
    comparisons = {
        "regular_tetrahedron (e^{i pi/3})": {
            "z": {"re": regular.real, "im": regular.imag},
            "D": D_regular,
            "note": "Lobachevsky constant v_3; figure-8 knot shape",
        },
        "half_plus_half_i (1/2 + i/2)": {
            "z": {"re": 0.5, "im": 0.5},
            "D": bloch_wigner(complex(0.5, 0.5)),
            "note": "Whitehead-link-like shape (approx)",
        },
    }

    witness = {
        "name": "lambda-descartes-q0",
        "description": (
            "Legendre lambda-invariant of the Descartes elliptic curve "
            "at the substrate parameter q_0.  Compares the per-crossing "
            "universal shape parameter (if z_c = lambda) to the regular "
            "tetrahedron shape e^{i pi/3} governing the figure-8 knot."
        ),
        "inputs": {
            "q_0": Q0,
            "hbar_q": HBAR_Q,
            "hbar_q_sq": HBAR_Q_SQ,
        },
        "descartes_weierstrass": {
            "p_q0": p,
            "r_q0": r,
            "j_invariant": j,
            "j_target_from_paper": 129.9,
            "j_error": abs(j - 129.9),
        },
        "legendre_lambda": {
            "u_root": u,
            "lambda_pair": [
                {"re": lam.real, "im": lam.imag} for lam in lam_pair
            ],
            "s3_orbit_first_root": [
                {"re": lam.real, "im": lam.imag} for lam in s3_orbit[0]
            ],
        },
        "bloch_wigner_at_lambda": D_values,
        "comparisons": comparisons,
        "ratio_D_lambda_to_v3": [
            D["D"] / D_regular for D in D_values
        ],
        "interpretation": (
            "If ratio_D_lambda_to_v3 == 1, the universal shape parameter "
            "ansatz z_c = lambda(q_0) exactly reproduces Thurston volume "
            "for knots triangulated by regular tetrahedra (figure-8, "
            "knot complement census minimum).  Ratio < 1 means the "
            "universal ansatz UNDER-predicts volume and per-knot gluing "
            "is required.  Ratio > 1 means OVER-prediction."
        ),
    }

    out_path = Path(__file__).parent / "lambda-descartes-q0.witness.json"
    out_path.write_text(json.dumps(witness, indent=2))
    print(f"Wrote {out_path}")
    print(f"  j({'q_0={:.6f}'.format(Q0)}) = {j:.3f}  (paper claims ~129.9)")
    print(f"  u_root = {u:.6f}")
    print(f"  lambda_pair = {lam_pair}")
    print(f"  D(lambda_0) = {D_values[0]['D']:.6f}")
    print(f"  D(lambda_1) = {D_values[1]['D']:.6f}")
    print(f"  D(e^(i pi/3)) = v_3 = {D_regular:.6f}")
    print(f"  ratio(lambda_0 / regular) = {D_values[0]['D']/D_regular:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
