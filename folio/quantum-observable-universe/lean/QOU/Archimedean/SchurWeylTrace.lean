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


/-! ### Signed quantum integers on `ℤ` -/

/-- The signed quantum integer `[N]`, `N ∈ ℤ`: `[−k] = −[k]`. -/
noncomputable def qZ (q : R) : ℤ → R
  | Int.ofNat k => qn q k
  | Int.negSucc k => -qn q (k + 1)

theorem qZ_nat (q : R) (k : ℕ) : qZ q (k : ℤ) = qn q k := rfl

theorem qZ_neg_nat (q : R) (k : ℕ) : qZ q (-(k : ℤ)) = -qn q k := by
  rcases k with _ | k
  · show qZ q (-((0 : ℕ) : ℤ)) = -qn q 0
    simp only [Nat.cast_zero, neg_zero, qn_zero]; rfl
  · rfl

theorem qZ_succ {q : R} (hq : q ≠ 0) (N : ℤ) : qZ q (N + 1) = q * qZ q N + q ^ (-N) := by
  obtain ⟨k, rfl | rfl⟩ := Int.eq_nat_or_neg N
  · rw [show (k : ℤ) + 1 = ((k + 1 : ℕ) : ℤ) by push_cast; ring, qZ_nat, qZ_nat, qn_succ' hq,
      zpow_neg, zpow_natCast, inv_pow]
  · rcases k with _ | j
    · simp only [Nat.cast_zero, neg_zero, zero_add, zpow_zero]
      change qn q 1 = q * qn q 0 + 1
      rw [qn_one, qn_zero]; ring
    · rw [show -((j + 1 : ℕ) : ℤ) + 1 = -(j : ℤ) by push_cast; ring, qZ_neg_nat, qZ_neg_nat,
        neg_neg, zpow_natCast, qn_succ]
      field_simp
      ring

theorem sq_eq_qZ (q : R) (o z : ℕ) : sq q o z = qZ q ((o : ℤ) - z) := by
  unfold sq
  split_ifs with h
  · rw [show (o : ℤ) - z = ((o - z : ℕ) : ℤ) by omega, qZ_nat]
  · rw [show (o : ℤ) - z = -((z - o : ℕ) : ℤ) by omega, qZ_neg_nat]

/-- `[k+1][b+1] = [k][b] + [b+k+1]` for every `b ∈ ℤ`. -/
theorem qZ_mul {q : R} (hq : q ≠ 0) (k : ℕ) (b : ℤ) :
    qn q (k + 1) * qZ q (b + 1) = qn q k * qZ q b + qZ q (b + k + 1) := by
  set G : ℤ → R := fun b => qn q (k + 1) * qZ q (b + 1) - (qn q k * qZ q b + qZ q (b + k + 1))
    with hG
  have hstep : ∀ b, G (b + 1) = q * G b := by
    intro b
    simp only [hG]
    rw [qZ_succ hq (b + 1), qZ_succ hq b, show b + 1 + k + 1 = (b + k + 1) + 1 by ring,
      qZ_succ hq (b + k + 1)]
    have e1 : q ^ (-b) = q ^ (-(b + 1)) * q := by
      rw [← zpow_add_one₀ hq]; ring_nf
    have e2 : q ^ (-(b + k + 1)) = q ^ (-(b + 1)) * (q ^ k)⁻¹ := by
      rw [← zpow_natCast, ← zpow_neg, ← zpow_add₀ hq]; ring_nf
    rw [e1, e2, qn_succ' hq k, inv_pow]
    ring
  have h0 : G 0 = 0 := by
    have e1 : qZ q ((0 : ℤ) + 1) = 1 := by change qn q 1 = 1; exact qn_one q
    have e0 : qZ q 0 = 0 := rfl
    have ek : qZ q ((0 : ℤ) + k + 1) = qn q (k + 1) := by
      rw [show (0 : ℤ) + k + 1 = ((k + 1 : ℕ) : ℤ) by push_cast; ring]; rfl
    simp only [hG]; rw [e1, e0, ek]; ring
  have hall : G b = 0 := by
    induction b using Int.induction_on with
    | zero => exact h0
    | succ i ih => rw [hstep, ih, mul_zero]
    | pred i ih =>
      have := hstep (-(i : ℤ) - 1)
      rw [show -(i : ℤ) - 1 + 1 = -(i : ℤ) by ring, ih] at this
      exact (mul_eq_zero.mp this.symm).resolve_left hq
  simp only [hG, sub_eq_zero] at hall
  exact hall

/-- `Σ_{i<k} [a + 2i] = [k][a + k − 1]` for `a ∈ ℤ`. -/
theorem sum_qZ {q : R} (hq : q ≠ 0) (a : ℤ) :
    ∀ k : ℕ, ∑ i ∈ Finset.range k, qZ q (a + 2 * i) = qn q k * qZ q (a + k - 1)
  | 0 => by simp
  | k + 1 => by
    rw [Finset.sum_range_succ, sum_qZ hq a k]
    have := qZ_mul hq k (a + k - 1)
    rw [show a + k - 1 + 1 = a + ((k + 1 : ℕ) : ℤ) - 1 by push_cast; ring,
      show a + k - 1 + k + 1 = a + 2 * (k : ℤ) by ring] at this
    rw [this]

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

/-! ## 6. The complement symmetry: `Eᵀ` is `E` at `q⁻¹`, conjugated by `0 ↔ 1` -/

/-- Exchange the two letters. -/
def fl (x : Fin 2) : Fin 2 := if x = 0 then 1 else 0

theorem fl_fl (x : Fin 2) : fl (fl x) = x := by
  rcases Fin.exists_fin_two.mp ⟨x, rfl⟩ with h | h <;> subst h <;> decide

theorem fl_eq_zero (x : Fin 2) : fl x = 0 ↔ x = 1 := by
  rcases Fin.exists_fin_two.mp ⟨x, rfl⟩ with h | h <;> subst h <;> decide

theorem fl_eq_one (x : Fin 2) : fl x = 1 ↔ x = 0 := by
  rcases Fin.exists_fin_two.mp ⟨x, rfl⟩ with h | h <;> subst h <;> decide

/-- The complement of a state. -/
def cmp {N : ℕ} (b : Fin N → Fin 2) : Fin N → Fin 2 := fun i => fl (b i)

theorem cmp_cmp {N : ℕ} (b : Fin N → Fin 2) : cmp (cmp b) = b := by
  funext i; exact fl_fl (b i)

theorem cmp_update {N : ℕ} (b : Fin N → Fin 2) (k : Fin N) (y : Fin 2) :
    cmp (Function.update b k y) = Function.update (cmp b) k (fl y) := by
  funext i; by_cases h : i = k
  · subst h; simp [cmp]
  · simp [cmp, Function.update_of_ne h]

theorem ones_cmp {N : ℕ} (b : Fin N → Fin 2) : ones (cmp b) + ones b = N := by
  have h := ones_add_zeros b
  have : ones (cmp b) = (Finset.univ.filter (fun i => ¬ b i = 1)).card := by
    unfold ones; congr 1; ext i; simp only [Finset.mem_filter, cmp, fl_eq_one]
    rcases Fin.exists_fin_two.mp ⟨b i, rfl⟩ with h | h <;> simp [h]
  omega

theorem ki_inv_fl {q : R} (hq : q ≠ 0) (x : Fin 2) : ki q⁻¹ (fl x) = ki q x := by
  rcases Fin.exists_fin_two.mp ⟨x, rfl⟩ with h | h <;> subst h <;> simp [ki, fl, inv_inv]

theorem phiN_inv_cmp (hq : q ≠ 0) {N : ℕ} (k : Fin N) (b : Fin N → Fin 2) :
    phiN q⁻¹ k (cmp b) = phiN q k b := by
  unfold phiN cmp
  refine Finset.prod_congr rfl fun l _ => ?_
  split_ifs <;> simp [ki_inv_fl hq]

/-- **`Eᵀ` at `q` is `E` at `q⁻¹` on complemented states.** -/
theorem Em_transpose (hq : q ≠ 0) {n : ℕ} (a b : Fin (n + 1) → Fin 2) :
    Em q n b a = Em q⁻¹ n (cmp a) (cmp b) := by
  classical
  rw [Em_apply', Em_apply']
  refine Finset.sum_congr rfl fun k _ => ?_
  -- `a k = 0 ∧ b = a[k ↦ 1]`  iff  `b k = 1 ∧ a = b[k ↦ 0]`
  by_cases hak : a k = 0
  · rw [if_pos hak]
    by_cases hb : b = Function.update a k 1
    · subst hb
      have h1 : cmp (Function.update a k 1) k = 0 := by simp [cmp, fl]
      have h2 : cmp a = Function.update (cmp (Function.update a k 1)) k 1 := by
        rw [cmp_update, Function.update_idem]
        funext i; by_cases h : i = k
        · subst h; simp [cmp, fl, hak]
        · simp [Function.update_of_ne h]
      rw [if_pos rfl, if_pos h1, if_pos h2, ← phiN_inv_cmp hq]
      unfold phiN
      refine Finset.prod_congr rfl fun l _ => ?_
      split_ifs with hl
      · rw [cmp_update]
        have : l ≠ k := ne_of_gt hl
        simp [Function.update_of_ne this]
      · rfl
    · rw [if_neg hb]
      split_ifs with h1 h2
      · exfalso; apply hb
        have := congrArg cmp h2
        rw [cmp_cmp, cmp_update, cmp_cmp] at this
        rw [this, Function.update_idem]
        have hbk : b k = 1 := by
          have := h1; simp only [cmp, fl_eq_zero] at this; exact this
        rw [← hbk, Function.update_eq_self]
      · rfl
      · rfl
  · rw [if_neg hak]
    split_ifs with h1 h2
    · exfalso; apply hak
      have := congrFun h2 k
      simp [cmp] at this
      rw [fl_eq_one] at this; exact this
    · rfl
    · rfl

/-! ## 7. Weight-space blocks; `E` is surjective on the upper half -/

/-- The weight-`m` states of `V^{⊗(n+1)}`. -/
abbrev St (n m : ℕ) := {b : Fin (n + 1) → Fin 2 // ones b = m}

/-- The block of `M` from weight `m` to weight `m'`. -/
def blk {n : ℕ} (M : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R) (m m' : ℕ) :
    Matrix (St n m') (St n m) R := Matrix.of fun a b => M a.1 b.1

/-- `M` preserves the weight (the number of ones). -/
def WP {n : ℕ} (M : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R) : Prop :=
  ∀ a b, M a b ≠ 0 → ones a = ones b

theorem sum_over_weight {n : ℕ} (f : (Fin (n + 1) → Fin 2) → R) (m : ℕ)
    (hf : ∀ v, ones v ≠ m → f v = 0) : ∑ v, f v = ∑ v : St n m, f v.1 := by
  classical
  rw [← Finset.sum_subset (Finset.subset_univ (Finset.univ.filter fun v => ones v = m))
    (fun v _ hv => hf v (by simpa using hv))]
  exact Finset.sum_subtype _ (by simp) f

theorem blk_Em_mul {n : ℕ} (q : R) {X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R}
    (hX : WP X) (m : ℕ) : blk (Em q n * X) m (m + 1) = blk (Em q n) m (m + 1) * blk X m m := by
  ext a b
  simp only [blk, Matrix.of_apply, Matrix.mul_apply]
  refine sum_over_weight (fun v => Em q n a.1 v * X v b.1) m fun v hv => ?_
  dsimp only
  by_cases h : X v b.1 = 0
  · rw [h, mul_zero]
  · exact absurd (by rw [hX v b.1 h, b.2]) hv

theorem blk_mul_Em {n : ℕ} (q : R) (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R)
    (m : ℕ) : blk (X * Em q n) m (m + 1) = blk X (m + 1) (m + 1) * blk (Em q n) m (m + 1) := by
  ext a b
  simp only [blk, Matrix.of_apply, Matrix.mul_apply]
  refine sum_over_weight (fun v => X a.1 v * Em q n v b.1) (m + 1) fun v hv => ?_
  dsimp only
  by_cases h : Em q n v b.1 = 0
  · rw [h, mul_zero]
  · exact absurd (by rw [Em_weight q v b.1 h, b.2]) hv

theorem blk_mul {n : ℕ} {X Y : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R}
    (hY : WP Y) (m : ℕ) : blk (X * Y) m m = blk X m m * blk Y m m := by
  ext a b
  simp only [blk, Matrix.of_apply, Matrix.mul_apply]
  refine sum_over_weight (fun v => X a.1 v * Y v b.1) m fun v hv => ?_
  dsimp only
  by_cases h : Y v b.1 = 0
  · rw [h, mul_zero]
  · exact absurd (by rw [hY v b.1 h, b.2]) hv

/-- The weight-`m` block of `X`, as a linear map. -/
noncomputable def Xl {n : ℕ} (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R) (m : ℕ) :
    (St n m → R) →ₗ[R] (St n m → R) := (blk X m m).mulVecLin

/-- `E` from weight `m` to weight `m + 1`, as a linear map. -/
noncomputable def El (q : R) (n m : ℕ) : (St n m → R) →ₗ[R] (St n (m + 1) → R) :=
  (blk (Em q n) m (m + 1)).mulVecLin

theorem El_comp_Xl {n : ℕ} (q : R) {X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R}
    (hX : WP X) (hc : X * Em q n = Em q n * X) (m : ℕ) :
    El q n m ∘ₗ Xl X m = Xl X (m + 1) ∘ₗ El q n m := by
  rw [El, Xl, Xl, ← Matrix.mulVecLin_mul, ← Matrix.mulVecLin_mul, ← blk_Em_mul q hX,
    ← blk_mul_Em, hc]

theorem ker_El_inv {n : ℕ} (q : R) {X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R}
    (hX : WP X) (hc : X * Em q n = Em q n * X) (m : ℕ) :
    ∀ v ∈ LinearMap.ker (El q n m), Xl X m v ∈ LinearMap.ker (El q n m) := by
  intro v hv
  rw [LinearMap.mem_ker] at hv ⊢
  rw [← LinearMap.comp_apply, El_comp_Xl q hX hc, LinearMap.comp_apply, hv, map_zero]

/-- **The standard module** `W_{r,j}`, `r = n + 1`: the vectors of weight `r − j` killed by
`E` (the highest-weight vectors of the summand `L_{r−2j}` of `V^{⊗r}`). -/
noncomputable def Wmod (q : R) (n j : ℕ) : Submodule R (St n (n + 1 - j) → R) :=
  LinearMap.ker (El q n (n + 1 - j))

/-- The trace of `X` on the kernel of `E` at weight `m`. -/
noncomputable def trK (q : R) {n : ℕ} (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R)
    (hX : WP X) (hc : X * Em q n = Em q n * X) (m : ℕ) : R :=
  LinearMap.trace R (LinearMap.ker (El q n m)) ((Xl X m).restrict (ker_El_inv q hX hc m))

theorem ones_le' {n : ℕ} (b : Fin (n + 1) → Fin 2) : ones b ≤ n + 1 := ones_le b

/-- **`E` is surjective on the upper half**: from weight `m` onto weight `m + 1` when
`r ≤ 2m + 1`. -/
theorem El_surj (hq : q ≠ 0) {n : ℕ} (hqn : QIntNonzero q (n + 1)) (m : ℕ)
    (hm : n + 1 ≤ 2 * m + 1) : Function.Surjective (El q n m) := by
  classical
  by_cases hmn : n + 1 < m + 1
  · intro y
    refine ⟨0, funext fun x => ?_⟩
    exact absurd x.2 (by have := ones_le' x.1; omega)
  set A := blk (Em q n) m (m + 1) with hA
  -- `Aᵀ` is injective
  have hinj : Function.Injective A.transpose.mulVecLin := by
    rw [← LinearMap.ker_eq_bot, eq_bot_iff]
    intro u hu
    rw [LinearMap.mem_ker, Matrix.mulVecLin_apply] at hu
    rw [Submodule.mem_bot]
    set v : (Fin (n + 1) → Fin 2) → R :=
      fun c => if h : ones (cmp c) = m + 1 then u ⟨cmp c, h⟩ else 0 with hv
    have hsv : Supp (n - m) v := by
      intro c hc
      have := ones_cmp c
      simp only [hv]
      rw [dif_neg (by omega)]
    have hEv : Em q⁻¹ n *ᵥ v = 0 := by
      funext a
      by_cases ha : ones a = n - m + 1
      · have hx : ones (cmp a) = m := by have := ones_cmp a; omega
        have h0 := congrFun hu ⟨cmp a, hx⟩
        simp only [Matrix.mulVec, dotProduct, Matrix.transpose_apply, hA, blk,
          Matrix.of_apply, Pi.zero_apply] at h0 ⊢
        rw [← h0, ← cmp_cmp a]
        rw [cmp_cmp]
        have e : ∀ c, Em q⁻¹ n a c * v c
            = (fun y => Em q n y (cmp a) * (if h : ones y = m + 1 then u ⟨y, h⟩ else 0)) (cmp c) := by
          intro c
          simp only [hv, Em_transpose hq (cmp a) (cmp c), cmp_cmp]
        rw [Finset.sum_congr rfl fun c _ => e c,
          Fintype.sum_equiv (Function.Involutive.toPerm cmp cmp_cmp)
            (fun c => (fun y => Em q n y (cmp a) *
              (if h : ones y = m + 1 then u ⟨y, h⟩ else 0)) (cmp c))
            (fun y => Em q n y (cmp a) * (if h : ones y = m + 1 then u ⟨y, h⟩ else 0))
            (fun c => rfl)]
        rw [sum_over_weight _ (m + 1) (fun y hy => by simp [hy])]
        refine Finset.sum_congr rfl fun y _ => ?_
        rw [dif_pos y.2]
      · exact supp_Em q⁻¹ hsv a ha
    have hqn' : QIntNonzero q⁻¹ (n + 1) := fun k h1 h2 => by rw [qn_inv hq]; exact hqn k h1 h2
    have hv0 := Em_inj (inv_ne_zero hq) hqn' (by omega) hsv hEv
    funext y
    have := congrFun hv0 (cmp y.1)
    simp only [hv, cmp_cmp, y.2, dif_pos, Pi.zero_apply] at this
    exact this
  have hrank : Module.finrank R (LinearMap.range (El q n m)) = Module.finrank R (St n (m + 1) → R) := by
    have h1 := Matrix.rank_transpose A
    unfold Matrix.rank at h1
    rw [LinearMap.finrank_range_of_inj hinj] at h1
    rw [El, ← hA, ← h1]
  rw [← LinearMap.range_eq_top]
  exact Submodule.eq_top_of_finrank_eq hrank

/-- **One step of the split**: on the upper half, the weight-`m` trace is the trace on the
kernel of `E` plus the weight-`(m+1)` trace. -/
theorem trace_step (hq : q ≠ 0) {n : ℕ} (hqn : QIntNonzero q (n + 1))
    {X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R} (hX : WP X)
    (hc : X * Em q n = Em q n * X) (m : ℕ) (hm : n + 1 ≤ 2 * m + 1) :
    (blk X m m).trace = trK q X hX hc m + (blk X (m + 1) (m + 1)).trace := by
  rw [← Matrix.trace_toLin'_eq, ← Matrix.trace_toLin'_eq, Matrix.toLin'_apply',
    Matrix.toLin'_apply']
  exact trace_eq_trace_ker_add (Xl X m) (Xl X (m + 1)) (El q n m) (El_surj hq hqn m hm)
    (El_comp_Xl q hX hc m) (ker_El_inv q hX hc m)

/-! ## 8. The trace split -/

theorem trace_blk_empty {n : ℕ} (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R)
    (m : ℕ) (hm : n + 1 < m) : (blk X m m).trace = 0 :=
  Finset.sum_eq_zero fun i _ => absurd i.2 (by have := ones_le' i.1; omega)

/-- **The split on the upper half.** For `s ≤ r` with `r ≤ 2(r − s) + 1`,
`T_{r−s}(X) = Σ_{j ≤ s} tr(X | ker E at weight r − j)`. -/
theorem trace_upper (hq : q ≠ 0) {n : ℕ} (hqn : QIntNonzero q (n + 1))
    {X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R} (hX : WP X)
    (hc : X * Em q n = Em q n * X) :
    ∀ s, s ≤ n + 1 → n + 1 ≤ 2 * (n + 1 - s) + 1 →
      (blk X (n + 1 - s) (n + 1 - s)).trace
        = ∑ j ∈ Finset.range (s + 1), trK q X hX hc (n + 1 - j) := by
  intro s
  induction s with
  | zero =>
    intro _ _
    rw [Nat.sub_zero, trace_step hq hqn hX hc (n + 1) (by omega),
      trace_blk_empty X (n + 1 + 1) (by omega)]
    simp
  | succ s ih =>
    intro hs hm
    rw [trace_step hq hqn hX hc (n + 1 - (s + 1)) hm,
      show n + 1 - (s + 1) + 1 = n + 1 - s by omega, ih (by omega) (by omega),
      Finset.sum_range_succ _ (s + 1)]
    ring

/-- `E` is injective from weight `m` when `2m < r`. -/
theorem El_inj (hq : q ≠ 0) {n : ℕ} (hqn : QIntNonzero q (n + 1)) (m : ℕ) (hm : 2 * m < n + 1) :
    Function.Injective (El q n m) := by
  classical
  rw [← LinearMap.ker_eq_bot, eq_bot_iff]
  intro u hu
  rw [LinearMap.mem_ker] at hu
  rw [Submodule.mem_bot]
  set v : (Fin (n + 1) → Fin 2) → R := fun c => if h : ones c = m then u ⟨c, h⟩ else 0 with hv
  have hsv : Supp m v := fun c hc => by simp only [hv]; rw [dif_neg hc]
  have hEv : Em q n *ᵥ v = 0 := by
    funext a
    by_cases ha : ones a = m + 1
    · have h0 := congrFun hu ⟨a, ha⟩
      simp only [El, Matrix.mulVecLin_apply, Matrix.mulVec, dotProduct, blk, Matrix.of_apply,
        Pi.zero_apply] at h0 ⊢
      rw [← h0, sum_over_weight _ m (fun c hc => by simp [hv, hc])]
      refine Finset.sum_congr rfl fun c _ => ?_
      simp only [hv]; rw [dif_pos c.2]
    · exact supp_Em q hsv a ha
  have hv0 := Em_inj hq hqn hm hsv hEv
  funext y
  have := congrFun hv0 y.1
  simp only [hv, y.2, dif_pos, Pi.zero_apply] at this
  exact this

/-- `E^k` from weight `m` to weight `m + k`. -/
noncomputable def Ec (q : R) (n m : ℕ) : (k : ℕ) → ((St n m → R) →ₗ[R] (St n (m + k) → R))
  | 0 => LinearMap.id
  | k + 1 => El q n (m + k) ∘ₗ Ec q n m k

theorem Ec_comp_Xl {n : ℕ} (q : R) {X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R}
    (hX : WP X) (hc : X * Em q n = Em q n * X) (m : ℕ) :
    ∀ k, Ec q n m k ∘ₗ Xl X m = Xl X (m + k) ∘ₗ Ec q n m k
  | 0 => by simp [Ec]
  | k + 1 => by
    rw [Ec, LinearMap.comp_assoc, Ec_comp_Xl q hX hc m k, ← LinearMap.comp_assoc,
      El_comp_Xl q hX hc, LinearMap.comp_assoc]
    rfl

/-- `E^k` on vectors. -/
noncomputable def Epow (q : R) (n k : ℕ) (v : (Fin (n + 1) → Fin 2) → R) :
    (Fin (n + 1) → Fin 2) → R :=
  (fun u => Em q n *ᵥ u)^[k] v

theorem Epow_succ (q : R) (n k : ℕ) (v : (Fin (n + 1) → Fin 2) → R) :
    Epow q n (k + 1) v = Em q n *ᵥ Epow q n k v := Function.iterate_succ_apply' _ _ _

theorem supp_Epow (q : R) {n m : ℕ} {v : (Fin (n + 1) → Fin 2) → R} (hv : Supp m v) :
    ∀ k, Supp (m + k) (Epow q n k v)
  | 0 => hv
  | k + 1 => by rw [Epow_succ]; exact supp_Em q (supp_Epow q hv k)

theorem Dg_mulVec' (hq : q ≠ 0) {n m : ℕ} {v : (Fin (n + 1) → Fin 2) → R} (hv : Supp m v) :
    Matrix.diagonal (Dg q) *ᵥ v = qZ q (2 * (m : ℤ) - ((n : ℤ) + 1)) • v := by
  by_cases hm : m ≤ n + 1
  · rw [Dg_mulVec hq hv, sq_eq_qZ]
    congr 2
    push_cast [Nat.cast_sub hm]; ring
  · have : v = 0 := funext fun b => hv b (by have := ones_le' b; omega)
    subst this; simp

/-- `E^{j+1} F v = F E^{j+1} v + (Σ_{i ≤ j} [2(m+i) − r]) E^j v` for `v` of weight `m`. -/
theorem Epow_Fm (hq : q ≠ 0) {n m : ℕ} {v : (Fin (n + 1) → Fin 2) → R} (hv : Supp m v) :
    ∀ j, Epow q n (j + 1) (Fm q n *ᵥ v)
      = Fm q n *ᵥ Epow q n (j + 1) v
        + (∑ i ∈ Finset.range (j + 1), qZ q (2 * (m : ℤ) - ((n : ℤ) + 1) + 2 * i)) • Epow q n j v
  | 0 => by
    rw [Epow_succ, show Epow q n 0 (Fm q n *ᵥ v) = Fm q n *ᵥ v from rfl, Em_Fm_mulVec hq,
      Dg_mulVec' hq hv, Epow_succ, show Epow q n 0 v = v from rfl]
    simp
  | j + 1 => by
    rw [Epow_succ, Epow_Fm hq hv j, Matrix.mulVec_add, Em_Fm_mulVec hq, Matrix.mulVec_smul,
      Dg_mulVec' hq (supp_Epow q hv (j + 1)), ← Epow_succ, ← Epow_succ, add_assoc, ← add_smul,
      Finset.sum_range_succ _ (j + 1), add_comm (qZ q _)]
    congr 3
    push_cast; ring

/-- **`E^k` is injective on `V_m` when `2m + k ≤ r`.** -/
theorem Epow_inj (hq : q ≠ 0) {n : ℕ} (hqn : QIntNonzero q (n + 1)) :
    ∀ m k, 2 * m + k ≤ n + 1 → ∀ v : (Fin (n + 1) → Fin 2) → R, Supp m v →
      Epow q n k v = 0 → v = 0 := by
  intro m
  induction m with
  | zero =>
    intro k
    induction k with
    | zero => intro _ v _ h; exact h
    | succ k ihk =>
      intro hk v hv h
      have hF : Fm q n *ᵥ v = 0 := Fm_supp_zero q hv
      have := Epow_Fm hq hv k
      rw [hF, h, Matrix.mulVec_zero, zero_add, sum_qZ hq] at this
      have hE : Epow q n (k + 1) (0 : (Fin (n + 1) → Fin 2) → R) = 0 := by
        clear this; generalize k + 1 = t; induction t with
        | zero => rfl
        | succ t iht => rw [Epow_succ, iht, Matrix.mulVec_zero]
      rw [hE] at this
      have hc : qn q (k + 1) * qZ q (2 * ((0 : ℕ) : ℤ) - ((n : ℤ) + 1) + ((k + 1 : ℕ) : ℤ) - 1) ≠ 0 := by
        rw [show 2 * ((0 : ℕ) : ℤ) - ((n : ℤ) + 1) + ((k + 1 : ℕ) : ℤ) - 1
          = -((n + 1 - k : ℕ) : ℤ) by push_cast [Nat.cast_sub (show k ≤ n + 1 by omega)]; ring,
          qZ_neg_nat]
        exact mul_ne_zero (hqn _ (by omega) (by omega)) (neg_ne_zero.mpr (hqn _ (by omega) (by omega)))
      exact ihk (by omega) v hv ((smul_eq_zero.mp this.symm).resolve_left hc)
  | succ m ihm =>
    intro k
    induction k with
    | zero => intro _ v _ h; exact h
    | succ k ihk =>
      intro hk v hv h
      have hFs : Supp m (Fm q n *ᵥ v) := supp_Fm q hv
      have hF : Fm q n *ᵥ v = 0 := by
        refine ihm (k + 2) (by omega) _ hFs ?_
        rw [Epow_Fm hq hv (k + 1), Epow_succ q n (k + 1), h, Matrix.mulVec_zero,
          Matrix.mulVec_zero, smul_zero, add_zero]
      have := Epow_Fm hq hv k
      have hE : Epow q n (k + 1) (0 : (Fin (n + 1) → Fin 2) → R) = 0 := by
        clear this; generalize k + 1 = t; induction t with
        | zero => rfl
        | succ t iht => rw [Epow_succ, iht, Matrix.mulVec_zero]
      rw [hF, h, Matrix.mulVec_zero, zero_add, sum_qZ hq, hE] at this
      have hc : qn q (k + 1) * qZ q (2 * ((m + 1 : ℕ) : ℤ) - ((n : ℤ) + 1) + ((k + 1 : ℕ) : ℤ) - 1)
          ≠ 0 := by
        rw [show 2 * ((m + 1 : ℕ) : ℤ) - ((n : ℤ) + 1) + ((k + 1 : ℕ) : ℤ) - 1
          = -((n + 1 - 2 * (m + 1) - k : ℕ) : ℤ) by
            push_cast [Nat.cast_sub (show k ≤ n + 1 - 2 * (m + 1) by omega),
              Nat.cast_sub (show 2 * (m + 1) ≤ n + 1 by omega)]; ring,
          qZ_neg_nat]
        exact mul_ne_zero (hqn _ (by omega) (by omega)) (neg_ne_zero.mpr (hqn _ (by omega) (by omega)))
      exact ihk (by omega) v hv ((smul_eq_zero.mp this.symm).resolve_left hc)

/-- Extension by zero of a weight-`m` vector. -/
noncomputable def ext0 {n : ℕ} (m : ℕ) (u : St n m → R) : (Fin (n + 1) → Fin 2) → R :=
  fun c => if h : ones c = m then u ⟨c, h⟩ else 0

theorem supp_ext0 {n m : ℕ} (u : St n m → R) : Supp m (ext0 m u) := fun c hc => by
  simp only [ext0]; rw [dif_neg hc]

theorem ext0_eq_zero {n m : ℕ} {u : St n m → R} (h : ext0 m u = 0) : u = 0 := by
  funext y
  have := congrFun h y.1
  simp only [ext0, y.2, dif_pos, Pi.zero_apply] at this
  exact this

theorem ext0_El (q : R) {n m : ℕ} (u : St n m → R) :
    ext0 (m + 1) (El q n m u) = Em q n *ᵥ ext0 m u := by
  classical
  funext a
  by_cases ha : ones a = m + 1
  · simp only [ext0, ha, dif_pos, El, Matrix.mulVecLin_apply, Matrix.mulVec, dotProduct, blk,
      Matrix.of_apply]
    rw [sum_over_weight (fun c => Em q n a c * (if h : ones c = m then u ⟨c, h⟩ else 0)) m
      (fun c hc => by simp [hc])]
    refine Finset.sum_congr rfl fun c _ => ?_
    rw [dif_pos c.2]
  · rw [supp_Em q (supp_ext0 u) a ha]
    simp only [ext0]; rw [dif_neg ha]

theorem ext0_Ec (q : R) {n m : ℕ} (u : St n m → R) :
    ∀ k, ext0 (m + k) (Ec q n m k u) = Epow q n k (ext0 m u)
  | 0 => rfl
  | k + 1 => by
    rw [Ec, LinearMap.comp_apply]
    show ext0 (m + k + 1) (El q n (m + k) (Ec q n m k u)) = _
    rw [ext0_El, ext0_Ec q u k, ← Epow_succ]

theorem Ec_inj (hq : q ≠ 0) {n : ℕ} (hqn : QIntNonzero q (n + 1)) (m k : ℕ)
    (h : 2 * m + k ≤ n + 1) : Function.Injective (Ec q n m k) := by
  rw [← LinearMap.ker_eq_bot, eq_bot_iff]
  intro u hu
  rw [LinearMap.mem_ker] at hu
  rw [Submodule.mem_bot]
  apply ext0_eq_zero
  refine Epow_inj hq hqn m k h _ (supp_ext0 u) ?_
  rw [← ext0_Ec, hu]
  funext c; simp [ext0]

theorem card_St (n m : ℕ) : Fintype.card (St n m) = (n + 1).choose m := by
  classical
  rw [Fintype.card_subtype, card_ones_eq]

/-- **The lower half is isomorphic to the upper half**: `T_m(X) = T_{r−m}(X)` for `2m < r`. -/
theorem trace_lower (hq : q ≠ 0) {n : ℕ} (hqn : QIntNonzero q (n + 1))
    {X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R} (hX : WP X)
    (hc : X * Em q n = Em q n * X) (m : ℕ) (hm : 2 * m < n + 1) :
    (blk X m m).trace = (blk X (n + 1 - m) (n + 1 - m)).trace := by
  set k := n + 1 - 2 * m with hk
  have hinj := Ec_inj hq hqn m k (by omega)
  have hdim : Module.finrank R (St n m → R) = Module.finrank R (St n (m + k) → R) := by
    rw [Module.finrank_fintype_fun_eq_card, Module.finrank_fintype_fun_eq_card, card_St, card_St,
      show m + k = n + 1 - m by omega, Nat.choose_symm (by omega)]
  have hbij : Function.Bijective (Ec q n m k) :=
    ⟨hinj, (LinearMap.injective_iff_surjective_of_finrank_eq_finrank hdim).mp hinj⟩
  set e := LinearEquiv.ofBijective (Ec q n m k) hbij
  have hconj : e.conj (Xl X m) = Xl X (m + k) := by
    apply LinearMap.ext; intro y
    obtain ⟨x, rfl⟩ := e.surjective y
    rw [LinearEquiv.conj_apply]
    simp only [LinearMap.comp_apply, LinearEquiv.coe_coe, LinearEquiv.symm_apply_apply]
    show Ec q n m k (Xl X m x) = Xl X (m + k) (Ec q n m k x)
    rw [← LinearMap.comp_apply, Ec_comp_Xl q hX hc m k, LinearMap.comp_apply]
  have h := LinearMap.trace_conj' (Xl X m) e
  rw [hconj, Xl, Xl, ← Matrix.toLin'_apply', ← Matrix.toLin'_apply', Matrix.trace_toLin'_eq,
    Matrix.trace_toLin'_eq] at h
  rw [← h, show m + k = n + 1 - m by omega]

/-- **The Schur–Weyl trace split** (`r = n + 1`, `[k]_q ≠ 0` for `1 ≤ k ≤ r`). For every
weight-preserving `X` commuting with `E`,
`tr(X | V_m) = Σ_{j ≤ min(m, r − m)} tr(X | W_{r,j})`, `W_{r,j} = ker E ∩ V_{r−j}`. -/
theorem trace_split (hq : q ≠ 0) {n : ℕ} (hqn : QIntNonzero q (n + 1))
    {X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R} (hX : WP X)
    (hc : X * Em q n = Em q n * X) (m : ℕ) (hm : m ≤ n + 1) :
    (blk X m m).trace = ∑ j ∈ Finset.range (min m (n + 1 - m) + 1), trK q X hX hc (n + 1 - j) := by
  rcases Nat.lt_or_ge (2 * m) (n + 1) with h | h
  · rw [trace_lower hq hqn hX hc m h, min_eq_left (by omega)]
    have := trace_upper hq hqn hX hc m (by omega) (by omega)
    exact this
  · rw [min_eq_right (by omega)]
    have := trace_upper hq hqn hX hc (n + 1 - m) (by omega) (by omega)
    rwa [show n + 1 - (n + 1 - m) = m by omega] at this

/-- The weight-space trace of `RossoJonesGeneral` is the trace of the block. -/
theorem T_eq_trace_blk {n : ℕ} (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R)
    (m : ℕ) : T X m = (blk X m m).trace := by
  classical
  rw [T, Matrix.trace]
  exact Finset.sum_subtype _ (by simp) (fun u => X u u)

end QOU.Archimedean.SchurWeylTrace







