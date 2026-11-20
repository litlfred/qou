### Naming: the electroweak carriers

The three carrier powers of [the Hoefsmit cell content](#thm:hoefsmit-ew-cell-content) are named after the electroweak force-carriers:

$$
  W \;\longleftrightarrow\; \sigma_1^{\,4} \;\;(\text{strands 1--2}),
  \quad
  Z \;\longleftrightarrow\; \sigma_3^{\,6} \;\;(\text{strands 3--4}),
  \quad
  H \;\longleftrightarrow\; \sigma_5^{\,8} \;\;(\text{strands 5--6}),
$$

and the six patterns other than $(s,s,s)$ and $(a,a,a)$ are named the $W^\pm, Z^\pm, H^\pm$ projectors. On its own strand pair the carrier $\sigma^{2k}$, $k = 2, 3, 4$, closes to a two-component link of writhe $2k$, and in the standard braid presentation of torus links that closure is the torus link $T(2, 2k)$; so the carriers are read as $T(2,4), T(2,6), T(2,8)$ on Bring's surface. This is a naming of constructions. That these links are the physical $W^\pm, Z$ and $H$ is [the electroweak/Higgs torus-link identification](#conj:electroweak-higgs-torus-link-triplet), and the boson-to-strand-pair assignment is part of [the categorical Higgs mechanism](#conj:categorical-higgs-mechanism). Neither is used by the theorem.

### Minimality of $n = 6$

Each EW carrier acts on a single strand-pair. Three carriers need three disjoint strand-pairs. For $n < 6$, carriers share strand-pairs, their generators no longer commute, and the simultaneous-eigenspace decomposition degenerates.

### Refinement: coupling via interface knot

The disjoint-product framing treats $W, Z, H$ as independent. The corrected EW braid uses an **interface knot** $\bowtie_K \in H_6(q)$ to mediate the coupling, analogous to the inter-nucleon interface in the deuteron derivation. The corrected braid is:

$$
  \beta_{\rm EW}(\bowtie_K)
  \;:=\;
  \sigma_1^{\,4} \cdot \bowtie_K^{(W \to Z)} \cdot \sigma_3^{\,6}
  \cdot \bowtie_K^{(Z \to H)} \cdot \sigma_5^{\,8} \cdot \bowtie_K^{(H \to W)}.
$$

This modifies pattern multiplicities, impacts bar-self-duality, gives the Higgs-vev automorphism a concrete form, and twists the 8 pure patterns.

### Resolution of the dimension-collapse issue

The six EW projectors live as rank-1 to rank-3 projectors in $\mathrm{End}_R(V^{\otimes 6})$. They sit alongside two non-EW projectors (vacuum and fully-broken), resolving the dimension-collapse issue of the $H_2(q)$-only completeness sum.

### The Plancherel weight is a degenerate special case

The earlier Plancherel-weighted multiplier framing is incorrect. The structural multiplier is the direct unweighted trace $\mathrm{tr}_{\rm pure}$, which preserves bar-self-duality automatically from the disjoint-strand-pair construction.

### Implication for $N_v$ derivation

The constrained-PSLQ basis for $N_v$ must use the direct cell-content trace $\mathrm{tr}_{\rm pure}$ as the structural input, demoting the Plancherel framing to a degenerate special case.

### Historical alignment: quaternionic electroweak theory

The disjoint-strand-pair identification parallels Morita's quaternionic formulation of the electroweak sector. The QOU tetraplectic boundary supplies a geometric home for the $\mathrm{SU}(2)$ structures. The unit-quaternion actions are norm-preserving and commute; identifying these algebraic actions with physical carriers is an interpretive alignment, not a derivation.
