**The picture.**

Hydrogen couples an electron to a small Borromean proton. The proton occupies the center as a compact $\mathcal{B}_3$ formed of three unknots with $\mathrm{Vol} \approx 7.328$. The electron is the word $e^- = \sigma_0\sigma_1\sigma_0 \in B_3$ ([electron knot](#def:electron-knot)), whose closure is the Hopf link. It loops around the proton and Hopf-links to it.

```tex
\begin{tikzcd}[row sep=4em, column sep=5em]
  & \underset{\text{\normalsize electron } e^- = \sigma_0\sigma_1\sigma_0}{\bigcirc\!\!\!\bigcirc}
    \ar[d, "\oplus"', "\text{Hopf}", dashed] & \\
  & \underset{\text{\normalsize small } \mathcal{B}_3}{\bullet}
    & \\
  & \underset{\text{proton (anchor)}}{\mathrm{Vol} \approx 7.328} &
\end{tikzcd}
```

The Borromean volume pins the massive proton in place. The Hopf link has no hyperbolic volume. The electron mass $m_e$ is the CAL-1 input, not derived here. The Hopf link $\oplus$ provides the electromagnetic binding.

**Shell transitions as strand-adding curls.**

The ground state is $e_1 = e^- = \sigma_0\sigma_1\sigma_0$, with writhe $w = 3$. Photon absorption is the strand-adding curl: it appends the next generator,

$$
  e_n = \sigma_0\sigma_1\sigma_0\,\sigma_2\cdots\sigma_n \in B_{n+2}
  \;\longmapsto\;
  e_{n+1} = e_n\,\sigma_{n+1} \in B_{n+3}.
$$

Appending $\sigma_{n+1}$ is a Markov stabilisation, so the closure stays the Hopf link. The word stays Gröbner–Shirshov reduced, and the level shows as its length. Each curl raises the writhe by $1$:

$$
  n \to n + 1
  \qquad\Longleftrightarrow\qquad
  w \to w + 1,
  \qquad\text{so}\qquad
  n = w - 2 = 1, 2, 3, \ldots
  \quad\text{for}\quad w = 3, 4, 5, \ldots
$$

This is [the shell--writhe correspondence](#conj:hydrogen-shell-writhe), item 1, proved in Lean. Where the added curls sit in the brane tower is not re-derived for the ruled electron.

**Backup reading.** If the electron is the trefoil $\sigma_0^3 \in B_2$, a level step adds two Reidemeister I curls on the same strand, $w \to w + 2$, and $n = (w - 1)/2$. That reading puts the ground state ($w = 3$) in the base space $\mathcal{S}_0$ and the extra curls of $w = 5$ in the blow-up $\mathcal{S}_1$. The sub-shell count below is also built on it.

**Sub-shells from resonance modes (backup reading).**

This count has not been re-derived for the ruled electron. Its closure has two components, and no counterpart of the trefoil normal-bundle construction below is on record for it.

The embedded backup trefoil $T_{2,3}$ vibrates transversely within its normal bundle $N_{T_{2,3}}$ in the Bring surface. Laplacian eigenvalues on the trefoil curve govern the resonance frequencies. The mode integers $\ell = 0, 1, 2, \ldots$ label the standing-wave patterns:

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

The sum $\sum(2\ell + 1) = n^2$ matches standard quantum mechanics. The backup trefoil model identifies $\ell$ with trefoil resonance modes and $n$ with the writhe framing number. The remaining step requires a proof:

*The space of sections of the normal bundle $N_{T_{2,3}}$ of the trefoil in the Bring's surface, at total framing twist $k = 2(n-1)$, has dimension $n^2$.*

This is stated as [The orbital space at shell $n$ is the space of framing-$k$ sections of the normal bundle](#conj:orbital-space-normal-bundle) in the Bring's-surface chapter.

The two ingredients of the count have different sources, and only one of them is representation-theoretic. The $2\ell + 1$ orientations are the dimension of the irreducible $\mathrm{SO}(3)$ representation $V_\ell$ carried by the mode, matching the spherical harmonics $Y_\ell^m$. The cutoff $\ell \leq n - 1$ is not: it is the length-and-framing bound already used above, that only modes of wavelength at least $L/n$ fit along the Seifert surface. In the eigenvalue form $\lambda_\ell \leq \lambda_{n-1}$ this is an arithmetic consequence rather than a group-theoretic one, and it is proved with no symmetry group entering the argument.
