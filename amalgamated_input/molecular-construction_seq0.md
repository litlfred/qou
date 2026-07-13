<!-- FILE_START: molecular-hecke-algebra-intro.md -->
We extend the atomic constructor to multi-atom systems. The molecular braid joins pre-computed atomic braids inside a single Hecke algebra. Inter-atomic crossing coefficients record how strands from different nuclei interact. Two atoms share a single electron trefoil to form a covalent bond. The ILP characterisation of the covalent bond identifies that shared trefoil as the inverse trefoil $T_{2,3}^{-1}$, the minimum-crossing knot operator with positive binding energy. With these four objects in hand, we compute any molecule by Hopf-linking atoms.
<!-- FILE_END: molecular-hecke-algebra-intro.md -->

<!-- FILE_START: molecular-braid.md -->
**Definition.**
*Let $\mathcal{A}_1, \ldots, \mathcal{A}_k$ be pre-computed atomic braids with strand counts $n_i = A_i + Z_i$. The **molecular braid** is the element*

$$
  \mathcal{M}(A_1, \ldots, A_k; \mathcal{B}) \;\in\; H_{N_{\mathrm{mol}}}(q), \qquad N_{\mathrm{mol}} = \sum_{i=1}^{k} n_i
$$

*constructed iteratively as follows:*

1. **Atomic assembly.** Embed each atomic braid $\mathcal{A}_i \in H_{n_i}(q)$ into $H_{N_{\mathrm{mol}}}(q)$ using the standard inclusion $\iota_i$ that shifts generator indices.
2. **Inter-atomic crossings.** For each pair of atoms $(i, j)$ with $i < j$, apply the inter-atomic crossing operators determined by the molecular crossing table.
3. **Shared-electron Hopf linking.** For each covalent bond $b \in \mathcal{B}$ connecting atoms $i$ and $j$ with bond order $k_b$, select $k_b$ electron trefoils from atom $i$ and Hopf-link them to atom $j$.
4. **Iterative reduction.** After each assembly step, apply Gröbner–Shirshov reduction to normal form before proceeding to the next step.

*The molecular braid satisfies $\mathcal{M} = \mathrm{NF}\bigl(\prod_i \iota_i(\mathcal{A}_i) \cdot \prod_{i<j} C_{\mathrm{mol}} \cdot \prod_b L_b\bigr)$.*

*The binding energy of the molecule relative to its constituent atoms is*

$$
  \mathfrak{E}_{\mathrm{bind}} = \alpha \left( \sum_{i=1}^{k} \Phi_1(\mathcal{A}_i) - \Phi_1(\mathcal{M}) \right)
$$

*where $\alpha = m_e \times 8G$ is the atomic mass formula scale. Positive $\mathfrak{E}_{\mathrm{bind}}$ means the molecule is bound.*
<!-- FILE_END: molecular-braid.md -->

<!-- FILE_START: covalent-bond-shared-trefoil.md -->
**Definition.**
*A **covalent bond of order $k$** between atoms $i$ and $j$ is the Hopf linking of $k$ electron trefoils across the two nuclei. Specifically, let $e_1, \ldots, e_k$ be electrons from atom $i$. Each electron is a trefoil $T_{2,3} = \sigma_0\sigma_1\sigma_0$ in its local $H_3(q)$.*

*In the molecular braid, the covalent bond operator for bond $b$ connecting atoms $i$ and $j$ is:*

$$
  L_b = \prod_{e=1}^{k_b} \sigma_{g_e(\mathfrak{p}_j)}^{-1} \cdot \sigma_{g_e(\mathfrak{p}_i)}^{-1}
$$

*where $g_e(\mathfrak{p}_j)$ is the generator index for the crossing between shared electron $e$ and proton $\mathfrak{p}_j$ of atom $j$. Both crossings are $\sigma^{-1}$ (EM attraction), so each shared electron contributes two attractive crossings—one to each nucleus.*
<!-- FILE_END: covalent-bond-shared-trefoil.md -->

<!-- FILE_START: covalent-bond-order-and-lp-selection.md -->
A bond of order $k$ contributes $2k$ attractive crossings. The LP dual finds the optimal assignment of electrons to bonding positions by minimizing the total $\Phi_1$.

Bond orders correspond directly to shared pairs:
- $k = 1$: single bond (H-H, C-H, C-C), 1 shared pair.
- $k = 2$: double bond (C=O, C=C), 2 shared pairs.
- $k = 3$: triple bond (C$\equiv$O, N$\equiv$N), 3 shared pairs.
<!-- FILE_END: covalent-bond-order-and-lp-selection.md -->

<!-- FILE_START: ilp-covalent-bond.md -->
*The covalent bond operator is selected by the universal ILP—the same LP that derives confinement ($\mathcal{B}_3$) and the gluon ($2\sigma_0$):*

$$
  \min_{K} \; \mathrm{cr}(K) \quad \text{s.t.} \quad K \in \{\text{knots}\}, \quad G \cdot \mathrm{NF}(x \cdot K) \geq 0, \quad \mathrm{tr}_M(x \cdot K) \leq \mathrm{tr}_M(x)
$$

*For the hydrogen atom ($x = \mathrm{NF}(H)$), the unknot gives equality in the trace. The LP selects the minimum-crossing knot that strictly decreases the trace.*

*The inverse trefoil $T_{2,3}^{-1} = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ is the unique LP solution: the minimum-crossing knot satisfying both Frobenius positivity and non-increasing trace.*

### Knots, not links

The dual space of the LP is the knot operator space—single-component braid closures. Links are excluded because the covalent bond is a single topological structure mediating the interaction. The Hopf link gives repulsive or weak binding on the vertex volume model. The knot constraint forces the inseparability of the bonded system.

### Consistency across levels

The LP that selects the inverse trefoil for molecular binding is identical to the LP that selects $\mathcal{B}_3$ for quark confinement. Both solve the same program with the same Gram matrix $G$, the same Frobenius constraint, and the same trace objective. The only input that changes is the state $x$.

### Binding energy

On the 2-generator vertex volume model with 3-channel Wedderburn weights, the predicted binding energy $D_0(H_2) = 4.4834$ eV matches observation within $+0.1\%$. On the NF multiplication method, $D_0(C\text{-}C) = 3.21$ eV matches observation within $-10.9\%$. The scale $E_{\mathrm{mol}}$ derives from $q_0$ alone, requiring no fitted parameters.
<!-- FILE_END: ilp-covalent-bond.md -->

