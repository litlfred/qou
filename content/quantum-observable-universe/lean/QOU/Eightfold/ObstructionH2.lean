import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.Module.Submodule.Basic
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.Tactic.LinearCombination

/-!
# QOU.Eightfold.ObstructionH2 — the H² step, so the obstruction class is well defined

`ObstructionClassForcesComplexType` proves that a self-dual representation has trivial
obstruction class, *given* `ObstructionDuality`'s two hypotheses, and its `CocycleModel`
section proves their content at the level of **cocycles**.  One gap remained: a cocycle
depends on the chosen lift, so "the obstruction class of `ρ`" is not yet well defined.

This file closes that gap by constructing `H²(Γ; ℤ/3)` for the trivial action — the
centre `μ₃` is fixed under conjugation, so the action is trivial — and proving

* `twist_mem_B2` — changing the lift by `t` shifts the cocycle by `t g + t h - t (g*h)`,
  which is a **coboundary**.  So the class does not depend on the lift.  This is the
  H² step.
* `obs_dual_holds` — negating a cocycle negates its class.
* `obs_congr_holds` — cohomologous cocycles have equal classes.
* `cls_eq_zero_of_cohomologous_neg` — **unconditionally**: a cocycle cohomologous to its
  own negation has trivial class.  No hypotheses, no instance to supply.

`eq_zero_of_eq_neg_module` generalises the `ZMod 3` arithmetic to any `ZMod 3`-module,
which is needed because `H²(M, ∂M; ℤ/3)` is `(ZMod 3)³` for L6a4 — not `ZMod 3`.

## Why this is not Mathlib's `groupCohomology.H2`

Mathlib has the general machinery, and the definitions here are transcribed from it —
`IsCocycle₂` and `IsCoboundary₂` in
`Mathlib/RepresentationTheory/Homological/GroupCohomology/LowDegree.lean`, specialised to
the trivial action (`g • a = a`).  It is **not imported**: that module's transitive cone
needs **79 further Mathlib oleans** (homological algebra and category theory) which the
restored cache does not carry, and building them is hours of compute against 2.6 GB of
free disk.  The trivial-action case needs none of it — cocycles and coboundaries are
submodules of `Γ × Γ → ZMod 3` and the quotient is a `Submodule` quotient.

**That gap is now CLOSED.**  `QOU.Eightfold.ObstructionH2Mathlib` proves
`Z2 Γ = cocycles₂ (triv3 Γ)` and `B2 Γ = coboundaries₂ (triv3 Γ)` — literal equality, not
isomorphism — so these are no longer merely "our" objects agreeing by transcription.  The
79 oleans were built (`scripts/build-missing-mathlib-oleans.sh`, 79/79, no failures); the
measured cost was ~40 minutes and **53 MB**, not the "hours against 2.6 GB of free disk"
this file first claimed.  The disk half of that claim was simply wrong.

The agreement lemmas need `Γ : Type` rather than `Type*`, because `Rep k G` puts `k` and
`G` in the same universe and `ZMod 3` is in `Type 0`.  The results in THIS file stay
universe-polymorphic; only the bridge to Mathlib is specialised.

## Scope

This is group cohomology of `Γ`.  The Ptolemy obstruction is the **relative** class in
`H²(M, ∂M; ℤ/3)`; that step is verified computationally, not here — negating the cocycle
acts on the Ptolemy variety as `u ↦ u²`
(`computations/ptolemy/ptolemy_duality_galois_check.py`, classes 1/2/3).
-/

namespace QOU.Eightfold.ObstructionH2

variable (Γ : Type*) [Group Γ]

abbrev C2 := Γ × Γ → ZMod 3

/-- 2-cocycles for the TRIVIAL action (Mathlib `IsCocycle₂` with `g • a = a`). -/
def Z2 : Submodule (ZMod 3) (C2 Γ) where
  carrier := {f | ∀ g h j : Γ, f (g * h, j) + f (g, h) = f (h, j) + f (g, h * j)}
  add_mem' := by
    intro a b ha hb g h j
    have := ha g h j; have := hb g h j
    simp only [Pi.add_apply]; linear_combination ha g h j + hb g h j
  zero_mem' := by intro g h j; simp
  smul_mem' := by
    intro r a ha g h j
    simp only [Pi.smul_apply, smul_eq_mul]
    linear_combination r * ha g h j

/-- 2-coboundaries for the trivial action (Mathlib `IsCoboundary₂`). -/
def B2 : Submodule (ZMod 3) (C2 Γ) where
  carrier := {f | ∃ t : Γ → ZMod 3, ∀ g h : Γ, t h - t (g * h) + t g = f (g, h)}
  add_mem' := by
    rintro a b ⟨s, hs⟩ ⟨t, ht⟩
    exact ⟨s + t, by intro g h; simp only [Pi.add_apply]; linear_combination hs g h + ht g h⟩
  zero_mem' := ⟨0, by intro g h; simp⟩
  smul_mem' := by
    rintro r a ⟨t, ht⟩
    exact ⟨r • t, by intro g h; simp only [Pi.smul_apply, smul_eq_mul]
                     linear_combination r * ht g h⟩

/-- Every coboundary is a cocycle. -/
theorem B2_le_Z2 : B2 Γ ≤ Z2 Γ := by
  rintro f ⟨t, ht⟩ g h j
  rw [← ht (g * h) j, ← ht g h, ← ht h j, ← ht g (h * j), mul_assoc]
  ring

/-- `H²(Γ; ℤ/3)` for the trivial action. -/
abbrev H2 := (Z2 Γ) ⧸ (Submodule.comap (Z2 Γ).subtype (B2 Γ))

variable {Γ}

/-- The class of a cocycle. -/
def cls (c : Z2 Γ) : H2 Γ := Submodule.Quotient.mk c

/-- **Lift-independence, the H² step.**  Twisting a lift by `t` shifts its cocycle by
`t g + t h - t (g*h)`, which is a coboundary — so the CLASS is unchanged. -/
theorem twist_mem_B2 (t : Γ → ZMod 3) :
    (fun p : Γ × Γ => t p.1 + t p.2 - t (p.1 * p.2)) ∈ B2 Γ :=
  ⟨t, by intro g h; ring⟩

/-- Two cocycles differing by a coboundary have the same class. -/
theorem cls_eq_of_sub_mem (c c' : Z2 Γ) (h : (c' : C2 Γ) - (c : C2 Γ) ∈ B2 Γ) :
    cls c' = cls c := by
  rw [cls, cls, Submodule.Quotient.eq]
  exact h

/-- **`obs_dual` at the level of classes.**  Negating a cocycle negates its class —
this is what carries `cocycle_dual` (`c* = c⁻¹`) up to `obs (dual ρ) = - obs ρ`. -/
theorem cls_neg (c : Z2 Γ) : cls (-c) = - cls c := rfl

/-- `x = -x` forces `x = 0` in ANY `ZMod 3`-module — not just `ZMod 3` itself.  Needed
because `H²(M, ∂M; ℤ/3)` is `(ZMod 3)³` for L6a4, not `ZMod 3`. -/
theorem eq_zero_of_eq_neg_module {M : Type*} [AddCommGroup M] [Module (ZMod 3) M]
    (x : M) (h : x = -x) : x = 0 := by
  have hx : x + x = 0 := by nth_rewrite 2 [h]; exact add_neg_cancel x
  have h2 : (2 : ZMod 3) • x = 0 := by rw [two_smul]; exact hx
  calc x = ((2 : ZMod 3) * 2) • x := by rw [show (2 * 2 : ZMod 3) = 1 from by decide, one_smul]
    _ = (2 : ZMod 3) • ((2 : ZMod 3) • x) := by rw [mul_smul]
    _ = 0 := by rw [h2, smul_zero]

/-- Cohomologous cocycles. -/
def Cohomologous (c c' : Z2 Γ) : Prop := (c' : C2 Γ) - (c : C2 Γ) ∈ B2 Γ

/-- **`obs_dual` and `obs_congr` both hold, for real, in this model.**  `dual` is negation
of the cocycle (that is `cocycle_dual`), `obs` is the H² class, and `Iso` is being
cohomologous. -/
theorem obs_dual_holds (c : Z2 Γ) : cls (-c) = - cls c := rfl

theorem obs_congr_holds (c c' : Z2 Γ) (h : Cohomologous c c') : cls c = cls c' :=
  (cls_eq_of_sub_mem c c' h).symm

/-- **The payoff, unconditionally.**  A cocycle cohomologous to its own negation has
trivial class — so a self-dual representation lies in the trivial obstruction class, and
every non-trivial class is barred from self-duality.  No hypotheses. -/
theorem cls_eq_zero_of_cohomologous_neg (c : Z2 Γ) (h : Cohomologous c (-c)) :
    cls c = 0 := by
  exact eq_zero_of_eq_neg_module _ ((obs_congr_holds c (-c) h).trans (obs_dual_holds c))


end QOU.Eightfold.ObstructionH2
