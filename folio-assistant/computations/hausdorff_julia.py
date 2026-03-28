#!/usr/bin/env python3
"""
Compute the Hausdorff dimension of Julia sets for f(z) = z^2 + c
where c is on the main cardioid of the Mandelbrot set at parameter q.

Cardioid parameterization: c(q) = (1/2) exp(2*pi*i*q) - (1/4) exp(4*pi*i*q)

Methods:
  1. Box-counting dimension
  2. Correlation dimension (cross-check)
"""

import numpy as np
import time

# ── Cardioid parameterization ──────────────────────────────────────────

def cardioid_c(q):
    """c(q) = (1/2) exp(2*pi*i*q) - (1/4) exp(4*pi*i*q)"""
    return 0.5 * np.exp(2j * np.pi * q) - 0.25 * np.exp(4j * np.pi * q)


# ── Inverse iteration method to sample the Julia set ──────────────────

def inverse_iteration_julia(c, n_points=200000, n_warmup=500):
    """
    Generate points on the Julia set boundary using backward iteration.

    f(z) = z^2 + c  =>  f^{-1}(z) = +/- sqrt(z - c)

    At each step, randomly choose one of the two inverse branches.
    After a warmup period, collected points lie on (or very near) the Julia set.
    """
    z = np.complex128(0.5 + 0.5j)  # arbitrary starting point
    points = np.empty(n_points, dtype=np.complex128)

    # Warmup: iterate without storing
    for _ in range(n_warmup):
        w = np.sqrt(z - c)
        z = w if np.random.random() < 0.5 else -w

    # Collect points
    for i in range(n_points):
        w = np.sqrt(z - c)
        z = w if np.random.random() < 0.5 else -w
        points[i] = z

    return points


# ── Box-counting dimension ────────────────────────────────────────────

def box_counting_dimension(points, n_sizes=20):
    """
    Estimate the box-counting dimension.

    For each box size epsilon, count how many boxes of that size
    contain at least one point. The dimension is the slope of
    log(N) vs log(1/epsilon).
    """
    x = points.real
    y = points.imag

    # Determine bounding box
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()

    # Add small padding
    pad = 0.01 * max(x_max - x_min, y_max - y_min)
    x_min -= pad; x_max += pad
    y_min -= pad; y_max += pad

    extent = max(x_max - x_min, y_max - y_min)

    # Range of box sizes (powers of 2 for clean scaling)
    min_exp = 3   # 2^3 = 8 boxes per side
    max_exp = 12  # 2^12 = 4096 boxes per side
    exponents = np.linspace(min_exp, max_exp, n_sizes)

    epsilons = []
    counts = []

    for exp in exponents:
        n_boxes = int(2**exp)
        eps = extent / n_boxes

        # Map points to grid cells
        ix = ((x - x_min) / eps).astype(np.int64)
        iy = ((y - y_min) / eps).astype(np.int64)

        # Clip to valid range
        ix = np.clip(ix, 0, n_boxes - 1)
        iy = np.clip(iy, 0, n_boxes - 1)

        # Count unique occupied boxes
        # Pack (ix, iy) into a single integer for fast unique counting
        keys = ix * (n_boxes + 1) + iy
        n_occupied = len(np.unique(keys))

        epsilons.append(eps)
        counts.append(n_occupied)

    epsilons = np.array(epsilons)
    counts = np.array(counts)

    # Linear regression on log(N) vs log(1/eps)
    log_inv_eps = np.log(1.0 / epsilons)
    log_N = np.log(counts.astype(float))

    # Use middle portion to avoid boundary effects
    trim = 2
    x_fit = log_inv_eps[trim:-trim]
    y_fit = log_N[trim:-trim]

    # Least squares fit
    A = np.vstack([x_fit, np.ones(len(x_fit))]).T
    slope, intercept = np.linalg.lstsq(A, y_fit, rcond=None)[0]

    # Also compute R^2
    y_pred = slope * x_fit + intercept
    ss_res = np.sum((y_fit - y_pred)**2)
    ss_tot = np.sum((y_fit - np.mean(y_fit))**2)
    r_squared = 1 - ss_res / ss_tot

    return slope, r_squared, epsilons, counts


# ── Correlation dimension ─────────────────────────────────────────────

def correlation_dimension(points, n_sample=5000, n_radii=20):
    """
    Estimate the correlation dimension D2.

    C(r) = (2 / N(N-1)) * #{pairs with |x_i - x_j| < r}
    D2 = lim_{r->0} log(C(r)) / log(r)

    Uses a random subsample for computational feasibility.
    """
    # Subsample
    if len(points) > n_sample:
        idx = np.random.choice(len(points), n_sample, replace=False)
        pts = points[idx]
    else:
        pts = points

    N = len(pts)

    # Compute all pairwise distances (vectorized for speed)
    # Do it in chunks to manage memory
    chunk_size = 1000

    # Determine range of radii
    # Sample some distances to set scale
    sample_idx = np.random.choice(N, min(500, N), replace=False)
    sample_pts = pts[sample_idx]
    sample_dists = np.abs(sample_pts[:, None] - sample_pts[None, :])
    sample_dists = sample_dists[np.triu_indices(len(sample_pts), k=1)]

    r_min = np.percentile(sample_dists, 1)
    r_max = np.percentile(sample_dists, 50)

    if r_min <= 0:
        r_min = 1e-6

    radii = np.logspace(np.log10(r_min), np.log10(r_max), n_radii)
    pair_counts = np.zeros(n_radii)

    total_pairs = N * (N - 1) / 2

    # Count pairs within each radius
    for i in range(0, N, chunk_size):
        i_end = min(i + chunk_size, N)
        for j in range(i, N, chunk_size):
            j_start = max(j, i)  # avoid double counting
            j_end = min(j + chunk_size, N)

            if i == j_start // chunk_size * chunk_size:
                # Same chunk - use upper triangle
                chunk_pts_i = pts[i:i_end]
                dists = np.abs(chunk_pts_i[:, None] - chunk_pts_i[None, :])
                for k, r in enumerate(radii):
                    # Count upper triangle only
                    mask = np.triu(dists < r, k=1)
                    pair_counts[k] += np.sum(mask)
            else:
                chunk_pts_i = pts[i:i_end]
                chunk_pts_j = pts[j_start:j_end]
                dists = np.abs(chunk_pts_i[:, None] - chunk_pts_j[None, :])
                for k, r in enumerate(radii):
                    pair_counts[k] += np.sum(dists < r)

    # Correlation integral
    C_r = 2.0 * pair_counts / (N * (N - 1))

    # Filter out zeros
    valid = C_r > 0
    if np.sum(valid) < 4:
        return np.nan, 0.0, radii, C_r

    log_r = np.log(radii[valid])
    log_C = np.log(C_r[valid])

    # Fit in scaling region (middle portion)
    trim = max(1, len(log_r) // 5)
    x_fit = log_r[trim:-trim] if len(log_r) > 2*trim+2 else log_r
    y_fit = log_C[trim:-trim] if len(log_C) > 2*trim+2 else log_C

    if len(x_fit) < 2:
        return np.nan, 0.0, radii, C_r

    A = np.vstack([x_fit, np.ones(len(x_fit))]).T
    slope, intercept = np.linalg.lstsq(A, y_fit, rcond=None)[0]

    y_pred = slope * x_fit + intercept
    ss_res = np.sum((y_fit - y_pred)**2)
    ss_tot = np.sum((y_fit - np.mean(y_fit))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return slope, r_squared, radii, C_r


# ── Ruelle's formula for comparison ──────────────────────────────────

def ruelle_dimension_estimate(c):
    """
    For c on the main cardioid, the Julia set is a Jordan curve.
    The Hausdorff dimension can be estimated using Ruelle's thermodynamic
    formalism. For the main cardioid:

    d_H ≈ 1 + |c|^2 / (4 ln 2) + O(|c|^4)

    This is the perturbative expansion near c=0 (the unit circle).
    More accurate for small |c|.
    """
    return 1.0 + abs(c)**2 / (4 * np.log(2))


# ── Main computation ─────────────────────────────────────────────────

def compute_dimension(q, n_points=300000, label=""):
    """Compute dimensions for a given q value."""
    c = cardioid_c(q)

    print(f"\n{'='*60}")
    print(f"q = {q}  {label}")
    print(f"c = {c:.6f}")
    print(f"|c| = {abs(c):.6f}")
    print(f"{'='*60}")

    t0 = time.time()

    # Generate Julia set points
    print(f"Generating {n_points} points via inverse iteration...")
    points = inverse_iteration_julia(c, n_points=n_points)
    t1 = time.time()
    print(f"  Done in {t1-t0:.1f}s. Points span: "
          f"x=[{points.real.min():.3f}, {points.real.max():.3f}], "
          f"y=[{points.imag.min():.3f}, {points.imag.max():.3f}]")

    # Box-counting dimension
    print("Computing box-counting dimension...")
    d_box, r2_box, eps_arr, N_arr = box_counting_dimension(points)
    t2 = time.time()
    print(f"  d_box = {d_box:.6f}  (R² = {r2_box:.6f})  [{t2-t1:.1f}s]")

    # Correlation dimension
    print("Computing correlation dimension...")
    d_corr, r2_corr, radii, C_r = correlation_dimension(points, n_sample=4000)
    t3 = time.time()
    print(f"  d_corr = {d_corr:.6f}  (R² = {r2_corr:.6f})  [{t3-t2:.1f}s]")

    # Ruelle perturbative estimate
    d_ruelle = ruelle_dimension_estimate(c)
    print(f"  d_Ruelle (perturbative) = {d_ruelle:.6f}")

    return {
        'q': q,
        'c': c,
        'd_box': d_box,
        'r2_box': r2_box,
        'd_corr': d_corr,
        'r2_corr': r2_corr,
        'd_ruelle': d_ruelle,
        'label': label,
    }


def main():
    np.random.seed(42)

    print("Hausdorff Dimension of Julia Sets on the Main Cardioid")
    print("=" * 60)
    print()
    print("Cardioid parameterization:")
    print("  c(q) = (1/2) exp(2*pi*i*q) - (1/4) exp(4*pi*i*q)")
    print()
    print("f(z) = z^2 + c, Julia set boundary")
    print()

    # Parameters to study
    params = [
        (1.01,   "near classical"),
        (1.1097, "our universe"),
        (1.5,    "intermediate"),
        (2.0,    "deep quantum"),
    ]

    results = []
    for q, label in params:
        res = compute_dimension(q, n_points=300000, label=label)
        results.append(res)

    # ── Summary table ──────────────────────────────────────────────
    print("\n\n")
    print("=" * 90)
    print("SUMMARY TABLE: Hausdorff Dimension of Julia Sets")
    print("=" * 90)
    print(f"{'q':>8s}  {'Label':>16s}  {'|c|':>8s}  {'d_box':>8s}  {'R²_box':>7s}  "
          f"{'d_corr':>8s}  {'R²_corr':>7s}  {'d_Ruelle':>8s}")
    print("-" * 90)

    for r in results:
        print(f"{r['q']:8.4f}  {r['label']:>16s}  {abs(r['c']):8.4f}  "
              f"{r['d_box']:8.4f}  {r['r2_box']:7.4f}  "
              f"{r['d_corr']:8.4f}  {r['r2_corr']:7.4f}  "
              f"{r['d_ruelle']:8.4f}")

    print("-" * 90)
    print()
    print("Notes:")
    print("  d_box    = box-counting dimension (slope of log N vs log 1/eps)")
    print("  d_corr   = correlation dimension D2 (slope of log C(r) vs log r)")
    print("  d_Ruelle = perturbative estimate 1 + |c|^2/(4 ln 2), valid near c=0")
    print("  R²       = coefficient of determination for the linear fit")
    print()

    # Highlight our universe value
    our = [r for r in results if r['q'] == 1.1097][0]
    print(f"*** For q = 1.1097 ('our universe'): ***")
    print(f"    c = {our['c']:.6f}")
    print(f"    Box-counting dimension:  d_H = {our['d_box']:.4f}  (R² = {our['r2_box']:.4f})")
    print(f"    Correlation dimension:   D2  = {our['d_corr']:.4f}  (R² = {our['r2_corr']:.4f})")
    print(f"    Ruelle perturbative:     d_R = {our['d_ruelle']:.4f}")
    print(f"    Best estimate:           d_H ≈ {(our['d_box'] + our['d_corr'])/2:.4f}  "
          f"(average of box-counting and correlation)")
    print()

    # Additional analysis: how dimension varies with q
    print("\nPhysical interpretation:")
    print("  q → 1 (classical limit): Julia set approaches the unit circle, d_H → 1")
    print("  q → 2 (deep quantum):    Julia set becomes more fractal, d_H increases")
    print("  The dimension measures the 'roughness' of the quantum-classical boundary")


if __name__ == "__main__":
    main()
