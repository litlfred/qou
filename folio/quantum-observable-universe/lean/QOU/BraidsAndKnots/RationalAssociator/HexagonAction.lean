import QOU.BraidsAndKnots.RationalAssociator.FarRelation

/-!
# The `GRT` right action preserves the hexagon

Bean `qou-3fdg` (stage 3e of the rational-associator plan, epic `qou-dk7p`). Builds on
`GRTAction.lean` (the action `φ̃(A, B) = φ(g A g⁻¹, B) · g`, as `actEval`) and
`FarRelation.lean` (the t-compatibility identity `TCompat`).

The hexagon is the repo's form (`LowDegree.lean`): at a three-strand family `(t₁₂, t₁₃, t₂₃)`,

    e((t₁₃ + t₂₃)) = φ(t₁₃, t₁₂) · e(t₁₃) · φ(t₂₃, t₁₃) · e(t₂₃) · φ(t₁₂, t₂₃),

where `e(x) = E(x)` for a one-variable noncommutative polynomial `E`; with `E` the exponential
`exp(X/2)` truncated at the nilpotence order this is Drinfeld's hexagon in a truncated algebra
(`hexagon_expHalfPoly_iff` relates it to `LowDegree.lean`).

* `hexagon_act_of_transport`: with `G₁ = g(t₁₃,t₁₂)`, `G₂ = g(t₂₃,t₁₃)`, `G₃ = g(t₁₂,t₂₃)`, the
  μ = 0 hexagon (5.14) of `g` in the form `G₂ G₃ G₁ = 1`, and the identity
  `G₁ t₁₃ G₁⁻¹ + G₃⁻¹ t₂₃ G₃ = t₁₃ + t₂₃`, the hexagon of `φ` at the transported family
  `(t₁₂, G₁ t₁₃ G₁⁻¹, G₃⁻¹ t₂₃ G₃)` implies the hexagon of `φ̃` at `(t₁₂, t₁₃, t₂₃)`.
* `hexagon_act`: the identity above follows from `DK3`, (5.13) at `(t₂₃, t₁₂)` and `TCompat` at
  `(t₂₃, t₁₃, t₁₂)`.
* `transported3_dk3`: the transported family is again `DK3`.
* `hexagon_act_all`: if `φ` satisfies the hexagon at every `DK3` family of `R`, then `φ̃`
  satisfies it at every `DK3` family at which `g` satisfies (5.13), (5.14) and `TCompat`.

No truncation is needed in these statements: the proof is an identity of products. Exact
check over `ℚ` in `U(𝔱₃)` through degree 5:
`computations/rational_associator/grt_far_relation/hexagon_act.py`. Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

section Hexagon

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- The hexagon of `φ` at a three-strand family, with the exponential given by the
one-variable polynomial `E` (evaluated as `eval x 0 E`). -/
def Hexagon (φ E : FreeAlgebra ℚ (Fin 2)) (t12 t13 t23 : R) : Prop :=
  eval (t13 + t23) 0 E =
    eval t13 t12 φ * eval t13 0 E * eval t23 t13 φ * eval t23 0 E * eval t12 t23 φ

/-- `exp(X/2)` truncated at degree 3, as a polynomial. -/
noncomputable def expHalfPoly : FreeAlgebra ℚ (Fin 2) :=
  1 + (1 / 2 : ℚ) • FreeAlgebra.ι ℚ 0 + (1 / 8 : ℚ) • (FreeAlgebra.ι ℚ 0 * FreeAlgebra.ι ℚ 0)

theorem eval_expHalfPoly (x b : R) : eval x b expHalfPoly = expHalf x := by
  simp [expHalfPoly, expHalf]

/-- With `E = expHalfPoly` and `φ = phiPoly c`, `Hexagon` is the hexagon of `LowDegree.lean`. -/
theorem hexagon_expHalfPoly_iff (c : ℚ) (t12 t13 t23 : R) :
    Hexagon (phiPoly c) expHalfPoly t12 t13 t23 ↔
      expHalf (t13 + t23) =
        phi c t13 t12 * expHalf t13 * phi c t23 t13 * expHalf t23 * phi c t12 t23 := by
  simp only [Hexagon, eval_expHalfPoly, eval_phiPoly]

theorem eval_conj_zero (u : Rˣ) (x : R) (E : FreeAlgebra ℚ (Fin 2)) :
    eval ((↑u⁻¹ : R) * x * u) 0 E = (↑u⁻¹ : R) * eval x 0 E * u := by
  simpa using eval_conj u x 0 E

/-- **The hexagon under the `GRT` action, given the transported family.** -/
theorem hexagon_act_of_transport (φ g E : FreeAlgebra ℚ (Fin 2)) {t12 t13 t23 : R}
    (G1 G2 G3 : Rˣ)
    (h1 : (G1 : R) = eval t13 t12 g) (h2 : (G2 : R) = eval t23 t13 g)
    (h3 : (G3 : R) = eval t12 t23 g)
    (h514 : eval t23 t13 g * eval t12 t23 g * eval t13 t12 g = 1)
    (hsum : (G1 : R) * t13 * ↑G1⁻¹ + (↑G3⁻¹ : R) * t23 * G3 = t13 + t23)
    (hφ : Hexagon φ E t12 ((G1 : R) * t13 * ↑G1⁻¹) ((↑G3⁻¹ : R) * t23 * G3)) :
    eval (t13 + t23) 0 E =
      actEval φ t13 t12 G1 * eval t13 0 E * actEval φ t23 t13 G2 * eval t23 0 E *
        actEval φ t12 t23 G3 := by
  have hZ : G2 * G3 = G1⁻¹ :=
    eq_inv_of_mul_eq_one_left (Units.ext (by simp [h1, h2, h3, h514]))
  have hG1 : G1 = (G2 * G3)⁻¹ := by rw [hZ, inv_inv]
  unfold Hexagon at hφ
  rw [hsum] at hφ
  rw [hφ]
  clear h1 h2 h3 h514 hsum hφ hZ
  subst hG1
  -- the five factors, one at a time
  have f1 : eval ((↑(G2 * G3)⁻¹ : R) * t13 * ↑(G2 * G3)⁻¹⁻¹) t12 φ =
      actEval φ t13 t12 (G2 * G3)⁻¹ * ↑(G2 * G3) := by
    simp only [actEval, inv_inv, mul_assoc, Units.inv_mul, mul_one]
  have f2 : eval ((↑(G2 * G3)⁻¹ : R) * t13 * ↑(G2 * G3)⁻¹⁻¹) 0 E =
      (↑(G2 * G3)⁻¹ : R) * eval t13 0 E * ↑(G2 * G3) := by
    simpa using eval_conj_zero (G2 * G3) t13 E
  have f3 : eval ((↑G3⁻¹ : R) * t23 * G3) ((↑(G2 * G3)⁻¹ : R) * t13 * ↑(G2 * G3)⁻¹⁻¹) φ =
      (↑(G2 * G3)⁻¹ : R) * actEval φ t23 t13 G2 * G3 := by
    have e : (↑G3⁻¹ : R) * t23 * G3 =
        (↑(G2 * G3)⁻¹ : R) * ((G2 : R) * t23 * ↑G2⁻¹) * ↑(G2 * G3) := by
      simp only [mul_inv_rev, Units.val_mul, mul_assoc, Units.inv_mul_cancel_left]
    rw [e, inv_inv, eval_conj]
    simp only [actEval, mul_inv_rev, Units.val_mul, mul_assoc]
  have f4 : eval ((↑G3⁻¹ : R) * t23 * G3) 0 E = (↑G3⁻¹ : R) * eval t23 0 E * G3 :=
    eval_conj_zero G3 t23 E
  have f5 : eval t12 ((↑G3⁻¹ : R) * t23 * G3) φ = (↑G3⁻¹ : R) * actEval φ t12 t23 G3 := by
    rw [actEval_eq]; simp [← mul_assoc]
  rw [f1, f2, f3, f4, f5]
  simp only [mul_assoc, Units.mul_inv_cancel_left]

/-- The identity `G₁ t₁₃ G₁⁻¹ + G₃⁻¹ t₂₃ G₃ = t₁₃ + t₂₃` from `DK3`, (5.13) at `(t₂₃, t₁₂)` and
t-compatibility at `(u, v, w) = (t₂₃, t₁₃, t₁₂)`. -/
theorem transported3_sum (g : FreeAlgebra ℚ (Fin 2)) {t12 t13 t23 : R}
    (hDK : DK3 t12 t13 t23) (G1 G3 K : Rˣ)
    (h3 : (G3 : R) = eval t12 t23 g) (hK : (K : R) = eval t23 t12 g)
    (h513 : eval t23 t12 g * eval t12 t23 g = 1) (htc : TCompat t13 t12 K G1) :
    (G1 : R) * t13 * ↑G1⁻¹ + (↑G3⁻¹ : R) * t23 * G3 = t13 + t23 := by
  have eK : K = G3⁻¹ := eq_inv_of_mul_eq_one_left (Units.ext (by simp [hK, h3, h513]))
  subst eK
  unfold TCompat at htc
  simp only [inv_inv] at htc
  have c12 : Commute t12 (t12 + t13 + t23) := by
    rw [add_assoc]; exact (Commute.refl t12).add_right hDK.n12_3
  have c23 : Commute t23 (t12 + t13 + t23) := hDK.n23_1.add_right (Commute.refl t23)
  have cG : Commute (G3 : R) (t12 + t13 + t23) := h3 ▸ commute_eval c12 c23 g
  rw [htc]
  have : (↑G3⁻¹ : R) * (t13 + t12) * G3 - t12 + (↑G3⁻¹ : R) * t23 * G3 =
      (↑G3⁻¹ : R) * (t12 + t13 + t23) * G3 - t12 := by noncomm_ring
  rw [this, conj_of_commute cG]; abel

/-- **The `GRT` action preserves the hexagon at a family**, given the hexagon of `φ` at the
transported family `(t₁₂, G₁ t₁₃ G₁⁻¹, G₃⁻¹ t₂₃ G₃)` and (5.13), (5.14), `TCompat` of `g`. -/
theorem hexagon_act (φ g E : FreeAlgebra ℚ (Fin 2)) {t12 t13 t23 : R}
    (hDK : DK3 t12 t13 t23) (G1 G2 G3 K : Rˣ)
    (h1 : (G1 : R) = eval t13 t12 g) (h2 : (G2 : R) = eval t23 t13 g)
    (h3 : (G3 : R) = eval t12 t23 g) (hK : (K : R) = eval t23 t12 g)
    (h513 : eval t23 t12 g * eval t12 t23 g = 1)
    (h514 : eval t23 t13 g * eval t12 t23 g * eval t13 t12 g = 1)
    (htc : TCompat t13 t12 K G1)
    (hφ : Hexagon φ E t12 ((G1 : R) * t13 * ↑G1⁻¹) ((↑G3⁻¹ : R) * t23 * G3)) :
    eval (t13 + t23) 0 E =
      actEval φ t13 t12 G1 * eval t13 0 E * actEval φ t23 t13 G2 * eval t23 0 E *
        actEval φ t12 t23 G3 :=
  hexagon_act_of_transport φ g E G1 G2 G3 h1 h2 h3 h514
    (transported3_sum g hDK G1 G3 K h3 hK h513 htc) hφ

/-- The transported family `(t₁₂, G₁ t₁₃ G₁⁻¹, G₃⁻¹ t₂₃ G₃)` is a `DK3` family. -/
theorem transported3_dk3 (g : FreeAlgebra ℚ (Fin 2)) {t12 t13 t23 : R}
    (hDK : DK3 t12 t13 t23) (G1 G3 : Rˣ)
    (h1 : (G1 : R) = eval t13 t12 g) (h3 : (G3 : R) = eval t12 t23 g)
    (hsum : (G1 : R) * t13 * ↑G1⁻¹ + (↑G3⁻¹ : R) * t23 * G3 = t13 + t23) :
    DK3 t12 ((G1 : R) * t13 * ↑G1⁻¹) ((↑G3⁻¹ : R) * t23 * G3) := by
  set c := t12 + t13 + t23 with hc
  have c12 : Commute t12 c := by rw [hc, add_assoc]; exact (Commute.refl t12).add_right hDK.n12_3
  have c13 : Commute t13 c := by
    rw [hc, show t12 + t13 + t23 = t13 + (t12 + t23) by abel]
    exact (Commute.refl t13).add_right hDK.n13_2
  have c23 : Commute t23 c := hDK.n23_1.add_right (Commute.refl t23)
  have cG1 : Commute (G1 : R) c := h1 ▸ commute_eval c13 c12 g
  have cG3 : Commute (G3 : R) c := h3 ▸ commute_eval c12 c23 g
  have cG1' : Commute (↑G1⁻¹ : R) c := cG1.units_inv_left
  have cG3' : Commute (↑G3⁻¹ : R) c := cG3.units_inv_left
  have cs13 : Commute ((G1 : R) * t13 * ↑G1⁻¹) c := (cG1.mul_left c13).mul_left cG1'
  have cs23 : Commute ((↑G3⁻¹ : R) * t23 * G3) c := (cG3'.mul_left c23).mul_left cG3
  have e13 : t12 + (↑G3⁻¹ : R) * t23 * G3 = c - (G1 : R) * t13 * ↑G1⁻¹ := by
    rw [hc, add_assoc t12 t13 t23, ← hsum]; abel
  have e23 : t12 + (G1 : R) * t13 * ↑G1⁻¹ = c - (↑G3⁻¹ : R) * t23 * G3 := by
    rw [hc, add_assoc t12 t13 t23, ← hsum]; abel
  refine ⟨?_, ?_, ?_⟩
  · rw [hsum]; exact hDK.n12_3
  · rw [e13]; exact cs13.sub_right (Commute.refl _)
  · rw [e23]; exact cs23.sub_right (Commute.refl _)

/-- **The hexagon set is preserved.** If `φ` satisfies the hexagon at every `DK3` family of `R`,
then `φ̃ = φ(g A g⁻¹, B) · g` satisfies it at every `DK3` family at which the evaluations of `g`
are the units `G₁, G₂, G₃, K` and `g` satisfies (5.13), (5.14) and `TCompat`. -/
theorem hexagon_act_all (φ g E : FreeAlgebra ℚ (Fin 2))
    (hφ : ∀ s12 s13 s23 : R, DK3 s12 s13 s23 → Hexagon φ E s12 s13 s23)
    {t12 t13 t23 : R} (hDK : DK3 t12 t13 t23) (G1 G2 G3 K : Rˣ)
    (h1 : (G1 : R) = eval t13 t12 g) (h2 : (G2 : R) = eval t23 t13 g)
    (h3 : (G3 : R) = eval t12 t23 g) (hK : (K : R) = eval t23 t12 g)
    (h513 : eval t23 t12 g * eval t12 t23 g = 1)
    (h514 : eval t23 t13 g * eval t12 t23 g * eval t13 t12 g = 1)
    (htc : TCompat t13 t12 K G1) :
    eval (t13 + t23) 0 E =
      actEval φ t13 t12 G1 * eval t13 0 E * actEval φ t23 t13 G2 * eval t23 0 E *
        actEval φ t12 t23 G3 :=
  hexagon_act φ g E hDK G1 G2 G3 K h1 h2 h3 hK h513 h514 htc
    (hφ _ _ _ (transported3_dk3 g hDK G1 G3 h1 h3
      (transported3_sum g hDK G1 G3 K h3 hK h513 htc)))

end Hexagon

end QOU.BraidsAndKnots.RationalAssociator
