---
# qou-phl4
title: 'PROVE(lean): YoungTableauStandard.lean — 3 cited sorries [cited sagan2001]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - repo-infra
    - cite-sagan2001
created_at: 2026-08-01T23:31:03Z
updated_at: 2026-08-31T02:57:36Z
parent: qou-k1mq
---

**File:** `QOU/BraidKnot/YoungTableauStandard.lean` (QOU)  ·  3 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidKnot/YoungTableauStandard.lean

### `branching_two_one`  —  line 121  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem branching_two_one (k : ℕ) (hk : 3 ≤ k) : 3 * (∑ p : Nat.Partition k, dimSYT p * fDimSkew (partitionShape p) mu21) = Nat.factorial k `
- **Cited:** `[sagan2001]`
  - [sagan2001] Sagan (2001), *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* — (no DOI/URL)
- **Tractability:** Branching identity 3·Σ_p dimSYT·fDimSkew = k!; combinatorial, repo SYT infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `skew_le_straight`  —  line 129  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem skew_le_straight (k : ℕ) : (∑ p : Nat.Partition k, fDimSkew (partitionShape p) mu21) ≤ (∑ p : Nat.Partition k, dimSYT p) `
- **Cited:** `[sagan2001]`, `[sagan2001]`
  - [sagan2001] Sagan (2001), *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* — (no DOI/URL)
- **Tractability:** Skew ≤ straight dimension inequality; combinatorial, repo SYT infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `sum_dimSYT_eq_involution`  —  line 136  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem sum_dimSYT_eq_involution (k : ℕ) : (∑ p : Nat.Partition k, dimSYT p) = involutionNumber k `
- **Cited:** `[sagan2001]`, `[sagan2001]`
  - [sagan2001] Sagan (2001), *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* — (no DOI/URL)
- **Tractability:** Σ_λ f^λ = involution number; RSK-corollary, Mathlib lacks the RSK correspondence.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.


## UPDATE 2026-08-30 (PR #6164) — `sum_dimSYT_eq_involution` is PROVED; this bean stays OPEN

`QOU.Mass.sum_dimSYT_eq_involution_keystone` proves that entry's exact statement, sorry-free
(QOU/Mass/SumSYTEqInvolution.lean). Its "Next step" above -- "Infra-blocked: needs Mathlib
theory that does not exist" -- was WRONG: the identity does not need RSK at all. Young's
lattice is a 1-differential poset, and that route proves it with finite combinatorics on
YoungDiagram. See bean qou-m3xr for the full chain and the lesson.

This bean tracks THREE entries and is NOT closed by that: `branching_two_one` and
`skew_le_straight`'s sibling entry are untouched. Also note the header framing here is stale
in a second way -- these were re-carried as `RSKIdentitiesContext` class fields, so they are
not `sorry`s and `#print axioms` on their consumers was already clean.


## ALL THREE ENTRIES ACCOUNTED FOR, 2026-08-31 — and the tiers were the informative part

* `sum_dimSYT_eq_involution` (tier **B**, infra-blocked) — **PROVED** (#6164/#6249), needing no
  RSK. The tier was wrong.
* `skew_le_straight` (tier **P**, repo-infra-dependent) — **PROVED unconditionally**, and has
  been for some time: `YoungTableauStandard.lean:587`, a four-line `Finset.sum_le_sum` split on
  the containment guard. No class, no sorry. The tier was RIGHT and the work got done.
* `branching_two_one` (tier **P**, repo-infra-dependent) — still open, but with a checked
  non-RSK route (bean `qou-b21r`). Tier RIGHT again.

**The cataloguer assigned tiers PER ENTRY and only the tier-B entries got the "Track upstream"
verdict.** That is the sharper statement of the defect: the failure is not that every item was
lumped together, it is that some genuinely in-repo items were **mis-tiered into B**, and B
carries advice ("track upstream") that is actively wrong for in-repo work.

Worked contrast, in this one file: `skew_le_straight` (P) is proved; `sum_dimSYT_eq_involution`
(B) sat, and turned out to need nothing upstream at all. Same file, same session, same author.
The tier decided the advice, and the advice decided whether anyone tried.

`qou-fj8u` (the hook-length formula) is the same mis-tiering: tier B, but the corpus has
`YoungDiagram`, `StandardYoungTableau`, branching and `upSum_eq` — it is tier-P work.

This bean stays OPEN on `branching_two_one` alone.
