/-
  Wiring the dual multiplier to the exceptional divisor.

  `LagrangianCollisionFlow` leaves one gap: no map from the configuration of two
  particles on their exceptional divisors to the multiplier `μ`.  This file
  supplies one and records exactly what it does and does not give.

  Data.  A dual optimum `μ★` of `g(μ) = min_i (c i − μ ⬝ x i)` (a vector, the
  shadow prices of the bond constraint), the spin label `n = 2j`, and the angle
  `γ` between the two coherent directions `u, v ∈ 𝒮_p ≅ S²`.

  * `peakMultiplier μ★ n γ = p_n(γ) • μ★`, with `p_n = cos^{2n}(γ/2)` the
    overlap probability (`EDCoherentLocality.overlap`).  Normalised so that
    the multiplier at coincidence is `μ★`.
  * `edMultiplier μ★ n γ = K_n(γ) • μ★`, with
    `K_n(γ) = (n+1) cos^{2n}(γ/2)` the reproducing kernel of the spin-`j`
    coherent states with respect to the normalised round measure (its sphere
    average is `1`, cited not derived, as `p_n` is).  Normalised so that the
    SPHERE-AVERAGED multiplier is `μ★`.

  Proved:

  * `overlap_antitoneOn`, `kernel_antitoneOn` — the multiplier weight decreases
    monotonically in `γ ∈ [0, π]` (approach = monotone increase).
  * `kernel_zero` — `K_n(0) = n + 1`; `kernel_le` — `K_n(γ) ≤ (n+1)(1+γ²/4)^{-n}`;
    `kernel_tendsto_zero` — for fixed `0 < |γ| ≤ π`, `K_n(γ) → 0` as `n → ∞`.
  * `kernel_gt_one_of_near` — `1 ≤ n`, `(n+1) γ² < 4` ⇒ `K_n(γ) > 1`.
  * `kernel_lt_one_of_far` — `|γ| ≤ π`, `32 < (n−1) γ⁴` ⇒ `K_n(γ) < 1`.
  * `ray_mem_cell_below` / `ray_mem_cell_above` — along the ray `t • μ★`, the
    cheapest word `a` (strictly cheapest, active at `μ★`) is the unique active
    word for `0 ≤ t < 1`, and a word `i` active at `μ★` whose channel reading
    `μ★ ⬝ x i` strictly dominates is the unique active word for `t > 1`.
  * `edMultiplier_selects_ilp` — under those hypotheses and `(n+1)γ² < 4`,
    the selected word at `edMultiplier μ★ n γ` is `i` (and locally constant).
  * `edMultiplier_selects_free` — when `32 < (n−1)γ⁴`, it is the free word `a`.
  * `peakMultiplier_selects_free` — NEGATIVE: with the peak normalisation the
    selected word is the free word `a` for EVERY `0 < γ ≤ π`; `i` is reached
    only on the wall at `γ = 0`, where the dual ties `a` and `i`.
  * `dual_monotoneOn_ray` — if `μ★` maximises `g`, `t ↦ g(t • μ★)` is monotone
    on `[0, 1]`; with `peak_dual_antitoneOn` the dual value along the peak path
    is a monotone function of `γ`.

  What is a choice: the normalisation (peak `μ★` vs average `μ★`), and the
  use of `μ★`'s direction (a one-parameter ray).  The thresholds are not fitted:
  they are the inequalities above.

  Archimedean (ℝ).
-/
import QOU.Archimedean.EDCoherentLocality
import QOU.Optimization.LagrangianCollisionFlow
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic.FieldSimp

namespace QOU.Optimization.EDMultiplier

open Real Filter Topology
open QOU.Archimedean.EDCoherentLocality QOU.Optimization.LagrangianCollisionFlow

/-! ### The overlap and the kernel on the divisor -/

theorem overlap_nonneg (n : ℕ) (γ : ℝ) : 0 ≤ overlap n γ := by
  unfold overlap; rw [pow_mul]; positivity

theorem overlap_le_one (n : ℕ) (γ : ℝ) : overlap n γ ≤ 1 := by
  unfold overlap; rw [pow_mul]
  exact pow_le_one₀ (sq_nonneg _) (Real.cos_sq_le_one _)

/-- **Monotone in the angle**: `p_n` decreases on `[0, π]`. -/
theorem overlap_antitoneOn (n : ℕ) : AntitoneOn (overlap n) (Set.Icc 0 π) := by
  intro a ha b hb hab
  unfold overlap
  have hc : Real.cos (b / 2) ≤ Real.cos (a / 2) :=
    Real.cos_le_cos_of_nonneg_of_le_pi (by linarith [ha.1]) (by linarith [hb.2, Real.pi_pos])
      (by linarith)
  have h0 : 0 ≤ Real.cos (b / 2) :=
    Real.cos_nonneg_of_neg_pi_div_two_le_of_le (by linarith [hb.1, Real.pi_pos])
      (by linarith [hb.2])
  exact pow_le_pow_left₀ h0 hc _

/-- Strictly below `1` away from coincidence. -/
theorem overlap_lt_one {n : ℕ} (hn : 1 ≤ n) {γ : ℝ} (h0 : 0 < γ) (hπ : γ ≤ π) :
    overlap n γ < 1 := by
  unfold overlap; rw [pow_mul]
  have hs : 0 < Real.sin (γ / 2) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith [Real.pi_pos])
  have hc : Real.cos (γ / 2) ^ 2 < 1 := by
    nlinarith [Real.sin_sq_add_cos_sq (γ / 2)]
  exact pow_lt_one₀ (sq_nonneg _) hc (by omega)

/-- Reproducing kernel of the spin-`n/2` coherent states for the normalised
round measure: `K_n(γ) = (n+1) cos^{2n}(γ/2)`. -/
noncomputable def kernel (n : ℕ) (γ : ℝ) : ℝ := ((n : ℝ) + 1) * overlap n γ

theorem kernel_nonneg (n : ℕ) (γ : ℝ) : 0 ≤ kernel n γ :=
  mul_nonneg (by positivity) (overlap_nonneg n γ)

theorem kernel_zero (n : ℕ) : kernel n 0 = n + 1 := by
  simp [kernel, overlap_zero]

theorem kernel_antitoneOn (n : ℕ) : AntitoneOn (kernel n) (Set.Icc 0 π) :=
  fun _ ha _ hb hab =>
    mul_le_mul_of_nonneg_left (overlap_antitoneOn n ha hb hab) (by positivity)

theorem kernel_le (n : ℕ) {γ : ℝ} (hγ : |γ| ≤ π) :
    kernel n γ ≤ ((n : ℝ) + 1) * (1 / (1 + γ ^ 2 / 4)) ^ n :=
  mul_le_mul_of_nonneg_left (overlap_le n hγ) (by positivity)

/-- **Locality**: for a fixed angle `0 < |γ| ≤ π`, `K_n(γ) → 0` as `n → ∞`. -/
theorem kernel_tendsto_zero {γ : ℝ} (hγ0 : γ ≠ 0) (hγ : |γ| ≤ π) :
    Tendsto (fun n : ℕ => kernel n γ) atTop (𝓝 0) := by
  set r : ℝ := 1 / (1 + γ ^ 2 / 4)
  have hpos : 0 < 1 + γ ^ 2 / 4 := by positivity
  have hr0 : 0 ≤ r := by positivity
  have hr1 : r < 1 := by
    have : 0 < γ ^ 2 := by positivity
    rw [div_lt_one hpos]; linarith
  have hup : Tendsto (fun n : ℕ => ((n : ℝ) + 1) * r ^ n) atTop (𝓝 0) := by
    have h := (tendsto_self_mul_const_pow_of_lt_one hr0 hr1).add
      (tendsto_pow_atTop_nhds_zero_of_lt_one hr0 hr1)
    rw [add_zero] at h
    refine h.congr (fun n => ?_)
    ring
  exact tendsto_of_tendsto_of_tendsto_of_le_of_le tendsto_const_nhds hup
    (fun n => kernel_nonneg n γ) (fun n => kernel_le n hγ)

/-- `(1+s)^n ≥ 1 + n s + n(n−1)/2 s²` for `s ≥ 0`. -/
theorem quad_le_pow {s : ℝ} (hs : 0 ≤ s) (n : ℕ) :
    1 + n * s + n * (n - 1) / 2 * s ^ 2 ≤ (1 + s) ^ n := by
  induction n with
  | zero => simp
  | succ k ih =>
    have h1 : 0 ≤ 1 + s := by linarith
    have hkk : (0 : ℝ) ≤ (k : ℝ) * ((k : ℝ) - 1) := by
      rcases Nat.eq_zero_or_pos k with h | h
      · simp [h]
      · have : (1 : ℝ) ≤ k := by exact_mod_cast h
        nlinarith
    have hstep := mul_le_mul_of_nonneg_right ih h1
    have hs3 : 0 ≤ (k : ℝ) * ((k : ℝ) - 1) / 2 * s ^ 3 := by positivity
    have hp : (1 + s) ^ (k + 1) = (1 + s) ^ k * (1 + s) := pow_succ (1 + s) k
    push_cast
    have expand : (1 + (k : ℝ) * s + (k : ℝ) * ((k : ℝ) - 1) / 2 * s ^ 2) * (1 + s)
        = 1 + ((k : ℝ) + 1) * s + ((k : ℝ) + 1) * ((k : ℝ) + 1 - 1) / 2 * s ^ 2
          + (k : ℝ) * ((k : ℝ) - 1) / 2 * s ^ 3 := by ring
    linarith [hstep, hs3, expand, hp]

/-- **Explicit outer radius**: `K_n(γ) < 1` once `32 < (n − 1) γ⁴`. -/
theorem kernel_lt_one_of_far {n : ℕ} {γ : ℝ} (hγ : |γ| ≤ π)
    (hfar : 32 < ((n : ℝ) - 1) * γ ^ 4) : kernel n γ < 1 := by
  set s := γ ^ 2 / 4 with hs_def
  have hs : 0 ≤ s := by positivity
  have hg4 : 0 ≤ γ ^ 4 := by positivity
  have hn1 : 0 < (n : ℝ) - 1 := by
    by_contra h
    push_neg at h
    nlinarith
  have hq := quad_le_pow hs n
  have hs2 : 2 < ((n : ℝ) - 1) * s ^ 2 := by
    have : s ^ 2 = γ ^ 4 / 16 := by rw [hs_def]; ring
    rw [this]; linarith
  have hbig : (n : ℝ) + 1 < (1 + s) ^ n := by
    have hn0 : (0 : ℝ) < n := by linarith
    nlinarith [mul_nonneg hn0.le hs]
  have hpos : 0 < (1 + s) ^ n := by positivity
  calc kernel n γ ≤ ((n : ℝ) + 1) * (1 / (1 + γ ^ 2 / 4)) ^ n := kernel_le n hγ
    _ = ((n : ℝ) + 1) / (1 + s) ^ n := by rw [div_pow, one_pow, mul_one_div]
    _ < 1 := by rw [div_lt_one hpos]; exact hbig

/-- **Explicit inner radius**: `K_n(γ) > 1` once `1 ≤ n` and `(n+1) γ² < 4`. -/
theorem kernel_gt_one_of_near {n : ℕ} (hn : 1 ≤ n) {γ : ℝ}
    (hnear : ((n : ℝ) + 1) * γ ^ 2 < 4) : 1 < kernel n γ := by
  have hn1 : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have hg2 : 0 ≤ γ ^ 2 := sq_nonneg γ
  have hg2' : γ ^ 2 < 2 := by nlinarith
  have hcos : 1 - γ ^ 2 / 8 ≤ Real.cos (γ / 2) := by
    have := Real.one_sub_sq_div_two_le_cos (x := γ / 2)
    have e : (γ / 2) ^ 2 / 2 = γ ^ 2 / 8 := by ring
    linarith
  have hc2 : 1 - γ ^ 2 / 4 ≤ Real.cos (γ / 2) ^ 2 := by
    have h0 : 0 ≤ 1 - γ ^ 2 / 8 := by linarith
    nlinarith [mul_le_mul hcos hcos h0 (le_trans h0 hcos)]
  have hb : 1 + (n : ℝ) * (-(γ ^ 2 / 4)) ≤ (1 + -(γ ^ 2 / 4)) ^ n :=
    one_add_mul_le_pow (by linarith) n
  have hp : (1 - γ ^ 2 / 4) ^ n ≤ overlap n γ := by
    unfold overlap; rw [pow_mul]
    exact pow_le_pow_left₀ (by linarith) hc2 n
  have hov : 1 - (n : ℝ) * (γ ^ 2 / 4) ≤ overlap n γ := by
    have e : (1 + -(γ ^ 2 / 4)) = 1 - γ ^ 2 / 4 := by ring
    rw [e] at hb; linarith
  unfold kernel
  have hpos : (0 : ℝ) < n + 1 := by linarith
  calc (1 : ℝ) < ((n : ℝ) + 1) * (1 - (n : ℝ) * (γ ^ 2 / 4)) := by nlinarith
    _ ≤ ((n : ℝ) + 1) * overlap n γ := mul_le_mul_of_nonneg_left hov hpos.le

/-! ### The multiplier and the dual cells along the ray of `μ★` -/

variable {ι : Type*} [Fintype ι] [Nonempty ι] {m : ℕ}

/-- Peak-normalised multiplier: `μ(γ) = p_n(γ) • μ★`. -/
noncomputable def peakMultiplier (μs : Fin m → ℝ) (n : ℕ) (γ : ℝ) : Fin m → ℝ :=
  overlap n γ • μs

/-- Kernel-normalised multiplier: `μ(γ) = K_n(γ) • μ★`. -/
noncomputable def edMultiplier (μs : Fin m → ℝ) (n : ℕ) (γ : ℝ) : Fin m → ℝ :=
  kernel n γ • μs

theorem edMultiplier_zero (μs : Fin m → ℝ) (n : ℕ) :
    edMultiplier μs n 0 = ((n : ℝ) + 1) • μs := by
  simp [edMultiplier, kernel_zero]

theorem peakMultiplier_zero (μs : Fin m → ℝ) (n : ℕ) : peakMultiplier μs n 0 = μs := by
  simp [peakMultiplier, overlap_zero]

omit [Fintype ι] [Nonempty ι] in
/-- Below `μ★`: the strictly cheapest word `a`, if still active at `μ★`, is
the unique active word on the whole segment `[0, μ★)`. -/
theorem ray_mem_cell_below {c : ι → ℝ} {x : ι → Fin m → ℝ} {a : ι} {μs : Fin m → ℝ}
    (hcheap : ∀ j, j ≠ a → c a < c j)
    (hact : ∀ j, c a - μs ⬝ᵥ x a ≤ c j - μs ⬝ᵥ x j)
    {t : ℝ} (ht0 : 0 ≤ t) (ht1 : t < 1) : t • μs ∈ cell c x a := by
  intro j hj
  have h0 := hcheap j hj
  have h1 := hact j
  rw [smul_dotProduct, smul_dotProduct, smul_eq_mul, smul_eq_mul]
  have e : (c j - t * (μs ⬝ᵥ x j)) - (c a - t * (μs ⬝ᵥ x a))
      = (1 - t) * (c j - c a) + t * ((c j - μs ⬝ᵥ x j) - (c a - μs ⬝ᵥ x a)) := by ring
  have : 0 < (1 - t) * (c j - c a) := mul_pos (by linarith) (by linarith)
  have : 0 ≤ t * ((c j - μs ⬝ᵥ x j) - (c a - μs ⬝ᵥ x a)) := mul_nonneg ht0 (by linarith)
  linarith

omit [Fintype ι] [Nonempty ι] in
/-- Beyond `μ★`: a word `i` active at `μ★` whose reading `μ★ ⬝ x i` strictly
dominates every other word's is the unique active word for every `t > 1`. -/
theorem ray_mem_cell_above {c : ι → ℝ} {x : ι → Fin m → ℝ} {i : ι} {μs : Fin m → ℝ}
    (hact : ∀ j, c i - μs ⬝ᵥ x i ≤ c j - μs ⬝ᵥ x j)
    (hdom : ∀ j, j ≠ i → μs ⬝ᵥ x j < μs ⬝ᵥ x i)
    {t : ℝ} (ht : 1 < t) : t • μs ∈ cell c x i := by
  intro j hj
  have h1 := hact j
  have h2 := hdom j hj
  rw [smul_dotProduct, smul_dotProduct, smul_eq_mul, smul_eq_mul]
  have e : (c j - t * (μs ⬝ᵥ x j)) - (c i - t * (μs ⬝ᵥ x i))
      = ((c j - μs ⬝ᵥ x j) - (c i - μs ⬝ᵥ x i)) + (t - 1) * (μs ⬝ᵥ x i - μs ⬝ᵥ x j) := by ring
  have : 0 < (t - 1) * (μs ⬝ᵥ x i - μs ⬝ᵥ x j) := mul_pos (by linarith) (by linarith)
  linarith

/-- `i` active at `μ★`, in the `∀ j` form used above. -/
theorem active_le {c : ι → ℝ} {x : ι → Fin m → ℝ} {μs : Fin m → ℝ} {i : ι}
    (h : Active c x μs i) (j : ι) : c i - μs ⬝ᵥ x i ≤ c j - μs ⬝ᵥ x j := by
  rw [← h]; exact dual_le c x μs j

/-- **Near coincidence the ILP word is selected** (kernel normalisation):
if `i` is active at `μ★` with dominant reading, `1 ≤ n` and `(n+1) γ² < 4`,
then `i` is the unique active word at `edMultiplier μ★ n γ`, and stays active
on a neighbourhood of it. -/
theorem edMultiplier_selects_ilp {c : ι → ℝ} {x : ι → Fin m → ℝ} {i : ι}
    {μs : Fin m → ℝ} (hact : Active c x μs i)
    (hdom : ∀ j, j ≠ i → μs ⬝ᵥ x j < μs ⬝ᵥ x i)
    {n : ℕ} (hn : 1 ≤ n) {γ : ℝ} (hnear : ((n : ℝ) + 1) * γ ^ 2 < 4) :
    edMultiplier μs n γ ∈ cell c x i ∧
      ∀ᶠ ν in 𝓝 (edMultiplier μs n γ), Active c x ν i := by
  have h := ray_mem_cell_above (active_le hact) hdom (kernel_gt_one_of_near hn hnear)
  exact ⟨h, selected_locally_constant h⟩

/-- **Far from coincidence the free word is selected** (kernel normalisation). -/
theorem edMultiplier_selects_free {c : ι → ℝ} {x : ι → Fin m → ℝ} {a : ι}
    {μs : Fin m → ℝ} (hcheap : ∀ j, j ≠ a → c a < c j) (hact : Active c x μs a)
    {n : ℕ} {γ : ℝ} (hγ : |γ| ≤ π) (hfar : 32 < ((n : ℝ) - 1) * γ ^ 4) :
    edMultiplier μs n γ ∈ cell c x a :=
  ray_mem_cell_below hcheap (active_le hact) (kernel_nonneg n γ) (kernel_lt_one_of_far hγ hfar)

/-- The same, for any `γ` with `K_n(γ) < 1` (the exact switch condition). -/
theorem edMultiplier_selects_free_of_kernel_lt {c : ι → ℝ} {x : ι → Fin m → ℝ} {a : ι}
    {μs : Fin m → ℝ} (hcheap : ∀ j, j ≠ a → c a < c j) (hact : Active c x μs a)
    {n : ℕ} {γ : ℝ} (hk : kernel n γ < 1) : edMultiplier μs n γ ∈ cell c x a :=
  ray_mem_cell_below hcheap (active_le hact) (kernel_nonneg n γ) hk

/-- **Negative result for the peak normalisation**: if the free word `a` is
active at `μ★` (as it is when `μ★` sits on the wall between `a` and the ILP
word), then for every `0 < γ ≤ π` and `n ≥ 1` the selected word at
`peakMultiplier μ★ n γ` is `a`, never the ILP word. -/
theorem peakMultiplier_selects_free {c : ι → ℝ} {x : ι → Fin m → ℝ} {a : ι}
    {μs : Fin m → ℝ} (hcheap : ∀ j, j ≠ a → c a < c j) (hact : Active c x μs a)
    {n : ℕ} (hn : 1 ≤ n) {γ : ℝ} (h0 : 0 < γ) (hπ : γ ≤ π) :
    peakMultiplier μs n γ ∈ cell c x a :=
  ray_mem_cell_below hcheap (active_le hact) (overlap_nonneg n γ) (overlap_lt_one hn h0 hπ)

/-- **The dual value increases along the segment to a maximiser.** -/
theorem dual_monotoneOn_ray {c : ι → ℝ} {x : ι → Fin m → ℝ} {μs : Fin m → ℝ}
    (hmax : ∀ ν, dual c x ν ≤ dual c x μs) :
    MonotoneOn (fun t : ℝ => dual c x (t • μs)) (Set.Icc 0 1) := by
  intro t₁ ht₁ t₂ ht₂ h12
  simp only
  rcases eq_or_lt_of_le ht₁.2 with h | h
  · have : t₂ = 1 := le_antisymm ht₂.2 (h ▸ h12)
    rw [h, this]
  · set a := (1 - t₂) / (1 - t₁)
    set b := (t₂ - t₁) / (1 - t₁)
    have hd : 0 < 1 - t₁ := by linarith
    have ha : 0 ≤ a := div_nonneg (by linarith [ht₂.2]) hd.le
    have hb : 0 ≤ b := div_nonneg (by linarith) hd.le
    have hab : a + b = 1 := by
      simp only [a, b]; field_simp; ring
    have hv : a • (t₁ • μs) + b • μs = t₂ • μs := by
      rw [smul_smul, ← add_smul]
      congr 1
      simp only [a, b]; field_simp; ring
    have hc := dual_concave c x (t₁ • μs) μs ha hb hab
    rw [hv] at hc
    have hm := mul_le_mul_of_nonneg_left (hmax (t₁ • μs)) hb
    have ha' : a = 1 - b := by linarith
    rw [ha'] at hc
    nlinarith

/-- Along the peak-normalised approach the dual value is a monotone function of
the angle: it decreases as `γ` grows on `[0, π]`, and equals `g(μ★)` at `γ = 0`. -/
theorem peak_dual_antitoneOn {c : ι → ℝ} {x : ι → Fin m → ℝ} {μs : Fin m → ℝ}
    (hmax : ∀ ν, dual c x ν ≤ dual c x μs) (n : ℕ) :
    AntitoneOn (fun γ => dual c x (peakMultiplier μs n γ)) (Set.Icc 0 π) := by
  intro γ₁ h₁ γ₂ h₂ h12
  exact dual_monotoneOn_ray hmax ⟨overlap_nonneg n γ₂, overlap_le_one n γ₂⟩
    ⟨overlap_nonneg n γ₁, overlap_le_one n γ₁⟩ (overlap_antitoneOn n h₁ h₂ h12)

end QOU.Optimization.EDMultiplier
