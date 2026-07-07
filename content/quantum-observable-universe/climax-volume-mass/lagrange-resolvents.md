Let $\zeta=e^{2\pi i/n}$. The discrete Fourier transform on $C_n$ ([Lagrange resolvent transform](#prop:lagrange-resolvent-transform)) diagonalises the cyclic action: $\sigma(w_k) = \zeta^{-k} w_k$. Any $C_n$-invariant polynomial constraint on the coordinates $x_j$ transforms to constraints on $C_n$-equivariant combinations of the Fourier modes $w_k$.

For $n = 5$ ([Bring's surface](#def:brings-surface)), the three power-sum equations become:

```tex
\begin{align}
  w_0 &= 0
    &&\text{(linear projection),}
    \label{eq:resolvent-linear}\\[4pt]
  w_1w_4+w_2w_3 &= 0
    &&\text{(Hermitian quadric),}
    \label{eq:resolvent-quadric}\\[4pt]
  w_1^2w_3+w_4^2w_2+w_2^2w_1+w_3^2w_4 &= 0
    &&\text{(symmetric cubic).}
    \label{eq:resolvent-cubic}
\end{align}
```

The quadric pairs conjugate modes ($w_k$ with $w_{5-k}$). The cubic pairs squared modes in the skip-one pattern. These are the $C_5$-equivariant invariants $h_2$ and $h_3$ ([aggregate color quantities](#rem:aggregate-color-quantities)).
