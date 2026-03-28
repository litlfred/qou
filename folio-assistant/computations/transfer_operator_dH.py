#!/usr/bin/env python3
"""
Transfer-operator computation of the Hausdorff dimension of the Julia set
for f(z) = z^2 + c on the main cardioid at the QOU substrate parameter
q = 1.1097.

Method (Bowen 1979, Ruelle 1982):
  The Hausdorff dimension d_H of the Julia set J(f) is the unique real
  number t such that the topological pressure vanishes:

      P(-t log|f'|) = 0.

  For f(z) = z^2 + c with c on the main cardioid, the Julia set is a
  quasicircle and f is conformally conjugate to z -> z^2 on the unit
  circle. The Ruelle transfer operator

      (L_t g)(z) = sum_{f(w)=z} |f'(w)|^{-t} g(w)

  has two inverse branches w_{\pm} = \pm sqrt(z - c), with derivatives
  f'(w) = 2w, so

      (L_t g)(z) = |2 w_+(z)|^{-t} g(w_+(z)) + |2 w_-(z)|^{-t} g(w_-(z)).

  The pressure P(t) = log(spectral_radius(L_t)). Setting P(t)=0 means
  finding the t where the leading eigenvalue of L_t equals 1.

Implementation:
  We discretize L_t on a grid of N points on (or near) the Julia set,
  approximate it as an N x N matrix, and find its leading eigenvalue
  via scipy.sparse.linalg.eigs. The dimension d_H is found by bisection
  on t where the leading eigenvalue crosses 1.

References:
  [bowen1979]  R. Bowen, "Hausdorff dimension of quasi-circles",
               Publ. Math. IHES 50 (1979), 11-25.
  [ruelle1982] D. Ruelle, "Repellers for real analytic maps",
               Ergodic Theory Dyn. Syst. 2 (1982), 99-107.
  [zinsmeister2000] M. Zinsmeister, "Thermodynamic Formalism and
               Holomorphic Dynamical Systems", SMF/AMS Texts (2000).
"""

import json
import time
from datetime import datetime, timezone

import numpy as np
from scipy import linalg as la


# ── Cardioid parameterization ──────────────────────────────────────────

def cardioid_c(q):
    """c(q) = (1/2) exp(2*pi*i*q) - (1/4) exp(4*pi*i*q)."""
    return 0.5 * np.exp(2j * np.pi * q) - 0.25 * np.exp(4j * np.pi * q)


# ── Julia set sampling via inverse iteration ──────────────────────────

def sample_julia_set(c, n_points=5000, n_warmup=1000):
    """
    Generate points on the Julia set boundary using backward iteration.
    f^{-1}(z) = +/- sqrt(z - c). After warmup, points converge to J(f).
    """
    rng = np.random.default_rng(42)
    z = np.complex128(0.5 + 0.5j)

    for _ in range(n_warmup):
        w = np.sqrt(z - c)
        z = w if rng.random() < 0.5 else -w

    points = np.empty(n_points, dtype=np.complex128)
    for i in range(n_points):
        w = np.sqrt(z - c)
        z = w if rng.random() < 0.5 else -w
        points[i] = z

    return points


# ── Transfer operator on Julia set grid ───────────────────────────────

def build_transfer_operator_matrix(c, grid_points, t):
    """
    Build the N x N matrix approximation to the Ruelle transfer operator

        (L_t g)(z) = sum_{f(w)=z} |f'(w)|^{-t} g(w)

    for f(z) = z^2 + c.

    The two inverse branches are w_{+/-}(z) = +/- sqrt(z - c).
    The derivative is f'(w) = 2w, so the weight is |2w|^{-t}.

    We approximate: for each grid point z_j, compute the two preimages
    w_+ and w_-, then express g(w_+/-) as a weighted combination of
    the grid values using a Gaussian kernel interpolation.

    Parameters
    ----------
    c : complex
        Parameter c on the main cardioid.
    grid_points : ndarray of complex
        N points on or near the Julia set.
    t : float
        Exponent parameter. d_H is the t where leading eigenvalue = 1.

    Returns
    -------
    L : ndarray, shape (N, N)
        Matrix approximation to L_t.
    """
    N = len(grid_points)
    L = np.zeros((N, N), dtype=np.float64)

    # Bandwidth for Gaussian kernel interpolation.
    # Set adaptively based on typical inter-point spacing.
    dists = np.abs(grid_points[:, None] - grid_points[None, :])
    np.fill_diagonal(dists, np.inf)
    min_dists = np.min(dists, axis=1)
    sigma = np.median(min_dists) * 1.5

    for j in range(N):
        z_j = grid_points[j]

        for sign in [1.0, -1.0]:
            # Inverse branch: w = sign * sqrt(z_j - c)
            w = sign * np.sqrt(z_j - c)

            # Weight: |f'(w)|^{-t} = |2w|^{-t}
            abs_deriv = abs(2.0 * w)
            if abs_deriv < 1e-15:
                continue
            weight = abs_deriv ** (-t)

            # Kernel interpolation: approximate delta(z - w) on the grid
            # using a Gaussian kernel
            displacements = np.abs(grid_points - w)
            kernel = np.exp(-0.5 * (displacements / sigma) ** 2)
            kernel_sum = np.sum(kernel)
            if kernel_sum < 1e-30:
                continue
            kernel /= kernel_sum

            # L[i, j] += weight * kernel[i] means:
            # (L_t g)(z_i) gets contribution weight * g(w) where g(w)
            # is interpolated from grid values
            L[:, j] += weight * kernel

    return L


def leading_eigenvalue(L):
    """Compute the leading (largest magnitude) eigenvalue of L."""
    eigenvalues = la.eigvals(L)
    return np.max(np.abs(eigenvalues))


# ── Bisection to find d_H ────────────────────────────────────────────

def find_hausdorff_dimension(c, grid_points, t_low=0.8, t_high=1.5,
                             tol=1e-6, max_iter=60, verbose=True):
    """
    Find d_H by bisection: the unique t where the leading eigenvalue
    of L_t equals 1, i.e., the spectral radius crosses 1.

    The spectral radius rho(L_t) is a decreasing function of t:
      - At t=0, L_0 is a Markov-type operator with rho >= 2
        (two branches each contributing ~1).
      - As t increases, the weights |2w|^{-t} shrink, reducing rho.
      - d_H is where rho(L_t) = 1.

    Parameters
    ----------
    c : complex
        Main cardioid parameter.
    grid_points : ndarray
        Discretization points on the Julia set.
    t_low, t_high : float
        Bracket for bisection.
    tol : float
        Convergence tolerance on t.
    max_iter : int
        Maximum bisection iterations.
    verbose : bool
        Print convergence info.

    Returns
    -------
    t_star : float
        Estimated Hausdorff dimension.
    history : list of (t, rho) tuples
        Bisection history.
    """
    history = []

    # Verify bracket: rho(t_low) > 1 and rho(t_high) < 1
    L_low = build_transfer_operator_matrix(c, grid_points, t_low)
    rho_low = leading_eigenvalue(L_low)

    L_high = build_transfer_operator_matrix(c, grid_points, t_high)
    rho_high = leading_eigenvalue(L_high)

    if verbose:
        print(f"  Bracket: rho({t_low:.4f}) = {rho_low:.6f}, "
              f"rho({t_high:.4f}) = {rho_high:.6f}")

    if rho_low < 1.0:
        print(f"  WARNING: rho(t_low) = {rho_low:.6f} < 1. "
              f"Lowering t_low.")
        t_low = max(0.5, t_low - 0.3)
    if rho_high > 1.0:
        print(f"  WARNING: rho(t_high) = {rho_high:.6f} > 1. "
              f"Raising t_high.")
        t_high = min(2.0, t_high + 0.3)

    for iteration in range(max_iter):
        t_mid = 0.5 * (t_low + t_high)
        L_mid = build_transfer_operator_matrix(c, grid_points, t_mid)
        rho_mid = leading_eigenvalue(L_mid)
        history.append((t_mid, rho_mid))

        if verbose and (iteration < 5 or iteration % 5 == 0):
            print(f"    iter {iteration:2d}: t = {t_mid:.8f}, "
                  f"rho = {rho_mid:.8f}")

        if rho_mid > 1.0:
            t_low = t_mid
        else:
            t_high = t_mid

        if t_high - t_low < tol:
            break

    t_star = 0.5 * (t_low + t_high)
    if verbose:
        print(f"  Converged: d_H = {t_star:.8f} "
              f"(bracket width {t_high - t_low:.2e})")

    return t_star, history


# ── Ruelle perturbative estimate ─────────────────────────────────────

def ruelle_perturbative(c):
    """
    First-order perturbative expansion (Ruelle 1982):

        d_H = 1 + |c|^2 / (4 ln 2) + O(|c|^4)

    Valid for c near 0 (i.e., near the cusp of the cardioid).
    """
    return 1.0 + abs(c) ** 2 / (4.0 * np.log(2))


def ruelle_second_order(c):
    """
    Second-order perturbative expansion including the |c|^4 correction.

    From Zinsmeister (2000), eq. (5.3):
        d_H = 1 + |c|^2/(4 ln 2) + O(|c|^4)

    The second-order coefficient depends on the Fourier spectrum of
    the conformal map. For the quadratic family a numerical estimate
    gives approximately:
        d_H ~ 1 + |c|^2/(4 ln 2) + (3/2)|c|^4/(4 ln 2)^2
    """
    a = abs(c) ** 2 / (4.0 * np.log(2))
    return 1.0 + a + 1.5 * a ** 2


# ── QOU prediction ───────────────────────────────────────────────────

def qou_prediction(q):
    """
    QOU-theoretic prediction for the Hausdorff dimension:

        d_H = (2q - 1)^2 / q^3
    """
    return (2.0 * q - 1.0) ** 2 / q ** 3


# ── Convergence study ────────────────────────────────────────────────

def convergence_study(c, grid_sizes, verbose=True):
    """
    Run the transfer operator computation at multiple grid resolutions
    to demonstrate convergence of d_H.

    Parameters
    ----------
    c : complex
        Cardioid parameter.
    grid_sizes : list of int
        Number of grid points for each run.
    verbose : bool
        Print per-run info.

    Returns
    -------
    results : list of dict
        Per-resolution results with keys 'N', 'd_H', 'time_s'.
    """
    results = []

    for N in grid_sizes:
        if verbose:
            print(f"\n--- Grid size N = {N} ---")

        t0 = time.time()
        grid = sample_julia_set(c, n_points=N, n_warmup=2000)
        d_H, history = find_hausdorff_dimension(
            c, grid, t_low=0.8, t_high=1.5, tol=1e-7, verbose=verbose
        )
        elapsed = time.time() - t0

        results.append({
            'N': N,
            'd_H': d_H,
            'time_s': elapsed,
            'n_bisection_steps': len(history),
        })

        if verbose:
            print(f"  N = {N:5d}, d_H = {d_H:.8f}, time = {elapsed:.1f}s")

    return results


# ── Main ─────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("Transfer-Operator Hausdorff Dimension of the Julia Set")
    print("Bowen-Ruelle thermodynamic formalism: P(-t log|f'|) = 0")
    print("=" * 70)

    # ── Parameters ────────────────────────────────────────────────────
    q = 1.1097
    c = cardioid_c(q)

    print(f"\nSubstrate parameter: q = {q}")
    print(f"Cardioid parameter:  c = {c:.10f}")
    print(f"                    |c| = {abs(c):.10f}")
    print(f"                    arg(c) = {np.degrees(np.angle(c)):.4f} deg")

    # ── Reference values ──────────────────────────────────────────────
    d_ruelle_1 = ruelle_perturbative(c)
    d_ruelle_2 = ruelle_second_order(c)
    d_qou = qou_prediction(q)

    print(f"\nReference values:")
    print(f"  Ruelle perturbative (1st order):  {d_ruelle_1:.8f}")
    print(f"  Ruelle perturbative (2nd order):  {d_ruelle_2:.8f}")
    print(f"  QOU prediction (2q-1)^2/q^3:      {d_qou:.8f}")

    # ── Convergence study ─────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("Convergence study: transfer operator on increasing grid sizes")
    print(f"{'=' * 70}")

    grid_sizes = [50, 100, 200, 400, 800]
    conv_results = convergence_study(c, grid_sizes, verbose=True)

    # ── Summary table ─────────────────────────────────────────────────
    print(f"\n\n{'=' * 70}")
    print("CONVERGENCE TABLE")
    print(f"{'=' * 70}")
    print(f"{'N':>6s}  {'d_H':>12s}  {'Delta':>12s}  {'Steps':>6s}  "
          f"{'Time (s)':>10s}")
    print("-" * 54)

    prev_dH = None
    for r in conv_results:
        delta = abs(r['d_H'] - prev_dH) if prev_dH is not None else float('nan')
        delta_str = f"{delta:.2e}" if prev_dH is not None else "---"
        print(f"{r['N']:6d}  {r['d_H']:12.8f}  {delta_str:>12s}  "
              f"{r['n_bisection_steps']:6d}  {r['time_s']:10.1f}")
        prev_dH = r['d_H']

    # Best estimate: use the largest grid
    best = conv_results[-1]
    d_H_best = best['d_H']

    print(f"\nBest transfer-operator estimate (N={best['N']}): "
          f"d_H = {d_H_best:.8f}")

    # ── Comparison ────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("COMPARISON OF METHODS")
    print(f"{'=' * 70}")
    print(f"  Transfer operator (N={best['N']}):     d_H = {d_H_best:.6f}")
    print(f"  Ruelle 1st order:                 d_H = {d_ruelle_1:.6f}")
    print(f"  Ruelle 2nd order:                 d_H = {d_ruelle_2:.6f}")
    print(f"  QOU prediction (2q-1)^2/q^3:      d_H = {d_qou:.6f}")

    print(f"\n  Transfer op. vs Ruelle 1st:  "
          f"Delta = {abs(d_H_best - d_ruelle_1):.6f}")
    print(f"  Transfer op. vs Ruelle 2nd:  "
          f"Delta = {abs(d_H_best - d_ruelle_2):.6f}")
    print(f"  Transfer op. vs QOU:         "
          f"Delta = {abs(d_H_best - d_qou):.6f}")
    print(f"  Ruelle 1st vs QOU:           "
          f"Delta = {abs(d_ruelle_1 - d_qou):.6f}")

    # ── Analysis ──────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("ANALYSIS")
    print(f"{'=' * 70}")
    print(f"""
For q = {q} on the main cardioid, the Julia set is a quasicircle
(a Jordan curve that is not smooth). Its Hausdorff dimension exceeds 1
by an amount controlled by |c|^2.

The transfer operator method discretizes the Ruelle operator L_t on
a grid of points sampled from the Julia set. The dimension d_H is the
unique t where the leading eigenvalue of L_t equals 1 (vanishing
pressure).

The Ruelle perturbative estimate d_H = 1 + |c|^2/(4 ln 2) is a
first-order approximation valid for small |c|. For |c| = {abs(c):.4f},
higher-order corrections are modest but measurable.

The QOU prediction d_H = (2q-1)^2/q^3 = {d_qou:.6f} is a distinct
theoretical formula from the substrate framework. Its deviation from
the numerical transfer-operator value quantifies the gap between the
QOU ansatz and classical conformal dynamics.
""")

    # ── Witness JSON ──────────────────────────────────────────────────
    witness = {
        "computation": "transfer-operator-hausdorff-dimension",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Hausdorff dimension of the Julia set for f(z)=z^2+c "
            "at q=1.1097 via the Ruelle transfer operator. "
            "d_H is the unique t where the spectral radius of L_t = 1 "
            "(Bowen-Ruelle thermodynamic formalism)."
        ),
        "substrate_parameter": {
            "q": q,
            "c_real": float(c.real),
            "c_imag": float(c.imag),
            "c_abs": float(abs(c)),
        },
        "method": {
            "name": "Ruelle transfer operator bisection",
            "description": (
                "Discretize L_t on N Julia set points, compute leading "
                "eigenvalue, bisect on t until spectral_radius(L_t)=1."
            ),
            "reference": "Bowen 1979, Ruelle 1982, Zinsmeister 2000",
        },
        "results": {
            "d_H_transfer_operator": {
                "value": round(d_H_best, 8),
                "grid_size": best['N'],
                "method": "transfer operator bisection",
            },
            "d_H_ruelle_first_order": {
                "value": round(d_ruelle_1, 8),
                "formula": "1 + |c|^2 / (4 ln 2)",
            },
            "d_H_ruelle_second_order": {
                "value": round(d_ruelle_2, 8),
                "formula": "1 + |c|^2/(4 ln 2) + (3/2)(|c|^2/(4 ln 2))^2",
            },
            "d_H_qou_prediction": {
                "value": round(d_qou, 8),
                "formula": "(2q - 1)^2 / q^3",
            },
        },
        "convergence": [
            {
                "N": r['N'],
                "d_H": round(r['d_H'], 8),
                "time_s": round(r['time_s'], 2),
                "bisection_steps": r['n_bisection_steps'],
            }
            for r in conv_results
        ],
        "deviations": {
            "transfer_vs_ruelle_1st": round(abs(d_H_best - d_ruelle_1), 8),
            "transfer_vs_ruelle_2nd": round(abs(d_H_best - d_ruelle_2), 8),
            "transfer_vs_qou": round(abs(d_H_best - d_qou), 8),
            "ruelle_1st_vs_qou": round(abs(d_ruelle_1 - d_qou), 8),
        },
    }

    witness_path = "transfer_operator_dH.witness.json"
    with open(witness_path, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"Witness data written to {witness_path}")


if __name__ == "__main__":
    main()
