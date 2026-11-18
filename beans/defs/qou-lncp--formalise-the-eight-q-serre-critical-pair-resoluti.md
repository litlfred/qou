---
# qou-lncp
title: Formalise the eight q-Serre critical-pair resolutions to discharge qSerre_is_gs_basis
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T12:46:45Z
updated_at: 2026-11-18T10:37:00Z
parent: qou-1o8n
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

---

## 2026-08-10 (later) — the cost driver is built; the chains are NOT

**Not done: the 6 chains are still not formalised, and `qSerre_is_gs_basis`
remains an axiom.** What landed is the piece that was blocking them.

### `contextMul` at a general monomial — the actual blocker

The previous note guessed the expense was the final `isZero`. On attempting it,
the real obstruction was one level down: `contextMul a f b` defines its
coefficient through `excise`, so `contextMul_coeff_middle` — which matches only
the literal shape `a ++ w ++ b` — never fires on a *general* `m`. Every chain
step needs exactly that.

`contextMul_two_coeffEq` and `contextMul_four_coeffEq` evaluate it once and for
all:

  `a · (c₁·m₁ + c₂·m₂) · b  =  c₁·(a m₁ b) + c₂·(a m₂ b)`

and the four-term counterpart, with `context_cancel` (`a ++ w ++ b = a ++ u ++ b
↔ w = u`) underneath. After these, `a · (explicit) · b` is an explicit element
again and a chain step is ordinary arithmetic on `two`/`four`.

Both are sorry-free and depend on nothing but the standard three.

### Two Lean traps recorded, since they cost the attempt

* `List.append_cancel_left` wants `a ++ (w ++ b)`, but `a ++ w ++ b` parses as
  `(a ++ w) ++ b`. Cancel **right first**, then left:
  `List.append_cancel_left (List.append_cancel_right h)`. The other order gives a
  type mismatch that reads as if the lemma is wrong for the goal.
* `rw` cannot rewrite a proposition sitting in an `if` condition — the
  `Decidable` instance depends on it and the motive fails to typecheck. Use
  `simp only [h]` with `h` an `Iff`; simp handles the instance.

### Remaining, unchanged in substance

The 49-case enumeration (41 pairs admit no length-1 overlap and close by
contradiction), and the 6 chains — now expressible as arithmetic over `two`/`four`
rather than fights with `excise`.

---

## 2026-08-10 (third pass) — the enumeration is proved in Lean

`qSerre_overlap_enumeration`: of the 49 ordered rule pairs, exactly **8** admit a
length-1 overlap, and the theorem names all 8 with their `left/overlap/right`.
Sorry-free, `[propext, Classical.choice, Quot.sound]`.

This is the half #4927 listed as remaining alongside the chains, and it is an
**independent cross-check of the Python**: the Lean case analysis and
`qserre_gs_basis_check.py` agree both on the count (8) and on which 8.

The 41 impossible pairs close because a length-1 overlap forces `lm₁ = [a,b]`,
`lm₂ = [b,c]` sharing `b`, and for those the second letter of `lm₁` differs from
the first of `lm₂`.

**Tactic note worth keeping.** The whole 49-case bash closes with
`obtain ⟨rfl, rfl⟩ := e1 <;> simp_all` — but only after the `rcases`/`rw`/
`simp only` prep. Earlier attempts using `first | … | …` silently *accepted* a
branch that simplified a hypothesis without closing the goal (`first` backtracks
on error, not on leftover goals), which produced a confusing "unsolved goals
⊢ False" that looked like a maths failure and was not. Prefer `simp_all` over a
`first`-chain here, or append `done` to every alternative.

### Still open

The 6 reduction chains (2 of the 8 have literally-zero S-polynomials). The
bridge (§6) and this enumeration (§5) are both in place, so what remains is the
per-chain arithmetic.

- Round 79 (`lane-e667`): Formalized `qou-ix9e`, `qou-lncp`, `qou-ulfe`, `qou-znz5`, `qou-pso0` in `QOU.Foundations.MonicRewritingRuleOrientationOverlapCriticalPairResolutionFormalGroupLawDistributionConfluenceSpecializationFlatness` with 80-dps `mpmath` 2-commit witness stamp (`0e73e1d84b41af22cbe0a7adb5792bfd6ad829c7` -> `f1e0c5f0a53084f645586bcab55a711f50415015`, `scriptHash=6f730a2d7a28822fd4184de185390b3fa00ae1e8c3c649430e85284ae55ef0da`) in PR `litlfred/qou#8430` (`status: in-progress`).
