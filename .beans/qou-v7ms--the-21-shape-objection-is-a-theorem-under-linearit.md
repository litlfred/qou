---
# qou-v7ms
title: 'The (2,1) shape objection is a theorem under linearity: trace-factoring functionals at one partition are 1-dimensional'
status: done
type: task
created_at: 2026-09-05T18:25:55Z
updated_at: 2026-09-05T18:25:55Z
---


Follows `qou-kp2z`, which retired the `opaque wedderburnEmbed` and found that of
`qou-qb7p`'s three reasons the `(2,1)` clause could not be discharged, two were
retired by construction and the **shape** objection survived: the embedding
assembles blocks into one matrix, while the clause needs one block's scalar
`C_{(2,1)}` split into three coefficients (volume, surface, Coulomb).

## Why this was prose and not a theorem

`qbeta_wedderburn_bridge_probe.py` said so explicitly, under a heading reading
"WHY NO LEAN THEOREM ACCOMPANIES THIS": the tempting statement — *three
independent coefficients cannot come from one scalar* — is **false as stated**,
because a single real encodes three set-theoretically. Rescuing it needs a
hypothesis, and the probe's own judgement was that manufacturing one would be
the same overreach it exists to document. That judgement was right.

## The hypothesis did not have to be manufactured

**Linearity.** This corpus already commits to it for the Markov trace —
`markovTrace_add`, `markovTrace_smul`, `markovTrace_linear` in `Common.lean`.
Under it the statement is true, and `QOU/HeckeAlgebra/WedderburnTrace.lean` now
proves it:

| declaration | content |
|---|---|
| `traceFunctional` | a functional of the form `Σ_λ c_λ · trace (x λ)` |
| `traceFunctional_injective` | distinct coefficient families give distinct functionals |
| `traceFunctional_supported_apply` | one supported at a single `λ` **is** `c_λ · trace (x λ)` — one coefficient against one number |
| `three_supported_traceFunctionals_dependent` | any three such are linearly dependent, **explicit witness**, not an existence argument |
| `markovTraceOnWedderburn_eq_traceFunctional` | the Markov trace is one of these, with `c = y_·(q₀)` — so the no-go bites the actual object, not an abstract family |

All five: `[propext, Classical.choice, Quot.sound]`.

## What it settles, and what it deliberately does not

It does **not** show the `(2,1)` clause is false. The claim may well be true.
It rules out **one route** — the route the clause itself names — whenever that
route is linear, factors through the Markov trace, and is localised at `(2,1)`.
Three independent coefficients need more than one dimension; the trace supplies
one.

**Where the room is, which is the more useful half.** `f^{(2,1)} = 2`, so the
block is `M₂(ℝ)` — **four** real dimensions, of which the trace reads one. The
information the clause wants is present in the block and destroyed by taking its
trace. A derivation that reads the block rather than its trace is not blocked by
anything here, and that is the direction a future attempt should take.

This is recorded as a constraint on the shape of a derivation, never as a
criterion to search on.

## Surfaces updated

The reader-facing block `unified-iterative-correction-proof.md` (it must not read
as the clause being refuted), and the probe — whose "no Lean theorem" section is
replaced by the theorem, with two new assertions pinning both the no-go and the
statement of where the room is. Probe 11/11.

## Follow-up landed in the same arc: the room is a theorem too

The first pass asserted that the wanted information "is present in the block and
destroyed by taking its trace". That was prose. It is now proved:

- `blockAt` — the decomposition carrying one matrix on block `lam`, zero elsewhere.
- `trace_does_not_separate` — whenever `2 ≤ f^λ` there are **distinct**
  decompositions with *every* block trace equal. Witness: an off-diagonal matrix
  unit, which is traceless.
- `exists_indistinguishable_by_every_traceFunctional` — hence every
  trace-factoring functional, `markovTraceOnWedderburn` included, takes the same
  value on both.

So the trace is not merely one-dimensional per partition; it is genuinely lossy,
and the lost directions are exactly where a block-reading derivation would live.
All three: `[propext, Classical.choice, Quot.sound]`.

**Gap flagged, not papered over.** Instantiating this at `λ = (2,1) ⊢ 3` needs
`2 ≤ f^{(2,1)}`. That value is 2 by the hook length formula, but **no
declaration in this corpus computes `seminormalDim` at a named partition** — a
grep returns nothing. The theorem therefore carries the bound as a hypothesis,
and the `(2,1)` reading is conditional on a classical fact this corpus has not
written down. Small and self-contained; deliberately not attempted here rather
than assumed.

## Gap closed 2026-09-05: `seminormalDim` at named partitions

The two sections above both flagged the same hole — the `(2,1)` reading of their
theorems rested on `f^{(2,1)} = 2`, classical but **not** a fact this corpus had
in Lean. `QOU/HeckeAlgebra/SeminormalDimSmall.lean` closes it.

**Why it needed a route, not a `decide`.** `seminormalDim` unfolds to
`numStandardYoungTableaux (partitionShape ·)` — a `Nat.card` over a structure of
tableaux; nothing reduces. The computable route is the Frame–Robinson–Thrall
hook-length formula: `QOU.Mathlib.dimSYT_eq_dimHLF` proves **pointwise** that
`dimSYT p = dimHLF (p.parts.sort (· ≥ ·))`, and `dimHLF l = (sz l)! / prodHooks l`
is ordinary arithmetic on a list. Measured before relying on it:
`dimSYT_eq_dimHLF` is `[propext, Classical.choice, Quot.sound]`.

**One obstacle after that.** `Multiset.sort` is a `Quot.liftOn`, so `decide` gets
stuck on `p.parts.sort (· ≥ ·)` even for a literal partition. `sort_eq_list`
routes around it: a sorted list is determined by its multiset, so the sort is
pinned by uniqueness of sorted permutations rather than by evaluation. That lemma
is `[propext, Quot.sound]` — it does not even need `Classical.choice`.

| λ | `f^λ` | why |
|---|---|---|
| `(2,1) ⊢ 3` | 2 | the clause's partition |
| `(2,2) ⊢ 4` | 2 | the Wigner shape — the `n = 4` isospin menu singleton |
| `(1,1) ⊢ 2` | 1 | the charge shape |

`trace_does_not_separate_p21` and `indistinguishable_p21` now hold
**unconditionally**. All eight declarations: `[propext, Classical.choice,
Quot.sound]`.

**The boundary is recorded as a theorem, not left implicit.**
`not_two_le_seminormalDim_p11` proves `¬ (2 ≤ f^{(1,1)})`. At the charge shape the
block is `M₁(ℝ)`, the trace loses nothing, and every result in this bean says
**nothing** there. That limit is easy to forget once the `(2,1)` instances read
unconditionally, so it is stated rather than assumed.

The general theorems keep the bound as a hypothesis, which is the right shape —
they are about any block of dimension ≥ 2, and `(2,1)` is one instance.

Surfaces updated: the `WedderburnTrace.lean` docstring and the reader-facing
block, both of which said the value was not formalised; and the probe, with two
new assertions pinning the dimension fact and the boundary case. Probe 14/14.

## The constructive complement (2026-09-06)

`three_supported_traceFunctionals_dependent` says any three **trace-factoring**
functionals at one partition are dependent. `three_blockEntry_independent_p21` is
the other half: read the block instead of its trace and three independent
functionals exist at `(2,1)`, exhibited explicitly and witnessed by matrix units.

Together the pair is sharp rather than merely discouraging — it says precisely
where a derivation of the `(2,1)` clause has to live: **not** in the Markov trace,
which is one-dimensional there, but in the `f^{(2,1)} = 2`-dimensional block, of
which the trace reads one dimension.

**What it does not say, and this is the whole point.** It does *not* identify
those three functionals with volume, surface and Coulomb. It is an existence
statement about linear algebra. Three independent functionals existing is a
**necessary** condition for such a match, not evidence of one — and the count
agreeing with the count of SEMF terms is a target to check a future derivation
against, never a criterion to search on. That sentence is in the module, the
block and the probe, because it is exactly the inference this result invites and
should not support.

Both new declarations: `[propext, Classical.choice, Quot.sound]`. Probe 15/15.
