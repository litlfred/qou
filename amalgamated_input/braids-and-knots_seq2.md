<!-- FILE_START: categorical-braiding-hecke-eigenbasis-intro.md -->
The preceding sub-section established the categorical origin of
braiding (the braid action on tensor products, why $B_3$, the
categorical boson-fermion identification, and the symmetric-
quotient colour data). This sub-section then asks: what is the
Hecke quotient of the braid action, and how does its representation
theory furnish a basis of knot states?

The blocks below trace the Jones-Markov trace + $\mathrm{tr}_M$
Hopf $\sigma_1^2$ closed-form + Hecke logarithmic decomposition +
Hecke-algebra-from-braiding + Hecke normal form + dark-vision
strand bandwidth + Markov-moves brane tower, then close with the
knot eigenbasis (existence + proof + exhaustiveness) plus the
Feynman eigenbasis identification.

The section's output is the **knot eigenbasis**: a basis of
$\mathrm{End}_{\mathbf{C}}(A)$ indexed by knot equivalence classes,
diagonalising the Hecke action and computed in closed form on the
two-strand $B_3$ kernel.  Subsequent sub-sections re-use this basis
(eigenvalues, multiplicities, and the Feynman identification) as
the substrate-arithmetic input for binding-energy and mass
predictions; the eigenbasis is the chapter's structural pivot.
<!-- FILE_END: categorical-braiding-hecke-eigenbasis-intro.md -->

<!-- FILE_START: eigenbasis-structural-lemmas.md -->
The categorical-confinement proposition writes every physical observable as a
sum of Wedderburn residues, $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi_\lambda$,
one term per Wedderburn channel $V_\lambda$. The *content/twist eigenbasis*
organises those channel characters $\chi_\lambda$ by the ribbon-twist
eigenvalue $\theta_\lambda = q^{2c(\lambda)}$ — the scalar by which the full
twist $\varDelta^2 \in Z(H_n(q))$ acts on $V_\lambda$ — and pins three
structural facts about each $\chi_\lambda(\beta)$. All three are now formalised
sorry-free in Lean (`QOU.BraidKnot.EigenbasisStructuralLemmas`):

1. **Order-parity $=$ word-length parity (L1).** For a braid word $\beta$ of
   length $L$, every Laurent exponent of $\chi_\lambda(\beta)(q)$ has parity
   $\equiv L \pmod 2$; equivalently $\chi_\lambda(\beta)(-q) = (-1)^L\,
   \chi_\lambda(\beta)(q)$. (Lean: `character_support_parity`, the literal
   support form, and `character_qneg_parity`, its $q \mapsto -q$ evaluation
   face.)

2. **Bar-involution $=$ conjugation duality (L2).** The bar involution
   $q \mapsto q^{-1}$ swaps the seminormal eigenvalues $q \leftrightarrow
   -q^{-1}$, the intertwiner $V_\lambda \cong V_{\lambda'}$ to the conjugate
   channel, so $\chi_\lambda(q^{-1}) = \varepsilon_\lambda\,\chi_{\lambda'}(q)$
   with $\varepsilon_\lambda \in \{\pm 1\}$. (Lean: `character_bar_conjugate`,
   stated as a rigorous conditional on the seminormal bar–conjugate relation;
   the duality constant is derived, $\varepsilon_\lambda = s^L$.)

3. **Framing generating function (L3).** Framing $\beta$ by $m$ full twists
   scales $\chi_\lambda$ by $\theta_\lambda^m$, so the framing tower is the
   single-pole rational $\chi_\lambda(\beta)/(1 - t\,\theta_\lambda)$, with its
   only pole at $t = q^{-2c(\lambda)}$. (Lean: `framing_gf_closed_form`, and
   `framing_gf_ribbon` / `framing_gf_ribbon_class` discharged against the
   ribbon eigenvalue.)

These are the structural backbone of the per-channel characters that the
confinement decomposition sums: the parity (1) controls which crossing-counts
can contribute to a given channel, the conjugation duality (2) is the
matter/antimatter symmetry of the channel weights, and the framing rational (3)
fixes how reframing a confined braid redistributes weight across the tower.
Each lemma is a rigorous conditional on a clearly stated categorical input (the
ribbon eigenvalue; the seminormal bar–conjugate relation), with the structural
conclusion derived — not assumed. The companion compute probe supplies the
exact-symbolic verification, and the Lean formalisation establishes the same
lemmas categorically.
<!-- FILE_END: eigenbasis-structural-lemmas.md -->

