
For horizontal $V, W$, the bracket reduces to $[V,W]_q = q^{-1}[V,W]$.
The mixed term $\varTheta([V,W]_q) = -q^{-1}d\varTheta(V,W)$ is in general
non-zero. Substituting into the next bracket:

```tex
\begin{align*}
  [[V,W]_q, U]_q
  &= q^{-2}[[V,W],U]
    - q^{-1}(1-q^{-1})d\varTheta(V,W)\mathcal{L}_\xi U,
\end{align*}
```

using $\varTheta(U)=0$ and $\varTheta([V,W]_q) = -q^{-1}d\varTheta(V,W)$.
Summing cyclically, the $q^{-2}$ terms assemble into $q^{-2}\mathrm{Jac}(U,V,W) = 0$
by the classical Jacobi identity, leaving only the $d\varTheta$ terms.
