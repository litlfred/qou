---
# qou-9iwt
title: Omega_q denotes at least 3 different objects — one is a topological space
status: todo
type: bug
priority: high
created_at: 2026-08-31T07:29:49Z
updated_at: 2026-08-31T07:29:50Z
---

Found while trying to run the `6 ∣ Ω_q` test that
`reeb_spectrum_pinned_by_periodicity` (bean `qou-qspc`) makes available. The
test could not be run, and the reason turned out to be more interesting than the
test.

## `Ω_q` is overloaded across at least three genuinely distinct objects

| # | where | what `Ω_q` IS |
|---|---|---|
| 1 | `quantum-observable-universes/categorical-reeb-derivation.md` + `.lean` | *"the smallest positive **integer** `Ω_q` such that `ξ_q^{Ω_q} = id_A`"*. Lean field `period : ℕ`. |
| 2 | `observations/q-plancherel-asymptotic-skeleton.md` | *"We define a topological **space** `Ω_q`"* — the target of pushforwards `ι_n : {λ ⊢ n} → Ω_q`. |
| 3 | `appendix-surreals/` — `rh-surreal-bound.md`, `collatz-surreal-bound.md`, `surreal-squeeze-interpretation.md`, `surreal-rate-calculus.md`, `p-vs-np-conjecture.md` | `Ω_q ≍ ε⁻¹` with `ε = 1/ω` the Reeb infinitesimal — an **infinite surreal**. |

**(2) is not a variant reading, it is a different kind of thing.** A topological
space is not a natural number, and no property of one transfers to the other.
(3) is equally hard: `ε⁻¹ ≍ ω` is infinite, so it is not the smallest positive
integer with `ξ^Ω = id` under any reading.

A fourth, weaker site: `q-geometric-langlands/explicit-formula.md:25` writes
`Ω_q = 1/2π`, but **in a deliberately unrelated datum used as a counterexample**
— so it is an arbitrary constant in a negative example rather than a competing
definition. Non-integer all the same.

This is the failure mode AGENTS.md names directly — *"attributes do not transfer
across overloaded symbols … distinct objects sharing a glyph is a recurring root
cause"* — and the notation register exists to catch exactly it.

## The immediate consequence, and it is mine

`reeb_spectrum_pinned_by_periodicity` yields `6 ∣ Ω` for reading **(1)** only. A
reader who carried it to the surreal `Ω_q ≍ ε⁻¹`, or to the topological space,
would be committing the category error the rule forbids. The Lean docstring has
been scoped to say so explicitly.

## And the test cannot be run at all

Measured: `CategoricalReebDerivation` has **zero instances** and there is **no
`period :=` assignment anywhere** in the tree — its 5 `.lean` occurrences are 3
in its own defining file and 2 in a docstring I wrote. So reading (1) has no
value in the corpus, and there is nothing for 6 to divide.

**I reported last turn that this was "a question with a computable answer".
That was wrong** — it is computable in principle, but the quantity it needs is
not pinned anywhere, so nothing can be computed today. Supplying a `period`
(i.e. inhabiting `CategoricalReebDerivation`) is the prerequisite, and that is
a separate piece of work.

## Suggested disposition

Rename per the notation register rather than unify: these are three objects. The
integer period and the surreal Reeb time are both legitimately "Reeb period"-ish
and need distinct glyphs; the Plancherel space is unrelated and should not be
`Ω_q` at all.
