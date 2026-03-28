Define the following aggregate quantities in color tube coordinates,
with $\zeta = e^{2\pi i/5}$:

```tex
\begin{align}
  \widetilde{S} &\;=\; \sigma + c_r + c_g + c_b
    &&\text{(total color deviation),}
    \label{eq:agg-S-tilde}\\[4pt]
  \widetilde{Q} &\;=\; \sigma c_b + c_r c_g
    &&\text{(paired color product),}
    \label{eq:agg-Q-tilde}\\[4pt]
  \widetilde{D} &\;=\; \zeta^{-1}\sigma + \zeta^{-2}c_r + \zeta^{-3}c_g + \zeta^{-4}c_b
    &&\text{(weighted color deviation),}
    \label{eq:agg-D-tilde}\\[4pt]
  \widetilde{C} &\;=\; \sigma^2 c_g + c_b^2 c_r + c_r^2\sigma + c_g^2 c_b
    &&\text{(intrinsic color cubic).}
    \label{eq:agg-C-tilde}
\end{align}
```

These are related to the unshifted aggregate quantities
$S = \sum_{k=1}^{4}w_k$ and $D = \sum_{k=1}^{4}\zeta^{-k}w_k$ by

```tex
\begin{equation}\label{eq:aggregate-shift}
  S \;=\; \widetilde{S} + 4z, \qquad D \;=\; \widetilde{D} - z,
\end{equation}
```

where the second identity uses $\sum_{k=1}^{4}\zeta^{-k} = -1$.
The inverse Lagrange resolvent transform
([Lagrange resolvents](#rem:lagrange-resolvents)) gives

```tex
\begin{equation}\label{eq:z-from-SD}
  z \;=\; \frac{x_0}{x_1} \;=\; \frac{S}{D}.
\end{equation}
```
