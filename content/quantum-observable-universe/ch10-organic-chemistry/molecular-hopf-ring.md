A **molecular Hopf ring** is the closed counterpart of a
molecular Hopf chain ([molecular Hopf chain](#def:molecular-hopf-chain)):
all atoms are bonded in a cycle with no free endpoints.

**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms.  A
**molecular Hopf ring** of length $N$ and bond order $k$ is the
composite

$$
  \mathcal{R}_N^{(k)}
  \;=\;
  \mathcal{A}_1
  \;\underset{B_k}{\bowtie}\;
  \mathcal{A}_2
  \;\underset{B_k}{\bowtie}\;
  \cdots
  \;\underset{B_k}{\bowtie}\;
  \mathcal{A}_N
  \;\underset{B_k}{\bowtie}\;
  \mathcal{A}_1
$$

where the final bond $B_k(R_N, R_1)$ closes the cycle.  The
linking matrix is the **circulant**

$$
  L^{\mathrm{ring}}_{ij}
  \;=\;
  \begin{cases}
    k & \text{if } |i - j| \equiv 1 \pmod{N}, \\
    0 & \text{otherwise}.
  \end{cases}
$$

**Crossing energy of the ring.**
The ring has $N$ bonds (one more than the chain):

$$
  E_{\mathrm{cross}}(\mathcal{R}_N^{(k)})
  \;=\;
  N \cdot E_{\mathrm{bond}}(k)
  \;+\;
  \Delta E_{\mathrm{closure}}(N, k),
$$

where $\Delta E_{\mathrm{closure}}$ is the **topological
rearrangement energy** — the cost of reorganising the global
braid word to accommodate the new $(N, 1)$ crossing.  This term
is absent in the chain and is the source of the ring-closure
energy barrier.

**Rigidity.**
In a ring, every atom's chain-backbone sites are fully consumed:
an interior atom in a ring with $k = 1$ uses 2 of its 4 sites for
ring bonds, the same as a chain interior atom.  But the
**endpoints no longer exist** — every atom is interior.  The ring
has no dangling links along the backbone direction, making it
topologically rigid: deforming the ring requires simultaneously
changing crossings at every bond, unlike a chain where the
endpoints can flex freely.
