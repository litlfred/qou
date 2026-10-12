import QOU.Archimedean.RossoJonesTorusLink
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Projection

/-!
# Schur–Weyl trace split on `V^{⊗r}` (WIP)
-/

namespace QOU.Archimedean.SchurWeylTrace

open QOU.Archimedean.RossoJonesGeneral

/-! ## 1. Trace across a surjection -/

theorem trace_eq_trace_ker_add {K V V' : Type*} [Field K] [AddCommGroup V] [Module K V]
    [FiniteDimensional K V] [AddCommGroup V'] [Module K V'] [FiniteDimensional K V']
    (X : V →ₗ[K] V) (X' : V' →ₗ[K] V') (φ : V →ₗ[K] V') (hφ : Function.Surjective φ)
    (hc : φ ∘ₗ X = X' ∘ₗ φ) (hK : ∀ v ∈ LinearMap.ker φ, X v ∈ LinearMap.ker φ) :
    LinearMap.trace K V X
      = LinearMap.trace K (LinearMap.ker φ) (X.restrict hK) + LinearMap.trace K V' X' := by
  classical
  obtain ⟨C, hC⟩ := Submodule.exists_isCompl (LinearMap.ker φ)
  set pK := (LinearMap.ker φ).linearProjOfIsCompl C hC
  set pC := C.linearProjOfIsCompl (LinearMap.ker φ) hC.symm
  have hsum : ∀ v : V, ((pK v : V) + (pC v : V)) = v :=
    Submodule.IsCompl.projection_add_projection_eq_self hC
  have hid : (LinearMap.id : V →ₗ[K] V)
      = (LinearMap.ker φ).subtype ∘ₗ pK + C.subtype ∘ₗ pC := by
    ext v; simp [hsum v]
  have h1 : LinearMap.trace K V X
      = LinearMap.trace K _ (pK ∘ₗ X ∘ₗ (LinearMap.ker φ).subtype)
        + LinearMap.trace K _ (pC ∘ₗ X ∘ₗ C.subtype) := by
    conv_lhs => rw [← LinearMap.comp_id X, hid]
    rw [LinearMap.comp_add, map_add]
    congr 1
    · rw [← LinearMap.comp_assoc]
      exact LinearMap.trace_comp_comm' pK (X ∘ₗ (LinearMap.ker φ).subtype)
    · rw [← LinearMap.comp_assoc]
      exact LinearMap.trace_comp_comm' pC (X ∘ₗ C.subtype)
  -- the kernel block is the restriction
  have h2 : pK ∘ₗ X ∘ₗ (LinearMap.ker φ).subtype = X.restrict hK := by
    ext v
    simp only [LinearMap.comp_apply, Submodule.coe_subtype, LinearMap.restrict_apply]
    have := Submodule.linearProjOfIsCompl_apply_left hC ⟨X v, hK v v.2⟩
    rw [this]
  -- the complement block is conjugate to X'
  have hφker : ∀ v : V, φ (pC v) = φ v := by
    intro v
    have hk : φ (pK v) = 0 := (pK v).2
    conv_rhs => rw [← hsum v]
    rw [map_add, hk, zero_add]
  set ψ : C →ₗ[K] V' := φ ∘ₗ C.subtype
  have hψi : Function.Injective ψ := by
    rw [← LinearMap.ker_eq_bot, eq_bot_iff]
    intro c hc0
    have h0 : (c : V) ∈ LinearMap.ker φ := hc0
    have : (c : V) ∈ LinearMap.ker φ ⊓ C := ⟨h0, c.2⟩
    rw [hC.inf_eq_bot, Submodule.mem_bot] at this
    rw [Submodule.mem_bot]; exact Subtype.ext this
  have hψs : Function.Surjective ψ := by
    intro y
    obtain ⟨v, rfl⟩ := hφ y
    exact ⟨pC v, hφker v⟩
  set e := LinearEquiv.ofBijective ψ ⟨hψi, hψs⟩
  have h3 : e.conj (pC ∘ₗ X ∘ₗ C.subtype) = X' := by
    apply LinearMap.ext; intro y
    obtain ⟨c, rfl⟩ := e.surjective y
    rw [LinearEquiv.conj_apply]
    simp only [LinearMap.comp_apply, LinearEquiv.coe_coe, LinearEquiv.symm_apply_apply]
    show φ (pC (X c)) = X' (φ c)
    rw [hφker, ← LinearMap.comp_apply φ X, hc, LinearMap.comp_apply]
  rw [h1, h2, ← h3, LinearMap.trace_conj']

/-! ## 2. Quantum integers -/

variable {R : Type*} [Field R]

/-- The quantum integer `[k] = q^{k−1} + q^{k−3} + ⋯ + q^{1−k}`, by `[k+1] = q^k + q⁻¹[k]`. -/
noncomputable def qn (q : R) : ℕ → R
  | 0 => 0
  | k + 1 => q ^ k + q⁻¹ * qn q k

@[simp] theorem qn_zero (q : R) : qn q 0 = 0 := rfl

theorem qn_succ (q : R) (k : ℕ) : qn q (k + 1) = q ^ k + q⁻¹ * qn q k := rfl

theorem qn_one (q : R) : qn q 1 = 1 := by simp [qn_succ]

/-- The other recursion, `[k+1] = q[k] + q^{−k}`. -/
theorem qn_succ' {q : R} (hq : q ≠ 0) (k : ℕ) : qn q (k + 1) = q * qn q k + q⁻¹ ^ k := by
  induction k with
  | zero => simp [qn_succ]
  | succ k ih =>
    conv_lhs => rw [qn_succ, ih]
    conv_rhs => rw [qn_succ]
    simp only [inv_pow, pow_succ]
    field_simp
    ring

/-- `[k]` is invariant under `q ↦ q⁻¹`. -/
theorem qn_inv {q : R} (hq : q ≠ 0) (k : ℕ) : qn q⁻¹ k = qn q k := by
  induction k with
  | zero => rfl
  | succ k ih => rw [qn_succ, ih, inv_inv, qn_succ' hq, inv_pow]; ring

/-- `[a+1][b+1] = [a][b] + [a+b+1]`. -/
theorem qn_mul {q : R} (hq : q ≠ 0) (a b : ℕ) :
    qn q (a + 1) * qn q (b + 1) = qn q a * qn q b + qn q (a + b + 1) := by
  induction a with
  | zero => simp [qn_succ]
  | succ a ih =>
    have hb : q ^ (a + 1) * qn q (b + 1) = q ^ a * qn q b + q ^ (a + b + 1) := by
      rw [qn_succ, mul_add, ← pow_add, show a + 1 + b = a + b + 1 by ring, pow_succ]
      field_simp
      ring
    rw [qn_succ q (a + 1), add_mul, hb, mul_assoc, ih, qn_succ q a,
      show a + 1 + b + 1 = (a + b + 1) + 1 by ring, qn_succ q (a + b + 1)]
    ring

/-- `Σ_{i<j} [D + 2i] = [j][D + j − 1]` for `D ≥ 1`. -/
theorem sum_qn (q : R) (hq : q ≠ 0) (D : ℕ) (hD : 1 ≤ D) :
    ∀ j, ∑ i ∈ Finset.range j, qn q (D + 2 * i) = qn q j * qn q (D + j - 1) := by
  intro j
  induction j with
  | zero => simp
  | succ j ih =>
    rw [Finset.sum_range_succ, ih]
    obtain ⟨E, rfl⟩ := Nat.exists_eq_add_of_le hD
    rw [show 1 + E + (j + 1) - 1 = (E + j) + 1 by omega, qn_mul hq,
      show 1 + E + j - 1 = E + j by omega, show j + (E + j) + 1 = 1 + E + 2 * j by ring]

/-- The signed quantum integer `[o − z]`, written with two naturals. -/
noncomputable def sq (q : R) (o z : ℕ) : R := if z ≤ o then qn q (o - z) else -qn q (z - o)

theorem sq_succ_left {q : R} (hq : q ≠ 0) (o z : ℕ) :
    sq q (o + 1) z = q * sq q o z + q ^ z * q⁻¹ ^ o := by
  unfold sq
  rcases Nat.lt_trichotomy z (o + 1) with h | h | h
  · rw [if_pos (by omega), if_pos (by omega), show o + 1 - z = (o - z) + 1 by omega, qn_succ' hq]
    obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le (show z ≤ o by omega)
    rw [show z + t - z = t by omega, pow_add, inv_pow, inv_pow]
    try simp only [inv_pow]
    field_simp
  · subst h
    rw [if_pos le_rfl, if_neg (by omega), Nat.sub_self, show o + 1 - o = 1 by omega, qn_one,
      qn_zero, pow_succ]
    try simp only [inv_pow]
    field_simp
    ring
  · rw [if_neg (by omega), if_neg (by omega)]
    obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le (show o + 1 ≤ z by omega)
    rw [show o + 1 + t - (o + 1) = t by omega, show o + 1 + t - o = t + 1 by omega, qn_succ,
      pow_add, pow_add]
    try simp only [inv_pow]
    field_simp
    ring

theorem sq_succ_right {q : R} (hq : q ≠ 0) (o z : ℕ) :
    sq q o (z + 1) = q⁻¹ * sq q o z - q ^ z * q⁻¹ ^ o := by
  unfold sq
  rcases Nat.lt_trichotomy (z + 1) o with h | h | h
  · rw [if_pos (by omega), if_pos (by omega)]
    obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le (show z + 1 ≤ o by omega)
    rw [show z + 1 + t - (z + 1) = t by omega, show z + 1 + t - z = t + 1 by omega, qn_succ' hq,
      pow_add, pow_add]
    try simp only [inv_pow]
    field_simp
    ring
  · subst h
    rw [if_pos le_rfl, if_pos (by omega), Nat.sub_self, show z + 1 - z = 1 by omega, qn_one,
      qn_zero, pow_succ]
    try simp only [inv_pow]
    field_simp
    ring
  · rcases Nat.eq_or_lt_of_le (show o ≤ z by omega) with h' | h'
    · subst h'
      rw [if_neg (by omega), if_pos le_rfl, Nat.sub_self, show o + 1 - o = 1 by omega, qn_one,
        qn_zero]
      simp only [inv_pow]
      field_simp
      ring
    · rw [if_neg (by omega), if_neg (by omega), show z + 1 - o = (z - o) + 1 by omega, qn_succ]
      obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le (show o ≤ z by omega)
      rw [show o + t - o = t by omega, pow_add]
      simp only [inv_pow]
      field_simp
      ring

/-! ## 3. The lowering operator `F` and the commutator `[E, F]` -/

variable {q : R}

open QOU.IwahoriHecke.TensorMarkovModel

/-- `K⁻¹` on one site: `q` on a zero, `q⁻¹` on a one. -/
noncomputable def kin (q : R) (x : Fin 2) : R := if x = 0 then q else q⁻¹

/-- The `K⁻¹`-string to the left of site `k`. -/
noncomputable def psi (q : R) {N : ℕ} (k : Fin N) (b : Fin N → Fin 2) : R :=
  ∏ l, if l < k then kin q (b l) else 1

/-- The `K`-string to the right of site `k` (the `phi` of `RossoJonesMiddle`, any length). -/
noncomputable def phiN (q : R) {N : ℕ} (k : Fin N) (b : Fin N → Fin 2) : R :=
  ∏ l, if k < l then ki q (b l) else 1

theorem phi_eq_phiN (q : R) {n : ℕ} (k : Fin (n + 1)) (b : Fin (n + 1) → Fin 2) :
    phi q k b = phiN q k b := rfl

/-- **The lowering operator** `F = Σ_k K⁻¹ ⊗ ⋯ ⊗ K⁻¹ ⊗ f_k` of `U_q(sl₂)` on `V^{⊗(n+1)}`,
`f : 1 ↦ 0`. -/
noncomputable def Fm (q : R) (n : ℕ) : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R :=
  Matrix.of fun a b => ∑ k, if b k = 1 then
    (if a = Function.update b k 0 then psi q k b else 0) else 0

/-- The diagonal of `[E, F]`. -/
noncomputable def Dg (q : R) {N : ℕ} (b : Fin N → Fin 2) : R :=
  ∑ k, (if b k = 1 then 1 else -1) * (psi q k b * phiN q k b)

theorem mul_Fm_apply (q : R) {n : ℕ} (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R)
    (a b : Fin (n + 1) → Fin 2) :
    (X * Fm q n) a b = ∑ k, if b k = 1 then X a (Function.update b k 0) * psi q k b else 0 := by
  classical
  rw [Matrix.mul_apply]
  simp only [Fm, Matrix.of_apply, Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun k _ => ?_
  by_cases hk : b k = 1
  · simp only [hk, if_true, mul_ite, mul_zero]
    rw [Finset.sum_ite_eq' Finset.univ, if_pos (Finset.mem_univ _)]
  · simp [hk]

/-- A conditional product changes at one site only. -/
theorem prod_cond_update {N : ℕ} (w : Fin 2 → R) (c : Fin N → Prop) [DecidablePred c]
    (b : Fin N → Fin 2) (j : Fin N) (y : Fin 2) :
    (∏ l, if c l then w (Function.update b j y l) else 1) * (if c j then w (b j) else 1)
      = (∏ l, if c l then w (b l) else 1) * (if c j then w y else 1) := by
  classical
  rw [← Finset.mul_prod_erase Finset.univ (fun l => if c l then w (Function.update b j y l) else 1)
      (Finset.mem_univ j),
    ← Finset.mul_prod_erase Finset.univ (fun l => if c l then w (b l) else 1) (Finset.mem_univ j)]
  have : ∏ l ∈ Finset.univ.erase j, (if c l then w (Function.update b j y l) else 1)
      = ∏ l ∈ Finset.univ.erase j, (if c l then w (b l) else 1) :=
    Finset.prod_congr rfl fun l hl => by
      rw [Function.update_of_ne (Finset.ne_of_mem_erase hl)]
  rw [this, Function.update_self]
  ring

theorem psi_update_self (q : R) {N : ℕ} (k : Fin N) (b : Fin N → Fin 2) (y : Fin 2) :
    psi q k (Function.update b k y) = psi q k b := by
  have h := prod_cond_update (kin q) (fun l => l < k) b k y
  simpa [psi] using h

theorem phiN_update_self (q : R) {N : ℕ} (k : Fin N) (b : Fin N → Fin 2) (y : Fin 2) :
    phiN q k (Function.update b k y) = phiN q k b := by
  have h := prod_cond_update (ki q) (fun l => k < l) b k y
  simpa [phiN] using h

/-- The off-diagonal weights of `EF` and `FE` agree. -/
theorem weight_swap {q : R} (hq : q ≠ 0) {N : ℕ} (b : Fin N → Fin 2) (k l : Fin N) (hkl : k ≠ l)
    (hk : b k = 1) (hl : b l = 0) :
    phiN q l (Function.update b k 0) * psi q k b
      = psi q k (Function.update b l 1) * phiN q l b := by
  rcases lt_or_gt_of_ne hkl with h | h
  · -- `k < l`: neither string sees the other site
    have h1 := prod_cond_update (ki q) (fun i => l < i) b k 0
    have h2 := prod_cond_update (kin q) (fun i => i < k) b l 1
    simp only [show ¬ l < k from not_lt.mpr h.le, if_false, mul_one] at h1 h2
    rw [show phiN q l (Function.update b k 0) = phiN q l b from h1,
      show psi q k (Function.update b l 1) = psi q k b from h2]
    ring
  · -- `l < k`
    have h1 := prod_cond_update (ki q) (fun i => l < i) b k 0
    have h2 := prod_cond_update (kin q) (fun i => i < k) b l 1
    simp only [h, if_true, hk, hl] at h1 h2
    change phiN q l (Function.update b k 0) * ki q 1 = phiN q l b * ki q 0 at h1
    change psi q k (Function.update b l 1) * kin q 0 = psi q k b * kin q 1 at h2
    simp only [ki, kin, if_true, show (1 : Fin 2) ≠ 0 by decide, if_false] at h1 h2
    have e1 : phiN q l (Function.update b k 0) = phiN q l b * q⁻¹ * q⁻¹ := by
      field_simp at h1 ⊢; linear_combination h1
    have e2 : psi q k (Function.update b l 1) = psi q k b * q⁻¹ * q⁻¹ := by
      field_simp at h2 ⊢; linear_combination h2
    rw [e1, e2]; ring

theorem Em_apply' (q : R) {n : ℕ} (a w : Fin (n + 1) → Fin 2) :
    Em q n a w = ∑ l, if w l = 0 then (if a = Function.update w l 1 then phiN q l w else 0)
      else 0 := rfl

theorem Fm_apply (q : R) {n : ℕ} (a w : Fin (n + 1) → Fin 2) :
    Fm q n a w = ∑ k, if w k = 1 then (if a = Function.update w k 0 then psi q k w else 0)
      else 0 := rfl

/-- **`[E, F]` is diagonal**, with entries `Dg`. -/
theorem Em_Fm_comm (hq : q ≠ 0) (n : ℕ) :
    Em q n * Fm q n - Fm q n * Em q n = Matrix.diagonal (Dg q) := by
  classical
  ext a b
  rw [Matrix.sub_apply, mul_Fm_apply, mul_Em_apply, Matrix.diagonal_apply]
  simp only [Em_apply', Fm_apply, phi_eq_phiN]
  -- both sides as double sums over (k, l): k the F-site, l the E-site
  set A : Fin (n + 1) → Fin (n + 1) → R := fun k l =>
    if b k = 1 then (if Function.update b k 0 l = 0 then
      (if a = Function.update (Function.update b k 0) l 1 then
        phiN q l (Function.update b k 0) * psi q k b else 0) else 0) else 0 with hA
  set B : Fin (n + 1) → Fin (n + 1) → R := fun k l =>
    if b l = 0 then (if Function.update b l 1 k = 1 then
      (if a = Function.update (Function.update b l 1) k 0 then
        psi q k (Function.update b l 1) * phiN q l b else 0) else 0) else 0 with hB
  have hEF : (∑ k, if b k = 1 then
      (∑ l, if Function.update b k 0 l = 0 then
        (if a = Function.update (Function.update b k 0) l 1 then
          phiN q l (Function.update b k 0) else 0) else 0) * psi q k b else 0)
      = ∑ k, ∑ l, A k l := by
    refine Finset.sum_congr rfl fun k _ => ?_
    by_cases hk : b k = 1
    · simp only [hA, hk, if_true, Finset.sum_mul]
      refine Finset.sum_congr rfl fun l _ => ?_
      split_ifs <;> ring
    · simp [hA, hk]
  have hFE : (∑ l, if b l = 0 then
      (∑ k, if Function.update b l 1 k = 1 then
        (if a = Function.update (Function.update b l 1) k 0 then
          psi q k (Function.update b l 1) else 0) else 0) * phiN q l b else 0)
      = ∑ k, ∑ l, B k l := by
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun l _ => ?_
    by_cases hl : b l = 0
    · simp only [hB, hl, if_true, Finset.sum_mul]
      refine Finset.sum_congr rfl fun k _ => ?_
      split_ifs <;> ring
    · simp [hB, hl]
  rw [hEF, hFE]
  simp only [← Finset.sum_sub_distrib]
  have hoff : ∀ k l, l ≠ k → A k l = B k l := by
    intro k l hlk
    have hkl : k ≠ l := Ne.symm hlk
    simp only [hA, hB, Function.update_of_ne hlk, Function.update_of_ne hkl,
      Function.update_comm hkl]
    by_cases hk : b k = 1
    · by_cases hl : b l = 0
      · simp only [hk, hl, if_true]
        split_ifs
        · exact weight_swap hq b k l hkl hk hl
        · rfl
      · simp [hk, hl]
    · simp [hk]
  have hdiag : ∀ k, ∑ l, (A k l - B k l) = A k k - B k k := by
    intro k
    rw [Finset.sum_eq_single k]
    · intro l _ hlk; rw [hoff k l hlk, sub_self]
    · intro h; exact absurd (Finset.mem_univ k) h
  simp only [hdiag]
  have hkk : ∀ k, A k k - B k k
      = if a = b then (if b k = 1 then 1 else -1) * (psi q k b * phiN q k b) else 0 := by
    intro k
    have h10 : ((1 : Fin 2) = 0) ↔ False := by decide
    have h01 : ((0 : Fin 2) = 1) ↔ False := by decide
    simp only [hA, hB, Function.update_self, Function.update_idem, phiN_update_self,
      psi_update_self]
    by_cases hk : b k = 1
    · have hk0 : b k ≠ 0 := by rw [hk]; decide
      simp only [hk, h10, if_true, if_false, sub_zero]
      rw [Function.update_eq_self_iff.mpr hk.symm]
      split_ifs <;> ring
    · have hk0 : b k = 0 := by
        rcases Fin.exists_fin_two.mp ⟨b k, rfl⟩ with h | h
        · exact h
        · exact absurd h hk
      simp only [hk0, h01, if_true, if_false, zero_sub]
      rw [Function.update_eq_self_iff.mpr hk0.symm]
      split_ifs <;> ring
  simp only [hkk]
  by_cases hab : a = b
  · subst hab; simp [Dg]
  · simp [hab]

/-! ## 4. The diagonal of `[E, F]` is the signed quantum integer `[2·ones − N]` -/

theorem psi_castSucc (q : R) {N : ℕ} (k : Fin N) (c : Fin N → Fin 2) (x : Fin 2) :
    psi q k.castSucc (Fin.snoc c x : Fin (N + 1) → Fin 2) = psi q k c := by
  rw [psi, Fin.prod_univ_castSucc]
  simp [Fin.snoc_castSucc, Fin.snoc_last, psi, not_lt.mpr (Fin.castSucc_lt_last k).le]

theorem psi_last (q : R) {N : ℕ} (c : Fin N → Fin 2) (x : Fin 2) :
    psi q (Fin.last N) (Fin.snoc c x : Fin (N + 1) → Fin 2) = ∏ l, kin q (c l) := by
  rw [psi, Fin.prod_univ_castSucc]
  simp [Fin.snoc_castSucc, Fin.castSucc_lt_last]

theorem phiN_castSucc (q : R) {N : ℕ} (k : Fin N) (c : Fin N → Fin 2) (x : Fin 2) :
    phiN q k.castSucc (Fin.snoc c x : Fin (N + 1) → Fin 2) = phiN q k c * ki q x := by
  rw [phiN, Fin.prod_univ_castSucc]
  simp [Fin.snoc_castSucc, Fin.snoc_last, phiN, Fin.castSucc_lt_last]

theorem phiN_last (q : R) {N : ℕ} (b : Fin (N + 1) → Fin 2) : phiN q (Fin.last N) b = 1 := by
  rw [phiN]
  exact Finset.prod_eq_one fun l _ => if_neg (not_lt.mpr (Fin.le_last l))

theorem Dg_snoc (q : R) {N : ℕ} (c : Fin N → Fin 2) (x : Fin 2) :
    Dg q (Fin.snoc c x : Fin (N + 1) → Fin 2)
      = Dg q c * ki q x + (if x = 1 then 1 else -1) * ∏ l, kin q (c l) := by
  rw [Dg, Fin.sum_univ_castSucc]
  simp only [Fin.snoc_castSucc, Fin.snoc_last, psi_castSucc, phiN_castSucc, psi_last, phiN_last,
    Dg, Finset.sum_mul]
  congr 1
  · refine Finset.sum_congr rfl fun k _ => ?_; ring
  · ring

theorem prod_kin (q : R) {N : ℕ} (c : Fin N → Fin 2) :
    (∏ l, kin q (c l)) = q ^ (N - ones c) * q⁻¹ ^ ones c := by
  classical
  have h : ∀ x : Fin 2, kin q x = if x = 1 then q⁻¹ else q := by
    intro x; rcases Fin.exists_fin_two.mp ⟨x, rfl⟩ with h | h <;> simp [h, kin]
  simp only [h]
  rw [Finset.prod_ite, Finset.prod_const, Finset.prod_const, mul_comm]
  have := ones_add_zeros c
  congr 2
  · omega

/-- **The diagonal of `[E, F]`**: on a state with `o` ones and `z` zeros it is `[o − z]`. -/
theorem Dg_eq (hq : q ≠ 0) : ∀ (N : ℕ) (b : Fin N → Fin 2), Dg q b = sq q (ones b) (N - ones b)
  | 0, b => by simp [Dg, sq, ones]
  | N + 1, b => by
    have hb := Fin.snoc_init_self b
    rw [← hb, Dg_snoc, Dg_eq hq N, prod_kin, ones_snoc]
    have hle := ones_le (Fin.init b)
    rcases Fin.exists_fin_two.mp ⟨b (Fin.last N), rfl⟩ with h | h
    · rw [h]
      simp only [show ((0 : Fin 2) = 1) ↔ False by decide, if_false, add_zero]
      rw [show N + 1 - ones (Fin.init b) = (N - ones (Fin.init b)) + 1 by omega, sq_succ_right hq]
      simp [ki]; ring
    · rw [h]
      simp only [if_true]
      rw [show N + 1 - (ones (Fin.init b) + 1) = N - ones (Fin.init b) by omega, sq_succ_left hq]
      simp [ki]; ring

/-! ## 5. `E` is injective on the lower half -/

open Matrix

/-- `F` lowers the weight by one. -/
theorem Fm_weight (q : R) {n : ℕ} (a b : Fin (n + 1) → Fin 2) (h : Fm q n a b ≠ 0) :
    ones a + 1 = ones b := by
  classical
  rw [Fm_apply] at h
  obtain ⟨k, -, hk⟩ := Finset.exists_ne_zero_of_sum_ne_zero h
  by_cases hb : b k = 1
  · rw [if_pos hb] at hk
    by_cases ha : a = Function.update b k 0
    · subst ha
      have h0 : Function.update b k 0 k = 0 := Function.update_self _ _ _
      have := ones_update (Function.update b k 0) k h0
      rwa [Function.update_idem, Function.update_eq_self_iff.mpr hb.symm, eq_comm] at this
    · rw [if_neg ha] at hk; exact absurd rfl hk
  · rw [if_neg hb] at hk; exact absurd rfl hk

/-- A vector supported on the weight-`m` states. -/
def Supp {n : ℕ} (m : ℕ) (v : (Fin (n + 1) → Fin 2) → R) : Prop := ∀ b, ones b ≠ m → v b = 0

theorem supp_Em {n m : ℕ} (q : R) {v : (Fin (n + 1) → Fin 2) → R} (hv : Supp m v) :
    Supp (m + 1) (Em q n *ᵥ v) := by
  intro a ha
  simp only [Matrix.mulVec, dotProduct]
  refine Finset.sum_eq_zero fun b _ => ?_
  by_cases hb : ones b = m
  · have : Em q n a b = 0 := by
      by_contra h; exact ha (by rw [Em_weight q a b h, hb])
    rw [this, zero_mul]
  · rw [hv b hb, mul_zero]

theorem supp_Fm {n m : ℕ} (q : R) {v : (Fin (n + 1) → Fin 2) → R} (hv : Supp (m + 1) v) :
    Supp m (Fm q n *ᵥ v) := by
  intro a ha
  simp only [Matrix.mulVec, dotProduct]
  refine Finset.sum_eq_zero fun b _ => ?_
  by_cases hb : ones b = m + 1
  · have : Fm q n a b = 0 := by
      by_contra h; exact ha (by have := Fm_weight q a b h; omega)
    rw [this, zero_mul]
  · rw [hv b hb, mul_zero]

theorem Fm_supp_zero {n : ℕ} (q : R) {v : (Fin (n + 1) → Fin 2) → R} (hv : Supp 0 v) :
    Fm q n *ᵥ v = 0 := by
  funext a
  simp only [Matrix.mulVec, dotProduct, Pi.zero_apply]
  refine Finset.sum_eq_zero fun b _ => ?_
  by_cases h : Fm q n a b = 0
  · rw [h, zero_mul]
  · have := Fm_weight q a b h
    rw [hv b (by omega), mul_zero]

theorem Dg_mulVec (hq : q ≠ 0) {n m : ℕ} {v : (Fin (n + 1) → Fin 2) → R} (hv : Supp m v) :
    Matrix.diagonal (Dg q) *ᵥ v = sq q m (n + 1 - m) • v := by
  funext b
  rw [Matrix.mulVec_diagonal, Pi.smul_apply, smul_eq_mul]
  by_cases hb : ones b = m
  · rw [Dg_eq hq, hb]
  · rw [hv b hb, mul_zero, mul_zero]

theorem Em_Fm_mulVec (hq : q ≠ 0) {n : ℕ} (v : (Fin (n + 1) → Fin 2) → R) :
    Em q n *ᵥ (Fm q n *ᵥ v) = Fm q n *ᵥ (Em q n *ᵥ v) + Matrix.diagonal (Dg q) *ᵥ v := by
  rw [Matrix.mulVec_mulVec, Matrix.mulVec_mulVec, ← Matrix.add_mulVec, ← Em_Fm_comm hq n]
  abel_nf

/-- The hypothesis replacing "`q` is not a root of unity": `[k] ≠ 0` for `1 ≤ k ≤ r`. -/
def QIntNonzero (q : R) (r : ℕ) : Prop := ∀ k, 1 ≤ k → k ≤ r → qn q k ≠ 0

/-- **`E` is injective on the lower half**: a weight-`m` vector with `2m < r` killed by `E`
is zero (`r = n + 1`, `[k] ≠ 0` for `k ≤ r`). -/
theorem Em_inj (hq : q ≠ 0) {n m : ℕ} (hqn : QIntNonzero q (n + 1)) (hm : 2 * m < n + 1)
    {v : (Fin (n + 1) → Fin 2) → R} (hv : Supp m v) (hE : Em q n *ᵥ v = 0) : v = 0 := by
  set w : ℕ → (Fin (n + 1) → Fin 2) → R := fun j => (fun u => Fm q n *ᵥ u)^[j] v with hw
  have wsucc : ∀ j, w (j + 1) = Fm q n *ᵥ w j := fun j => Function.iterate_succ_apply' _ _ _
  have hsupp : ∀ j, j ≤ m → Supp (m - j) (w j) := by
    intro j
    induction j with
    | zero => intro _; simpa [hw] using hv
    | succ j ih =>
      intro hj
      rw [wsucc]
      have := ih (by omega)
      rw [show m - j = (m - (j + 1)) + 1 by omega] at this
      exact supp_Fm q this
  set D := n + 1 - 2 * m with hD
  have hc : ∀ j, j ≤ m → Em q n *ᵥ w (j + 1)
      = (-∑ i ∈ Finset.range (j + 1), qn q (D + 2 * i)) • w j := by
    intro j
    induction j with
    | zero =>
      intro _
      rw [wsucc, Em_Fm_mulVec hq, show w 0 = v from rfl, hE, Matrix.mulVec_zero, zero_add,
        Dg_mulVec hq hv]
      congr 1
      simp only [sq]
      rw [if_neg (by omega), show n + 1 - m - m = D by omega]
      simp
    | succ j ih =>
      intro hj
      rw [wsucc (j + 1), Em_Fm_mulVec hq, ih (by omega), Matrix.mulVec_smul, ← wsucc,
        Dg_mulVec hq (hsupp (j + 1) hj), ← add_smul]
      congr 1
      rw [Finset.sum_range_succ _ (j + 1)]
      simp only [sq]
      rw [if_neg (by omega), show n + 1 - (m - (j + 1)) - (m - (j + 1)) = D + 2 * (j + 1) by omega]
      ring
  have hcne : ∀ j, j ≤ m → (-∑ i ∈ Finset.range (j + 1), qn q (D + 2 * i)) ≠ 0 := by
    intro j hj
    rw [neg_ne_zero, sum_qn q hq D (by omega) (j + 1)]
    exact mul_ne_zero (hqn _ (by omega) (by omega)) (hqn _ (by omega) (by omega))
  have htop : w (m + 1) = 0 := by
    rw [wsucc]
    have := hsupp m le_rfl
    rw [Nat.sub_self] at this
    exact Fm_supp_zero q this
  have hdown : ∀ t, t ≤ m + 1 → w (m + 1 - t) = 0 := by
    intro t
    induction t with
    | zero => intro _; simpa using htop
    | succ t ih =>
      intro ht
      have h1 := hc (m - t) (by omega)
      have hz : w (m - t + 1) = 0 := by
        rw [show m - t + 1 = m + 1 - t by omega]; exact ih (by omega)
      rw [hz, Matrix.mulVec_zero] at h1
      have h2 := (smul_eq_zero.mp h1.symm).resolve_left (hcne (m - t) (by omega))
      rwa [show m + 1 - (t + 1) = m - t by omega]
  have := hdown (m + 1) le_rfl
  rwa [Nat.sub_self] at this

end QOU.Archimedean.SchurWeylTrace




