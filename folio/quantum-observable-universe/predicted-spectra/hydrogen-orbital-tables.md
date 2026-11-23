| Shell $n$ | Writhe $w$ | Sub-shells | Orbitals ($n^2$) | States ($2n^2$) |
|----------:|----------:|-----------|--------:|-------:|
| 1 | 3 | $s$ | 1 | 2 |
| 2 | 4 | $s, p$ | 4 | 8 |
| 3 | 5 | $s, p, d$ | 9 | 18 |
| 4 | 6 | $s, p, d, f$ | 16 | 32 |

**The quantum numbers.**

| Symbol | Name | Values | Knot meaning |
|--------|------|--------|-------------|
| $n$ | Principal | $1, 2, 3, \ldots$ | Writhe $w = n + 2$ of the level word $e_n$ |
| $\ell$ | Angular momentum | $0, 1, \ldots, n-1$ | Not re-derived (backup: Fourier mode on trefoil torus) |
| $m$ | Magnetic | $-\ell, \ldots, +\ell$ | Projection onto Reeb axis |
| $s$ | Spin | $\pm \tfrac{1}{2}$ | Crossing orientation in Hopf link |

- **$n$**: The level. The level-$n$ word $e_n = \sigma_0\sigma_1\sigma_0\sigma_2\cdots\sigma_n$ carries $n - 1$ strand-adding curls beyond the electron $\sigma_0\sigma_1\sigma_0$, so $w = n + 2$ ([shell--writhe correspondence](#conj:hydrogen-shell-writhe)). In the backup trefoil reading $w = 2n + 1$.
- **$\ell$**: Not re-derived for the ruled electron. In the backup trefoil reading it is the Fourier mode of the curl distribution on the trefoil's torus, oscillating around the $(2,3)$ winding.
- **$m$**: The projection of that oscillation onto the Reeb flow direction. This determines the spatial orientation.
- **$s$**: The two crossing orientations within the Hopf link (exchanged by the fiber adjoint involution), corresponding to spin up and spin down.

**The $2n^2$ capacity.**

Each orbital holds two electrons (spin up and spin down), representing two crossing orientations within the Hopf link. Shell $n$ thus holds $2n^2$ electrons:

$$
  2n^2 =  2 \sum_{\ell=0}^{n-1} (2\ell + 1)
  =  2(1 + 3 + 5 + \cdots + (2n-1)).
$$

For hydrogen (one electron), only the $n = 1, \ell = 0$ orbital is occupied in the ground state.

**Origin of $1/n^2$ energy levels.**

At shell $n$, the Seifert surface of the Hopf link between electron and proton is an $n$-fold covering of the base surface, scaling in area as $n^2$. In the backup trefoil reading the R-I curls distribute over this surface, so the crossing energy per curl scales as $1/n^2$. This scaling has not been re-derived for the ruled electron:

$$
  E_n =  -\frac{E_{\mathrm{ion}}}{n^2}
  =  -\frac{13.6 \text{ eV}}{n^2}.
$$

In the backup reading this recovers the Rydberg formula from the R-I crossing energy on the Hopf link Seifert surface.

**Hydrogen spectral series as level transitions.**

| Transition | Curls added | $\Delta E$ | $\lambda$ | Series |
|------------|----------|-----------|----------|--------|
| $n=1 \to 2$ | $+1$ | $10.2$ eV | $121.6$ nm | Lyman-$\alpha$ |
| $n=1 \to 3$ | $+2$ | $12.1$ eV | $102.6$ nm | Lyman-$\beta$ |
| $n=2 \to 3$ | $+1$ | $1.89$ eV | $656.3$ nm | Balmer-$\alpha$ |
| $n=3 \to 4$ | $+1$ | $0.66$ eV | $1875$ nm | Paschen-$\alpha$ |

Each line is one [photon](#def:photon). The strand-adding curl appends one generator per absorbed photon, so a single photon that raises the level by $2$ (Lyman-$\beta$) is not yet accounted for. In the backup trefoil reading the column doubles ($+2$ R-I moves per level). The $\Delta E$ and $\lambda$ columns are the measured hydrogen lines, not derived here.
