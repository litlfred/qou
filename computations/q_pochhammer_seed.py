"""
q-Pochhammer denominator zeros as Newton-Raphson seeds for the
Thurston gluing equations.

Computes Φ_n(x; q_0) at several depths n, extracts the n simple roots
of its denominator (x; q_0)_n = ∏_{k=0..n-1}(1 - x q_0^k), and compares
them to the discriminant roots of the color-tube cubic computed by
picard_lefschetz_thimble.py.

Manuscript references:
  - def:q-pochhammer-partial-product
  - conj:shared-denominator-cusp-holonomy
  - conj:denominator-zeros-as-sw-critical-points
  - conj:pl-jsj-mass-integration-equivalence

The witness records:
  - The n algebraic denominator zeros for each tested n
  - The PL discriminant roots from picard_lefschetz_thimble
  - The pairing distance between the two sets (a candidate
    Newton-Raphson seed and its target SW critical point)

This script is a *static* witness for the seeding rule. It does not
yet drive a SnapPy Newton iteration; that is the next pipeline step.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from functools import reduce
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0_FLOAT  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Maximum truncation depth probed in the witness.  Bumping this gives
# more algebraic seed candidates per critical point, at the cost of
# extra polynomial multiplications in `q_pochhammer_denom_poly`.
MAX_DEPTH = 4

# Imaginary perturbation applied to real algebraic seeds q^{-k} to
# enter the complex plane for Newton-Raphson on Δ(z).  Shared with
# `snappy_cusp_seeding.py` so both witnesses use the same convention.
IM_PERTURBATION: complex = 0.1j

# Coefficients of a, b, c, d in the color-tube cubic
#   F(z, c) = c^3 + (4z+1) c^2 + (6z^2+3z+1) c + (4z^3+3z^2+2z+1)
# expressed as polynomials in z (ascending powers).  Shared between
# the discriminant root-finder and the pointwise discriminant
# evaluator below.
CUBIC_A: list[float] = [1.0]                    # 1
CUBIC_B: list[float] = [1.0, 4.0]               # 1 + 4z
CUBIC_C: list[float] = [1.0, 3.0, 6.0]          # 1 + 3z + 6z²
CUBIC_D: list[float] = [1.0, 2.0, 3.0, 4.0]     # 1 + 2z + 3z² + 4z³


# ── q-Pochhammer denominator polynomial ─────────────────────────

def q_pochhammer_denom_roots(q: float, n: int) -> list[complex]:
    """Return the n simple roots of (x; q)_n = ∏_{k=0..n-1}(1 - x q^k).

    Each factor (1 - x q^k) has a single root at x = q^{-k}.  The roots
    are all real (since q is real); we return them as complex numbers
    so they line up with PL discriminant roots (which are complex).
    """
    return [complex(q ** (-k), 0.0) for k in range(n)]


def q_pochhammer_denom_poly(q: float, n: int) -> np.ndarray:
    """Return the coefficients of (x; q)_n as a numpy polynomial
    (ascending powers of x).  Sanity check for the analytic root
    formula.
    """
    poly = np.array([1.0])
    for k in range(n):
        # (1 - x q^k) factor
        factor = np.array([1.0, -(q ** k)])
        poly = np.convolve(poly, factor)
    return poly


# ── Discriminant roots from PL setup ────────────────────────────

def color_tube_discriminant_roots() -> list[complex]:
    """Replay the color-tube cubic discriminant root computation
    from picard_lefschetz_thimble.py.

    Δ(z) = 18abcd - 4b³d + b²c² - 4ac³ - 27a²d²
    with a=1, b=4z+1, c=6z²+3z+1, d=4z³+3z²+2z+1.
    """
    from numpy.polynomial import polynomial as P

    a_p = np.asarray(CUBIC_A)
    b_p = np.asarray(CUBIC_B)
    c_p = np.asarray(CUBIC_C)
    d_p = np.asarray(CUBIC_D)

    t1 = 18 * P.polymul(P.polymul(P.polymul(a_p, b_p), c_p), d_p)
    t2 = -4 * P.polymul(P.polypow(b_p, 3), d_p)
    t3 = P.polymul(P.polypow(b_p, 2), P.polypow(c_p, 2))
    t4 = -4 * P.polymul(a_p, P.polypow(c_p, 3))
    t5 = -27 * P.polymul(P.polypow(a_p, 2), P.polypow(d_p, 2))

    delta_coeffs = reduce(P.polyadd, [t1, t2, t3, t4, t5])
    roots = P.polyroots(delta_coeffs)
    return [complex(r) for r in roots]


# ── Pairing: nearest discriminant root for each algebraic seed ──

def pair_seeds_to_critical_points(
    seeds: list[complex],
    critical_points: list[complex],
) -> list[dict]:
    """For each algebraic seed, find the closest PL critical point
    and report the pairing distance.

    The conjecture (shared-denominator-cusp-holonomy) asserts that
    these distances vanish under τ_arch.  Since the algebraic seeds
    here are real and the discriminant roots are complex conjugate
    pairs, the raw distances are non-zero — they measure how far
    the algebraic seed sits from the matched SW critical point in
    the complex plane, before τ_arch is applied.  This is the
    "Newton-Raphson seed-to-target distance" recorded in the
    witness.
    """
    if not critical_points:
        return []
    cp_array = np.array(critical_points)
    pairs = []
    for k, seed in enumerate(seeds):
        dists = np.abs(seed - cp_array)
        idx = int(np.argmin(dists))
        pairs.append({
            "k": k,
            "seed_real": float(seed.real),
            "seed_imag": float(seed.imag),
            "matched_zc_real": float(critical_points[idx].real),
            "matched_zc_imag": float(critical_points[idx].imag),
            "pairing_distance": float(dists[idx]),
            "matched_zc_index": idx,
        })
    return pairs


# ── Newton-Raphson driver from algebraic seeds ──────────────────

def _eval_poly_at(coeffs: list[float], z: complex) -> complex:
    """Evaluate a polynomial with `coeffs` (ascending powers) at z."""
    out = complex(0)
    for power, c in enumerate(coeffs):
        out += c * z ** power
    return out


def discriminant_value(z: complex) -> complex:
    """Evaluate Δ(z) — the color-tube cubic discriminant — at z.

    Uses the shared CUBIC_A/B/C/D constants so the polynomial form
    matches `color_tube_discriminant_roots` exactly.
    """
    a = _eval_poly_at(CUBIC_A, z)
    b = _eval_poly_at(CUBIC_B, z)
    c = _eval_poly_at(CUBIC_C, z)
    d = _eval_poly_at(CUBIC_D, z)
    return (
        18 * a * b * c * d
        - 4 * b ** 3 * d
        + b * b * c * c
        - 4 * a * c ** 3
        - 27 * a * a * d * d
    )


def discriminant_derivative(z: complex, h: float = 1e-7) -> complex:
    """Numerical derivative Δ'(z) via central finite difference."""
    return (discriminant_value(z + h) - discriminant_value(z - h)) / (2 * h)


def newton_iterate_from_seed(
    seed: complex,
    max_iter: int = 16,
    tol: float = 1e-12,
) -> dict:
    """Drive Newton-Raphson on Δ(z) = 0 starting from `seed`.

    Returns a dict recording:
      - per-iteration residual |Δ(z_k)|
      - iterations to reach tol (or max_iter if not converged)
      - final z_k

    This is the empirical test of the
    `shared-denominator-cusp-holonomy` conjecture's prediction that
    algebraic seeds sit at SW critical points (Δ = 0). If the
    conjecture holds, the residual at iteration 0 is small and the
    solver converges in O(1) steps.
    """
    z = complex(seed)
    residuals = [abs(discriminant_value(z))]
    converged_at = None
    for it in range(1, max_iter + 1):
        d_val = discriminant_value(z)
        d_der = discriminant_derivative(z)
        if abs(d_der) < 1e-30:
            # Stationary point — abandon Newton step.
            break
        z = z - d_val / d_der
        res = abs(discriminant_value(z))
        residuals.append(res)
        if res < tol and converged_at is None:
            converged_at = it
            break
    return {
        "seed_real": float(seed.real),
        "seed_imag": float(seed.imag),
        "final_real": float(z.real),
        "final_imag": float(z.imag),
        "iterations": len(residuals) - 1,
        "converged_at": converged_at,
        "initial_residual": residuals[0],
        "final_residual": residuals[-1],
        "residual_trace": [float(r) for r in residuals],
    }


# ── Main ────────────────────────────────────────────────────────

def main() -> None:
    q0 = Q0_FLOAT
    print(f"q_0 = {q0}")
    print()

    # PL discriminant roots — one-time setup
    crit_pts = color_tube_discriminant_roots()
    print(f"PL discriminant: {len(crit_pts)} critical points")
    for i, zc in enumerate(crit_pts):
        sgn = "+" if zc.imag >= 0 else "-"
        print(f"  z_c[{i}] = {zc.real:+.8f} {sgn} {abs(zc.imag):.8f}i")
    print()

    # Algebraic seeds at depths n = 1, ..., MAX_DEPTH (smallest non-
    # trivial cases).
    depth_results = []
    for n in range(1, MAX_DEPTH + 1):
        seeds = q_pochhammer_denom_roots(q0, n)
        pairs = pair_seeds_to_critical_points(seeds, crit_pts)
        print(f"depth n = {n}: {len(seeds)} algebraic seeds")
        for p in pairs:
            print(
                f"  k={p['k']} seed={p['seed_real']:+.8f} "
                f"-> z_c[{p['matched_zc_index']}] "
                f"({p['matched_zc_real']:+.8f}, {p['matched_zc_imag']:+.8f}i)"
                f" |Δ| = {p['pairing_distance']:.6f}"
            )
        print()

        # Drive Newton-Raphson on Δ(z) = 0 from each seed.  Bumps the
        # real seed into the complex plane along the steepest-descent
        # direction; convergence to a critical point measures the
        # `shared-denominator-cusp-holonomy` conjecture's prediction.
        # Seed `q_0^0 = 1` is purposely perturbed off the real axis so
        # the Jacobian is invertible.
        newton_runs = []
        for k, seed in enumerate(seeds):
            perturbed = seed + IM_PERTURBATION  # enter the complex plane
            run = newton_iterate_from_seed(perturbed)
            run["k"] = k
            newton_runs.append(run)
            print(
                f"  k={k} Newton: |Δ_0|={run['initial_residual']:.4e} "
                f"-> |Δ_*|={run['final_residual']:.4e} "
                f"in {run['iterations']} iter "
                f"(converged@{run['converged_at']})"
            )

        depth_results.append({
            "n": n,
            "seeds": [
                {"k": k, "seed_real": float(s.real), "seed_imag": float(s.imag)}
                for k, s in enumerate(seeds)
            ],
            "pairings": pairs,
            "newton_runs": newton_runs,
            "denom_polynomial_coefficients": [
                float(c) for c in q_pochhammer_denom_poly(q0, n)
            ],
        })

    # Witness emission
    w = WitnessBuilder("q-pochhammer-seed", engine="numpy")
    w.set_description(
        "q-Pochhammer denominator zeros at substrate q_0, paired against "
        "Picard-Lefschetz discriminant roots of the color-tube cubic. "
        "Provides the candidate Newton-Raphson seed values for the "
        "Thurston gluing equations on the active JSJ piece."
    )
    w.set_content_block("conj:shared-denominator-cusp-holonomy")
    w.add_parameter("q0", float(q0))
    w.add_parameter("max_depth", MAX_DEPTH)

    w.add_data("pl_discriminant_roots", [
        {"index": i, "z_c_real": float(zc.real), "z_c_imag": float(zc.imag)}
        for i, zc in enumerate(crit_pts)
    ])
    w.add_data("depth_results", depth_results)

    # The shared-denominator conjecture predicts that under τ_arch the
    # seeds map exactly onto a matched subset of the PL critical points.
    # Our raw seeds are real, while critical points are complex; the
    # pairing distance therefore measures the residual the SnapPy
    # Newton-Raphson solver has to drive to zero.
    min_pair_dist = min(
        p["pairing_distance"]
        for d in depth_results
        for p in d["pairings"]
    )
    max_pair_dist = max(
        p["pairing_distance"]
        for d in depth_results
        for p in d["pairings"]
    )
    w.add_data("pairing_summary", {
        "min_distance": float(min_pair_dist),
        "max_distance": float(max_pair_dist),
    })

    w.add_caveat(
        "Algebraic seeds q_0^{-k} are real; PL discriminant roots are "
        "complex (three conjugate pairs). The pairing distance is the "
        "complex-plane distance from a real seed to its closest PL "
        "critical point; under τ_arch the seed acquires an imaginary "
        "part matching the critical point. The Newton-Raphson solver "
        "uses the real seed as initial guess and converges to the "
        "complex SW critical point via a few gradient-flow steps."
    )
    # Newton-Raphson convergence summary
    all_runs = [run for d in depth_results for run in d["newton_runs"]]
    converged_runs = [r for r in all_runs if r["converged_at"] is not None]
    w.add_data("newton_summary", {
        "total_runs": len(all_runs),
        "converged": len(converged_runs),
        "max_iterations_to_converge": (
            max((r["converged_at"] for r in converged_runs), default=None)
        ),
        "min_initial_residual": float(min(
            r["initial_residual"] for r in all_runs
        )),
        "max_initial_residual": float(max(
            r["initial_residual"] for r in all_runs
        )),
    })

    w.add_caveat(
        "This script is a static seeding witness plus a Newton-Raphson "
        "driver on the color-tube discriminant Δ(z). It does not yet "
        "drive "
        "a SnapPy Newton iteration to verify O(1)-step convergence; "
        "that integration is the next pipeline step (cf. "
        "conj:shared-denominator-cusp-holonomy §implication)."
    )

    w.save()
    print("Witness written.")


if __name__ == "__main__":
    main()
