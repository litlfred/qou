import QOU.KZ.Drinfeld.Hexagon
import QOU.KZ.Drinfeld.Braided
import QOU.MathlibExt.Ribbon

/-!
# The twist of `D_ℏ`: `θ_X = exp(iπℏ Ω_X)`, `Ω_X` the `sl₂` Casimir

Stage S5 of bean `qou-zoyv`. `Ω_X = tsl(X, X)` is the Casimir of the diagonal `sl₂`-action on
`V^{⊗X}`. It commutes with every equivariant map (naturality), and
`Ω_{X ⊗ Y} = Ω_X + Ω_Y + 2 t^{sl}_{X,Y}` with commuting summands, while
`β_{Y,X} β_{X,Y} = exp(2πiℏ t^{sl}_{X,Y})`; together these are the balancing axiom.
Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S5)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory MonoidalCategory Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues Obj

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

section Leaf

variable {L : Type*} [Fintype L] [DecidableEq L]

theorem sum_update (i : L) (y : L → Fin 2) (F : (L → Fin 2) → ℂ)
    (hF : ∀ z, ¬ (∀ j, j ≠ i → y j = z j) → F z = 0) :
    ∑ z, F z = ∑ k : Fin 2, F (Function.update y i k) := by
  have hinj : Function.Injective (fun k : Fin 2 => Function.update y i k) := fun k k' h => by
    have := congrFun h i; simpa using this
  rw [← Finset.sum_image (fun k _ k' _ h => hinj h)]
  symm
  apply Finset.sum_subset (Finset.subset_univ _)
  intro z _ hz
  apply hF
  intro h
  apply hz
  rw [Finset.mem_image]
  refine ⟨z i, Finset.mem_univ _, ?_⟩
  funext j
  by_cases hj : j = i
  · subst hj; simp
  · rw [Function.update_of_ne hj]; exact h j hj

theorem leafOp_mul_same (i : L) (a b : Matrix (Fin 2) (Fin 2) ℂ) :
    leafOp i a * leafOp i b = leafOp i (a * b) := by
  ext y x
  rw [Matrix.mul_apply, sum_update i y]
  · simp only [leafOp, Matrix.of_apply, Function.update_self, Matrix.mul_apply]
    by_cases h : ∀ j, j ≠ i → y j = x j
    · rw [if_pos h, mul_one, Fin.sum_univ_two, Fin.sum_univ_two]
      have h1 : ∀ k : Fin 2, (∀ j, j ≠ i → y j = Function.update y i k j) := fun k j hj => by
        rw [Function.update_of_ne hj]
      have h2 : ∀ k : Fin 2, (∀ j, j ≠ i → Function.update y i k j = x j) := fun k j hj => by
        rw [Function.update_of_ne hj]; exact h j hj
      rw [if_pos (h1 0), if_pos (h2 0), if_pos (h1 1), if_pos (h2 1)]
      ring
    · rw [if_neg h, mul_zero]
      apply Finset.sum_eq_zero
      intro k _
      have hk : ¬ ∀ j, j ≠ i → Function.update y i k j = x j := fun h' =>
        h (fun j hj => by rw [← h' j hj, Function.update_of_ne hj])
      simp [hk]
  · intro z hz
    simp only [leafOp, Matrix.of_apply]
    rw [if_neg hz]; simp

theorem leafOp_comm {i j : L} (hij : i ≠ j) (a b : Matrix (Fin 2) (Fin 2) ℂ) :
    Commute (leafOp i a) (leafOp j b) := by
  show leafOp i a * leafOp j b = leafOp j b * leafOp i a
  ext y x
  rw [leafOp_mul_leafOp_apply hij, leafOp_mul_leafOp_apply (Ne.symm hij)]
  rw [mul_comm (a (y i) (x i))]
  congr 1
  apply if_congr _ rfl rfl
  exact ⟨fun h k h1 h2 => h k h2 h1, fun h k h1 h2 => h k h2 h1⟩

theorem leafOp_sub (i : L) (a b : Matrix (Fin 2) (Fin 2) ℂ) :
    leafOp i (a - b) = leafOp i a - leafOp i b := by
  ext y x; simp only [leafOp, Matrix.of_apply, Matrix.sub_apply]; split_ifs <;> simp

theorem leafOp_one (i : L) : leafOp i (1 : Matrix (Fin 2) (Fin 2) ℂ) = 1 := by
  ext y x
  simp only [leafOp, Matrix.of_apply, Matrix.one_apply]
  by_cases h : y = x
  · subst h; simp
  · rw [if_neg h]
    by_cases hi : y i = x i
    · rw [if_pos hi, one_mul, if_neg]
      intro h'; apply h; funext j
      by_cases hj : j = i
      · subst hj; exact hi
      · exact h' j hj
    · rw [if_neg hi, zero_mul]

theorem blk_comm {S T : Finset L} (h : Disjoint S T) (a b : Matrix (Fin 2) (Fin 2) ℂ) :
    Commute (blk S a) (blk T b) :=
  Commute.sum_left _ _ _ fun i hi => Commute.sum_right _ _ _ fun j hj =>
    leafOp_comm (fun e => Finset.disjoint_left.1 h hi (by subst e; exact hj)) a b

theorem blk_bracket (S : Finset L) (a b : Matrix (Fin 2) (Fin 2) ℂ) :
    blk S a * blk S b - blk S b * blk S a = blk S (a * b - b * a) := by
  simp only [blk, Finset.sum_mul_sum]
  rw [Finset.sum_comm (s := S) (t := S) (f := fun i j => leafOp i b * leafOp j a),
    ← Finset.sum_sub_distrib]
  simp only [← Finset.sum_sub_distrib]
  rw [Finset.sum_congr rfl fun i hi => Finset.sum_eq_single_of_mem i hi fun j _ hji => by
    rw [(leafOp_comm (Ne.symm hji) a b).eq, sub_self]]
  simp [leafOp_mul_same, leafOp_sub]

theorem blk_union {S T : Finset L} (h : Disjoint S T) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    blk (S ∪ T) a = blk S a + blk T a := by
  simp [blk, Finset.sum_union h]

end Leaf

/-! ### The `sl₂` Casimir is central -/

section Casimir

variable {R : Type*} [Ring R] [Algebra ℂ R]

/-- In any `ℂ`-algebra, the Casimir `EF + FE + ½H²` of an `sl₂`-triple commutes with `E`, `F`, `H`. -/
theorem casimir_comm (E F H : R) (hEF : E * F - F * E = H) (hHE : H * E - E * H = 2 • E)
    (hHF : H * F - F * H = -(2 • F)) :
    Commute (E * F + F * E + (1 / 2 : ℂ) • (H * H)) E ∧
      Commute (E * F + F * E + (1 / 2 : ℂ) • (H * H)) F ∧
      Commute (E * F + F * E + (1 / 2 : ℂ) • (H * H)) H := by
  have half : ∀ Y : R, (1 / 2 : ℂ) • (2 • Y) = Y := fun Y => by
    rw [two_nsmul, ← two_smul ℂ Y, smul_smul]; norm_num
  have FE : F * E - E * F = -H := by rw [← hEF]; abel
  refine ⟨?_, ?_, ?_⟩
  · rw [Commute, SemiconjBy, ← sub_eq_zero]
    have X1 : (E * F + F * E) * E - E * (E * F + F * E) = (F * E - E * F) * E + E * (F * E - E * F) := by
      noncomm_ring
    have X2 : H * H * E - E * (H * H) = H * (H * E - E * H) + (H * E - E * H) * H := by noncomm_ring
    rw [FE, hHE] at *
    calc (E * F + F * E + (1 / 2 : ℂ) • (H * H)) * E - E * (E * F + F * E + (1 / 2 : ℂ) • (H * H))
        = ((E * F + F * E) * E - E * (E * F + F * E)) + (1 / 2 : ℂ) • (H * H * E - E * (H * H)) := by
          rw [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_sub]; abel
      _ = 0 := by
          rw [X1, X2, mul_smul_comm, smul_mul_assoc, ← smul_add, half]; noncomm_ring
  · rw [Commute, SemiconjBy, ← sub_eq_zero]
    have X1 : (E * F + F * E) * F - F * (E * F + F * E) = (E * F - F * E) * F + F * (E * F - F * E) := by
      noncomm_ring
    have X2 : H * H * F - F * (H * H) = H * (H * F - F * H) + (H * F - F * H) * H := by noncomm_ring
    rw [hEF, hHF] at *
    calc (E * F + F * E + (1 / 2 : ℂ) • (H * H)) * F - F * (E * F + F * E + (1 / 2 : ℂ) • (H * H))
        = ((E * F + F * E) * F - F * (E * F + F * E)) + (1 / 2 : ℂ) • (H * H * F - F * (H * H)) := by
          rw [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_sub]; abel
      _ = 0 := by
          rw [X1, X2, mul_neg, neg_mul, mul_smul_comm, smul_mul_assoc, ← neg_add, ← smul_add,
            smul_neg, half]; abel
  · rw [Commute, SemiconjBy, ← sub_eq_zero]
    have X1 : (E * F + F * E) * H - H * (E * F + F * E) =
        E * (F * H - H * F) + (E * H - H * E) * F + F * (E * H - H * E) + (F * H - H * F) * E := by
      noncomm_ring
    have e1 : F * H - H * F = 2 • F := by rw [← neg_sub, hHF, neg_neg]
    have e2 : E * H - H * E = -(2 • E) := by rw [← neg_sub, hHE]
    rw [e1, e2] at X1
    calc (E * F + F * E + (1 / 2 : ℂ) • (H * H)) * H - H * (E * F + F * E + (1 / 2 : ℂ) • (H * H))
        = (E * F + F * E) * H - H * (E * F + F * E) := by
          rw [add_mul, mul_add, smul_mul_assoc, mul_smul_comm]; noncomm_ring
      _ = 0 := by rw [X1]; noncomm_ring

end Casimir

theorem sl2_ef : eS * fS - fS * eS = hS := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [eS, fS, hS]
theorem sl2_he : hS * eS - eS * hS = 2 • eS := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [eS, hS] <;> norm_num
theorem sl2_hf : hS * fS - fS * hS = -(2 • fS) := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [fS, hS] <;> norm_num

section Tsl

variable {L : Type*} [Fintype L] [DecidableEq L]

theorem leafOp_add (i : L) (a b : Matrix (Fin 2) (Fin 2) ℂ) :
    leafOp i (a + b) = leafOp i a + leafOp i b := by
  ext y x; simp only [leafOp, Matrix.of_apply, Matrix.add_apply]; split_ifs <;> simp

theorem blk_nsmul (S : Finset L) (n : ℕ) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    blk S (n • a) = n • blk S a := by
  induction n with
  | zero =>
      rw [zero_nsmul, zero_nsmul]
      have h0 : ∀ i : L, leafOp i (0 : Matrix (Fin 2) (Fin 2) ℂ) = 0 := fun i => by
        ext; simp [leafOp]
      simp [blk, h0]
  | succ n ih =>
      rw [succ_nsmul, succ_nsmul, ← ih]
      simp only [blk, leafOp_add, Finset.sum_add_distrib]

theorem blk_neg (S : Finset L) (a : Matrix (Fin 2) (Fin 2) ℂ) : blk S (-a) = -blk S a := by
  have := leafOp_sub (L := L)
  simp only [blk, ← Finset.sum_neg_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  have h := leafOp_sub i 0 a
  rw [zero_sub] at h
  rw [h]
  have h0 : leafOp i (0 : Matrix (Fin 2) (Fin 2) ℂ) = 0 := by ext; simp [leafOp]
  rw [h0, zero_sub]

/-- **The block Casimir `Ω_S = tsl(S, S)` commutes with the `sl₂`-action on `S`.** -/
theorem tsl_self_comm (S : Finset L) :
    Commute (tsl S S) (blk S eS) ∧ Commute (tsl S S) (blk S fS) ∧ Commute (tsl S S) (blk S hS) := by
  have := casimir_comm (blk S eS) (blk S fS) (blk S hS)
    (by rw [blk_bracket, sl2_ef]) (by rw [blk_bracket, sl2_he, blk_nsmul])
    (by rw [blk_bracket, sl2_hf, blk_neg, blk_nsmul])
  exact this

theorem tsl_self_comm_blk_disj {S T : Finset L} (h : Disjoint S T) (b : Matrix (Fin 2) (Fin 2) ℂ) :
    Commute (tsl S S) (blk T b) := by
  unfold tsl
  have c := fun a => blk_comm h a b
  exact ((((c eS).mul_left (c fS)).add_left ((c fS).mul_left (c eS))).add_left
    (((c hS).mul_left (c hS)).smul_left _))

theorem tsl_self_comm_tsl {S T : Finset L} (h : Disjoint S T) :
    Commute (tsl S S) (tsl S T) := by
  obtain ⟨ce, cf, ch⟩ := tsl_self_comm S
  have d := fun b => tsl_self_comm_blk_disj h b
  unfold tsl at *
  exact (((ce.mul_right (d fS)).add_right (cf.mul_right (d eS))).add_right
    ((ch.mul_right (d hS)).smul_right _))

theorem tsl_self_comm_tsl' {S T : Finset L} (h : Disjoint S T) :
    Commute (tsl T T) (tsl S T) := by
  rw [tsl_comm h]; exact tsl_self_comm_tsl h.symm

theorem tsl_self_comm_self {S T : Finset L} (h : Disjoint S T) :
    Commute (tsl S S) (tsl T T) := by
  have d := fun b => tsl_self_comm_blk_disj h b
  unfold tsl at *
  exact (((d eS).mul_right (d fS)).add_right ((d fS).mul_right (d eS))).add_right
    (((d hS).mul_right (d hS)).smul_right _)

theorem tsl_union_left {S T : Finset L} (h : Disjoint S T) (W : Finset L) :
    tsl (S ∪ T) W = tsl S W + tsl T W := by
  simp only [tsl, blk_union h, Matrix.add_mul, smul_add]; abel

theorem tsl_union_right {S T : Finset L} (h : Disjoint S T) (W : Finset L) :
    tsl W (S ∪ T) = tsl W S + tsl W T := by
  simp only [tsl, blk_union h, Matrix.mul_add, smul_add]; abel

/-- `Ω_{S ∪ T} = Ω_S + Ω_T + 2 t^{sl}_{S,T}`. -/
theorem tsl_union_self {S T : Finset L} (h : Disjoint S T) :
    tsl (S ∪ T) (S ∪ T) = tsl S S + tsl T T + (tsl S T + tsl S T) := by
  rw [tsl_union_left h, tsl_union_right h, tsl_union_right h, tsl_comm h.symm]; abel

end Tsl

section TwistMat

theorem leafOp_smul {L : Type*} [Fintype L] [DecidableEq L] (i : L) (r : ℂ)
    (a : Matrix (Fin 2) (Fin 2) ℂ) : leafOp i (r • a) = r • leafOp i a := by
  ext y x; simp [leafOp]

theorem blk_smul {L : Type*} [Fintype L] [DecidableEq L] (S : Finset L) (r : ℂ)
    (a : Matrix (Fin 2) (Fin 2) ℂ) : blk S (r • a) = r • blk S a := by
  simp [blk, leafOp_smul, Finset.smul_sum]

theorem blk_add {L : Type*} [Fintype L] [DecidableEq L] (S : Finset L)
    (a b : Matrix (Fin 2) (Fin 2) ℂ) : blk S (a + b) = blk S a + blk S b := by
  simp [blk, leafOp_add, Finset.sum_add_distrib]

theorem traceless_decomp (a : Matrix (Fin 2) (Fin 2) ℂ) (ha : a.trace = 0) :
    a = a 0 1 • eS + a 1 0 • fS + a 0 0 • hS := by
  rw [Matrix.trace_fin_two] at ha
  have h11 : a 1 1 = -a 0 0 := by linear_combination ha
  ext i j; fin_cases i <;> fin_cases j <;> simp [eS, fS, hS, h11]

/-- `Ω_X` commutes with the diagonal action of every traceless `a`. -/
theorem tsl_univ_comm_diag {L : Type*} [Fintype L] [DecidableEq L] (a : Matrix (Fin 2) (Fin 2) ℂ)
    (ha : a.trace = 0) : Commute (tsl (univ : Finset L) univ) (diag L a) := by
  obtain ⟨ce, cf, ch⟩ := tsl_self_comm (univ : Finset L)
  rw [← blk_univ, traceless_decomp a ha, blk_add, blk_add, blk_smul, blk_smul, blk_smul]
  exact ((ce.smul_right _).add_right (cf.smul_right _)).add_right (ch.smul_right _)

variable (c : ℂ)

/-- The twist matrix `θ_X = exp(iπℏ Ω_X)`. -/
def θmat (X : Obj) : EndL (Leaves X) := expi (c • tsl (univ : Finset (Leaves X)) univ)

/-- Its inverse. -/
def θinv (X : Obj) : EndL (Leaves X) :=
  expi (L := Leaves X) (-(c • tsl (univ : Finset (Leaves X)) univ))

theorem equivariant_θmat (X : Obj) : Equivariant (θmat c X) := by
  intro a ha
  rw [ρ_eq_diag, θmat]
  exact (commute_expi ((tsl_univ_comm_diag a ha).symm.smul_right c)).eq

theorem equivariant_θinv (X : Obj) : Equivariant (θinv c X) := by
  intro a ha
  rw [ρ_eq_diag, θinv]
  exact (commute_expi ((tsl_univ_comm_diag (L := Leaves X) a ha).symm.smul_right c).neg_right).eq

theorem θmat_natural {X Y : Obj} (f : X ⟶ Y) : f.1 * θmat c X = θmat c Y * f.1 := by
  have ht : f.1 * tsl (univ : Finset (Leaves X)) univ = tsl (univ : Finset (Leaves Y)) univ * f.1 :=
    intertwine_tsl _ (fun a ha => by rw [blk_univ, blk_univ, ← ρ_eq_diag, ← ρ_eq_diag, f.2 a ha])
      (fun a ha => by rw [blk_univ, blk_univ, ← ρ_eq_diag, ← ρ_eq_diag, f.2 a ha])
  unfold θmat expi
  apply KZIntertwine.exp_intertwine
  rw [Matrix.mul_smul, Matrix.mul_smul, ht, Matrix.smul_mul, Matrix.smul_mul]

theorem θmat_unit : θmat c unit = 1 := by
  have : (univ : Finset (Leaves unit)) = ∅ := Finset.univ_eq_empty
  have h0 : tsl (∅ : Finset (Leaves unit)) ∅ = 0 := by simp [tsl, blk]
  rw [θmat, this, h0, smul_zero]
  simp [expi]

theorem univ_tensor (X Y : Obj) : (univ : Finset (Leaves (tensor X Y))) = bL X Y ∪ bR X Y := by
  ext k; rcases k with k | k <;> simp [bL, bR]

theorem βmat_βmat (X Y : Obj) :
    βmat c Y X * βmat c X Y = expi (c • tsl (bL X Y) (bR X Y)) * expi (c • tsl (bL X Y) (bR X Y)) := by
  have hL : (bL Y X).map (swapLegs X Y).symm.toEmbedding = bR X Y := by
    ext k; rcases k with k | k <;> simp [bL, bR, swapLegs]
  have hR : (bR Y X).map (swapLegs X Y).symm.toEmbedding = bL X Y := by
    ext k; rcases k with k | k <;> simp [bL, bR, swapLegs]
  rw [βmat, βmat, Matrix.mul_assoc, ← Matrix.mul_assoc (expi _) (reidx _), expi_tsl_mul_reidx, hL,
    hR, tsl_comm (disj_bLR X Y).symm, ← Matrix.mul_assoc, ← Matrix.mul_assoc, reidx_mul,
    show swapLegs Y X = (swapLegs X Y).symm from (Equiv.sumComm_symm _ _).symm,
    Equiv.self_trans_symm, reidx_refl, Matrix.one_mul]

theorem expi_three {L : Type*} [Fintype L] [DecidableEq L] (A B C : EndL L) (cAB : Commute A B)
    (cAC : Commute A C) (cBC : Commute B C) :
    expi (A + B + (C + C)) = expi A * expi B * (expi C * expi C) := by
  rw [expi_add ((cAC.add_right cAC).add_left (cBC.add_right cBC)), expi_add cAB,
    expi_add (Commute.refl C)]

theorem θmat_tensor (X Y : Obj) :
    θmat c (tensor X Y) = kron (θmat c X) (θmat c Y) * βmat c Y X * βmat c X Y := by
  have d := disj_bLR X Y
  have hk : kron (θmat c X) (θmat c Y) =
      expi (c • tsl (bL X Y) (bL X Y)) * expi (c • tsl (bR X Y) (bR X Y)) := by
    rw [← Matrix.mul_one (θmat c X), ← Matrix.one_mul (θmat c Y), ← kron_mul, θmat, θmat,
      kron_expi_one, one_kron_expi, kron_smul_left, kron_smul_right, kron_tsl_one, one_kron_tsl]
    rfl
  rw [Matrix.mul_assoc, βmat_βmat, hk, θmat, univ_tensor, tsl_union_self d, smul_add, smul_add, smul_add]
  exact expi_three _ _ _ ((tsl_self_comm_self d).smul_left c |>.smul_right c)
    ((tsl_self_comm_tsl d).smul_left c |>.smul_right c)
    ((tsl_self_comm_tsl' d).smul_left c |>.smul_right c)

end TwistMat

end QOU.KZ.Drinfeld
