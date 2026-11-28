import QOU.MassTheory.BetaBranching

/-!
# Jucys–Murphy class sums by the up-down recursion

Partitions `λ ⊢ n` are beta-sets with `L > n` beads (`parts L n`), weighted by
`w = 1 / ∏ hooks`, so `f^λ = n! · w`. Adding a box at bead `b` adds the content
`b - ℓ + 1`; removing one at `b` removes `b - ℓ`.

The branching rules of `BetaBranching` give the master recursion
`(n+1) W_{n+1}[F] = ∑_{μ ⊢ n} w(μ) ∑_{□ addable} F(μ + □)`. For `F` a quartic in the added
content, the addable sum is the removable sum plus the interlacing moments (`stepA`), and the
removable sum at the next size is the up measure (`stepB`). This closes on the five sums
`∑ f^λ`, `∑ f^λ p₂`, `∑ f^λ p₁²`, `∑ f^λ p₄`, `∑ f^λ p₂²`, which are given in closed form in
the involution numbers `I_n` (`jm_class_sums`). These are the class-sum inputs of the `q = 1`
expansion in `computations/cyclotomic_boundary_q1_expansion.py` (`CLASS_SUMS`).
-/

namespace QOU.Mass.JMClassSums
open Finset QOU.Mass.DividedDifference QOU.Mass.HookContentBeta QOU.Mass.UpDownMoments
  QOU.Mass.BetaBranching

/-- `W L n F = ∑_{λ ⊢ n, ℓ(λ) ≤ L} F(λ) / ∏ hooks`. -/
def W (L n : ℕ) (F : Finset ℕ → ℚ) : ℚ := ∑ B ∈ parts L n, w B * F B

lemma sum_wUp_addable' (B : Finset ℕ) (φ : ℕ → ℚ) :
    ∑ b ∈ B, wUp (cS B) b * φ b = ∑ b ∈ addable B, wUp (cS B) b * φ b := by
  unfold addable
  rw [← sum_filter_add_sum_filter_not B (fun b => b + 1 ∉ B), add_eq_left]
  refine sum_eq_zero (fun b hb => ?_)
  rw [mem_filter, not_not] at hb
  have : ((b : ℚ) + 1) ∈ cS B := mem_image.mpr ⟨b + 1, hb.2, by push_cast; rfl⟩
  rw [wUp_eq_zero _ this, zero_mul]

lemma card_of_parts {L n : ℕ} {B : Finset ℕ} (hB : B ∈ parts L n) : B.card = L :=
  (mem_parts.mp hB).1

lemma size_of_parts {L n : ℕ} {B : Finset ℕ} (hB : B ∈ parts L n) : size B = n :=
  (mem_parts.mp hB).2

/-- **Master recursion.** `(n+1) W_{n+1}[F] = ∑_{μ ⊢ n} w(μ) ∑_{□ addable} F(μ + □)`. -/
theorem master (L n : ℕ) (hL : 0 < L) (F : Finset ℕ → ℚ) :
    ((n : ℚ) + 1) * W L (n + 1) F
      = ∑ μ ∈ parts L n, w μ * ∑ a ∈ addable μ, F (mv μ a (a + 1)) := by
  simp_rw [mul_sum]
  rw [sum_addable_eq_sum_removable L n (fun μ a => w μ * F (mv μ a (a + 1))), W, mul_sum]
  refine sum_congr rfl (fun B hB => ?_)
  have hne : B.Nonempty := by
    rw [← card_pos, card_of_parts hB]; exact hL
  have h := sum_removable_w B hne
  rw [size_of_parts hB] at h
  push_cast at h
  calc ((n : ℚ) + 1) * (w B * F B) = (w B * ((n : ℚ) + 1)) * F B := by ring
    _ = (∑ b ∈ removable B, w (mv B b (b - 1))) * F B := by rw [h]
    _ = ∑ b ∈ removable B, w (mv B b (b - 1)) * F (mv (mv B b (b - 1)) (b - 1) (b - 1 + 1)) := by
        rw [sum_mul]; refine sum_congr rfl (fun b hb => ?_)
        rw [removable, mem_filter] at hb
        rw [Nat.sub_add_cancel hb.2.1, mv_mv hb.1 hb.2.2]

/-- **Removal sums via the up measure.** -/
theorem remSum (L n : ℕ) (G : Finset ℕ → ℚ) (φ : ℚ → ℚ) :
    ∑ μ ∈ parts L (n + 1), w μ * (G μ * ∑ r ∈ removable μ, φ ((r : ℚ) - μ.card))
      = ∑ ν ∈ parts L n, w ν * ∑ b ∈ ν, wUp (cS ν) b
          * (G (mv ν b (b + 1)) * φ ((b : ℚ) - ν.card + 1)) := by
  have hR : ∀ ν ∈ parts L n, w ν * ∑ b ∈ ν, wUp (cS ν) b
          * (G (mv ν b (b + 1)) * φ ((b : ℚ) - ν.card + 1))
        = ∑ b ∈ addable ν, w (mv ν b (b + 1)) * (G (mv ν b (b + 1)) * φ ((b : ℚ) - ν.card + 1)) := by
    intro ν _
    rw [sum_wUp_addable' ν (fun b => G (mv ν b (b + 1)) * φ ((b : ℚ) - ν.card + 1)), mul_sum]
    refine sum_congr rfl (fun b hb => ?_)
    rw [addable, mem_filter] at hb
    rw [mv, w_up hb.1 hb.2]; ring
  rw [sum_congr rfl hR, sum_addable_eq_sum_removable L n
    (fun ν b => w (mv ν b (b + 1)) * (G (mv ν b (b + 1)) * φ ((b : ℚ) - ν.card + 1)))]
  refine sum_congr rfl (fun μ _ => ?_)
  rw [mul_sum, mul_sum]
  refine sum_congr rfl (fun r hr => ?_)
  rw [removable, mem_filter] at hr
  rw [Nat.sub_add_cancel hr.2.1, mv_mv hr.1 hr.2.2, card_mv hr.1 hr.2.2, Nat.cast_sub hr.2.1]
  push_cast; ring_nf

lemma removable_empty_of_size_zero {B : Finset ℕ} (hs : size B = 0) : removable B = ∅ := by
  ext b
  simp only [removable, mem_filter, notMem_empty, iff_false, not_and]
  intro hb h1 hb1
  have hsub : B.filter (· < b) ⊆ (range b).erase (b - 1) := by
    intro c hc; rw [mem_filter] at hc
    exact mem_erase.mpr ⟨fun e => hb1 (e ▸ hc.1), mem_range.mpr hc.2⟩
  have := card_le_card hsub
  rw [card_erase_of_mem (mem_range.mpr (by omega)), card_range] at this
  have hlo : lo B b + 1 ≤ b := by unfold lo; omega
  have h2 := term_le_size B hb
  rw [hs] at h2
  have : ((lo B b : ℕ) : ℚ) + 1 ≤ b := by exact_mod_cast hlo
  linarith

/-- General form of `remSum`. -/
theorem remSum' (L n : ℕ) (φ : Finset ℕ → ℚ → ℚ) :
    ∑ μ ∈ parts L (n + 1), w μ * ∑ r ∈ removable μ, φ μ ((r : ℚ) - μ.card)
      = ∑ ν ∈ parts L n, w ν * ∑ b ∈ ν, wUp (cS ν) b * φ (mv ν b (b + 1)) ((b : ℚ) - ν.card + 1) := by
  have hR : ∀ ν ∈ parts L n, w ν * ∑ b ∈ ν, wUp (cS ν) b * φ (mv ν b (b + 1)) ((b : ℚ) - ν.card + 1)
        = ∑ b ∈ addable ν, w (mv ν b (b + 1)) * φ (mv ν b (b + 1)) ((b : ℚ) - ν.card + 1) := by
    intro ν _
    rw [sum_wUp_addable' ν (fun b => φ (mv ν b (b + 1)) ((b : ℚ) - ν.card + 1)), mul_sum]
    refine sum_congr rfl (fun b hb => ?_)
    rw [addable, mem_filter] at hb
    rw [mv, w_up hb.1 hb.2]; ring
  rw [sum_congr rfl hR, sum_addable_eq_sum_removable L n
    (fun ν b => w (mv ν b (b + 1)) * φ (mv ν b (b + 1)) ((b : ℚ) - ν.card + 1))]
  refine sum_congr rfl (fun μ _ => ?_)
  rw [mul_sum]
  refine sum_congr rfl (fun r hr => ?_)
  rw [removable, mem_filter] at hr
  rw [Nat.sub_add_cancel hr.2.1, mv_mv hr.1 hr.2.2, card_mv hr.1 hr.2.2, Nat.cast_sub hr.2.1]
  push_cast; ring_nf

/-- A quartic in the content. -/
def quart (a0 a1 a2 a3 a4 c : ℚ) : ℚ := a0 + a1 * c + a2 * c ^ 2 + a3 * c ^ 3 + a4 * c ^ 4

/-- Up measure against a quartic. -/
lemma upPoly (B : Finset ℕ) (h0 : 0 ∈ B) (a0 a1 a2 a3 a4 : ℚ) :
    ∑ b ∈ B, wUp (cS B) b * quart a0 a1 a2 a3 a4 ((b : ℚ) - B.card + 1)
      = a0 + a2 * size B + a3 * (2 * contentPow 1 B)
        + a4 * (size B ^ 2 / 2 + size B / 2 + 3 * contentPow 2 B) := by
  obtain ⟨m0, m1, m2, m3, m4⟩ := up_moments B h0
  have e : ∀ b ∈ B, wUp (cS B) b * quart a0 a1 a2 a3 a4 ((b : ℚ) - B.card + 1)
      = a0 * wUp (cS B) b + a1 * (wUp (cS B) b * ((b : ℚ) - B.card + 1))
        + a2 * (wUp (cS B) b * ((b : ℚ) - B.card + 1) ^ 2)
        + a3 * (wUp (cS B) b * ((b : ℚ) - B.card + 1) ^ 3)
        + a4 * (wUp (cS B) b * ((b : ℚ) - B.card + 1) ^ 4) := by
    intro b _; unfold quart; ring
  rw [sum_congr rfl e]
  simp only [sum_add_distrib, ← mul_sum]
  rw [m0, m1, m2, m3, m4]; ring

/-- Addable boxes against a quartic: removable boxes plus the interlacing moments. -/
lemma addPoly (B : Finset ℕ) (h0 : 0 ∈ B) (a0 a1 a2 a3 a4 : ℚ) :
    ∑ a ∈ addable B, quart a0 a1 a2 a3 a4 ((a : ℚ) - B.card + 1)
      = ∑ r ∈ removable B, quart a0 a1 a2 a3 a4 ((r : ℚ) - B.card)
        + (a0 + a2 * (2 * size B) + a3 * (6 * contentPow 1 B)
          + a4 * (2 * size B + 12 * contentPow 2 B)) := by
  obtain ⟨t0, t1, t2, t3, t4⟩ := interlace_moments B h0
  simp only [quart, sum_add_distrib, ← mul_sum, sum_const, nsmul_eq_mul, mul_one] at *
  linear_combination a0 * t0 + a1 * t1 + a2 * t2 + a3 * t3 + a4 * t4

variable (α0 α1 α2 α3 α4 β0 β1 β2 β3 β4 : Finset ℕ → ℚ)

/-- The quartic attached to coefficient functions at `B`. -/
def qa (α0 α1 α2 α3 α4 : Finset ℕ → ℚ) (B : Finset ℕ) (c : ℚ) : ℚ :=
  quart (α0 B) (α1 B) (α2 B) (α3 B) (α4 B) c

/-- The interlacing part `A F`. -/
def Aop (α0 _α1 α2 α3 α4 : Finset ℕ → ℚ) (B : Finset ℕ) : ℚ :=
  α0 B + α2 B * (2 * size B) + α3 B * (6 * contentPow 1 B) + α4 B * (2 * size B + 12 * contentPow 2 B)

/-- The up-measure part `B F`. -/
def Bop (β0 _β1 β2 β3 β4 : Finset ℕ → ℚ) (B : Finset ℕ) : ℚ :=
  β0 B + β2 B * size B + β3 B * (2 * contentPow 1 B)
    + β4 B * (size B ^ 2 / 2 + size B / 2 + 3 * contentPow 2 B)

/-- Removal remainder. -/
def Rem (α0 α1 α2 α3 α4 : Finset ℕ → ℚ) (L n : ℕ) : ℚ := ∑ μ ∈ parts L n, w μ * ∑ r ∈ removable μ, qa α0 α1 α2 α3 α4 μ ((r : ℚ) - μ.card)

theorem stepA (L n : ℕ) (hL : n < L) (F : Finset ℕ → ℚ)
    (hF : ∀ μ ∈ parts L n, ∀ a ∈ addable μ,
      F (mv μ a (a + 1)) = qa α0 α1 α2 α3 α4 μ ((a : ℚ) - μ.card + 1)) :
    ((n : ℚ) + 1) * W L (n + 1) F = W L n (Aop α0 α1 α2 α3 α4) + Rem α0 α1 α2 α3 α4 L n := by
  rw [master L n (by omega), W, Rem, ← sum_add_distrib]
  refine sum_congr rfl (fun μ hμ => ?_)
  have h0 := zero_mem_of_parts hμ hL
  rw [sum_congr rfl (hF μ hμ)]
  simp only [qa]
  rw [addPoly μ h0, Aop]; ring

theorem stepB (L n : ℕ) (hL : n < L)
    (h : ∀ ν ∈ parts L n, ∀ b ∈ addable ν,
      qa α0 α1 α2 α3 α4 (mv ν b (b + 1)) ((b : ℚ) - ν.card + 1)
        = qa β0 β1 β2 β3 β4 ν ((b : ℚ) - ν.card + 1)) :
    Rem α0 α1 α2 α3 α4 L (n + 1) = W L n (Bop β0 β1 β2 β3 β4) := by
  rw [Rem, remSum' L n (fun μ c => qa α0 α1 α2 α3 α4 μ c), W]
  refine sum_congr rfl (fun ν hν => ?_)
  have h0 := zero_mem_of_parts hν hL
  congr 1
  rw [sum_wUp_addable' ν (fun b => qa α0 α1 α2 α3 α4 (mv ν b (b + 1)) ((b : ℚ) - ν.card + 1)),
    sum_congr rfl (fun b hb => by rw [h ν hν b hb]),
    ← sum_wUp_addable' ν (fun b => qa β0 β1 β2 β3 β4 ν ((b : ℚ) - ν.card + 1))]
  simp only [qa]
  rw [upPoly ν h0, Bop]

theorem rem_zero (L : ℕ) : Rem α0 α1 α2 α3 α4 L 0 = 0 := by
  unfold Rem
  refine sum_eq_zero (fun μ hμ => ?_)
  rw [removable_empty_of_size_zero (by rw [size_of_parts hμ]; norm_num), sum_empty, mul_zero]


/-! ### Base case and linearity -/

lemma lo_eq_of_size_zero {B : Finset ℕ} (hs : size B = 0) {b : ℕ} (hb : b ∈ B) : lo B b = b := by
  have hnn : ∀ x ∈ B, (0 : ℚ) ≤ (x : ℚ) - lo B x := fun x _ => by
    have : ((lo B x : ℕ) : ℚ) ≤ x := by exact_mod_cast lo_le B x
    linarith
  unfold size at hs
  have := (sum_eq_zero_iff_of_nonneg hnn).mp hs b hb
  have : ((lo B b : ℕ) : ℚ) = b := by linarith
  exact_mod_cast this

lemma contentPow_of_size_zero (k : ℕ) {B : Finset ℕ} (hs : size B = 0) : contentPow k B = 0 := by
  unfold contentPow
  refine sum_eq_zero (fun b hb => ?_)
  rw [lo_eq_of_size_zero hs hb, Nat.sub_self, range_zero, sum_empty]

lemma lo_range {L b : ℕ} (hb : b < L) : lo (range L) b = b := by
  unfold lo
  have : (range L).filter (· < b) = range b := by
    ext x; simp only [mem_filter, mem_range]; constructor
    · exact fun h => h.2
    · intro h; exact ⟨by omega, h⟩
  rw [this, card_range]

lemma parts_zero (L : ℕ) : parts L 0 = {range L} := by
  ext B; rw [mem_parts, mem_singleton]; constructor
  · rintro ⟨hc, hs⟩
    refine eq_of_subset_of_card_le (fun b hb => mem_range.mpr ?_) (by rw [hc, card_range])
    have := lt_of_size hs hb; rw [hc] at this; omega
  · rintro rfl
    refine ⟨card_range L, ?_⟩
    unfold size
    refine sum_eq_zero (fun b hb => ?_)
    rw [lo_range (mem_range.mp hb)]; ring

lemma w_range (L : ℕ) : w (range L) = 1 := by
  rw [w_eq_inv_hookProd, hookProd, prod_eq_one (fun b hb => ?_), inv_one]
  rw [filter_eq_empty_iff.mpr (fun g hg => ?_), prod_empty]
  rw [mem_range] at hb hg
  exact not_not.mpr (mem_range.mpr (by omega))

lemma W_zero (L : ℕ) (F : Finset ℕ → ℚ) : W L 0 F = F (range L) := by
  rw [W, parts_zero, sum_singleton, w_range, one_mul]

lemma W_congr {L n : ℕ} {F G : Finset ℕ → ℚ} (h : ∀ B ∈ parts L n, F B = G B) :
    W L n F = W L n G := sum_congr rfl (fun B hB => by rw [h B hB])

/-- The five Jucys–Murphy class sums, as weighted sums over beta-sets. -/
def S0 (L n : ℕ) : ℚ := W L n (fun _ => 1)
def S2 (L n : ℕ) : ℚ := W L n (contentPow 2)
def S11 (L n : ℕ) : ℚ := W L n (fun B => contentPow 1 B ^ 2)
def S4 (L n : ℕ) : ℚ := W L n (contentPow 4)
def S22 (L n : ℕ) : ℚ := W L n (fun B => contentPow 2 B ^ 2)

lemma W_comb (L n : ℕ) (a0 a2 a11 a4 a22 : ℚ) :
    W L n (fun B => a0 + a2 * contentPow 2 B + a11 * contentPow 1 B ^ 2 + a4 * contentPow 4 B
      + a22 * contentPow 2 B ^ 2)
      = a0 * S0 L n + a2 * S2 L n + a11 * S11 L n + a4 * S4 L n + a22 * S22 L n := by
  simp only [S0, S2, S11, S4, S22, W, mul_sum, ← sum_add_distrib]
  exact sum_congr rfl (fun B _ => by ring)

/-- Two steps of the recursion, combined. -/
theorem step2 (L n : ℕ) (hn : n + 1 < L) (F α0 α1 α2 α3 α4 β0 β1 β2 β3 β4 : Finset ℕ → ℚ)
    (hF : ∀ μ ∈ parts L (n + 1), ∀ a ∈ addable μ,
      F (mv μ a (a + 1)) = qa α0 α1 α2 α3 α4 μ ((a : ℚ) - μ.card + 1))
    (h : ∀ ν ∈ parts L n, ∀ b ∈ addable ν,
      qa α0 α1 α2 α3 α4 (mv ν b (b + 1)) ((b : ℚ) - ν.card + 1)
        = qa β0 β1 β2 β3 β4 ν ((b : ℚ) - ν.card + 1)) :
    ((n : ℚ) + 2) * W L (n + 2) F
      = W L (n + 1) (Aop α0 α1 α2 α3 α4) + W L n (Bop β0 β1 β2 β3 β4) := by
  have hA := stepA α0 α1 α2 α3 α4 L (n + 1) (by omega) F hF
  rw [stepB α0 α1 α2 α3 α4 β0 β1 β2 β3 β4 L n (by omega) h] at hA
  push_cast at hA
  rw [show (n : ℚ) + 2 = n + 1 + 1 by ring]; exact hA

theorem step1 (L : ℕ) (hL : 0 < L) (F α0 α1 α2 α3 α4 : Finset ℕ → ℚ)
    (hF : ∀ μ ∈ parts L 0, ∀ a ∈ addable μ,
      F (mv μ a (a + 1)) = qa α0 α1 α2 α3 α4 μ ((a : ℚ) - μ.card + 1)) :
    W L 1 F = W L 0 (Aop α0 α1 α2 α3 α4) := by
  have hA := stepA α0 α1 α2 α3 α4 L 0 hL F hF
  rw [rem_zero, add_zero] at hA
  simpa using hA


/-! ### The five recursions -/

theorem stepS (L n : ℕ) (hn : n + 1 < L) (F α0 α1 α2 α3 α4 β0 β1 β2 β3 β4 : Finset ℕ → ℚ)
    (hF : ∀ μ ∈ parts L (n + 1), ∀ a ∈ addable μ,
      F (mv μ a (a + 1)) = qa α0 α1 α2 α3 α4 μ ((a : ℚ) - μ.card + 1))
    (h : ∀ ν ∈ parts L n, ∀ b ∈ addable ν,
      qa α0 α1 α2 α3 α4 (mv ν b (b + 1)) ((b : ℚ) - ν.card + 1)
        = qa β0 β1 β2 β3 β4 ν ((b : ℚ) - ν.card + 1))
    (a0 a2 a11 a4 a22 b0 b2 b11 b4 b22 : ℚ)
    (hA : ∀ B ∈ parts L (n + 1), Aop α0 α1 α2 α3 α4 B = a0 + a2 * contentPow 2 B
      + a11 * contentPow 1 B ^ 2 + a4 * contentPow 4 B + a22 * contentPow 2 B ^ 2)
    (hB : ∀ B ∈ parts L n, Bop β0 β1 β2 β3 β4 B = b0 + b2 * contentPow 2 B
      + b11 * contentPow 1 B ^ 2 + b4 * contentPow 4 B + b22 * contentPow 2 B ^ 2) :
    ((n : ℚ) + 2) * W L (n + 2) F
      = (a0 * S0 L (n + 1) + a2 * S2 L (n + 1) + a11 * S11 L (n + 1) + a4 * S4 L (n + 1)
          + a22 * S22 L (n + 1))
        + (b0 * S0 L n + b2 * S2 L n + b11 * S11 L n + b4 * S4 L n + b22 * S22 L n) := by
  rw [step2 L n hn F α0 α1 α2 α3 α4 β0 β1 β2 β3 β4 hF h, W_congr hA, W_congr hB, W_comb, W_comb]

/-- Rewrites a test function by the moves of `contentPow`. -/
macro "mvtac" : tactic => `(tactic| (
  intro μ _ a ha
  rw [addable, mem_filter] at ha
  simp only [qa, quart, contentPow_up 1 (by norm_num) ha.1 ha.2,
    contentPow_up 2 (by norm_num) ha.1 ha.2, contentPow_up 4 (by norm_num) ha.1 ha.2]
  try ring))

macro "lintac" : tactic => `(tactic| (
  intro B hB
  simp only [Aop, Bop, size_of_parts hB]
  try push_cast
  try ring))

theorem rec0 (L n : ℕ) (hn : n + 1 < L) :
    ((n : ℚ) + 2) * S0 L (n + 2) = S0 L (n + 1) + S0 L n := by
  have := stepS L n hn (fun _ => 1) (fun _ => 1) (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => 0)
    (fun _ => 1) (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => 0) (by mvtac) (by mvtac)
    1 0 0 0 0 1 0 0 0 0 (by lintac) (by lintac)
  rw [S0]; linarith [this]

theorem recC2 (L n : ℕ) (hn : n + 1 < L) :
    ((n : ℚ) + 2) * S2 L (n + 2) = 2 * (n + 1) * S0 L (n + 1) + S2 L (n + 1)
      + 2 * n * S0 L n + S2 L n := by
  have := stepS L n hn (contentPow 2) (contentPow 2) (fun _ => 0) (fun _ => 1) (fun _ => 0)
    (fun _ => 0) (contentPow 2) (fun _ => 0) (fun _ => 2) (fun _ => 0) (fun _ => 0)
    (by mvtac) (by mvtac) (2 * (n + 1)) 1 0 0 0 (2 * n) 1 0 0 0 (by lintac) (by lintac)
  rw [S2]; linarith [this]

theorem recC11 (L n : ℕ) (hn : n + 1 < L) :
    ((n : ℚ) + 2) * S11 L (n + 2) = 2 * (n + 1) * S0 L (n + 1) + S11 L (n + 1)
      + 4 * n * S0 L n + S11 L n := by
  have := stepS L n hn (fun B => contentPow 1 B ^ 2) (fun B => contentPow 1 B ^ 2)
    (fun B => 2 * contentPow 1 B) (fun _ => 1) (fun _ => 0) (fun _ => 0)
    (fun B => contentPow 1 B ^ 2) (fun B => 4 * contentPow 1 B) (fun _ => 4) (fun _ => 0)
    (fun _ => 0) (by mvtac) (by mvtac) (2 * (n + 1)) 0 1 0 0 (4 * n) 0 1 0 0 (by lintac)
    (by lintac)
  rw [S11]; linarith [this]

theorem recC4 (L n : ℕ) (hn : n + 1 < L) :
    ((n : ℚ) + 2) * S4 L (n + 2) = 2 * (n + 1) * S0 L (n + 1) + 12 * S2 L (n + 1) + S4 L (n + 1)
      + (n ^ 2 + n) * S0 L n + 6 * S2 L n + S4 L n := by
  have := stepS L n hn (contentPow 4) (contentPow 4) (fun _ => 0) (fun _ => 0) (fun _ => 0)
    (fun _ => 1) (contentPow 4) (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => 2)
    (by mvtac) (by mvtac) (2 * (n + 1)) 12 0 1 0 (n ^ 2 + n) 6 0 1 0 (by lintac) (by lintac)
  rw [S4]; linarith [this]

theorem recC22 (L n : ℕ) (hn : n + 1 < L) :
    ((n : ℚ) + 2) * S22 L (n + 2) = 2 * (n + 1) * S0 L (n + 1) + (4 * (n + 1) + 12) * S2 L (n + 1)
      + S22 L (n + 1) + (2 * n ^ 2 + 2 * n) * S0 L n + (4 * n + 12) * S2 L n + S22 L n := by
  have := stepS L n hn (fun B => contentPow 2 B ^ 2) (fun B => contentPow 2 B ^ 2) (fun _ => 0)
    (fun B => 2 * contentPow 2 B) (fun _ => 0) (fun _ => 1) (fun B => contentPow 2 B ^ 2)
    (fun _ => 0) (fun B => 4 * contentPow 2 B) (fun _ => 0) (fun _ => 4)
    (by mvtac) (by mvtac) (2 * (n + 1)) (4 * (n + 1) + 12) 0 0 1 (2 * n ^ 2 + 2 * n) (4 * n + 12)
    0 0 1 (by lintac) (by lintac)
  rw [S22]; linarith [this]


/-! ### Initial values -/

lemma range_mem_parts (L : ℕ) : range L ∈ parts L 0 := by rw [parts_zero]; exact mem_singleton_self _

lemma size_range (L : ℕ) : size (range L) = 0 := by
  have := (mem_parts.mp (range_mem_parts L)).2; simpa using this

lemma cP_range (k L : ℕ) : contentPow k (range L) = 0 := contentPow_of_size_zero k (size_range L)

theorem init0 (L : ℕ) :
    S0 L 0 = 1 ∧ S2 L 0 = 0 ∧ S11 L 0 = 0 ∧ S4 L 0 = 0 ∧ S22 L 0 = 0 := by
  simp only [S0, S2, S11, S4, S22, W_zero, cP_range]; norm_num

theorem init1 (L : ℕ) (hL : 0 < L) :
    S0 L 1 = 1 ∧ S2 L 1 = 0 ∧ S11 L 1 = 0 ∧ S4 L 1 = 0 ∧ S22 L 1 = 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [S0, step1 L hL _ (fun _ => 1) (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => 0) (by mvtac),
      W_zero]; simp [Aop]
  · rw [S2, step1 L hL _ (contentPow 2) (fun _ => 0) (fun _ => 1) (fun _ => 0) (fun _ => 0)
      (by mvtac), W_zero]; simp [Aop, cP_range, size_range]
  · rw [S11, step1 L hL _ (fun B => contentPow 1 B ^ 2) (fun B => 2 * contentPow 1 B) (fun _ => 1)
      (fun _ => 0) (fun _ => 0) (by mvtac), W_zero]; simp [Aop, cP_range, size_range]
  · rw [S4, step1 L hL _ (contentPow 4) (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => 1)
      (by mvtac), W_zero]; simp [Aop, cP_range, size_range]
  · rw [S22, step1 L hL _ (fun B => contentPow 2 B ^ 2) (fun _ => 0) (fun B => 2 * contentPow 2 B)
      (fun _ => 0) (fun _ => 1) (by mvtac), W_zero]; simp [Aop, cP_range, size_range]


/-! ### Closed forms in involution numbers -/

/-- Involution numbers: `I 0 = I 1 = 1`, `I (n+2) = I (n+1) + (n+1) I n`. -/
def I : ℕ → ℚ
  | 0 => 1
  | 1 => 1
  | n + 2 => I (n + 1) + (n + 1) * I n

lemma I_ss (n : ℕ) : I (n + 2) = I (n + 1) + (n + 1) * I n := rfl

def g2 (n : ℕ) : ℚ := (n : ℚ) * (n - 1) / 2 * I n + (n : ℚ) * (n - 1) * (n - 2) / 3 * I (n - 3)

def g11 (n : ℕ) : ℚ := (n : ℚ) * (n - 1) / 2 * I n + (n : ℚ) * (n - 1) * (n - 2) * I (n - 3)
  + (n : ℚ) * (n - 1) * (n - 2) * (n - 3) / 2 * I (n - 4)

def g4 (n : ℕ) : ℚ := (n : ℚ) * (n - 1) * (4 * n - 5) / 6 * I n
  + (n : ℚ) * (n - 1) * (n - 2) * (3 * n - 4) / 3 * I (n - 3)
  + (n : ℚ) * (n - 1) * (n - 2) * (n - 3) * I (n - 4)
  + (n : ℚ) * (n - 1) * (n - 2) * (n - 3) * (n - 4) / 5 * I (n - 5)

def g22 (n : ℕ) : ℚ := (n : ℚ) * (n - 1) * (3 * n ^ 2 + n - 8) / 12 * I n
  + (n : ℚ) * (n - 1) * (n - 2) * (n - 2) * (n + 4) / 3 * I (n - 3)
  + 2 * ((n : ℚ) * (n - 1) * (n - 2) * (n - 3)) * I (n - 4)
  + (n : ℚ) * (n - 1) * (n - 2) * (n - 3) * (n - 4) * I (n - 5)
  + 4 * ((n : ℚ) * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5)) / 9 * I (n - 6)

macro "cftac" : tactic => `(tactic| (
  intro n
  rcases Nat.lt_or_ge n 6 with hn | hn
  · interval_cases n <;> norm_num [g2, g11, g4, g22, I]
  · obtain ⟨m, hm⟩ : ∃ m, n = m + 6 := ⟨n - 6, by omega⟩
    subst hm
    simp only [g2, g11, g4, g22, show m + 6 + 2 - 3 = m + 5 by omega,
      show m + 6 + 2 - 4 = m + 4 by omega, show m + 6 + 2 - 5 = m + 3 by omega,
      show m + 6 + 2 - 6 = m + 2 by omega, show m + 6 + 1 - 3 = m + 4 by omega,
      show m + 6 + 1 - 4 = m + 3 by omega, show m + 6 + 1 - 5 = m + 2 by omega,
      show m + 6 + 1 - 6 = m + 1 by omega, show m + 6 - 3 = m + 3 by omega,
      show m + 6 - 4 = m + 2 by omega, show m + 6 - 5 = m + 1 by omega,
      show m + 6 - 6 = m by omega, I_ss]
    push_cast; ring))

lemma g2_rec : ∀ n : ℕ, g2 (n + 2) = 2 * (n + 1) * I (n + 1) + g2 (n + 1)
    + (n + 1) * (2 * n * I n + g2 n) := by cftac

lemma g11_rec : ∀ n : ℕ, g11 (n + 2) = 2 * (n + 1) * I (n + 1) + g11 (n + 1)
    + (n + 1) * (4 * n * I n + g11 n) := by cftac

lemma g4_rec : ∀ n : ℕ, g4 (n + 2) = 2 * (n + 1) * I (n + 1) + 12 * g2 (n + 1) + g4 (n + 1)
    + (n + 1) * ((n ^ 2 + n) * I n + 6 * g2 n + g4 n) := by cftac

lemma g22_rec : ∀ n : ℕ, g22 (n + 2) = 2 * (n + 1) * I (n + 1) + (4 * (n + 1) + 12) * g2 (n + 1)
    + g22 (n + 1) + (n + 1) * ((2 * n ^ 2 + 2 * n) * I n + (4 * n + 12) * g2 n + g22 n) := by cftac


/-! ### The class sums in closed form -/

/-- `n! · W[F]` for the five Jucys–Murphy class sums, by the up-down recursion. -/
theorem class_sums (L : ℕ) : ∀ n, n < L →
    (n.factorial : ℚ) * S0 L n = I n ∧ (n.factorial : ℚ) * S2 L n = g2 n
      ∧ (n.factorial : ℚ) * S11 L n = g11 n ∧ (n.factorial : ℚ) * S4 L n = g4 n
      ∧ (n.factorial : ℚ) * S22 L n = g22 n := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    match n with
    | 0 =>
      intro _
      obtain ⟨a, b, c, d, e⟩ := init0 L
      rw [a, b, c, d, e]; norm_num [g2, g11, g4, g22, I]
    | 1 =>
      intro hL
      obtain ⟨a, b, c, d, e⟩ := init1 L (by omega)
      rw [a, b, c, d, e]; norm_num [g2, g11, g4, g22, I]
    | m + 2 =>
      intro hL
      obtain ⟨e00, e20, e110, e40, e220⟩ := ih m (by omega) (by omega)
      obtain ⟨e01, e21, e111, e41, e221⟩ := ih (m + 1) (by omega) (by omega)
      have r0 := rec0 L m (by omega)
      have r2 := recC2 L m (by omega)
      have r11 := recC11 L m (by omega)
      have r4 := recC4 L m (by omega)
      have r22 := recC22 L m (by omega)
      rw [Nat.factorial_succ] at e01 e21 e111 e41 e221
      rw [Nat.factorial_succ, Nat.factorial_succ]
      push_cast at *
      set a : ℚ := (m.factorial : ℚ)
      refine ⟨?_, ?_, ?_, ?_, ?_⟩
      · linear_combination (m + 1) * a * r0 + e01 + (m + 1) * e00 - I_ss m
      · linear_combination (m + 1) * a * r2 + 2 * (m + 1) * e01 + e21 + 2 * m * (m + 1) * e00
          + (m + 1) * e20 - g2_rec m
      · linear_combination (m + 1) * a * r11 + 2 * (m + 1) * e01 + e111 + 4 * m * (m + 1) * e00
          + (m + 1) * e110 - g11_rec m
      · linear_combination (m + 1) * a * r4 + 2 * (m + 1) * e01 + 12 * e21 + e41
          + (m + 1) * (m ^ 2 + m) * e00 + 6 * (m + 1) * e20 + (m + 1) * e40 - g4_rec m
      · linear_combination (m + 1) * a * r22 + 2 * (m + 1) * e01 + (4 * (m + 1) + 12) * e21 + e221
          + (m + 1) * (2 * m ^ 2 + 2 * m) * e00 + (m + 1) * (4 * m + 12) * e20 + (m + 1) * e220
          - g22_rec m


/-- **Jucys–Murphy class sums.** Over beta-sets with `n + 1` beads (partitions `λ ⊢ n`), with
`f^λ = n! / ∏ hooks` and `p_k(λ) = ∑_{□ ∈ λ} c(□)^k`:
`∑ f^λ = I_n`, `∑ f^λ p₂ = g2 n`, `∑ f^λ p₁² = g11 n`, `∑ f^λ p₄ = g4 n`, `∑ f^λ p₂² = g22 n`. -/
theorem jm_class_sums (n : ℕ) :
    ∑ B ∈ parts (n + 1) n, (n.factorial : ℚ) / hookProd B = I n
      ∧ ∑ B ∈ parts (n + 1) n, (n.factorial : ℚ) / hookProd B * contentPow 2 B = g2 n
      ∧ ∑ B ∈ parts (n + 1) n, (n.factorial : ℚ) / hookProd B * contentPow 1 B ^ 2 = g11 n
      ∧ ∑ B ∈ parts (n + 1) n, (n.factorial : ℚ) / hookProd B * contentPow 4 B = g4 n
      ∧ ∑ B ∈ parts (n + 1) n, (n.factorial : ℚ) / hookProd B * contentPow 2 B ^ 2 = g22 n := by
  obtain ⟨a, b, c, d, e⟩ := class_sums (n + 1) n (by omega)
  simp only [S0, S2, S11, S4, S22, W, mul_sum, w_eq_inv_hookProd] at a b c d e
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [← a]; exact sum_congr rfl (fun B _ => by ring)
  · rw [← b]; exact sum_congr rfl (fun B _ => by ring)
  · rw [← c]; exact sum_congr rfl (fun B _ => by ring)
  · rw [← d]; exact sum_congr rfl (fun B _ => by ring)
  · rw [← e]; exact sum_congr rfl (fun B _ => by ring)

end QOU.Mass.JMClassSums

