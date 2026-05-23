| Shell $n$ | Writhe $w$ | Sub-shells | Orbitals ($n^2$) | States ($2n^2$) |
|----------:|----------:|-----------|--------:|-------:|
| 1 | 3 | $s$ | 1 | 2 |
| 2 | 5 | $s, p$ | 4 | 8 |
| 3 | 7 | $s, p, d$ | 9 | 18 |
| 4 | 9 | $s, p, d, f$ | 16 | 32 |

**The quantum numbers.**

| Symbol | Name | Values | Knot meaning |
|--------|------|--------|-------------|
| $n$ | Principal | $1, 2, 3, \ldots$ | Writhe level $w = 2n + 1$ |
| $\ell$ | Angular momentum | $0, 1, \ldots, n-1$ | Fourier mode on trefoil torus |
| $m$ | Magnetic | $-\ell, \ldots, +\ell$ | Projection onto Reeb axis |
| $s$ | Spin | $\pm \tfrac{1}{2}$ | Crossing orientation in Hopf link |

- **$n$**: the writhe level — how many R-I curls have been added
  at the exceptional divisor.
- **$\ell$**: which Fourier mode of the curl distribution on
  the trefoil's torus — how the writhe excitation oscillates
  around the $(2,3)$ winding.
- **$m$**: the projection of that oscillation onto the Reeb
  flow direction — the spatial orientation.
- **$s$**: the two crossing orientations within the Hopf link
  (the fiber adjoint involution exchanges them) — spin up
  and spin down.

**The $2n^2$ capacity.**

Each orbital can hold **two electrons** (spin up and spin
down), corresponding to the trefoil's two crossing
orientations within the Hopf link.  So each shell $n$ holds
$2n^2$ electrons:

$$
  2n^2 =  2 \sum_{\ell=0}^{n-1} (2\ell + 1)
  =  2(1 + 3 + 5 + \cdots + (2n-1))
$$

For hydrogen (one electron), only the $n = 1$, $\ell = 0$
orbital is occupied in the ground state.

**Why $1/n^2$ energy levels.**

At shell $n$, the Seifert surface of the Hopf link between
electron and proton is an $n$-fold covering of the base
surface, with area $\propto n^2$.  The R-I curls are
distributed over this surface.  The crossing energy per curl
scales as $1/n^2$ (same energy spread over larger area):

$$
  E_n =  -\frac{E_{\mathrm{ion}}}{n^2}
  =  -\frac{13.6 \text{ eV}}{n^2}
$$

This is the Rydberg formula, derived from the R-I crossing
energy on the Hopf link Seifert surface.

**Hydrogen spectral series as R-I transitions.**

| Transition | R-I moves | $\Delta E$ | $\lambda$ | Series |
|------------|----------|-----------|----------|--------|
| $n=1 \to 2$ | $+2$ | $10.2$ eV | $121.6$ nm | Lyman-$\alpha$ |
| $n=1 \to 3$ | $+4$ | $12.1$ eV | $102.6$ nm | Lyman-$\beta$ |
| $n=2 \to 3$ | $+2$ | $1.89$ eV | $656.3$ nm | Balmer-$\alpha$ |
| $n=3 \to 4$ | $+2$ | $0.66$ eV | $1875$ nm | Paschen-$\alpha$ |

Each transition absorbs or emits a photon ($\mathbf{1}_{B_4}$ 4-strand identity, knot-trivial)
whose energy equals the R-I crossing energy difference.
