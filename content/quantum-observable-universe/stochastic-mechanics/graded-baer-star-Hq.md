**Conjecture (graded Baer-* on $\mathcal{H}_q$ across the depth filtration).**

*Let $\mathcal{H}_q$ be the substrate convolution Hopf algebra ([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)), filtered by iterated-integral depth ([keystone correspondence](#conj:gb-depth-period-correspondence)):*

$$
  G^{(0)}(\mathcal{H}_q) \;\subseteq\; G^{(1)}(\mathcal{H}_q)
  \;\subseteq\; G^{(2)}(\mathcal{H}_q) \;\subseteq\; \cdots.
$$

*Each filtration piece $G^{(n)}(\mathcal{H}_q)$ forms a Baer-*-ring under the bar involution. The inclusions $G^{(n)} \hookrightarrow G^{(n+1)}$ operate as **Baer-*-morphisms**. They send projections to projections and preserve the annihilator-generation property. Equivalently: $\mathcal{H}_q$ admits a system of orthogonal projections $\{p_n^{(i)}\}_{n,i}$ indexed by depth $n$ and intra-depth label $i$, satisfying:*

- *each $p_n^{(i)}$ is self-adjoint under $* \colon q \mapsto q^{-1}$,*
- *$p_n^{(i)} p_m^{(j)} = 0$ when $(n, i) \neq (m, j)$,*
- *$\sum_{i} p_n^{(i)} \cdot \mathrm{id}_{G^{(n)}} = \mathrm{id}_{G^{(n)}}$ (completeness at each depth).*

### Structural justification

Discharging this conjecture grants three consequences:

1. **Explicit Goncharov-period witnesses.** Each projection $p_n^{(i)} \cdot \mathrm{Li}_n^q(z)$ under $\tau_{\mathrm{arch}}$ generates a *specific* element of $\mathcal{P}_n / \mathcal{P}_{n-1}$. This names a real-number period class via a finite algebraic label. (Without graded Baer-*, B1 only asserts existence.)
2. **Graded Mikusiński localisation.** The field-of-fractions tower $\mathcal{M}_q^{(n)}$ inherits a graded Baer-* structure. Each $\mathcal{M}_q^{(n)}$ forms a Baer-*-ring. Its "delta at depth $n$" equals $1/\omega^n$ on the surreal envelope, corresponding to a specific projection. The graded Titchmarsh question ([keystone §discharge targets](#conj:gb-depth-period-correspondence)) becomes tractable: zero divisors at depth $n$ correspond precisely to non-trivial $p_n^{(i)} \cdot p_n^{(j)}$ for $i \neq j$.
3. **Bar-involution-equivariant period theory.** Self-adjoint $p_n^{(i)}$ generate *real* periods (bar-fixed loci of $\mathcal{P}_n$). Bar-swapped pairs generate *chirality-twisted* periods (eigenspaces of bar with eigenvalue $-1$, equivalently periods of motives with a Tate twist). See [`rem:chirality-period-pairing`](#rem:chirality-period-pairing).

### Reduction to known structure

At depth 0 (scalars + $\exp_q$), the Baer-* property is trivial. $G^{(0)}$ is a field.

At depth 1 ($\log_q$ adjoined), the property mirrors Baker's theorem infrastructure. It governs annihilators of $\log\alpha$-relations among algebraic $\alpha$. Baer-* at this depth demands the linear independence of logarithms of multiplicatively independent algebraics (Baker 1966; Wüstholz). This is conjecturally known.

At depth 2 ($\mathrm{Li}_2^q$ adjoined), the property reduces to the Hecke algebra Baer-* result ([`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic)). The depth-2 grouplikes pair with $H_n(q)$-cells via the Markov trace. The projections are the Hoefsmit idempotents $e_\lambda$, lifted to $\mathcal{H}_q$ via Schur–Weyl duality.

At depth $\geq 3$, the property remains open. The depth-3 case requires identifying projections compatible with the trilog grouplike $\mathrm{Li}_3^q$. See the depth-3 witness ([`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)).
