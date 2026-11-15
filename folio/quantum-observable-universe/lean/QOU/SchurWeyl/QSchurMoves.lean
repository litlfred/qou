/-
Copyright (c) 2026 QOU contributors.
-/
import QOU.SchurWeyl.QuantumGLAction

/-!
# Powers of a one-letter move on `V^{⊗n}` (G3.4-DJ, obligation O1)

`M = siteOp (E_{yx}) w` moves one letter `x ↦ y` at some site `s` with the tail weight
`∏_{k > s} w(b k)`. `raiseOp q qi i j` is the case `x = i, y = j`; `lowerOp q qi i j` is
`x = j, y = i`; both use `w = kap q qi i j`.

**Closed form** (`move_pow_mulVec_single`): for a word `c` and `k : ℕ`,

  `M^k e_c = G_k · Σ_{S ⊆ c⁻¹(x), |S| = k} Θ_c(S) · e_{c[S ↦ y]}`,

where `Θ_c(S) = ∏_{s ∈ S} ∏_{k > s, k ∉ S} w(c k)` and
`G_k = ∏_{r=1}^{k} h_r`, `h_r = Σ_{t < r} w(x)^t w(y)^{r−1−t}` (a homogeneous Gaussian
integer; for `raiseOp`, `h_r = q^{1−r} [r]_{q²}`).

Proof: induction on `k`, regrouping `(S, s) ↦ insert s S` and the identity
`Θ(S'∖s) · ∏_{k>s} w(c[S'∖s] k) = Θ(S') · w(x)^{#S'_{<s}} w(y)^{#S'_{>s}}`.
Generic commutative ring (§7c).
-/

namespace QOU.SchurWeyl.QSchurMoves

open QOU.SchurWeyl.QuantumGL Matrix Finset

variable {R : Type*} [CommRing R] {d n : ℕ}

/-- The basis vector `e_b`. -/
abbrev bv (b : Fin n → Fin d) : (Fin n → Fin d) → R := Pi.single b 1

/-- The one-letter move `x ↦ y` with tail weight `w`. -/
def move (x y : Fin d) (w : Fin d → R) : Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  siteOp (Matrix.single y x 1) w

/-- **One move on a basis vector.** -/
theorem move_mulVec_single (x y : Fin d) (w : Fin d → R) (b : Fin n → Fin d) :
    move x y w *ᵥ bv b
      = ∑ s ∈ univ.filter (fun s => b s = x),
          (∏ k ∈ Ioi s, w (b k)) • bv (Function.update b s y) := by
  classical
  funext a
  have hl : (move x y w *ᵥ bv b) a = move x y w a b := by
    simp [bv, mulVec_single]
  rw [hl, move, siteOp, Matrix.sum_apply, Finset.sum_apply]
  simp only [Pi.smul_apply, smul_eq_mul, bv, siteTerm, of_apply]
  rw [Finset.sum_filter]
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [single_apply']
  by_cases ha : a = Function.update b s y
  · subst ha
    have hag : ∀ k, k ≠ s → Function.update b s y k = b k := fun k hk =>
      Function.update_of_ne hk _ _
    rw [if_pos hag, Function.update_self, Pi.single_eq_same, mul_one]
    by_cases hb : b s = x
    · rw [if_pos ⟨rfl, hb⟩, if_pos hb, one_mul]
    · rw [if_neg (fun h => hb h.2), if_neg hb, zero_mul]
  · rw [Pi.single_apply, if_neg ha, mul_zero, ite_self]
    by_cases hag : ∀ k, k ≠ s → a k = b k
    · rw [if_pos hag]
      by_cases h1 : a s = y ∧ b s = x
      · exfalso; apply ha
        funext k
        by_cases hk : k = s
        · subst hk; rw [Function.update_self]; exact h1.1
        · rw [Function.update_of_ne hk]; exact hag k hk
      · rw [if_neg h1, zero_mul]
    · rw [if_neg hag]

/-! ### Notation for the closed form -/

/-- Overwrite the sites in `S` with the letter `y`. -/
def updS (y : Fin d) (c : Fin n → Fin d) (S : Finset (Fin n)) : Fin n → Fin d :=
  fun k => if k ∈ S then y else c k

/-- `Θ_c(S) = ∏_{s ∈ S} ∏_{k > s, k ∉ S} w(c k)`. -/
def theta (w : Fin d → R) (c : Fin n → Fin d) (S : Finset (Fin n)) : R :=
  ∏ s ∈ S, ∏ k ∈ (Ioi s).filter (fun k => k ∉ S), w (c k)

/-- The homogeneous Gaussian integer `h_r(a, b) = Σ_{t < r} a^t b^{r−1−t}`. -/
def hq (a b : R) (r : ℕ) : R := ∑ t ∈ range r, a ^ t * b ^ (r - 1 - t)

/-- `G_k = ∏_{r=1}^{k} h_r`. -/
def gq (a b : R) (k : ℕ) : R := ∏ r ∈ range k, hq a b (r + 1)

theorem hq_succ (a b : R) (r : ℕ) : hq a b (r + 1) = a ^ r + b * hq a b r := by
  unfold hq
  rw [sum_range_succ, Nat.add_sub_cancel, Nat.sub_self, pow_zero, mul_one, add_comm,
    mul_sum]
  congr 1
  refine sum_congr rfl fun t ht => ?_
  rw [mem_range] at ht
  rw [show r - t = (r - 1 - t) + 1 by omega, pow_succ]
  ring

/-- `Σ_{s ∈ S} a^{#S_{<s}} b^{#S_{>s}} = h_{|S|}(a, b)`. -/
theorem sum_pow_card_lt_gt (a b : R) (S : Finset (Fin n)) :
    ∑ s ∈ S, a ^ (S.filter (· < s)).card * b ^ (S.filter (s < ·)).card = hq a b S.card := by
  induction S using Finset.induction_on_max with
  | h0 => simp [hq]
  | step m T hlt ih =>
    have hmT : m ∉ T := fun h => lt_irrefl m (hlt m h)
    rw [sum_insert hmT, card_insert_of_notMem hmT, hq_succ]
    have h1 : ((insert m T).filter (· < m)).card = T.card := by
      rw [filter_insert, if_neg (lt_irrefl m)]
      congr 1
      exact filter_true_of_mem fun t ht => hlt t ht
    have h2 : ((insert m T).filter (m < ·)).card = 0 := by
      rw [card_eq_zero, filter_eq_empty_iff]
      intro t ht
      rcases mem_insert.1 ht with rfl | ht
      · exact lt_irrefl _
      · exact not_lt.2 (le_of_lt (hlt t ht))
    rw [h1, h2, pow_zero, mul_one, ← ih, mul_sum]
    congr 1
    refine sum_congr rfl fun s hs => ?_
    have h3 : ((insert m T).filter (· < s)).card = (T.filter (· < s)).card := by
      rw [filter_insert, if_neg (not_lt.2 (le_of_lt (hlt s hs)))]
    have h4 : ((insert m T).filter (s < ·)).card = (T.filter (s < ·)).card + 1 := by
      rw [filter_insert, if_pos (hlt s hs), card_insert_of_notMem]
      simp [hmT]
    rw [h3, h4, pow_succ]
    ring

/-! ### The weight identity -/

/-- The tail weight of moving site `s` out of `c[S'∖s]`. -/
theorem tail_updS_erase (y : Fin d) (w : Fin d → R) (c : Fin n → Fin d) (S' : Finset (Fin n))
    (s : Fin n) :
    ∏ k ∈ Ioi s, w (updS y c (S'.erase s) k)
      = w y ^ (S'.filter (s < ·)).card * ∏ k ∈ (Ioi s).filter (fun k => k ∉ S'), w (c k) := by
  classical
  rw [← prod_filter_mul_prod_filter_not (Ioi s) (fun k => k ∈ S')]
  congr 1
  · rw [prod_congr rfl (g := fun _ => w y), prod_const]
    · congr 1
      congr 1
      ext k; simp [and_comm]
    · intro k hk
      simp only [mem_filter, mem_Ioi] at hk
      simp [updS, hk.2, ne_of_gt hk.1]
  · refine prod_congr rfl fun k hk => ?_
    simp only [mem_filter] at hk
    simp [updS, hk.2]

theorem theta_erase (x : Fin d) (w : Fin d → R) (c : Fin n → Fin d) {S' : Finset (Fin n)}
    (hS : ∀ t ∈ S', c t = x) {s : Fin n} (hs : s ∈ S') :
    theta w c (S'.erase s)
      = w x ^ (S'.filter (· < s)).card *
          ∏ s' ∈ S'.erase s, ∏ k ∈ (Ioi s').filter (fun k => k ∉ S'), w (c k) := by
  classical
  unfold theta
  have hin : ∀ s' ∈ S'.erase s, ∏ k ∈ (Ioi s').filter (fun k => k ∉ S'.erase s), w (c k)
      = (if s' < s then w x else 1) * ∏ k ∈ (Ioi s').filter (fun k => k ∉ S'), w (c k) := by
    intro s' hs'
    by_cases hlt : s' < s
    · rw [if_pos hlt]
      have : (Ioi s').filter (fun k => k ∉ S'.erase s)
          = insert s ((Ioi s').filter (fun k => k ∉ S')) := by
        ext k
        simp only [mem_filter, mem_Ioi, mem_erase, mem_insert, not_and, ne_eq]
        constructor
        · rintro ⟨h1, h2⟩
          by_cases hk : k = s
          · exact Or.inl hk
          · exact Or.inr ⟨h1, fun h => h2 hk h⟩
        · rintro (rfl | ⟨h1, h2⟩)
          · exact ⟨hlt, fun h => absurd rfl h⟩
          · exact ⟨h1, fun _ h => h2 h⟩
      rw [this, prod_insert (by simp [hs]), hS s hs]
    · rw [if_neg hlt, one_mul]
      refine prod_congr ?_ fun _ _ => rfl
      ext k
      simp only [mem_filter, mem_Ioi, mem_erase, not_and, ne_eq]
      constructor
      · rintro ⟨h1, h2⟩
        refine ⟨h1, fun h => h2 ?_ h⟩
        rintro rfl; exact hlt h1
      · rintro ⟨h1, h2⟩; exact ⟨h1, fun _ h => h2 h⟩
  rw [prod_congr rfl hin, prod_mul_distrib, prod_ite, prod_const_one, mul_one, prod_const]
  congr 3
  ext t; simp only [mem_filter, mem_erase]
  constructor
  · rintro ⟨⟨_, h⟩, h'⟩; exact ⟨h, h'⟩
  · rintro ⟨h, h'⟩; exact ⟨⟨ne_of_lt h', h⟩, h'⟩

theorem theta_mul_tail (x y : Fin d) (w : Fin d → R) (c : Fin n → Fin d)
    {S' : Finset (Fin n)} (hS : ∀ t ∈ S', c t = x) {s : Fin n} (hs : s ∈ S') :
    theta w c (S'.erase s) * ∏ k ∈ Ioi s, w (updS y c (S'.erase s) k)
      = theta w c S' * (w x ^ (S'.filter (· < s)).card * w y ^ (S'.filter (s < ·)).card) := by
  rw [theta_erase x w c hS hs, tail_updS_erase, theta, ← mul_prod_erase S' _ hs]
  ring

/-! ### The closed form -/

/-- Sites carrying the letter `x`. -/
def sitesOf (c : Fin n → Fin d) (x : Fin d) : Finset (Fin n) := univ.filter (fun k => c k = x)

theorem updS_insert (y : Fin d) (c : Fin n → Fin d) (S : Finset (Fin n)) (s : Fin n) :
    Function.update (updS y c S) s y = updS y c (insert s S) := by
  funext k
  by_cases hk : k = s
  · subst hk; simp [updS]
  · rw [Function.update_of_ne hk]; simp [updS, hk]

/-- Regrouping `(S, s) ↦ insert s S`. -/
theorem sum_powersetCard_sum_sdiff {M : Type*} [AddCommMonoid M] (I : Finset (Fin n)) (k : ℕ)
    (f : Finset (Fin n) → Fin n → M) :
    ∑ S ∈ I.powersetCard k, ∑ s ∈ I \ S, f S s
      = ∑ S' ∈ I.powersetCard (k + 1), ∑ s ∈ S', f (S'.erase s) s := by
  classical
  rw [sum_sigma', sum_sigma']
  refine sum_nbij' (fun p => ⟨insert p.2 p.1, p.2⟩) (fun p => ⟨p.1.erase p.2, p.2⟩)
    ?_ ?_ ?_ ?_ ?_
  · rintro ⟨S, s⟩ h
    simp only [mem_sigma, mem_powersetCard, mem_sdiff] at h ⊢
    refine ⟨⟨insert_subset h.2.1 h.1.1, ?_⟩, mem_insert_self _ _⟩
    rw [card_insert_of_notMem h.2.2, h.1.2]
  · rintro ⟨S, s⟩ h
    simp only [mem_sigma, mem_powersetCard, mem_sdiff] at h ⊢
    refine ⟨⟨(erase_subset _ _).trans h.1.1, ?_⟩, h.1.1 h.2, notMem_erase _ _⟩
    rw [card_erase_of_mem h.2, h.1.2, Nat.add_sub_cancel]
  · rintro ⟨S, s⟩ h
    simp only [mem_sigma, mem_sdiff] at h
    simp [erase_insert h.2.2]
  · rintro ⟨S, s⟩ h
    simp only [mem_sigma] at h
    simp [insert_erase h.2]
  · rintro ⟨S, s⟩ h
    simp only [mem_sigma, mem_sdiff] at h
    simp [erase_insert h.2.2]

/-- **Closed form for `M^k e_c`.** -/
theorem move_pow_mulVec (x y : Fin d) (hxy : x ≠ y) (w : Fin d → R) (c : Fin n → Fin d)
    (k : ℕ) :
    (move x y w) ^ k *ᵥ bv c
      = gq (w x) (w y) k • ∑ S ∈ (sitesOf c x).powersetCard k,
          theta w c S • bv (updS y c S) := by
  classical
  induction k with
  | zero =>
    have : updS y c ∅ = c := by funext k; simp [updS]
    simp only [pow_zero, one_mulVec, gq, range_zero, prod_empty, one_smul,
      powersetCard_zero, sum_singleton, theta, this]
  | succ k ih =>
    rw [pow_succ', ← mulVec_mulVec, ih, mulVec_smul, mulVec_sum]
    simp_rw [mulVec_smul, move_mulVec_single, smul_sum, smul_smul]
    -- the sites of `c[S]` carrying `x` are `sitesOf c x ∖ S`
    have hsites : ∀ S ∈ (sitesOf c x).powersetCard k,
        univ.filter (fun s => updS y c S s = x) = sitesOf c x \ S := by
      intro S hS
      ext s
      simp only [mem_filter, mem_univ, true_and, mem_sdiff, sitesOf, updS]
      by_cases hs : s ∈ S
      · simp [hs, Ne.symm hxy]
      · simp [hs]
    rw [sum_congr rfl fun S hS => by rw [hsites S hS]]
    simp_rw [updS_insert]
    rw [sum_powersetCard_sum_sdiff (sitesOf c x) k
      (fun S s => (gq (w x) (w y) k * (theta w c S * ∏ k ∈ Ioi s, w (updS y c S k))) •
        bv (updS y c (insert s S)))]
    refine sum_congr rfl fun S' hS' => ?_
    have hsub : ∀ t ∈ S', c t = x := fun t ht => by
      have := (mem_powersetCard.1 hS').1 ht
      simpa [sitesOf] using this
    have hcard : S'.card = k + 1 := (mem_powersetCard.1 hS').2
    rw [sum_congr rfl fun s hs => by
      rw [theta_mul_tail x y w c hsub hs, insert_erase hs]]
    rw [← sum_smul, ← mul_sum, ← mul_sum, sum_pow_card_lt_gt, hcard]
    congr 1
    unfold gq
    rw [prod_range_succ]
    ring

end QOU.SchurWeyl.QSchurMoves
