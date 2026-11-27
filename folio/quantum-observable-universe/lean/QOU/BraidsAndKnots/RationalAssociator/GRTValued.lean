import QOU.BraidsAndKnots.RationalAssociator.GRTFlow

/-!
# The action theorems with the second factor given by values, and with defects

Bean `qou-3fdg` (stage 4, epic `qou-dk7p`). Drinfeld's numbering (1991, §5): (5.12) inversion,
(5.13) the `μ = 0` hexagon, (5.14) `t`-compatibility, (5.15) the pentagon, (5.16) the group law.

The action theorems of `GRTAction.lean`, `TransportedDK4.lean`, `FarRelation.lean`,
`HexagonAction.lean` and `GRTClosure.lean` take the second factor `g` of `φ ∘ g` as a polynomial
`g ∈ ℚ⟨A, B⟩` and use it only through

* its values `G = g(a, b)` at finitely many pairs, which are units, and
* `commute_eval`: `g(a, b)` commutes with every `x` that commutes with `a` and `b`.

This file restates them for a **value function** `γ : R → R → R` with that commutation
property (`CommProp γ`), not necessarily the evaluation of a polynomial. The stage-4 flow
argument (`GRTDoubling.lean`) needs this: there `γ(a, b) = 1 + ε·y(a, b)` in the dual numbers,
which is not the value of any polynomial over `ℚ` at the points `a, b`.

The theorems are also restated **with defects**: instead of assuming that `φ` satisfies a
condition at the transported family and concluding that `φ ∘ γ` satisfies it, each says that the
defect of `φ ∘ γ` equals (a unit times) the defect of `φ` at the transported family. Every
hypothesis on `γ` is exact. Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

section Valued

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- `γ(a, b)` commutes with everything that commutes with both `a` and `b`. -/
def CommProp (γ : R → R → R) : Prop :=
  ∀ a b x : R, Commute a x → Commute b x → Commute (γ a b) x

/-- The pentagon of the values `γ` at a four-strand family, in the form of `Pentagon`. -/
def PentagonV (γ : R → R → R) (t12 t13 t23 t24 t34 : R) : Prop :=
  γ t12 (t23 + t24) * γ (t13 + t23) t34 = γ t23 t34 * γ (t12 + t13) (t24 + t34) * γ t12 t23

/-- The pentagon defect of `φ` at a four-strand family. -/
noncomputable def pentDefect (φ : FreeAlgebra ℚ (Fin 2)) (t12 t13 t23 t24 t34 : R) : R :=
  eval t12 (t23 + t24) φ * eval (t13 + t23) t34 φ -
    eval t23 t34 φ * eval (t12 + t13) (t24 + t34) φ * eval t12 t23 φ

/-! ### The pentagon -/

/-- **The pentagon under the action, with defect.** For a `DK4` family `t` and units `Ga … Ge`
equal to the values of `γ` at the five cofaces, with `γ`'s pentagon, the pentagon defect of
`φ ∘ γ` at `t` is `Gc Gb` times the pentagon defect of `φ` at the transported family. -/
theorem pentagon_actV (φ : FreeAlgebra ℚ (Fin 2)) (γ : R → R → R) (hγ : CommProp γ)
    {t12 t13 t14 t23 t24 t34 : R}
    (hDK : DK4 t12 t13 t14 t23 t24 t34) (Ga Gb Gc Gd Ge : Rˣ)
    (ha : (Ga : R) = γ t12 t23) (hb : (Gb : R) = γ (t13 + t23) t34)
    (hc : (Gc : R) = γ t12 (t23 + t24)) (hd : (Gd : R) = γ (t12 + t13) (t24 + t34))
    (he : (Ge : R) = γ t23 t34)
    (hg : PentagonV γ t12 t13 t23 t24 t34) :
    actEval φ t12 (t23 + t24) Gc * actEval φ (t13 + t23) t34 Gb -
      actEval φ t23 t34 Ge * actEval φ (t12 + t13) (t24 + t34) Gd * actEval φ t12 t23 Ga =
    ↑(Gc * Gb) * (let s := transported t12 t13 t23 t24 t34 Ga Gb Gc
      pentDefect φ s.1 s.2.1 s.2.2.1 s.2.2.2.1 s.2.2.2.2) := by
  have hP : Gc * Gb = Ge * Gd * Ga := by
    ext; simp only [Units.val_mul]; rw [ha, hb, hc, hd, he]; exact hg
  have cb12 : Commute (Gb : R) t12 := hb ▸ hγ _ _ _ hDK.n12_3.symm hDK.f12_34.symm
  have cc34 : Commute (Gc : R) t34 := hc ▸ hγ _ _ _ hDK.f12_34 hDK.n34_2.symm
  have cd23 : Commute (Gd : R) t23 := hd ▸ hγ _ _ _ hDK.n23_1.symm hDK.n23_4.symm
  have ca3 : Commute (Ga : R) (t12 + t13 + t23) := by
    rw [ha]
    refine hγ _ _ _ ?_ ?_
    · have := hDK.n12_3; rw [show t12 + t13 + t23 = t12 + (t13 + t23) by abel]
      exact (Commute.refl t12).add_right this
    · have := hDK.n23_1; rw [show t12 + t13 + t23 = (t12 + t13) + t23 by abel]
      exact this.add_right (Commute.refl t23)
  have ce3 : Commute (Ge : R) (t23 + t24 + t34) := by
    rw [he]
    refine hγ _ _ _ ?_ ?_
    · rw [show t23 + t24 + t34 = t23 + (t24 + t34) by abel]
      exact (Commute.refl t23).add_right hDK.n23_4
    · rw [show t23 + t24 + t34 = (t23 + t24) + t34 by abel]
      exact hDK.n34_2.add_right (Commute.refl t34)
  have hP' : Gc * Gb = Ge * (Gd * Ga) := by rw [hP, mul_assoc]
  have F1 : (↑(Gc * Gb)⁻¹ : R) * t34 * ↑(Gc * Gb) = (↑Gb⁻¹ : R) * t34 * Gb :=
    conj_mul_of_commute cc34
  have F2 : (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) = (↑Ga⁻¹ : R) * t23 * Ga :=
    conj_mul_of_commute cd23
  have F3 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gc * Gb) =
      (↑(Gd * Ga)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gd * Ga) := by
    rw [hP']; exact conj_mul_of_commute ce3
  simp only [transported, pentDefect]
  have k1 : ∀ x y : R, x + (y - x) = y := fun x y => by abel
  have k2 : ∀ x y : R, y - x + x = y := fun x y => by abel
  rw [k1, k2]
  have eL1 : (↑Gb⁻¹ : R) * eval t12 ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) φ * Gb =
      eval t12 ((↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb)) φ := by
    have a2 : (↑Gb⁻¹ : R) * ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) * Gb =
        (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) := by
      simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
    rw [← eval_conj, conj_of_commute cb12, a2]
  have eR1 : (↑(Gd * Ga)⁻¹ : R) * eval t23 ((↑Ge⁻¹ : R) * t34 * Ge) φ * ↑(Gd * Ga) =
      eval ((↑Ga⁻¹ : R) * t23 * Ga) ((↑Gb⁻¹ : R) * t34 * Gb) φ := by
    have a2 : (↑(Gd * Ga)⁻¹ : R) * ((↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) =
        (↑Gb⁻¹ : R) * t34 * Gb := by
      rw [← F1, hP']; simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
    rw [← eval_conj, F2, a2]
  have eR2 : (↑Ga⁻¹ : R) * eval (t12 + t13) ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) φ * Ga =
      eval (t12 + (t13 + t23 - (↑Ga⁻¹ : R) * t23 * Ga))
        ((↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga +
          (↑Gb⁻¹ : R) * t34 * Gb) φ := by
    have a1 : (↑Ga⁻¹ : R) * (t12 + t13) * Ga = t12 + (t13 + t23 - (↑Ga⁻¹ : R) * t23 * Ga) := by
      have : (↑Ga⁻¹ : R) * (t12 + t13) * Ga =
          (↑Ga⁻¹ : R) * (t12 + t13 + t23) * Ga - (↑Ga⁻¹ : R) * t23 * Ga := by noncomm_ring
      rw [this, conj_of_commute ca3]; abel
    have a2 : (↑Ga⁻¹ : R) * ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) * Ga =
        (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga +
          (↑Gb⁻¹ : R) * t34 * Gb := by
      have b1 : (↑Ga⁻¹ : R) * ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) * Ga =
          (↑(Gd * Ga)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gd * Ga) -
            (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) := by
        simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
      have b2 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) =
          (↑(Gc * Gb)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gc * Gb) -
            (↑(Gc * Gb)⁻¹ : R) * t34 * ↑(Gc * Gb) := by noncomm_ring
      rw [b1, b2, F3, F2, F1]; abel
    rw [← eval_conj, a1, a2]
  simp only [actEval_eq]
  have lhs : (Gc : R) * eval t12 ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) φ *
      ((Gb : R) * eval (t13 + t23) ((↑Gb⁻¹ : R) * t34 * Gb) φ) =
      ↑(Gc * Gb) * ((↑Gb⁻¹ : R) * eval t12 ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) φ * Gb) *
        eval (t13 + t23) ((↑Gb⁻¹ : R) * t34 * Gb) φ := by
    simp only [Units.val_mul, mul_assoc, Units.mul_inv_cancel_left]
  have rhs : (Ge : R) * eval t23 ((↑Ge⁻¹ : R) * t34 * Ge) φ *
      ((Gd : R) * eval (t12 + t13) ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) φ) *
      ((Ga : R) * eval t12 ((↑Ga⁻¹ : R) * t23 * Ga) φ) =
      ↑(Ge * (Gd * Ga)) *
        ((↑(Gd * Ga)⁻¹ : R) * eval t23 ((↑Ge⁻¹ : R) * t34 * Ge) φ * ↑(Gd * Ga)) *
        ((↑Ga⁻¹ : R) * eval (t12 + t13) ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) φ * Ga) *
        eval t12 ((↑Ga⁻¹ : R) * t23 * Ga) φ := by
    simp only [mul_inv_rev, Units.val_mul, mul_assoc, Units.mul_inv_cancel_left]
  rw [lhs, rhs, eL1, eR1, eR2, ← hP']
  simp only [mul_sub, mul_assoc]

/-- The `{2, 3, 4}` coface of the transported family is a `DK3` family (values version). -/
theorem transported_d0V (γ : R → R → R) (hγ : CommProp γ) {t12 t13 t14 t23 t24 t34 : R}
    (hDK : DK4 t12 t13 t14 t23 t24 t34) (Ga Gb Gc Gd Ge : Rˣ)
    (ha : (Ga : R) = γ t12 t23) (hb : (Gb : R) = γ (t13 + t23) t34)
    (hc : (Gc : R) = γ t12 (t23 + t24)) (hd : (Gd : R) = γ (t12 + t13) (t24 + t34))
    (he : (Ge : R) = γ t23 t34)
    (hg : PentagonV γ t12 t13 t23 t24 t34) :
    let s := transported t12 t13 t23 t24 t34 Ga Gb Gc
    DK3 s.2.2.1 s.2.2.2.1 s.2.2.2.2 := by
  have hP' : Gc * Gb = Ge * (Gd * Ga) := by
    ext; simp only [Units.val_mul]; rw [ha, hb, hc, hd, he, ← mul_assoc]; exact hg
  have cc34 : Commute (Gc : R) t34 := hc ▸ hγ _ _ _ hDK.f12_34 hDK.n34_2.symm
  have cd23 : Commute (Gd : R) t23 := hd ▸ hγ _ _ _ hDK.n23_1.symm hDK.n23_4.symm
  have ce3 : Commute (Ge : R) (t23 + t24 + t34) := by
    rw [he]
    refine hγ _ _ _ ?_ ?_
    · rw [show t23 + t24 + t34 = t23 + (t24 + t34) by abel]
      exact (Commute.refl t23).add_right hDK.n23_4
    · rw [show t23 + t24 + t34 = (t23 + t24) + t34 by abel]
      exact hDK.n34_2.add_right (Commute.refl t34)
  have key := (dk3_twist hDK.d0 Ge ce3).unitsConj (Gd * Ga)
  have F1 : (↑(Gc * Gb)⁻¹ : R) * t34 * ↑(Gc * Gb) = (↑Gb⁻¹ : R) * t34 * Gb :=
    conj_mul_of_commute cc34
  have F2 : (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) = (↑Ga⁻¹ : R) * t23 * Ga :=
    conj_mul_of_commute cd23
  have F3 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gc * Gb) =
      (↑(Gd * Ga)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gd * Ga) := by
    rw [hP']; exact conj_mul_of_commute ce3
  have e3 : (↑(Gd * Ga)⁻¹ : R) * ((↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) =
      (↑Gb⁻¹ : R) * t34 * Gb := by
    rw [← F1, hP']; simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
  have e2 : (↑(Gd * Ga)⁻¹ : R) * (t24 + t34 - (↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) =
      (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga := by
    have b1 : (↑(Gd * Ga)⁻¹ : R) * (t24 + t34 - (↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) =
        (↑(Gd * Ga)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gd * Ga) -
          (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) -
          (↑(Gd * Ga)⁻¹ : R) * ((↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) := by noncomm_ring
    have b2 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) =
        (↑(Gc * Gb)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gc * Gb) -
          (↑(Gc * Gb)⁻¹ : R) * t34 * ↑(Gc * Gb) := by noncomm_ring
    rw [b1, b2, e3, F3, F2, F1]; abel
  rw [F2, e2, e3] at key
  exact key

/-- **The transported family is a `DK4` family, given the far relation** (values version). -/
theorem transported_dk4V (γ : R → R → R) (hγ : CommProp γ) {t12 t13 t14 t23 t24 t34 : R}
    (hDK : DK4 t12 t13 t14 t23 t24 t34) (Ga Gb Gc Gd Ge : Rˣ)
    (ha : (Ga : R) = γ t12 t23) (hb : (Gb : R) = γ (t13 + t23) t34)
    (hc : (Gc : R) = γ t12 (t23 + t24)) (hd : (Gd : R) = γ (t12 + t13) (t24 + t34))
    (he : (Ge : R) = γ t23 t34)
    (hg : PentagonV γ t12 t13 t23 t24 t34)
    (hfar : let s := transported t12 t13 t23 t24 t34 Ga Gb Gc
      Commute s.2.1 s.2.2.2.1) :
    let s := transported t12 t13 t23 t24 t34 Ga Gb Gc
    DK4 s.1 s.2.1 (transported14 t14 t24 t34 s) s.2.2.1 s.2.2.2.1 s.2.2.2.2 := by
  have d0 := transported_d0V γ hγ hDK Ga Gb Gc Gd Ge ha hb hc hd he hg
  simp only [transported, transported14] at hfar d0 ⊢
  obtain ⟨l0, l1, l2, l3, l4, l6, l8, l9, l10, l12⟩ := locals_of_dk4 hDK
  obtain ⟨c12, c13, c14, c23, c24, c34⟩ := commute_total hDK
  set c4 := t12 + t13 + t14 + t23 + t24 + t34 with hc4
  set s23 := (↑Ga⁻¹ : R) * t23 * Ga with hs23
  set s34 := (↑Gb⁻¹ : R) * t34 * Gb with hs34
  set w := (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) with hw
  have cG : ∀ (G : Rˣ) (a b : R), (G : R) = γ a b → Commute a c4 → Commute b c4 →
      Commute (G : R) c4 ∧ Commute (↑G⁻¹ : R) c4 := fun G a b h h1 h2 =>
    ⟨h ▸ hγ _ _ _ h1 h2, (h ▸ hγ _ _ _ h1 h2).units_inv_left⟩
  obtain ⟨ca, ca'⟩ := cG Ga _ _ ha c12 c23
  obtain ⟨cb, cb'⟩ := cG Gb _ _ hb (c13.add_left c23) c34
  obtain ⟨cc, cc'⟩ := cG Gc _ _ hc c12 (c23.add_left c24)
  have cs23 : Commute s23 c4 := (ca'.mul_left c23).mul_left ca
  have cs34 : Commute s34 c4 := (cb'.mul_left c34).mul_left cb
  have cw : Commute w c4 := by
    have : Commute (↑(Gc * Gb)⁻¹ : R) c4 := by
      simp only [mul_inv_rev, Units.val_mul]; exact cb'.mul_left cc'
    have h2 : Commute (↑(Gc * Gb) : R) c4 := by
      simp only [Units.val_mul]; exact cc.mul_left cb
    exact (this.mul_left (c23.add_left c24)).mul_left h2
  have cb12 : Commute (Gb : R) t12 := hb ▸ hγ _ _ _ hDK.n12_3.symm hDK.f12_34.symm
  have cad : Commute (Ga : R) (t14 + t24 + t34) := ha ▸ hγ _ _ _ l1 l4
  have ca3 : Commute (Ga : R) (t12 + t13 + t23) := by
    rw [ha]
    refine hγ _ _ _ ?_ ?_
    · rw [show t12 + t13 + t23 = t12 + (t13 + t23) by abel]
      exact (Commute.refl t12).add_right hDK.n12_3
    · rw [show t12 + t13 + t23 = (t12 + t13) + t23 by abel]
      exact hDK.n23_1.add_right (Commute.refl t23)
  have a1 : (↑Ga⁻¹ : R) * (t12 + t13) * Ga = t12 + (t13 + t23 - s23) := by
    have : (↑Ga⁻¹ : R) * (t12 + t13) * Ga =
        (↑Ga⁻¹ : R) * (t12 + t13 + t23) * Ga - (↑Ga⁻¹ : R) * t23 * Ga := by noncomm_ring
    rw [this, conj_of_commute ca3]; abel
  have Ed : t14 + t24 + t34 - (w - s23) - s34 + (w - s23) + s34 = t14 + t24 + t34 := by abel
  have E123 : t12 + (t13 + t23 - s23) + (t14 + t24 + t34 - (w - s23) - s34) =
      c4 - s23 - (w - s23 + s34) := by rw [hc4]; abel
  apply dk4_of_locals
  · rw [show t13 + t23 - s23 + s23 = t13 + t23 by abel]; exact l0
  · rw [Ed]; exact l1
  · rw [show t13 + t23 - s23 + s23 = t13 + t23 by abel, Ed]; exact l2
  · rw [← a1]; exact Commute.unitsConj Ga l3
  · rw [Ed]; have := Commute.unitsConj Ga l4; rwa [conj_of_commute cad] at this
  · exact d0.n12_3
  · rw [E123]
    have hx : Commute (w - s23 + s34) c4 := (cw.sub_left cs23).add_left cs34
    exact (hx.sub_right d0.n12_3.symm).sub_right (Commute.refl _)
  · exact d0.n23_1
  · rw [E123]
    rw [show c4 - s23 - (w - s23 + s34) = c4 - (s23 + (w - s23)) - s34 by abel]
    exact (cs34.sub_right d0.n23_1).sub_right (Commute.refl _)
  · have := Commute.unitsConj Gb l12; rwa [conj_of_commute cb12] at this
  · exact hfar

/-- **The far relation from t-compatibility** (values version). -/
theorem far_of_tcompatV (γ : R → R → R) (hγ : CommProp γ) {t12 t13 t14 t23 t24 t34 : R}
    (hDK : DK4 t12 t13 t14 t23 t24 t34) (Ga Gb Gc Gd Ge K H M W J L : Rˣ)
    (ha : (Ga : R) = γ t12 t23) (hb : (Gb : R) = γ (t13 + t23) t34)
    (hc : (Gc : R) = γ t12 (t23 + t24)) (hd : (Gd : R) = γ (t12 + t13) (t24 + t34))
    (he : (Ge : R) = γ t23 t34)
    (hK : (K : R) = γ t13 t23) (hH : (H : R) = γ t23 t24)
    (hM : (M : R) = γ t13 (t23 + t34)) (hW : (W : R) = γ (t12 + t23) t24)
    (hJ : (J : R) = γ t34 t23) (hL : (L : R) = γ t24 t23)
    (hg : PentagonV γ t12 t13 t23 t24 t34) (hg' : PentagonV γ t13 t12 t23 t34 t24)
    (hu1 : γ t34 t23 * γ t23 t34 = 1) (hu2 : γ t24 t23 * γ t23 t24 = 1)
    (hA : TCompat t13 t23 Ga K) (hB : TCompat t24 t23 J L) :
    let s := transported t12 t13 t23 t24 t34 Ga Gb Gc
    Commute s.2.1 s.2.2.2.1 := by
  simp only [transported]
  have eJ : J = Ge⁻¹ := eq_inv_of_mul_eq_one_left (Units.ext (by simp [hJ, he, hu1]))
  have eL : L = H⁻¹ := eq_inv_of_mul_eq_one_left (Units.ext (by simp [hL, hH, hu2]))
  subst eJ eL
  have P : Gc * Gb = Ge * (Gd * Ga) := Units.ext (by
    simp only [Units.val_mul, ha, hb, hc, hd, he]; rw [← mul_assoc]; exact hg)
  have P' : M * W = H * Gd * K := Units.ext (by
    simp only [Units.val_mul, hM, hW, hH, hd, hK]
    have := hg'; unfold PentagonV at this
    rw [add_comm t12 t13, add_comm t24 t34]; exact this)
  set Y := K⁻¹ * Ga with hY
  have S13 : t13 + t23 - (↑Ga⁻¹ : R) * t23 * Ga = (↑Y⁻¹ : R) * t13 * Y := by
    have e : (↑Y⁻¹ : R) * t13 * Y = (↑Ga⁻¹ : R) * ((K : R) * t13 * ↑K⁻¹) * Ga := by
      simp only [hY, mul_inv_rev, inv_inv, Units.val_mul]; noncomm_ring
    rw [e, hA, mul_sub, sub_mul, conj_conj]
  have cd : Commute (Gd : R) t23 := hd ▸ hγ _ _ _ hDK.n23_1.symm hDK.n23_4.symm
  have cM : Commute (M : R) t24 := hM ▸ hγ _ _ _ hDK.f13_24 hDK.n24_3.symm
  have cW : Commute (W : R) t13 := hW ▸ hγ _ _ _ hDK.n13_2.symm hDK.f13_24.symm
  have S24 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga =
      (↑Y⁻¹ : R) * ((↑W⁻¹ : R) * t24 * W) * Y := by
    have hB' : (↑Ge⁻¹ : R) * (t23 + t24) * Ge = (↑H⁻¹ : R) * t24 * H + t23 := by
      unfold TCompat at hB
      simp only [inv_inv] at hB
      rw [hB, add_comm t24 t23]; abel
    have e1 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) =
        (↑(Gd * Ga)⁻¹ : R) * ((↑Ge⁻¹ : R) * (t23 + t24) * Ge) * ↑(Gd * Ga) := by
      rw [P]; simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
    have e2 : (↑Ga⁻¹ : R) * t23 * Ga = (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) :=
      (conj_mul_of_commute cd).symm
    have e3 : (↑Y⁻¹ : R) * ((↑W⁻¹ : R) * t24 * W) * Y =
        (↑(H * Gd * Ga)⁻¹ : R) * t24 * ↑(H * Gd * Ga) := by
      have hZ : H * Gd * Ga = M * W * Y := by rw [P', hY]; simp [mul_assoc]
      rw [hZ, mul_assoc M W Y, conj_mul_of_commute cM]
      simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
    rw [e1, hB', e2, e3]
    simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
  rw [S13, S24]
  apply Commute.unitsConj
  have := Commute.unitsConj W hDK.f13_24
  rwa [show (↑W⁻¹ : R) * t13 * W = t13 from conj_of_commute cW] at this

/-! ### The hexagon -/

/-- The hexagon defect of `φ` (with exponential `E`) at a three-strand family. -/
noncomputable def hexDefect (φ E : FreeAlgebra ℚ (Fin 2)) (t12 t13 t23 : R) : R :=
  eval (t13 + t23) 0 E -
    eval t13 t12 φ * eval t13 0 E * eval t23 t13 φ * eval t23 0 E * eval t12 t23 φ

/-- **The hexagon under the action, with defect.** -/
theorem hexagon_actV (φ E : FreeAlgebra ℚ (Fin 2)) {t12 t13 t23 : R} (G1 G2 G3 : Rˣ)
    (hZ : G2 * G3 = G1⁻¹)
    (hsum : (G1 : R) * t13 * ↑G1⁻¹ + (↑G3⁻¹ : R) * t23 * G3 = t13 + t23) :
    eval (t13 + t23) 0 E -
      actEval φ t13 t12 G1 * eval t13 0 E * actEval φ t23 t13 G2 * eval t23 0 E *
        actEval φ t12 t23 G3 =
    hexDefect φ E t12 ((G1 : R) * t13 * ↑G1⁻¹) ((↑G3⁻¹ : R) * t23 * G3) := by
  have hG1 : G1 = (G2 * G3)⁻¹ := by rw [hZ, inv_inv]
  unfold hexDefect
  rw [hsum]
  congr 1
  clear hsum hZ
  subst hG1
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

/-- `G₁ t₁₃ G₁⁻¹ + G₃⁻¹ t₂₃ G₃ = t₁₃ + t₂₃` (values version of `transported3_sum`). -/
theorem transported3_sumV (γ : R → R → R) (hγ : CommProp γ) {t12 t13 t23 : R}
    (hDK : DK3 t12 t13 t23) (G1 G3 : Rˣ)
    (h3 : (G3 : R) = γ t12 t23) (htc : TCompat t13 t12 G3⁻¹ G1) :
    (G1 : R) * t13 * ↑G1⁻¹ + (↑G3⁻¹ : R) * t23 * G3 = t13 + t23 := by
  unfold TCompat at htc
  simp only [inv_inv] at htc
  have c12 : Commute t12 (t12 + t13 + t23) := by
    rw [add_assoc]; exact (Commute.refl t12).add_right hDK.n12_3
  have c23 : Commute t23 (t12 + t13 + t23) := hDK.n23_1.add_right (Commute.refl t23)
  have cG : Commute (G3 : R) (t12 + t13 + t23) := h3 ▸ hγ _ _ _ c12 c23
  rw [htc]
  have : (↑G3⁻¹ : R) * (t13 + t12) * G3 - t12 + (↑G3⁻¹ : R) * t23 * G3 =
      (↑G3⁻¹ : R) * (t12 + t13 + t23) * G3 - t12 := by noncomm_ring
  rw [this, conj_of_commute cG]; abel

/-- The transported three-strand family is `DK3` (values version of `transported3_dk3`). -/
theorem transported3_dk3V (γ : R → R → R) (hγ : CommProp γ) {t12 t13 t23 : R}
    (hDK : DK3 t12 t13 t23) (G1 G3 : Rˣ)
    (h1 : (G1 : R) = γ t13 t12) (h3 : (G3 : R) = γ t12 t23)
    (hsum : (G1 : R) * t13 * ↑G1⁻¹ + (↑G3⁻¹ : R) * t23 * G3 = t13 + t23) :
    DK3 t12 ((G1 : R) * t13 * ↑G1⁻¹) ((↑G3⁻¹ : R) * t23 * G3) := by
  set c := t12 + t13 + t23 with hc
  have c12 : Commute t12 c := by rw [hc, add_assoc]; exact (Commute.refl t12).add_right hDK.n12_3
  have c13 : Commute t13 c := by
    rw [hc, show t12 + t13 + t23 = t13 + (t12 + t23) by abel]
    exact (Commute.refl t13).add_right hDK.n13_2
  have c23 : Commute t23 c := hDK.n23_1.add_right (Commute.refl t23)
  have cG1 : Commute (G1 : R) c := h1 ▸ hγ _ _ _ c13 c12
  have cG3 : Commute (G3 : R) c := h3 ▸ hγ _ _ _ c12 c23
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

/-! ### (5.12) and (5.14) -/

/-- The (5.14) defect of `φ` at `(u, v, w)`, polynomial form. -/
noncomputable def tcDefect (φ : FreeAlgebra ℚ (Fin 2)) (u v w : R) : R :=
  eval v w φ * v * eval w v φ - (eval u w φ * (v + w) * eval w u φ - w)

/-- **(5.12) under the action, with defect.** With `U = γ(a,b)` and `U⁻¹ = γ(b,a)`, the (5.12)
defect of `φ ∘ γ` at `(a, b)` is the (5.12) defect of `φ` at `(U a U⁻¹, b)`. -/
theorem inv_actV (φ : FreeAlgebra ℚ (Fin 2)) {a b : R} (U : Rˣ) :
    actEval φ a b U * actEval φ b a U⁻¹ - 1 =
      eval ((U : R) * a * ↑U⁻¹) b φ * eval b ((U : R) * a * ↑U⁻¹) φ - 1 := by
  congr 1
  have key : (U : R) * eval ((↑U⁻¹ : R) * b * U) a φ * ↑U⁻¹ =
      eval b ((U : R) * a * ↑U⁻¹) φ := by
    have h := eval_conj U⁻¹ ((↑U⁻¹ : R) * b * U) a φ
    simp only [inv_inv] at h
    have hb : (U : R) * ((↑U⁻¹ : R) * b * U) * ↑U⁻¹ = b := by
      simp [mul_assoc]
    rw [hb] at h
    exact h.symm
  simp only [actEval, inv_inv]
  rw [← key]
  simp only [mul_assoc]

/-- **(5.14) under the action, with defect.** For a `DK3` family `(u, v, w)` and units
`Uu = γ(u, w)`, `Uv = γ(v, w)` whose inverses are `γ(w, u)`, `γ(w, v)`, if `γ` satisfies (5.14)
at `(u, v, w)` then the (5.14) defect of `φ ∘ γ` at `(u, v, w)` is the (5.14) defect of `φ` at
the `DK3` family `(Uu u Uu⁻¹, Uv v Uv⁻¹, w)`. -/
theorem tc_actV (φ : FreeAlgebra ℚ (Fin 2)) (γ : R → R → R) (hγ : CommProp γ) {u v w : R}
    (hDK : DK3 u v w) (Uu Uv : Rˣ) (hu : (Uu : R) = γ u w) (hu' : (↑Uu⁻¹ : R) = γ w u)
    (hv : (Uv : R) = γ v w) (hv' : (↑Uv⁻¹ : R) = γ w v)
    (h2 : γ v w * v * γ w v = γ u w * (v + w) * γ w u - w) :
    actEval φ v w Uv * v * actEval φ w v Uv⁻¹ -
        (actEval φ u w Uu * (v + w) * actEval φ w u Uu⁻¹ - w) =
      tcDefect φ ((Uu : R) * u * ↑Uu⁻¹) ((Uv : R) * v * ↑Uv⁻¹) w ∧
    DK3 ((Uu : R) * u * ↑Uu⁻¹) ((Uv : R) * v * ↑Uv⁻¹) w := by
  have hcomp : ∀ (U : Rˣ) (x y z : R), actEval φ x y U * z * actEval φ y x U⁻¹ =
      eval ((U : R) * x * ↑U⁻¹) y φ * ((U : R) * z * ↑U⁻¹) *
        eval y ((U : R) * x * ↑U⁻¹) φ := by
    intro U x y z
    have key : (U : R) * eval ((↑U⁻¹ : R) * y * U) x φ * ↑U⁻¹ =
        eval y ((U : R) * x * ↑U⁻¹) φ := by
      have h := eval_conj U⁻¹ ((↑U⁻¹ : R) * y * U) x φ
      simp only [inv_inv] at h
      have hb : (U : R) * ((↑U⁻¹ : R) * y * U) * ↑U⁻¹ = y := by simp [mul_assoc]
      rw [hb] at h
      exact h.symm
    rw [← key]
    simp only [actEval, inv_inv, mul_assoc, Units.inv_mul_cancel_left]
  set u' := (Uu : R) * u * ↑Uu⁻¹
  set v' := (Uv : R) * v * ↑Uv⁻¹
  have t2 : v' = (Uu : R) * (v + w) * ↑Uu⁻¹ - w := by
    simp only [v', hu, hu', hv, hv']; exact h2
  have hvw : (Uu : R) * (v + w) * ↑Uu⁻¹ = v' + w := by rw [t2]; abel
  set c := u + v + w with hc
  have cu : Commute u c := by
    rw [hc, add_assoc]; exact (Commute.refl u).add_right hDK.n12_3
  have cv : Commute v c := by
    rw [hc, show u + v + w = v + (u + w) by abel]; exact (Commute.refl v).add_right hDK.n13_2
  have cw : Commute w c := hDK.n23_1.add_right (Commute.refl w)
  have cGu : Commute (Uu : R) c := hu ▸ hγ _ _ _ cu cw
  have cGu' : Commute (↑Uu⁻¹ : R) c := cGu.units_inv_left
  have cGv : Commute (Uv : R) c := hv ▸ hγ _ _ _ cv cw
  have cGv' : Commute (↑Uv⁻¹ : R) c := cGv.units_inv_left
  have hcu : (Uu : R) * c * ↑Uu⁻¹ = c := by
    rw [cGu.eq, mul_assoc, Units.mul_inv, mul_one]
  have hu'c : u' = c - (v' + w) := by
    rw [← hvw, ← hcu]
    simp only [u', hc]; noncomm_ring
  have cu' : Commute u' c := (cGu.mul_left cu).mul_left cGu'
  have cv' : Commute v' c := (cGv.mul_left cv).mul_left cGv'
  have htot : u' + v' + w = c := by rw [hu'c]; abel
  have dk' : DK3 u' v' w := by
    apply dk3_of_total <;> rw [htot]
    · exact cu'
    · exact cv'
    · exact cw
  refine ⟨?_, dk'⟩
  rw [hcomp, hcomp, hvw]
  rfl

end Valued

end QOU.BraidsAndKnots.RationalAssociator
