Write $\mathcal{O}_q = \mathcal{O}_q(\mathrm{SU}(2))$.
The Hopf comultiplication satisfies *coassociativity*:

```tex
\begin{equation}\label{eq:coassociativity}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \mathcal{O}_q
    \ar[r, "\Delta_q"]
    \ar[d, "\Delta_q"']
  & \mathcal{O}_q \otimes \mathcal{O}_q
    \ar[d, "\mathrm{id} \otimes \Delta_q"]
  \\
  \mathcal{O}_q \otimes \mathcal{O}_q
    \ar[r, "\Delta_q \otimes \mathrm{id}"']
  & \mathcal{O}_q \otimes \mathcal{O}_q \otimes \mathcal{O}_q
\end{tikzcd}
\end{equation}
```

Non-cocommutativity and the self-duality short exact sequence are
developed categorically in
[Remarks](#rem:hopf-non-cocommutativity)
and [](#rem:self-dual-ses).
