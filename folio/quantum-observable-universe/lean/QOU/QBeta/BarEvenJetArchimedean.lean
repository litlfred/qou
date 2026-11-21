import QOU.QBeta.BarEvenJet
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Add

/-!
# The real instance of `FixedPointJet` (archimedean half of `BarEvenJet`, split per §7c)

The analysis is exactly two facts: the product rule, so that `f ↦ f(1) + f'(1) ε` is a ring
map, and `(q⁻¹)′(1) = −1`, so that the bar involution acts on the tangent by `−1`.
-/

namespace QOU.QBeta.BarEvenJet

open DualNumber TrivSqZeroExt


/-- Real functions differentiable at `1`, as a subring of `ℝ → ℝ`. -/
def diffAtOne : Subring (ℝ → ℝ) where
  carrier := {f | DifferentiableAt ℝ f 1}
  mul_mem' := fun ha hb => ha.mul hb
  one_mem' := differentiableAt_const _
  add_mem' := fun ha hb => ha.add hb
  zero_mem' := differentiableAt_const _
  neg_mem' := fun ha => ha.neg

theorem hasDerivAt_inv_one : HasDerivAt (fun x : ℝ => x⁻¹) (-1) 1 := by
  simpa using hasDerivAt_inv (one_ne_zero (α := ℝ))

theorem comp_inv_mem {f : ℝ → ℝ} (hf : f ∈ diffAtOne) : (fun x => f x⁻¹) ∈ diffAtOne := by
  show DifferentiableAt ℝ (fun x => f x⁻¹) 1
  have hf1 : DifferentiableAt ℝ f ((1 : ℝ)⁻¹) := by rw [inv_one]; exact hf
  exact hf1.comp (1 : ℝ) hasDerivAt_inv_one.differentiableAt

/-- The bar involution `f ↦ f ∘ (·)⁻¹` on `diffAtOne`. -/
noncomputable def realBar : diffAtOne →+* diffAtOne where
  toFun f := ⟨fun x => f.1 x⁻¹, comp_inv_mem f.2⟩
  map_one' := rfl
  map_mul' _ _ := rfl
  map_zero' := rfl
  map_add' _ _ := rfl

/-- The first-order jet `f ↦ f(1) + f'(1) ε`. -/
noncomputable def realJet : diffAtOne →+* DualNumber ℝ where
  toFun f := (f.1 1, deriv f.1 1)
  map_one' := by
    ext
    · rfl
    · show deriv (fun _ : ℝ => (1 : ℝ)) 1 = 0
      simp
  map_mul' f g := by
    ext
    · simp [TrivSqZeroExt.fst_mul]
    · simp only [DualNumber.snd_mul, TrivSqZeroExt.fst_mk, TrivSqZeroExt.snd_mk]
      show deriv (fun x => f.1 x * g.1 x) 1 = _
      have h : HasDerivAt (fun x => f.1 x * g.1 x)
          (deriv f.1 1 * g.1 1 + f.1 1 * deriv g.1 1) 1 :=
        (f.2.hasDerivAt).mul (g.2.hasDerivAt)
      rw [h.deriv]
      ring
  map_zero' := by
    ext
    · rfl
    · show deriv (fun _ : ℝ => (0 : ℝ)) 1 = 0
      simp
  map_add' f g := by
    ext
    · rfl
    · show deriv (fun x => f.1 x + g.1 x) 1 = deriv f.1 1 + deriv g.1 1
      have h : HasDerivAt (fun x => f.1 x + g.1 x) (deriv f.1 1 + deriv g.1 1) 1 :=
        HasDerivAt.add f.2.hasDerivAt g.2.hasDerivAt
      exact h.deriv

/-- **The real instance.** -/
noncomputable def realFixedPointJet : FixedPointJet diffAtOne ℝ where
  ι := realBar
  jet := realJet
  jet_ι f := by
    ext
    · show f.1 (1 : ℝ)⁻¹ = f.1 1
      rw [inv_one]
    · show deriv (fun x => f.1 x⁻¹) 1 = -deriv f.1 1
      have hf1 : HasDerivAt f.1 (deriv f.1 1) ((1 : ℝ)⁻¹) := by
        rw [inv_one]; exact f.2.hasDerivAt
      have := (hf1.comp (1 : ℝ) hasDerivAt_inv_one).deriv
      simpa using this

/-- **The original statement recovered as an instance** (global bar-evenness form):
a real function differentiable at `1` with `f(q⁻¹) = f(q)` for all `q` has `f'(1) = 0`.
`BarEvenForcesStationarity.deriv_at_one_eq_zero_of_barEven` is the germ form. -/
theorem deriv_at_one_eq_zero_of_barEven' {f : ℝ → ℝ} (hf : DifferentiableAt ℝ f 1)
    (hsym : ∀ x, f x⁻¹ = f x) : deriv f 1 = 0 := by
  have h := snd_jet_eq_zero_of_invariant realFixedPointJet (by norm_num : IsUnit (2 : ℝ))
    (f := ⟨f, hf⟩) (Subtype.ext (funext hsym))
  exact h

end QOU.QBeta.BarEvenJet
