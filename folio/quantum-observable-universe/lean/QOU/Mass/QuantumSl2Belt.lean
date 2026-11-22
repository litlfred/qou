import QOU.Mass.QuantumSl2HighestWeight

/-!
# The belt: partial quantum trace of the monodromy

Stage 2d of deriving Zheng's tangle functions. Let `M = Ř′Ř` be the double braiding on
`V_{m+1} ⊗ V_{m'+1}`. Its partial quantum trace over the second factor,

    T_{ij} = Σ_r q^{m'−2r} M_{(i,r),(j,r)},

is the operator that a closed `V_{m'+1}`-coloured belt induces on a `V_{m+1}`-coloured strand.
We show `T` is the scalar `Σ_r q^{(m+1)(m'−2r)}`, and that this scalar times `[m+1]` is
`[(m+1)(m'+1)]`: the belt is `[ab]/[b]` with `a = m'+1`, `b = m+1`.

The proof uses only that `M` commutes with `Δ(F)` (`monodromy_deltaF`) and the explicit
entries of `M` at the top vectors `v_0 ⊗ v_r`. No Clebsch–Gordan basis is needed.

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, proof of Lemma 1
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

section Belt

variable (s : 𝕜) (hs : s ≠ 0)

/-- `Ř` preserves the grading `p + r`. -/
theorem rCheckMat_grade (m m' : ℕ) (y : Fin (m' + 1) × Fin (m + 1)) (x : Fin (m + 1) × Fin (m' + 1))
    (h : (y.1 : ℕ) + y.2 ≠ x.1 + x.2) : rCheckMat s hs m m' y x = 0 := by
  unfold rCheckMat rMat cartanTheta
  rw [submatrix_apply, diagonal_mul, rSum_apply_grade s hs m m' _ _ _ (by simp [Prod.swap]; omega),
    mul_zero]

/-- The monodromy `M = Ř′Ř` on `V_{m+1} ⊗ V_{m'+1}`. -/
def mono (m m' : ℕ) : Matrix (Fin (m + 1) × Fin (m' + 1)) (Fin (m + 1) × Fin (m' + 1)) 𝕜 :=
  rCheckMat s hs m' m * rCheckMat s hs m m'

/-- `M` preserves the grading `p + r`. -/
theorem mono_grade (m m' : ℕ) (x y : Fin (m + 1) × Fin (m' + 1))
    (h : (x.1 : ℕ) + x.2 ≠ y.1 + y.2) : mono s hs m m' x y = 0 := by
  unfold mono
  rw [mul_apply]
  refine Finset.sum_eq_zero fun z _ => ?_
  by_cases hz : (z.1 : ℕ) + z.2 = y.1 + y.2
  · rw [rCheckMat_grade s hs m' m x z (by omega), zero_mul]
  · rw [rCheckMat_grade s hs m m' z y hz, mul_zero]

/-- The column of `S` at `v_0 ⊗ v_r` is the unit column (`E` kills `v_0`). -/
theorem rSum_apply_col0 (m m' M : ℕ) (r : Fin (m' + 1)) (x : Fin (m + 1) × Fin (m' + 1)) :
    Rep.rSum s (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m') M x (⟨0, by omega⟩, r)
      = if x = (⟨0, by omega⟩, r) then 1 else 0 := by
  unfold Rep.rSum
  rw [Matrix.sum_apply, Finset.sum_eq_single 0]
  · simp only [Matrix.smul_apply, kroneckerMap_apply, pow_zero, one_apply, smul_eq_mul]
    have hc : rcoef s 0 = 1 := by simp [rcoef, qfact]
    rw [hc, one_mul]
    by_cases hx : x = (⟨0, by omega⟩, r)
    · subst hx; simp
    · rw [if_neg hx]
      by_cases h1 : x.1 = (⟨0, by omega⟩ : Fin (m + 1))
      · have h2 : x.2 ≠ r := by
          intro h2; apply hx; ext <;> simp [h1, h2]
        rw [if_neg h2, mul_zero]
      · rw [if_neg h1, zero_mul]
  · intro n _ hn
    rw [Matrix.smul_apply, kroneckerMap_apply,
      show (irrep (pow_ne_zero 2 hs) m).E = irrepE (s ^ 2) m from rfl,
      irrepE_pow_apply (s ^ 2) m n x.1 _ (by simp; omega), zero_mul, smul_zero]
  · simp

/-- **The top diagonal entries of the monodromy:** `M_{(0,r),(0,r)} = s^{2 m (m'−2r)}`. -/
theorem mono_top (m m' : ℕ) (r : Fin (m' + 1)) :
    mono s hs m m' (⟨0, by omega⟩, r) (⟨0, by omega⟩, r) = s ^ (2 * ((m : ℤ) * wt m' r)) := by
  unfold mono
  rw [mul_apply, Finset.sum_eq_single (r, ⟨0, by omega⟩)]
  · unfold rCheckMat rMat cartanTheta
    simp only [submatrix_apply, diagonal_mul, Prod.swap, id]
    rw [rSum_apply_top s hs m' m _ r r.isLt, rSum_apply_col0 s hs m m' _ r]
    simp only [if_true]
    have h0 : wt m 0 = m := by simp [wt]
    rw [mul_one, mul_one, ← zpow_add₀ hs, h0]
    congr 1; ring
  · intro z _ hz
    unfold rCheckMat rMat cartanTheta
    simp only [submatrix_apply, diagonal_mul, id]
    rw [rSum_apply_col0 s hs m m' _ r, if_neg, mul_zero, mul_zero]
    intro h; apply hz
    rcases z with ⟨z1, z2⟩
    simp only [Prod.swap, Prod.mk.injEq] at h
    rw [h.1, h.2]
  · simp

/-- **The belt operator**: the partial quantum trace of `M` over `V_{m'+1}`,
`T_{ij} = Σ_r q^{m'−2r} M_{(i,r),(j,r)}` with `q = s²`. -/
def beltOp (m m' : ℕ) : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜 :=
  fun i j => ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * mono s hs m m' (i, r) (j, r)

/-- `T` is diagonal. -/
theorem beltOp_offdiag (m m' : ℕ) (i j : Fin (m + 1)) (h : i ≠ j) : beltOp s hs m m' i j = 0 := by
  unfold beltOp
  refine Finset.sum_eq_zero fun r _ => ?_
  rw [mono_grade s hs m m' _ _ (by simp; omega), mul_zero]

/-- The top entry `T_{00} = Σ_r q^{(m+1)(m'−2r)}`. -/
theorem beltOp_top (m m' : ℕ) :
    beltOp s hs m m' ⟨0, by omega⟩ ⟨0, by omega⟩
      = ∑ r : Fin (m' + 1), s ^ (2 * (((m : ℤ) + 1) * wt m' r)) := by
  unfold beltOp
  refine Finset.sum_congr rfl fun r _ => ?_
  rw [mono_top, ← zpow_add₀ hs]
  congr 1; ring

/-- Entries of `Δ(F)`. -/
theorem deltaF_apply (q : 𝕜) (m m' : ℕ) (x y : Fin (m + 1) × Fin (m' + 1)) :
    deltaF q m m' x y = irrepKm q m x.1 y.1 * irrepF q m' x.2 y.2
      + irrepF q m x.1 y.1 * (1 : Matrix (Fin (m' + 1)) (Fin (m' + 1)) 𝕜) x.2 y.2 := by
  simp [deltaF, kroneckerMap_apply]

theorem irrepKm_apply_eq (s : 𝕜) (hs : s ≠ 0) (m : ℕ) (i j : Fin (m + 1)) :
    irrepKm (s ^ 2) m i j = if i = j then s ^ (-(2 * wt m j)) else 0 := by
  unfold irrepKm
  rw [diagonal_apply]
  split_ifs with h
  · subst h; exact irrepKm_diag_eq s hs (Nat.lt_succ_iff.mp i.isLt)
  · rfl

/-- `(M Δ(F))_{(a,r),(b,r)}` for `a = b+1`. -/
theorem mono_deltaF_apply (m m' : ℕ) (a b : Fin (m + 1)) (hab : (a : ℕ) = b + 1)
    (r : Fin (m' + 1)) :
    (mono s hs m m' * deltaF (s ^ 2) m m') (a, r) (b, r)
      = qint (s ^ 2) (b + 1) * mono s hs m m' (a, r) (a, r)
        + s ^ (-(2 * wt m b)) * ∑ y, mono s hs m m' (a, r) (b, y) * irrepF (s ^ 2) m' y r := by
  rw [mul_apply, Fintype.sum_prod_type]
  simp only [deltaF_apply, mul_add, Finset.sum_add_distrib, irrepKm_apply_eq s hs]
  rw [add_comm]
  congr 1
  · rw [Finset.sum_eq_single a]
    · rw [Finset.sum_eq_single r]
      · simp [irrepF, hab, mul_comm]
      · intro y _ hy; rw [one_apply, if_neg hy]; ring
      · simp
    · intro x _ hx
      refine Finset.sum_eq_zero fun y _ => ?_
      have : irrepF (s ^ 2) m x b = 0 := by
        simp only [irrepF]; rw [if_neg]; intro h; apply hx; ext; omega
      rw [this]; ring
    · simp
  · rw [Finset.sum_eq_single b]
    · simp only [if_true, Finset.mul_sum]
      refine Finset.sum_congr rfl fun y _ => ?_
      ring
    · intro x _ hx
      refine Finset.sum_eq_zero fun y _ => ?_
      rw [if_neg hx]; ring
    · simp

/-- `(Δ(F) M)_{(a,r),(b,r)}` for `a = b+1`. -/
theorem deltaF_mono_apply (m m' : ℕ) (a b : Fin (m + 1)) (hab : (a : ℕ) = b + 1)
    (r : Fin (m' + 1)) :
    (deltaF (s ^ 2) m m' * mono s hs m m') (a, r) (b, r)
      = qint (s ^ 2) (b + 1) * mono s hs m m' (b, r) (b, r)
        + s ^ (-(2 * wt m a)) * ∑ y, irrepF (s ^ 2) m' r y * mono s hs m m' (a, y) (b, r) := by
  rw [mul_apply, Fintype.sum_prod_type]
  simp only [deltaF_apply, add_mul, Finset.sum_add_distrib, irrepKm_apply_eq s hs]
  rw [add_comm]
  congr 1
  · rw [Finset.sum_eq_single b]
    · rw [Finset.sum_eq_single r]
      · simp [irrepF, hab]
      · intro y _ hy; rw [one_apply, if_neg (Ne.symm hy)]; ring
      · simp
    · intro x _ hx
      refine Finset.sum_eq_zero fun y _ => ?_
      have : irrepF (s ^ 2) m a x = 0 := by
        simp only [irrepF]; rw [if_neg]; intro h; apply hx; ext; omega
      rw [this]; ring
    · simp
  · rw [Finset.sum_eq_single a]
    · simp only [if_true, Finset.mul_sum]
      refine Finset.sum_congr rfl fun y _ => ?_
      ring
    · intro x _ hx
      refine Finset.sum_eq_zero fun y _ => ?_
      rw [if_neg (Ne.symm hx)]; ring
    · simp

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hq2 in
/-- **The belt is constant along the `F`-chain:** `[b+1] T_{b+1,b+1} = [b+1] T_{bb}`. -/
theorem beltOp_step (m m' : ℕ) (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0)
    (a b : Fin (m + 1)) (hab : (a : ℕ) = b + 1) :
    qint (s ^ 2) (b + 1) * beltOp s hs m m' a a = qint (s ^ 2) (b + 1) * beltOp s hs m m' b b := by
  have hc : mono s hs m m' * deltaF (s ^ 2) m m' = deltaF (s ^ 2) m m' * mono s hs m m' :=
    monodromy_deltaF s hs hq2 m m' hint
  have hsum : ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (mono s hs m m' * deltaF (s ^ 2) m m') (a, r) (b, r)
      = ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (deltaF (s ^ 2) m m' * mono s hs m m') (a, r) (b, r) := by
    rw [hc]
  simp only [mono_deltaF_apply s hs m m' a b hab, deltaF_mono_apply s hs m m' a b hab, mul_add,
    Finset.sum_add_distrib] at hsum
  have hcross : ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (s ^ (-(2 * wt m b)) *
        ∑ y, mono s hs m m' (a, r) (b, y) * irrepF (s ^ 2) m' y r)
      = ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (s ^ (-(2 * wt m a)) *
        ∑ y, irrepF (s ^ 2) m' r y * mono s hs m m' (a, y) (b, r)) := by
    simp only [Finset.mul_sum]
    rw [Finset.sum_comm (f := fun (r y : Fin (m' + 1)) => s ^ (2 * wt m' r) * (s ^ (-(2 * wt m a)) *
      (irrepF (s ^ 2) m' r y * mono s hs m m' (a, y) (b, r))))]
    refine Finset.sum_congr rfl fun r _ => Finset.sum_congr rfl fun y _ => ?_
    by_cases h : (y : ℕ) = r + 1
    · have he : s ^ (2 * wt m' r) * s ^ (-(2 * wt m b)) = s ^ (2 * wt m' y) * s ^ (-(2 * wt m a)) := by
        rw [← zpow_add₀ hs, ← zpow_add₀ hs]
        congr 1; unfold wt; omega
      calc s ^ (2 * wt m' r) * (s ^ (-(2 * wt m b)) * (mono s hs m m' (a, r) (b, y) * irrepF (s ^ 2) m' y r))
          = (s ^ (2 * wt m' r) * s ^ (-(2 * wt m b))) * (irrepF (s ^ 2) m' y r * mono s hs m m' (a, r) (b, y)) := by ring
        _ = _ := by rw [he]; ring
    · have hF : irrepF (s ^ 2) m' y r = 0 := by simp only [irrepF]; rw [if_neg h]
      rw [hF]; ring
  rw [hcross] at hsum
  have h := add_right_cancel hsum
  unfold beltOp
  simp only [Finset.mul_sum]
  calc ∑ r : Fin (m' + 1), qint (s ^ 2) (b + 1) * (s ^ (2 * wt m' r) * mono s hs m m' (a, r) (a, r))
      = ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (qint (s ^ 2) (b + 1) * mono s hs m m' (a, r) (a, r)) :=
        Finset.sum_congr rfl fun r _ => by ring
    _ = ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (qint (s ^ 2) (b + 1) * mono s hs m m' (b, r) (b, r)) := h
    _ = _ := Finset.sum_congr rfl fun r _ => by ring

include hq2 in
/-- **The belt is a scalar.** If `[k] ≠ 0` for `1 ≤ k ≤ m`, then `T = T_{00} · 1`. -/
theorem beltOp_eq_smul_one (m m' : ℕ) (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0)
    (hstr : ∀ k < m, qint (s ^ 2) (k + 1) ≠ 0) :
    beltOp s hs m m' = beltOp s hs m m' ⟨0, by omega⟩ ⟨0, by omega⟩ • (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) := by
  have hdiag : ∀ (i : ℕ) (hi : i < m + 1), beltOp s hs m m' ⟨i, hi⟩ ⟨i, hi⟩
      = beltOp s hs m m' ⟨0, by omega⟩ ⟨0, by omega⟩ := by
    intro i
    induction i with
    | zero => intro hi; rfl
    | succ i ih =>
      intro hi
      have hst := beltOp_step s hs hq2 m m' hint ⟨i + 1, hi⟩ ⟨i, by omega⟩ rfl
      rw [← ih (by omega)]
      exact mul_left_cancel₀ (hstr i (by omega)) hst
  ext i j
  rw [smul_apply, one_apply, smul_eq_mul]
  by_cases h : i = j
  · subst h; rw [if_pos rfl, mul_one]; exact hdiag i i.isLt
  · rw [if_neg h, mul_zero]; exact beltOp_offdiag s hs m m' i j h

/-- The geometric identity `(x − x⁻¹) Σ_{r ≤ n} x^{n−2r} = x^{n+1} − x^{−(n+1)}`. -/
theorem geom_wt (x : 𝕜) (hx : x ≠ 0) (n : ℕ) :
    (x - x⁻¹) * ∑ r : Fin (n + 1), x ^ wt n r = x ^ ((n : ℤ) + 1) - x ^ (-((n : ℤ) + 1)) := by
  rw [Fin.sum_univ_eq_sum_range (fun r => x ^ wt n r)]
  induction n with
  | zero => simp [wt, zpow_neg]
  | succ n ih =>
    have hshift : ∑ r ∈ Finset.range (n + 1), x ^ wt (n + 1) r = x * ∑ r ∈ Finset.range (n + 1), x ^ wt n r := by
      rw [Finset.mul_sum]
      refine Finset.sum_congr rfl fun r _ => ?_
      rw [← zpow_one_add₀ hx]; congr 1; unfold wt; push_cast; ring
    rw [Finset.sum_range_succ, hshift, mul_add, ← mul_assoc, mul_comm (x - x⁻¹) x, mul_assoc, ih]
    have hl : wt (n + 1) (n + 1) = -((n : ℤ) + 1) := by unfold wt; push_cast; ring
    rw [hl]
    have e1 : x * x ^ ((n : ℤ) + 1) = x ^ (((n + 1 : ℕ) : ℤ) + 1) := by
      rw [← zpow_one_add₀ hx]; congr 1; push_cast; ring
    have e2 : x * x ^ (-((n : ℤ) + 1)) = x ^ (-(n : ℤ)) := by
      rw [← zpow_one_add₀ hx]; congr 1; ring
    have e3 : x⁻¹ * x ^ (-((n : ℤ) + 1)) = x ^ (-(((n + 1 : ℕ) : ℤ) + 1)) := by
      rw [← zpow_neg_one, ← zpow_add₀ hx]; congr 1; push_cast; ring
    have e4 : x * x ^ (-((n : ℤ) + 1)) = x ^ (-(n : ℤ)) := e2
    rw [mul_sub, e1, e2, sub_mul, e2, e3]
    ring

include hs hq2 in
/-- **The belt value.** `[m+1] · Σ_r q^{(m+1)(m'−2r)} = [(m+1)(m'+1)]`, i.e. the belt of colour
`a = m'+1` around a strand of colour `b = m+1` is `[ab]/[b]`. -/
theorem belt_value (m m' : ℕ) :
    qint (s ^ 2) (m + 1) * ∑ r : Fin (m' + 1), s ^ (2 * (((m : ℤ) + 1) * wt m' r))
      = qint (s ^ 2) ((m + 1) * (m' + 1)) := by
  set x : 𝕜 := s ^ (2 * ((m : ℤ) + 1)) with hxdef
  have hx : x ≠ 0 := zpow_ne_zero _ hs
  have hterm : ∀ r : Fin (m' + 1), s ^ (2 * (((m : ℤ) + 1) * wt m' r)) = x ^ wt m' r := by
    intro r; rw [hxdef, ← zpow_mul]; congr 1; ring
  simp only [hterm]
  have hg := geom_wt x hx m'
  have hq1 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0 := hq2
  have hpow : ∀ k : ℕ, (s ^ 2) ^ k = s ^ ((2 : ℤ) * k) := by
    intro k; rw [← pow_mul, ← zpow_natCast]; norm_cast
  have hxq : x - x⁻¹ = qint (s ^ 2) (m + 1) * (s ^ 2 - (s ^ 2)⁻¹) := by
    unfold qint
    rw [div_mul_cancel₀ _ hq1, inv_pow, hpow, hxdef]
    push_cast; ring_nf
  have hR : x ^ ((m' : ℤ) + 1) - x ^ (-((m' : ℤ) + 1))
      = qint (s ^ 2) ((m + 1) * (m' + 1)) * (s ^ 2 - (s ^ 2)⁻¹) := by
    unfold qint
    rw [div_mul_cancel₀ _ hq1, inv_pow, hpow, zpow_neg, hxdef, ← zpow_mul]
    push_cast; ring_nf
  rw [hxq, hR, mul_assoc, mul_comm (s ^ 2 - (s ^ 2)⁻¹), ← mul_assoc] at hg
  exact mul_right_cancel₀ hq1 (by linear_combination hg)

include hq2 in
/-- **The belt (Zheng's `B`).** A closed `V_{m'+1}`-coloured belt around a `V_{m+1}`-coloured
strand acts as the scalar `[(m+1)(m'+1)]/[m+1]`: `[m+1] · T = [(m+1)(m'+1)] · 1`.
For `m = 2n`, `m' = N−1` this is `B(n) = [N(2n+1)]/[2n+1]`. -/
theorem belt_eq (m m' : ℕ) (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0)
    (hstr : ∀ k < m, qint (s ^ 2) (k + 1) ≠ 0) :
    qint (s ^ 2) (m + 1) • beltOp s hs m m'
      = qint (s ^ 2) ((m + 1) * (m' + 1)) • (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) := by
  rw [beltOp_eq_smul_one s hs hq2 m m' hint hstr, smul_smul, beltOp_top,
    belt_value s hs hq2 m m']

include hq2 in
/-- **The twist (Zheng's `T`).** On the string `Δ(F)^i w_{m−n}` generating the summand
`V_{2n+1} ⊂ V_{m+1} ⊗ V_{m+1}`, the full twist `M = Ř′Ř`, corrected to zero framing by the factor
`q^{m(m+2)} = θ_{V_{m+1}}²`, acts by `q^{2n(n+1)} = θ_{V_{2n+1}}`. With `m = N−1` and `t = q²`
this is `T(n,t) = t^{n(n+1)}`, the framing factor being `t^{(N²−1)/2}`. -/
theorem twist_eq (m n i : ℕ) (hn : n ≤ m) (hint : ∀ k < rOrder m m, qint (s ^ 2) (k + 1) ≠ 0)
    (hint1 : ∀ p < m - n, qint (s ^ 2) (m - p) ≠ 0) :
    (s ^ 2) ^ ((m : ℤ) * (m + 2)) • (mono s hs m m *ᵥ
        (deltaF (s ^ 2) m m ^ i *ᵥ hwVec (s ^ 2) m m (m - n)))
      = (s ^ 2) ^ (2 * (n : ℤ) * (n + 1)) •
        (deltaF (s ^ 2) m m ^ i *ᵥ hwVec (s ^ 2) m m (m - n)) := by
  unfold mono
  rw [monodromy_deltaF_pow_hwVec s hs hq2 m m (m - n) i (by omega) (by omega) hint hint1 hint1,
    smul_smul, ← zpow_add₀ (pow_ne_zero 2 hs)]
  congr 2
  push_cast [Nat.cast_sub hn]
  ring

end Belt

end QOU.Mass.QuantumSl2
