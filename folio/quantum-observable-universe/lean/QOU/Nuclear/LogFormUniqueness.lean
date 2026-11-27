/-
Copyright (c) 2026 litlfred. Released under CC BY 4.0.
-/
import Mathlib.Topology.Instances.RealVectorSpace
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The log form of the binding law is the unique extensive form

`QOU.Nuclear.InterfaceScalar.logForm_extensive` shows that `B = -a · log r` turns
a product of bond ratios into a sum of energies, and `linearForm_not_extensive`
shows that `B = a · (1 - r)` does not. This file proves the converse that the
2026-08-08 audit (`docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`
§10a) states in prose: every continuous map from the positive trace ratios to the
reals that sends products to sums is a constant multiple of `log`.

So a binding functional `B(r)` of the trace ratio `r = tr_atom / tr_free` that is
continuous and extensive over independent subsystems
(`B(r₁ r₂) = B(r₁) + B(r₂)`, because the trace is multiplicative on disjoint
blocks) is forced to be `B(r) = -c · log r`. The scale `c` is not fixed here.

Archimedean (AGENTS.md §7c): the statement is about `Real.log` and continuity on
`(0, ∞)`, so it lives over `ℝ`.

Reference: J. Aczél, *Lectures on Functional Equations and Their Applications*
(1966), §2.1 (the Cauchy equation under continuity).
-/

namespace QOU.Nuclear.LogFormUniqueness

open Real

/-- **Cauchy uniqueness on `(ℝ₊, ×)`.** A function on the positive reals that is
continuous there and sends products to sums equals `f e · log x`. -/
theorem eq_mul_log_of_mul_add (f : ℝ → ℝ) (hf : ContinuousOn f (Set.Ioi 0))
    (hmul : ∀ x y : ℝ, 0 < x → 0 < y → f (x * y) = f x + f y) :
    ∀ x : ℝ, 0 < x → f x = f (exp 1) * log x := by
  -- `g t = f (exp t)` is additive and continuous on all of `ℝ`.
  have hf1 : f 1 = 0 := by
    have h := hmul 1 1 one_pos one_pos
    rw [one_mul] at h
    linarith
  have hgc : Continuous (fun t : ℝ => f (exp t)) :=
    hf.comp_continuous continuous_exp (fun t => exp_pos t)
  let G : ℝ →+ ℝ :=
    { toFun := fun t => f (exp t)
      map_zero' := by simp [hf1]
      map_add' := fun s t => by
        show f (exp (s + t)) = f (exp s) + f (exp t)
        rw [exp_add]
        exact hmul _ _ (exp_pos s) (exp_pos t) }
  have hG : Continuous G := hgc
  intro x hx
  have key : G (log x • (1 : ℝ)) = log x • G 1 := map_real_smul G hG (log x) 1
  simp only [smul_eq_mul, mul_one] at key
  have hGx : G (log x) = f x := by
    show f (exp (log x)) = f x
    rw [exp_log hx]
  have hG1 : G 1 = f (exp 1) := rfl
  rw [hGx, hG1] at key
  rw [key, mul_comm]

/-- **The binding law is forced to the log form.** A binding functional of the
trace ratio that is continuous on `(0, ∞)` and extensive over independent
subsystems is `B r = -c · log r`, with `c = -B (exp 1)`. -/
theorem binding_eq_neg_mul_log (B : ℝ → ℝ) (hB : ContinuousOn B (Set.Ioi 0))
    (hext : ∀ r₁ r₂ : ℝ, 0 < r₁ → 0 < r₂ → B (r₁ * r₂) = B r₁ + B r₂) :
    ∃ c : ℝ, ∀ r : ℝ, 0 < r → B r = -c * log r :=
  ⟨-B (exp 1), fun r hr => by
    rw [eq_mul_log_of_mul_add B hB hext r hr]; ring⟩

/-- The linear form `B r = a (1 - r)` is not of this shape unless `a = 0`: it is
continuous, so by `binding_eq_neg_mul_log` it can be extensive only if it is a
multiple of `log`, which it is not (compare at `r = 2` and `r = 4`). -/
theorem linear_form_not_extensive_unless_zero (a : ℝ)
    (hext : ∀ r₁ r₂ : ℝ, 0 < r₁ → 0 < r₂ →
      a * (1 - r₁ * r₂) = a * (1 - r₁) + a * (1 - r₂)) :
    a = 0 := by
  have h := hext 2 2 (by norm_num) (by norm_num)
  nlinarith [h]

end QOU.Nuclear.LogFormUniqueness
