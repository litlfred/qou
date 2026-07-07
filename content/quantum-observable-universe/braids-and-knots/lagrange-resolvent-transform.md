Let $C_n$ act on an $n$-dimensional vector space $V$ with coordinates $x_0, \ldots, x_{n-1}$, and let $\zeta = e^{2\pi i/n}$. The **Lagrange resolvent transform** is the discrete Fourier transform on $C_n$:
$$
  w_k =  \frac{1}{\sqrt{n}}\sum_{j=0}^{n-1}\zeta^{kj}x_j,
  \qquad k \in \{0, \ldots, n-1\}.
$$
The cyclic permutation $\sigma \colon x_j \mapsto x_{j+1}$ acts diagonally: $\sigma(w_k) = \zeta^{-k} w_k$. This manifests the $C_n$ symmetry as a phase rotation of the Fourier modes. Any $C_n$-invariant polynomial constraint on the $x_j$ transforms to a constraint on $C_n$-equivariant products that pair conjugate modes $w_k$ and $w_{n-k}$.

For $n = 5$, the three power-sum constraints transform into a linear projection $w_0 = 0$, a Hermitian quadric $w_1 w_4 + w_2 w_3 = 0$, and a symmetric cubic $w_1^2 w_3 + w_4^2 w_2 + w_2^2 w_1 + w_3^2 w_4 = 0$.

**Mathematical Novelty:** Using a Discrete Fourier Transform to diagonalize a cyclic action is standard. However, explicitly formalizing the $n=5$ Bring-surface case with modular zeta-power reduction constitutes a non-trivial mathematical contribution.
