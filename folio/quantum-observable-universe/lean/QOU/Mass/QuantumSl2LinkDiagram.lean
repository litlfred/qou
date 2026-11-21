import QOU.MathlibExt.LinkDiagramClosure
import QOU.Knot.WhiteheadMarkovClosure

/-!
# The coloured `U_q(sl₂)` state sum on link diagram codes

For every colour `N = d + 1` the braiding `Ř` of `V_{d+1} ⊗ V_{d+1}` (`rCheckMat`) and its inverse
give a state-sum model `rModel` on diagram codes, with turn weight `K = q^H` (`qWt`). Its crossing
tensors are read so that the level matrix of a letter is the strand operator of the braid group
action (`levelMat_rModel_true`, `levelMat_rModel_false`). By `value_braidClosure`, the value of
the closure of a word is then the quantum trace of `QuantumSl2MarkovTrace`:

    value (rModel) (braidClosure w) = τ(β_w)                        (`value_rModel_braidClosure`).

For the Whitehead word this is the braid-closure trace of van der Veen's formula
(`value_rModel_whitehead`), and with the writhe `−1` of the closure code,

    vdvWhiteheadLinkJones q N = [N]⁻¹ · θ · value (rModel) (closure)  (`vdvWhiteheadLinkJones_eq_value`).

**Not done here.** Reidemeister invariance of `rModel` (`Model.Invariant`) for every `N`: the
parallel R2 and R3 identities follow from `Ř Ř⁻¹ = 1` and the braid relation, but R1 with the loop
traced on the left and the antiparallel R2 are new identities. Once they are proved,
`normValue_eq` turns the last formula into a statement about every code Reidemeister-equivalent to
the Whitehead closure.

-- Ref: [turaev1988] Turaev, "The Yang–Baxter equation and invariants of links", Invent. Math. 92
-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1
-/

namespace QOU.Mass.QuantumSl2.LinkDiagram

open Matrix
open QOU.MathlibExt.PL.Diagram
open QOU.Mass.QuantumSl2.BraidAction
open QOU.Mass.QuantumSl2.MarkovTrace
open QOU.Mass.QuantumSl2.Markov (rCheckInv rCheck_mul_inv theta)
open QOU.IwahoriHecke.TensorEmbed (coxA)
open QOU.IwahoriHecke.BraidGroup (BraidGroupN braidGen)

variable {𝕜 : Type*} [Field 𝕜] (s : 𝕜) (hs : s ≠ 0) (d : ℕ)

include hs in
theorem qWt_ne_zero (r : Fin (d + 1)) : qWt s d r ≠ 0 := zpow_ne_zero _ hs

/-- **The coloured `U_q(sl₂)` model.** A positive crossing reads `Ř` from `(oin, uin)` to
`(uout, oout)`, a negative one reads `Ř⁻¹` from `(uin, oin)` to `(oout, uout)`. -/
noncomputable def rModel : Model 𝕜 (Fin (d + 1)) where
  X b uin uout oin oout :=
    if b then rCheckMat s hs d d (oin, uin) (uout, oout)
    else rCheckInv s hs d (uin, oin) (oout, uout)
  K r := Units.mk0 (qWt s d r) (qWt_ne_zero s hs d r)
  base := 0

theorem levelMat_rModel_true {m : ℕ} (i : Fin m) :
    levelMat (rModel s hs d) (i, true) = strandMat (rCheckMat s hs d d) i := by
  ext a c
  simp [levelMat, strandMat, pembed_apply, rModel]

theorem levelMat_rModel_false {m : ℕ} (i : Fin m) :
    levelMat (rModel s hs d) (i, false) = strandMat (rCheckInv s hs d) i := by
  ext a c
  simp [levelMat, strandMat, pembed_apply, rModel]

/-- The braid of a word: `(i, true)` is `σᵢ`, `(i, false)` is `σᵢ⁻¹`. -/
def wordBraid {m : ℕ} (w : List (Fin m × Bool)) : BraidGroupN m :=
  (w.map fun x => if x.2 then braidGen (coxA m) x.1 else (braidGen (coxA m) x.1)⁻¹).prod

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (hint : ∀ k, 0 < k → k ≤ 2 * d → qint (s ^ 2) k ≠ 0)

include hq2 hint in
theorem levelMat_rModel {m : ℕ} (x : Fin m × Bool) :
    levelMat (rModel s hs d) x =
      ((rCheckRep s hs d hq2 hint m
          (if x.2 then braidGen (coxA m) x.1 else (braidGen (coxA m) x.1)⁻¹) :
        (Matrix (Fin (m + 1) → Fin (d + 1)) (Fin (m + 1) → Fin (d + 1)) 𝕜)ˣ) :
          Matrix (Fin (m + 1) → Fin (d + 1)) (Fin (m + 1) → Fin (d + 1)) 𝕜) := by
  obtain ⟨i, b⟩ := x
  cases b
  · rw [levelMat_rModel_false]
    exact (rCheckRep_braidGen_inv s hs d hq2 hint m i).symm
  · rw [levelMat_rModel_true]
    exact (rCheckRep_braidGen s hs d hq2 hint m i).symm

include hq2 hint in
theorem prod_levelMat_rModel {m : ℕ} (w : List (Fin m × Bool)) :
    (w.map (levelMat (rModel s hs d))).prod =
      ((rCheckRep s hs d hq2 hint m (wordBraid w) :
        (Matrix (Fin (m + 1) → Fin (d + 1)) (Fin (m + 1) → Fin (d + 1)) 𝕜)ˣ) :
          Matrix (Fin (m + 1) → Fin (d + 1)) (Fin (m + 1) → Fin (d + 1)) 𝕜) := by
  induction w with
  | nil => simp [wordBraid]
  | cons x w ih =>
      rw [List.map_cons, List.prod_cons, ih, levelMat_rModel s hs d hq2 hint x]
      simp only [wordBraid, List.map_cons, List.prod_cons, map_mul, Units.val_mul]

include hq2 hint in
/-- **The value of a braid closure is the quantum trace of the braid.** -/
theorem value_rModel_braidClosure {m : ℕ} (w : List (Fin m × Bool)) :
    value (rModel s hs d) (braidClosure w) = qtrace s hs d hq2 hint ⟨m, wordBraid w⟩ := by
  rw [value_braidClosure, prod_levelMat_rModel s hs d hq2 hint, qtrace, wtrace]
  refine Finset.sum_congr rfl fun a _ => ?_
  simp [siteWt, rModel]

/-! ### The Reidemeister identities that follow from the braid action -/

section Identities

open QOU.Mass.QuantumSl2.Markov (ptr ptr_rCheck ptr_rCheckInv rCheckInv_mul)

theorem rModel_X_true (uin uout oin oout : Fin (d + 1)) :
    (rModel s hs d).X true uin uout oin oout = rCheckMat s hs d d (oin, uin) (uout, oout) := rfl

theorem rModel_X_false (uin uout oin oout : Fin (d + 1)) :
    (rModel s hs d).X false uin uout oin oout = rCheckInv s hs d (uin, oin) (oout, uout) := rfl

theorem rModel_K (r : Fin (d + 1)) : ((rModel s hs d).K r : 𝕜) = qWt s d r := rfl

/-- **Parallel R2** for every colour, from `Ř Ř⁻¹ = 1 = Ř⁻¹ Ř`. -/
theorem rModel_r2par (b : Bool) (a b' c e : Fin (d + 1)) :
    ∑ i, ∑ j, (rModel s hs d).X b c j a i * (rModel s hs d).X (!b) j e i b' =
      if a = b' ∧ c = e then 1 else 0 := by
  cases b
  · have h := congrFun (congrFun (rCheckInv_mul s hs d) (c, a)) (e, b')
    rw [mul_apply, Fintype.sum_prod_type] at h
    simp only [Bool.not_false, rModel_X_false, rModel_X_true]
    rw [h, one_apply]
    simp [Prod.ext_iff, and_comm]
  · have h := congrFun (congrFun (rCheck_mul_inv s hs d) (a, c)) (b', e)
    rw [mul_apply, Fintype.sum_prod_type, Finset.sum_comm] at h
    simp only [Bool.not_true, rModel_X_false, rModel_X_true]
    rw [h, one_apply]
    simp [Prod.ext_iff]

include hq2 hint in
/-- **R3** for every colour, from the braid relation. -/
theorem rModel_r3 (a₀ a₂ b₀ b₂ c₀ c₂ : Fin (d + 1)) :
    ∑ i, ∑ j, ∑ k, (rModel s hs d).X true b₀ j a₀ i * (rModel s hs d).X true c₀ k i a₂ *
      (rModel s hs d).X true k c₂ j b₂ =
    ∑ i, ∑ j, ∑ k, (rModel s hs d).X true c₀ k b₀ j * (rModel s hs d).X true k c₂ a₀ i *
      (rModel s hs d).X true j b₂ i a₂ := by
  have h := congrFun (congrFun (QOU.Mass.QuantumSl2.rCheck_braid s hs hq2 d hint)
    ((a₀, b₀), c₀)) ((c₂, b₂), a₂)
  simp only [mul_apply, Fintype.sum_prod_type, QOU.Mass.QuantumSl2.leg12_apply,
    QOU.Mass.QuantumSl2.leg23_apply, one_apply, mul_ite, ite_mul, mul_one, mul_zero,
    zero_mul, Finset.sum_ite_eq, Finset.sum_ite_eq', Finset.mem_univ, if_true,
    Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_mul] at h
  simp only [rModel_X_true]
  rw [← h, Finset.sum_comm]
  exact Finset.sum_congr rfl fun j _ => Finset.sum_comm

include hq2 hint in
/-- R1 with the loop traced on the right (`ptr(Ř^{±1}) = θ^{±1}`). -/
theorem rModel_r1_right (b : Bool) (x y : Fin (d + 1)) :
    ∑ i, kinkW (rModel s hs d) (!b) b x y i *
        ((((rModel s hs d).K i ^ kinkTurn (!b) b : 𝕜ˣ)) : 𝕜) =
      ((thetaU s hs d ^ signZ b : 𝕜ˣ) : 𝕜) * if x = y then 1 else 0 := by
  cases b
  · have h := congrFun (congrFun (ptr_rCheckInv s hs d hq2 hint) x) y
    simp only [ptr, smul_apply, one_apply, smul_eq_mul] at h
    simp only [Bool.not_false, kinkW_true, rModel_X_false, kinkTurn, signZ]
    simp only [Bool.true_eq_false, Bool.false_eq_true, if_false, zpow_one, zpow_neg_one,
      Units.val_inv_eq_inv_val, thetaU, Units.val_mk0, rModel_K]
    rw [← h]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [qWt, mul_comm]
  · have h := congrFun (congrFun (ptr_rCheck s hs d hq2 hint) x) y
    simp only [ptr, smul_apply, one_apply, smul_eq_mul] at h
    simp only [Bool.not_true, kinkW_false, rModel_X_true, kinkTurn, signZ]
    simp only [Bool.false_eq_true, if_false, if_true, zpow_one, thetaU,
      Units.val_mk0, rModel_K]
    rw [← h]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [qWt, mul_comm]

end Identities

/-! ### Writhe -/

/-- The writhe of a closure code is the exponent sum of the word. -/
theorem writhe_braidClosure {m : ℕ} (w : List (Fin m × Bool)) :
    writhe (braidClosure w) = (w.map fun x => if x.2 then (1 : ℤ) else -1).sum := by
  have h : ∀ k : Fin w.length, (letterCrossing k (w.get k).1 (w.get k).2).pos = (w.get k).2 := by
    intro k
    unfold letterCrossing
    cases (w.get k).2 <;> rfl
  simp only [writhe, braidClosure, Multiset.map_map, Function.comp_def, Finset.sum_map_val, h]
  rw [← List.sum_ofFn]
  congr 1
  exact List.ofFn_getElem_eq_map w (fun x => if x.2 then (1 : ℤ) else -1)

/-! ### The Whitehead link -/

/-- The Whitehead braid `σ₁⁻² σ₂ σ₁⁻¹ σ₂` as a word. -/
def whiteheadList : List (Fin 2 × Bool) := [(0, false), (0, false), (1, true), (0, false), (1, true)]

theorem wordBraid_whiteheadList :
    wordBraid whiteheadList = QOU.Knot.FigureEightVolume.whiteheadWord := by
  simp [wordBraid, whiteheadList, QOU.Knot.FigureEightVolume.whiteheadWord, mul_assoc]

theorem writhe_braidClosure_whiteheadList : writhe (braidClosure whiteheadList) = -1 := by
  rw [writhe_braidClosure]; decide

section Whitehead

open QOU.Knot.FigureEightVolume

variable (σ : ℂ) (hσ : σ ≠ 0) (m : ℕ) (hq2' : σ ^ 2 - (σ ^ 2)⁻¹ ≠ 0)
  (hint' : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (σ ^ 2) i ≠ 0)

include hq2' hint' in
/-- **van der Veen's Whitehead formula is the normalised state sum of the closure code.** -/
theorem vdvWhiteheadLinkJones_eq_normValue :
    vdvWhiteheadLinkJones (σ ^ 2) (m + 1)
      = (qint (σ ^ 2) (m + 1))⁻¹ *
          normValue (rModel σ hσ m) (thetaU σ hσ m) ⟨_, braidClosure whiteheadList⟩ := by
  rw [vdvWhiteheadLinkJones_eq_jones σ hσ m hq2' hint', QOU.MathlibExt.MarkovMoves.normalise_apply,
    writhe_whiteheadWord,
    normValue, writhe_braidClosure_whiteheadList,
    value_rModel_braidClosure σ hσ m hq2' (hint_le σ m hint'), wordBraid_whiteheadList]
  simp

end Whitehead

end QOU.Mass.QuantumSl2.LinkDiagram
