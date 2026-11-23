**Remark (categorical coordinate of the commutative limit).**
The Hecke generator $\sigma = P \circ R$ on $V \otimes V$ has eigenvalues $(\lambda_+, \lambda_-) = (q, -q^{-1})$ on the symmetric/antisymmetric decomposition $S^2 V \oplus \Lambda^2 V$ ([def:crossing-energy](#def:crossing-energy)). At $q = 1$ ([def:commutative-qou](#def:commutative-qou)), the eigenvalues collapse to $(+1, -1) = \mathbb{Z}_2$, and the per-crossing weight $q - q^{-1}$ vanishes identically. The categorical structure of the commutative limit is recovered by extracting the *square root* of the antisymmetric eigenvalue $\lambda_- = -1$:

$$
  i  =  \sqrt{\lambda_-}, \qquad i^2 + 1  =  0  \;\text{in}\; R[i].
$$

The categorical structure forces the ring extension $R[i]$ (the universal $R$-algebra containing an element $i$ with $i^2 = -1$). The element $i$ is the **categorical coordinate of $\mathbb{P}(V)$ in the commutative limit**, mirroring the role of $q$ in the non-commutative theory. The construction is intrinsic to $R$; no real or complex numbers are assumed. When $R$ already contains a square root of $-1$ (e.g. the archimedean realisation where $R = \mathbb{C}$, see [archimedean realisations](#rem:archimedean-realisations)), $i \in R$ is canonical. When $R$ does not (e.g. $R = \mathbb{Z}[q, q^{-1}]$ at $q = 1$), $R[i]$ is the minimal extension realising $\lambda_-$ as a categorical square.

**Categorical-coordinate dictionary.**

See [Table 1](#tbl:commutative-crossing-energy-table1-data).

**Deformation hierarchy.** The discrete Weyl group $\mathbb{Z}_2$ embeds into the continuous maximal torus, which itself is the $q = 1$ fibre of the quantum torus:

$$
  \mathbb{Z}_2  \;\hookrightarrow\;  \mathrm{U}(1)  \;\hookrightarrow\;
   \mathrm{U}_q(1).
$$

Each inclusion identifies a different categorical coordinate on $\mathrm{End}(\mathbf{1})$. The value $-1$ generates $\mathbb{Z}_2$; $i$ generates $\mathrm{U}(1)$ at the quarter-turn $\varTheta = \pi/2$; and $q$ generates $\mathrm{U}_q(1)$ off-locus. The standard non-commutative deformation $\mathrm{SU}(2) \rightsquigarrow \mathrm{SU}_q(2)$ acts on the second inclusion. The commutative-limit *enlargement* $\mathbb{Z}_2 \hookrightarrow \mathrm{U}(1)$ acts on the first. These are the two mechanisms to escape the $q = 1$ degeneracy of $q - q^{-1}$.

**Three categorical readings of $i$ on $\mathbb{P}(V)$.**

1. *Algebraic.* $i = \sqrt{\lambda_-} \in \mathrm{End}_{R[i]}(\mathbf{1})$ is the categorical square root of the antisymmetric braiding eigenvalue. This single datum appears in three faces: Wick rotation, CR complex structure, and arrow of time. All reduce to the binary choice of braiding orientation $c_{V,V}$ vs $c_{V,V}^{-1}$ ([rem:i-as-braiding-orientation](#rem:i-as-braiding-orientation)).
2. *Geometric.* $J = i \cdot \mathrm{id}_V \in \mathrm{End}_{R[i]}(V)$ is an endomorphism with $J^2 = -\mathrm{id}_V$, descending to a complex structure on $\mathbb{P}(V) = \mathrm{Proj}(\mathrm{Sym}\, V^\vee)$ over $R[i]$. In the archimedean realisation, this recovers the standard complex structure on the exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$ ([def:exceptional-divisor](#def:exceptional-divisor)).
3. *Equivariant.* The maximal torus $\mathrm{U}(1) \subset \mathrm{SU}(2)$ acts on $\mathbb{P}(V)$ with $i$ as the quarter-turn generator. The orbit space is $[0, \pi]$ with phase fibre $\varphi \in S^1$ over the interior ([prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction)).

The three readings coincide because each computes the same categorical datum: a square root of $\lambda_-$ in $\mathrm{End}_{R[i]}(V)$.

**Affine-chart origin.** Both $q$ and $i$ originate from the chart-transition data of $\mathbb{P}(V)$ ([rem:affine-chart-origin-of-i-and-q](#rem:affine-chart-origin-of-i-and-q)). The parameter $q$ constitutes the chart-transition coefficient $z\,w = q^{-1}$ on the quantum projective line $\mathbb{P}_q(V)$. The element $i$ is the square root of the chart-swap involution $\iota: z \mapsto z^{-1}$ that the transition collapses to at $q = 1$. Formally, the **categorical-coordinate ring** is the universal $R$-algebra extension $R[i, q^{\pm 1}] = R[q, q^{-1}][i]/(i^2 + 1)$ ([prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring)) in which $q$ is invertible and the involution-eigenvalue $-1$ possesses a square root. The chart-transition automorphism group factors as $\langle q \rangle \rtimes \langle \iota \rangle$ over this ring.

**Half-twist and ribbon structures.** The ribbon element $v = q^{1/2}$ is *not* required for the categorical-coordinate construction. It appears only when $\mathbf{C}$ carries an additional ribbon twist $\varTheta_V = q^{1/2}\,\mathrm{id}_V$ for framed-link invariants or Reshetikhin--Turaev TQFT ([rem:sqrt-q-ribbon-structure](#rem:sqrt-q-ribbon-structure)). Extract the square root of $\lambda_-$ within $R[i]$, not from any ribbon datum. It remains independent of the eigenvalue-labelling convention $q := \lambda_+$ ([rem:braiding-unit-circle-convention](#rem:braiding-unit-circle-convention)).

**Crossing energy in the commutative limit.** Setting $q = e^{i\varTheta}$ on the unit circle of $\mathrm{End}(\mathbf{1})$ gives

$$
  q - q^{-1}  =  2i \sin\varTheta,
$$

with $\varTheta \in [0, \pi]$ tracking the orbit-space interval of [prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction). The endpoints $\varTheta = 0, \pi$ define the polar fixed points (zero weight). The interior constitutes the free $S^1$-fibre. The point $\varTheta = \pi/2$ (where $q = i$) marks the location of maximum weight $|2i \sin(\pi/2)| = 2$. The Hecke energy $q - q^{-1}$ of the non-commutative theory operates as the algebraic deformation of this commutative-limit form.
