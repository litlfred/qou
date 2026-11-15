---
# qou-hlxp
title: 'Research: can parity be the map σ ↦ −σ (covering q ↦ q⁻¹), and can P exist at the observable level?'
status: todo
type: task
priority: normal
tags:
    - quark-state
    - chirality
    - parity
parent: qou-qs0e
created_at: 2026-11-15T10:00:00Z
updated_at: 2026-11-15T10:00:00Z
---

Owner decision D-H5 = D + C (relayed by coordinator 2026-11-15). This bean is (C).

Established (`QOU/QuarkState/HelicityCommonSource.lean`; audit
`docs/audits/2026-11-15-helicity-common-source-flavour-chirality.md` §10):
- The letter maps flip σ↦σ⁻¹, swap σ↦−σ⁻¹ and neg σ↦−σ form a Klein four-group.
- neg exchanges the eigenprojectors (`neg_Pp`) and sends e⁻ ↦ −e⁻ (`neg_electron`): the
  profile of P, with the sign (−1)^length.
- neg is NOT a K-linear algebra map unless q² = 1 (`no_linear_neg`). It exists only covering
  q ↦ q⁻¹ on the scalars, which has no counterpart at real q₀ (ℝ has no nontrivial ring
  automorphism; standard, not formalised).

Research questions (open; nothing adopted):
1. Argue, or refute, reading R2: that q ↦ q⁻¹ carries no physical content, so neg is P and not
   PT (under R1, where q ↦ q⁻¹ is antilinear-like, neg is PT). The deciding input must be
   DERIVED, e.g. from what the archimedean functor does with q ↦ q⁻¹, not chosen to match
   physics.
2. Can P exist at the observable level? Candidates: a map between H(q₀) and H(q₀⁻¹) composed
   with an identification, or a P acting on the cone side (stream 6b) rather than on letters.
3. The sign (−1)^length on odd words (P(e⁻) = −e⁻): is it observable? It negates traces.

Anti-fit: no number may decide any of these.
