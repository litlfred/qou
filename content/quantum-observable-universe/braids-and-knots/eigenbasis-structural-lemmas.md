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
conclusion derived — not assumed. The exact-symbolic verification is the probe
`eigenbasis-structural-lemmas` (merged in PR #2502); the present remark records
the Lean formalisation that closes its `lean_followup`.
