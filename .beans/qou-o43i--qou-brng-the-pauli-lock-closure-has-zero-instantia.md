---
# qou-o43i
title: 'qou-brng: the Pauli-lock closure has ZERO instantiation sites — its equal-scalars hypothesis is not a corpus claim a D9 witness could settle'
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T20:22:33Z
updated_at: 2026-09-05T20:23:23Z
---

Follows `qou-brng`'s 2026-09-04 entry, which named `separable_interface_degenerate`'s
equal-scalars hypothesis as *"where the residue actually is"* and set the next step as
*"a witness for D9 would make the equal-scalars question decidable for the first time."*

**Both halves need correcting, and the correction is measured rather than argued.**

## 1. The theorem has ZERO instantiation sites — measured, and now guarded

`scripts/separable-interface-instantiation-audit.py` (new; `--selftest` 5/5, `--strict`
gates) strips Lean comments — nested block comments included — and only then searches.
Over every tracked file: **1 declaration, 0 applications, 28 prose citations in 13 files**
(16 `.md`, 8 `.py` docstrings, 2 JSON, 2 Lean *docstrings*).

That matters because `fSpin : Sp → R` and `fIso : Is → R` are **arbitrary functions on
arbitrary types**. `hplus`/`hminus` are the antecedent of a statement quantified over
every possible pair of scalar assignments — not a claim about anything in this corpus.
They become a corpus claim only when the theorem is *instantiated* at the corpus's own
constructions, and nothing does that.

The `μ₊ = (z + q⁻¹)/(q + q⁻¹)`, `μ₋ = (q − z)/(q + q⁻¹)` identification lives in the
theorem's **docstring**, never in its statement. The `y₂`/`y₁₁` link is a different
section of the same file (`weight_eq_proj_scalar`, `WeightsDetermineZ`, lines 355–394),
about different variables. `qou-brng` cites `InterfaceScalar.lean:365–384` for the
identification and that citation is to a docstring-adjacent theorem, not to the one that
closes the channel — the same name-vs-content class as `markovZ`/`markovZc`.

## 2. A D9 witness cannot settle it, because D9's carrier was rebuilt around a different claim

`class IsospinFromCanonicalBowtie` was repaired on 2026-09-04 (#6671) from the
content-free `holds : Prop` to a refutable class with three fields: `0 < q`, `q ≠ 1`, and
one real equation `ratio = (1−q⁻¹)²(q−q⁻¹)(q+q⁻¹)(1+(1−q⁻¹)³)/3`. Its own header states
that the categorical half — the crystal functional and the isospin swap — is **NOT
encoded**.

So an instance of D9 supplies a real-number identity. The equal-scalars question is about
projector scalars of a swap construction. **The two objects do not touch**: a D9 witness
in the carrier's current shape decides nothing here. That is worth knowing before someone
spends a tranche building one, which is what the bean's "Next" line invites.

Note `qou-brng`'s "D9 has no witness" is still literally true — no instance exists — but
its *reasoning* was superseded the same day by the carrier's own header, which records
that a witness under the old shape would have been trivial and proved nothing.

## 3. Formalised: the closure is carried entirely by its hypotheses

Two new sorry-free library files, `lean`-direct exit 0, standard three axioms
(`degeneracy_is_commutativity` has none), split per §7c into generic and archimedean:

* `QOU/QBeta/SeparableInterfaceHypothesesHaveContent.lean` (generic —
  `CommRing`/`CommMonoid`/`Field`, no `ℝ`)
  - `separability_hypotheses_have_content` — drop `hplus`/`hminus` and the conclusion is
    **false**: `5 ≠ 6` on a two-element index type. So the closure is not a tautology.
  - `degeneracy_is_commutativity` — with the hypotheses in force the residual mathematics
    is `mul_comm`. The theorem's proof *is* `rw [hplus, hminus, mul_comm …]`. Everything
    it asserts about physics is asserted by its antecedent.
  - `asymmetry_attainable_with_distinct_scalars` — if the two SU(2)s carry different
    pairs, the channel ratio is **any** field element. Not a weakened bound; none at all.
    Scope (b) on {separable interface, distinct scalar pairs}, invariant: a field has no
    nontrivial multiplicative constraint between two free elements.
* `QOU/QBeta/SeparableInterfaceHypothesesHaveContentReal.lean` (archimedean)
  - `distinct_positive_scalars_reach_any_ratio` — the escape survives positivity, so it is
    not an artefact of admitting negative or zero weights.
  - `measured_asymmetry_attainable` — the measured **33.7055** is one of the values
    reached. What the hypothesis excludes is not a correction; it is the whole effect.

## What this does NOT say

Not a refutation of `separable_interface_degenerate`, which is correct and sorry-free.
Not a claim that the two SU(2)s carry different scalars — that stays exactly as
unestablished as its converse; this is a statement about what the Lean asserts. Nothing
about the linking-matrix result (`lk` IS `I₃`, both channels at `I₃ = 0`, achievable
asymmetry exactly 1), which is untouched and rests on its own argument. Nothing about the
sibling's pair-layer obstruction, which remains a second independent reason the fifth
closure is weak.

## Detector observation, deliberately NOT swept

`scripts/check-sidecars.sh` counts the literal `(R :=` as evidence a file declares a
generic result (`GEN` regex, line 139). AGENTS.md §7c prescribes exactly that spelling for
the archimedean sibling — *"consumes the generic result via a `(R := ℝ)` instantiation"* —
so a correctly-split file gets reported as "§7c MIXED generic + archimedean". A
specialisation is the opposite of generic evidence.

**Left alone on purpose.** My first-pass measurement of the blast radius was noisy (the
grep matched Mathlib and used `\s` under BRE), and AGENTS.md's own rule is not to launch a
sweep off a shaky number. The file here uses `@f ℝ _` instead, and says so in its
docstring rather than sidestepping silently. A proper measurement of how many library
files this misclassifies is a follow-up, not this tranche.

## Verification

`lean -DautoImplicit=false -s 65536` exit 0 on both files; `#print axioms` on all six
declarations shows only `propext`/`Classical.choice`/`Quot.sound`, and none on
`degeneracy_is_commutativity`. `scripts/check-sidecars.sh` clean on both (`generic OK` /
`ℝ justified`), authors-note Lean-coverage refreshed (738/749 provable sorry-free, 98.5%).
`precision-gates.sh --changed` is RED — **pre-existing on main, not this tranche**: zero
`computations/` files are touched here, and the witnesses the gate regenerated were
reverted per its own instruction.
