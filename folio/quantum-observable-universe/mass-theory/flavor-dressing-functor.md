**Definition.**
*The **flavor dressing functor** assigns a dressed-mass scale to each quark flavor:*

$$
  \mu \colon \mathbf{Flavor} \longrightarrow \mathbb{R}_{>0},
  \qquad
  q \in \{\mathfrak{u}, \mathfrak{d}, \mathfrak{s}, \mathfrak{c}, \mathfrak{b}, \mathfrak{t}\}
  \longmapsto
  \mu_q \in \mathbb{R}_{>0}.
$$

*The discrete category $\mathbf{Flavor}$ contains the six quark flavors and identity morphisms. The target $\mathbb{R}_{>0}$ is the positive real line with canonical commutative-monoid structure under multiplication.*

The primary focus is the light doublet $\{\mathfrak{u}, \mathfrak{d}\}$; heavy flavors are included in $\mathbf{Flavor}$ for forward compatibility, with their individual $\mu_q$ values left open.

The functor bridges two categorical layers:

1. **Aether side.** The splitting $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ is determined by the aether flavor split modulo the pair-skein factor.
2. **Bounds side.** The splitting respects the categorical bound enforced by the aether factors $\hbar_q$, $h_q$, and $[2]_q$.

The flavor dressing functor composes with the shell dressing morphism at the hadron and atom levels:

```tex
\begin{tikzcd}
  \mathbf{Flavor}
  \arrow[r, "\mu"] \arrow[d, "\Phi"]
  & \mathbb{R}_{>0}
  \\
  \mathbf{Hadron}
  \arrow[r, "m_{\mathrm{bare}}"']
  & \mathbb{R}_{>0}
  \arrow[u, "P_{\mathrm{bare}} \mapsto P_{\mathrm{dressed}}"']
\end{tikzcd}
```

Here $\Phi$ is the quark-content functor. The right-vertical arrow lifts a bare hadron mass to its electron-dressed atomic mass.

The discrete-category framing ensures compatibility with other categorical constructions. Sums over flavors in hadronic mass formulas become natural transformations of functors rather than ad-hoc weighted sums.
