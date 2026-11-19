The non-commutative de Rham complex carries two canonical endomorphisms: the full differential $d$ and the vertical differential $\pi_V \circ d$. These span a one-parameter family of first-order operators:

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
\end{equation}
```

The **aether parameter** $q \in \mathrm{End}(\mathbf{1})$ (also referred to in purely algebraic contexts as the deformation or substrate parameter) is the unique value for which $d_q$ acts as $q^{-1}d$ on horizontal forms and as $d$ on vertical forms.
