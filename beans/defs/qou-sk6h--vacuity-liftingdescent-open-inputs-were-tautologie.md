---
# qou-sk6h
title: 'VACUITY: LiftingDescent ''open inputs'' were tautologies — RESOLVED'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T11:24:08Z
updated_at: 2026-10-04T15:25:26Z
---


## Finding

Nine declarations across three `QOU/LiftingDescent/tm_*.lean` files were
*defined* so that the files' own "open input" theorems collapsed to tautologies:

```lean
def descendedBlowupCount : ℕ := 0     -- ⇒ ∏ over Finset.range 0 is the empty product
def descendedMIdisc (i : ℕ) : ℝ := 1  -- ⇒ "disc contribution is trivial" is rfl
def descendedMI : ℝ := unknotHolonomy
def descendedMIcore : ℝ := unknotHolonomy   -- ⇒ the Stokes clause is rfl
def transientBlowupCount : ℕ := 0
def transientMItotal : ℝ := 0         -- ⇒ additivity is 0 = 0
def MI (i : ℕ) : ℝ := ∫ t in (0:ℝ)..(z i), lnq (1+t)/t  -- ⇒ chart evaluation is rfl
```

Six theorems whose docstrings read "**Open input** … body is `sorry`" contained
no `sorry` and asserted nothing; the three headline lemmas then "derived" their
conclusions from them.

## Resolution

Primitives made `opaque`; the six open inputs stated honestly with `sorry` plus
the citations they already carried ([yekutieli2015], [faddeev_kashaev1994],
[manuscript]). The three headline lemmas keep real proofs and are NOT sorried —
they now genuinely compose the open inputs, which is what their docstrings
always claimed ("*Derived* (not assumed)").

`phi_q_integral_representation` deliberately stays `rfl`: `Phi_q` really is
defined as that integral and its docstring says the representation is
definitional. That one was always honest.

Verified lean-direct: all three files exit 0; 6 sorries, each cited.

## Why it survived — the generalisable part

`#print axioms` on the three headline lemmas:

    before  [propext, Classical.choice, Quot.sound]            ← reads as fully proved
    after   [propext, sorryAx, Classical.choice, Quot.sound]   ← honestly open

**A vacuous proof is invisible to the axiom audit**: no `sorry`, no `axiom`, no
`native_decide`, so no existing detector fires — the same blind spot AGENTS.md
§3b-tax records for empty Prop carriers. Note also the direction of the trap:
the *docstrings were honest the whole time* while the code was not.

Suggested follow-up (not done here): add a *definition-collapsed* detector to
`lean-vacuity-axiom-audit.ts` — a theorem proved by `rfl`/`simp` whose statement
mentions a `def` in the same file that renders it definitionally true. That is
mechanically checkable and is exactly this shape.

## Context

Found while running the first-ever full from-source build of the QOU library
(1606 modules, 1461 green, 141 real failures). Pre-existing — but the
namespace-drift sweep's compile fixes had just turned these files green at
sorry=0, which *overstated* their soundness and removed the only outward signal.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: title says RESOLVED; dup-of qou-nkfq subject
