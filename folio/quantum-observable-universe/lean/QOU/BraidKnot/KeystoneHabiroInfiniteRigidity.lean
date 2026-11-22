/-
Copyright (c) 2026 litlfred. All rights reserved.

# Infinite-root rigidity — the clean form of Habiro all-roots agreement (chips bwsc + bwsd)

Strengthens the finite interpolation rigidity
(`KeystoneGaugeRowRigidity.eq_of_eval_agree_card`,
`KeystoneHabiroRootFamily.eq_of_root_family_agreement`) to the **infinite-root**
form that matches the actual Habiro rigidity: a unified WRT invariant is an element
of the Habiro ring `Ẑ[q]` determined by its values at **all** roots of unity
(`habiro2004`).  If the gauge-row polynomial agrees with the value-map polynomial at
*infinitely many* fibre roots, they are equal — **with no degree hypothesis**
(bwsd's bounded-degree assumption is dissolved by using the full root family).

* `eq_of_infinite_agreement` — agreement on any infinite real set forces equality.
* `foldValues_infinite` — the fibre-root fold values `{2cos(π/N) : N}` are an
  infinite set (the WRT/Habiro all-levels family).
* `eq_of_habiro_root_agreement` — the combined statement: agreement of the gauge row
  with the value map across the full fold family forces equality, hence continuation
  to the substrate `t₀`, **without** the bounded-degree hypothesis.

**Honest scope (STRICT).** This dissolves the *degree* half of the residual (bwsd)
by using infinitely many roots; the remaining open content is purely **bwsc** — that
the gauge row `bwS0` actually agrees with the value map at those roots (WRT =
modular-data), of which `KeystoneLRAmplitudeReal` (#4365) is the `Σ(2,3,5)` slice.
No fit; nothing wired; L2 unchanged.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-- Ref: [habiro2004] https://doi.org/10.1007/s00222-007-0071-0
-/
import QOU.BraidKnot.KeystoneHabiroRootFamily

namespace QOU.BraidKnot.KeystoneHabiroInfiniteRigidity

open Polynomial Real

/-- **Infinite-root rigidity.** If two real polynomials agree on an infinite set of
points, they are equal.  (A nonzero polynomial has finitely many roots.) -/
theorem eq_of_infinite_agreement (p q : ℝ[X]) (S : Set ℝ)
    (hS : S.Infinite) (h : ∀ x ∈ S, p.eval x = q.eval x) : p = q := by
  apply Polynomial.eq_of_infinite_eval_eq
  exact hS.mono (fun x hx => h x hx)

/-- The single-index fibre fold family `N ↦ 2cos(π/(N+2))` is injective: the angles
`π/(N+2)` are distinct in `(0, π]` and `cos` is injective there. -/
theorem foldOne_injective :
    Function.Injective (fun N : ℕ => 2 * Real.cos (π / ((N : ℝ) + 2))) := by
  intro N M hNM
  have hcos : Real.cos (π / ((N : ℝ) + 2)) = Real.cos (π / ((M : ℝ) + 2)) := by
    have : (2 : ℝ) * Real.cos (π / ((N : ℝ) + 2)) = 2 * Real.cos (π / ((M : ℝ) + 2)) := hNM
    linarith
  have hmemN : π / ((N : ℝ) + 2) ∈ Set.Icc (0 : ℝ) π := by
    constructor
    · positivity
    · rw [div_le_iff₀ (by positivity)]
      nlinarith [Real.pi_pos, (by positivity : (0:ℝ) ≤ (N:ℝ))]
  have hmemM : π / ((M : ℝ) + 2) ∈ Set.Icc (0 : ℝ) π := by
    constructor
    · positivity
    · rw [div_le_iff₀ (by positivity)]
      nlinarith [Real.pi_pos, (by positivity : (0:ℝ) ≤ (M:ℝ))]
  have hangle : π / ((N : ℝ) + 2) = π / ((M : ℝ) + 2) :=
    Real.strictAntiOn_cos.injOn hmemN hmemM hcos
  -- π/(N+2) = π/(M+2) with π > 0 ⇒ N = M
  have hπ : (π : ℝ) ≠ 0 := ne_of_gt Real.pi_pos
  have h1 : ((N : ℝ) + 2) ≠ 0 := by positivity
  have h2 : ((M : ℝ) + 2) ≠ 0 := by positivity
  rw [div_eq_div_iff h1 h2] at hangle
  -- hangle : π * (M + 2) = π * (N + 2)
  have hden : ((M : ℝ) + 2) = ((N : ℝ) + 2) := mul_left_cancel₀ hπ hangle
  have : (N : ℝ) = (M : ℝ) := by linarith
  exact_mod_cast this

/-- The fibre-root fold values `{2cos(π/(N+2)) : N ∈ ℕ}` form an **infinite** set —
the WRT/Habiro all-levels root family. -/
theorem foldValues_infinite :
    (Set.range (fun N : ℕ => 2 * Real.cos (π / ((N : ℝ) + 2)))).Infinite :=
  Set.infinite_range_of_injective foldOne_injective

/-- **Habiro all-roots agreement forces equality (no degree bound).** If the
gauge-row polynomial `bwPoly` agrees with the value-map polynomial `valPoly` at every
fold value `2cos(π/(N+2))` (the full fibre-root family), then `bwPoly = valPoly` —
hence they agree at the substrate `t₀`.  The bounded-degree hypothesis (bwsd) is
dissolved by the infinitude of the root family; the sole residual is the agreement
itself (bwsc / WRT = modular-data). -/
theorem eq_of_habiro_root_agreement (bwPoly valPoly : ℝ[X])
    (h : ∀ N : ℕ, bwPoly.eval (2 * Real.cos (π / ((N : ℝ) + 2)))
      = valPoly.eval (2 * Real.cos (π / ((N : ℝ) + 2)))) :
    bwPoly = valPoly := by
  refine eq_of_infinite_agreement bwPoly valPoly
    (Set.range (fun N : ℕ => 2 * Real.cos (π / ((N : ℝ) + 2)))) foldValues_infinite ?_
  rintro x ⟨N, rfl⟩
  exact h N

/-- **Two roots are insufficient (the Σ(2,3,5) slice alone does not pin the value
map).** For any two distinct fibre points `a ≠ b` and any value-map polynomial `V`,
there is a *different* polynomial `W ≠ V` agreeing with `V` at both points
(`W = V + (X−a)(X−b)`).  So the two-flat-connection agreement of `KeystoneLRAmplitudeReal`
(#4365) cannot alone force `bwS0 = V` — brackets the residual `bwsc` from below:
2 roots fail, the infinite family (`eq_of_habiro_root_agreement`) succeeds, so the
open work is exactly *extending the WRT agreement from the Σ(2,3,5) slice toward the
full root family*. -/
theorem two_roots_insufficient (a b : ℝ) (hab : a ≠ b) (V : ℝ[X]) :
    ∃ W : ℝ[X], W ≠ V ∧ W.eval a = V.eval a ∧ W.eval b = V.eval b := by
  refine ⟨V + (X - C a) * (X - C b), ?_, ?_, ?_⟩
  · intro hWV
    have hP : (X - C a) * (X - C b) = 0 := by linear_combination hWV
    have hne : (X - C a) * (X - C b) ≠ (0 : ℝ[X]) :=
      mul_ne_zero (X_sub_C_ne_zero a) (X_sub_C_ne_zero b)
    exact hne hP
  · simp [eval_add, eval_mul, eval_sub, eval_X, eval_C]
  · simp [eval_add, eval_mul, eval_sub, eval_X, eval_C]

end QOU.BraidKnot.KeystoneHabiroInfiniteRigidity
