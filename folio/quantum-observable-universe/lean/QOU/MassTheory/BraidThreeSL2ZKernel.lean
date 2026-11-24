import Mathlib.Tactic
import Mathlib.Algebra.Group.Subgroup.Pointwise
import QOU.MassTheory.BorromeanWordForcing

/-!
# The kernel of `B₃ → SL(2, ℤ)` is `⟨Δ⁴⟩`

This file proves `kernelIsDeltaFour : KernelIsDeltaFour`. That is the classical fact
`ker(B₃ → SL(2, ℤ)) = ⟨Δ⁴⟩`, i.e. `B₃ / ⟨Δ⁴⟩ ≅ SL(2, ℤ)`. Here `B₃` is
`QOU.MathlibExt.Braid.BraidGroup 2`, the map is the integer Burau representation
at `t = −1` (`burauNeg`: `σ₀ ↦ [[1, 1], [0, 1]]`, `σ₁ ↦ [[1, 0], [−1, 1]]`), and
`Δ = σ₀σ₁σ₀`. With surjectivity (`burauNeg_surjective`) it gives the isomorphism.
`QOU.Mass.BorromeanWordForcing.isConj_of_burauNeg_isConj` took the kernel fact as a
hypothesis; `isConj_of_burauNeg_isConj'` below discharges it.

## The proof

Put `x = Δ`, `y = σ₀σ₁` and `z = Δ²`. Then `x² = y³ = z` (`x_sq`, `y_cube`), so `z`
commutes with `x` and `y`, and `σ₀ = y⁻¹x`, `σ₁ = xy⁻¹` (`σ0_eq`, `σ1_eq`).

* **Normal form** (`isNF_all`). Every braid equals
  `z^m · y^e · (x y^{e₁}) ⋯ (x y^{e_k}) · x^f` with `e, eᵢ ∈ {−1, 0, 1}`, `eᵢ ≠ 0`,
  `f ∈ {0, 1}`. The set of such elements contains `1` and is closed under left
  multiplication by `x`, `y`, `y⁻¹` and `x⁻¹ = z⁻¹x`, hence by `σᵢ^{±1}`.
* **Ping-pong** (`good_blocks`). The images of the blocks `xy` and `xy⁻¹` are
  `[[−1, 1], [0, −1]]` and `[[1, 0], [−1, 1]]`. Every non-empty product of them has
  sign pattern `[[+, −], [−, +]]` or `[[−, +], [+, −]]` with non-zero off-diagonal part.
* **Conclusion.** If the normal form maps to `1`, a case check on `(m mod 2, e, f)`
  against that sign pattern forces `k = 0`, `e = 0`, `f = 0` and `m` even, so the
  braid is `z^{2j} = (Δ⁴)^j`.
-/

namespace QOU.Mass.BorromeanWordForcing

open QOU.MathlibExt.Braid Matrix.SpecialLinearGroup ModularGroup

namespace KernelProof

/-- `x = Δ = σ₀σ₁σ₀`. -/
def xx : BraidGroup 2 := delta
/-- `y = σ₀σ₁`. -/
def yy : BraidGroup 2 := σ 0 * σ 1
/-- `z = Δ²`. -/
def zz : BraidGroup 2 := delta ^ 2

theorem x_sq : xx * xx = zz := by simp [xx, zz, pow_two]

theorem y_cube : yy ^ 3 = zz := by
  have h := braid_rel
  calc yy ^ 3 = σ 0 * σ 1 * σ 0 * (σ 1 * σ 0 * σ 1) := by
        simp only [yy, pow_succ, pow_zero, one_mul, mul_assoc]
    _ = zz := by rw [← h]; simp [zz, delta, pow_two]

theorem y_sq : yy * yy = zz * yy⁻¹ := by
  rw [← y_cube]; simp [pow_succ, mul_assoc]

theorem yinv_sq : yy⁻¹ * yy⁻¹ = zz⁻¹ * yy := by
  rw [← y_cube]; group

theorem comm_x : Commute xx zz := by
  rw [← x_sq]; exact (Commute.refl xx).mul_right (Commute.refl xx)

theorem comm_y : Commute yy zz := by
  rw [← y_cube]; exact (Commute.refl yy).pow_right 3

theorem σ0_eq : σ 0 = yy⁻¹ * xx := by
  simp only [yy, xx, delta]; group

theorem σ1_eq : σ 1 = xx * yy⁻¹ := by
  simp only [yy, xx, delta]; rw [braid_rel]; group

/-- The sign of a block exponent. -/
def sgn (b : Bool) : ℤ := if b then 1 else -1

/-- A block `x y^{±1}`. -/
def blk (b : Bool) : BraidGroup 2 := xx * yy ^ sgn b

/-- A product of blocks. -/
def blocks (bs : List Bool) : BraidGroup 2 := (bs.map blk).prod

theorem blocks_cons (b : Bool) (bs : List Bool) : blocks (b :: bs) = blk b * blocks bs := by
  simp [blocks]

/-- The tail `x^f`. -/
def tl (f : Bool) : BraidGroup 2 := if f then xx else 1

/-- The core `y^e · blocks · x^f`. -/
def core (e : ℤ) (bs : List Bool) (f : Bool) : BraidGroup 2 := yy ^ e * blocks bs * tl f

/-- Normal form: `z^m · core`, with `e ∈ {−1, 0, 1}`. -/
def IsNF (g : BraidGroup 2) : Prop :=
  ∃ (m e : ℤ) (bs : List Bool) (f : Bool), -1 ≤ e ∧ e ≤ 1 ∧ g = zz ^ m * core e bs f

/-- A left multiplier that sends a core to `z^j · core'` preserves normal form. -/
theorem isNF_left (u : BraidGroup 2) (hc : Commute u zz)
    (h : ∀ (e : ℤ) (bs : List Bool) (f : Bool), -1 ≤ e → e ≤ 1 →
      ∃ (j e' : ℤ) (bs' : List Bool) (f' : Bool), -1 ≤ e' ∧ e' ≤ 1 ∧
        u * core e bs f = zz ^ j * core e' bs' f')
    {g : BraidGroup 2} (hg : IsNF g) : IsNF (u * g) := by
  obtain ⟨m, e, bs, f, h1, h2, rfl⟩ := hg
  obtain ⟨j, e', bs', f', h1', h2', hj⟩ := h e bs f h1 h2
  refine ⟨m + j, e', bs', f', h1', h2', ?_⟩
  rw [← mul_assoc, (hc.zpow_right m).eq, mul_assoc, hj, ← mul_assoc, ← zpow_add]

theorem isNF_zz (k : ℤ) {g : BraidGroup 2} (hg : IsNF g) : IsNF (zz ^ k * g) := by
  obtain ⟨m, e, bs, f, h1, h2, rfl⟩ := hg
  exact ⟨k + m, e, bs, f, h1, h2, by rw [← mul_assoc, ← zpow_add]⟩

theorem isNF_x {g : BraidGroup 2} (hg : IsNF g) : IsNF (xx * g) := by
  refine isNF_left xx comm_x ?_ hg
  intro e bs f h1 h2
  obtain rfl | rfl | rfl : e = -1 ∨ e = 0 ∨ e = 1 := by omega
  · exact ⟨0, 0, false :: bs, f, by norm_num, by norm_num, by
      simp [core, blocks_cons, blk, sgn, mul_assoc]⟩
  · rcases bs with _ | ⟨b, bs⟩
    · cases f
      · exact ⟨0, 0, [], true, by norm_num, by norm_num, by simp [core, blocks, tl]⟩
      · exact ⟨1, 0, [], false, by norm_num, by norm_num, by
          simp [core, blocks, tl, ← x_sq]⟩
    · refine ⟨1, sgn b, bs, f, by cases b <;> simp [sgn], by cases b <;> simp [sgn], ?_⟩
      simp only [core, blocks_cons, blk, zpow_zero, one_mul, zpow_one, ← x_sq, mul_assoc]
  · exact ⟨0, 0, true :: bs, f, by norm_num, by norm_num, by
      simp [core, blocks_cons, blk, sgn, mul_assoc]⟩

theorem isNF_y {g : BraidGroup 2} (hg : IsNF g) : IsNF (yy * g) := by
  refine isNF_left yy comm_y ?_ hg
  intro e bs f h1 h2
  obtain rfl | rfl | rfl : e = -1 ∨ e = 0 ∨ e = 1 := by omega
  · exact ⟨0, 0, bs, f, by norm_num, by norm_num, by simp [core, mul_assoc]⟩
  · exact ⟨0, 1, bs, f, by norm_num, by norm_num, by simp [core, mul_assoc]⟩
  · refine ⟨1, -1, bs, f, by norm_num, by norm_num, ?_⟩
    simp only [core, zpow_one, zpow_neg, ← mul_assoc, y_sq]

theorem isNF_yinv {g : BraidGroup 2} (hg : IsNF g) : IsNF (yy⁻¹ * g) := by
  refine isNF_left yy⁻¹ comm_y.inv_left ?_ hg
  intro e bs f h1 h2
  obtain rfl | rfl | rfl : e = -1 ∨ e = 0 ∨ e = 1 := by omega
  · refine ⟨-1, 1, bs, f, by norm_num, by norm_num, ?_⟩
    simp only [core, zpow_one, zpow_neg, ← mul_assoc, yinv_sq]
  · exact ⟨0, -1, bs, f, by norm_num, by norm_num, by simp [core, mul_assoc]⟩
  · exact ⟨0, 0, bs, f, by norm_num, by norm_num, by simp [core, mul_assoc]⟩

theorem isNF_xinv {g : BraidGroup 2} (hg : IsNF g) : IsNF (xx⁻¹ * g) := by
  have : xx⁻¹ * g = zz ^ (-1 : ℤ) * (xx * g) := by
    rw [← x_sq]; group
  rw [this]; exact isNF_zz _ (isNF_x hg)

/-- **Normal form.** Every braid in `B₃` is in normal form. -/
theorem isNF_all (g : BraidGroup 2) : IsNF g := by
  have hg : g ∈ Subgroup.closure (Set.range (PresentedGroup.of :
      Fin 2 → PresentedGroup (braidRelators 2))) := by
    rw [PresentedGroup.closure_range_of]; exact Subgroup.mem_top g
  induction hg using Subgroup.closure_induction_left with
  | one => exact ⟨0, 0, [], false, by norm_num, by norm_num, by simp [core, blocks, tl]⟩
  | mul_left u hu y _ ih =>
    obtain ⟨i, rfl⟩ := hu
    change IsNF (σ i * y)
    fin_cases i
    · change IsNF (σ 0 * y); rw [σ0_eq, mul_assoc]; exact isNF_yinv (isNF_x ih)
    · change IsNF (σ 1 * y); rw [σ1_eq, mul_assoc]; exact isNF_x (isNF_yinv ih)
  | inv_mul_cancel u hu y _ ih =>
    obtain ⟨i, rfl⟩ := hu
    change IsNF ((σ i)⁻¹ * y)
    fin_cases i
    · change IsNF ((σ 0)⁻¹ * y); rw [σ0_eq, mul_inv_rev, inv_inv, mul_assoc]
      exact isNF_xinv (isNF_y ih)
    · change IsNF ((σ 1)⁻¹ * y); rw [σ1_eq, mul_inv_rev, inv_inv, mul_assoc]
      exact isNF_y (isNF_xinv ih)

/-! ## Ping-pong in `SL(2, ℤ)` -/

/-- The integer matrix of `burauNeg g`. -/
def φ (g : BraidGroup 2) : Matrix (Fin 2) (Fin 2) ℤ := ↑(burauNeg g)

theorem φ_mul (g h : BraidGroup 2) : φ (g * h) = φ g * φ h := by
  simp [φ, Matrix.SpecialLinearGroup.coe_mul]

theorem φ_one : φ 1 = 1 := by simp [φ]

theorem φ_x : φ xx = !![0, 1; -1, 0] := by
  simp only [φ, xx, burauNeg_delta, Matrix.SpecialLinearGroup.coe_inv]
  ext i j; fin_cases i <;> fin_cases j <;> simp [S, Matrix.adjugate_fin_two]

theorem φ_y : φ yy = !![0, 1; -1, 1] := by
  simp only [yy, φ_mul]
  simp only [φ, burauNeg_σ]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [burauGen, Matrix.mul_apply, Fin.sum_univ_two]

theorem φ_yinv : φ yy⁻¹ = !![1, -1; 1, 0] := by
  simp only [φ, map_inv, Matrix.SpecialLinearGroup.coe_inv]
  have := φ_y; simp only [φ] at this; rw [this]
  ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.adjugate_fin_two]

theorem φ_z : φ zz = !![-1, 0; 0, -1] := by
  rw [← x_sq, φ_mul, φ_x]
  ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]

theorem φ_blk_true : φ (blk true) = !![-1, 1; 0, -1] := by
  simp only [blk, sgn, if_true, zpow_one, φ_mul, φ_x, φ_y]
  ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]

theorem φ_blk_false : φ (blk false) = !![1, 0; -1, 1] := by
  simp only [blk, sgn, Bool.false_eq_true, if_false, zpow_neg, zpow_one, φ_mul, φ_x, φ_yinv]
  ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]

/-- The ping-pong sign pattern: `[[+, −], [−, +]]` or `[[−, +], [+, −]]`, with non-zero
off-diagonal part. -/
def Good (M : Matrix (Fin 2) (Fin 2) ℤ) : Prop :=
  (0 ≤ M 0 0 ∧ M 0 1 ≤ 0 ∧ M 1 0 ≤ 0 ∧ 0 ≤ M 1 1 ∧ M 0 1 + M 1 0 ≤ -1) ∨
  (M 0 0 ≤ 0 ∧ 0 ≤ M 0 1 ∧ 0 ≤ M 1 0 ∧ M 1 1 ≤ 0 ∧ 1 ≤ M 0 1 + M 1 0)

theorem good_blk (b : Bool) : Good (φ (blk b)) := by
  cases b
  · rw [φ_blk_false]; left; simp
  · rw [φ_blk_true]; right; simp

theorem good_blk_mul (b : Bool) (M : Matrix (Fin 2) (Fin 2) ℤ) (hM : Good M) :
    Good (φ (blk b) * M) := by
  unfold Good at hM ⊢
  cases b
  · rw [φ_blk_false]; simp [Matrix.mul_apply, Fin.sum_univ_two]; omega
  · rw [φ_blk_true]; simp [Matrix.mul_apply, Fin.sum_univ_two]; omega

/-- **Ping-pong.** Every non-empty product of blocks has the sign pattern `Good`. -/
theorem good_blocks : ∀ (bs : List Bool), bs ≠ [] → Good (φ (blocks bs))
  | [], h => absurd rfl h
  | [b], _ => by simpa [blocks] using good_blk b
  | b :: c :: bs, _ => by
    rw [blocks_cons, φ_mul]
    exact good_blk_mul b _ (good_blocks (c :: bs) (List.cons_ne_nil _ _))

/-- If a normal form with `z`-exponent `0` or `1` maps to `1`, it is the empty word. -/
theorem nf_trivial (r e : ℤ) (bs : List Bool) (f : Bool) (hr : r = 0 ∨ r = 1)
    (h1 : -1 ≤ e) (h2 : e ≤ 1) (h : φ (zz ^ r * core e bs f) = 1) :
    r = 0 ∧ e = 0 ∧ bs = [] ∧ f = false := by
  have hP : (bs = [] ∧ φ (blocks bs) = 1) ∨ Good (φ (blocks bs)) := by
    rcases bs with _ | ⟨b, bs⟩
    · left; exact ⟨rfl, by simp [blocks, φ_one]⟩
    · right; exact good_blocks _ (List.cons_ne_nil _ _)
  simp only [core, φ_mul] at h
  generalize φ (blocks bs) = P at h hP
  obtain rfl | rfl | rfl : e = -1 ∨ e = 0 ∨ e = 1 := by omega
  all_goals
    rcases hr with rfl | rfl <;> cases f <;>
    simp only [tl, zpow_zero, zpow_one, zpow_neg, φ_one, φ_z, φ_x, φ_yinv, φ_y,
      Bool.false_eq_true, if_false, if_true, one_mul, mul_one] at h <;>
    have h00 := congrFun (congrFun h 0) 0 <;>
    have h01 := congrFun (congrFun h 0) 1 <;>
    have h10 := congrFun (congrFun h 1) 0 <;>
    have h11 := congrFun (congrFun h 1) 1 <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.vecMul, dotProduct] at h00 h01 h10 h11 <;>
    rcases hP with ⟨hb, rfl⟩ | hG <;>
    first
    | exact ⟨rfl, rfl, hb, rfl⟩
    | (exfalso; simp at h00 h01 h10 h11)
    | (exfalso; unfold Good at hG; omega)

end KernelProof

open KernelProof in
/-- **The kernel of `burauNeg : B₃ → SL(2, ℤ)` is `⟨Δ⁴⟩`.** -/
theorem kernelIsDeltaFour : KernelIsDeltaFour := by
  intro g hg
  obtain ⟨m, e, bs, f, h1, h2, rfl⟩ := isNF_all g
  have hm : zz ^ m = (delta ^ 4) ^ (m / 2) * zz ^ (m % 2) := by
    have : (delta ^ 4 : BraidGroup 2) = zz ^ (2 : ℤ) := by
      simp only [zz, zpow_ofNat, ← pow_mul]
    rw [this, ← zpow_mul, ← zpow_add, Int.mul_ediv_add_emod]
  have hk : burauNeg ((delta ^ 4) ^ (m / 2)) = 1 := by
    rw [map_zpow, burauNeg_delta_four, one_zpow]
  have h' : φ (zz ^ (m % 2) * core e bs f) = 1 := by
    have := congrArg (fun A : Matrix.SpecialLinearGroup (Fin 2) ℤ =>
      (A : Matrix (Fin 2) (Fin 2) ℤ)) hg
    simp only [hm, mul_assoc, map_mul, hk, one_mul] at this
    simpa [φ, map_mul] using this
  obtain ⟨hr, rfl, rfl, rfl⟩ := nf_trivial (m % 2) e bs f (by omega) h1 h2 h'
  refine ⟨m / 2, ?_⟩
  rw [hm, hr]; simp [core, blocks, tl]

/-- `isConj_of_burauNeg_isConj` with its kernel hypothesis discharged: writhe-0 braids
with conjugate `SL(2, ℤ)` images are conjugate in `B₃`. -/
theorem isConj_of_burauNeg_isConj' {g h : BraidGroup 2}
    (hg : exponentSum 2 g = 1) (hh : exponentSum 2 h = 1)
    (hc : IsConj (burauNeg g) (burauNeg h)) : IsConj g h :=
  isConj_of_burauNeg_isConj kernelIsDeltaFour hg hh hc

end QOU.Mass.BorromeanWordForcing
