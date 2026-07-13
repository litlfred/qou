<!-- FILE_START: intro-kashiwara-jones-quantum-dilog.md -->
The Kashiwara crystal-basis framework and the Jones polynomial present two faces of the same categorical data: one combinatorial, one analytic. This section identifies the quantum dilogarithm $\mathrm{Li}_2^q$ as the bridge. The Kashiwara-Jones alternation evaluates a Jones polynomial at the Kashiwara crystal-basis sum, producing a quantum-dilogarithm identity that completes the cycle.

The sequence proceeds in three steps. We first establish the Kashiwara-Jones alternation as a generating-function identity. We then specialize the identity to the substrate parameter and expose the quantum-dilogarithm cocycle that governs the combinatorial decomposition. Finally, we survey the consequences for Reshetikhin-Turaev invariants, the quantum Volume Conjecture, and Hopf-categorical extensions.

This establishes $\mathrm{Li}_2^q$ as the canonical level-2 categorical cocycle for the $q$-geometric-Langlands framework.
<!-- FILE_END: intro-kashiwara-jones-quantum-dilog.md -->

<!-- FILE_START: kashiwara-jones-alternation-interpretation.md -->
The categorical precision ladder exhibits an empirical alternating pattern in its coefficients:

| $k$ | Origin |
|:---:|:---|
| 1 | Kashiwara crystal $\tilde f_1$ matrix element $b$ |
| 2 | Kashiwara $\tilde f_1^\dagger \tilde f_1$ return amplitude $b^2$ |
| 3 | Classical-limit Jones $J_{\text{Hopf}}(q=1) = -2$ |
| 4 | Mixed: $b^2 + 1/2$ |

This alternation stems from the fact that the Kashiwara and Jones contributions arise from different moduli spaces. The Kashiwara crystal lives in the moduli of finite-dimensional $U_q(\mathfrak{sl}_2)$ representations. The Jones polynomial lives in the moduli of knot complements. The Markov trace sits at the intersection, computing the closure of a typed braid that lives in $H_n(q)$ and produces a link invariant.

The parity rule governs this alternation. Even $k$ stays within the Kashiwara block, as the Hecke quadratic reduces $\sigma_i^k$ to a polynomial within $H_n(q)$, generating no link invariant. Odd $k$ produces an even crossing number upon closure, yielding a topological link invariant. The Jones value of this link emerges via the Markov trace.

The precision ladder utilizes a Gröbner-Buchberger filtration indexed by jet order. The Hecke quadratic increases jet order by one. The precision-ladder rungs correspond exactly to distinct jet orders, with the twist scaling as $\hbar_q^{2k}$. Hyperbolic closures contribute topological volume and integer Jones values, while torus operators remain geometrically trivial. The alternating pattern breaks down at $c_5, c_6$ because mixed-order links and cross-block Hoefsmit couplings introduce simultaneous Kashiwara and Jones contributions. The trace serves as the structural bridge interleaving these two moduli spaces.
<!-- FILE_END: kashiwara-jones-alternation-interpretation.md -->

<!-- FILE_START: canonical-braid-interface-composition.md -->
**Definition (canonical-braid interface composition).**
*Let $\beta(Z, N) \in H_{3A}(q)$ be the canonical atomic braid in standard pppnnn ordering. The $A - 1$ inter-nucleon interface generators $\sigma_{3k + 2}$ are classified by the flavour pair they bridge:*

See [Table 1](#tbl:canonical-braid-interface-composition-table1-data).

*The composition $(n_{pp}, n_{pn}, n_{nn})$ counts these three types. Under canonical ordering, the closed forms are:*

$$
n_{pp} = \max(0, Z - 1), \quad
n_{nn} = \max(0, N - 1), \quad
n_{pn} = \begin{cases} 1 & Z \geq 1, N \geq 1 \\ 0 & \text{else}\end{cases}
$$

*with total count summing to $A - 1$.*

See [Table 2](#tbl:canonical-braid-interface-composition-table2-data).

The asymmetric counts $(n_{pp}, n_{nn})$ encode the $Z \leftrightarrow N$ asymmetry directly. Alternative orderings produce different interface compositions. The canonical formalism fixes the pppnnn ordering.

The interface asymmetry isolates the ${}^{3}$He anomaly. A linear fit across the interfaces evaluates the 4-atom set, requiring evaluation against larger $A$ to verify structural predictions.
<!-- FILE_END: canonical-braid-interface-composition.md -->

<!-- FILE_START: prop-rigid-monoidal-structural-gap-invariance.md -->
*Let $\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$ be the rigid monoidal category. Let $\tau \colon \mathrm{End}_{\mathbf{C}}(A^{\otimes n}) \to \mathbb{C}_q$ be the canonical Markov trace. Define the categorical structural gap for a confined particle $\mathfrak{H}$ as:*

$$
  \Delta_{\mathrm{cat}}(\mathfrak{H}) := B_{\mathrm{AME}}(\mathfrak{H}) - m_e \cdot \rho \cdot \bigl|\tau(\beta_{\mathfrak{H}})\bigr|.
$$

*The value $\Delta_{\mathrm{cat}}(\mathfrak{H})$ depends only on the categorical-trace invariant $\tau(\beta_{\mathfrak{H}})$. It is strictly invariant under any choice of operator-volume convention.*

The Markov trace $\tau$ is uniquely determined by the categorical axioms up to the choice of parameter $z$. Operator-volume conventions vary only the non-categorical regularizer. Differences in regularizer choices cancel into the identical $\Delta_{\mathrm{cat}}$ value.

The Type-B folding maps the stable matter fixed points into a symmetric Kashiwara crystal. The spin involution acts as the folded-crystal involution. The Markov trace and LP-dual operator selections are strictly spin-invariant. This rigidly unifies pair-knot selection at magic shells, substrate-binding symmetry, and convention independence.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: prop-rigid-monoidal-structural-gap-invariance.md -->

<!-- FILE_START: qz-bicompletion.md -->
**Definition (proposed; conjectural utility).**
*The $(q, z)$-bicompletion is the inverse limit*

$$
  \widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z} := \varprojlim_{(m, n)} \mathbb{Z}[q^{\pm 1}, z] \big/ \bigl(I_{m,n}\bigr),
$$

*indexed by pairs $(m, n) \in \mathbb{N}^2$, with the bigraded ideal*

$$
  I_{m,n} := \bigl((q;q)_m \cdot P_n(q, z)\bigr).
$$

The bicompletion unifies the $q$-only Habiro ring and the $z$-only Habiro ring at the apex of the cyclotomic completions diagram.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: qz-bicompletion.md -->

<!-- FILE_START: qz-bicompletion-properties.md -->
The $(q, z)$-bicompletion governs the conjectural mass element. It unifies the colored Jones invariants (living in $\widehat{\mathbb{Z}[q]}$) and the brane-tower partial sums (living in the $z$-Habiro ring). The mass formula couples these pieces through the $q$-deformed Markov-trace pairing. A single ambient ring is necessary to formalize this relation algebraically.

The conjectural mass element $\mathfrak{m}^{\widehat{\;}}$ simultaneously recovers the colored Jones invariants and the brane-tower partial sums under respective cyclotomic projections. This construction elevates the asymptotic Volume Conjecture to a rigorous algebraic identity within the bicompletion. Open challenges include finalizing the existence proof and identifying the corresponding $p$-adic projections.
<!-- FILE_END: qz-bicompletion-properties.md -->

<!-- FILE_START: quantum-dilogarithm-stratified.md -->
*Let $A = H_n(R, q)$ be a semisimple Hecke algebra. Decompose its centre $Z(A)$ by GB-depth of partitions. The analytic quantum dilogarithm admits a centre-stratified expansion:*

$$
  \mathrm{tr}_M\!\bigl(\Phi_q(z_i) \cdot T_w\bigr) = \sum_{k = 0}^{\infty} \bigl\langle \phi_q^{(k)}(z_i),\, T_w \bigr\rangle,
$$

*where the depth-$k$ coefficient $\phi_q^{(k)}$ is the Frobenius dual of the truncation increment. The partial sum $\Phi_q^{[\leq k]}$ captures exactly the $\bigoplus_{j \leq k} Z^{(j)}(A)$-content.*

**Corollary (truncation).**
*For $T_w$ with NF support depth $k_\star(T_w)$, the trace truncates precisely to:*

$$
  \mathrm{tr}_M\!\bigl(\Phi_q(z_i) \cdot T_w\bigr) = \mathrm{tr}_M\!\bigl(\Phi_q^{[\leq k_\star(T_w)]}(z_i) \cdot T_w\bigr).
$$

The analytic infinite product truncates to a finite product as a Frobenius-paired identity. The truncation depth is structurally locked to the NF support of $T_w$. The analytic divergence is a side-effect, absent from the categorical mass.
<!-- FILE_END: quantum-dilogarithm-stratified.md -->

<!-- FILE_START: q-pochhammer-partial-product.md -->
**Definition.**
*The $q$-Pochhammer partial product at depth $n$ is the finite rational function:*

$$
  \Phi_n(x; q) := \prod_{k=0}^{n-1} \frac{1}{1 - x q^k} = \frac{1}{(x; q)_n}.
$$

*The denominator $(x; q)_n$ carries simple roots at $x = q^{-k}$. This finite product is structurally valid at the $q_0 > 1$ substrate. It corresponds exactly to the categorical truncation $\Phi_q^{[\leq n]}$.*

The partial product satisfies the one-step recurrence $\Phi_{n+1} = \Phi_n / (1 - x q^n)$, which mirrors the filtration induction step. The denominator zeros $x = q^{-k}$ define the cuspidal boundary of the JSJ geometry. The algebraic engine uses these zeros as exact initial seeds for the Newton-Raphson solver.
<!-- FILE_END: q-pochhammer-partial-product.md -->

<!-- FILE_START: phi-q-categorical-truncation.md -->
*Let $\mathfrak{H}$ be a confined particle with Hecke NF $T_w$. The categorical brane-tower contribution truncates to the finite sum:*

$$
  \mathfrak{m}^{\mathrm{tower}}_{q,\mathcal{K}}(T_w) = \sum_{k=0}^{k_\star(T_w)} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(T_w) = \sum_i \Phi_q^{[\leq k_\star(T_w)]}(z_i).
$$

*The depth $k_\star(T_w)$ is exactly the maximum GB-depth among the support partitions. Truncation at any deeper level $k \geq k_\star$ yields the identical categorical value.*
<!-- FILE_END: phi-q-categorical-truncation.md -->

<!-- FILE_START: phi-q-categorical-truncation-interpretation.md -->
The parameter $k_{\max}$ recorded in witness data represents the Coxeter-length filtration. This strictly differs from the structural GB-depth $k_\star(T_w)$. The witness $k_{\max}$ overestimates depth due to strand-padding artifacts.

The structural truncation depth sets a rigid upper bound $k_\star \leq n_0$. The canonical real-valued mass requires the uniform $z$-Habiro bound to achieve canonical closed-form agreement, as truncation depths diverge empirically if left unregularized.
<!-- FILE_END: phi-q-categorical-truncation-interpretation.md -->

<!-- FILE_START: pachner-pentagon-borromean.md -->
**Conjecture (D15 Pachner-Pentagon closure).**
*The Pachner $2$–$3$ move on the ideal-tetrahedron decomposition of the Borromean complement realises the Pentagon identity for $\Phi_q$ at the state-sum level. The $-3/4$ coefficient of the Markov trace matches the difference between the 8-octahedron and 16-tetrahedron decompositions.*

The Borromean complement triangulates into 8 ideal octahedra, splitting into 16 tetrahedra via the Pachner move. Pachner invariance demands that $\Phi_q$ satisfy the Pentagon identity. The conjecture identifies the $h^4 = -3/4$ coefficient categorically with the state-sum evaluation of this 16-tetrahedron network. This establishes a high-value cross-validation linking the geometric Pentagon to the topological Markov trace.
<!-- FILE_END: pachner-pentagon-borromean.md -->

<!-- FILE_START: q-rogers-pentagon-archimedean.md -->
*The pre-$\tau$ bare pentagon operates formally in the Hopf algebra without log-squared terms. Under the archimedean realization functor, the post-$\tau$ pentagon acquires the $\log_q^2$ correction:*

$$
  \mathrm{Li}_2^q(u) + \mathrm{Li}_2^q(v) - \mathrm{Li}_2^q(uv) - \mathrm{Li}_2^q(\alpha) - \mathrm{Li}_2^q(\beta) = \log_q\!\!\left(\frac{1-u}{1-uv}\right) \cdot \log_q\!\!\left(\frac{1-v}{1-uv}\right) + O\bigl((q-1)^2\bigr).
$$

The realization functor introduces rational denominators, triggering the $\log_q^2$ Rogers correction. This correction anchors the post-$\tau$ pentagon as the definitive identity for the analytic Volume-conjecture framework. The $O((q-1)^2)$ residual acts as the formal testable prediction for archimedean convergence.
<!-- FILE_END: q-rogers-pentagon-archimedean.md -->

