import QOU.Archimedean.RossoJonesMiddle

/-!
# Rosso–Jones for torus links: all `(r, s)`, including `gcd(r, s) > 1`

WIP.
-/

namespace QOU.Archimedean.RossoJonesGeneral

open QOU.IwahoriHecke.TensorMarkovModel QOU.IwahoriHecke.JonesNormalForm
open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix QOU.IwahoriHecke.QuantumTrace
open QOU.IwahoriHecke.MarkovPeel

variable {R : Type*} [Field R] {q : R}

/-! ## Step 1. The telescoping, summed (no coprimality) -/

/-- **The weight-space traces of `γ^p` from those of the two weighted rotations**, for every
`p`: `T_m(γ^p) = Σ_{j ≤ m} T_j(ρ^p) − Σ_{j < m} T_j(ρ'^p)`. -/
theorem T_gam_eq_sum (hq : q ≠ 0) (n p : ℕ) : ∀ m,
    T (gam q n ^ p) m = ∑ j ∈ Finset.range (m + 1), T (rho q n ^ p) j
      - ∑ j ∈ Finset.range m, T (rho' q n ^ p) j
  | 0 => by
    rw [Finset.sum_range_one, Finset.sum_range_zero, sub_zero, T_zero, rho, T_rotMat_pow_zero]
    simp [cRho, Fin.init, qz, ← pow_mul]
  | m + 1 => by
    rw [T_gam_succ hq, T_gam_eq_sum hq n p m,
      Finset.sum_range_succ (fun j => T (rho q n ^ p) j) (m + 1),
      Finset.sum_range_succ (fun j => T (rho' q n ^ p) j) m]
    ring

/-! ## Step 2. Counting ones -/

theorem ones_eq_sum {n : ℕ} (u : Fin n → Fin 2) :
    ones u = ∑ i, if u i = 1 then 1 else 0 := by
  rw [ones, Finset.card_filter]

theorem ones_comp_equiv {n : ℕ} (u : Fin n → Fin 2) (e : Fin n ≃ Fin n) :
    ones (fun i => u (e i)) = ones u := by
  rw [ones_eq_sum, ones_eq_sum]
  exact Equiv.sum_comp e (fun i => if u i = 1 then 1 else 0)

theorem ones_rot {n : ℕ} (b : Fin (n + 1) → Fin 2) : ones (rot b) = ones b := by
  have : rot b = fun i => b (Equiv.subRight (1 : Fin (n + 1)) i) := funext (rot_apply b)
  rw [this, ones_comp_equiv]

theorem ones_rot_iterate {n : ℕ} (b : Fin (n + 1) → Fin 2) (k : ℕ) :
    ones (rot^[k] b) = ones b := by
  induction k with
  | zero => rfl
  | succ k ih => rw [Function.iterate_succ_apply', ones_rot, ih]

theorem ones_snoc {n : ℕ} (c : Fin n → Fin 2) (x : Fin 2) :
    ones (Fin.snoc c x : Fin (n + 1) → Fin 2) = ones c + if x = 1 then 1 else 0 := by
  rw [ones_eq_sum, ones_eq_sum, Fin.sum_univ_castSucc]
  simp

theorem prod_qo_eq {n : ℕ} (q : R) (c : Fin n → Fin 2) : (∏ i, qo q (c i)) = q ^ ones c := by
  classical
  simp only [qo]
  rw [Finset.prod_ite, Finset.prod_const_one, mul_one, Finset.prod_const]
  rfl

theorem ones_add_zeros {n : ℕ} (c : Fin n → Fin 2) :
    ones c + (Finset.univ.filter (fun i => ¬ c i = 1)).card = n := by
  rw [ones, Finset.filter_card_add_filter_neg_card_eq_card]; simp

theorem prod_qz_eq {n : ℕ} (q : R) (c : Fin n → Fin 2) :
    (∏ i, qz q (c i)) = q ^ (n - ones c) := by
  classical
  have h01 : ∀ x : Fin 2, (x = 0) ↔ ¬ x = 1 := by decide
  simp only [qz, h01]
  rw [Finset.prod_ite, Finset.prod_const_one, mul_one, Finset.prod_const]
  congr 1
  have := ones_add_zeros c
  omega

theorem ones_eq_init {n : ℕ} (b : Fin (n + 1) → Fin 2) :
    ones b = ones (Fin.init b) + if b (Fin.last n) = 1 then 1 else 0 := by
  conv_lhs => rw [← Fin.snoc_init_self b]
  rw [ones_snoc]

/-! ## Step 3. The two weighted rotations depend only on the weight and the last letter -/

/-- A weighted rotation whose weight depends only on the number of ones and the last letter. -/
noncomputable def wRot {n : ℕ} (α β : ℕ → R) : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R :=
  rotMat fun b => if b (Fin.last n) = 0 then α (ones b) else β (ones b)

theorem rho_eq_wRot (q : R) (n : ℕ) :
    rho q n = wRot (n := n) (fun j => q ^ (n - j)) (fun j => q ^ (j - 1) * q⁻¹ ^ 2) := by
  unfold rho wRot
  congr 1
  funext b
  rw [cRho, prod_qz_eq, prod_qo_eq, ones_eq_init b]
  rcases Fin.exists_fin_two.mp ⟨b (Fin.last n), rfl⟩ with h | h <;> simp [h]

theorem rho'_eq_wRot (q : R) (n : ℕ) :
    rho' q n = wRot (n := n) (fun j => q ^ (n - j) * q⁻¹ ^ 2) (fun j => q ^ (j - 1)) := by
  unfold rho' wRot
  congr 1
  funext b
  rw [cRho', prod_qz_eq, prod_qo_eq, ones_eq_init b]
  rcases Fin.exists_fin_two.mp ⟨b (Fin.last n), rfl⟩ with h | h <;> simp [h]

/-- The number of ones among the last letters of `b, rot b, …, rot^{p−1} b`. -/
def lastOnes {n : ℕ} (p : ℕ) (b : Fin (n + 1) → Fin 2) : ℕ :=
  ((Finset.range p).filter (fun k => b (Fin.last n - k • (1 : Fin (n + 1))) = 1)).card

theorem rot_iterate_last {n : ℕ} (b : Fin (n + 1) → Fin 2) (k : ℕ) :
    rot^[k] b (Fin.last n) = b (Fin.last n - k • (1 : Fin (n + 1))) := by
  rw [rot_iterate]

theorem prod_wRot_weights {n : ℕ} (α β : ℕ → R) (p : ℕ) (b : Fin (n + 1) → Fin 2) :
    (∏ k ∈ Finset.range p, (fun b : Fin (n + 1) → Fin 2 =>
        if b (Fin.last n) = 0 then α (ones b) else β (ones b)) (rot^[k] b))
      = α (ones b) ^ (p - lastOnes p b) * β (ones b) ^ lastOnes p b := by
  classical
  have h01 : ∀ (x : Fin 2) (u v : R), (if x = 0 then u else v) = if x = 1 then v else u := by
    intro x u v; rcases Fin.exists_fin_two.mp ⟨x, rfl⟩ with h | h <;> simp [h]
  simp only [ones_rot_iterate, rot_iterate_last, h01]
  rw [Finset.prod_ite, Finset.prod_const, Finset.prod_const, mul_comm]
  have hc := Finset.filter_card_add_filter_neg_card_eq_card
    (s := Finset.range p) (fun k => b (Fin.last n - k • (1 : Fin (n + 1))) = 1)
  rw [Finset.card_range] at hc
  unfold lastOnes
  congr 2
  omega

/-! ## Step 4. Double counting: `(n + 1) · lastOnes = p · ones` on `rot^p`-fixed states -/

theorem periodic_shift (f : ℕ → ℕ) (P : ℕ) (hf : ∀ k, f (k + P) = f k) :
    ∀ t k, f (P * t + k) = f k := by
  intro t
  induction t with
  | zero => intro k; simp
  | succ t ih =>
    intro k
    rw [show P * (t + 1) + k = (P * t + k) + P by ring, hf, ih]

theorem sum_range_mul_of_periodic (f : ℕ → ℕ) (P : ℕ) (hf : ∀ k, f (k + P) = f k) :
    ∀ t, ∑ k ∈ Finset.range (P * t), f k = t * ∑ k ∈ Finset.range P, f k := by
  intro t
  induction t with
  | zero => simp
  | succ t ih =>
    rw [Nat.mul_succ, Finset.sum_range_add, ih]
    simp only [periodic_shift f P hf t]
    ring

theorem nsmul_one_self (n : ℕ) : (n + 1) • (1 : Fin (n + 1)) = 0 := by
  apply Fin.ext; rw [val_nsmul_one, Nat.mod_self]; rfl

theorem nat_nsmul_one_val {n : ℕ} (i : Fin (n + 1)) : (i : ℕ) • (1 : Fin (n + 1)) = i := by
  apply Fin.ext; rw [val_nsmul_one, Nat.mod_eq_of_lt i.isLt]

theorem rot_fixed_iff {n p : ℕ} (b : Fin (n + 1) → Fin 2) :
    rot^[p] b = b ↔ ∀ i, b (i - p • (1 : Fin (n + 1))) = b i := by
  rw [rot_iterate, funext_iff]

theorem lastOnes_mul {n p : ℕ} (b : Fin (n + 1) → Fin 2) (hb : rot^[p] b = b) :
    (n + 1) * lastOnes p b = p * ones b := by
  classical
  have hp := (rot_fixed_iff b).mp hb
  set c : ℕ → ℕ := fun k => if b (Fin.last n - k • (1 : Fin (n + 1))) = 1 then 1 else 0 with hc
  have hcn : ∀ k, c (k + (n + 1)) = c k := by
    intro k; simp only [hc]; rw [add_nsmul, nsmul_one_self, add_zero]
  have hcp : ∀ k, c (k + p) = c k := by
    intro k; simp only [hc, add_nsmul, ← sub_sub, hp]
  have hS : lastOnes p b = ∑ k ∈ Finset.range p, c k := by
    rw [lastOnes, Finset.card_filter]
  have hO : ∑ k ∈ Finset.range (n + 1), c k = ones b := by
    rw [← Fin.sum_univ_eq_sum_range c]
    simp only [hc, nat_nsmul_one_val]
    rw [← ones_comp_equiv b (Equiv.subLeft (Fin.last n)), ones_eq_sum]
    rfl
  have h1 := sum_range_mul_of_periodic c (n + 1) hcn p
  have h2 := sum_range_mul_of_periodic c p hcp (n + 1)
  rw [mul_comm p (n + 1), h1, hO] at h2
  rw [hS, ← h2]

/-! ## Step 5. The trace of a power of a weighted rotation -/

/-- The weight-`j` states fixed by `rot^p`. -/
noncomputable def fixSet (n p j : ℕ) : Finset (Fin (n + 1) → Fin 2) :=
  Finset.univ.filter fun b => ones b = j ∧ rot^[p] b = b

theorem T_wRot_pow {n : ℕ} (α β : ℕ → R) (p j : ℕ) :
    T (wRot (n := n) α β ^ p) j
      = ((fixSet n p j).card : R) * (α j ^ (p - p * j / (n + 1)) * β j ^ (p * j / (n + 1))) := by
  classical
  have hval : ∀ b ∈ fixSet n p j,
      (∏ k ∈ Finset.range p, (fun b : Fin (n + 1) → Fin 2 =>
        if b (Fin.last n) = 0 then α (ones b) else β (ones b)) (rot^[k] b))
        = α j ^ (p - p * j / (n + 1)) * β j ^ (p * j / (n + 1)) := by
    intro b hb
    obtain ⟨hj, hfix⟩ := (Finset.mem_filter.mp hb).2
    have hS : lastOnes p b = p * j / (n + 1) := by
      rw [← hj, ← lastOnes_mul b hfix, Nat.mul_div_cancel_left _ (Nat.succ_pos n)]
    rw [prod_wRot_weights, hS, hj]
  unfold T wRot
  simp only [rotMat_pow_apply]
  rw [Finset.sum_ite, Finset.sum_const_zero, add_zero, Finset.filter_filter]
  have hset : Finset.univ.filter (fun b : Fin (n + 1) → Fin 2 => ones b = j ∧ b = rot^[p] b)
      = fixSet n p j := by
    unfold fixSet
    congr 1; funext b; simp only [eq_comm (a := b)]
  rw [hset, Finset.sum_congr rfl hval, Finset.sum_const, nsmul_eq_mul]

/-! ## Step 6. Counting the fixed states -/

/-- `rot^p` fixes `b` iff `rot^s` does, for any `s` with `s ∣ p` and `s ≡ p x (mod n + 1)`;
first the iteration lemma. -/
theorem shift_mul {n : ℕ} (b : Fin (n + 1) → Fin 2) (s : ℕ)
    (h : ∀ i, b (i - s • (1 : Fin (n + 1))) = b i) :
    ∀ t i, b (i - (s * t) • (1 : Fin (n + 1))) = b i := by
  intro t
  induction t with
  | zero => intro i; simp
  | succ t ih =>
    intro i
    rw [Nat.mul_succ, add_nsmul, ← sub_sub, h, ih]

theorem rot_fixed_iff_gcd {n p : ℕ} (b : Fin (n + 1) → Fin 2) :
    rot^[p] b = b ↔ ∀ i, b (i - (Nat.gcd (n + 1) p) • (1 : Fin (n + 1))) = b i := by
  rw [rot_fixed_iff]
  set d := Nat.gcd (n + 1) p with hd
  constructor
  · intro hp
    by_cases hdiv : (n + 1) ∣ p
    · have : d = n + 1 := Nat.gcd_eq_left hdiv
      intro i; rw [this, nsmul_one_self, sub_zero]
    · have hlt : Nat.gcd p (n + 1) < n + 1 := by
        rcases Nat.lt_or_ge (Nat.gcd p (n + 1)) (n + 1) with h | h
        · exact h
        · exfalso; apply hdiv
          have h1 : Nat.gcd p (n + 1) ≤ n + 1 := Nat.gcd_le_right _ (Nat.succ_pos n)
          have h2 : Nat.gcd p (n + 1) = n + 1 := le_antisymm h1 h
          rw [← h2]; exact Nat.gcd_dvd_left _ _
      obtain ⟨x, hx⟩ := Nat.exists_mul_emod_eq_gcd hlt
      have hpx : (p * x) • (1 : Fin (n + 1)) = d • (1 : Fin (n + 1)) := by
        apply Fin.ext
        rw [val_nsmul_one, val_nsmul_one, hx, hd, Nat.gcd_comm (n + 1) p, Nat.mod_eq_of_lt hlt]
      intro i
      rw [← hpx]
      exact shift_mul b p hp x i
  · intro hdp i
    have := shift_mul b d hdp (p / d) i
    rwa [Nat.mul_div_cancel' (Nat.gcd_dvd_right _ _)] at this

/-- The periodic extension of a word of length `d`. -/
def perExt {n d : ℕ} (hd : 0 < d) (c : Fin d → Fin 2) : Fin (n + 1) → Fin 2 :=
  fun i => c ⟨(i : ℕ) % d, Nat.mod_lt _ hd⟩

/-- The first `d` letters. -/
def restr {n d : ℕ} (hdn : d ≤ n + 1) (b : Fin (n + 1) → Fin 2) : Fin d → Fin 2 :=
  fun k => b ⟨k, lt_of_lt_of_le k.isLt hdn⟩

theorem perExt_periodic {n d : ℕ} (hd : 0 < d) (hdvd : d ∣ n + 1) (c : Fin d → Fin 2) :
    ∀ i, perExt (n := n) hd c (i - d • (1 : Fin (n + 1))) = perExt hd c i := by
  intro i
  unfold perExt
  congr 2
  have hdn : d ≤ n + 1 := Nat.le_of_dvd (Nat.succ_pos n) hdvd
  have hv : ((d • (1 : Fin (n + 1)) : Fin (n + 1)) : ℕ) = d % (n + 1) := val_nsmul_one d
  rw [Fin.coe_sub, hv, Nat.mod_mod_of_dvd _ hdvd]
  rcases Nat.lt_or_ge d (n + 1) with h | h
  · rw [Nat.mod_eq_of_lt h]
    obtain ⟨e, he⟩ := hdvd
    rcases e with _ | e
    · simp at he
    · have h2 : n + 1 - d = d * e := by rw [he, Nat.mul_succ, Nat.add_sub_cancel]
      rw [h2, add_comm, Nat.add_mul_mod_self_left]
  · have : d = n + 1 := le_antisymm hdn h
    subst this
    rw [Nat.mod_self, Nat.sub_zero, Nat.add_mod_left]

theorem eq_perExt_restr {n d : ℕ} (hd : 0 < d) (hdn : d ≤ n + 1) (b : Fin (n + 1) → Fin 2)
    (hb : ∀ i, b (i - d • (1 : Fin (n + 1))) = b i) : perExt hd (restr hdn b) = b := by
  funext i
  have hi := shift_mul b d hb ((i : ℕ) / d) i
  rw [← hi]
  unfold perExt restr
  congr 1
  have hle : ((d * ((i : ℕ) / d)) • (1 : Fin (n + 1))) ≤ i := by
    rw [Fin.le_def, val_nsmul_one, Nat.mod_eq_of_lt (lt_of_le_of_lt (Nat.mul_div_le _ _) i.isLt)]
    exact Nat.mul_div_le _ _
  apply Fin.ext
  rw [Fin.coe_sub_iff_le.mpr hle, val_nsmul_one,
    Nat.mod_eq_of_lt (lt_of_le_of_lt (Nat.mul_div_le _ _) i.isLt)]
  have := Nat.mod_add_div (i : ℕ) d
  simp only
  omega

theorem restr_perExt {n d : ℕ} (hd : 0 < d) (hdn : d ≤ n + 1) (c : Fin d → Fin 2) :
    restr hdn (perExt (n := n) hd c) = c := by
  funext k
  simp only [perExt, restr]
  congr 1
  exact Fin.ext (Nat.mod_eq_of_lt k.isLt)

theorem ones_perExt {n d e : ℕ} (hd : 0 < d) (he : n + 1 = d * e) (c : Fin d → Fin 2) :
    ones (perExt (n := n) hd c) = e * ones c := by
  classical
  set g : ℕ → ℕ := fun k => if c ⟨k % d, Nat.mod_lt _ hd⟩ = 1 then 1 else 0 with hg
  have h1 : ones (perExt (n := n) hd c) = ∑ k ∈ Finset.range (n + 1), g k := by
    rw [ones_eq_sum, ← Fin.sum_univ_eq_sum_range g]; rfl
  have h2 : ones c = ∑ k ∈ Finset.range d, g k := by
    rw [ones_eq_sum, ← Fin.sum_univ_eq_sum_range g]
    refine Finset.sum_congr rfl fun k _ => ?_
    simp only [hg, Nat.mod_eq_of_lt k.isLt]
  have hper : ∀ k, g (k + d) = g k := by
    intro k; simp only [hg, Nat.add_mod_right]
  rw [h1, h2, he, sum_range_mul_of_periodic g d hper e]

/-- The number of `0/1` words of length `d` with `k` ones is `C(d, k)`. -/
theorem card_ones_eq (d k : ℕ) :
    (Finset.univ.filter fun c : Fin d → Fin 2 => ones c = k).card = d.choose k := by
  classical
  rw [show d.choose k = (Finset.powersetCard k (Finset.univ : Finset (Fin d))).card by
    rw [Finset.card_powersetCard, Finset.card_univ, Fintype.card_fin]]
  refine Finset.card_nbij' (fun c => Finset.univ.filter fun i => c i = 1)
    (fun s i => if i ∈ s then 1 else 0) ?_ ?_ ?_ ?_
  · intro c hc
    rw [Finset.mem_coe, Finset.mem_filter] at hc
    rw [Finset.mem_coe, Finset.mem_powersetCard]
    exact ⟨Finset.subset_univ _, hc.2⟩
  · intro s hs
    rw [Finset.mem_coe, Finset.mem_powersetCard] at hs
    rw [Finset.mem_coe, Finset.mem_filter]
    refine ⟨Finset.mem_univ _, ?_⟩
    rw [← hs.2, ones]
    congr 1
    ext i; by_cases h : i ∈ s <;> simp [h]
  · intro c _
    funext i
    rcases Fin.exists_fin_two.mp ⟨c i, rfl⟩ with h | h <;> simp [h]
  · intro s _
    ext i; by_cases h : i ∈ s <;> simp [h]

end QOU.Archimedean.RossoJonesGeneral
