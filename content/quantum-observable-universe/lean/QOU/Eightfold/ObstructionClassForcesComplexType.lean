import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# QOU.Eightfold.ObstructionClassForcesComplexType — self-duality forces a trivial obstruction

`AmphichiralHolonomyIsSelfDual` pruned route E's **geometric** leg: the holonomy of an
amphichiral knot is self-dual, hence not the complex-type object the flavour gate needs.
What survived was a *non-geometric* boundary-unipotent `PGL(3,ℂ)` representation.

Searching for one of those means decomposing a Ptolemy variety, which is expensive.  This
file replaces that search with an arithmetic obstruction, and the payoff is that a whole
**obstruction class** can be certified complex type at once, without solving anything.

## The argument

A boundary-unipotent `PGL(3,ℂ)` representation `ρ` carries an obstruction class
`σ(ρ) ∈ H²(M, ∂M; ℤ/3)`: lift each generator to `SL(3,ℂ)`, and the failure of the
relations is a 2-cocycle valued in the centre `μ₃`.

Two facts about that class are **topological inputs**, carried here as the explicit
hypotheses of `ObstructionDuality` rather than asserted:

* `obs_dual` — duality negates the class.  Lifting `ρ* = ᵗρ⁻¹` means inverse-transposing
  the lifts, and a central `ζ • 1 ↦ ζ⁻¹ • 1`, so the cocycle inverts.
* `obs_congr` — isomorphic representations have equal classes (the class is an invariant
  of `ρ` up to conjugation).

Given both, self-duality forces `σ = -σ`, so `2σ = 0`; and `2` is invertible mod `3`, so
`σ = 0`.  Contrapositive: **no representation in a non-trivial obstruction class is
self-dual.**  That is `not_selfDual_of_obs_ne_zero`, the form a search actually uses —
it reduces "exhibit a complex-type representation" to "exhibit *any* point of the Ptolemy
variety in a non-trivial class", i.e. to the ideal being proper.

## Scope

This proves an implication about any structure satisfying the two hypotheses; it does not
prove the hypotheses, which are the cited topological facts, and it says nothing about
whether such a representation exists for a given manifold.  Non-emptiness is a separate,
computational question.

Empirically consistent: for `4₁` at `n = 3`, obstruction class 0 has 6 solutions of which
4 are self-dual, while the non-trivial class has 2 solutions and **none** are self-dual.
-/

namespace QOU.Eightfold

/-- In `ZMod n` with `n = 2m+1` odd, `x + x = 0` forces `x = 0`: `2` is invertible. -/
theorem eq_zero_of_add_self_eq_zero_odd {n m : ℕ} (hn : n = 2 * m + 1)
    (x : ZMod n) (h : x + x = 0) : x = 0 := by
  have hcast : (2 : ZMod n) * (m : ZMod n) + 1 = 0 := by
    have hz : ((2 * m + 1 : ℕ) : ZMod n) = 0 := by
      rw [← hn]; exact ZMod.natCast_self n
    push_cast at hz
    exact hz
  have key : ((m : ZMod n) + 1) * (x + x) = x := by
    calc ((m : ZMod n) + 1) * (x + x)
        = (2 * (m : ZMod n) + 1) * x + x := by ring
      _ = 0 * x + x := by rw [hcast]
      _ = x := by ring
  rw [h, mul_zero] at key
  exact key.symm

/-- The `ℤ/3` case used by the obstruction argument. -/
theorem eq_zero_of_eq_neg_zmod_three (x : ZMod 3) (h : x = -x) : x = 0 := by
  refine eq_zero_of_add_self_eq_zero_odd (m := 1) rfl x ?_
  -- `rw [h]` would rewrite BOTH occurrences, leaving `-x + -x = 0`, which needs
  -- the very fact being proved.  `linear_combination` uses `h` once.
  linear_combination h

/-- The two topological inputs, named so the theorem below wears what it uses.

`obs` is the obstruction class to lifting a boundary-unipotent `PGL(3,ℂ)` representation
to `SL(3,ℂ)`; `dual` is `ρ ↦ ᵗρ⁻¹`; `Iso` is isomorphism of representations. -/
class ObstructionDuality (Rep : Type*) (Iso : Rep → Rep → Prop) (dual : Rep → Rep)
    (obs : Rep → ZMod 3) : Prop where
  /-- Duality negates the obstruction class. -/
  obs_dual : ∀ ρ, obs (dual ρ) = - obs ρ
  /-- The obstruction class is an isomorphism invariant. -/
  obs_congr : ∀ ρ τ, Iso ρ τ → obs ρ = obs τ

variable {Rep : Type*} {Iso : Rep → Rep → Prop} {dual : Rep → Rep} {obs : Rep → ZMod 3}

/-- A self-dual representation has trivial obstruction class. -/
theorem obs_eq_zero_of_selfDual [inst : ObstructionDuality Rep Iso dual obs]
    (ρ : Rep) (h : Iso ρ (dual ρ)) : obs ρ = 0 :=
  eq_zero_of_eq_neg_zmod_three _ ((inst.obs_congr ρ (dual ρ) h).trans (inst.obs_dual ρ))

/-- **The form a search uses.**  Every representation in a non-trivial obstruction class
fails to be self-dual — hence is of complex type, with no variety decomposition required. -/
theorem not_selfDual_of_obs_ne_zero [ObstructionDuality Rep Iso dual obs]
    (ρ : Rep) (h : obs ρ ≠ 0) : ¬ Iso ρ (dual ρ) :=
  fun hsd => h (obs_eq_zero_of_selfDual ρ hsd)

end QOU.Eightfold
