---
# qou-7t1n
title: 'GAP: b1_hyperbolic_rows made the QOU library inconsistent (FIXED); audit the same shape elsewhere'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T17:15:19Z
updated_at: 2026-11-17T06:55:30Z
parent: qou-rtxm
---


## The library was inconsistent

`QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean` carried

```lean
axiom b1_hyperbolic_rows
    (n_hyperbolic_rows_verified : ℕ)
    (bloch_suslin van_der_veen : Prop) :
    bloch_suslin → van_der_veen → 3 ≤ n_hyperbolic_rows_verified
```

**Every binder is universally quantified, including the count.** So it
asserts `3 ≤ n` for *every* `n : ℕ`, given *any* two `Prop`s:

```lean
theorem b1_axiom_is_inconsistent : False := by
  have h : (3 : ℕ) ≤ 0 := b1_hyperbolic_rows 0 True True trivial trivial
  omega
```

Compiled, exit 0, `#print axioms` naming `b1_hyperbolic_rows` as the only
non-standard dependency. This is **not** the vacuity class — it is `False`.
Every statement in the import cone of `QOU.AppendixSurreals` was provable.

Blast radius: one importer, `QOU/AppendixSurreals.lean` (the aggregator), so
in practice everything that pulls in the AppendixSurreals module.

## Fixed (PR on branch claude/axiom-triage-batch3-2026-08-08)

Stop quantifying over what was meant to be fixed:

- `BlochSuslinRegulator`, `VanDerVeenVolumeConjecture` — named `opaque Prop`s,
  not bound `Prop` variables.
- `HyperbolicRow` — an enumerated type (`borromean | whitehead | twistKnot`)
  with `deriving Fintype`, not an anonymous numeral.
- `b1_holds_at_row` — the conjecture, per row: conditional on the two inputs,
  `B1HoldsAt r` for each `r`. This is where the content lives and it is
  falsifiable.
- `b1_hyperbolic_rows` — now a **theorem**, deriving
  `3 ≤ card {r | B1HoldsAt r}` from the per-row conjecture plus
  `Fintype.card HyperbolicRow = 3`.

Note the near-miss: defining `nVerified := 3` and keeping `3 ≤ nVerified`
would have traded unsoundness for vacuity (`3 ≤ 3` is `rfl`). The count has to
be *derived*, not named.

The exploit no longer typechecks. Verified with `scripts/lean-verify-cone.sh`:
the file and its importer exit 0.

## Detector extended — and three parsing bugs that each hid a real defect

`scripts/lean-one-sided-binder-audit.py` now reports two signals. Corpus is
clean (0 UNSOUND) after the fix; self-test 5/5 pins both real defects and both
false positives.

Getting it to catch B1 took three fixes, each worth remembering because each
one *silently* produced a confident wrong answer:

1. **Order relations.** The detector split only on `=`. A one-sided `=`
   collapses; a one-sided `≤` over an unconstrained numeric binder is
   *unsound*. Now splits on `≤ ≥ < > =`.
2. **Binder form.** It matched only `axiom f : ∀ (n : ℕ), …`. B1 used
   `axiom f (n : ℕ) : …` — binders before the colon — so the file was skipped
   outright. Both forms now handled.
3. **Name-length cap.** A `len(var) > 3` heuristic, tuned for the `z`/`q`
   collapse cases, excluded `n_hyperbolic_rows_verified` (26 chars). The cap
   now applies to the COLLAPSE signal only.

Plus a fourth, caught in review of my own output: without comment stripping,
the scanner read the *docstring* of the fixed file — which quotes the old
axiom in a ```lean fence — and re-reported it as live. Comments are stripped
before scanning.

## Follow-up

The corpus is clean for *this* shape, but the shape generalises past what the
detector covers:

- Non-relational conclusions with an unconstrained binder (`P n` for all `n`
  where only one `n` was meant).
- Conclusions behind `∃`, which the splitter does not descend into —
  `weierstrass_diff_eq_axiom` was that variant and needed a human read.
- Statements where the binder *is* constrained, but only vacuously.

More generally: **`#print axioms` is not a soundness check.** It reports which
axioms a proof depends on, not whether those axioms are jointly satisfiable.
Nothing in this repo checks the latter. A cheap partial guard would be a CI
declaration `example : False := by exact? ` — or simply attempting `False`
against each library module — but that is not currently done anywhere.

## UPDATE — three more inconsistencies, from two more files

B1 was not alone. Continuing the `qou-i6cn` read turned up **three further
axioms that each independently prove `False`**, in two files. Total for the
session: **four unsound axioms across three files.**

### `QOU/BraidKnot/LpDualityHypothesisClass.lean` — two

```lean
axiom schrijver_strong_duality : ∀ (lp : OperatorSelectionLP), lp.duality_gap = 0
axiom schrijver_complementary_slackness :
    ∀ (lp : OperatorSelectionLP) (lam : lp.Λ), lam ∈ lp.active_set ↔ lp.tight lam
```

`OperatorSelectionLP` carries `primal_obj`, `dual_obj`, `active_set` and
`tight` as **arbitrary independent fields** — no feasibility, boundedness or
optimality data at all — and `duality_gap` is *defined* as
`|primal_obj − dual_obj|`. So the first says any two reals are equal; the
second says an empty active set matches a universally-true tightness
predicate. Both refuted with a two-line witness structure.

Schrijver §7.2/§7.4 hold for a *bounded and feasible* LP *at its optimum*.
Those hypotheses were dropped, and the structure cannot even state them.

### `QOU/FlavorDressing/DressedMassFromSubstrateSplit.lean` — one

```lean
axiom dressed_mass_split_substrate_closed_form
    (F : FlavorDressingFunctor) (M_N q : ℝ) (_hM : 0 < M_N) (_hq : 1 < q) :
    F.μ Flavor.down - F.μ Flavor.up = M_N * substrate_split_factor q
```

`F`, `M_N`, `q` are mutually unrelated — nothing ties the nucleon-mass scale
to the dressing. The left side is fixed by `F`; the right varies freely with
`M_N`. The constant dressing `μ ≡ 1` makes the left side `0`, forcing
`substrate_split_factor q = 0` — and that is a *concrete* strictly-positive
expression, so it is refutable rather than merely collapsing.

**How it got there is the instructive part.** The docstring records that a
review (Gemini #696) flagged the downstream theorem as a **tautology**; the
repair was to introduce this axiom. The tautology fix over-corrected into
unsoundness: the statement stopped being empty by starting to be false. Worth
keeping in mind when draining the vacuity queue — the two failure modes are
adjacent, and the obvious fix for one is a route into the other.

## Pattern across all four

Every one has the same shape: **a cited theorem transcribed without the
hypotheses that make it true**, quantified over a structure too weak to state
those hypotheses. Not one is a mathematical error by the author — the
citations are apt and the intent is right in each case. The defect is
entirely in the Lean transcription, which is why reading the `.md` never
reveals it and why `#print axioms` stays clean downstream.

## Detector now carries three signals

`scripts/lean-one-sided-binder-audit.py`, self-test 6/6, corpus **0 UNSOUND /
0 advisory**:

- **UNSOUND** — a whole side of an order relation is a bare unconstrained
  binder (B1).
- **ADVISORY** — an unconditional claim relating projections of an arbitrary
  structure (the LP and flavour-dressing cases). Fatal iff the projected
  fields are independent, which needs a human; flagged, not auto-failed. This
  signal found the flavour-dressing one on its own after being written for
  the LP one.
- **COLLAPSE** — the original one-sided-`=` case.

## What still is not checked

`#print axioms` reports *dependency*, not *satisfiability*. Nothing in this
repo checks that the axiom set is consistent, which is exactly why four
`False`-proving axioms sat in the tree with clean-looking audits. A cheap
partial guard worth considering: a CI step that, for each library module
declaring axioms, attempts `example : False` with a small tactic battery plus
degenerate-witness construction. It would not be complete, but all four of
this session's cases fall to a two-line witness.

## 2026-11-17 — Finite Hyperbolic Row Count & Consistent LP Duality (`litlfred/qou#8237`)
- Formalized `HyperbolicRow`, `countVerifiedRows_le_three`, `three_le_countVerifiedRows_iff`, and `consistent_lp_duality_gap_iff_slack_zero` over generic `CommRingOps R` in `folio/quantum-observable-universe/lean/QOU/Foundations/BarConditionHyperbolicSphericalMetric.lean` (wired into `QOU.lean`, `0` `sorry`, `0` warnings, `0` vacuity advisories, commit `62b14488de4f16d02964a9976964f16ed12bcdcd`, PR [https://github.com/litlfred/qou/pull/8237](https://github.com/litlfred/qou/pull/8237)).
- Kept `status: in-progress` per no-unilateral-closure policy.
