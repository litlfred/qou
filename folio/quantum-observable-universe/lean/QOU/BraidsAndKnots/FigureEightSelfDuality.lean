/-
  Self-duality kills the imaginary face — the keystone CS(4_1)=0, formalized
  over a generic commutative ring with a bar-involution σ (NOT ℂ; §7c).

  Context (vpug / keystone). The QOU complex volume splits a substrate element
  V into a bar-EVEN (cosh / Vol / binding / Re) part and a bar-ODD (sinh /
  Chern–Simons / Q_β / Im) part — the archimedean (ℂ) instance being
  Re/Im under complex conjugation. The figure-eight 4_1 (the Higgs) is
  AMPHICHIRAL (self-dual: 4_1 = mirror 4_1), so its colored Jones is σ-fixed
  (J_N(q)=J_N(q^-1), verified exactly in figure_eight_aj_operator.py). The
  consequence — Im V(4_1) = CS(4_1) = 0, so the Higgs knot contributes ONLY the
  real (mass) face m_μ/m_e = Vol(4_1)/ℏ_q² — is here PROVED algebraically over
  any (R, σ): a σ-fixed element has zero bar-odd part.

  This is the (R,σ)-generalization the literature's ℂ-results need (owner's
  "not just ℂ"): bar-involution σ replaces complex conjugation; the elementary
  self-duality argument is ring algebra. The hard saddle asymptotics
  (Vol(4_1) limit) stay conditional — see QOU/Knot/FigureEightVolume.lean.

  Complements the bar-parity descent in
  mass-endomorphism/binding-qbeta-complex-volume.lean (invol_descent); the NEW
  content here is the self-dual ⇒ Im-vanishes theorem.

  -- Ref: [kashaev1997] https://doi.org/10.1007/BF01239527
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

namespace QOU.Knot.SelfDuality

variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- bar-EVEN part: `V + σV` (cosh / Vol / binding / Re face). -/
def barEven (V : R) : R := V + σ V

/-- bar-ODD part: `V − σV` (sinh / Chern–Simons / Q_β / Im face). -/
def barOdd (V : R) : R := V - σ V

/-- The two parities reconstruct `2V`. -/
theorem barEven_add_barOdd (V : R) : barEven σ V + barOdd σ V = 2 * V := by
  simp only [barEven, barOdd]; ring

/-- **Self-duality kills the imaginary face.** A σ-fixed (amphichiral /
    self-dual) element — the figure-eight 4_1 / Higgs — has zero bar-ODD part.
    This is CS(4_1) = 0 = Im V(4_1), proved over any `(R, σ)`. -/
theorem selfDual_barOdd_zero (V : R) (hV : σ V = V) : barOdd σ V = 0 := by
  simp only [barOdd, hV, sub_self]

/-- For a self-dual element only the bar-EVEN (Vol / mass) face survives:
    `barEven σ V = 2V`. -/
theorem selfDual_barEven_two (V : R) (hV : σ V = V) : barEven σ V = 2 * V := by
  simp only [barEven, hV]; ring

/-- **Recurrence descent (the c_k ladder).** A three-term recurrence
    `Vp = c·Vk − Vm` with a σ-fixed (bar-even) multiplier `c` descends to BOTH
    parity recurrences at once — the algebraic engine of the c_k ladder
    (bar-even binding `c₂=−8` and bar-odd Q_β `c₂=−1` from one relation). -/
theorem recurrence_descent {Vp Vk Vm c : R} (hc : σ c = c)
    (h : Vp = c * Vk - Vm) :
    barEven σ Vp = c * barEven σ Vk - barEven σ Vm ∧
    barOdd σ Vp = c * barOdd σ Vk - barOdd σ Vm := by
  have hσ : σ Vp = c * σ Vk - σ Vm := by
    rw [h, map_sub, map_mul, hc]
  refine ⟨?_, ?_⟩
  · simp only [barEven]; rw [hσ, h]; ring
  · simp only [barOdd]; rw [hσ, h]; ring

/-- **Keystone corollary.** For the self-dual Higgs knot, the complex volume is
    purely real: its bar-odd (CS / Q_β / Im) face is 0 and its bar-even
    (Vol / mass / Re) face is `2V`. Hence `Q_β` cannot be the figure-eight's own
    imaginary face — it must live in the many-body binding defect (see the
    CAL-123 reanalysis audit). -/
theorem higgs_complex_volume_real (V : R) (hSelfDual : σ V = V) :
    barOdd σ V = 0 ∧ barEven σ V = 2 * V :=
  ⟨selfDual_barOdd_zero σ V hSelfDual, selfDual_barEven_two σ V hSelfDual⟩

/-! ## §2. Explicit 3-Strand `4₁` Braid Word Mirror-Conjugation Amphichirality -/

/-- The canonical 3-strand Artin braid word `σ₁ σ₂⁻¹ σ₁ σ₂⁻¹` of the figure-eight knot `4₁`,
encoded by signed generator indices `[1, -2, 1, -2]` (`1 ↦ σ₁`, `-2 ↦ σ₂⁻¹`). -/
def figureEightBraidWord : List ℤ := [1, -2, 1, -2]

/-- The mirror braid word obtained by inverting every crossing sign (`σᵢ^ε ↦ σᵢ^{-ε}`). -/
def mirrorBraidWord (w : List ℤ) : List ℤ :=
  w.map Neg.neg

/-- The 3-strand diagram-flip involution `(1 ↔ 2, -1 ↔ -2)` corresponding to conjugation
by the half-twist `Δ₃ = σ₁ σ₂ σ₁` (`Δ₃ σ₁ Δ₃⁻¹ = σ₂`, `Δ₃ σ₂ Δ₃⁻¹ = σ₁`). -/
def flipThreeStrandGen (g : ℤ) : ℤ :=
  if g = 1 then 2
  else if g = -1 then -2
  else if g = 2 then 1
  else if g = -2 then -1
  else g

/-- Action of the 3-strand diagram-flip involution on a braid word. -/
def flipThreeStrandWord (w : List ℤ) : List ℤ :=
  w.map flipThreeStrandGen

/-- **Explicit 3-Strand `4₁` Braid Amphichirality Theorem:**
1. The mirror word `mirrorBraidWord figureEightBraidWord` is `[-1, 2, -1, 2]`.
2. Rotating `mirrorBraidWord figureEightBraidWord` cyclically by 1 step (Markov conjugation
   in the braid closure) yields `[2, -1, 2, -1]`, which is identically the diagram-flipped
   (`Δ₃`-conjugated) word `flipThreeStrandWord figureEightBraidWord`. -/
theorem figureEightBraidWord_mirror_rotate_eq_flip :
    mirrorBraidWord figureEightBraidWord = [-1, 2, -1, 2] ∧
    (mirrorBraidWord figureEightBraidWord).rotate 1 =
      flipThreeStrandWord figureEightBraidWord := by
  decide

/-! ## §3. Explicit `LaurentPolynomial ℤ` Bar-Involution (`q ↦ q⁻¹`) for `4₁` vs. `3₁` -/

open LaurentPolynomial

/-- The additive-group negation isomorphism `k ↦ -k` on `ℤ`, corresponding
to the multiplicative inversion `q^k ↦ q^{-k}` on Laurent monomials `T k`. -/
def negIntAddEquiv : ℤ ≃+ ℤ where
  toFun x := -x
  invFun x := -x
  left_inv x := neg_neg x
  right_inv x := neg_neg x
  map_add' x y := neg_add x y

/-- The bar-involution `q ↦ q⁻¹` on `LaurentPolynomial ℤ`, sending `T k ↦ T (-k)`. -/
noncomputable def laurentBar : LaurentPolynomial ℤ →+* LaurentPolynomial ℤ :=
  (AddMonoidAlgebra.domCongr ℤ ℤ negIntAddEquiv).toRingHom

@[simp]
theorem laurentBar_T (k : ℤ) :
    laurentBar (T k : LaurentPolynomial ℤ) = (T (-k) : LaurentPolynomial ℤ) := by
  unfold laurentBar T
  exact AddMonoidAlgebra.domCongr_single (R := ℤ) (A := ℤ) negIntAddEquiv k (1 : ℤ)

/-- Evaluating `T k : LaurentPolynomial ℤ` at exponent `m : ℤ` gives `if k = m then 1 else 0`. -/
theorem coeff_T (k m : ℤ) :
    (T k : LaurentPolynomial ℤ).coeff m = if k = m then 1 else 0 := by
  unfold T
  exact AddMonoidAlgebra.coeff_single_apply

/-- The Jones polynomial of the figure-eight knot `4₁` in `ℤ[q, q⁻¹]`:
`J(4₁; q) = q² - q + 1 - q⁻¹ + q⁻²`. -/
noncomputable def jonesFigureEight : LaurentPolynomial ℤ :=
  T 2 - T 1 + 1 - T (-1) + T (-2)

/-- The Jones polynomial of the right-handed trefoil knot `3₁` in `ℤ[q, q⁻¹]`:
`J(3₁; q) = q + q³ - q⁴`. -/
noncomputable def jonesTrefoil : LaurentPolynomial ℤ :=
  T 1 + T 3 - T 4

/-- **Exact Bar-Invariance of the Figure-Eight Jones Polynomial (`4₁` Amphichirality):**
`laurentBar jonesFigureEight = jonesFigureEight` (`J(4₁; q⁻¹) = J(4₁; q)`), so its bar-odd
part in `ℤ[q, q⁻¹]` vanishes identically. -/
theorem laurentBar_jonesFigureEight :
    laurentBar jonesFigureEight = jonesFigureEight ∧
    barOdd laurentBar jonesFigureEight = 0 := by
  have hfix : laurentBar jonesFigureEight = jonesFigureEight := by
    unfold jonesFigureEight
    have h1 : (1 : LaurentPolynomial ℤ) = T 0 := rfl
    rw [h1]
    simp only [map_add, map_sub, laurentBar_T, neg_zero]
    have h2 : (- -1 : ℤ) = 1 := rfl
    have h3 : (- -2 : ℤ) = 2 := rfl
    rw [h2, h3]
    ring
  exact ⟨hfix, selfDual_barOdd_zero laurentBar jonesFigureEight hfix⟩

/-- **Chirality Contrast for the Trefoil (`3₁` is NOT Bar-Invariant):**
`laurentBar jonesTrefoil ≠ jonesTrefoil` (`q⁻¹ + q⁻³ - q⁻⁴ ≠ q + q³ - q⁴`), so its
bar-odd part `barOdd laurentBar jonesTrefoil` is non-zero. -/
theorem laurentBar_jonesTrefoil_ne :
    laurentBar jonesTrefoil ≠ jonesTrefoil ∧
    barOdd laurentBar jonesTrefoil ≠ 0 := by
  have hne : laurentBar jonesTrefoil ≠ jonesTrefoil := by
    intro h
    have hcoeff : (laurentBar jonesTrefoil).coeff 1 = jonesTrefoil.coeff 1 :=
      congrArg (fun p : LaurentPolynomial ℤ => p.coeff 1) h
    have hL : (laurentBar jonesTrefoil).coeff 1 = 0 := by
      unfold jonesTrefoil
      rw [map_sub, map_add, laurentBar_T, laurentBar_T, laurentBar_T,
        AddMonoidAlgebra.coeff_sub, AddMonoidAlgebra.coeff_add,
        Finsupp.sub_apply, Finsupp.add_apply, coeff_T, coeff_T, coeff_T]
      decide
    have hR : jonesTrefoil.coeff 1 = 1 := by
      unfold jonesTrefoil
      rw [AddMonoidAlgebra.coeff_sub, AddMonoidAlgebra.coeff_add,
        Finsupp.sub_apply, Finsupp.add_apply, coeff_T, coeff_T, coeff_T]
      decide
    rw [hL, hR] at hcoeff
    exact zero_ne_one hcoeff
  refine ⟨hne, ?_⟩
  intro hodd
  unfold barOdd at hodd
  exact hne (sub_eq_zero.mp hodd).symm

/-! ## §4. Archimedean Complex Conjugation Reality Theorem (`ℂ`) -/

/-- **Archimedean Self-Duality Reality Theorem (`ℂ`):**
Under the complex conjugation bar-involution `starRingEnd ℂ : ℂ →+* ℂ`, a complex
volume / log-asymptotic invariant `V = Vol + i · CS ∈ ℂ` is fixed (`star V = V`, i.e.
the mirror invariant `V_mirror = star V` equals `V`) if and only if its imaginary
(Chern–Simons) face vanishes (`V.im = 0`), in which case `barOdd (starRingEnd ℂ) V = 0`
and `(barEven (starRingEnd ℂ) V).im = 0 ∧ (barEven (starRingEnd ℂ) V).re = 2 * V.re`. -/
theorem archimedean_selfDual_iff_im_eq_zero (V : ℂ) :
    (starRingEnd ℂ V = V ↔ V.im = 0) ∧
    (starRingEnd ℂ V = V →
      barOdd (starRingEnd ℂ) V = 0 ∧
      barEven (starRingEnd ℂ) V = 2 * (V.re : ℂ)) := by
  have hiff : starRingEnd ℂ V = V ↔ V.im = 0 := Complex.conj_eq_iff_im
  refine ⟨hiff, fun h => ⟨selfDual_barOdd_zero (starRingEnd ℂ) V h, ?_⟩⟩
  rw [selfDual_barEven_two (starRingEnd ℂ) V h]
  have hre : (V.re : ℂ) = V := Complex.conj_eq_iff_re.mp h
  rw [hre]

end QOU.Knot.SelfDuality
