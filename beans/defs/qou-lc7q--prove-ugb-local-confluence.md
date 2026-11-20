---
# qou-lc7q
title: 'Prove UGB local_confluence (Bergman diamond lemma), the last Diamond-Lemma axiom'
status: completed
type: task
priority: high
created_at: 2026-11-20T17:00:00Z
updated_at: 2026-11-20T19:00:00Z
parent: qou-uhx0
---

W12, owner approval 2026-11-20 ("3"). `UGB.GrobnerShirshov.local_confluence` (CompositionLemma.lean:83) is the one axiom left under `normal_form_unique` and every `heckeCompleted_*` uniqueness result (`reduction_well_founded` proved in PR #8582).

## Scoping (2026-11-20)

Statement: GS basis (every overlap/inclusion S-polynomial has SOME reduction to zero) + no quasi-zeros + unit leading coefficients ⇒ any two single steps f → g₁, f → g₂ have a common multi-step reduct.

Why it is not a short proof:
- The docstring's three-case sketch (disjoint / overlap / inclusion) is the textbook outline, but in the linear setting it does not close locally. In the overlap case the hypothesis gives `g₁ − g₂ = c·(a·spoly·b) →* 0`, and a reduction of a difference does not by itself give a common reduct of g₁ and g₂: reduction is not additive (a step needs a non-zero coefficient, which a sum can cancel).
- Bergman (1978, Lemma 1.1 and the proof of Thm 1.2) and Guiraud–Hoffbeck–Malbos (critical-pair lemma for TERMINATING left-monomial linear rewriting systems) both close it with an induction on the order: "everything strictly below w is reduction-unique" is used while resolving branchings at w. So the honest Lean route proves reduction-uniqueness directly by well-founded induction (the `DMLt` order of PR #8582 is the measure), and derives `local_confluence` and `confluence` from it, not the other way round.
- Ring generality: the axiom is stated for any Ring k with unit lc. Bergman works over a commutative base ring with monic rules; non-commutative k needs checking (c·lc = coefficient is solved on the left).

## Plan
1. `reduction_unique_below`: by WF induction on the max live monomial, any f all of whose live monomials are < w has a unique normal form.
2. The I_w-ideal lemma (Bergman 1.1): if every ambiguity at a word ≤ w resolves relative to `< w`, then `a·r·b` reduces to 0 for every rule r with `a·lm(r)·b ≤ w`.
3. Branch cases at a single word: disjoint, overlap (uses `overlap_resolves` + step 2), inclusion.
4. Conclude unique NF ⇒ `local_confluence` as a theorem with the same signature.

Estimate: several sessions, ~1–2k Lean lines. Not started in code.

## 2026-11-20 17:30 — the axiom as stated is FALSE (W12, PR #8612)
`local_confluence` demands a structurally equal common reduct, but steps fix their target only up to CoeffEq (free `support` superset). Counterexample (axiom-free, `LocalConfluenceSupportRefutation.lean`): monic one-letter rule `K` over ℤ, `K → 0` with support ∅ and with support {K}; both normal, unequal. `example : False` compiles from the axiom. `normal_form_unique` (structural `=`) is false for the same reason. Repair: Diamond Lemma up to CoeffEq, then restate consumers.

Also: k must be commutative for the proof: the S-polynomial is `lc₂·rel₁C − lc₁·A·rel₂`; it is a unit multiple of the monic composition only if lc₁lc₂ = lc₂lc₁.

## Resolution (W12, 2026-11-20) — PR #8612 @ 02d6e886030 (ready-to-merge)
- `DiamondLemma.lean`: `Diamond.reductionUnique` — GS basis + unit lc + CommRing ⇒ all normal forms CoeffEq. Bergman Thm 1.2 (operators, Lemma 1.1 additivity, JM ideal below v, disjoint/overlap/inclusion, WF induction). ~1000 lines, sorry-free, axioms = propext/Classical.choice/Quot.sound.
- `local_confluence` axiom deleted (it was false: `LocalConfluenceSupportRefutation`, axiom proved False); now a theorem up to CoeffEq. `confluence`, `normal_form_unique` and 8 consumers restated up to CoeffEq; `composition_lemma` needs no uniqueness.
- UGB now has no Diamond-Lemma axiom. Remaining UGB axioms elsewhere (not this bean): `qSerre_is_gs_basis` (NormalForms.lean), JetOrder's three, StrongMultiplicativity's `tensorOrder`.
- Follow-up after #8598 merges: one sentence each in `hecke-normal-form.ts` authorNote and `nuclear-groebner-reduction-proof.md` (both still say local_confluence is an axiom).
