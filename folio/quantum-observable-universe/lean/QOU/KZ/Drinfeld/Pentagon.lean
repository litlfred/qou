import QOU.KZ.Drinfeld.Transport

/-!
# The pentagon for the associator of `D_ℏ`

Stage S2 of bean `qou-zoyv`. The matrix identity behind `MonoidalCategory.pentagon`:

  `(1 ⊗ α_{X,Y,Z}) · α_{W, X⊗Y, Z} · (α_{W,X,Y} ⊗ 1) = α_{W, X, Y⊗Z} · α_{W⊗X, Y, Z}`.

All reindexings are moved to the left (`reidx_ΦB`). Whiskering is handled by `kron_ΦB_one` and
`one_kron_ΦB`. What remains is `BlockResidues.pentagon_blocks` for the four leg blocks of
`((W ⊗ X) ⊗ Y) ⊗ Z`.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues QOU.KZ.DrinfeldAssociator Obj

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable (Ψ : Associator.{0}) {c : ℂ} (hc : Transcendental ℚ c)
include Ψ hc

variable {L L' : Type} [Fintype L] [DecidableEq L] [Fintype L'] [DecidableEq L']

theorem ΦB_mul_reidx (e : L ≃ L') (S T U : Finset L') :
    ΦB Ψ hc S T U * reidx e =
      reidx e * ΦB Ψ hc (S.map e.symm.toEmbedding) (T.map e.symm.toEmbedding)
        (U.map e.symm.toEmbedding) := by
  have h := reidx_ΦB Ψ hc e.symm S T U
  calc ΦB Ψ hc S T U * reidx e = reidx e * (reidx e.symm * ΦB Ψ hc S T U) * reidx e := by
        rw [← Matrix.mul_assoc, reidx_mul, Equiv.symm_trans_self, reidx_refl, Matrix.one_mul]
    _ = _ := by
        rw [h, Matrix.mul_assoc, Matrix.mul_assoc, reidx_mul, Equiv.self_trans_symm, reidx_refl,
          Matrix.mul_one]

omit Ψ hc in
theorem kron_mul_one {L L' L'' M : Type*} [Fintype L'] [DecidableEq L'] [Fintype M] [DecidableEq M]
    (A : Matrix (L → Fin 2) (L' → Fin 2) ℂ) (B : Matrix (L' → Fin 2) (L'' → Fin 2) ℂ) :
    kron (A * B) (1 : EndL M) = kron A (1 : EndL M) * kron B (1 : EndL M) := by
  rw [kron_mul, Matrix.one_mul]

omit Ψ hc in
theorem one_kron_mul {L L' L'' M : Type*} [Fintype L'] [DecidableEq L'] [Fintype M] [DecidableEq M]
    (A : Matrix (L → Fin 2) (L' → Fin 2) ℂ) (B : Matrix (L' → Fin 2) (L'' → Fin 2) ℂ) :
    kron (1 : EndL M) (A * B) = kron (1 : EndL M) A * kron (1 : EndL M) B := by
  rw [kron_mul, Matrix.one_mul]

section Pent

variable (W X Y Z : Obj)

/-- The four leg blocks of `((W ⊗ X) ⊗ Y) ⊗ Z`. -/
def P1 : Finset (Leaves (tensor (tensor (tensor W X) Y) Z)) :=
  univ.map ((Function.Embedding.inl.trans Function.Embedding.inl).trans Function.Embedding.inl)
def P2 : Finset (Leaves (tensor (tensor (tensor W X) Y) Z)) :=
  univ.map ((Function.Embedding.inr.trans Function.Embedding.inl).trans Function.Embedding.inl)
def P3 : Finset (Leaves (tensor (tensor (tensor W X) Y) Z)) :=
  univ.map (Function.Embedding.inr.trans Function.Embedding.inl)
def P4 : Finset (Leaves (tensor (tensor (tensor W X) Y) Z)) :=
  univ.map Function.Embedding.inr

omit Ψ hc in
theorem blk1 : (blkX W X Y).map (Function.Embedding.inl :
    Leaves (tensor (tensor W X) Y) ↪ Leaves (tensor (tensor (tensor W X) Y) Z)) = P1 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkX, P1, Function.Embedding.trans_apply]

omit Ψ hc in
theorem blk2 : (blkY W X Y).map (Function.Embedding.inl :
    Leaves (tensor (tensor W X) Y) ↪ Leaves (tensor (tensor (tensor W X) Y) Z)) = P2 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkY, P2, Function.Embedding.trans_apply]

omit Ψ hc in
theorem blk3 : (blkZ W X Y).map (Function.Embedding.inl :
    Leaves (tensor (tensor W X) Y) ↪ Leaves (tensor (tensor (tensor W X) Y) Z)) = P3 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkZ, P3, Function.Embedding.trans_apply]

/-- Legs of `(W ⊗ (X ⊗ Y)) ⊗ Z` from `((W ⊗ X) ⊗ Y) ⊗ Z`. -/
def e1 : Leaves (tensor (tensor (tensor W X) Y) Z) ≃ Leaves (tensor (tensor W (tensor X Y)) Z) :=
  Equiv.sumCongr (assocLegs W X Y) (Equiv.refl _)

omit Ψ hc in
theorem blk2X : (blkX W (tensor X Y) Z).map (e1 W X Y Z).symm.toEmbedding = P1 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkX, P1, e1, assocLegs]

omit Ψ hc in
theorem blk2Y : (blkY W (tensor X Y) Z).map (e1 W X Y Z).symm.toEmbedding =
    P2 W X Y Z ∪ P3 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkY, P2, P3, e1, assocLegs]

omit Ψ hc in
theorem blk2Z : (blkZ W (tensor X Y) Z).map (e1 W X Y Z).symm.toEmbedding = P4 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkZ, P4, e1, assocLegs]

/-- Legs of `W ⊗ ((X ⊗ Y) ⊗ Z)` from `((W ⊗ X) ⊗ Y) ⊗ Z`. -/
def e12 : Leaves (tensor (tensor (tensor W X) Y) Z) ≃ Leaves (tensor W (tensor (tensor X Y) Z)) :=
  (e1 W X Y Z).trans (assocLegs W (tensor X Y) Z)

omit Ψ hc in
theorem blk3X : ((blkX X Y Z).map (Function.Embedding.inr :
    Leaves (tensor (tensor X Y) Z) ↪ Leaves (tensor W (tensor (tensor X Y) Z)))).map
      (e12 W X Y Z).symm.toEmbedding = P2 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkX, P2, e12, e1, assocLegs]

omit Ψ hc in
theorem blk3Y : ((blkY X Y Z).map (Function.Embedding.inr :
    Leaves (tensor (tensor X Y) Z) ↪ Leaves (tensor W (tensor (tensor X Y) Z)))).map
      (e12 W X Y Z).symm.toEmbedding = P3 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkY, P3, e12, e1, assocLegs]

omit Ψ hc in
theorem blk3Z : ((blkZ X Y Z).map (Function.Embedding.inr :
    Leaves (tensor (tensor X Y) Z) ↪ Leaves (tensor W (tensor (tensor X Y) Z)))).map
      (e12 W X Y Z).symm.toEmbedding = P4 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkZ, P4, e12, e1, assocLegs]

omit Ψ hc in
theorem blk4X : blkX (tensor W X) Y Z = P1 W X Y Z ∪ P2 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkX, P1, P2]

omit Ψ hc in
theorem blk4Y : blkY (tensor W X) Y Z = P3 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkY, P3]

omit Ψ hc in
theorem blk4Z : blkZ (tensor W X) Y Z = P4 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkZ, P4]

omit Ψ hc in
theorem blk5X : (blkX W X (tensor Y Z)).map (assocLegs (tensor W X) Y Z).symm.toEmbedding =
    P1 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkX, P1, assocLegs]

omit Ψ hc in
theorem blk5Y : (blkY W X (tensor Y Z)).map (assocLegs (tensor W X) Y Z).symm.toEmbedding =
    P2 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkY, P2, assocLegs]

omit Ψ hc in
theorem blk5Z : (blkZ W X (tensor Y Z)).map (assocLegs (tensor W X) Y Z).symm.toEmbedding =
    P3 W X Y Z ∪ P4 W X Y Z := by
  ext k; rcases k with ((k | k) | k) | k <;> simp [blkZ, P3, P4, assocLegs]

omit Ψ hc in
theorem legs_pentagon :
    (e12 W X Y Z).trans (Equiv.sumCongr (Equiv.refl _) (assocLegs X Y Z)) =
      (assocLegs (tensor W X) Y Z).trans (assocLegs W X (tensor Y Z)) := by
  ext k; rcases k with ((k | k) | k) | k <;> rfl

omit Ψ hc in
theorem disjP {A B : Finset (Leaves (tensor (tensor (tensor W X) Y) Z))}
    (h : ∀ k, k ∈ A → k ∉ B) : Disjoint A B := Finset.disjoint_left.2 h

/-- The four blocks of `((W ⊗ X) ⊗ Y) ⊗ Z` as a `Blocks` structure. -/
def blocks4 : Blocks (Leaves (tensor (tensor (tensor W X) Y) Z)) where
  X1 := P1 W X Y Z
  X2 := P2 W X Y Z
  X3 := P3 W X Y Z
  X4 := P4 W X Y Z
  d12 := disjP W X Y Z (by intro k; rcases k with ((k | k) | k) | k <;> simp [P1, P2])
  d13 := disjP W X Y Z (by intro k; rcases k with ((k | k) | k) | k <;> simp [P1, P3])
  d14 := disjP W X Y Z (by intro k; rcases k with ((k | k) | k) | k <;> simp [P1, P4])
  d23 := disjP W X Y Z (by intro k; rcases k with ((k | k) | k) | k <;> simp [P2, P3])
  d24 := disjP W X Y Z (by intro k; rcases k with ((k | k) | k) | k <;> simp [P2, P4])
  d34 := disjP W X Y Z (by intro k; rcases k with ((k | k) | k) | k <;> simp [P3, P4])

/-- The block pentagon in terms of `ΦB`. -/
theorem pentagon_ΦB :
    ΦB Ψ hc (P2 W X Y Z) (P3 W X Y Z) (P4 W X Y Z) *
        ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z ∪ P3 W X Y Z) (P4 W X Y Z) *
        ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z) (P3 W X Y Z) =
      ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z) (P3 W X Y Z ∪ P4 W X Y Z) *
        ΦB Ψ hc (P1 W X Y Z ∪ P2 W X Y Z) (P3 W X Y Z) (P4 W X Y Z) := by
  have PB := Ψ.pentagon_blocksN (n := 2) hc (blocks4 W X Y Z)
  have q1 : ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z ∪ P3 W X Y Z) (P4 W X Y Z) =
      Ψ.ΦN ((blockRes 2 c (blocks4 W X Y Z)).t12 + (blockRes 2 c (blocks4 W X Y Z)).t13)
        ((blockRes 2 c (blocks4 W X Y Z)).t24 + (blockRes 2 c (blocks4 W X Y Z)).t34)
        (nr1213 hc _) (nr2434 hc _) :=
    Ψ.ΦN_congr
      (by
        show c • tB ℂ 2 (P1 W X Y Z) (P2 W X Y Z ∪ P3 W X Y Z) =
          c • tB ℂ 2 (P1 W X Y Z) (P2 W X Y Z) + c • tB ℂ 2 (P1 W X Y Z) (P3 W X Y Z)
        rw [tB_union_right (show Disjoint (P2 W X Y Z) (P3 W X Y Z) from (blocks4 W X Y Z).d23),
          smul_add])
      (by
        show c • tB ℂ 2 (P2 W X Y Z ∪ P3 W X Y Z) (P4 W X Y Z) =
          c • tB ℂ 2 (P2 W X Y Z) (P4 W X Y Z) + c • tB ℂ 2 (P3 W X Y Z) (P4 W X Y Z)
        rw [tB_union_left (show Disjoint (P2 W X Y Z) (P3 W X Y Z) from (blocks4 W X Y Z).d23),
          smul_add]) _ _ _ _
  have q2 : ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z) (P3 W X Y Z ∪ P4 W X Y Z) =
      Ψ.ΦN (blockRes 2 c (blocks4 W X Y Z)).t12
        ((blockRes 2 c (blocks4 W X Y Z)).t23 + (blockRes 2 c (blocks4 W X Y Z)).t24)
        (nr12 hc _) (nr2324 hc _) :=
    Ψ.ΦN_congr rfl
      (by
        show c • tB ℂ 2 (P2 W X Y Z) (P3 W X Y Z ∪ P4 W X Y Z) =
          c • tB ℂ 2 (P2 W X Y Z) (P3 W X Y Z) + c • tB ℂ 2 (P2 W X Y Z) (P4 W X Y Z)
        rw [tB_union_right (show Disjoint (P3 W X Y Z) (P4 W X Y Z) from (blocks4 W X Y Z).d34),
          smul_add]) _ _ _ _
  have q3 : ΦB Ψ hc (P1 W X Y Z ∪ P2 W X Y Z) (P3 W X Y Z) (P4 W X Y Z) =
      Ψ.ΦN ((blockRes 2 c (blocks4 W X Y Z)).t13 + (blockRes 2 c (blocks4 W X Y Z)).t23)
        (blockRes 2 c (blocks4 W X Y Z)).t34 (nr1323 hc _) (nr34 hc _) :=
    Ψ.ΦN_congr
      (by
        show c • tB ℂ 2 (P1 W X Y Z ∪ P2 W X Y Z) (P3 W X Y Z) =
          c • tB ℂ 2 (P1 W X Y Z) (P3 W X Y Z) + c • tB ℂ 2 (P2 W X Y Z) (P3 W X Y Z)
        rw [tB_union_left (show Disjoint (P1 W X Y Z) (P2 W X Y Z) from (blocks4 W X Y Z).d12),
          smul_add]) rfl _ _ _ _
  rw [q1, q2, q3]
  exact PB

/-- **The pentagon for `D_ℏ`** (matrix form, `ℏ` transcendental). -/
theorem pentagon_mat :
    kron (1 : EndL (Leaves W)) (αmat Ψ hc X Y Z) * (αmat Ψ hc W (tensor X Y) Z *
      kron (αmat Ψ hc W X Y) (1 : EndL (Leaves Z))) =
    αmat Ψ hc W X (tensor Y Z) * αmat Ψ hc (tensor W X) Y Z := by
  -- the three factors on the left
  have h1 : kron (αmat Ψ hc W X Y) (1 : EndL (Leaves Z)) =
      reidx (e1 W X Y Z) * ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z) (P3 W X Y Z) := by
    rw [αmat, kron_mul_one, kron_reidx_one, kron_ΦB_one, blk1, blk2, blk3]; rfl
  have h3 : kron (1 : EndL (Leaves W)) (αmat Ψ hc X Y Z) =
      reidx (Equiv.sumCongr (Equiv.refl _) (assocLegs X Y Z)) *
        ΦB Ψ hc ((blkX X Y Z).map Function.Embedding.inr) ((blkY X Y Z).map Function.Embedding.inr)
          ((blkZ X Y Z).map Function.Embedding.inr) := by
    rw [αmat, one_kron_mul, one_kron_reidx, one_kron_ΦB]
  have m2 : ΦB Ψ hc (blkX W (tensor X Y) Z) (blkY W (tensor X Y) Z) (blkZ W (tensor X Y) Z) *
      reidx (e1 W X Y Z) = reidx (e1 W X Y Z) *
        ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z ∪ P3 W X Y Z) (P4 W X Y Z) := by
    rw [ΦB_mul_reidx, ΦB_congr Ψ hc (blk2X W X Y Z) (blk2Y W X Y Z) (blk2Z W X Y Z)]
  have m3 : ΦB Ψ hc ((blkX X Y Z).map Function.Embedding.inr) ((blkY X Y Z).map Function.Embedding.inr)
      ((blkZ X Y Z).map Function.Embedding.inr) * reidx (e12 W X Y Z) =
      reidx (e12 W X Y Z) * ΦB Ψ hc (P2 W X Y Z) (P3 W X Y Z) (P4 W X Y Z) := by
    rw [ΦB_mul_reidx, ΦB_congr Ψ hc (blk3X W X Y Z) (blk3Y W X Y Z) (blk3Z W X Y Z)]
  have m5 : ΦB Ψ hc (blkX W X (tensor Y Z)) (blkY W X (tensor Y Z)) (blkZ W X (tensor Y Z)) *
      reidx (assocLegs (tensor W X) Y Z) = reidx (assocLegs (tensor W X) Y Z) *
        ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z) (P3 W X Y Z ∪ P4 W X Y Z) := by
    rw [ΦB_mul_reidx, ΦB_congr Ψ hc (blk5X W X Y Z) (blk5Y W X Y Z) (blk5Z W X Y Z)]
  have hL : kron (1 : EndL (Leaves W)) (αmat Ψ hc X Y Z) * (αmat Ψ hc W (tensor X Y) Z *
      kron (αmat Ψ hc W X Y) (1 : EndL (Leaves Z))) =
      reidx ((e12 W X Y Z).trans (Equiv.sumCongr (Equiv.refl _) (assocLegs X Y Z))) *
        (ΦB Ψ hc (P2 W X Y Z) (P3 W X Y Z) (P4 W X Y Z) *
          ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z ∪ P3 W X Y Z) (P4 W X Y Z) *
          ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z) (P3 W X Y Z)) := by
    rw [h3, h1, αmat]
    rw [Matrix.mul_assoc (reidx (assocLegs W (X.tensor Y) Z)),
      ← Matrix.mul_assoc (ΦB Ψ hc (blkX W (X.tensor Y) Z) (blkY W (X.tensor Y) Z) (blkZ W (X.tensor Y) Z))
        (reidx (e1 W X Y Z)), m2]
    rw [← Matrix.mul_assoc (reidx (assocLegs W (X.tensor Y) Z)),
      ← Matrix.mul_assoc (reidx (assocLegs W (X.tensor Y) Z)), reidx_mul]
    rw [show (e1 W X Y Z).trans (assocLegs W (X.tensor Y) Z) = e12 W X Y Z from rfl]
    rw [Matrix.mul_assoc (reidx ((Equiv.refl W.Leaves).sumCongr (assocLegs X Y Z))),
      Matrix.mul_assoc (reidx (e12 W X Y Z)),
      ← Matrix.mul_assoc (ΦB Ψ hc (map Function.Embedding.inr (blkX X Y Z))
        (map Function.Embedding.inr (blkY X Y Z)) (map Function.Embedding.inr (blkZ X Y Z)))
        (reidx (e12 W X Y Z)), m3, Matrix.mul_assoc (reidx (e12 W X Y Z)),
      ← Matrix.mul_assoc (reidx ((Equiv.refl W.Leaves).sumCongr (assocLegs X Y Z))), reidx_mul,
      Matrix.mul_assoc (ΦB Ψ hc (P2 W X Y Z) (P3 W X Y Z) (P4 W X Y Z))]
  have hR : αmat Ψ hc W X (tensor Y Z) * αmat Ψ hc (tensor W X) Y Z =
      reidx ((assocLegs (tensor W X) Y Z).trans (assocLegs W X (tensor Y Z))) *
        (ΦB Ψ hc (P1 W X Y Z) (P2 W X Y Z) (P3 W X Y Z ∪ P4 W X Y Z) *
          ΦB Ψ hc (P1 W X Y Z ∪ P2 W X Y Z) (P3 W X Y Z) (P4 W X Y Z)) := by
    rw [αmat, αmat, ΦB_congr Ψ hc (blk4X W X Y Z) (blk4Y W X Y Z) (blk4Z W X Y Z)]
    rw [Matrix.mul_assoc (reidx (assocLegs W X (Y.tensor Z))),
      ← Matrix.mul_assoc (ΦB Ψ hc (blkX W X (Y.tensor Z)) (blkY W X (Y.tensor Z)) (blkZ W X (Y.tensor Z)))
        (reidx (assocLegs (W.tensor X) Y Z)), m5, Matrix.mul_assoc (reidx (assocLegs (W.tensor X) Y Z)),
      ← Matrix.mul_assoc (reidx (assocLegs W X (Y.tensor Z))), reidx_mul]
  rw [hL, hR, legs_pentagon, pentagon_ΦB]

end Pent

end QOU.KZ.Drinfeld
