---
# qou-9iwt
title: Omega_q denotes at least 3 different objects — one is a topological space
status: todo
type: bug
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-31T07:29:49Z
updated_at: 2026-10-04T15:10:44Z
parent: qou-lv2z
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

## Re-measured 2026-09-04 — the headline is RESOLVED; two other readings are not

**The disposition this bean recommends has been carried out.** The notation
register now rules on `Ω_q` explicitly
([`notation-collisions.md`](../content/quantum-observable-universe/notation/notation-collisions.md)):

> **$\Omega_q$** = the **Reeb period** only. … the $q$-deformed **Kerov
> limit-shape space** — the target of the Plancherel pushforwards $\iota_n$ —
> is $\mathcal{K}_q$ (calligraphic, per the space convention; **was written
> $\Omega_q$ before, colliding with the period**). A topological space is not a
> period; do not carry $6 \mid \Omega_q$ to $\mathcal{K}_q$ or to the surreal.

So reading **(2)**, the topological space, was renamed — and the register even
records the history. Measured: `observations/q-plancherel-asymptotic-skeleton.md`,
the file this bean cites for that reading, now contains **0** occurrences of
`Omega_q`. Readings **(1)** integer period and **(3)** infinite surreal are
adjudicated as *"the same period lifted, not a collision"*, with the scope caveat
(`6 ∣ Ω_q` is integer-regime only) stated in the register itself.

### But the surface is LARGER than this bean recorded, and two readings survive

This bean enumerates ~8 files. Measured on `main`: **22 files** carry `Omega_q`.
Two of them use it for objects the register does not claim.

**A. `Ω_q(ϱ)` — the $q$-holonomy residue — is a FOURTH object, undocumented.**
`q-local-system.md` defines

    L_q(ϱ) = id + (q − 1)·Ω_q(ϱ),   Ω_q(ϱ) ∈ End(τ(L_q))

an **endomorphism**, a function of a loop — not the integer period, not the
surreal, not the space, not the differential. `q-gl-kummer-filtration.md` uses it
too. The register contains **zero** occurrences of the word "monodromy", so this
reading was never adjudicated.

*Claimed rather than renamed*, because it already follows the register's own
disambiguation pattern: it is never written without its loop argument, exactly as
$\zeta(s)$ and $H_q(\lambda)$ are. The register entry now says so, and says the
`6 ∣ Ω_q` divisibility does not reach it either.

**B. `q-oper.md:16` writes the differential TWO WAYS ON ONE LINE.** The
transversality condition uses $\Omega^1_q$ — the register's superscripted
spelling — and eight words later the same canonical-bundle object appears as
$H^0(X, \Omega_q^{\otimes 2})$, a **bare** $\Omega_q$ with a tensor power, which
under the register's own ruling reads as a power of the *period*. Corrected to
$(\Omega^1_q)^{\otimes 2}$, and the register now states that tensor powers keep
the superscript.

### The fourth site this bean flagged is fine as recorded

`explicit-formula.md:25`'s `Ω_q = 1/2π` remains the deliberate counterexample
datum, and line 8 of the same file says *"$\Omega_q$ is the Reeb period"* —
consistent with the register.

### Note on the render battery

Checking the edit, my own delimiter check reported `\left 3 / \right 0` on the
register. All three are `\leftrightarrow`: `\left` is a *prefix* of it. That is
the same prefix trap AGENTS.md documents for `\begin{align` vs
`\begin{aligned}` — reproduced inside a checker written to enforce that very
rule. Both files pass the battery once it is read correctly.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
