#!/usr/bin/env python3
"""
Mod-p Mandelbrot and Julia visualisations for z |-> z^2 + c
over Z[i]/(p) (Gaussian integers reduced mod a rational prime p).

There is no direct 2D Mandelbrot analogue in C_p: the naive set
{c : orbit of 0 bounded} is just the closed unit disk |c|_p <= 1.
The genuine non-archimedean structure lives on the Berkovich tree,
which is not planar.

What this script renders is the next best thing: the field of
orbit-of-0 periods on Z[i]/(p) for a sequence of primes. This is a
useful arithmetic-dynamics picture but does NOT visually converge
to the classical Mandelbrot set. See the generated README for the
careful statement and the Baker-Rumely / Favre-Rivera-Letelier
equidistribution results that connect mod-p arithmetic to the
bifurcation measure on partial M.

Output:
  folio-assistant/computations/p_adic_mandelbrot/
    p=2.png, p=3.png, ..., p=37.png        (per-prime panels)
    grid-mandelbrot.png                     (multi-prime grid)
    grid-julia-c-minus-1.png                (Julia for c = -1)
    classical-mandelbrot.png                (reference image)
    README.md                               (legend + theory note)
  folio-assistant/computations/p-adic-mandelbrot.witness.json

Run:
    /tmp/padic-venv/bin/python folio-assistant/computations/p_adic_mandelbrot.py
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def _trace_orbit(p: int, za: int, zb: int, ca: int, cb: int,
                 seen: np.ndarray) -> tuple[int, int]:
    """Iterate z |-> z^2 + c starting from (za, zb) with c = (ca, cb)
    in Z[i]/(p), using a pre-allocated p x p int32 array `seen` for
    state tracking (caller must reset to -1). Returns (tau, rho).
    """
    seen.fill(-1)
    step = 0
    while True:
        prev = seen[za, zb]
        if prev != -1:
            return int(prev), step - int(prev)
        seen[za, zb] = step
        new_a = (za * za - zb * zb + ca) % p
        new_b = (2 * za * zb + cb) % p
        za, zb = new_a, new_b
        step += 1


def orbit_period_grid(p: int, c0_real: int = 0, c0_imag: int = 0) -> np.ndarray:
    """For every c = a + b*i in Z[i]/(p), compute (preperiod tau, period rho)
    of the orbit of 0 under z |-> z^2 + c.

    Returns an array of shape (p, p, 2) where pixel (a, b) holds
    [tau, rho] for c = (a + b*i) mod p.

    Note: Z[i]/(p) is F_{p^2} when p == 3 (mod 4) and F_p x F_p otherwise;
    the cycle-detection logic treats it uniformly as a finite ring.
    """
    out = np.zeros((p, p, 2), dtype=np.int32)
    seen = np.full((p, p), -1, dtype=np.int32)
    z0a, z0b = c0_real % p, c0_imag % p
    for a in range(p):
        for b in range(p):
            tau, rho = _trace_orbit(p, z0a, z0b, a, b, seen)
            out[a, b, 0] = tau
            out[a, b, 1] = rho
    return out


def julia_period_grid(p: int, ca: int, cb: int) -> np.ndarray:
    """For every starting z = a + b*i in Z[i]/(p), compute (tau, rho)
    of the orbit under z |-> z^2 + c with c = ca + cb*i.
    """
    out = np.zeros((p, p, 2), dtype=np.int32)
    seen = np.full((p, p), -1, dtype=np.int32)
    ca, cb = ca % p, cb % p
    for a in range(p):
        for b in range(p):
            tau, rho = _trace_orbit(p, a, b, ca, cb, seen)
            out[a, b, 0] = tau
            out[a, b, 1] = rho
    return out


def classical_mandelbrot(width: int = 800, height: int = 800,
                          x_min: float = -2.0, x_max: float = 0.5,
                          y_min: float = -1.25, y_max: float = 1.25,
                          max_iter: int = 256) -> np.ndarray:
    xs = np.linspace(x_min, x_max, width)
    ys = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(xs, ys)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    escape = np.full(C.shape, max_iter, dtype=np.int32)
    mask = np.ones(C.shape, dtype=bool)
    for k in range(max_iter):
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        diverged = mask & (np.abs(Z) > 2.0)
        escape[diverged] = k
        mask &= ~diverged
        if not mask.any():
            break
    return escape


def plot_period_grid(grid: np.ndarray, p: int, title: str, ax) -> None:
    """Plot the period field (rho) for a mod-p grid. Higher period = brighter."""
    rho = grid[:, :, 1].T  # transpose so a is x, b is y
    # log-scale-ish colour for legibility across primes
    vmax = max(2, int(rho.max()))
    norm = mcolors.PowerNorm(gamma=0.5, vmin=1, vmax=vmax)
    im = ax.imshow(
        rho,
        origin="lower",
        cmap="viridis",
        norm=norm,
        extent=[-0.5, p - 0.5, -0.5, p - 0.5],
        interpolation="nearest",
    )
    ax.set_title(title, fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
    return im


def render_per_prime_panels(out_dir: Path) -> dict:
    """Render one PNG per prime, plus the multi-panel grid."""
    summary: dict = {}
    n_primes = len(PRIMES)
    ncols = 4
    nrows = (n_primes + ncols - 1) // ncols
    fig_grid, axes = plt.subplots(nrows, ncols, figsize=(14, 3.7 * nrows),
                                   squeeze=False)
    axes_flat = axes.flatten()
    for ax in axes_flat[n_primes:]:
        ax.axis("off")

    for idx, p in enumerate(PRIMES):
        grid = orbit_period_grid(p)
        rho = grid[:, :, 1]
        tau = grid[:, :, 0]
        summary[str(p)] = {
            "max_period": int(rho.max()),
            "mean_period": float(rho.mean()),
            "max_tail": int(tau.max()),
            "fixed_point_count": int((rho == 1).sum()),
            "preperiodic_zero_count": int((tau > 0).sum()),
        }

        # standalone PNG
        fig, ax = plt.subplots(figsize=(6, 6))
        plot_period_grid(grid, p, f"Mod-{p} Mandelbrot: period of 0-orbit", ax)
        ax.set_xlabel("Re(c) mod p")
        ax.set_ylabel("Im(c) mod p")
        fig.tight_layout()
        fig.savefig(out_dir / f"p={p}.png", dpi=150)
        plt.close(fig)

        # grid panel
        plot_period_grid(grid, p, f"p = {p}", axes_flat[idx])

    fig_grid.suptitle(
        "Mod-p Mandelbrot: orbit-of-0 period for $z \\mapsto z^2 + c$ over $\\mathbb{Z}[i]/(p)$",
        fontsize=13,
    )
    fig_grid.tight_layout(rect=[0, 0, 1, 0.97])
    fig_grid.savefig(out_dir / "grid-mandelbrot.png", dpi=150)
    plt.close(fig_grid)

    return summary


def render_julia_panels(out_dir: Path, ca: int = -1, cb: int = 0) -> None:
    """Render Julia (in z-plane) at fixed c, for a grid of primes."""
    n_primes = len(PRIMES)
    ncols = 4
    nrows = (n_primes + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(14, 3.7 * nrows),
                              squeeze=False)
    axes_flat = axes.flatten()
    for ax in axes_flat[n_primes:]:
        ax.axis("off")
    for idx, p in enumerate(PRIMES):
        grid = julia_period_grid(p, ca, cb)
        plot_period_grid(grid, p, f"p = {p}", axes_flat[idx])
    label = f"c = {ca}" + (f" + {cb}i" if cb else "")
    fig.suptitle(
        f"Mod-p Julia: orbit period of $z \\mapsto z^2 + c$ over $\\mathbb{{Z}}[i]/(p)$, {label}",
        fontsize=13,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    suffix = f"c{ca}" + (f"_{cb}i" if cb else "")
    fig.savefig(out_dir / f"grid-julia-{suffix}.png", dpi=150)
    plt.close(fig)


def render_classical(out_dir: Path) -> None:
    escape = classical_mandelbrot(width=800, height=800, max_iter=256)
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.imshow(
        escape,
        origin="lower",
        cmap="magma",
        extent=[-2.0, 0.5, -1.25, 1.25],
        interpolation="bilinear",
    )
    ax.set_title("Classical Mandelbrot (escape time over $\\mathbb{C}$)", fontsize=12)
    ax.set_xlabel("Re(c)")
    ax.set_ylabel("Im(c)")
    fig.tight_layout()
    fig.savefig(out_dir / "classical-mandelbrot.png", dpi=150)
    plt.close(fig)


README = """\
# Mod-p Mandelbrot / Julia visualisations

Generated by `folio-assistant/computations/p_adic_mandelbrot.py`.

## Honest statement

There is **no direct 2D analogue of the Mandelbrot set in
$\\mathbb{C}_p$**. The naive set
$\\{c \\in \\mathbb{C}_p : \\text{orbit of }0\\text{ bounded}\\}$
for $z^2 + c$ is just the closed unit disk
($|c|_p \\le 1$): no fractal boundary. The genuine non-archimedean
"Mandelbrot" is a subset of the **Berkovich projective line**,
which is an infinitely-branching real tree, not a planar picture.

What is shown here is the next best thing: **mod-$p$ arithmetic
dynamics**. For each rational prime $p$ we plot the Gaussian
residue grid $\\mathbb{Z}[i]/(p)$, with each pixel
$(a, b) \\leftrightarrow c = a + bi \\bmod p$ coloured by the
**period** of the orbit of $0$ under $z \\mapsto z^2 + c$ in the
finite ring $\\mathbb{Z}[i]/(p)$. (Over a finite ring every orbit
is eventually periodic, so this is well-defined.)

Pixel colour: `viridis` with a square-root norm. Dim = small
period; bright = long period (close to the maximum $p^2$).

## What the pictures actually tell you

- The mod-$p$ Mandelbrot grid is **not** a coarse approximation of
  the classical Mandelbrot set $M \\subset \\mathbb{C}$. As $p$
  grows the grid becomes more textured but does not visually
  converge to $M$.
- It **does** carry genuine arithmetic-dynamics information: the
  Misiurewicz parameters in $\\partial M$ are characterised by
  polynomial equations $\\Phi_n(c) = \\Phi_m(c)$ where
  $\\Phi_k = f_c^{\\circ k}(0)$. Reducing those polynomials mod $p$
  picks out the parameters with orbit-of-$0$ period $\\le n - m$ in
  $\\mathbb{Z}[i]/(p)$, and *those* point sets, lifted to
  $\\overline{\\mathbb{Q}}$, equidistribute to the bifurcation
  measure on $\\partial M$ as their height grows
  (Baker–Rumely 2010; Favre–Rivera-Letelier 2006). The heatmap
  shown here is the raw period field, which is a strict
  superset of those Misiurewicz loci.
- The mod-$p$ Julia at fixed $c$ (`grid-julia-c-1.png`) shows
  symmetry $z \\leftrightarrow -z$ — visible at every $p$ — and
  occasional attractor structure (e.g. the ring of equal-period
  points at $p = 17$).

## Files

- `p={2,3,5,7,...,37}.png` — per-prime mod-$p$ Mandelbrot
- `grid-mandelbrot.png` — twelve-prime panel
  ($p = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37$)
- `grid-julia-c-1.png` — mod-$p$ Julia at $c = -1$ (basilica)
- `classical-mandelbrot.png` — escape-time picture over
  $\\mathbb{C}$, for context only

## What is *not* here

- No Berkovich-tree visualisation. That would require rendering a
  graph (every type-II point branching $p+1$ ways), not a heatmap.
  Drop a request if you want it.
- No Misiurewicz lift. Computing roots of $\\Phi_n - \\Phi_m$ over
  $\\mathbb{C}$ for several $(n, m)$ and overlaying on classical
  $M$ would be the picture that actually matches the
  "$p \\to \\infty$ approximation" story. Also a separate task.

## References

- M. Baker, R. Rumely, *Potential Theory and Dynamics on the
  Berkovich Projective Line*, AMS Mathematical Surveys and
  Monographs **159** (2010).
- C. Favre, J. Rivera-Letelier, *Équidistribution quantitative des
  points de petite hauteur sur la droite projective*, Math. Ann.
  **335** (2006), 311–361.
- R. Benedetto, *Dynamics in One Non-Archimedean Variable*, AMS
  Graduate Studies in Mathematics **198** (2019).
- L. DeMarco, X. Wang, H. Ye, *Bifurcation measures and quadratic
  rational maps*, Proc. London Math. Soc. **111** (2015), 149–180.
"""


def main() -> None:
    here = Path(__file__).parent
    out_dir = here / "p_adic_mandelbrot"
    out_dir.mkdir(exist_ok=True)

    print(f"[p-adic-mandelbrot] writing PNGs to {out_dir}")

    summary = render_per_prime_panels(out_dir)
    render_julia_panels(out_dir, ca=-1, cb=0)
    render_classical(out_dir)

    (out_dir / "README.md").write_text(README, encoding="utf-8")

    witness = {
        "title": "Mod-p Mandelbrot / Julia visualisations for z -> z^2 + c",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "primes": PRIMES,
        "per_prime": summary,
        "outputs": {
            "per_prime_pngs": [f"p_adic_mandelbrot/p={p}.png" for p in PRIMES],
            "grid_mandelbrot": "p_adic_mandelbrot/grid-mandelbrot.png",
            "grid_julia_basilica": "p_adic_mandelbrot/grid-julia-c-1.png",
            "classical_reference": "p_adic_mandelbrot/classical-mandelbrot.png",
            "readme": "p_adic_mandelbrot/README.md",
        },
        "method": (
            "For each prime p in PRIMES, enumerate every Gaussian residue "
            "c in Z[i]/(p) and run the iteration z_{k+1} = z_k^2 + c "
            "starting from z_0 = 0 until the orbit revisits a state. "
            "Record (preperiod tau, period rho). Render the rho-field as a "
            "p x p heatmap (viridis, sqrt-norm). Julia variant fixes c and "
            "varies the starting state. Classical Mandelbrot rendered "
            "via standard escape time over C for visual comparison."
        ),
        "notes": [
            "Z[i]/(p) is F_{p^2} when p = 3 (mod 4); F_p x F_p when p = 1 (mod 4); F_4 when p = 2.",
            "The naive C_p-Mandelbrot for z^2+c is the closed unit disk (|c|_p <= 1) "
            "and carries no fractal boundary; the genuinely fractal non-archimedean "
            "structure lives on the Berkovich tree.",
            "The mod-p period heatmap is NOT a coarse approximation of the classical "
            "Mandelbrot set. The equidistribution theorem (Baker-Rumely / Favre-"
            "Rivera-Letelier) applies to roots of Misiurewicz polynomials Phi_n - "
            "Phi_m, lifted to algebraic numbers, not to the raw period field.",
        ],
    }
    witness_path = here / "p-adic-mandelbrot.witness.json"
    witness_path.write_text(json.dumps(witness, indent=2), encoding="utf-8")
    print(f"[p-adic-mandelbrot] wrote witness {witness_path}")
    print(f"[p-adic-mandelbrot] done. {len(PRIMES)} primes rendered.")


if __name__ == "__main__":
    main()
