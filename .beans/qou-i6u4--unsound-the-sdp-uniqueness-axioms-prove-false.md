---
# qou-i6u4
title: 'UNSOUND: the SDP uniqueness axioms prove False'
status: completed
type: task
priority: high
created_at: 2026-09-05T19:41:40Z
updated_at: 2026-09-05T20:26:52Z
---

## Finding

Four of the five SDP axioms in `QOU/MathlibExt/` are **inconsistent** — each
one alone derives `False`, verified `lean`-direct, `#print axioms` showing no
`sorryAx` and the axiom itself as the only non-standard dependency.

| axiom | file | status |
|---|---|---|
| `strict_complementarity_unique_axiom` | `SDP.lean:286` | **proves False** |
| `slater_strict_complementarity_kernel_axiom` | `SDPRealUniqueness.lean:189` | **proves False** |
| `SDPRankUniqueness` | `SDPRealUniqueness.lean:587` | **proves False** |
| `strict_complementarity_kernel_disjoint` | `SDPRankEquality.lean:208` | **proves False** |
| `affine_slater_rigidity` | `SDPRankEquality.lean:672` | guarded by a rank equation — see below |

## The counterexample

`n = 1`, `ι = Empty`, `cost = 0`. Then every PSD matrix is feasible, `objAt` is
identically `0`, and the dual slack `S = cost - Σ = 0`. So `Φ* = 0` and
`Φ' = 1` are both feasible with equal objective, and every extra hypothesis the
axioms carry is satisfied *vacuously*:

- `dualSlack_psd`: `(0 : Matrix _ _ ℝ).PosSemidef` — holds.
- `obj_eq_dualObj`: `0 = 0` — holds.
- `_h_S_diff` / `_h_diff_S`: `0 * (Φ' - Φ*) = 0` — holds because `S = 0`.
- `_h_constraint_diff`: vacuous over `Empty`.
- `h_slater`: the identity is PosDef with no constraints — holds.

Conclusion: `1 = 0`.

## Why the extra hypotheses do not save the real layer

This is the part I got wrong on first reading and am recording so the next
agent does not repeat it. `SDPRealUniqueness` looks sound where `SDP.lean` looks
thin: its `RealStrongDualityPair` carries genuine `dualSlack_psd` /
`obj_eq_dualObj` fields where `StrongDualityPair` has `True` placeholders, and
its axioms carry `_h_S_diff` and `_h_constraint_diff` on top. I cleared it on
that structural difference.

**Structure is not soundness.** The complementarity-difference hypotheses say
`Φ' - Φ*` lies in `ker S`. When `S = 0` that kernel is everything, so the
hypotheses constrain nothing and the axiom fires unguarded.

## What the true theorem is

Alizadeh-Haeberly-Overton 1997 does not say strict complementarity implies a
unique primal optimum. It says the primal optimum is unique iff the dual is
**nondegenerate** (given strict complementarity). None of the five axioms carries
a nondegeneracy hypothesis. `affine_slater_rigidity` is the only one carrying
anything with real force — `rank Φ* + rank S = n`, which the `n = 1` example
fails (`0 + 0 ≠ 1`).

## Why two prior audits missed it

`docs/audits/2026-08-26-live-axiom-surface-recheck.md` and
`docs/audits/2026-09-03-axiom-tier-triage.md` both examined this exact
five-axiom family, eight days and two days ago. Both asked *is the citation
real* and *can Mathlib close it*; the 2026-09-03 one concluded the tier is
"blocked one level lower" on conic duality. Neither asked whether the Lean
statement **is** the cited theorem. An axiom with an impeccable citation to a
true published theorem can still be a false Lean proposition, and nothing in the
axiom-triage tradition here tests for that.

## Blast radius

No false *consequence* has landed. The live consumers all instantiate
`cost = 1` (identity), not `cost = 0`:

- `nucleusEmptySDP` (`NucleusEmptySDPUniqueness.lean`) has `cost := 1`, so its
  objective is `trace Φ` and its uniqueness claim (PSD + zero trace ⟹ zero) is
  **true**; only the route through the axiom is rotten, and that file already
  carries a sorry-free alternative (`nucleus_uniqueness_closed`).
- `CanonicalKnotIdSDPUniqueness.lean:124,135` consume
  `strict_complementarity_unique` / `_optimum_subsingleton` generically.

So this is a false axiom with, so far, only true consequences drawn from it.
That is luck, not design.


## RESOLVED — all five refuted, deleted, and rerouted (PR #6882)

`affine_slater_rigidity` fell too, to a second counterexample. Its rank guard
`rank Φ⋆ + rank S = n` is real — the `n = 1` example fails it (`0 + 0 ≠ 1`) —
but insufficient: `n = 2`, no constraints, `cost = diag(1,0)`, `Φ⋆ = diag(0,1)`,
`D = diag(0,1)` **satisfies** it (`1 + 1 = 2`) with `S · D = 0` and `D ≠ 0`.

Two derived theorems were false as well: `rank_equality_under_strict_complementarity`
and the `real_strict_complementarity_unique` pair.

### Delivered

- **`QOU/MathlibExt/SDPUniquenessCounterexamples.lean`** — proves the five
  **negations** directly, not `False` from the axioms, so it survives their
  deletion and blocks the statements from returning. `#print axioms` on all
  five: `[propext, Classical.choice, Quot.sound]`.
- All five axioms **deleted**, each leaving a section comment naming its
  counterexample theorem and concrete instance.
- The uninhabitable `class SlaterStrictComplementarityKernel` deleted — its
  single field *was* the false proposition.
- Every consumer rerouted onto the proven interior case (`dualSlack` PosDef).
  `nucleusTrivialStrictCompPair` was re-pointed rather than renamed, so all
  **eleven** per-nucleus files stayed untouched.
- **30/30** files importing the SDP chain `lean`-direct exit 0.

### Nothing true was lost

Every live consumer has `cost = 1` and no constraints, so its dual slack is the
identity — positive-definite — and discharges the interior hypothesis outright.
The axioms were supplying a false *unconditional default* over the top of a
correct *conditional* design: `SDPSlaterUniqueness` already had two proven,
axiom-free instances.

### The reusable lesson

The two prior audits of this exact family (2026-08-26, 2026-09-03) asked *is the
citation real* and *can Mathlib close it*. Neither asked whether the Lean
statement **is** the cited theorem. An axiom with an impeccable citation to a
true published theorem can still be a false Lean proposition — and here five
were. Worth adding to the axiom-triage method as a third question.
