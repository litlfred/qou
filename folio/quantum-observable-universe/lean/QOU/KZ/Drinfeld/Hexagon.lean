import QOU.KZ.Drinfeld.Braiding
import QOU.KZ.Drinfeld.Pentagon

/-!
# The hexagons of `D_ℏ`

Stage S3 of bean `qou-zoyv`. The block hexagon

  `Φ(t₂₃, t₁₃) e^{iπ t^{sl}_{1,23}} Φ(t₁₂, t₂₃) = e^{iπ t^{sl}_{13}} Φ(t₁₂, t₁₃) e^{iπ t^{sl}_{12}}`

(`hexagon_sl`) follows from `BlockResidues.hexagon_blocks` through
`KZHexagonCentral.hexagon_rearranged`; the scalar parts `½|S||T|` separating the `𝔤𝔩₂` and
`sl₂` residues are central and cancel. Pulled back along the leg bijections this gives
Mathlib's two hexagon axioms in matrix form. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S3)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory MonoidalCategory Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues
  QOU.KZ.DrinfeldAssociator Obj

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

section Block

variable {L : Type} [Fintype L] [DecidableEq L] (Ψ : Associator.{0}) {c : ℂ}
  (hc : Transcendental ℚ c)

/-- `Φ(ℏ t_{S,T}, ℏ t_{U,V})` on `V^{⊗L}`. -/
def Φt (S T U V : Finset L) : EndL L :=
  Ψ.ΦN (c • tB ℂ 2 S T) (c • tB ℂ 2 U V) (nonResonant_tB Ψ hc S T) (nonResonant_tB Ψ hc U V)

theorem ΦB_eq_Φt (S T U : Finset L) : ΦB Ψ hc S T U = Φt Ψ hc S T T U := rfl

theorem Φt_congr {S T U V S' T' U' V' : Finset L} (h1 : tB ℂ 2 S T = tB ℂ 2 S' T')
    (h2 : tB ℂ 2 U V = tB ℂ 2 U' V') : Φt Ψ hc S T U V = Φt Ψ hc S' T' U' V' :=
  Ψ.ΦN_congr (by rw [h1]) (by rw [h2]) _ _ _ _

omit [Fintype L] [DecidableEq L] in
theorem expi_eq_eπ {L : Type*} [Fintype L] [DecidableEq L] (M : EndL L) :
    expi M = KZHexagon.eπ (-M) := by
  unfold expi KZHexagon.eπ; rw [neg_smul_neg]

/-- The block hexagon with the `𝔤𝔩₂` residues. -/
theorem hexagon_gl {X1 X2 X3 : Finset L} (d12 : Disjoint X1 X2) (d13 : Disjoint X1 X3)
    (d23 : Disjoint X2 X3) :
    Φt Ψ hc X2 X3 X1 X3 * expi (c • tB ℂ 2 X1 X2 + c • tB ℂ 2 X1 X3) * Φt Ψ hc X1 X2 X2 X3 =
      expi (c • tB ℂ 2 X1 X3) * Φt Ψ hc X1 X2 X1 X3 * expi (c • tB ℂ 2 X1 X2) := by
  have nm := @not_mem_of_disjoint L
  have smc : ∀ {x y : Matrix (L → Fin 2) (L → Fin 2) ℂ}, Commute x y →
      Commute (c • x) (c • y) := fun h => (h.smul_left c).smul_right c
  have cA : Commute (c • tB ℂ 2 X1 X2) (c • tB ℂ 2 X2 X3 + c • tB ℂ 2 X1 X3) := by
    rw [← smul_add, add_comm, ← tB_union_left d12]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [ha, hb])
      (fun a ha b hb => by simp [nm d13 ha, nm d23 hb]))
  have cB : Commute (c • tB ℂ 2 X2 X3) (c • tB ℂ 2 X1 X2 + c • tB ℂ 2 X1 X3) := by
    rw [← smul_add, ← tB_union_right d23]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [nm d12.symm ha, nm d13.symm hb])
      (fun a ha b hb => by simp [ha, hb]))
  have cC : Commute (c • tB ℂ 2 X1 X3) (c • tB ℂ 2 X1 X2 + c • tB ℂ 2 X2 X3) := by
    rw [← smul_add, tB_comm X1 X2, ← tB_union_right d13]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [nm d12 ha, nm d23.symm hb])
      (fun a ha b hb => by simp [ha, hb]))
  rw [expi_eq_eπ, expi_eq_eπ, expi_eq_eπ]
  exact Ψ.hexagon_rearrangedN (c • tB ℂ 2 X1 X2) (c • tB ℂ 2 X2 X3)
    (c • tB ℂ 2 X1 X3) _ _ _
    (by rw [add_assoc]; exact ((Commute.refl _).add_right cA).symm)
    (by rw [add_comm (c • tB ℂ 2 X1 X2), add_assoc]; exact ((Commute.refl _).add_right cB).symm)
    (by rw [add_comm _ (c • tB ℂ 2 X1 X3)]; exact ((Commute.refl _).add_right cC).symm)
    (Ψ.hexagon_blocksN hc d12 d13 d23)

omit Ψ hc in
/-- `e^{iπ r}` as a scalar matrix. -/
theorem commute_expi_scalar (r : ℂ) (M : EndL L) : Commute (expi (r • (1 : EndL L))) M :=
  (commute_expi (commute_scalar r M).symm).symm

omit Ψ hc in
theorem expi_scalar_mul (r s : ℂ) :
    expi (r • (1 : EndL L)) * expi (s • (1 : EndL L)) = expi ((r + s) • (1 : EndL L)) := by
  rw [← expi_add ((commute_scalar r _)), add_smul]

omit Ψ hc in
/-- `e^{iπℏ t^{sl}} = e^{iπℏ t} · e^{−iπℏ|S||T|/2}`. -/
theorem expi_tsl {S T : Finset L} (h : Disjoint S T) :
    expi (c • tsl S T) = expi (c • tB ℂ 2 S T) *
      expi ((-(c * ((1 / 2 : ℂ) * (S.card * T.card : ℕ)))) • (1 : EndL L)) := by
  rw [← expi_add (commute_scalar _ _).symm, tB_eq_tsl h, smul_add, smul_smul, neg_smul,
    add_neg_cancel_right]

/-- **The block hexagon** with the `sl₂` braiding residues. -/
theorem hexagon_sl {X1 X2 X3 : Finset L} (d12 : Disjoint X1 X2) (d13 : Disjoint X1 X3)
    (d23 : Disjoint X2 X3) :
    Φt Ψ hc X2 X3 X1 X3 * expi (c • tsl X1 (X2 ∪ X3)) * Φt Ψ hc X1 X2 X2 X3 =
      expi (c • tsl X1 X3) * Φt Ψ hc X1 X2 X1 X3 * expi (c • tsl X1 X2) := by
  have d : Disjoint X1 (X2 ∪ X3) := Finset.disjoint_union_right.2 ⟨d12, d13⟩
  set z₂ := expi ((-(c * ((1 / 2 : ℂ) * (X1.card * X2.card : ℕ)))) • (1 : EndL L))
  set z₃ := expi ((-(c * ((1 / 2 : ℂ) * (X1.card * X3.card : ℕ)))) • (1 : EndL L))
  have hz : expi ((-(c * ((1 / 2 : ℂ) * (X1.card * (X2 ∪ X3).card : ℕ)))) • (1 : EndL L)) =
      z₂ * z₃ := by
    rw [expi_scalar_mul, Finset.card_union_of_disjoint d23]
    congr 2; push_cast; ring
  rw [expi_tsl d, expi_tsl d13, expi_tsl d12, tB_union_right d23, smul_add, hz]
  have H := hexagon_gl Ψ hc d12 d13 d23
  have c2 : ∀ M, Commute z₂ M := commute_expi_scalar _
  have c3 : ∀ M, Commute z₃ M := commute_expi_scalar _
  calc Φt Ψ hc X2 X3 X1 X3 * (expi (c • tB ℂ 2 X1 X2 + c • tB ℂ 2 X1 X3) * (z₂ * z₃)) *
        Φt Ψ hc X1 X2 X2 X3
      = Φt Ψ hc X2 X3 X1 X3 * expi (c • tB ℂ 2 X1 X2 + c • tB ℂ 2 X1 X3) * Φt Ψ hc X1 X2 X2 X3 *
          (z₂ * z₃) := by
        simp only [Matrix.mul_assoc]
        rw [← Matrix.mul_assoc z₂ z₃, ← ((c2 _).mul_left (c3 _)).eq]
    _ = expi (c • tB ℂ 2 X1 X3) * Φt Ψ hc X1 X2 X1 X3 * expi (c • tB ℂ 2 X1 X2) * (z₂ * z₃) := by
        rw [H]
    _ = expi (c • tB ℂ 2 X1 X3) * z₃ * Φt Ψ hc X1 X2 X1 X3 * (expi (c • tB ℂ 2 X1 X2) * z₂) := by
        simp only [Matrix.mul_assoc]
        rw [(c2 z₃).eq, ← Matrix.mul_assoc (expi (c • tB ℂ 2 X1 X2)) z₃ z₂,
          ← (c3 (expi (c • tB ℂ 2 X1 X2))).eq, Matrix.mul_assoc z₃,
          ← Matrix.mul_assoc (Φt Ψ hc X1 X2 X1 X3) z₃, ← (c3 (Φt Ψ hc X1 X2 X1 X3)).eq,
          Matrix.mul_assoc z₃]

omit [Fintype L] [DecidableEq L] in
theorem tsl_comm {L : Type*} [Fintype L] [DecidableEq L] {S T : Finset L} (h : Disjoint S T) : tsl S T = tsl T S := by
  have e1 := tB_eq_tsl h
  have e2 := tB_eq_tsl h.symm
  rw [tB_comm, e2, mul_comm T.card] at e1
  exact (add_right_cancel e1).symm

end Block

section Transport

variable {L L' : Type} [Fintype L] [DecidableEq L] [Fintype L'] [DecidableEq L']
  (Ψ : Associator.{0}) {c : ℂ} (hc : Transcendental ℚ c)

theorem reidx_blk (e : L ≃ L') (S : Finset L) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    reidx e * blk S a = blk (S.map e.toEmbedding) a * reidx e := by
  simp only [blk, Matrix.mul_sum, Matrix.sum_mul, reidx_leafOp, Finset.sum_map]
  rfl

theorem reidx_tsl (e : L ≃ L') (S T : Finset L) :
    reidx e * tsl S T = tsl (S.map e.toEmbedding) (T.map e.toEmbedding) * reidx e :=
  intertwine_tsl _ (fun a _ => reidx_blk e S a) (fun a _ => reidx_blk e T a)

theorem reidx_expi_tsl (e : L ≃ L') (S T : Finset L) :
    reidx e * expi (c • tsl S T) =
      expi (c • tsl (S.map e.toEmbedding) (T.map e.toEmbedding)) * reidx e := by
  unfold expi
  apply KZIntertwine.exp_intertwine
  rw [Matrix.mul_smul, Matrix.mul_smul, reidx_tsl, Matrix.smul_mul, Matrix.smul_mul]

theorem expi_tsl_mul_reidx (e : L ≃ L') (S T : Finset L') :
    expi (c • tsl S T) * reidx e =
      reidx e * expi (c • tsl (S.map e.symm.toEmbedding) (T.map e.symm.toEmbedding)) := by
  have h := reidx_expi_tsl (c := c) e.symm S T
  calc expi (c • tsl S T) * reidx e = reidx e * (reidx e.symm * expi (c • tsl S T)) * reidx e := by
        rw [← Matrix.mul_assoc, reidx_mul, Equiv.symm_trans_self, reidx_refl, Matrix.one_mul]
    _ = _ := by
        rw [h, Matrix.mul_assoc, Matrix.mul_assoc, reidx_mul, Equiv.self_trans_symm, reidx_refl,
          Matrix.mul_one]

include Ψ hc in
theorem reidx_Φt (e : L ≃ L') (S T U V : Finset L) :
    reidx e * Φt Ψ hc S T U V =
      Φt Ψ hc (S.map e.toEmbedding) (T.map e.toEmbedding) (U.map e.toEmbedding)
        (V.map e.toEmbedding) * reidx e :=
  Ψ.ΦN_intertwine _ _ _ _ (reidx e)
    (by rw [Matrix.mul_smul, Matrix.smul_mul, reidx_tB])
    (by rw [Matrix.mul_smul, Matrix.smul_mul, reidx_tB])
    _ _ _ _ (nonResonant_fromBlocks_tB Ψ hc _ _ _ _) (nonResonant_fromBlocks_tB Ψ hc _ _ _ _)

include Ψ hc in
theorem Φt_mul_reidx (e : L ≃ L') (S T U V : Finset L') :
    Φt Ψ hc S T U V * reidx e =
      reidx e * Φt Ψ hc (S.map e.symm.toEmbedding) (T.map e.symm.toEmbedding)
        (U.map e.symm.toEmbedding) (V.map e.symm.toEmbedding) := by
  have h := reidx_Φt Ψ hc e.symm S T U V
  calc Φt Ψ hc S T U V * reidx e = reidx e * (reidx e.symm * Φt Ψ hc S T U V) * reidx e := by
        rw [← Matrix.mul_assoc, reidx_mul, Equiv.symm_trans_self, reidx_refl, Matrix.one_mul]
    _ = _ := by
        rw [h, Matrix.mul_assoc, Matrix.mul_assoc, reidx_mul, Equiv.self_trans_symm, reidx_refl,
          Matrix.mul_one]

theorem kron_tsl_one (S T : Finset L) :
    kron (tsl S T) (1 : EndL L') =
      tsl (S.map Function.Embedding.inl) (T.map Function.Embedding.inl) := by
  simp only [tsl, blk_inl, kron_add_left, kron_smul_left, kron_mul_one]

theorem one_kron_tsl (S T : Finset L') :
    kron (1 : EndL L) (tsl S T) =
      tsl (S.map Function.Embedding.inr) (T.map Function.Embedding.inr) := by
  simp only [tsl, blk_inr, kron_add_right, kron_smul_right, one_kron_mul]

theorem kron_expi_one (M : EndL L) : kron (expi M) (1 : EndL L') = expi (kron M 1) := by
  have h := NormedSpace.map_exp ℂ (whL L L')
    (LinearMap.continuous_of_finiteDimensional (whL L L').toLinearMap)
    (((Real.pi : ℂ) * Complex.I) • M)
  unfold expi
  rw [← kron_smul_left]
  exact h

theorem one_kron_expi (M : EndL L') : kron (1 : EndL L) (expi M) = expi (kron 1 M) := by
  have h := NormedSpace.map_exp ℂ (whR L L')
    (LinearMap.continuous_of_finiteDimensional (whR L L').toLinearMap)
    (((Real.pi : ℂ) * Complex.I) • M)
  unfold expi
  rw [← kron_smul_right]
  exact h

end Transport

section Whiskered

variable (c : ℂ)

theorem kron_βmat_one (X Y : Obj) (M : Type) [Fintype M] [DecidableEq M] :
    kron (βmat c X Y) (1 : EndL M) =
      reidx (Equiv.sumCongr (swapLegs X Y) (Equiv.refl M)) *
        expi (c • tsl ((bL X Y).map Function.Embedding.inl) ((bR X Y).map Function.Embedding.inl)) := by
  rw [βmat, kron_mul_one, kron_reidx_one, kron_expi_one, kron_smul_left, kron_tsl_one]

theorem one_kron_βmat (X Y : Obj) (M : Type) [Fintype M] [DecidableEq M] :
    kron (1 : EndL M) (βmat c X Y) =
      reidx (Equiv.sumCongr (Equiv.refl M) (swapLegs X Y)) *
        expi (c • tsl ((bL X Y).map Function.Embedding.inr) ((bR X Y).map Function.Embedding.inr)) := by
  rw [βmat, one_kron_mul, one_kron_reidx, one_kron_expi, kron_smul_right, one_kron_tsl]

end Whiskered

section Forward

variable (X Y Z : Obj)

/-- The leg bijection `(X ⊗ Y) ⊗ Z ≃ (Y ⊗ Z) ⊗ X` along the top of the hexagon. -/
def eTop : Leaves (tensor (tensor X Y) Z) ≃ Leaves (tensor (tensor Y Z) X) :=
  (assocLegs X Y Z).trans (swapLegs X (tensor Y Z))

/-- The leg bijection `(X ⊗ Y) ⊗ Z ≃ (Y ⊗ X) ⊗ Z`. -/
def eA : Leaves (tensor (tensor X Y) Z) ≃ Leaves (tensor (tensor Y X) Z) :=
  Equiv.sumCongr (swapLegs X Y) (Equiv.refl _)

theorem fwd1 : (bL X (tensor Y Z)).map (assocLegs X Y Z).symm.toEmbedding = blkX X Y Z := by
  ext k; rcases k with (k | k) | k <;> simp [bL, blkX, assocLegs]

theorem fwd2 : (bR X (tensor Y Z)).map (assocLegs X Y Z).symm.toEmbedding =
    blkY X Y Z ∪ blkZ X Y Z := by
  ext k; rcases k with (k | k) | k <;> simp [bR, blkY, blkZ, assocLegs]

theorem fwd3X : (blkX Y Z X).map (eTop X Y Z).symm.toEmbedding = blkY X Y Z := by
  ext k; rcases k with (k | k) | k <;> simp [blkX, blkY, eTop, assocLegs, swapLegs]

theorem fwd3Y : (blkY Y Z X).map (eTop X Y Z).symm.toEmbedding = blkZ X Y Z := by
  ext k; rcases k with (k | k) | k <;> simp [blkY, blkZ, eTop, assocLegs, swapLegs]

theorem fwd3Z : (blkZ Y Z X).map (eTop X Y Z).symm.toEmbedding = blkX X Y Z := by
  ext k; rcases k with (k | k) | k <;> simp [blkZ, blkX, eTop, assocLegs, swapLegs]

theorem fwd4L : ((bL X Y).map (Function.Embedding.inl :
    Leaves (tensor X Y) ↪ Leaves (tensor X Y) ⊕ Leaves Z)) = blkX X Y Z := by
  rw [bL, Finset.map_map]; rfl

theorem fwd4R : ((bR X Y).map (Function.Embedding.inl :
    Leaves (tensor X Y) ↪ Leaves (tensor X Y) ⊕ Leaves Z)) = blkY X Y Z := by
  rw [bR, Finset.map_map]; rfl

theorem fwd5X : (blkX Y X Z).map (eA X Y Z).symm.toEmbedding = blkY X Y Z := by
  ext k; rcases k with (k | k) | k <;> simp [blkX, blkY, eA, swapLegs]

theorem fwd5Y : (blkY Y X Z).map (eA X Y Z).symm.toEmbedding = blkX X Y Z := by
  ext k; rcases k with (k | k) | k <;> simp [blkX, blkY, eA, swapLegs]

theorem fwd5Z : (blkZ Y X Z).map (eA X Y Z).symm.toEmbedding = blkZ X Y Z := by
  ext k; rcases k with (k | k) | k <;> simp [blkZ, eA, swapLegs]

theorem fwd6L : ((bL X Z).map (Function.Embedding.inr :
    Leaves (tensor X Z) ↪ Leaves Y ⊕ Leaves (tensor X Z))).map
      ((eA X Y Z).trans (assocLegs Y X Z)).symm.toEmbedding = blkX X Y Z := by
  ext k; rcases k with (k | k) | k <;> simp [bL, blkX, eA, swapLegs, assocLegs]

theorem fwd6R : ((bR X Z).map (Function.Embedding.inr :
    Leaves (tensor X Z) ↪ Leaves Y ⊕ Leaves (tensor X Z))).map
      ((eA X Y Z).trans (assocLegs Y X Z)).symm.toEmbedding = blkZ X Y Z := by
  ext k; rcases k with (k | k) | k <;> simp [bR, blkZ, eA, swapLegs, assocLegs]

theorem legs_hexagon_fwd : (eTop X Y Z).trans (assocLegs Y Z X) =
    ((eA X Y Z).trans (assocLegs Y X Z)).trans
      (Equiv.sumCongr (Equiv.refl _) (swapLegs X Z)) := by
  ext k; rcases k with (k | k) | k <;> rfl

theorem disj_blkXZ : Disjoint (blkX X Y Z) (blkZ X Y Z) := by
  rw [Finset.disjoint_left]; intro k; rcases k with (k | k) | k <;> simp [blkX, blkZ]

variable (Ψ : Associator.{0}) {c : ℂ} (hc : Transcendental ℚ c)

/-- **The forward hexagon for `D_ℏ`** (matrix form). -/
theorem hexagon_fwd_mat :
    αmat Ψ hc Y Z X * (βmat c X (tensor Y Z) * αmat Ψ hc X Y Z) =
      kron (1 : EndL (Leaves Y)) (βmat c X Z) *
        (αmat Ψ hc Y X Z * kron (βmat c X Y) (1 : EndL (Leaves Z))) := by
  have hL : αmat Ψ hc Y Z X * (βmat c X (tensor Y Z) * αmat Ψ hc X Y Z) =
      reidx ((eTop X Y Z).trans (assocLegs Y Z X)) *
        (Φt Ψ hc (blkY X Y Z) (blkZ X Y Z) (blkX X Y Z) (blkZ X Y Z) *
          expi (c • tsl (blkX X Y Z) (blkY X Y Z ∪ blkZ X Y Z)) *
          Φt Ψ hc (blkX X Y Z) (blkY X Y Z) (blkY X Y Z) (blkZ X Y Z)) := by
    rw [βmat, αmat, αmat]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (expi _) (reidx (assocLegs X Y Z)), expi_tsl_mul_reidx, fwd1, fwd2]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (reidx (swapLegs _ _)) (reidx (assocLegs X Y Z)), reidx_mul,
      show (assocLegs X Y Z).trans (swapLegs X (tensor Y Z)) = eTop X Y Z from rfl,
      ΦB_eq_Φt, ΦB_eq_Φt, ← Matrix.mul_assoc (Φt Ψ hc _ _ _ _) (reidx (eTop X Y Z)), Φt_mul_reidx,
      fwd3X, fwd3Y, fwd3Z]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (reidx (assocLegs Y Z X)) (reidx (eTop X Y Z)), reidx_mul,
      Φt_congr Ψ hc rfl (tB_comm (blkZ X Y Z) (blkX X Y Z))]
  have hR : kron (1 : EndL (Leaves Y)) (βmat c X Z) *
        (αmat Ψ hc Y X Z * kron (βmat c X Y) (1 : EndL (Leaves Z))) =
      reidx (((eA X Y Z).trans (assocLegs Y X Z)).trans
        (Equiv.sumCongr (Equiv.refl _) (swapLegs X Z))) *
        (expi (c • tsl (blkX X Y Z) (blkZ X Y Z)) *
          Φt Ψ hc (blkX X Y Z) (blkY X Y Z) (blkX X Y Z) (blkZ X Y Z) *
          expi (c • tsl (blkX X Y Z) (blkY X Y Z))) := by
    rw [kron_βmat_one, one_kron_βmat, fwd4L, fwd4R,
      show Equiv.sumCongr (swapLegs X Y) (Equiv.refl (Leaves Z)) = eA X Y Z from rfl, αmat,
      ΦB_eq_Φt]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (Φt Ψ hc _ _ _ _) (reidx (eA X Y Z)), Φt_mul_reidx, fwd5X, fwd5Y, fwd5Z]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (reidx (assocLegs Y X Z)) (reidx (eA X Y Z)), reidx_mul]
    rw [← Matrix.mul_assoc (expi _) (reidx ((eA X Y Z).trans (assocLegs Y X Z))),
      expi_tsl_mul_reidx, fwd6L, fwd6R]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (reidx (Equiv.sumCongr _ _)) (reidx ((eA X Y Z).trans _)), reidx_mul,
      Φt_congr Ψ hc (tB_comm (blkY X Y Z) (blkX X Y Z)) rfl]
  rw [hL, hR, legs_hexagon_fwd,
    hexagon_sl Ψ hc (disj_blkXY X Y Z) (disj_blkXZ X Y Z) (disj_blkYZ X Y Z)]

end Forward

section Reverse

variable (X Y Z : Obj)

/-- The leg blocks of `X ⊗ (Y ⊗ Z)`. -/
def R1 : Finset (Leaves (tensor X (tensor Y Z))) := bL X (tensor Y Z)
def R2 : Finset (Leaves (tensor X (tensor Y Z))) :=
  (bL Y Z).map (Function.Embedding.inr : Leaves (tensor Y Z) ↪ Leaves X ⊕ Leaves (tensor Y Z))
def R3 : Finset (Leaves (tensor X (tensor Y Z))) :=
  (bR Y Z).map (Function.Embedding.inr : Leaves (tensor Y Z) ↪ Leaves X ⊕ Leaves (tensor Y Z))

theorem dR12 : Disjoint (R1 X Y Z) (R2 X Y Z) := by
  rw [Finset.disjoint_left]; intro k; rcases k with k | (k | k) <;> simp [R1, R2, bL]
theorem dR13 : Disjoint (R1 X Y Z) (R3 X Y Z) := by
  rw [Finset.disjoint_left]; intro k; rcases k with k | (k | k) <;> simp [R1, R3, bL, bR]
theorem dR23 : Disjoint (R2 X Y Z) (R3 X Y Z) := by
  rw [Finset.disjoint_left]; intro k; rcases k with k | (k | k) <;> simp [R2, R3, bL, bR]

/-- The leg bijection along the top of the reverse hexagon. -/
def fRev : Leaves (tensor X (tensor Y Z)) ≃ Leaves (tensor (tensor Z X) Y) :=
  (((assocLegs X Y Z).symm.trans (swapLegs (tensor X Y) Z))).trans (assocLegs Z X Y).symm

/-- `X ⊗ (Y ⊗ Z) ≃ X ⊗ (Z ⊗ Y) ≃ (X ⊗ Z) ⊗ Y`. -/
def gRev : Leaves (tensor X (tensor Y Z)) ≃ Leaves (tensor (tensor X Z) Y) :=
  (Equiv.sumCongr (Equiv.refl _) (swapLegs Y Z)).trans (assocLegs X Z Y).symm

theorem rv1X : (blkX X Y Z).map (assocLegs X Y Z).toEmbedding = R1 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [blkX, R1, bL, assocLegs]
theorem rv1Y : (blkY X Y Z).map (assocLegs X Y Z).toEmbedding = R2 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [blkY, R2, bL, assocLegs]
theorem rv1Z : (blkZ X Y Z).map (assocLegs X Y Z).toEmbedding = R3 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [blkZ, R3, bR, assocLegs]

theorem rv2L : (bL (tensor X Y) Z).map (assocLegs X Y Z).toEmbedding = R1 X Y Z ∪ R2 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [R1, R2, bL, assocLegs]
theorem rv2R : (bR (tensor X Y) Z).map (assocLegs X Y Z).toEmbedding = R3 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [R3, bR, assocLegs]

theorem rv3X : (blkX Z X Y).map (fRev X Y Z).symm.toEmbedding = R3 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [blkX, R3, bR, fRev, assocLegs, swapLegs]
theorem rv3Y : (blkY Z X Y).map (fRev X Y Z).symm.toEmbedding = R1 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [blkY, R1, bL, fRev, assocLegs, swapLegs]
theorem rv3Z : (blkZ Z X Y).map (fRev X Y Z).symm.toEmbedding = R2 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [blkZ, R2, bL, fRev, assocLegs, swapLegs]

theorem rv4X : (blkX X Z Y).map (gRev X Y Z).symm.toEmbedding = R1 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [blkX, R1, bL, gRev, assocLegs, swapLegs]
theorem rv4Y : (blkY X Z Y).map (gRev X Y Z).symm.toEmbedding = R3 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [blkY, R3, bR, gRev, assocLegs, swapLegs]
theorem rv4Z : (blkZ X Z Y).map (gRev X Y Z).symm.toEmbedding = R2 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [blkZ, R2, bL, gRev, assocLegs, swapLegs]

theorem rv5L : ((bL X Z).map (Function.Embedding.inl :
    Leaves (tensor X Z) ↪ Leaves (tensor X Z) ⊕ Leaves Y)).map
      (gRev X Y Z).symm.toEmbedding = R1 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [bL, R1, gRev, assocLegs, swapLegs]
theorem rv5R : ((bR X Z).map (Function.Embedding.inl :
    Leaves (tensor X Z) ↪ Leaves (tensor X Z) ⊕ Leaves Y)).map
      (gRev X Y Z).symm.toEmbedding = R3 X Y Z := by
  ext k; rcases k with k | (k | k) <;> simp [bR, R3, gRev, assocLegs, swapLegs]

theorem legs_hexagon_rev : fRev X Y Z =
    (gRev X Y Z).trans (Equiv.sumCongr (swapLegs X Z) (Equiv.refl _)) := by
  ext k; rcases k with k | (k | k) <;> rfl

variable (Ψ : Associator.{0}) {c : ℂ} (hc : Transcendental ℚ c)

theorem αinv_eq (X Y Z : Obj) : αinv Ψ hc X Y Z =
    Φt Ψ hc (blkY X Y Z) (blkZ X Y Z) (blkX X Y Z) (blkY X Y Z) * reidx (assocLegs X Y Z).symm :=
  rfl

/-- **The reverse hexagon for `D_ℏ`** (matrix form). -/
theorem hexagon_rev_mat :
    αinv Ψ hc Z X Y * (βmat c (tensor X Y) Z * αinv Ψ hc X Y Z) =
      kron (βmat c X Z) (1 : EndL (Leaves Y)) *
        (αinv Ψ hc X Z Y * kron (1 : EndL (Leaves X)) (βmat c Y Z)) := by
  have hL : αinv Ψ hc Z X Y * (βmat c (tensor X Y) Z * αinv Ψ hc X Y Z) =
      reidx (fRev X Y Z) *
        (Φt Ψ hc (R1 X Y Z) (R2 X Y Z) (R3 X Y Z) (R1 X Y Z) *
          expi (c • tsl (R1 X Y Z ∪ R2 X Y Z) (R3 X Y Z)) *
          Φt Ψ hc (R2 X Y Z) (R3 X Y Z) (R1 X Y Z) (R2 X Y Z)) := by
    rw [αinv_eq, αinv_eq, βmat]
    simp only [Matrix.mul_assoc]
    rw [Φt_mul_reidx, Equiv.symm_symm, rv1X, rv1Y, rv1Z]
    rw [← Matrix.mul_assoc (expi _) (reidx (assocLegs X Y Z).symm), expi_tsl_mul_reidx,
      Equiv.symm_symm, rv2L, rv2R]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (reidx (swapLegs _ _)) (reidx (assocLegs X Y Z).symm), reidx_mul]
    rw [← Matrix.mul_assoc (reidx (assocLegs Z X Y).symm) (reidx _), reidx_mul,
      show ((assocLegs X Y Z).symm.trans (swapLegs (tensor X Y) Z)).trans
        (assocLegs Z X Y).symm = fRev X Y Z from rfl]
    rw [← Matrix.mul_assoc (Φt Ψ hc _ _ _ _) (reidx (fRev X Y Z)), Φt_mul_reidx, rv3X, rv3Y, rv3Z]
    simp only [Matrix.mul_assoc]
  have hR : kron (βmat c X Z) (1 : EndL (Leaves Y)) *
        (αinv Ψ hc X Z Y * kron (1 : EndL (Leaves X)) (βmat c Y Z)) =
      reidx ((gRev X Y Z).trans (Equiv.sumCongr (swapLegs X Z) (Equiv.refl _))) *
        (expi (c • tsl (R1 X Y Z) (R3 X Y Z)) *
          Φt Ψ hc (R3 X Y Z) (R2 X Y Z) (R1 X Y Z) (R3 X Y Z) *
          expi (c • tsl (R2 X Y Z) (R3 X Y Z))) := by
    rw [kron_βmat_one, one_kron_βmat, αinv_eq]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (reidx (assocLegs X Z Y).symm) (reidx _), reidx_mul,
      show (Equiv.sumCongr (Equiv.refl (Leaves X)) (swapLegs Y Z)).trans (assocLegs X Z Y).symm =
        gRev X Y Z from rfl]
    rw [← Matrix.mul_assoc (Φt Ψ hc _ _ _ _) (reidx (gRev X Y Z)), Φt_mul_reidx, rv4X, rv4Y, rv4Z]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (expi _) (reidx (gRev X Y Z)), expi_tsl_mul_reidx, rv5L, rv5R]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (reidx (Equiv.sumCongr _ _)) (reidx (gRev X Y Z)), reidx_mul]
    rfl
  have H := hexagon_sl Ψ hc (dR23 X Y Z).symm (dR13 X Y Z).symm (dR12 X Y Z).symm
  have d : Disjoint (R3 X Y Z) (R2 X Y Z ∪ R1 X Y Z) :=
    Finset.disjoint_union_right.2 ⟨(dR23 X Y Z).symm, (dR13 X Y Z).symm⟩
  have h1 : Φt Ψ hc (R2 X Y Z) (R1 X Y Z) (R3 X Y Z) (R1 X Y Z) =
      Φt Ψ hc (R1 X Y Z) (R2 X Y Z) (R3 X Y Z) (R1 X Y Z) := Φt_congr Ψ hc (tB_comm _ _) rfl
  have h2 : Φt Ψ hc (R3 X Y Z) (R2 X Y Z) (R2 X Y Z) (R1 X Y Z) =
      Φt Ψ hc (R2 X Y Z) (R3 X Y Z) (R1 X Y Z) (R2 X Y Z) :=
    Φt_congr Ψ hc (tB_comm _ _) (tB_comm _ _)
  have h3 : Φt Ψ hc (R3 X Y Z) (R2 X Y Z) (R3 X Y Z) (R1 X Y Z) =
      Φt Ψ hc (R3 X Y Z) (R2 X Y Z) (R1 X Y Z) (R3 X Y Z) := Φt_congr Ψ hc rfl (tB_comm _ _)
  rw [h1, h2, h3, tsl_comm d, Finset.union_comm, tsl_comm (dR13 X Y Z).symm,
    tsl_comm (dR23 X Y Z).symm] at H
  rw [hL, hR, legs_hexagon_rev, H]

end Reverse

end QOU.KZ.Drinfeld
