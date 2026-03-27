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

**Shell transitions as Reidemeister I moves.**

The trefoil $T_{2,3}$ has **writhe** $w = +3$ in its minimal
diagram (three positive crossings).  Photon absorption performs
a **Reidemeister I move** on the trefoil's embedding within
the Hopf link to the proton: a curl is added at the exceptional
divisor, increasing the writhe by $+2$ (two R-I moves
preserving the knot type):

$$
  n \to n + 1
  \qquad\Longleftrightarrow\qquad
  w \to w + 2
  \qquad\Longleftrightarrow\qquad
  \text{two R-I moves at exceptional divisor.}
$$

The bare mass $m_e = 0.511$ MeV is unchanged — R-I preserves
the knot type
([Reidemeister invariance](#prop:reidemeister-mass-invariance)).
The binding energy $E_n = -13.6/n^2$ eV changes — R-I changes
the embedding.  The electron is still a trefoil (same
particle); it is in a different state (different writhe).

The **shell number** $n$ is the writhe level:

$$
  n \;=\; \frac{w - 1}{2} \;=\; 1, 2, 3, 4, \ldots
  \qquad\text{for}\quad w = 3, 5, 7, 9, \ldots
$$

The curls added by R-I are **localized at the exceptional
divisor** of the brane tower.  The ground-state trefoil
($w = 3$) lives entirely in the base space $\mathcal{S}_0$.  An excited
trefoil ($w = 5$) has its extra curls in the blow-up $\mathcal{S}_1$.

**Sub-shells from resonance modes of the trefoil.**

The trefoil $T_{2,3}$ is a closed curve embedded in the Bring
surface.  It can **vibrate transversely** — oscillate within
its normal bundle $N_{T_{2,3}}$.  The resonance frequencies of
this vibration are the eigenvalues of the Laplacian on the
trefoil curve, and the mode numbers $\ell = 0, 1, 2, \ldots$
label the standing-wave patterns:

- Mode $\ell = 0$: uniform (no oscillation) — the $s$ orbital.
- Mode $\ell = 1$: one wavelength around the curve — the $p$
  orbital.
- Mode $\ell = 2$: two wavelengths — the $d$ orbital.

At shell $n$, the Seifert surface at linking level $n$ has
effective length $\propto n$.  Only modes with wavelength
$\geq L/n$ fit on the trefoil at this level, giving the
cutoff $\ell = 0, 1, \ldots, n - 1$.  Each mode $\ell$
vibrates transversely in the $3$-dimensional ambient space and
can be oriented in $2\ell + 1$ ways (the standing-wave
patterns on a circle embedded in $\mathbb{R}^3$, projected
onto the sphere, are the spherical harmonics $Y_\ell^m$):

$$
  \sum_{\ell=0}^{n-1} (2\ell + 1) \;=\; n^2
  \quad\text{orbitals per shell.}
$$

This matches observation exactly for all $n$.

**Honesty remark.**  The counting $\sum(2\ell + 1) = n^2$ is
the standard quantum-mechanical result (eigenvalues of the
Laplacian on $S^2$ decomposed under $\mathrm{SO}(3)$).  What
is **new** here is the identification of $\ell$ with
resonance modes of the trefoil vibration and $n$ with the
writhe level (R-I framing number).  The step that remains to
be **proven** is:

*The space of sections of the normal bundle
$N_{T_{2,3}}$ of the trefoil in the Bring surface, at total
framing twist $k = 2(n-1)$, has dimension $n^2$.*

This is
[Proposition](#prop:orbital-space-normal-bundle) below.
The $2\ell + 1$ orientations per mode and the cutoff
$\ell \leq n - 1$ would then follow from the
$\mathrm{SO}(3)$ representation theory of this space.

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
  2n^2 \;=\; 2 \sum_{\ell=0}^{n-1} (2\ell + 1)
  \;=\; 2(1 + 3 + 5 + \cdots + (2n-1))
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
  E_n \;=\; -\frac{E_{\mathrm{ion}}}{n^2}
  \;=\; -\frac{13.6 \text{ eV}}{n^2}
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

Each transition absorbs or emits a photon (point $\varnothing$)
whose energy equals the R-I crossing energy difference.
