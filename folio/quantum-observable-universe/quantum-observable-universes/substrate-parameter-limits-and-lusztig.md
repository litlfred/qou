The family $d_q$ of the definition, with its two limits:

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

At $q = 1$, $d_q$ recovers $d$. As $q \to \infty$, $d_q$ projects fully onto the Reeb direction. When realized physically over a base space $M$, $q$ becomes a local substrate field $q \colon M \to k^{\times}$. Algebraically, this corresponds to the Lusztig integral form $\mathcal{U}^{\mathbb{Z}}_q(\mathfrak{su}(2))$, which undergoes a base change via $q \mapsto q_0$.
