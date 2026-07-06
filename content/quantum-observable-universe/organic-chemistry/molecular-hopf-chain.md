A **molecular Hopf chain** is a linear sequence of atoms bonded
by covalent Hopf links ([covalent bond](#def:covalent-bond-types)),
where the first and last atoms retain unused linking sites — the
unclosed "missing link" that distinguishes an open chain from a
closed ring.

**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms with residual
sub-links $R_1, \ldots, R_N$.  A **molecular Hopf chain** of
length $N$ and bond order $k$ is the composite

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

where the operator $\underset{B_k}{\oplus}$ joins two adjacent atoms
by an order-$k$ covalent bond, and $B_k(R_i, R_{i+1})$ is that bond —
formed between the residual sub-links $R_i$ and $R_{i+1}$ of the atoms
it connects.  The **linking matrix** of the chain is the
$N \times N$ matrix

$$
  L^{\mathrm{chain}}_{ij}
  = 
  \begin{cases}
    k & \text{if } |i - j| = 1, \\
    0 & \text{otherwise}.
  \end{cases}
$$

This is a **tridiagonal** matrix — each atom is linked only to its
immediate neighbours.

**Boundary conditions.**
The endpoint atoms $\mathcal{A}_1$ and $\mathcal{A}_N$ each
consume only $k$ of their available linking sites for the chain
bond.  The remaining open sites are **free endpoints**: they can
bond to hydrogen, to side chains, or remain as dangling links.
For a homoatomic chain of carbon atoms ($k = 1$), each interior
carbon uses 2 of its 4 sites for the chain backbone, leaving 2
for side bonds; each endpoint carbon uses 1, leaving 3.

**Crossing energy of the chain.**
The total crossing energy is the sum over $N - 1$ bonds:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_N^{(k)})
  = 
  (N - 1) \cdot E_{\mathrm{bond}}(k).
$$

The absence of a bond between $\mathcal{A}_1$ and $\mathcal{A}_N$
— the **missing link** — is the defining feature distinguishing
chains from rings.
