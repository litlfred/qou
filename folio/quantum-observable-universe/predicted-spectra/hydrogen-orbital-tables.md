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

- **$n$**: The writhe level. This counts the R-I curls added at the exceptional divisor.
- **$\ell$**: The Fourier mode of the curl distribution on the trefoil's torus. This dictates how the writhe excitation oscillates around the $(2,3)$ winding.
- **$m$**: The projection of that oscillation onto the Reeb flow direction. This determines the spatial orientation.
- **$s$**: The two crossing orientations within the Hopf link (exchanged by the fiber adjoint involution), corresponding to spin up and spin down.

**The $2n^2$ capacity.**

Each orbital holds two electrons (spin up and spin down), representing the trefoil's two crossing orientations within the Hopf link. Shell $n$ thus holds $2n^2$ electrons:

$$
  2n^2 =  2 \sum_{\ell=0}^{n-1} (2\ell + 1)
  =  2(1 + 3 + 5 + \cdots + (2n-1)).
$$

For hydrogen (one electron), only the $n = 1, \ell = 0$ orbital is occupied in the ground state.

**Origin of $1/n^2$ energy levels.**

At shell $n$, the Seifert surface of the Hopf link between electron and proton is an $n$-fold covering of the base surface, scaling in area as $n^2$. The R-I curls distribute over this surface. Consequently, the crossing energy per curl scales as $1/n^2$:

$$
  E_n =  -\frac{E_{\mathrm{ion}}}{n^2}
  =  -\frac{13.6 \text{ eV}}{n^2}.
$$

This recovers the Rydberg formula directly from the R-I crossing energy on the Hopf link Seifert surface.

**Hydrogen spectral series as R-I transitions.**

| Transition | R-I moves | $\Delta E$ | $\lambda$ | Series |
|------------|----------|-----------|----------|--------|
| $n=1 \to 2$ | $+2$ | $10.2$ eV | $121.6$ nm | Lyman-$\alpha$ |
| $n=1 \to 3$ | $+4$ | $12.1$ eV | $102.6$ nm | Lyman-$\beta$ |
| $n=2 \to 3$ | $+2$ | $1.89$ eV | $656.3$ nm | Balmer-$\alpha$ |
| $n=3 \to 4$ | $+2$ | $0.66$ eV | $1875$ nm | Paschen-$\alpha$ |

Each transition absorbs or emits a photon ($\mathbf{1}_{B_4}$ 4-strand identity, knot-trivial). The photon energy equals the R-I crossing energy difference.
