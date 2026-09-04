---
# 08a2
title: 'EPIC: keystone de-abstraction — hard Mathlib-gap infra (tiered)'
status: in-progress
type: epic
priority: normal
tags:
    - keystone-infra
    - lean
created_at: 2026-06-25T17:06:53Z
updated_at: 2026-09-03T04:04:20Z
---

Make the still-abstracted keystone §3b classes (post #2791/#2797) genuinely faithful. Corpus-grep (2026-06-25) found QOU already has substantial Lean infra (IwahoriHecke/*, MathlibExt/Q*, BraidKnot/Cl3Zeta5OrbitSum, BringTrilog*, BraidLinkTypes, ζ5/Goncharov), so most work is WIRING keystones to existing infra; only geometric-Langlands / motivic-Galois / Jones-polynomial are genuinely research-grade. Cached Mathlib: YoungDiagram, PresentedGroup, RootsOfUnity+IsPrimitiveRoot, Complex.Circle, Nat.Choose.



---
**Tier-1 delivered — #3580** (`YoungTableauStandard.lean`, lean-direct EXIT=0, 2026-07-11): defined the `StandardYoungTableau`/`SkewStandardYoungTableau` types Mathlib lacks + `fDim`/`fDimSkew` counts; `entry_lt_card` + `involutionNumber_pos` + `c8_superexp` corollary genuinely proved. Keystone C8 super-exp lower bound now unconditional modulo exactly 3 cited RSK sorries (branching Σf^λ f^{λ/(2,1)}=k!/3; skew↪straight; Σf^λ=I(k)) — the shared Tier-2 fill also needed by Identity I. Same infra unblocks bean wsxl (#3574).


---

**Tier-2 measured 2026-09-03 — the paragraph above is stale in two different ways, and the second is a category error, not a status lag.**

Measured on `origin/main`, `content/quantum-observable-universe/lean/QOU/BraidKnot/YoungTableauStandard.lean`:

| the claim above | measured |
|---|---|
| "unconditional modulo exactly **3 cited RSK sorries**" | **zero `sorry` terms in the file.** `grep -n sorry` returns 12 lines; every one is prose — the word inside backticks in a docstring, or the compound "sorry-free". Verified by re-grepping with backticked matches excluded: the sole survivor is line 535, "sorry-free". |
| `Σ_{λ⊢k} f^λ = I(k)` open | **proved unconditionally**, `:612`, body `QOU.Mass.sum_dimSYT_eq_involution_keystone k`. Closed 2026-08-30. Its own docstring records that "requires massive infrastructure (the RSK correspondence)" was a **mis-diagnosis**: Young's lattice is a 1-differential poset, and that route needs no insertion, no bumping, no permutation↔tableau-pair bijection. |
| skew ↪ straight open | **proved unconditionally**, `:587`, by the explicit extension `straightOfSkew` — fill `(2,1)` with `κ = 1,2,3`, shift each skew value into `{4, …, n}`. Elementary once the injection is written down; no Jacobi–Trudi, no RSK. |
| branching `Σ_{λ⊢k} f^λ f^{λ/(2,1)} = k!/3` open | **still open on main.** `RSKIdentitiesContext` (`:546`) now carries exactly this **one** field; `branching_two_one` (`:572`) is `[ctx]`-conditional with body `ctx.branching_two_one k hk`; no instance exists anywhere on main. |

**Why "3 sorries" is the wrong shape, not merely the wrong number.** These gaps were never sorries, and the distinction is load-bearing for anyone reading `#print axioms`. A `sorry` puts `sorryAx` in the **term**, so the axiom print is dirty and the declaration advertises its own gap. An `RSKIdentitiesContext` field puts the gap in the **signature**: `#print axioms branching_two_one` comes back *clean*, and the honesty lives entirely in the fact that no instance can be found. Reading class fields as sorries invites the opposite error — taking a clean axiom print as evidence a result is unconditional. The file's own docstring at `:563` now says this explicitly; this epic body predates it.

**Status of the one remaining field.** Proved, unconditionally and without RSK, on `claude/skew-branching-bijection-2026-08-31` (PR #6363, pending merge): `SkewSYTBranchingBijection.lean` (the skew branching rule, via the erase-max bijection) → `SkewBranchingSum.lean` (the general sum, by one-step induction on `k`, collapsing with `upSum_eq` after reindexing the pairs through `rankExchange`) → `SkewBranchingTwoOne.lean` (`μ = (2,1)`, `f^{(2,1)} = 2`, and the instance). That makes **three consecutive** "Mathlib lacks X, therefore blocked" verdicts in this arc that turned out to be mis-diagnoses rather than infrastructure facts.

So the Tier-2 fill this epic scopes is **complete pending that merge**, and `wsxl` (#3574) is unblocked — marked completed on the same branch.
