---
# qou-5w0u
title: 'B2: relate QBridgeSystem to the abstract BridgeSystem, or state why there is no map'
status: completed
type: task
priority: normal
created_at: 2026-09-07T06:35:11Z
updated_at: 2026-09-07T07:16:01Z
---

**COMPLETED as ALREADY-DONE (2026-09-07). The map exists and is formalized; I opened this bean without reading past line 120 of the file whose header names it.**

`QOU/Mathlib/QAlienBridgeEquation.lean` is 594 lines, not the ~120 I read. It
already carries the relation, and more than the relation:

- `euler_weight_additive_qweight_multiplicative` (line 257) — on the SAME family
  `Delta_n := t^n * E` over the SAME grading, the classical weight is `n`
  (additive) and the q-weight is `c^n` (multiplicative). The two are not rival
  conventions: the multiplicative weight is the multiplicative character
  `c^(-)` evaluated on the additive one, and the grading is the invariant.
- `polyQEuler_weights` (line 344) — the SAME theorem instantiated concretely on
  `R[X]` with the genuine dilation `X -> cX` and Euler operator `X d/dX`, so
  both hypotheses hold simultaneously and the theorem is not vacuous. The file
  says so in its own docstring; the anti-vacuity worry was already handled.
- `unipotentSystem` / `polyUnipotentSystem` — a genuinely MIXED (non-semisimple)
  model off the q-logarithm relation `sigma t = t + 1`, so the `unipotent` field
  is not decorative either.

**There is no functor `QBridgeSystem -> BridgeSystem` and there should not be**:
the two conjugate by different kinds of object (an automorphism vs a
derivation), which is a type-level fact, not a theorem to prove. The header
argues the dichotomy is forced. Nothing to state.

**Correction owed on my own Brick-0 report.** I reported `QBridgeSystem` as
"never instantiated". That is FALSE. It is instantiated four times inside its
own file (lines 220, 329, 370, 437). What I measured was cross-file IMPORTERS,
which is 2 (`C1NewtonRamification`, `C1FuchsianExponents`, both in prose
references). "Zero importers" and "never instantiated" are different claims and
I reported the second having measured the first.
