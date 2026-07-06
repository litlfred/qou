**Remark (categorical coordinate of the commutative limit).**
The Hecke generator $\sigma = P \circ R$ on $V \otimes V$ has eigenvalues $(\lambda_+, \lambda_-) = (q, -q^{-1})$ on the symmetric/antisymmetric decomposition $S^2 V \oplus \Lambda^2 V$ ([def:crossing-energy](#def:crossing-energy)). At $q = 1$ ([def:commutative-qou](#def:commutative-qou)), these eigenvalues collapse to $(+1, -1) = \mathbb{Z}_2$, identically vanishing the per-crossing weight $q - q^{-1}$. We recover the categorical structure of the commutative limit by extracting the square root of the antisymmetric eigenvalue $\lambda_- = -1$:

$$
  i  =  \sqrt{\lambda_-}, \qquad i^2 + 1  =  0  \;\text{in}\; R[i].
$$

The categorical structure forces the ring extension $R[i]$. Thus $i$ is the categorical coordinate of $\mathbb{P}(V)$ in the commutative limit, perfectly mirroring the role of $q$ in the non-commutative theory. This construction is intrinsic to $R$. When $R$ contains a square root of $-1$ (e.g., the archimedean realisation $R = \mathbb{C}$), $i \in R$ is canonical; otherwise (e.g., $R = \mathbb{Z}[q, q^{-1}]$ at $q = 1$), $R[i]$ provides the minimal extension realising $\lambda_-$ as a categorical square.

**Categorical-coordinate dictionary.**

See [Table 1](#tbl:commutative-crossing-energy-table1-data).

**Deformation hierarchy.** The discrete Weyl group $\mathbb{Z}_2$ embeds into the continuous maximal torus, which forms the $q = 1$ fibre of the quantum torus:

$$
  \mathbb{Z}_2  \;\hookrightarrow\;  \mathrm{U}(1)  \;\hookrightarrow\;
   \mathrm{U}_q(1).
$$

Each inclusion detects a distinct categorical coordinate on $\mathrm{End}(\mathbf{1})$. The coordinate $-1$ generates $\mathbb{Z}_2$, $i$ generates $\mathrm{U}(1)$ at the quarter-turn $\varTheta = \pi/2$, and $q$ generates $\mathrm{U}_q(1)$ off-locus. These two inclusions provide the two mechanisms to escape the $q = 1$ degeneracy of $q - q^{-1}$. The commutative-limit enlargement $\mathbb{Z}_2 \hookrightarrow \mathrm{U}(1)$ acts on the first; the non-commutative deformation $\mathrm{SU}(2) \rightsquigarrow \mathrm{SU}_q(2)$ acts on the second.

**Three categorical readings of $i$ on $\mathbb{P}(V)$.**
Because each reading computes the same square root of $\lambda_-$ in $\mathrm{End}_{R[i]}(V)$, the three readings coincide:

1. **Algebraic.** The value $i = \sqrt{\lambda_-} \in \mathrm{End}_{R[i]}(\mathbf{1})$ is the categorical square root of the antisymmetric braiding eigenvalue. This single datum governs Wick rotation, CR complex structure, and the arrow of time, all reducing to the binary choice of braiding orientation $c_{V,V}$ versus $c_{V,V}^{-1}$ ([rem:i-as-braiding-orientation](#rem:i-as-braiding-orientation)).
2. **Geometric.** The endomorphism $J = i \cdot \mathrm{id}_V \in \mathrm{End}_{R[i]}(V)$ squares to $-\mathrm{id}_V$, descending to a complex structure on $\mathbb{P}(V) = \mathrm{Proj}(\mathrm{Sym}\, V^\vee)$ over $R[i]$. In the archimedean realisation, this matches the standard complex structure on the exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$ ([def:exceptional-divisor](#def:exceptional-divisor)).
3. **Equivariant.** The maximal torus $\mathrm{U}(1) \subset \mathrm{SU}(2)$ acts on $\mathbb{P}(V)$ with $i$ as the quarter-turn generator. The orbit space is $[0, \pi]$ with phase fibre $\varphi \in S^1$ over the interior ([prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction)).

**Affine-chart origin.**
The chart-transition data of $\mathbb{P}(V)$ originates both $q$ and $i$ ([rem:affine-chart-origin-of-i-and-q](#rem:affine-chart-origin-of-i-and-q)). On the quantum projective line $\mathbb{P}_q(V)$, $q$ is the chart-transition coefficient $z\,w = q^{-1}$. At $q = 1$, the transition collapses to the chart-swap involution $\iota: z \mapsto z^{-1}$, and $i$ is the square root of this involution. Formally, the categorical-coordinate ring $R[i, q^{\pm 1}] = R[q, q^{-1}][i]/(i^2 + 1)$ ([prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring)) acts as the universal $R$-algebra extension wherein $q$ is invertible and $-1$ has a square root. Over this ring, the chart-transition automorphism group factors as $\langle q \rangle \rtimes \langle \iota \rangle$.

**Half-twist and ribbon structures.**
The categorical-coordinate construction never requires the ribbon element $v = q^{1/2}$. It appears exclusively when $\mathbf{C}$ carries an additional ribbon twist $\varTheta_V = q^{1/2}\,\mathrm{id}_V$ for framed-link invariants or Reshetikhin--Turaev TQFT ([rem:sqrt-q-ribbon-structure](#rem:sqrt-q-ribbon-structure)). The extracted square root of $\lambda_-$ lies strictly in $R[i]$ rather than any ribbon datum, standing independent of the eigenvalue-labelling convention $q := \lambda_+$ ([rem:braiding-unit-circle-convention](#rem:braiding-unit-circle-convention)).

**Crossing energy in the commutative limit.**
Setting $q = e^{i\varTheta}$ on the unit circle of $\mathrm{End}(\mathbf{1})$ yields:

$$
  q - q^{-1}  =  2i \sin\varTheta,
$$

where $\varTheta \in [0, \pi]$ tracks the orbit-space interval of [prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction). The polar fixed points $\varTheta = 0, \pi$ have zero weight. The interior acts as the free $S^1$-fibre. At $\varTheta = \pi/2$ (where $q = i$), the weight reaches its maximum $|2i \sin(\pi/2)| = 2$. The non-commutative Hecke energy $q - q^{-1}$ is exactly the algebraic deformation of this commutative-limit form.
