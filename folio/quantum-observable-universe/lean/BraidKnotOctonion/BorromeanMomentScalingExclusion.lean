/-
# Borromean/Brunnian cluster vs residual-moment A-scaling: structural exclusion

The Δ_λ residual-moment closure would identify the A-body irreducible residual
moment `μ_A` with the A-component Brunnian cluster `c_A`. A genuine Brunnian
A-link has first non-vanishing Milnor invariant at length `A`, so its Hecke
trace deficit has leading order `O(h^{2(A-1)})` (`h = q - q⁻¹` the Hecke
parameter). Measured at the substrate `h ≈ 0.209 < 1` (A=3: order 4.1; A=4:
order 6.06 — `a4_h12_brunnian_deficit_measure_probe.py`), so the cluster
magnitude is `c_A = κ_A · h^{2(A-1)}` with `0 < h < 1`.

This file formalizes the structural consequence measured in
`borromean_two_moment_consistency_probe.py`
(`docs/audits/2026-08-01-deltalambda-borromean-two-moment-consistency.md`):
because `0 < h < 1`, the cluster-order sequence is **strictly decreasing in A**
(the clusters VANISH as `A → ∞`), whereas the physical residual moments GROW.
A strictly-decreasing sequence meets a strictly-increasing one **at most once**,
so the identification `c_A = μ_A` can hold for at most a single `A` and is
structurally excluded as a magnitude closure for the moment *sequence*.

This is a scope-(a) structural statement: it does not refute the Milnor-parity
SIGN law (which is derived separately and stands); it shows the *magnitude*
identification cannot be a closure. No physical constant is fitted here — the
`κ`, the growth of `μ`, and `0 < h < 1` enter as hypotheses; the conclusion is
derived.
-/
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Order.Monotone.Basic

namespace QOU.MassTheory.BorromeanMomentScaling

open Function

/-- The order-normalized Brunnian cluster magnitude as a function of the level
index `k = A - 1`: `c(k) = κ · r^k` with `r = h² ∈ (0,1)` the per-order Hecke
suppression. (Working in `k` avoids `ℕ`-subtraction; `A ↦ A-1` is a bijection.) -/
noncomputable def clusterOrd (r κ : ℝ) (k : ℕ) : ℝ := κ * r ^ k

/-- With `0 < r < 1` and `κ > 0`, the Brunnian cluster order is **strictly
antitone** in the level index: co-present bonds are ever more `h`-suppressed, so
the cluster magnitude strictly decreases as the body-order `A` grows. -/
theorem clusterOrd_strictAnti {r κ : ℝ} (hr0 : 0 < r) (hr1 : r < 1)
    (hκ : 0 < κ) : StrictAnti (clusterOrd r κ) := by
  intro a b hab
  simp only [clusterOrd]
  apply mul_lt_mul_of_pos_left _ hκ
  -- goal: r ^ b < r ^ a  (exponent strictly decreasing, base in (0,1))
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_lt hab
  have h1 : (0 : ℝ) < r ^ a := pow_pos hr0 a
  have h2 : r ^ (d + 1) < 1 := pow_lt_one₀ hr0.le hr1 (Nat.succ_ne_zero d)
  have key : r ^ (a + d + 1) = r ^ a * r ^ (d + 1) := by
    rw [Nat.add_assoc, pow_add]
  rw [key]
  calc r ^ a * r ^ (d + 1) < r ^ a * 1 := mul_lt_mul_of_pos_left h2 h1
    _ = r ^ a := mul_one _

/-- **Cross-at-most-once.** A strictly antitone real sequence `f` and a strictly
monotone (increasing) real sequence `g` can agree at **at most one** index. -/
theorem eq_at_most_once {f g : ℕ → ℝ} (hf : StrictAnti f) (hg : StrictMono g)
    {a b : ℕ} (ha : f a = g a) (hb : f b = g b) : a = b := by
  rcases lt_trichotomy a b with h | h | h
  · exfalso
    have hf' : f b < f a := hf h
    have hg' : g a < g b := hg h
    -- f b < f a = g a < g b = f b : contradiction
    rw [ha, hb] at hf'
    exact absurd hf' (not_lt.mpr hg'.le)
  · exact h
  · exfalso
    have hf' : f a < f b := hf h
    have hg' : g b < g a := hg h
    rw [ha, hb] at hf'
    exact absurd hf' (not_lt.mpr hg'.le)

/-- **Structural exclusion (main statement).** If the Brunnian cluster order
`c_A = κ·r^{A-1}` (`r = h² ∈ (0,1)`, `κ > 0`) is identified with a strictly
increasing residual-moment sequence `μ`, then the identification `c = μ` holds
for **at most one** body-order — hence it cannot be a magnitude closure for the
whole sequence. The clusters are strictly decreasing while the moments strictly
increase; they cross at most once. -/
theorem brunnian_identification_at_most_one_A
    {r κ : ℝ} (hr0 : 0 < r) (hr1 : r < 1) (hκ : 0 < κ)
    {μ : ℕ → ℝ} (hμ : StrictMono μ)
    {a b : ℕ} (ha : clusterOrd r κ a = μ a) (hb : clusterOrd r κ b = μ b) :
    a = b :=
  eq_at_most_once (clusterOrd_strictAnti hr0 hr1 hκ) hμ ha hb

/-- The clusters tend to `0` as the body-order grows (`0 < r < 1`), so they
cannot track an unbounded (growing) moment sequence: an explicit witness that
the exclusion is not vacuous. -/
theorem clusterOrd_tendsto_zero {r κ : ℝ} (hr0 : 0 ≤ r) (hr1 : r < 1) :
    Filter.Tendsto (clusterOrd r κ) Filter.atTop (nhds 0) := by
  have h : Filter.Tendsto (fun k : ℕ => r ^ k) Filter.atTop (nhds 0) :=
    tendsto_pow_atTop_nhds_zero_of_lt_one hr0 hr1
  have := h.const_mul κ
  simpa [clusterOrd, mul_comm] using this

/-- **Strict positivity of the Brunnian cluster magnitude at every level `k` (`bean qou-f1wk`).** -/
theorem clusterOrd_pos {r κ : ℝ} (hr0 : 0 < r) (hκ : 0 < κ) (k : ℕ) :
    0 < clusterOrd r κ k := by
  have hk : (0 : ℝ) < r ^ k := pow_pos hr0 k
  exact mul_pos hκ hk

/-- **Pointwise strict decrease of the Brunnian cluster magnitude (`bean qou-f1wk`).** -/
theorem clusterOrd_lt_of_lt {r κ : ℝ} (hr0 : 0 < r) (hr1 : r < 1) (hκ : 0 < κ)
    {a b : ℕ} (hab : a < b) :
    clusterOrd r κ b < clusterOrd r κ a :=
  clusterOrd_strictAnti hr0 hr1 hκ hab

end QOU.MassTheory.BorromeanMomentScaling
