import QOU.KZ.NonResonantInt
import QOU.KZ.KZShiftPhi
import QOU.KZ.GLnKZ
import QOU.KZ.KZHexagonCentral

/-!
# Block KZ residues on `V^{⊗N}` and the pentagon for every four-block partition

Stage S2 of bean `qou-zoyv`. For pairwise disjoint sets of tensor legs `X, Y ⊆ {0, …, N−1}`
the block Casimir is `t_{X,Y} = ∑_{i ∈ X, j ∈ Y} P_{ij}` (`tB`). This is the split `𝔤𝔩_n`
Casimir between the sub-tensor products `V^{⊗X}` and `V^{⊗Y}`
(`GLnResidues.casimirLeg_eq_flipL`). It is the residue of the associator `α_{X,Y,Z}` of the
Drinfeld category.

* `commute_flip_tB`: `P_{ab}` commutes with `t_{X,Y}` when the transposition `(ab)` preserves
  `X` and `Y`. Conjugation by `P_{ab}` permutes the summands.
* `blockRes_rel`: the infinitesimal pure-braid relations `KZ4.Res.Rel` for the block residues
  of any four pairwise disjoint blocks.
* `nonResonant_smul_tB…`: every block residue and every sum of block residues is an integer
  matrix, so `ℏ` times it is non-resonant for transcendental `ℏ`
  (`NonResonantInt.nonResonant_smul_intMatrix`).
* `pentagon_blocks`: Drinfeld's pentagon `Φ^{234} Φ^{1,23,4} Φ^{123} = Φ^{1,2,34} Φ^{12,3,4}` for
  the block residues of any four disjoint blocks. This is the identity behind Mathlib's
  `MonoidalCategory.pentagon` for `α_{X,Y,Z} = Φ(ℏ t_{X,Y}, ℏ t_{Y,Z})`.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

namespace QOU.KZ.BlockResidues

open QOU.KZ.FuchsianFormal QOU.KZ.GLnResidues QOU.KZ.KZ4

section Algebra

variable (K : Type*) [Field K] (n : ℕ) {L : Type*} [Fintype L] [DecidableEq L]

/-- The action of a permutation of the legs `L` on `V^{⊗L}`. -/
def permL (σ : Equiv.Perm L) : Matrix (L → Fin n) (L → Fin n) K :=
  permMat K (fun x : L → Fin n => x ∘ σ)

theorem permL_mul (σ τ : Equiv.Perm L) : permL K n σ * permL K n τ = permL K n (τ * σ) :=
  permMat_mul K _ _

/-- The flip `P_{ij}` of two legs. -/
abbrev flipL (i j : L) : Matrix (L → Fin n) (L → Fin n) K := permL K n (Equiv.swap i j)

/-- The block Casimir `t_{X,Y} = ∑_{i ∈ X, j ∈ Y} P_{ij}`. -/
def tB (X Y : Finset L) : Matrix (L → Fin n) (L → Fin n) K :=
  ∑ i ∈ X, ∑ j ∈ Y, flipL K n i j

variable {K n}

/-- Conjugation of a flip by a flip. -/
theorem flip_mul_flip (a b i j : L) :
    flipL K n a b * flipL K n i j =
      flipL K n (Equiv.swap a b i) (Equiv.swap a b j) * flipL K n a b := by
  simp only [flipL, permL_mul]
  congr 1
  rw [Equiv.swap_apply_apply, Equiv.swap_inv]
  simp only [← mul_assoc, Equiv.swap_mul_self, one_mul]

omit [Fintype L] in
/-- Reindexing a sum over a set preserved by a transposition. -/
theorem sum_swap_eq {M : Type*} [AddCommMonoid M] (a b : L) (X : Finset L)
    (hX : ∀ x, Equiv.swap a b x ∈ X ↔ x ∈ X) (g : L → M) :
    ∑ i ∈ X, g (Equiv.swap a b i) = ∑ i ∈ X, g i :=
  Finset.sum_bij' (fun i _ => Equiv.swap a b i) (fun i _ => Equiv.swap a b i)
    (fun i hi => (hX i).2 hi) (fun i hi => (hX i).2 hi) (fun i _ => by simp)
    (fun i _ => by simp) (fun i _ => rfl)

/-- `P_{ab}` commutes with `t_{X,Y}` when `(ab)` preserves both blocks. -/
theorem commute_flip_tB (a b : L) (X Y : Finset L)
    (hX : ∀ x, Equiv.swap a b x ∈ X ↔ x ∈ X) (hY : ∀ x, Equiv.swap a b x ∈ Y ↔ x ∈ Y) :
    Commute (flipL K n a b) (tB K n X Y) := by
  show flipL K n a b * tB K n X Y = tB K n X Y * flipL K n a b
  simp only [tB, Finset.mul_sum, Finset.sum_mul]
  calc ∑ i ∈ X, ∑ j ∈ Y, flipL K n a b * flipL K n i j
      = ∑ i ∈ X, ∑ j ∈ Y, flipL K n (Equiv.swap a b i) (Equiv.swap a b j) * flipL K n a b :=
        Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => flip_mul_flip a b i j
    _ = ∑ i ∈ X, ∑ j ∈ Y, flipL K n i (Equiv.swap a b j) * flipL K n a b :=
        sum_swap_eq a b X hX (fun i => ∑ j ∈ Y,
          flipL K n i (Equiv.swap a b j) * flipL K n a b)
    _ = _ := Finset.sum_congr rfl fun i _ =>
        sum_swap_eq a b Y hY (fun j => flipL K n i j * flipL K n a b)

omit [Fintype L] in
/-- A transposition of two points both inside or both outside `X` preserves `X`. -/
theorem swap_mem_iff {a b : L} {X : Finset L} (h : a ∈ X ↔ b ∈ X) (x : L) :
    Equiv.swap a b x ∈ X ↔ x ∈ X := by
  by_cases hxa : x = a
  · subst hxa; simp [h]
  · by_cases hxb : x = b
    · subst hxb; simp [h]
    · rw [Equiv.swap_apply_of_ne_of_ne hxa hxb]

theorem tB_union_left {X X' Y : Finset L} (h : Disjoint X X') :
    tB K n (X ∪ X') Y = tB K n X Y + tB K n X' Y := by
  simp only [tB, Finset.sum_union h]

theorem tB_union_right {X Y Y' : Finset L} (h : Disjoint Y Y') :
    tB K n X (Y ∪ Y') = tB K n X Y + tB K n X Y' := by
  simp only [tB, Finset.sum_union h, Finset.sum_add_distrib]

theorem tB_comm (X Y : Finset L) : tB K n X Y = tB K n Y X := by
  rw [tB, tB, Finset.sum_comm]
  simp only [flipL, Equiv.swap_comm]

/-- A flip `P_{ab}` with `a ∈ X₁`, `b ∈ X₂` commutes with `t_{U,W}` if each of `U`, `W` contains
both or neither of `a, b`. -/
theorem commute_tB_tB {X₁ X₂ U W : Finset L}
    (hU : ∀ a ∈ X₁, ∀ b ∈ X₂, (a ∈ U ↔ b ∈ U)) (hW : ∀ a ∈ X₁, ∀ b ∈ X₂, (a ∈ W ↔ b ∈ W)) :
    Commute (tB K n X₁ X₂) (tB K n U W) :=
  Commute.sum_left _ _ _ fun a ha => Commute.sum_left _ _ _ fun b hb =>
    commute_flip_tB a b U W (swap_mem_iff (hU a ha b hb)) (swap_mem_iff (hW a ha b hb))

end Algebra

/-! ### The four-block residues -/

section Blocks

variable (n : ℕ) {L : Type*} [Fintype L] [DecidableEq L]

/-- Four pairwise disjoint blocks of tensor legs. -/
structure Blocks (L : Type*) where
  X1 : Finset L
  X2 : Finset L
  X3 : Finset L
  X4 : Finset L
  d12 : Disjoint X1 X2
  d13 : Disjoint X1 X3
  d14 : Disjoint X1 X4
  d23 : Disjoint X2 X3
  d24 : Disjoint X2 X4
  d34 : Disjoint X3 X4

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

/-- The KZ residues `ℏ t_{X_a, X_b}` of a four-block partition. -/
noncomputable def blockRes (c : ℂ) (B : Blocks L) : Res (Matrix (L → Fin n) (L → Fin n) ℂ) where
  t12 := c • tB ℂ n B.X1 B.X2
  t13 := c • tB ℂ n B.X1 B.X3
  t23 := c • tB ℂ n B.X2 B.X3
  t24 := c • tB ℂ n B.X2 B.X4
  t34 := c • tB ℂ n B.X3 B.X4

omit [Fintype L] [DecidableEq L] in
theorem not_mem_of_disjoint {X Y : Finset L} (h : Disjoint X Y) {a : L} (ha : a ∈ X) :
    a ∉ Y := Finset.disjoint_left.1 h ha

/-- **The infinitesimal pure-braid relations for block residues.** -/
theorem blockRes_rel (c : ℂ) (B : Blocks L) : (blockRes n c B).Rel := by
  have nm := @not_mem_of_disjoint L
  have smc : ∀ {x y : Matrix (L → Fin n) (L → Fin n) ℂ}, Commute x y →
      Commute (c • x) (c • y) := fun h => (h.smul_left c).smul_right c
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · -- [t12, t34]
    exact smc (commute_tB_tB
      (fun a ha b hb => by simp [nm B.d13 ha, nm B.d23 hb])
      (fun a ha b hb => by simp [nm B.d14 ha, nm B.d24 hb]))
  · -- [t13, t24]
    exact smc (commute_tB_tB
      (fun a ha b hb => by simp [nm B.d12 ha, nm B.d23.symm hb])
      (fun a ha b hb => by simp [nm B.d14 ha, nm B.d34 hb]))
  · -- [t12, t13 + t23]
    show Commute (c • tB ℂ n B.X1 B.X2) (c • tB ℂ n B.X1 B.X3 + c • tB ℂ n B.X2 B.X3)
    rw [← smul_add, ← tB_union_left B.d12]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [ha, hb])
      (fun a ha b hb => by simp [nm B.d13 ha, nm B.d23 hb]))
  · -- [t23, t12 + t13]
    show Commute (c • tB ℂ n B.X2 B.X3) (c • tB ℂ n B.X1 B.X2 + c • tB ℂ n B.X1 B.X3)
    rw [← smul_add, ← tB_union_right B.d23]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [nm B.d12.symm ha, nm B.d13.symm hb])
      (fun a ha b hb => by simp [ha, hb]))
  · -- [t23, t24 + t34]
    show Commute (c • tB ℂ n B.X2 B.X3) (c • tB ℂ n B.X2 B.X4 + c • tB ℂ n B.X3 B.X4)
    rw [← smul_add, ← tB_union_left B.d23]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [ha, hb])
      (fun a ha b hb => by simp [nm B.d24 ha, nm B.d34 hb]))
  · -- [t24, t23 + t34]
    show Commute (c • tB ℂ n B.X2 B.X4) (c • tB ℂ n B.X2 B.X3 + c • tB ℂ n B.X3 B.X4)
    rw [← smul_add, tB_comm B.X2 B.X3, ← tB_union_right B.d24]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [nm B.d23 ha, nm B.d34.symm hb])
      (fun a ha b hb => by simp [ha, hb]))

/-! ### Integrality and non-resonance -/

/-- The integer permutation matrix of `σ` on `V^{⊗N}`. -/
def permZ (σ : Equiv.Perm L) : Matrix (L → Fin n) (L → Fin n) ℤ :=
  Matrix.of fun x y => if y ∘ σ = x then 1 else 0

/-- The integer block Casimir. -/
def tBZ (X Y : Finset L) : Matrix (L → Fin n) (L → Fin n) ℤ :=
  ∑ i ∈ X, ∑ j ∈ Y, permZ n (Equiv.swap i j)

theorem permL_intCast (σ : Equiv.Perm L) :
    permL ℂ n σ = (Int.castRingHom ℂ).mapMatrix (permZ n σ) := by
  ext x y
  simp only [permL, permMat, permZ, RingHom.mapMatrix_apply, Matrix.map_apply, Matrix.of_apply,
    Function.comp_def]
  split_ifs <;> simp

theorem tB_intCast (X Y : Finset L) :
    tB ℂ n X Y = (Int.castRingHom ℂ).mapMatrix (tBZ n X Y) := by
  simp only [tB, tBZ, map_sum, flipL, permL_intCast]

variable {n}

/-- `ℏ M` is non-resonant for an integer matrix `M` and transcendental `ℏ`. -/
theorem nonResonant_cast {c : ℂ} (hc : Transcendental ℚ c) (M : Matrix (L → Fin n)
    (L → Fin n) ℤ) : NonResonant (c • (Int.castRingHom ℂ).mapMatrix M) :=
  NonResonantInt.nonResonant_smul_intMatrix M c hc

variable {c : ℂ} (hc : Transcendental ℚ c) (B : Blocks L)
include hc

theorem nr12 : NonResonant (blockRes n c B).t12 := by
  simp only [blockRes, tB_intCast]; exact nonResonant_cast hc _
theorem nr23 : NonResonant (blockRes n c B).t23 := by
  simp only [blockRes, tB_intCast]; exact nonResonant_cast hc _
theorem nr34 : NonResonant (blockRes n c B).t34 := by
  simp only [blockRes, tB_intCast]; exact nonResonant_cast hc _
theorem nr123 : NonResonant (blockRes n c B).T123 := by
  simp only [Res.T123, blockRes, tB_intCast, ← smul_add, ← map_add]; exact nonResonant_cast hc _
theorem nr234 : NonResonant (blockRes n c B).T234 := by
  simp only [Res.T234, blockRes, tB_intCast, ← smul_add, ← map_add]; exact nonResonant_cast hc _
theorem nr1213 : NonResonant ((blockRes n c B).t12 + (blockRes n c B).t13) := by
  simp only [blockRes, tB_intCast, ← smul_add, ← map_add]; exact nonResonant_cast hc _
theorem nr2434 : NonResonant ((blockRes n c B).t24 + (blockRes n c B).t34) := by
  simp only [blockRes, tB_intCast, ← smul_add, ← map_add]; exact nonResonant_cast hc _
theorem nr2324 : NonResonant ((blockRes n c B).t23 + (blockRes n c B).t24) := by
  simp only [blockRes, tB_intCast, ← smul_add, ← map_add]; exact nonResonant_cast hc _
theorem nr1323 : NonResonant ((blockRes n c B).t13 + (blockRes n c B).t23) := by
  simp only [blockRes, tB_intCast, ← smul_add, ← map_add]; exact nonResonant_cast hc _

/-- **The pentagon for every four-block partition of `V^{⊗N}`**, `ℏ` transcendental:
`Φ^{234} Φ^{1,23,4} Φ^{123} = Φ^{1,2,34} Φ^{12,3,4}` with `t_{ab} = ℏ t_{X_a, X_b}`. -/
theorem pentagon_blocks :
    KZPentagon.Φ (blockRes n c B).t23 (blockRes n c B).t34 (nr23 hc B) (nr34 hc B) *
      KZPentagon.Φ ((blockRes n c B).t12 + (blockRes n c B).t13)
        ((blockRes n c B).t24 + (blockRes n c B).t34) (nr1213 hc B) (nr2434 hc B) *
      KZPentagon.Φ (blockRes n c B).t12 (blockRes n c B).t23 (nr12 hc B) (nr23 hc B) =
    KZPentagon.Φ (blockRes n c B).t12 ((blockRes n c B).t23 + (blockRes n c B).t24)
        (nr12 hc B) (nr2324 hc B) *
      KZPentagon.Φ ((blockRes n c B).t13 + (blockRes n c B).t23) (blockRes n c B).t34
        (nr1323 hc B) (nr34 hc B) :=
  KZShiftPhi.pentagon_drinfeld _ (blockRes_rel n c B) _ _ _ (nr123 hc B) (nr234 hc B) _ _ _ _

end Blocks

/-! ### The hexagon for three blocks -/

section Hexagon

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {n : ℕ} {L : Type*} [Fintype L] [DecidableEq L] {c : ℂ}

/-- **The central hexagon for three disjoint blocks**, `ℏ` transcendental. With
`t_{ab} = t_{X_a, X_b}` and `T = t₁₂ + t₂₃ + t₁₃`:
`e^{−iπℏt₁₂} Φ(ℏt₁₃, ℏt₁₂) e^{−iπℏt₁₃} Φ(ℏt₂₃, ℏt₁₃) e^{−iπℏt₂₃} Φ(ℏt₁₂, ℏt₂₃) = e^{−iπℏT}`. -/
theorem hexagon_blocks (hc : Transcendental ℚ c) {X1 X2 X3 : Finset L}
    (d12 : Disjoint X1 X2) (d13 : Disjoint X1 X3) (d23 : Disjoint X2 X3) :
    KZHexagon.eπ (c • tB ℂ n X1 X2) *
      KZPentagon.Φ (c • tB ℂ n X1 X3) (c • tB ℂ n X1 X2)
        (by rw [tB_intCast]; exact nonResonant_cast hc _)
        (by rw [tB_intCast]; exact nonResonant_cast hc _) *
      KZHexagon.eπ (c • tB ℂ n X1 X3) *
      KZPentagon.Φ (c • tB ℂ n X2 X3) (c • tB ℂ n X1 X3)
        (by rw [tB_intCast]; exact nonResonant_cast hc _)
        (by rw [tB_intCast]; exact nonResonant_cast hc _) *
      KZHexagon.eπ (c • tB ℂ n X2 X3) *
      KZPentagon.Φ (c • tB ℂ n X1 X2) (c • tB ℂ n X2 X3)
        (by rw [tB_intCast]; exact nonResonant_cast hc _)
        (by rw [tB_intCast]; exact nonResonant_cast hc _) =
    KZHexagon.eπ (c • tB ℂ n X1 X2 + c • tB ℂ n X2 X3 + c • tB ℂ n X1 X3) := by
  have nm := @not_mem_of_disjoint L
  have smc : ∀ {x y : Matrix (L → Fin n) (L → Fin n) ℂ}, Commute x y →
      Commute (c • x) (c • y) := fun h => (h.smul_left c).smul_right c
  -- `A = ℏt₁₂` commutes with `ℏ(t₁₃ + t₂₃) = ℏ t_{X₁ ∪ X₂, X₃}`
  have cA : Commute (c • tB ℂ n X1 X2) (c • tB ℂ n X2 X3 + c • tB ℂ n X1 X3) := by
    rw [← smul_add, add_comm, ← tB_union_left d12]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [ha, hb])
      (fun a ha b hb => by simp [nm d13 ha, nm d23 hb]))
  have cB : Commute (c • tB ℂ n X2 X3) (c • tB ℂ n X1 X2 + c • tB ℂ n X1 X3) := by
    rw [← smul_add, ← tB_union_right d23]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [nm d12.symm ha, nm d13.symm hb])
      (fun a ha b hb => by simp [ha, hb]))
  have cC : Commute (c • tB ℂ n X1 X3) (c • tB ℂ n X1 X2 + c • tB ℂ n X2 X3) := by
    rw [← smul_add, tB_comm X1 X2, ← tB_union_right d13]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [nm d12 ha, nm d23.symm hb])
      (fun a ha b hb => by simp [ha, hb]))
  have h := KZHexagonCentral.hexagon_central (c • tB ℂ n X1 X2) (c • tB ℂ n X2 X3)
    (c • tB ℂ n X1 X3) (by rw [tB_intCast]; exact nonResonant_cast hc _)
    (by rw [tB_intCast]; exact nonResonant_cast hc _)
    (by rw [tB_intCast]; exact nonResonant_cast hc _)
    (by
      have e : -(c • tB ℂ n X1 X2) - c • tB ℂ n X2 X3 =
          c • (Int.castRingHom ℂ).mapMatrix (-(tBZ n X1 X2 + tBZ n X2 X3)) := by
        rw [tB_intCast, tB_intCast, map_neg, map_add, smul_neg, smul_add]; abel
      rw [e]; exact nonResonant_cast hc _)
    (by rw [add_assoc]; exact ((Commute.refl _).add_right cA).symm)
    (by rw [add_comm (c • tB ℂ n X1 X2), add_assoc]; exact ((Commute.refl _).add_right cB).symm)
    (by rw [add_comm _ (c • tB ℂ n X1 X3)]; exact ((Commute.refl _).add_right cC).symm)
  exact h

end Hexagon

end QOU.KZ.BlockResidues
