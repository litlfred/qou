The $q$-Hodge star $\star_q$ ([$q$-Hodge star](#def:q-hodge-star)) is an
involution on $\Omega^2(A)$, so its eigenspaces give the splitting
$\Omega^2(A) = \Omega^+(A) \oplus \Omega^-(A)$ and hence
the short exact sequence

```tex
\begin{equation}\label{eq:self-dual-ses}
\begin{tikzcd}[column sep=2em]
  0 \ar[r]
  & \Omega^-(A)
    \ar[r, "\iota"]
  & \Omega^2(A)
    \ar[r, "\pi^+"]
  & \Omega^+(A)
    \ar[r]
  & 0
\end{tikzcd}
\end{equation}
```

where $\Omega^{\pm}(A) = \ker(\mathrm{id} \mp \star_q)$.
The instanton condition
([categorical instanton](#def:categorical-instanton)) is exactly
$F_\nabla \in \ker(\pi^-)$, i.e. $F_\nabla^- = 0$.
In the archimedean realisation ([self-dual curvature](#prop:self-dual-curvature)),
$\star_q$ specialises to $*_H$ and the sequence becomes
$0 \to \Gamma(\Lambda^-\!H^* \otimes \mathrm{Ad}(P)) \to
\Gamma(\Lambda^2 H^* \otimes \mathrm{Ad}(P)) \to
\Gamma(\Lambda^+\!H^* \otimes \mathrm{Ad}(P)) \to 0$.
