import QOU.Mass.QuantumSl2Belt

/-!
# The clasp: closed forms

Stage 3 of deriving Zheng's tangle functions (van der Veen 2008, Lemma 1). The clasp tangle
has antiparallel strands, so it is the monodromy `M = Ř′Ř` turned through 90°:
`X = (cap ⊗ 1 ⊗ 1)(1 ⊗ M ⊗ 1)(1 ⊗ 1 ⊗ cup)`. Read at the output `v_j ⊗ v_0`, the eigenvalue
of `X` on `w_j` is a sum over the support `v_k ⊗ v_{j−k}` of `w_j`, and each summand is a
single product of `q`-integers equal to van der Veen's `k`-th term (checked exactly in
`computations/whitehead_clasp_rotated_monodromy_check.py`).

This file proves that term identity (`claspTerm_eq_vdvTerm`), sorry-free, from closed forms of
the highest-weight coefficients and of the entries of `Eⁿ`, `Fⁿ`. It treats the cup and cap
coefficients as given numbers; their invariance (and the snake identity) is a separate step.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, proof of Lemma 1
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VII, XIV
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

theorem qfact_succ (q : 𝕜) (n : ℕ) : qfact q (n + 1) = qfact q n * qint q (n + 1) := by
  unfold qfact; rw [Finset.prod_range_succ]

/-- Rising product: `[a]! · Π_{i<k} [a+i+1] = [a+k]!`. -/
theorem qfact_mul_prod_up (q : 𝕜) (a k : ℕ) :
    qfact q a * ∏ i ∈ Finset.range k, qint q (a + i + 1) = qfact q (a + k) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Finset.prod_range_succ, ← mul_assoc, ih, ← Nat.add_assoc, qfact_succ]

/-- Falling product: `[m−k]! · Π_{i<k} [m−i] = [m]!` for `k ≤ m`. -/
theorem qfact_mul_prod_down (q : 𝕜) (m k : ℕ) (hk : k ≤ m) :
    qfact q (m - k) * ∏ i ∈ Finset.range k, qint q (m - i) = qfact q m := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Finset.prod_range_succ, ← ih (by omega),
      show m - k = (m - (k + 1)) + 1 by omega, qfact_succ,
      show m - (k + 1) + 1 = m - k by omega]
    ring

/-- `Σ_{i<k} (m − 2(j−1−i)) = k (m − 2j + k + 1)` for `k ≤ j`. -/
theorem sum_wt_hw (m j k : ℕ) (hk : k ≤ j) :
    ∑ i ∈ Finset.range k, wt m (j - 1 - i) = (k : ℤ) * ((m : ℤ) - 2 * j + k + 1) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ, ih (by omega)]
    unfold wt
    rw [show j - 1 - k = j - (k + 1) by omega, Nat.cast_sub hk]
    push_cast; ring

/-- **Closed form of the highest-weight coefficients** in `V_{m+1} ⊗ V_{m+1}`:
`a_k^{(j)} [m]! [m−j]! = (−1)^k q^{−k(m−2j+k+1)} [m−k]! [m−j+k]!`. -/
theorem hwCoef_closed (q : 𝕜) (hq : q ≠ 0) (m j k : ℕ) (hkj : k ≤ j) (hjm : j ≤ m)
    (hint : ∀ i < k, qint q (m - i) ≠ 0) :
    hwCoef q m m j k * qfact q m * qfact q (m - j)
      = (-1) ^ k * q ^ (-((k : ℤ) * ((m : ℤ) - 2 * j + k + 1)))
          * qfact q (m - k) * qfact q (m - j + k) := by
  have h := hwCoef_mul_prod q hq m m j k hint
  rw [sum_wt_hw m j k hkj] at h
  have hd := qfact_mul_prod_down q m k (by omega)
  have hu := qfact_mul_prod_up q (m - j) k
  rw [← hd, ← hu]
  calc hwCoef q m m j k * (qfact q (m - k) * ∏ i ∈ Finset.range k, qint q (m - i)) * qfact q (m - j)
      = (hwCoef q m m j k * ∏ i ∈ Finset.range k, qint q (m - i)) * qfact q (m - k)
          * qfact q (m - j) := by ring
    _ = _ := by rw [h]; ring

/-- Entries of `Eⁿ`: `(Eⁿ)_{a,b} = Π_{l<n} [m−a−l]` when `b = a + n`. -/
theorem irrepE_pow_entry (q : 𝕜) (m n : ℕ) (a b : Fin (m + 1)) (hab : (b : ℕ) = a + n) :
    (irrepE q m ^ n) a b = ∏ l ∈ Finset.range n, qint q (m - a - l) := by
  induction n generalizing a with
  | zero =>
    have : a = b := by ext; omega
    subst this; simp
  | succ n ih =>
    have ha : (a : ℕ) + 1 < m + 1 := by omega
    rw [pow_succ', mul_apply, Finset.sum_eq_single ⟨a + 1, ha⟩]
    · rw [ih ⟨a + 1, ha⟩ (by simp; omega), Finset.prod_range_succ']
      simp only [irrepE, if_true]
      rw [mul_comm]
      congr 1
      · refine Finset.prod_congr rfl fun l _ => ?_
        congr 1; omega
      · congr 1; omega
    · intro x _ hx
      have : irrepE q m a x = 0 := by
        simp only [irrepE]; rw [if_neg]; intro h'; apply hx; ext; simp; omega
      rw [this, zero_mul]
    · simp

/-- Entries of `Fⁿ`: `(Fⁿ)_{b,a} = Π_{l<n} [a+l+1]` when `b = a + n`. -/
theorem irrepF_pow_entry (q : 𝕜) (m n : ℕ) (a b : Fin (m + 1)) (hab : (b : ℕ) = a + n) :
    (irrepF q m ^ n) b a = ∏ l ∈ Finset.range n, qint q (a + l + 1) := by
  induction n generalizing a with
  | zero =>
    have : a = b := by ext; omega
    subst this; simp
  | succ n ih =>
    have ha : (a : ℕ) + 1 < m + 1 := by omega
    rw [pow_succ, mul_apply, Finset.sum_eq_single ⟨a + 1, ha⟩]
    · rw [ih ⟨a + 1, ha⟩ (by simp; omega), Finset.prod_range_succ']
      simp only [irrepF]
      rw [if_pos (by simp)]
      congr 1
      refine Finset.prod_congr rfl fun l _ => ?_
      congr 1; simp; omega
    · intro x _ hx
      have : irrepF q m x a = 0 := by
        simp only [irrepF]; rw [if_neg]; intro h'; apply hx; ext; simp; omega
      rw [this, mul_zero]
    · simp

section ClaspEntry

variable (s : 𝕜) (hs : s ≠ 0)

/-- The column of `S` at `v_p ⊗ v_m` is the unit column (`F` kills `v_m`). -/
theorem rSum_apply_colBot (m m' M : ℕ) (p : Fin (m + 1)) (x : Fin (m + 1) × Fin (m' + 1)) :
    Rep.rSum s (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m') M x (p, ⟨m', by omega⟩)
      = if x = (p, ⟨m', by omega⟩) then 1 else 0 := by
  unfold Rep.rSum
  rw [Matrix.sum_apply, Finset.sum_eq_single 0]
  · simp only [Matrix.smul_apply, kroneckerMap_apply, pow_zero, one_apply, smul_eq_mul]
    have hc : rcoef s 0 = 1 := by simp [rcoef, qfact]
    rw [hc, one_mul]
    by_cases hx : x = (p, ⟨m', by omega⟩)
    · subst hx; simp
    · rw [if_neg hx]
      by_cases h1 : x.1 = p
      · have h2 : x.2 ≠ ⟨m', by omega⟩ := by
          intro h2; apply hx; ext <;> simp [h1, h2]
        rw [if_neg h2, mul_zero]
      · rw [if_neg h1, zero_mul]
  · intro n _ hn
    rw [Matrix.smul_apply, kroneckerMap_apply,
      show (irrep (pow_ne_zero 2 hs) m').F = irrepF (s ^ 2) m' from rfl,
      irrepF_pow_apply (s ^ 2) m' n x.2 _ (by have := x.2.isLt; simp; omega), mul_zero, smul_zero]
  · simp

/-- **The clasp entry of the monodromy**, a single product:
`M_{(m−k, j),(j−k, m)} = s^{wt(m)wt(j−k)} s^{wt(j)wt(m−k)} c_{m−j} (E^{m−j})_{j,m} (F^{m−j})_{m−k,j−k}`. -/
theorem mono_clasp_entry (m j k : ℕ) (hkj : k ≤ j) (hjm : j ≤ m) :
    mono s hs m m (⟨m - k, by omega⟩, ⟨j, by omega⟩) (⟨j - k, by omega⟩, ⟨m, by omega⟩)
      = s ^ (wt m m * wt m (j - k)) * s ^ (wt m j * wt m (m - k)) * rcoef s (m - j)
        * (irrepE (s ^ 2) m ^ (m - j)) ⟨j, by omega⟩ ⟨m, by omega⟩
        * (irrepF (s ^ 2) m ^ (m - j)) ⟨m - k, by omega⟩ ⟨j - k, by omega⟩ := by
  unfold mono
  rw [mul_apply, Finset.sum_eq_single (⟨m, by omega⟩, ⟨j - k, by omega⟩)]
  · unfold rCheckMat rMat cartanTheta
    simp only [submatrix_apply, diagonal_mul, Prod.swap, id]
    rw [rSum_apply_colBot s hs m m _ _ (⟨j - k, by omega⟩, ⟨m, by omega⟩), if_pos rfl, mul_one]
    unfold Rep.rSum
    rw [Matrix.sum_apply, Finset.sum_eq_single (m - j)]
    · simp only [Matrix.smul_apply, kroneckerMap_apply, smul_eq_mul]
      rw [show (irrep (pow_ne_zero 2 hs) m).E = irrepE (s ^ 2) m from rfl,
        show (irrep (pow_ne_zero 2 hs) m).F = irrepF (s ^ 2) m from rfl,
        mul_comm (wt m (j - k)) (wt m m)]
      ring
    · intro n _ hn
      rw [Matrix.smul_apply, kroneckerMap_apply,
        show (irrep (pow_ne_zero 2 hs) m).E = irrepE (s ^ 2) m from rfl,
        irrepE_pow_apply (s ^ 2) m n _ _ (by simp; omega), zero_mul, smul_zero]
    · intro h; exfalso; exact h (Finset.mem_range.mpr (by unfold rOrder; omega))
  · intro z _ hz
    unfold rCheckMat rMat cartanTheta
    simp only [submatrix_apply, diagonal_mul, id]
    rw [rSum_apply_colBot s hs m m _ _ (z.swap), if_neg, mul_zero, mul_zero]
    intro h; apply hz
    rcases z with ⟨z1, z2⟩
    simp only [Prod.swap, Prod.mk.injEq] at h
    rw [h.1, h.2]
  · simp

end ClaspEntry

/-! ## The per-term identity

With `m = k + a + n` and `j = k + a` (so `n = m − j`, the vdV index), the `k`-th summand of the
clasp eigenvalue at output `v_j ⊗ v_0` is
`(a_k(j)/a_j(j)) · b_k · a_m · M_{(m−k, j),(j−k, m)}`, where `a_p(j)` are the coefficients of the
highest-weight vector `w_j` and `a_p = a_p(m)`, `b_p` are the cup and cap coefficients.
`claspTerm_eq_vdvTerm` shows it equals van der Veen's `k`-th summand. -/

section ClaspTerm
variable (s : 𝕜) (hs : s ≠ 0)

include hs in
theorem sq_zpow_split (z : ℤ) (P Q : ℕ) (h : z = (P : ℤ) - Q) :
    (s ^ 2) ^ z = s ^ (2 * P) / s ^ (2 * Q) := by
  rw [h, zpow_sub₀ (pow_ne_zero 2 hs), zpow_natCast, zpow_natCast, ← pow_mul, ← pow_mul]

include hs in
theorem s_zpow_split (z : ℤ) (P Q : ℕ) (h : z = (P : ℤ) - Q) :
    s ^ z = s ^ P / s ^ Q := by
  rw [h, zpow_sub₀ hs, zpow_natCast, zpow_natCast]

theorem qfact_ne_zero' (N : ℕ) (hint : ∀ i, 0 < i → i ≤ N → qint (s ^ 2) i ≠ 0) (i : ℕ)
    (hi : i ≤ N) : qfact (s ^ 2) i ≠ 0 := by
  unfold qfact
  exact Finset.prod_ne_zero_iff.mpr (fun r hr => hint _ (by omega)
    (by have := Finset.mem_range.mp hr; omega))

theorem neg_one_pow_inv (x : ℕ) : ((-1 : 𝕜) ^ x)⁻¹ = (-1) ^ x := by
  rw [← inv_pow, inv_neg_one]

/-- The cup coefficient `a_p` on `v_p ⊗ v_{m−p}`. -/
def cupCoef (m p : ℕ) : 𝕜 := hwCoef (s ^ 2) m m m p

/-- The cap coefficient `b_p = (−1)^m q^{m−2p} / a_p`. -/
def capCoef (m p : ℕ) : 𝕜 := (-1) ^ m * (s ^ 2) ^ ((m : ℤ) - 2 * p) / cupCoef s m p

/-- The `k`-th term of the clasp at output `v_j ⊗ v_0`, with `m = k + a + n`, `j = k + a`. -/
def claspTerm (k a n : ℕ) : 𝕜 :=
  hwCoef (s ^ 2) (k + a + n) (k + a + n) (k + a) k
      / hwCoef (s ^ 2) (k + a + n) (k + a + n) (k + a) (k + a)
    * capCoef s (k + a + n) k * cupCoef s (k + a + n) (k + a + n)
    * mono s hs (k + a + n) (k + a + n) (⟨k + a + n - k, by omega⟩, ⟨k + a, by omega⟩)
        (⟨k + a - k, by omega⟩, ⟨k + a + n, by omega⟩)

theorem claspTerm_closed (k a n : ℕ)
    (hint : ∀ i, 0 < i → i ≤ k + a + n → qint (s ^ 2) i ≠ 0) :
    claspTerm s hs k a n
      = (-1) ^ (k + a) * (s ^ 2 - (s ^ 2)⁻¹) ^ n * qfact (s ^ 2) (n + k) * qfact (s ^ 2) (a + n)
          * s ^ (2 * (a * (a + n + 1)))
        / (qfact (s ^ 2) n * qfact (s ^ 2) k * qfact (s ^ 2) a
          * s ^ (2 * (k * (k + n + 1)) + n * (n + 1))) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hf := qfact_ne_zero' s (k + a + n) hint
  have hfm := hf (k + a + n) le_rfl
  have hfn := hf n (by omega)
  have hfk := hf k (by omega)
  have hfa := hf a (by omega)
  have hfan := hf (a + n) (by omega)
  have hfnk := hf (n + k) (by omega)
  have hf0 : qfact (s ^ 2) 0 = 1 := by simp [qfact]
  -- the four highest-weight coefficients
  have h1 : hwCoef (s ^ 2) (k + a + n) (k + a + n) (k + a) k
      = (-1) ^ k * (s ^ (2 * (k * a)) / s ^ (2 * (k * (n + 1)))) * qfact (s ^ 2) (a + n)
        * qfact (s ^ 2) (n + k) / (qfact (s ^ 2) (k + a + n) * qfact (s ^ 2) n) := by
    have h := hwCoef_closed (s ^ 2) hq (k + a + n) (k + a) k (by omega) (by omega)
      (fun i hi => hint _ (by omega) (by omega))
    rw [show k + a + n - (k + a) = n by omega, show k + a + n - k = a + n by omega,
      show n + k = n + k from rfl, sq_zpow_split s hs _ (k * a) (k * (n + 1))] at h
    · rw [eq_div_iff (mul_ne_zero hfm hfn), ← h]; ring
    · push_cast; ring
  have h2 : hwCoef (s ^ 2) (k + a + n) (k + a + n) (k + a) (k + a)
      = (-1) ^ (k + a) / s ^ (2 * ((k + a) * (n + 1))) := by
    have h := hwCoef_closed (s ^ 2) hq (k + a + n) (k + a) (k + a) le_rfl (by omega)
      (fun i hi => hint _ (by omega) (by omega))
    rw [show k + a + n - (k + a) = n by omega, show n + (k + a) = k + a + n by omega,
      sq_zpow_split s hs _ 0 ((k + a) * (n + 1))] at h
    · rw [eq_div_iff (pow_ne_zero _ hs)]
      apply mul_right_cancel₀ (mul_ne_zero hfm hfn)
      rw [show hwCoef (s ^ 2) (k + a + n) (k + a + n) (k + a) (k + a) * s ^ (2 * ((k + a) * (n + 1)))
          * (qfact (s ^ 2) (k + a + n) * qfact (s ^ 2) n)
          = (hwCoef (s ^ 2) (k + a + n) (k + a + n) (k + a) (k + a) * qfact (s ^ 2) (k + a + n)
            * qfact (s ^ 2) n) * s ^ (2 * ((k + a) * (n + 1))) by ring, h]
      field_simp
      simp
    · push_cast; ring
  have h3 : hwCoef (s ^ 2) (k + a + n) (k + a + n) (k + a + n) k
      = (-1) ^ k * (s ^ (2 * (k * (a + n))) / s ^ (2 * k)) * qfact (s ^ 2) (a + n)
        * qfact (s ^ 2) k / qfact (s ^ 2) (k + a + n) := by
    have h := hwCoef_closed (s ^ 2) hq (k + a + n) (k + a + n) k (by omega) le_rfl
      (fun i hi => hint _ (by omega) (by omega))
    rw [Nat.sub_self, zero_add, hf0, mul_one, show k + a + n - k = a + n by omega,
      sq_zpow_split s hs _ (k * (a + n)) k] at h
    · rw [eq_div_iff hfm, h]
    · push_cast; ring
  have h4 : hwCoef (s ^ 2) (k + a + n) (k + a + n) (k + a + n) (k + a + n)
      = (-1) ^ (k + a + n) / s ^ (2 * (k + a + n)) := by
    have h := hwCoef_closed (s ^ 2) hq (k + a + n) (k + a + n) (k + a + n) le_rfl le_rfl
      (fun i hi => hint _ (by omega) (by omega))
    rw [Nat.sub_self, zero_add, hf0, mul_one, mul_one,
      sq_zpow_split s hs _ 0 (k + a + n)] at h
    · rw [eq_div_iff (pow_ne_zero _ hs)]
      apply mul_right_cancel₀ hfm
      rw [show hwCoef (s ^ 2) (k + a + n) (k + a + n) (k + a + n) (k + a + n) * s ^ (2 * (k + a + n))
          * qfact (s ^ 2) (k + a + n)
          = (hwCoef (s ^ 2) (k + a + n) (k + a + n) (k + a + n) (k + a + n) * qfact (s ^ 2) (k + a + n))
            * s ^ (2 * (k + a + n)) by ring, h]
      field_simp
      simp
    · push_cast; ring
  have hE : (irrepE (s ^ 2) (k + a + n) ^ (k + a + n - (k + a))) ⟨k + a, by omega⟩ ⟨k + a + n, by omega⟩
      = qfact (s ^ 2) n := by
    rw [irrepE_pow_entry _ _ _ _ _ (by simp)]
    have hd := qfact_mul_prod_down (s ^ 2) n n le_rfl
    rw [Nat.sub_self, hf0, one_mul] at hd
    rw [← hd, show k + a + n - (k + a) = n by omega]
  have hF : (irrepF (s ^ 2) (k + a + n) ^ (k + a + n - (k + a))) ⟨k + a + n - k, by omega⟩
      ⟨k + a - k, by omega⟩ = qfact (s ^ 2) (a + n) / qfact (s ^ 2) a := by
    rw [irrepF_pow_entry _ _ _ _ _ (by simp; omega), eq_div_iff hfa]
    have hu := qfact_mul_prod_up (s ^ 2) a n
    rw [← hu, show k + a + n - (k + a) = n by omega, mul_comm]
    exact congrArg _ (Finset.prod_congr rfl (fun l _ => by congr 1; simp))
  unfold claspTerm capCoef cupCoef
  rw [h1, h2, h3, h4, mono_clasp_entry s hs (k + a + n) (k + a) k (by omega) (by omega), hE, hF,
    sq_zpow_split s hs _ (k + a + n) (2 * k),
    s_zpow_split s hs (wt (k + a + n) (k + a + n) * wt (k + a + n) (k + a - k))
      ((k + a + n) * a) ((k + a + n) * (k + n)),
    s_zpow_split s hs (wt (k + a + n) (k + a) * wt (k + a + n) (k + a + n - k))
      (a * a + 2 * n * k) (n * n + k * k),
    show k + a + n - (k + a) = n by omega]
  · unfold rcoef
    have hnn : s ^ (n * (n - 1)) = s ^ (n * n) / s ^ n := by
      rcases n with _ | n
      · simp
      · rw [eq_div_iff (pow_ne_zero _ hs), ← pow_add]; congr 1
    rw [hnn, show ((-1 : 𝕜)) ^ (k + a + n) = (-1) ^ k * (-1) ^ a * (-1) ^ n by rw [pow_add, pow_add],
      show ((-1 : 𝕜)) ^ (k + a) = (-1) ^ k * (-1) ^ a from pow_add _ _ _]
    generalize s ^ 2 - (s ^ 2)⁻¹ = X
    generalize hA : qfact (s ^ 2) (n + k) = A at hfnk
    generalize hB : qfact (s ^ 2) (a + n) = B at hfan
    generalize hC : qfact (s ^ 2) (k + a + n) = C at hfm
    generalize hD : qfact (s ^ 2) n = D at hfn
    generalize hE' : qfact (s ^ 2) k = E at hfk
    generalize hF' : qfact (s ^ 2) a = F at hfa
    rcases Nat.even_or_odd k with hk | hk <;> rcases Nat.even_or_odd a with ha | ha <;>
      rcases Nat.even_or_odd n with hn | hn <;>
      rw [hk.neg_one_pow, ha.neg_one_pow, hn.neg_one_pow] <;> field_simp <;> ring
  all_goals
    try unfold wt
    try simp only [show k + a - k = a by omega, show k + a + n - k = a + n by omega]
    push_cast; ring

include hs in
/-- `1 − t^x = −q^x (q − q⁻¹) [x]` with `q = s²`, `t = q²`. -/
theorem one_sub_tpow (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (x : ℕ) :
    1 - ((s ^ 2) ^ 2) ^ x = -((s ^ 2) ^ x * (s ^ 2 - (s ^ 2)⁻¹) * qint (s ^ 2) x) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hX : (s ^ 2) ^ x * (s ^ 2)⁻¹ ^ x = 1 := by rw [← mul_pow, mul_inv_cancel₀ hq, one_pow]
  unfold qint
  rw [mul_assoc, mul_div_assoc', mul_div_cancel_left₀ _ hq2, mul_sub, hX]
  ring

include hs in
/-- `[c]! · Π_{i<n} (1 − t^{c+i+1}) = (−1)ⁿ (q − q⁻¹)ⁿ s^{2nc + n(n+1)} [c+n]!`. -/
theorem qfact_mul_prod_one_sub (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (c n : ℕ) :
    qfact (s ^ 2) c * ∏ i ∈ Finset.range n, (1 - ((s ^ 2) ^ 2) ^ (c + i + 1))
      = (-1) ^ n * (s ^ 2 - (s ^ 2)⁻¹) ^ n * s ^ (2 * (n * c) + n * (n + 1))
        * qfact (s ^ 2) (c + n) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.prod_range_succ, ← mul_assoc, ih, one_sub_tpow s hs hq2,
      show c + (n + 1) = (c + n) + 1 by omega, qfact_succ, show c + n + 1 = c + n + 1 from rfl]
    ring

/-- van der Veen's `k`-th summand of `C(n, t)` (2008, Lemma 1), with `N = m + 1`,
`m = k + a + n`, `t = q² = s⁴`, and `t^{N(N−1)/2}` written `s^{2N(N−1)}`. -/
def vdvTerm (k a n : ℕ) : 𝕜 :=
  (-1) ^ (k + a + n) * s ^ (2 * ((k + a + n + 1) * (k + a + n)))
    / s ^ (4 * ((k + a + n + 1) * (n + k)))
    * ∏ i ∈ Finset.Icc 1 n, (1 - ((s ^ 2) ^ 2) ^ (k + a + n + 1 - i - k))
        * (1 - ((s ^ 2) ^ 2) ^ (i + k)) / (1 - ((s ^ 2) ^ 2) ^ i)

include hs in
include hs in
theorem vdvTerm_closed (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (k a n : ℕ)
    (hint : ∀ i, 0 < i → i ≤ k + a + n → qint (s ^ 2) i ≠ 0) :
    vdvTerm s k a n
      = (-1) ^ (k + a) * (s ^ 2 - (s ^ 2)⁻¹) ^ n * qfact (s ^ 2) (n + k) * qfact (s ^ 2) (a + n)
          * s ^ (2 * (a * (a + n + 1)))
        / (qfact (s ^ 2) n * qfact (s ^ 2) k * qfact (s ^ 2) a
          * s ^ (2 * (k * (k + n + 1)) + n * (n + 1))) := by
  have hf := qfact_ne_zero' s (k + a + n) hint
  have hfn := hf n (by omega)
  have hfk := hf k (by omega)
  have hfa := hf a (by omega)
  have hf0 : qfact (s ^ 2) 0 = 1 := by simp [qfact]
  unfold vdvTerm
  rw [← Finset.Ico_add_one_right_eq_Icc, Finset.prod_Ico_eq_prod_range, Nat.add_sub_cancel,
    Finset.prod_div_distrib, Finset.prod_mul_distrib]
  have hA : ∏ i ∈ Finset.range n, (1 - ((s ^ 2) ^ 2) ^ (k + a + n + 1 - (1 + i) - k))
      = ∏ i ∈ Finset.range n, (1 - ((s ^ 2) ^ 2) ^ (a + i + 1)) := by
    rw [← Finset.prod_range_reflect]
    exact Finset.prod_congr rfl (fun i hi => by
      have := Finset.mem_range.mp hi; congr 2; omega)
  have hB : ∏ i ∈ Finset.range n, (1 - ((s ^ 2) ^ 2) ^ (1 + i + k))
      = ∏ i ∈ Finset.range n, (1 - ((s ^ 2) ^ 2) ^ (k + i + 1)) := by
    exact Finset.prod_congr rfl (fun i _ => by congr 2; omega)
  have hC : ∏ i ∈ Finset.range n, (1 - ((s ^ 2) ^ 2) ^ (1 + i))
      = ∏ i ∈ Finset.range n, (1 - ((s ^ 2) ^ 2) ^ (0 + i + 1)) := by
    exact Finset.prod_congr rfl (fun i _ => by congr 2; omega)
  have pA := qfact_mul_prod_one_sub s hs hq2 a n
  have pB := qfact_mul_prod_one_sub s hs hq2 k n
  have pC := qfact_mul_prod_one_sub s hs hq2 0 n
  rw [hf0, one_mul, zero_add, mul_zero] at pC
  rw [mul_comm (qfact (s ^ 2) a)] at pA
  rw [mul_comm (qfact (s ^ 2) k)] at pB
  rw [hA, hB, hC, eq_div_of_mul_eq hfa pA, eq_div_of_mul_eq hfk pB, pC,
    show ((-1 : 𝕜)) ^ (k + a + n) = (-1) ^ k * (-1) ^ a * (-1) ^ n by rw [pow_add, pow_add],
    show ((-1 : 𝕜)) ^ (k + a) = (-1) ^ k * (-1) ^ a from pow_add _ _ _,
    show k + n = n + k from add_comm _ _]
  generalize s ^ 2 - (s ^ 2)⁻¹ = X at hq2
  generalize qfact (s ^ 2) (n + k) = A
  generalize qfact (s ^ 2) (a + n) = B
  generalize hD : qfact (s ^ 2) n = D at hfn
  generalize qfact (s ^ 2) k = E at hfk
  generalize qfact (s ^ 2) a = F at hfa
  rcases Nat.even_or_odd k with hk | hk <;> rcases Nat.even_or_odd a with ha | ha <;>
    rcases Nat.even_or_odd n with hn | hn <;>
    rw [hk.neg_one_pow, ha.neg_one_pow, hn.neg_one_pow] <;> field_simp <;> ring

/-- **The clasp term is van der Veen's term.** -/
theorem claspTerm_eq_vdvTerm (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (k a n : ℕ)
    (hint : ∀ i, 0 < i → i ≤ k + a + n → qint (s ^ 2) i ≠ 0) :
    claspTerm s hs k a n = vdvTerm s k a n := by
  rw [claspTerm_closed s hs k a n hint, vdvTerm_closed s hs hq2 k a n hint]

end ClaspTerm

end QOU.Mass.QuantumSl2
