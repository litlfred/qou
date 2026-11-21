Define the following $C_5$-equivariant quantities in color tube coordinates, with $\zeta = e^{2\pi i/5}$:

```tex
\begin{align}
  p_1(c) &=  \sigma + c_r + c_g + c_b
    &&\text{(first power sum),}
    \label{eq:agg-p1}\\[4pt]
  h_2(c) &=  \sigma c_b + c_r c_g
    &&\text{(Hermitian quadric),}
    \label{eq:agg-h2}\\[4pt]
  \chi_\zeta(c) &=  \zeta^{-1}\sigma + \zeta^{-2}c_r + \zeta^{-3}c_g + \zeta^{-4}c_b
    &&\text{($C_5$ character),}
    \label{eq:agg-chi}\\[4pt]
  h_3(c) &=  \sigma^2 c_g + c_b^2 c_r + c_r^2\sigma + c_g^2 c_b
    &&\text{(Hermitian cubic).}
    \label{eq:agg-h3}
\end{align}
```

The subscript on $h_k$ denotes the degree of the $C_5$-equivariant invariant. $h_2$ pairs conjugate resolvents ($w_k$ with $w_{5-k}$). $h_3$ pairs squared resolvents in a skip-one pattern. The character $\chi_\zeta$ is the $\zeta$-weighted sum (the Fourier dual of $p_1$).

These relate to the unshifted resolvent invariants $S = \sum_{k=1}^{4}w_k$ and $D = \sum_{k=1}^{4}\zeta^{-k}w_k$ by

```tex
\begin{equation}\label{eq:aggregate-shift}
  S =  p_1(c) + 4z, \qquad D =  \chi_\zeta(c) - z.
\end{equation}
```

The second identity uses $\sum_{k=1}^{4}\zeta^{-k} = -1$. The inverse [Lagrange resolvent transform](#prop:lagrange-resolvent-transform) yields

```tex
\begin{equation}\label{eq:z-from-SD}
  z =  \frac{x_0}{x_1} =  \frac{S}{D}.
\end{equation}
```
