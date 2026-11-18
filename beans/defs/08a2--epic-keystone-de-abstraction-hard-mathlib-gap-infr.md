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
updated_at: 2026-11-18T11:12:15Z
parent: qou-rtxm
---

Make the still-abstracted keystone §3b classes (post #2791/#2797) genuinely faithful. Corpus-grep (2026-06-25) found QOU already has substantial Lean infra (IwahoriHecke/*, MathlibExt/Q*, BraidKnot/Cl3Zeta5OrbitSum, BringTrilog*, BraidLinkTypes, ζ5/Goncharov), so most work is WIRING keystones to existing infra; only geometric-Langlands / motivic-Galois / Jones-polynomial are genuinely research-grade. Cached Mathlib: YoungDiagram, PresentedGroup, RootsOfUnity+IsPrimitiveRoot, Complex.Circle, Nat.Choose.



---
**Tier-1 delivered — #3580** (`YoungTableauStandard.lean`, lean-direct EXIT=0, 2026-07-11): defined the `StandardYoungTableau`/`SkewStandardYoungTableau` types Mathlib lacks + `fDim`/`fDimSkew` counts; `entry_lt_card` + `involutionNumber_pos` + `c8_superexp` corollary genuinely proved. Keystone C8 super-exp lower bound now unconditional modulo exactly 3 cited RSK sorries (branching Σf^λ f^{λ/(2,1)}=k!/3; skew↪straight; Σf^λ=I(k)) — the shared Tier-2 fill also needed by Identity I. Same infra unblocks bean wsxl (#3574).


---

**Tier-2 measured 2026-09-03 — the paragraph above is stale in two different ways, and the second is a category error, not a status lag.**

Measured on `origin/main`, `folio/quantum-observable-universe/lean/QOU/BraidKnot/YoungTableauStandard.lean`:

| the claim above | measured |
|---|---|
| "unconditional modulo exactly **3 cited RSK sorries**" | **zero `sorry` terms in the file.** `grep -n sorry` returns 12 lines; every one is prose — the word inside backticks in a docstring, or the compound "sorry-free". Verified by re-grepping with backticked matches excluded: the sole survivor is line 535, "sorry-free". |
| `Σ_{λ⊢k} f^λ = I(k)` open | **proved unconditionally**, `:612`, body `QOU.Mass.sum_dimSYT_eq_involution_keystone k`. Closed 2026-08-30. Its own docstring records that "requires massive infrastructure (the RSK correspondence)" was a **mis-diagnosis**: Young's lattice is a 1-differential poset, and that route needs no insertion, no bumping, no permutation↔tableau-pair bijection. |
| skew ↪ straight open | **proved unconditionally**, `:587`, by the explicit extension `straightOfSkew` — fill `(2,1)` with `κ = 1,2,3`, shift each skew value into `{4, …, n}`. Elementary once the injection is written down; no Jacobi–Trudi, no RSK. |
| branching `Σ_{λ⊢k} f^λ f^{λ/(2,1)} = k!/3` open | **still open on main.** `RSKIdentitiesContext` (`:546`) now carries exactly this **one** field; `branching_two_one` (`:572`) is `[ctx]`-conditional with body `ctx.branching_two_one k hk`; no instance exists anywhere on main. |

**Why "3 sorries" is the wrong shape, not merely the wrong number.** These gaps were never sorries, and the distinction is load-bearing for anyone reading `#print axioms`. A `sorry` puts `sorryAx` in the **term**, so the axiom print is dirty and the declaration advertises its own gap. An `RSKIdentitiesContext` field puts the gap in the **signature**: `#print axioms branching_two_one` comes back *clean*, and the honesty lives entirely in the fact that no instance can be found. Reading class fields as sorries invites the opposite error — taking a clean axiom print as evidence a result is unconditional. The file's own docstring at `:563` now says this explicitly; this epic body predates it.

**Status of the one remaining field.** Proved, unconditionally and without RSK, on `claude/skew-branching-bijection-2026-08-31` (PR #6363, pending merge): `SkewSYTBranchingBijection.lean` (the skew branching rule, via the erase-max bijection) → `SkewBranchingSum.lean` (the general sum, by one-step induction on `k`, collapsing with `upSum_eq` after reindexing the pairs through `rankExchange`) → `SkewBranchingTwoOne.lean` (`μ = (2,1)`, `f^{(2,1)} = 2`, and the instance). That makes **three consecutive** "Mathlib lacks X, therefore blocked" verdicts in this arc that turned out to be mis-diagnoses rather than infrastructure facts.

So the Tier-2 fill this epic scopes is **complete pending that merge**, and `wsxl` (#3574) is unblocked — marked completed on the same branch.


## 2026-09-04 — Tier-2 VERIFIED complete; PR #6363 merged

The body above ends *"complete pending that merge"*. **The merge landed.** All three
files are on `main`:

- `QOU/Mathlib/SkewSYTBranchingBijection.lean`
- `QOU/Mathlib/SkewBranchingSum.lean`
- `QOU/Mathlib/SkewBranchingTwoOne.lean`

and `SkewBranchingTwoOne` supplies the instance at
`QOU.BraidKnot.YoungTableauStandard.rskIdentitiesContextInstance` (:77).

**Verified by axiom audit, not by grep** — and specifically *not* by the test this
bean itself warns against. Its own note says a `[RSKIdentitiesContext]`-conditional
theorem prints clean axioms **even with no instance**, so a clean print on
`branching_two_one` proves nothing on its own. The load-bearing fact is that the
**instance exists and is itself clean**:

| declaration | `#print axioms` |
|---|---|
| `rskIdentitiesContextInstance` | `[propext, Classical.choice, Quot.sound]` |
| `branching_two_one_holds` | same |
| `branching_two_one` | same |
| `c8_superexp` | same |

`lean`-direct **exit 0**; all three files grep-clean of real `sorry` terms (the
only matches are backticked prose and the string "sorry-free").

**So `c8_superexp` is now unconditional**, and the Tier-2 fill this epic scopes is
**closed**. Left `in-progress` because the epic covers further tiers — the
genuinely research-grade items (geometric-Langlands, motivic-Galois,
Jones-polynomial) named in the header are untouched by this.



## Reorganisation 2026-10-04

Now the epic for P3.GAP under Lean / Mathlib foundations.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

- Round 79 (`lane-e667`): Formalized `qou-ix9e`, `qou-lncp`, `qou-ulfe`, `qou-znz5`, `qou-pso0` in `QOU.Foundations.MonicRewritingRuleOrientationOverlapCriticalPairResolutionFormalGroupLawDistributionConfluenceSpecializationFlatness` with 80-dps `mpmath` 2-commit witness stamp (`0e73e1d84b41af22cbe0a7adb5792bfd6ad829c7` -> `f1e0c5f0a53084f645586bcab55a711f50415015`, `scriptHash=6f730a2d7a28822fd4184de185390b3fa00ae1e8c3c649430e85284ae55ef0da`) in PR `litlfred/qou#8430` (`status: in-progress`).

- Round 81 (`lane-e667`): Formalized `rttg`, `qou-50vf`, `qou-aezg`, `qou-dcvv`, `qou-fwah` in `QOU.Foundations.FramedTangleSnakeCoherenceFourTermChordRelationSingularResolutionAlternationFiltrationProfileShiftCubePairBoundaryLift` with 80-dps `mpmath` 2-commit witness stamp (`202f38f5def66efc61fb7c2f38594348be909ef6` -> `8be6d39b672d7e4c20d56580366adaf778190be7`, `scriptHash=08594954abfff6ef5f50f03f78c3a5e07152d5280835430790282602d58a4a45`) in PR `litlfred/qou#8437` (`status: in-progress`).

- Round 82 (`lane-e667`): Formalized `qou-71ma`, `qou-n226`, `qou-oilr`, `qou-omuz`, `qou-wxmm` in `QOU.Foundations.ValuationGradeSelectionUpperHalfPlaneNonDegeneracyTwistedPairCohomologyDimensionLaurentRingUnitDivisionLinearDualityCertificate` with 80-dps `mpmath` 2-commit witness stamp (`84401456f07c58b1279d96f566c292313ce4c028` -> `0c9aa2b99fc76a7fc726e889fc36119e8f63d65c`, `scriptHash=f07174204f482f7a01972e149c17324ec39a978434a088c3f7d45077e7857c97`) in PR `litlfred/qou#8441` (`status: in-progress`).
