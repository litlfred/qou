import Mathlib.Tactic
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Order.Filter.Basic
import QOU.MathlibExt.QIntegerCanonical

open Filter Topology
open QOU.QInteger

noncomputable abbrev qNumberSym (q : ℝ) (n : ℤ) : ℝ :=
  qIntBalZ q n

theorem qNumberSym_classical_limit_nat (n : ℕ) :
    Tendsto (fun q : ℝ => qNumberSym q n) (𝓝[≠] 1) (𝓝 (n : ℝ)) := by
  have h_pos : ∀ᶠ q : ℝ in 𝓝 1, 0 < q := by
    apply IsOpen.mem_nhds isOpen_Ioi
    exact (by positivity : (0 : ℝ) < 1)
  have h_pos2 : ∀ᶠ q : ℝ in 𝓝[≠] 1, 0 < q := nhdsWithin_le_nhds h_pos
  
  have h_eq : (fun q : ℝ => q⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, (q ^ 2) ^ i) =ᶠ[𝓝[≠] 1] (fun q => qNumberSym q n) := by
    filter_upwards [h_pos2, self_mem_nhdsWithin] with q hq0' hq1'
    have hq0 : q ≠ 0 := ne_of_gt hq0'
    have hq1 : q ^ 2 ≠ 1 := by
      intro h
      have h2 : q = 1 ∨ q = -1 := sq_eq_one_iff.mp h
      rcases h2 with rfl | rfl
      · exact hq1' rfl
      · linarith
    rw [qNumberSym, qIntBalZ_natCast, qIntBal_eq_twist_canonical q n hq0 hq1, qIntGeo_def]
  
  have h_lim : Tendsto (fun q : ℝ => q⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, (q ^ 2) ^ i) (𝓝[≠] 1) (𝓝 ((1 : ℝ)⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, ((1 : ℝ) ^ 2) ^ i)) := by
    apply Tendsto.mul
    · refine Tendsto.pow ?_ _
      exact (continuousAt_inv₀ one_ne_zero).tendsto.mono_left nhdsWithin_le_nhds
    · refine tendsto_finset_sum _ (fun i _ => ?_)
      refine Tendsto.pow ?_ _
      refine Tendsto.pow ?_ _
      exact continuous_id.continuousAt.tendsto.mono_left nhdsWithin_le_nhds

  have h_eval : ((1 : ℝ)⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, ((1 : ℝ) ^ 2) ^ i) = (n : ℝ) := by
    simp
  
  rw [h_eval] at h_lim
  exact Tendsto.congr' h_eq h_lim

theorem qNumberSym_classical_limit (n : ℤ) :
    Tendsto (fun q : ℝ => qNumberSym q n) (𝓝[≠] 1) (𝓝 (n : ℝ)) := by
  cases n with
  | ofNat n => exact qNumberSym_classical_limit_nat n
  | negSucc n =>
      have h_eq : (fun q : ℝ => qNumberSym q (Int.negSucc n)) = fun q : ℝ => -qNumberSym q (n + 1) := by
        ext q
        have : Int.negSucc n = -((n + 1 : ℕ) : ℤ) := rfl
        rw [this, qNumberSym, qNumberSym, qIntBalZ_neg]
        push_cast
        rfl
      rw [h_eq]
      have H := qNumberSym_classical_limit_nat (n + 1)
      have H2 := Tendsto.neg H
      have H3 : -((n + 1 : ℕ) : ℝ) = (Int.negSucc n : ℝ) := by
        push_cast
        rfl
      rw [H3] at H2
      exact H2
