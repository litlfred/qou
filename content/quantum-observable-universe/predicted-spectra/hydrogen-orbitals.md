**The picture.**

Hydrogen couples a large trefoil electron to a small Borromean proton. The proton occupies the center as a compact $\mathcal{B}_3$ formed of three unknots with $\mathrm{Vol} \approx 7.328$. The electron $T_{2,3}$ loops around the proton. They Hopf-link. The electron passes through the proton's Seifert surface exactly once.

The trefoil spins around the Borromean anchor. This motion sweeps out the electron cloud. The trefoil writhe and wrapping determine the cloud shape.

```tex
\begin{tikzcd}[row sep=4em, column sep=5em]
  & \underset{\text{\normalsize large } T_{2,3}}{\bigcirc\!\!\!\bigcirc\!\!\!\bigcirc}
    \ar[d, "\oplus"', "\text{Hopf}", dashed] & \\
  & \underset{\text{\normalsize small } \mathcal{B}_3}{\bullet}
    & \\
  & \underset{\text{proton (anchor)}}{\mathrm{Vol} \approx 7.328} &
\end{tikzcd}
```

The Borromean volume pins the massive proton in place. The zero volume of the trefoil keeps the electron light. Vacuum drag alone supplies its mass. The Hopf link $\oplus$ provides the electromagnetic binding.

**Shell transitions as Reidemeister I moves.**

The minimal diagram of the trefoil $T_{2,3}$ has writhe $w = +3$. Photon absorption executes a Reidemeister I move on the trefoil embedding within the Hopf link. This adds a curl at the exceptional divisor and increases the writhe by $+2$.

$$
  n \to n + 1
  \qquad\Longleftrightarrow\qquad
  w \to w + 2
  \qquad\Longleftrightarrow\qquad
  \text{two R-I moves at exceptional divisor.}
$$

The topological mass $m_e \approx 0.511$ MeV remains unchanged. Reidemeister moves preserve knot type (the Reidemeister mass-invariance conjecture). The binding energy $E_n = -13.6/n^2$ eV changes because R-I moves alter the embedding. The electron remains a trefoil but shifts to a higher writhe state.

The shell number $n$ matches the writhe level:

$$
  n =  \frac{w - 1}{2} =  1, 2, 3, 4, \ldots
  \qquad\text{for}\quad w = 3, 5, 7, 9, \ldots
$$

The added curls localize at the exceptional divisor of the brane tower. The ground-state trefoil ($w = 3$) lies in the base space $\mathcal{S}_0$. An excited trefoil ($w = 5$) places extra curls in the blow-up $\mathcal{S}_1$.

**Sub-shells from resonance modes.**

The embedded trefoil $T_{2,3}$ vibrates transversely within its normal bundle $N_{T_{2,3}}$ in the Bring surface. Laplacian eigenvalues on the trefoil curve govern the resonance frequencies. The mode integers $\ell = 0, 1, 2, \ldots$ label the standing-wave patterns:

- Mode $\ell = 0$: Uniform (no oscillation) — the $s$ orbital.
- Mode $\ell = 1$: One wavelength around the curve — the $p$ orbital.
- Mode $\ell = 2$: Two wavelengths — the $d$ orbital.

At linking level $n$, the Seifert surface has effective length proportional to $n$. Only modes with wavelength $\geq L/n$ fit. This yields the cutoff $\ell = 0, 1, \ldots, n - 1$. Each mode $\ell$ vibrates transversely in ambient $3$-space. Projected onto the sphere, the $2\ell + 1$ standing-wave orientations match the spherical harmonics $Y_\ell^m$. Thus:

$$
  \sum_{\ell=0}^{n-1} (2\ell + 1) =  n^2
  \quad\text{orbitals per shell.}
$$

This sum reproduces the observed capacity for all $n$.

**Note on geometric counting.**

The sum $\sum(2\ell + 1) = n^2$ matches standard quantum mechanics. The topological model identifies $\ell$ with trefoil resonance modes and $n$ with the writhe framing number. The remaining step requires a proof:

*The space of sections of the normal bundle $N_{T_{2,3}}$ of the trefoil in the Bring's surface, at total framing twist $k = 2(n-1)$, has dimension $n^2$.*

This is stated as [`conj:orbital-space-normal-bundle`](#conj:orbital-space-normal-bundle) in the Bring's-surface chapter.

The two ingredients of the count have different sources, and only one of them is representation-theoretic. The $2\ell + 1$ orientations are the dimension of the irreducible $\mathrm{SO}(3)$ representation $V_\ell$ carried by the mode, matching the spherical harmonics $Y_\ell^m$. The cutoff $\ell \leq n - 1$ is not: it is the length-and-framing bound already used above, that only modes of wavelength at least $L/n$ fit along the Seifert surface. In the eigenvalue form $\lambda_\ell \leq \lambda_{n-1}$ this is an arithmetic consequence rather than a group-theoretic one, and it is proved as `mode_cutoff_iff` in the Lean sibling of that conjecture, with no symmetry group entering the argument.
