import QOU.FluidDynamics.LambCalculus
import QOU.FluidDynamics.BeltramiSteadyEuler

/-!
# The two archimedean Lamb calculi

* `coord`: ℝ³ in coordinates, scalar fields `SField`, vector fields `Fin 3 → SField`.
  The Lamb identity is `lamb₁/₂/₃` of `BeltramiSteadyEuler`, on fields with
  differentiable coordinate slices. This is where the analysis (`deriv`) lives.
* `sl2 s`: left-invariant fields on `(sl₂(ℝ), diag(1,1,s²))` in the basis `(X, Y, V)`,
  with the Koszul connection and the metric cross product. Here `|u|²` is constant, so
  the gradient is zero and the Lamb identity reads `∇_u u = −u × curl u`, which is
  polynomial algebra (`sl2_lamb`).

Both instances feed `LambCalculus.steady_euler_of_beltrami`. For `sl2` this gives
`∇_V V = 0` from `curl V = −s V` (`sl2_nab_V`), recovering `L3.nab_VV` from the class.
-/

namespace QOU.FluidDynamics.LambCalculusArchimedean

open QOU.FluidDynamics BeltramiSteadyEuler

/-! ## Coordinates on ℝ³ -/

/-- Read a coordinate vector of scalar fields as a `VField`. -/
def toV (u : Fin 3 → SField) : VField := ⟨u 0, u 1, u 2⟩

/-- **The coordinate Lamb calculus on ℝ³.** -/
noncomputable def coord : LambCalculus SField (Fin 3 → SField) where
  good u := (toV u).SlicesDiff
  adv u := ![(toV u).adv (u 0), (toV u).adv (u 1), (toV u).adv (u 2)]
  ke u := (toV u).ke
  grad f := ![px f, py f, pz f]
  curl u := ![(toV u).curl₁, (toV u).curl₂, (toV u).curl₃]
  cross := LambCalculus.crossLin
  cross_self := LambCalculus.crossLin_self
  grad_neg f := by
    ext i x y z
    fin_cases i
    · exact deriv_neg_fun (fun a => f a y z) x
    · exact deriv_neg_fun (fun b => f x b z) y
    · exact deriv_neg_fun (fun c => f x y c) z
  lamb u hu := by
    ext i x y z
    fin_cases i
    · simpa [LambCalculus.crossLin_apply] using lamb₁ (toV u) hu x y z
    · simpa [LambCalculus.crossLin_apply] using lamb₂ (toV u) hu x y z
    · simpa [LambCalculus.crossLin_apply] using lamb₃ (toV u) hu x y z

/-! ## Left-invariant fields on `sl₂(ℝ)` -/

/-- Coefficients `(a, b, c)` as an `L3`. -/
def toL3 (v : Fin 3 → ℝ) : L3 := ⟨v 0, v 1, v 2⟩

/-- An `L3` as a coefficient vector. -/
def ofL3 (u : L3) : Fin 3 → ℝ := ![u.a, u.b, u.c]

/-- The metric cross product of `diag(1,1,s²)`, orientation `(X, Y, V)`, in the basis
`(X, Y, V)`: pass to the orthonormal frame `(X, Y, V/s)`, take the cross product, and
pass back. -/
noncomputable def sl2Cross (s : ℝ) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) :=
  LinearMap.mk₂ ℝ
    (fun u w => ![s * (u 1 * w 2 - u 2 * w 1), s * (u 2 * w 0 - u 0 * w 2),
      (u 0 * w 1 - u 1 * w 0) / s])
    (fun _ _ _ => by ext i; fin_cases i <;> simp <;> ring)
    (fun _ _ _ => by ext i; fin_cases i <;> simp <;> ring)
    (fun _ _ _ => by ext i; fin_cases i <;> simp <;> ring)
    (fun _ _ _ => by ext i; fin_cases i <;> simp <;> ring)

theorem sl2Cross_apply (s : ℝ) (u w : Fin 3 → ℝ) :
    sl2Cross s u w = ![s * (u 1 * w 2 - u 2 * w 1), s * (u 2 * w 0 - u 0 * w 2),
      (u 0 * w 1 - u 1 * w 0) / s] := rfl

/-- **The left-invariant Lamb identity** on `(sl₂(ℝ), diag(1,1,s²))`:
`∇_u u = −u × curl u`. -/
theorem sl2_lamb {s : ℝ} (hs : s ≠ 0) (v : Fin 3 → ℝ) :
    ofL3 (L3.nab s (toL3 v) (toL3 v)) = 0 - sl2Cross s v (ofL3 (L3.curl s (toL3 v))) := by
  ext i
  fin_cases i <;>
    simp [ofL3, toL3, sl2Cross_apply, L3.nab, L3.K, L3.g, L3.br, L3.curl, L3.e3,
      L3.eX, L3.eY, L3.eV] <;> field_simp <;> ring

/-- **The left-invariant Lamb calculus** on `(sl₂(ℝ), diag(1,1,s²))`. The kinetic energy
of a left-invariant field is constant, so the gradient is zero. -/
noncomputable def sl2 {s : ℝ} (hs : s ≠ 0) : LambCalculus ℝ (Fin 3 → ℝ) where
  good _ := True
  adv v := ofL3 (L3.nab s (toL3 v) (toL3 v))
  ke v := L3.g s (toL3 v) (toL3 v) / 2
  grad _ := 0
  curl v := ofL3 (L3.curl s (toL3 v))
  cross := sl2Cross s
  cross_self u := by ext i; fin_cases i <;> simp [sl2Cross_apply, mul_comm]
  grad_neg _ := by simp
  lamb v _ := sl2_lamb hs v

/-- `curl V = −s V` in coefficients. -/
theorem sl2_curl_V {s : ℝ} (hs : s ≠ 0) :
    (sl2 hs).curl (ofL3 L3.eV) = (-s) • ofL3 L3.eV := by
  ext i; fin_cases i <;>
    simp [sl2, ofL3, toL3, L3.curl, L3.g, L3.br, L3.e3, L3.eX, L3.eY, L3.eV] <;>
    field_simp

/-- **`∇_V V = 0`, from the class.** `V` is Beltrami, so by
`LambCalculus.adv_eq_grad_of_beltrami` its self-advection is the gradient of a constant. -/
theorem sl2_nab_V {s : ℝ} (hs : s ≠ 0) : ofL3 (L3.nab s L3.eV L3.eV) = 0 := by
  have h := (sl2 hs).adv_eq_grad_of_beltrami trivial (sl2_curl_V hs)
  simpa [sl2, toL3, ofL3] using h

end QOU.FluidDynamics.LambCalculusArchimedean
