**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms with residual sub-links $R_1, \ldots, R_N$. A **molecular Hopf chain** of length $N$ and bond order $k$ is the composite

$$
  \mathcal{C}_N^{(k)}
  = 
  \mathcal{A}_1
   \underset{B_k}{\oplus}
  \mathcal{A}_2
   \underset{B_k}{\oplus}
  \cdots
   \underset{B_k}{\oplus}
  \mathcal{A}_N
$$

where $\underset{B_k}{\oplus}$ joins two adjacent atoms by an order-$k$ covalent bond $B_k(R_i, R_{i+1})$. The **linking matrix** is the tridiagonal $N \times N$ matrix:

$$
  L^{\mathrm{chain}}_{ij}
  = 
  \begin{cases}
    k & \text{if } |i - j| = 1, \\
    0 & \text{otherwise}.
  \end{cases}
$$

**Boundary conditions.**
The endpoint atoms $\mathcal{A}_1$ and $\mathcal{A}_N$ consume only $k$ of their available linking sites for the chain bond. The remaining open sites are **free endpoints**.

**Crossing energy of the chain.**
The total crossing energy is the sum over $N - 1$ bonds:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_N^{(k)})
  = 
  (N - 1) \cdot E_{\mathrm{bond}}(k).
$$

The absence of a bond between $\mathcal{A}_1$ and $\mathcal{A}_N$ is the missing link distinguishing chains from rings.
