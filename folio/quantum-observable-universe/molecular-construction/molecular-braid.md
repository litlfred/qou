Let $\mathcal{A}_1, \ldots, \mathcal{A}_k$ be pre-computed atomic braids with strand counts $n_i = A_i + Z_i$. The **molecular braid** is the element

$$
  \mathcal{M}(A_1, \ldots, A_k; \mathcal{B}) \;\in\; H_{N_{\mathrm{mol}}}(q), \qquad N_{\mathrm{mol}} = \sum_{i=1}^{k} n_i
$$

constructed iteratively as follows:

1. **Atomic assembly.** Embed each atomic braid $\mathcal{A}_i \in H_{n_i}(q)$ into $H_{N_{\mathrm{mol}}}(q)$ using the standard inclusion $\iota_i$ that shifts generator indices.
2. **Inter-atomic crossings.** For each pair of atoms $(i, j)$ with $i < j$, apply the inter-atomic crossing operators determined by the molecular crossing table.
3. **Shared-electron Hopf linking.** For each covalent bond $b \in \mathcal{B}$ connecting atoms $i$ and $j$ with bond order $k_b$, select $k_b$ electron trefoils from atom $i$ and Hopf-link them to atom $j$.
4. **Iterative reduction.** After each assembly step, apply Gröbner–Shirshov reduction to normal form before proceeding to the next step.

Equivalently, $\mathcal{M} = \mathrm{NF}\bigl(\prod_i \iota_i(\mathcal{A}_i) \cdot \prod_{i<j} C_{\mathrm{mol}} \cdot \prod_b L_b\bigr)$.

The **binding energy** of the molecule relative to its constituent atoms is

$$
  \mathfrak{E}_{\mathrm{bind}} = \alpha \left( \sum_{i=1}^{k} \Phi_1(\mathcal{A}_i) - \Phi_1(\mathcal{M}) \right)
$$

where $\alpha = m_e \times 8G$ is the atomic mass formula scale.
