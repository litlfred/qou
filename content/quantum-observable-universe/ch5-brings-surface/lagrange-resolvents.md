Let $\zeta=e^{2\pi i/5}$.  Apply the discrete Fourier transform to the
coordinates $x_j$ of Bring's surface
([Definition](#def:brings-surface)):

$$
  w_k \;=\; \frac{1}{\sqrt{5}}\sum_{j=0}^{4}\zeta^{kj}\,x_j,
  \qquad k\in\{0,1,2,3,4\}.
$$

Under this change of basis the three defining power-sum equations become the
following *spectral forms*:

```tex
\begin{align}
  w_0 &= 0
    &&\text{(linear projection),}
    \label{eq:resolvent-linear}\\[4pt]
  w_1\,w_4+w_2\,w_3 &= 0
    &&\text{(Hermitian quadric),}
    \label{eq:resolvent-quadric}\\[4pt]
  w_1^2\,w_3+w_4^2\,w_2+w_2^2\,w_1+w_3^2\,w_4 &= 0
    &&\text{(symmetric cubic).}
    \label{eq:resolvent-cubic}
\end{align}
```

The cyclic permutation $\sigma\colon x_j\mapsto x_{j+1}$ acts by
$\sigma(w_k)=\zeta^{-k}w_k$, so the $C_5$ symmetry is manifest as a phase
rotation $w_k\mapsto\zeta^k\,w_k$.
