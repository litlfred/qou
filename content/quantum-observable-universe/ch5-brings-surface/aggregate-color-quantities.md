Define the following aggregate quantities in color tube coordinates,
with $\zeta = e^{2\pi i/5}$:

```tex
\begin{align}
  \widetilde{S} &\;=\; \sigma + r + g + b
    &&\text{(total color deviation),}
    \label{eq:agg-S-tilde}\\[4pt]
  \widetilde{Q} &\;=\; \sigma b + r g
    &&\text{(paired color product),}
    \label{eq:agg-Q-tilde}\\[4pt]
  \widetilde{D} &\;=\; \zeta^{-1}\sigma + \zeta^{-2}r + \zeta^{-3}g + \zeta^{-4}b
    &&\text{(weighted color deviation),}
    \label{eq:agg-D-tilde}\\[4pt]
  \widetilde{C} &\;=\; \sigma^2 g + b^2 r + r^2\sigma + g^2 b
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
