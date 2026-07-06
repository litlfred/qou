Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
([quantum observable universe](#def:quantum-observable-universe)) with
weight decomposition $\pi_H, \pi_V$
([weight decomposition](#def:weight-decomposition)) and Reeb derivation
$\xi$ ([categorical Reeb](#def:categorical-reeb)).  The non-commutative
de Rham complex $(\Omega^\bullet(A), d)$ carries two canonical
endomorphisms:

1. the full differential $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$;
2. the vertical differential $\pi_V \circ d$, which retains only the
   component along the Reeb direction.

These span a one-parameter family of first-order operators
parametrised by $q \in \mathrm{End}(\mathbf{1}) \cong k^{\times}$:

$$
  d_q =  q^{-1}d +  (1 - q^{-1})\pi_V \circ d.
$$

```tex
\begin{equation}\label{eq:substrate-family-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "d"] \ar[d, "\pi_V \circ d"'] \ar[dr, "d_q"]
  & \Omega^{k+1}(A) \\
  \Omega^{k+1}(A)
  & {} \ar[u, phantom, "q{=}1"' near start]
    \ar[l, phantom, "q{\to}\infty" near start]
\end{tikzcd}
\qquad\text{(substrate family)}
\end{equation}
```

The **substrate parameter** is the unique element
$q \in \mathrm{End}(\mathbf{1}) \cong k$ such that $d_q$
acts as $q^{-1}d$ on horizontal forms and as $d$ on vertical forms.
Geometrically, $q$ is the fibre coordinate on the
$\mathbb{G}_m$-family of interpolations.
