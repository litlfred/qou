import QOU.Mass.QuantumSl2LinkDiagram
import QOU.Mass.QuantumSl2CrossingSymmetry

/-!
# Reidemeister invariance of the coloured `U_q(sl₂)` diagram model

For every colour `N = d + 1`, the model `rModel` of `QuantumSl2LinkDiagram` satisfies the local
identities of `Model.Invariant` with framing factor the twist `θ = s^{d(d+2)}`
(`rModel_invariant`). Two of the identities were proved there from the braid action (parallel R2,
R3) and from the right partial trace (R1 with the loop on the right). The other two need two
symmetries of the braiding `Ř`:

* **Reflection** (`rCheckMat_flip`): `Ř` is unchanged by `v_a ⊗ v_b ↦ v_{d−b} ⊗ v_{d−a}`. Under
  `v_j ↦ v_{d−j}` the matrix of `Eⁿ` becomes that of `Fⁿ` (`irrepE_pow_rev`), the Cartan weights
  change sign, and the two tensor legs are exchanged. This turns R1 with the loop on the left into
  R1 with the loop on the right (`rModel_r1_left`).
* **Crossing symmetry** (`rCheckInv_apply_eq`): from `rot Ř = Ř⁻¹` (`rotOp_rCheck_mul_rCheck`),
  `Ř⁻¹_{(y₁,y₂),(x₁,x₂)} = b_{x₁} a_{d−y₂} Ř_{(d−x₁,y₁),(x₂,d−y₂)}`, with `a`, `b` the cup and cap
  coefficients. Substituting it into the antiparallel bigon turns the sum into an entry of
  `Ř Ř⁻¹` or `Ř⁻¹ Ř`; the turn weight `K = q^H` is exactly what makes the leftover factor
  `K(i) a_{d−i} / a_i = (−1)^d` independent of the summation index (`rModel_r2anti`).

By `normValue_eq`, the writhe-normalised value of `rModel` is then an invariant of
`ReidemeisterEquiv`, and van der Veen's Whitehead formula holds for every code equivalent to the
closure of the Whitehead braid (`vdvWhiteheadLinkJones_eq_normValue_of_equiv`).

-- Ref: [turaev1988] Turaev, "The Yang–Baxter equation and invariants of links", Invent. Math. 92
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV (duality and the R-matrix)
-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1
-/

namespace QOU.Mass.QuantumSl2.LinkDiagram

open Matrix
open QOU.MathlibExt.PL.Diagram
open QOU.Mass.QuantumSl2.MarkovTrace
open QOU.Mass.QuantumSl2.Markov (rCheckInv rCheck_mul_inv rCheckInv_mul rCheckMat_apply)

variable {𝕜 : Type*} [Field 𝕜]

/-! ### Reflection of the weights -/

section Reflection

variable (q : 𝕜) (d : ℕ)

theorem irrepE_rev (i j : Fin (d + 1)) : irrepE q d i.rev j.rev = irrepF q d i j := by
  simp only [irrepE, irrepF, Fin.val_rev]
  have := i.isLt; have := j.isLt
  by_cases h : (i : ℕ) = j + 1
  · rw [if_pos (by omega), if_pos h]; congr 1; omega
  · rw [if_neg (by omega), if_neg h]

theorem irrepE_pow_submatrix_rev (n : ℕ) :
    (irrepE q d ^ n).submatrix Fin.revPerm Fin.revPerm = irrepF q d ^ n := by
  induction n with
  | zero => simp [Matrix.submatrix_one_equiv]
  | succ n ih =>
    rw [pow_succ, pow_succ, ← ih, ← Matrix.submatrix_mul_equiv (e₂ := Fin.revPerm)]
    congr 1
    ext i j
    exact irrepE_rev q d i j

theorem irrepE_pow_rev (n : ℕ) (i j : Fin (d + 1)) :
    (irrepE q d ^ n) i.rev j.rev = (irrepF q d ^ n) i j := by
  rw [← irrepE_pow_submatrix_rev q d n]; rfl

theorem irrepF_pow_rev (n : ℕ) (i j : Fin (d + 1)) :
    (irrepF q d ^ n) i.rev j.rev = (irrepE q d ^ n) i j := by
  rw [← irrepE_pow_rev, Fin.rev_rev, Fin.rev_rev]

theorem wt_rev (r : Fin (d + 1)) : wt d r.rev = -wt d r := by
  unfold wt; rw [Fin.val_rev]; have := r.isLt; push_cast [show (r : ℕ) ≤ d by omega]; omega

end Reflection

/-- The reflection `(a, b) ↦ (d − b, d − a)` of a pair of weights. -/
def flipE (d : ℕ) : (Fin (d + 1) × Fin (d + 1)) ≃ (Fin (d + 1) × Fin (d + 1)) where
  toFun x := (x.2.rev, x.1.rev)
  invFun x := (x.2.rev, x.1.rev)
  left_inv x := by simp
  right_inv x := by simp

theorem flipE_apply (d : ℕ) (x : Fin (d + 1) × Fin (d + 1)) : flipE d x = (x.2.rev, x.1.rev) := rfl

variable (s : 𝕜) (hs : s ≠ 0) (d : ℕ)

/-- **The braiding is invariant under the reflection** `v_a ⊗ v_b ↦ v_{d−b} ⊗ v_{d−a}`. -/
theorem rCheckMat_flip (y x : Fin (d + 1) × Fin (d + 1)) :
    rCheckMat s hs d d (flipE d y) (flipE d x) = rCheckMat s hs d d y x := by
  rw [rCheckMat_apply, rCheckMat_apply]
  obtain ⟨y1, y2⟩ := y
  obtain ⟨x1, x2⟩ := x
  simp only [flipE_apply, wt_rev, Prod.swap]
  congr 1
  · ring_nf
  · simp only [Rep.rSum, Matrix.sum_apply, Matrix.smul_apply, kroneckerMap_apply, smul_eq_mul]
    refine Finset.sum_congr rfl fun n _ => ?_
    change rcoef s n * ((irrepE (s ^ 2) d ^ n) y1.rev x2.rev * (irrepF (s ^ 2) d ^ n) y2.rev x1.rev)
      = rcoef s n * ((irrepE (s ^ 2) d ^ n) y2 x1 * (irrepF (s ^ 2) d ^ n) y1 x2)
    rw [irrepE_pow_rev, irrepF_pow_rev, mul_comm ((irrepF _ _ ^ n) _ _)]

theorem rCheckMat_submatrix_flip :
    (rCheckMat s hs d d).submatrix (flipE d) (flipE d) = rCheckMat s hs d d := by
  ext y x; exact rCheckMat_flip s hs d y x

theorem rCheckInv_submatrix_flip :
    (rCheckInv s hs d).submatrix (flipE d) (flipE d) = rCheckInv s hs d := by
  have h : (rCheckInv s hs d).submatrix (flipE d) (flipE d) * rCheckMat s hs d d = 1 := by
    conv_lhs => rw [← rCheckMat_submatrix_flip s hs d]
    rw [Matrix.submatrix_mul_equiv, rCheckInv_mul, Matrix.submatrix_one_equiv]
  calc (rCheckInv s hs d).submatrix (flipE d) (flipE d)
      = (rCheckInv s hs d).submatrix (flipE d) (flipE d) * (rCheckMat s hs d d * rCheckInv s hs d) := by
        rw [rCheck_mul_inv, Matrix.mul_one]
    _ = rCheckInv s hs d := by rw [← Matrix.mul_assoc, h, Matrix.one_mul]

theorem rCheckInv_flip (y x : Fin (d + 1) × Fin (d + 1)) :
    rCheckInv s hs d (flipE d y) (flipE d x) = rCheckInv s hs d y x := by
  conv_rhs => rw [← rCheckInv_submatrix_flip s hs d]
  rfl

theorem qWt_rev (r : Fin (d + 1)) : qWt s d r.rev = (qWt s d r)⁻¹ := by
  simp only [qWt, wt_rev, mul_neg, zpow_neg]

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (hint : ∀ k, 0 < k → k ≤ 2 * d → qint (s ^ 2) k ≠ 0)

include hq2 hint in
/-- **R1 with the loop traced on the left**, from the right-traced R1 and the reflection. -/
theorem rModel_r1_left (b : Bool) (x y : Fin (d + 1)) :
    ∑ i, kinkW (rModel s hs d) b b x y i * ((((rModel s hs d).K i ^ kinkTurn b b : 𝕜ˣ)) : 𝕜) =
      ((thetaU s hs d ^ signZ b : 𝕜ˣ) : 𝕜) * if x = y then 1 else 0 := by
  have h := rModel_r1_right s hs d hq2 hint b x.rev y.rev
  simp only [Fin.rev_inj] at h
  rw [← h, ← Equiv.sum_comp Fin.revPerm]
  refine Finset.sum_congr rfl fun i _ => ?_
  cases b
  · have hf := rCheckInv_flip s hs d (i.rev, x) (i.rev, y)
    simp only [flipE_apply, Fin.rev_rev] at hf
    simp only [Fin.revPerm_apply, kinkW_true, kinkW_false, Bool.not_false, kinkTurn, if_true,
      Bool.true_eq_false, if_false, zpow_one, zpow_neg_one, Units.val_inv_eq_inv_val, rModel_K,
      rModel_X_false, qWt_rev, inv_inv]
    rw [← hf]
  · have hf := rCheckMat_flip s hs d (i.rev, x) (i.rev, y)
    simp only [flipE_apply, Fin.rev_rev] at hf
    simp only [Fin.revPerm_apply, kinkW_true, kinkW_false, Bool.not_true, kinkTurn, if_true,
      Bool.false_eq_true, if_false, zpow_one, zpow_neg_one, Units.val_inv_eq_inv_val, rModel_K,
      rModel_X_true, qWt_rev, inv_inv]
    rw [← hf]

/-! ### Crossing symmetry in coordinates -/

section Crossing

/-- The cup coefficient `a_p` on `V_{d+1}`. -/
abbrev cupA (p : Fin (d + 1)) : 𝕜 := hwCoef (s ^ 2) d d d p

/-- The cap coefficient `b_p` on `V_{d+1}`. -/
abbrev capB (p : Fin (d + 1)) : 𝕜 := capCoefQ (s ^ 2) d p

include hint in
theorem hintD : ∀ i, 0 < i → i ≤ d → qint (s ^ 2) i ≠ 0 := fun i h1 h2 => hint i h1 (by omega)

include hs hint in
theorem capB_mul_cupA_rev (p : Fin (d + 1)) : capB s d p * cupA s d p.rev = 1 := by
  have h := snake_coef (s ^ 2) (pow_ne_zero 2 hs) d (hintD s d hint) p (by omega)
  unfold capB cupA
  rwa [show ((p.rev : Fin (d + 1)) : ℕ) = d - p by rw [Fin.val_rev]; omega]

include hs hint in
theorem capB_mul_cupA (p : Fin (d + 1)) : capB s d p * cupA s d p = (-1) ^ d * qWt s d p := by
  have ha := hwCoef_ne_zero (s ^ 2) (pow_ne_zero 2 hs) d (hintD s d hint) p (by omega)
  unfold capB cupA capCoefQ qWt wt
  rw [div_mul_cancel₀ _ ha, ← zpow_natCast s 2, ← zpow_mul]
  push_cast; ring_nf

include hq2 hint in
/-- **`rot Ř = Ř⁻¹`.** -/
theorem rotOp_rCheck_eq_inv : rotOp (s ^ 2) d (rCheckMat s hs d d) = rCheckInv s hs d := by
  have h := rotOp_rCheck_mul_rCheck s hs d hq2 (hintD s d hint)
  calc rotOp (s ^ 2) d (rCheckMat s hs d d)
      = rotOp (s ^ 2) d (rCheckMat s hs d d) * (rCheckMat s hs d d * rCheckInv s hs d) := by
        rw [rCheck_mul_inv, Matrix.mul_one]
    _ = rCheckInv s hs d := by rw [← Matrix.mul_assoc, h, Matrix.one_mul]

include hq2 hint in
/-- **Crossing symmetry in coordinates:** `Ř⁻¹_{(y₁,y₂),(x₁,x₂)} = b_{x₁} a_{d−y₂} Ř_{(d−x₁,y₁),(x₂,d−y₂)}`. -/
theorem rCheckInv_apply_eq (y1 y2 x1 x2 : Fin (d + 1)) :
    rCheckInv s hs d (y1, y2) (x1, x2) =
      capB s d x1 * rCheckMat s hs d d (x1.rev, y1) (x2, y2.rev) * cupA s d y2.rev := by
  rw [← rotOp_rCheck_eq_inv s hs d hq2 hint, rotOp_apply]
  have h1 := x1.isLt; have h2 := y2.isLt
  rw [Finset.sum_eq_single x1.rev]
  · rw [Finset.sum_eq_single y2.rev]
    · simp only [capVec, cupVec, hwVec, Fin.val_rev]
      rw [if_pos (by omega), if_pos (by omega)]
      rfl
    · intro γ _ hγ
      simp only [cupVec, hwVec]
      rw [if_neg, mul_zero]
      intro h; apply hγ; ext; rw [Fin.val_rev]; omega
    · simp
  · intro β _ hβ
    refine Finset.sum_eq_zero fun γ _ => ?_
    simp only [capVec]
    rw [if_neg, zero_mul, zero_mul]
    intro h; apply hβ; ext; rw [Fin.val_rev]; omega
  · simp

include hq2 hint in
/-- **Antiparallel R2** for every colour, from the crossing symmetry `rot Ř = Ř⁻¹`. -/
theorem rModel_r2anti (b : Bool) (a b' c e : Fin (d + 1)) :
    ∑ i, ∑ k, (rModel s hs d).X b k e a i * ((((rModel s hs d).K i ^ bigonTurn b : 𝕜ˣ)) : 𝕜) *
      (rModel s hs d).X (!b) c k i b' =
      if a = b' ∧ c = e then ((((rModel s hs d).K a ^ bigonTurn b : 𝕜ˣ)) : 𝕜) else 0 := by
  have hsq : ((-1 : 𝕜) ^ d) ^ 2 = 1 := by rw [← pow_mul, mul_comm, pow_mul, neg_one_sq, one_pow]
  have hA := capB_mul_cupA_rev s hs d hint
  have hB := capB_mul_cupA s hs d hint
  cases b
  · -- negative bigon: `Σ Ř⁻¹((k,a),(i,e)) K(i)⁻¹ Ř((i,c),(k,b'))`
    simp only [Bool.not_false, rModel_X_false, rModel_X_true, bigonTurn, Bool.false_eq_true,
      if_false, zpow_neg_one, Units.val_inv_eq_inv_val, rModel_K]
    have key : ∀ i k : Fin (d + 1),
        rCheckInv s hs d (k, a) (i, e) * (qWt s d i)⁻¹ * rCheckMat s hs d d (i, c) (k, b') =
          ((-1) ^ d * cupA s d a.rev * capB s d b'.rev) *
            (rCheckInv s hs d (c, b'.rev) (i.rev, k) * rCheckMat s hs d d (i.rev, k) (e, a.rev)) := by
      intro i k
      have hq : qWt s d i ≠ 0 := qWt_ne_zero s hs d i
      have hbi : capB s d i = (-1) ^ d * qWt s d i * capB s d i.rev := by
        have h1 := hA i.rev; have h2 := hB i
        rw [Fin.rev_rev] at h1
        linear_combination (-capB s d i) * h1 + capB s d i.rev * h2
      have hb' := hA b'.rev
      rw [Fin.rev_rev] at hb'
      rw [rCheckInv_apply_eq s hs d hq2 hint k a i e, rCheckInv_apply_eq s hs d hq2 hint c b'.rev i.rev k,
        Fin.rev_rev, Fin.rev_rev, hbi]
      have hq' : qWt s d i * (qWt s d i)⁻¹ = 1 := mul_inv_cancel₀ hq
      linear_combination ((-1) ^ d * capB s d i.rev * rCheckMat s hs d d (i.rev, k) (e, a.rev) *
        cupA s d a.rev * rCheckMat s hs d d (i, c) (k, b')) * hq' -
        ((-1) ^ d * capB s d i.rev * rCheckMat s hs d d (i.rev, k) (e, a.rev) *
        cupA s d a.rev * rCheckMat s hs d d (i, c) (k, b')) * hb'
    simp only [key, ← Finset.mul_sum]
    have hmul := congrFun (congrFun (rCheckInv_mul s hs d) (c, b'.rev)) (e, a.rev)
    rw [mul_apply, Fintype.sum_prod_type, ← Equiv.sum_comp Fin.revPerm] at hmul
    simp only [Fin.revPerm_apply] at hmul
    rw [hmul, one_apply]
    by_cases h : a = b' ∧ c = e
    · obtain ⟨rfl, rfl⟩ := h
      rw [if_pos rfl, if_pos ⟨rfl, rfl⟩, mul_one]
      have h2 := hB a.rev
      rw [qWt_rev] at h2
      linear_combination (-1) ^ d * h2 + (qWt s d a)⁻¹ * hsq
    · rw [if_neg, if_neg h, mul_zero]
      intro h'; apply h
      simp only [Prod.mk.injEq, Fin.rev_inj] at h'
      exact ⟨h'.2.symm, h'.1⟩
  · -- positive bigon: `Σ Ř((a,k),(e,i)) K(i) Ř⁻¹((c,i),(b',k))`
    simp only [Bool.not_true, rModel_X_false, rModel_X_true, bigonTurn, if_true, zpow_one,
      rModel_K]
    have key : ∀ i k : Fin (d + 1),
        rCheckMat s hs d d (a, k) (e, i) * qWt s d i * rCheckInv s hs d (c, i) (b', k) =
          ((-1) ^ d * capB s d b' * cupA s d a) *
            (rCheckMat s hs d d (b'.rev, c) (k, i.rev) * rCheckInv s hs d (k, i.rev) (a.rev, e)) := by
      intro i k
      have hw : qWt s d i * cupA s d i.rev = (-1) ^ d * cupA s d i := by
        linear_combination ((-1) ^ d * cupA s d i) * hA i - ((-1) ^ d * cupA s d i.rev) * hB i -
          (qWt s d i * cupA s d i.rev) * hsq
      have ha := hA a.rev
      rw [Fin.rev_rev] at ha
      rw [rCheckInv_apply_eq s hs d hq2 hint c i b' k, rCheckInv_apply_eq s hs d hq2 hint k i.rev a.rev e,
        Fin.rev_rev, Fin.rev_rev]
      linear_combination (rCheckMat s hs d d (a, k) (e, i) * capB s d b' *
          rCheckMat s hs d d (b'.rev, c) (k, i.rev)) * hw -
        ((-1) ^ d * capB s d b' * rCheckMat s hs d d (b'.rev, c) (k, i.rev) *
          rCheckMat s hs d d (a, k) (e, i) * cupA s d i) * ha
    simp only [key, ← Finset.mul_sum]
    have hmul := congrFun (congrFun (rCheck_mul_inv s hs d) (b'.rev, c)) (a.rev, e)
    rw [mul_apply, Fintype.sum_prod_type_right, ← Equiv.sum_comp Fin.revPerm] at hmul
    simp only [Fin.revPerm_apply] at hmul
    rw [hmul, one_apply]
    by_cases h : a = b' ∧ c = e
    · obtain ⟨rfl, rfl⟩ := h
      rw [if_pos rfl, if_pos ⟨rfl, rfl⟩, mul_one]
      linear_combination (-1) ^ d * hB a + qWt s d a * hsq
    · rw [if_neg, if_neg h, mul_zero]
      intro h'; apply h
      simp only [Prod.mk.injEq, Fin.rev_inj] at h'
      exact ⟨h'.1.symm, h'.2⟩

end Crossing

include hq2 hint in
/-- **The coloured model is Reidemeister invariant** for every colour `N = d + 1`, with framing
factor the twist `θ = s^{d(d+2)}`. -/
theorem rModel_invariant : (rModel s hs d).Invariant (thetaU s hs d) where
  r1 u b x y := by
    cases u <;> cases b
    · exact rModel_r1_left s hs d hq2 hint false x y
    · exact rModel_r1_right s hs d hq2 hint true x y
    · exact rModel_r1_right s hs d hq2 hint false x y
    · exact rModel_r1_left s hs d hq2 hint true x y
  r2par := rModel_r2par s hs d
  r2anti := rModel_r2anti s hs d hq2 hint
  r3 := rModel_r3 s hs d hq2 hint

/-! ### The Whitehead link as a link-level statement -/

section Whitehead

open QOU.Knot.FigureEightVolume

variable (σ : ℂ) (hσ : σ ≠ 0) (m : ℕ) (hq2' : σ ^ 2 - (σ ^ 2)⁻¹ ≠ 0)
  (hint' : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (σ ^ 2) i ≠ 0)

include hq2' hint' in
/-- **van der Veen's Whitehead formula is a link invariant of diagram codes.** For every code `D`
Reidemeister-equivalent to the closure of the Whitehead braid, and every colour `N = m + 1`,

    vdvWhiteheadLinkJones q N = [N]⁻¹ · θ^{−w(D)} · value (rModel) D. -/
theorem vdvWhiteheadLinkJones_eq_normValue_of_equiv {D : Bundled}
    (hD : ReidemeisterEquiv ⟨_, braidClosure whiteheadList⟩ D) :
    vdvWhiteheadLinkJones (σ ^ 2) (m + 1)
      = (qint (σ ^ 2) (m + 1))⁻¹ * normValue (rModel σ hσ m) (thetaU σ hσ m) D := by
  rw [vdvWhiteheadLinkJones_eq_normValue σ hσ m hq2' hint',
    normValue_eq (rModel_invariant σ hσ m hq2' (hint_le σ m hint')) hD]

end Whitehead

end QOU.Mass.QuantumSl2.LinkDiagram
