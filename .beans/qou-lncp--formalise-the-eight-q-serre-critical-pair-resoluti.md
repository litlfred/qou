---
# qou-lncp
title: Formalise the eight q-Serre critical-pair resolutions to discharge qSerre_is_gs_basis
status: todo
type: task
created_at: 2026-08-10T12:46:45Z
updated_at: 2026-08-10T12:46:45Z
---


---

## 2026-08-10 — the axiom is reduced to exactly the 8 pairs, machine-checked

New module
[`UGB/GrobnerShirshov/QSerreCriticalPairs.lean`](../content/unital-groebner-bases/lean/UGB/GrobnerShirshov/QSerreCriticalPairs.lean).
Everything below is sorry-free and depends on nothing but
`[propext, Classical.choice, Quot.sound]`.

### The structural facts

* `qSerre_lm_length` — all seven leading monomials are **two-letter** words.
* `qSerre_rule_eq_of_lm_eq` — the seven are pairwise distinct, so a rule of the
  system is determined by its leading monomial.

Those two collapse most of `IsGrobnerShirshovBasis`, which quantifies over
*every* composition and so looks unbounded:

* **`inclusion_resolves` is fully DISCHARGED** (`qSerre_inclusion_resolves`).
  `outer.lm = left ++ inner.lm ++ right` with both sides length 2 forces
  `left = right = []` on length grounds alone, hence `outer = inner`, hence the
  S-polynomial is a difference of an element with itself. No computation.
* **Overlaps admit only two shapes** (`qSerre_overlap_shape`): `|overlap| = 1`
  (the genuine pairs, `left`/`right` single letters) or `|overlap| = 2`
  (degenerate — the rules coincide), and the degenerate one resolves
  (`qSerre_overlap_resolves_of_length_two`).

### The payoff

`qSerre_is_gs_basis_of_critical_pairs` — **a theorem**:

> if every overlap composition with `|overlap| = 1` has an S-polynomial
> reducing to zero, then the q-Serre system **is** a Gröbner–Shirshov basis.

So the axiom's entire remaining content is the length-1 case, which qou-18s7
enumerated: **8 ambiguities, all verified to resolve**. Discharging that
hypothesis discharges the axiom outright.

### Measured remainder — 6 chains, not 8

Computing `spoly = a·tail₂ − tail₁·c` (the ambient word cancels because the
rules are monic) for each of the 8:

* **R1/R2** on `K K⁻¹ K` and **R2/R1** on `K⁻¹ K K⁻¹` have `tail = 1` on both
  sides, so `spoly = K − K = 0` **literally**. Those two need no reduction at
  all — `MultiStepReduction.refl` plus `isZero`.
* the other **6** need a genuine chain: R1/R6, R1/R7, R2/R3, R2/R4 are two steps
  each; R3/R5 and R6/R5 are longer, being the ones that pass through rule 5's
  four-term right-hand side.

Cost driver for each chain: the `CoeffEq` field of `SingleStepReduction` is
cheap if the target is *defined* as `sub f (smul c (contextMul a rel b))` —
then it is `fun _ => rfl`. The expensive obligations are evaluating
`f.coeff (a ++ lm ++ b) ≠ 0` at a concrete word, and the final `isZero`, which
is an identity of coefficient functions at *every* monomial and so a case bash
over the ~6 concrete words in play.

### Also

41 of the 49 ordered rule pairs admit no length-1 overlap at all (the second
letter of `lm₁` differs from the first of `lm₂`); those close by contradiction
from the decomposition equations. That enumeration is not yet written — it is
part of discharging `hcp`.
