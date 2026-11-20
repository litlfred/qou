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
updated_at: 2026-11-20T16:06:50Z
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

## 2026-11-15 exact pullback of the convention-D trace (PR #7960, issue #7959)

Each letter map is a K-linear algebra isomorphism: neg and flip go H_n(q) → H_n(q⁻¹), and ι goes
H_n(q) → H_n(q). Pull the convention-D Ocneanu trace back along each map (exact sympy, n = 2, 3, 4,
`computations/probes/parity_neg_pullback_of_d_trace_probe.py`):
- flip: gives the D trace exactly (z_D is bar-fixed).
- neg and ι: give the Markov trace with z = −1/(q(q²+1)) = z_D(−1/q), the transposed convention. It
  kills the q-symmetriser at n = 3, where D kills the q-antisymmetriser.
Bearing on the research questions:
- Q1: as a map H(q) → H(q⁻¹), neg is K-linear; no antilinear reading is needed.
- Q3: the observable sign question is sharper than (−1)^length. P sends the D trace to a different
  Markov trace, so tr_D∘P is not ±tr_D at any n ≥ 2.
P is not a symmetry of the ruled trace. Status stays todo, since Q2 (P at the observable level) is
open.

## Progress (PR #8457)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/PairingSpaceActionRetypeRuledOddProjectionLetterInvolutionPullbackQuotientKernelMultiplierSlope.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_h0ou_hlx8_hlxp_i9gk_slpd_probe.witness.json` (`Commit 1` = `6615e05829d98e7dc8f3151a6136022620b0fa75`, `HEAD` = `87f824354a46b08a4af8436ed872967b2f3dfc59`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8457, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
