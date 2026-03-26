**The picture.**
Hydrogen is a large trefoil (electron) with a small Borromean
knot (proton) threaded through it.  The proton sits at the
center — a dense, compact $\mathcal{B}_3$ of three unknots with
$\mathrm{Vol} = 7.328$.  The electron $T_{2,3}$ is a much
larger trefoil that loops around the proton, Hopf-linked by
passing through the proton's Seifert surface once.

The trefoil **spins** around the Borromean anchor.  This
spinning — the trefoil sweeping out a volume as it orbits —
is what we observe as the **electron cloud**.  The shape of
the cloud is determined by the writhe of the trefoil and how
it wraps around the proton.

```tex
\begin{tikzcd}[row sep=4em, column sep=5em]
  & \underset{\text{\normalsize large } T_{2,3}}{\bigcirc\!\!\!\bigcirc\!\!\!\bigcirc}
    \ar[d, "\bowtie"', "\text{Hopf}", dashed] & \\
  & \underset{\text{\normalsize small } \mathcal{B}_3}{\bullet}
    & \\
  & \underset{\text{proton (anchor)}}{\mathrm{Vol} = 7.328} &
\end{tikzcd}
```

The trefoil orbits the Borromean anchor.  The Borromean volume
pins the proton in place (massive); the trefoil's zero volume
makes the electron light (mass from vacuum drag only).  The
Hopf link $\bowtie$ is the electromagnetic binding: the
trefoil threads through the proton's Seifert surface.

**Hydrogen orbitals from trefoil geometry.**

The trefoil $T_{2,3}$ has **writhe** $w = +3$ in its minimal
diagram (three positive crossings).  The writhe can increase
by adding curls (Reidemeister I moves): $w = +3, +5, +7, \ldots$
Each pair of added curls corresponds to a higher energy state.

The **shell number** $n$ is the writhe level:

$$
  n \;=\; \frac{w - 1}{2} \;=\; 1, 2, 3, 4, \ldots
  \qquad\text{for}\quad w = 3, 5, 7, 9, \ldots
$$

At each shell $n$, the trefoil has $w = 2n + 1$ crossings.
The **sub-shells** correspond to the distinct ways of
distributing the $2(n-1)$ added curls around the three lobes
of the trefoil:

| Shell $n$ | Writhe $w$ | Added curls | Sub-shells | Orbitals | States ($2n^2$) |
|----------:|----------:|-----------:|-----------|--------:|-------:|
| 1 | 3 | 0 | $s$ only | 1 | 2 |
| 2 | 5 | 2 | $s, p$ | 4 | 8 |
| 3 | 7 | 4 | $s, p, d$ | 9 | 18 |
| 4 | 9 | 6 | $s, p, d, f$ | 16 | 32 |

**Sub-shell structure from curl placement.**

The trefoil has **three lobes** (from its $(2,3)$ winding).
The $2(n-1)$ added curls can be distributed among these three
lobes.  The angular momentum quantum number $\ell$ counts how
many distinct lobes carry curls:

- $\ell = 0$ ($s$ sub-shell): all curls on the **same lobe**.
  The trefoil stays roughly spherical.  One orbital.

- $\ell = 1$ ($p$ sub-shell): curls on **two lobes**.  The
  trefoil becomes elongated along one axis.  Three orbitals
  ($m = -1, 0, +1$), one for each choice of axis.

- $\ell = 2$ ($d$ sub-shell): curls on **all three lobes**
  with one distinguished.  Five orbitals ($m = -2, \ldots, +2$).

- $\ell = 3$ ($f$ sub-shell): curls on all three lobes with
  two distinguished.  Seven orbitals.

The magnetic quantum number $m$ is the **orientation** of the
curl pattern relative to the Reeb flow direction.

**The $2n^2$ capacity.**

Each orbital can hold **two electrons** (spin up and spin
down), corresponding to the trefoil's two crossing
orientations within the Hopf link (the fiber adjoint involution
exchanges the two).  So each shell $n$ holds $2n^2$ electrons:

$$
  2n^2 \;=\; 2 \sum_{\ell=0}^{n-1} (2\ell + 1)
  \;=\; 2(1 + 3 + 5 + \cdots + (2n-1))
$$

For hydrogen (one electron), only the $n = 1$, $\ell = 0$
orbital is occupied in the ground state.  Photon absorption
promotes the electron to a higher writhe state.

**Why $1/n^2$ energy levels.**

At writhe $w = 2n + 1$, the trefoil has $2(n-1)$ extra
crossings beyond the minimal 3.  Each crossing lives on the
Seifert surface of the Hopf link between electron and proton.
At shell $n$, the Seifert surface has area $\propto n^2$
(it is an $n$-fold covering of the base surface).  The
crossing energy per crossing therefore scales as $1/n^2$:

$$
  E_n \;=\; -\frac{E_{\mathrm{ion}}}{n^2}
  \;=\; -\frac{13.6 \text{ eV}}{n^2}
$$

The total energy is the **crossing energy of the Hopf link**
at linking level $n$, divided by the area of the Seifert
surface.  This is the Rydberg formula, derived from the knot
geometry.

**Hydrogen spectral series as writhe transitions.**

| Transition | $\Delta w$ | $\Delta E$ | Wavelength | Name |
|------------|-----------|-----------|------------|------|
| $n=1 \to 2$ | $+2$ | $10.2$ eV | $121.6$ nm | Lyman-$\alpha$ |
| $n=1 \to 3$ | $+4$ | $12.1$ eV | $102.6$ nm | Lyman-$\beta$ |
| $n=2 \to 3$ | $+2$ | $1.89$ eV | $656.3$ nm | Balmer-$\alpha$ |
| $n=3 \to 4$ | $+2$ | $0.66$ eV | $1875$ nm | Paschen-$\alpha$ |

Each transition absorbs or emits a photon (point $\varnothing$)
that adds or removes two curls from the trefoil.  The photon's
wavelength $\lambda = hc / \Delta E$ is determined by the
writhe change and the crossing energy scale.
