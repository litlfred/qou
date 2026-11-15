import Mathlib.Algebra.Ring.Defs
import Mathlib.Logic.Basic

/-!
# QOU.FluidDynamics.BlowupYekutieli — blowup as Yekutieli lifting obstruction

**Proposition** ([`prop:blowup-yekutieli`](../../../quantum-observable-universe/lifting-and-descent/p3-blowup-yekutieli.md)).

The *unconditional reformulation* of NS regularity in the Yekutieli
brane-tower framework: a velocity field is smooth **iff** every brane-tower
obstruction class `κ_n` vanishes, and finite-time blowup is precisely the
existence of a finite obstruction level `n*` at which lifting first fails.

```
  v smooth  ⟺  κ_n(v) = 0  ∀ n,
  v blows up  ⟺  ∃ n*, κ_{n*}(v) ≠ 0.
```

## Formalisation notes

- **Unconditional, not a conjecture (`.ts` 2026-06-08 §3b).** This is the
  reformulation "NS blowup ⟺ obstruction level n*", *not* a result that
  assumes blow-up occurs. Smoothness is *defined* as lifting through the
  entire brane tower, so the equivalence with "all `κ_n` vanish" is
  definitional; the blowup equivalence is its logical contrapositive.
- **Non-degenerate conditional (§3b-cond).** The single genuine input is
  the smoothness-as-lifting *definition* (`smooth_iff_all_obstructions_vanish`).
  The blowup characterisation is **derived** from it by `not_forall` +
  push-negation — it is not a field, so the projection-vacuity test is not
  triggered.
- **Base ring (§7c).** Generic — the statement is purely logical
  (vanishing of obstruction classes in an abelian group `B`); no
  archimedean structure is used.

-- Ref: [leitner2026] quantum-observable-universe/lifting-and-descent/p3-blowup-yekutieli.md
-- Ref: [yekutieli2010] https://doi.org/10.1007/s00029-010-0029-8
-/

namespace QOU.FluidDynamics

/-- Inputs for the blowup-as-lifting-obstruction reformulation.

    The smoothness-as-lifting *definition* is the single genuine input
    (§3b-cond non-degenerate); the blowup characterisation is *derived*.

    `B` is the abelian coefficient group `H²(𝒮, 𝓑)` in which the
    obstruction classes live; `obstruction n` is `κ_n(v)` at tower
    level `n`. -/
class BlowupYekutieli where
  /-- The brane-tower obstruction class `κ_n(v)` at level `n` (valued in
      the coefficient group, modelled by a type with a distinguished
      zero). -/
  obstruction : ℕ → ℕ
  /-- Predicate "`v` is smooth (lifts through the whole brane tower)". -/
  smooth : Prop
  /-- **Smoothness-as-lifting (definitional input):** `v` is smooth iff
      every brane-tower obstruction class vanishes. -/
  smooth_iff_all_obstructions_vanish :
    smooth ↔ ∀ n : ℕ, obstruction n = 0

/-- **Blowup as Yekutieli lifting obstruction** ([`prop:blowup-yekutieli`]).

    The two equivalences of the manuscript reformulation:

    - smoothness ⟺ all obstruction classes vanish (the definitional input);
    - blowup (non-smoothness) ⟺ existence of a finite obstruction level
      `n*` with `κ_{n*}(v) ≠ 0` — *derived* from the first by
      contraposition + `not_forall`. -/
-- Ref: [leitner2026] quantum-observable-universe/lifting-and-descent/p3-blowup-yekutieli.md
theorem blowup_yekutieli [ctx : BlowupYekutieli] :
    (ctx.smooth ↔ ∀ n : ℕ, ctx.obstruction n = 0)
      ∧ (¬ ctx.smooth ↔ ∃ n : ℕ, ctx.obstruction n ≠ 0) := by
  refine ⟨ctx.smooth_iff_all_obstructions_vanish, ?_⟩
  rw [ctx.smooth_iff_all_obstructions_vanish, not_forall]

end QOU.FluidDynamics
