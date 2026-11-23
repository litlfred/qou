import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Analysis.Normed.Group.FunctionSeries
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic

/-!
# Horizon entropy as the `q`-dimension partition-function pole

Formalisation and unconditional QOU instantiation of `conj:lqg-entropy-qdim-partition-pole`.

The block recasts the LQG horizon-entropy state count algebraically: for non-trivial
puncture spins `j = (n + 1) / 2 ∈ ½ℤ_{>0}` (`2j = n + 1`, `n : ℕ`), the per-puncture
`q`-dimension partition function

  `Z₁(s) = Σ_{n : ℕ} [n + 2]_q · exp(-s · C_q(V_{(n+1)/2}))`

has a unique critical value `s⋆ > 0` with `Z₁(s⋆) = 1`, the horizon generating
function `Σ_k Z₁(s)^k = (1 - Z₁(s))⁻¹` poles there, the closed-horizon `U(1)`
Gauss law `Σ_p m_p = 0` is equivalent to triviality of the diagonal `U(1)` Cartan
action (trace closure into `1 → 1`), and `γ = s⋆ / (2π)` fixes the Barbero–Immirzi
parameter.

What this file proves (zero `sorry`, zero `axiom`):
1. **Conditional pole interface (`LQGEntropyQDimPartitionPole`)**: derives existence
   and uniqueness of `s⋆`, the geometric-series pole `(1 - Z₁(s))⁻¹` for `s > s⋆`
   with divergence at `s = s⋆`, and the Immirzi relation `γ = s⋆ / (2π)`.
2. **Spin-zero exclusion (`Z1_gt_one_if_spin_zero_included`)**: if `j = 0` (`qdim 0 = 1`,
   `casimir 0 = 0`) were included alongside any positive puncture channel `qdim 1 > 0`,
   then `1 < Z₁(s)` for every convergent `s`, so `Z₁(s) = 1` would have no root.
3. **Closed-horizon `U(1)` Gauss constraint (`u1_gauss_constraint_iff_sum_zero`)**:
   on `m` punctures with magnetic weights `w : Fin m → ℤ`, the diagonal `U(1)` action
   `z ↦ ∏ᵢ z^{wᵢ}` is trivial (`∀ z : Circle, … = 1`) iff `∑ᵢ wᵢ = 0`.
4. **Unconditional QOU quantum-group instantiation (`qou_lqg_partition_pole_holds`,
   `qou_exists_unique_positive_critical`)**: for every real `q > 1`, the genuine QOU
   puncture `q`-dimension `qouPunctureQDim q n = [n + 2]_q` and quantum Casimir
   `qouCasimir q n = [(n+1)/2]_q · [(n+3)/2]_q` satisfy `LQGEntropyQDimPartitionPole`
   on an explicit window `[qouPoleLo q, qouPoleHi q] ⊂ (0, ∞)` and admit a globally
   unique critical root `s⋆ > 0` with `Z₁(s⋆) = 1`.

Ref: [leitner2026] conj:lqg-entropy-qdim-partition-pole
Ref: [domagala-lewandowski-2004]
Ref: [meissner2004]
Ref: [ashtekar-baez-corichi-krasnov-1998]
-/

namespace QOU.GravitySpacetime

noncomputable def Z1 (qdim casimir : ℕ → ℝ) (s : ℝ) : ℝ :=
  ∑' n : ℕ, qdim n * Real.exp (-s * casimir n)

class LQGEntropyQDimPartitionPole
    (qdim casimir : ℕ → ℝ) (lo hi : ℝ) : Prop where
  lo_lt_hi : lo < hi
  Z1_continuous : ContinuousOn (Z1 qdim casimir) (Set.Icc lo hi)
  Z1_strictAnti : StrictAntiOn (Z1 qdim casimir) (Set.Icc lo hi)
  Z1_super : 1 < Z1 qdim casimir lo
  Z1_sub : Z1 qdim casimir hi < 1

namespace LQGEntropyQDimPartitionPole

variable {qdim casimir : ℕ → ℝ} {lo hi : ℝ}
variable [h : LQGEntropyQDimPartitionPole qdim casimir lo hi]

theorem exists_critical : ∃ s ∈ Set.Icc lo hi, Z1 qdim casimir s = 1 := by
  have hle : lo ≤ hi := le_of_lt h.lo_lt_hi
  have hsub : Set.Icc (1:ℝ) (Z1 qdim casimir lo) ⊆
      (Z1 qdim casimir) '' (Set.Icc lo hi) := by
    have hiv := intermediate_value_Icc' hle h.Z1_continuous
    exact fun y hy => hiv ⟨le_of_lt (lt_of_lt_of_le h.Z1_sub hy.1), hy.2⟩
  obtain ⟨s, hs, hval⟩ := hsub ⟨le_refl 1, le_of_lt h.Z1_super⟩
  exact ⟨s, hs, hval⟩

theorem critical_unique {s t : ℝ}
    (hs : s ∈ Set.Icc lo hi) (ht : t ∈ Set.Icc lo hi)
    (hsv : Z1 qdim casimir s = 1) (htv : Z1 qdim casimir t = 1) : s = t :=
  h.Z1_strictAnti.injOn hs ht (hsv.trans htv.symm)

theorem exists_unique_critical :
    ∃! s, s ∈ Set.Icc lo hi ∧ Z1 qdim casimir s = 1 := by
  obtain ⟨s, hs, hval⟩ := exists_critical (h := h)
  refine ⟨s, ⟨hs, hval⟩, ?_⟩
  rintro t ⟨ht, htv⟩
  exact critical_unique (h := h) ht hs htv hval

/-- Subcritical horizon-state generating function (`s > s⋆`):
    when `Z₁(s⋆) = 1`, `s⋆ < s`, and `0 ≤ Z₁(s)`, the multi-puncture sum
    `∑_{k≥0} Z₁(s)^k` converges to the resolvent `(1 - Z₁(s))⁻¹`. -/
theorem horizonGenerating_eq_resolvent {sStar s : ℝ}
    (hsStar : sStar ∈ Set.Icc lo hi) (hs : s ∈ Set.Icc lo hi)
    (hcrit : Z1 qdim casimir sStar = 1) (hlt : sStar < s)
    (hnonneg : 0 ≤ Z1 qdim casimir s) :
    (∑' k : ℕ, (Z1 qdim casimir s) ^ k) = (1 - Z1 qdim casimir s)⁻¹ := by
  have hZlt : Z1 qdim casimir s < 1 := by
    rw [← hcrit]
    exact h.Z1_strictAnti hsStar hs hlt
  exact tsum_geometric_of_lt_one hnonneg hZlt

/-- Critical pole of the horizon-state generating function (`s = s⋆`):
    at `Z₁(s⋆) = 1`, the series `∑_{k≥0} Z₁(s⋆)^k` diverges (`¬ Summable`). -/
theorem horizonGenerating_not_summable_at_critical {sStar : ℝ}
    (hcrit : Z1 qdim casimir sStar = 1) :
    ¬ Summable (fun k : ℕ => (Z1 qdim casimir sStar) ^ k) := by
  intro hsum
  have h1 : Summable (fun _ : ℕ => (1 : ℝ)) := by
    simpa [hcrit] using hsum
  have hzero : (1 : ℝ) = 0 := tendsto_nhds_unique tendsto_const_nhds h1.tendsto_atTop_zero
  norm_num at hzero

noncomputable def immirzi (sStar : ℝ) : ℝ := sStar / (2 * Real.pi)

theorem immirzi_pos {sStar : ℝ} (hs : 0 < sStar) : 0 < immirzi sStar := by
  unfold immirzi; positivity

theorem immirzi_eq_iff {sStar g : ℝ} :
    immirzi sStar = g ↔ sStar = 2 * Real.pi * g := by
  unfold immirzi
  rw [div_eq_iff (by positivity : (2:ℝ) * Real.pi ≠ 0)]
  constructor <;> intro hEq <;> linarith [hEq]

end LQGEntropyQDimPartitionPole

/-! ### Satisfiability witness -/

noncomputable def witnessQdim : ℕ → ℝ := fun n => if n = 0 then 2 else 0
noncomputable def witnessCasimir : ℕ → ℝ := fun _ => 1

theorem Z1_witness (s : ℝ) : Z1 witnessQdim witnessCasimir s = 2 * Real.exp (-s) := by
  unfold Z1
  rw [tsum_eq_single 0 (by intro n hn; simp [witnessQdim, witnessCasimir, hn])]
  simp [witnessQdim, witnessCasimir]

instance witness_pole :
    LQGEntropyQDimPartitionPole witnessQdim witnessCasimir 0 1 where
  lo_lt_hi := by norm_num
  Z1_continuous := by
    have hfun : Z1 witnessQdim witnessCasimir = fun s => 2 * Real.exp (-s) := by
      funext s; exact Z1_witness s
    rw [hfun]
    exact (by continuity : Continuous fun s : ℝ => 2 * Real.exp (-s)).continuousOn
  Z1_strictAnti := by
    intro a _ b _ hab
    simp only [Z1_witness]
    have : Real.exp (-b) < Real.exp (-a) := Real.exp_lt_exp.mpr (by linarith)
    linarith
  Z1_super := by
    rw [Z1_witness, neg_zero, Real.exp_zero]
    norm_num
  Z1_sub := by
    simp only [Z1_witness]
    have h2 : (2:ℝ) < Real.exp 1 := by
      have := Real.add_one_lt_exp (x := (1:ℝ)) (by norm_num)
      linarith
    rw [Real.exp_neg]
    rw [mul_inv_lt_iff₀ (Real.exp_pos 1)]
    linarith

/-! ### Why `j = 0` must be excluded from puncture state counting -/

/-- If the trivial representation `j = 0` (`qdim 0 = 1`, `casimir 0 = 0`) is included
    alongside non-negative puncture weights with `0 < qdim 1`, then `1 < Z₁(s)` at
    every `s` where the series converges, so `Z₁(s) = 1` has no solution. Physical
    horizon punctures therefore range over non-trivial spins `j ∈ ½ℤ_{>0}`. -/
theorem Z1_gt_one_if_spin_zero_included {qdim casimir : ℕ → ℝ}
    (hq0 : qdim 0 = 1) (hc0 : casimir 0 = 0)
    (hq_nonneg : ∀ n, 0 ≤ qdim n) (hq1 : 0 < qdim 1)
    (s : ℝ) (hsum : Summable (fun n => qdim n * Real.exp (-s * casimir n))) :
    1 < Z1 qdim casimir s := by
  unfold Z1
  have hfin : ∑ i ∈ ({0, 1} : Finset ℕ), qdim i * Real.exp (-s * casimir i) ≤
      ∑' n : ℕ, qdim n * Real.exp (-s * casimir n) :=
    hsum.sum_le_tsum ({0, 1} : Finset ℕ)
      (fun i _ => mul_nonneg (hq_nonneg i) (le_of_lt (Real.exp_pos _)))
  have htwo : ∑ i ∈ ({0, 1} : Finset ℕ), qdim i * Real.exp (-s * casimir i) =
      1 + qdim 1 * Real.exp (-s * casimir 1) := by
    simp [hq0, hc0]
  have hpos : 0 < qdim 1 * Real.exp (-s * casimir 1) :=
    mul_pos hq1 (Real.exp_pos _)
  linarith

/-! ### Claim 2: Closed-horizon `U(1)` Gauss constraint as trace closure -/

/-- Diagonal `U(1)` Cartan action on an `m`-puncture horizon boundary state with
    puncture magnetic weights `w : Fin m → ℤ`. -/
noncomputable def u1HorizonAction {m : ℕ} (w : Fin m → ℤ) (z : Circle) : Circle :=
  ∏ i : Fin m, z ^ (w i)

private lemma circle_prod_zpow {α : Type*} [DecidableEq α] (s : Finset α)
    (w : α → ℤ) (z : Circle) :
    (∏ i ∈ s, z ^ (w i)) = z ^ (∑ i ∈ s, w i) := by
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih =>
      rw [Finset.prod_insert ha, Finset.sum_insert ha, ih, zpow_add]

theorem u1HorizonAction_eq_zpow_sum {m : ℕ} (w : Fin m → ℤ) (z : Circle) :
    u1HorizonAction w z = z ^ (∑ i : Fin m, w i) :=
  circle_prod_zpow Finset.univ w z

private lemma circle_exp_npow (θ : ℝ) :
    ∀ n : ℕ, (Circle.exp θ) ^ n = Circle.exp ((n : ℝ) * θ)
  | 0 => by simp
  | n + 1 => by
      rw [pow_succ, circle_exp_npow θ n, ← Circle.exp_add]
      push_cast
      ring_nf

private lemma circle_exp_inv (θ : ℝ) : (Circle.exp θ)⁻¹ = Circle.exp (-θ) := by
  apply inv_eq_of_mul_eq_one_right
  rw [← Circle.exp_add, add_neg_cancel, Circle.exp_zero]

private lemma circle_exp_zpow (θ : ℝ) :
    ∀ k : ℤ, (Circle.exp θ) ^ k = Circle.exp ((k : ℝ) * θ)
  | Int.ofNat n => by simp [circle_exp_npow]
  | Int.negSucc n => by
      rw [zpow_negSucc, circle_exp_npow, circle_exp_inv]
      push_cast
      ring_nf

private lemma circle_exp_pi_div_two_ne_one :
    Circle.exp (Real.pi / 2) ≠ (1 : Circle) := by
  intro h1
  have hre : ((Circle.exp (Real.pi / 2) : ℂ)).re = ((1 : Circle) : ℂ).re :=
    congrArg Complex.re (congrArg Subtype.val h1)
  rw [Circle.coe_exp, Complex.exp_mul_I] at hre
  have hcos : Complex.cos ((Real.pi / 2 : ℝ) : ℂ) = (Real.cos (Real.pi / 2) : ℂ) :=
    (Complex.ofReal_cos (Real.pi / 2)).symm
  have hsin : Complex.sin ((Real.pi / 2 : ℝ) : ℂ) = (Real.sin (Real.pi / 2) : ℂ) :=
    (Complex.ofReal_sin (Real.pi / 2)).symm
  rw [hcos, hsin] at hre
  simp [Real.cos_pi_div_two] at hre

/-- **Closed-horizon `U(1)` Gauss constraint = trace closure:**
    the `m`-puncture diagonal `U(1)` action is trivial (so the closed-link
    evaluation descends to an invariant morphism `1 → 1`) iff `∑ᵢ wᵢ = 0`. -/
theorem u1_gauss_constraint_iff_sum_zero {m : ℕ} (w : Fin m → ℤ) :
    (∀ z : Circle, u1HorizonAction w z = 1) ↔ (∑ i : Fin m, w i) = 0 := by
  constructor
  · intro hall
    by_contra hne
    set k : ℤ := ∑ i : Fin m, w i
    have hkR : (k : ℝ) ≠ 0 := Int.cast_ne_zero.mpr hne
    have hspec := hall (Circle.exp (Real.pi / (2 * (k : ℝ))))
    rw [u1HorizonAction_eq_zpow_sum, circle_exp_zpow] at hspec
    have hangle : (k : ℝ) * (Real.pi / (2 * (k : ℝ))) = Real.pi / 2 := by
      field_simp
    rw [hangle] at hspec
    exact circle_exp_pi_div_two_ne_one hspec
  · intro hzero z
    rw [u1HorizonAction_eq_zpow_sum, hzero, zpow_zero]

/-! ### Unconditional QOU quantum-group data over non-trivial punctures `2j = n + 1` -/

/-- Half-integer quantum integer `[k / 2]_q = (q^{k/2} - q^{-k/2}) / (q - q⁻¹)`
    expressed via `Real.sqrt q`. -/
noncomputable def qHalfInt (q : ℝ) (k : ℕ) : ℝ :=
  (Real.sqrt q ^ k - (Real.sqrt q)⁻¹ ^ k) / (q - q⁻¹)

/-- Genuine QOU puncture `q`-dimension `[2j + 1]_q = [n + 2]_q` on non-trivial
    boundary spins `2j = n + 1` (`n : ℕ`, so `j = 1/2, 1, 3/2, …`). -/
noncomputable def qouPunctureQDim (q : ℝ) (n : ℕ) : ℝ :=
  (q ^ (n + 2) - q⁻¹ ^ (n + 2)) / (q - q⁻¹)

/-- Genuine QOU quantum Casimir eigenvalue `[j]_q · [j + 1]_q` on `V_j` for
    non-trivial boundary spins `j = (n + 1) / 2` (`n : ℕ`). -/
noncomputable def qouCasimir (q : ℝ) (n : ℕ) : ℝ :=
  qHalfInt q (n + 1) * qHalfInt q (n + 3)

private lemma q_sub_inv_pos {q : ℝ} (hq : 1 < q) : 0 < q - q⁻¹ := by
  have hinv : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  linarith

private lemma one_lt_sqrt {q : ℝ} (hq : 1 < q) : 1 < Real.sqrt q := by
  calc (1 : ℝ) = Real.sqrt 1 := Real.sqrt_one.symm
    _ < Real.sqrt q := Real.sqrt_lt_sqrt (by norm_num) hq

/-- Elementary convexity / telescoping lower bound for Laurent differences:
    for all `x ≥ 1` and `k : ℕ`, `k · (x - x⁻¹) ≤ x^k - x⁻ᵏ`. -/
theorem nat_mul_sub_inv_le_pow_sub_inv_pow {x : ℝ} (hx : 1 ≤ x) :
    ∀ k : ℕ, (k : ℝ) * (x - x⁻¹) ≤ x ^ k - x⁻¹ ^ k
  | 0 => by simp
  | k + 1 => by
      have ih := nat_mul_sub_inv_le_pow_sub_inv_pow hx k
      have hx0 : 0 < x := by linarith
      have hx_ne : x ≠ 0 := ne_of_gt hx0
      have h1 : x * x⁻¹ ^ (k + 1) = x⁻¹ ^ k := by
        rw [pow_succ', ← mul_assoc, mul_inv_cancel₀ hx_ne, one_mul]
      have h2 : x ^ k * x⁻¹ ^ (k + 1) = x⁻¹ := by
        rw [pow_succ, ← mul_assoc, ← mul_pow, mul_inv_cancel₀ hx_ne, one_pow, one_mul]
      have h3 : x * x⁻¹ = 1 := mul_inv_cancel₀ hx_ne
      have hident :
          (x - 1) * (x ^ k - 1) * (1 - x⁻¹ ^ (k + 1)) =
            ((x ^ (k + 1) - x⁻¹ ^ (k + 1)) - (x ^ k - x⁻¹ ^ k)) - (x - x⁻¹) := by
        calc (x - 1) * (x ^ k - 1) * (1 - x⁻¹ ^ (k + 1))
            = x * x ^ k - x - x ^ k + 1 - (x - 1) * (x ^ k * x⁻¹ ^ (k + 1)) +
                x * x⁻¹ ^ (k + 1) - x⁻¹ ^ (k + 1) := by ring
          _ = x ^ (k + 1) - x - x ^ k + 1 - (x - 1) * x⁻¹ + x⁻¹ ^ k - x⁻¹ ^ (k + 1) := by
                rw [← pow_succ' x k, h2, h1]
          _ = x ^ (k + 1) - x - x ^ k + 1 - (x * x⁻¹ - x⁻¹) + x⁻¹ ^ k - x⁻¹ ^ (k + 1) := by
                ring
          _ = ((x ^ (k + 1) - x⁻¹ ^ (k + 1)) - (x ^ k - x⁻¹ ^ k)) - (x - x⁻¹) := by
                rw [h3]; ring
      have hxk : 1 ≤ x ^ k := one_le_pow₀ hx
      have hyk : x⁻¹ ^ (k + 1) ≤ 1 :=
        pow_le_one₀ (by positivity) (inv_le_one_of_one_le₀ hx)
      have hnonneg : 0 ≤ (x - 1) * (x ^ k - 1) * (1 - x⁻¹ ^ (k + 1)) :=
        mul_nonneg (mul_nonneg (by linarith) (by linarith)) (by linarith)
      push_cast
      linarith [hident, hnonneg, ih]

theorem qHalfInt_one_pos {q : ℝ} (hq : 1 < q) : 0 < qHalfInt q 1 := by
  unfold qHalfInt
  simp only [pow_one]
  have hs := one_lt_sqrt hq
  have hsinv : (Real.sqrt q)⁻¹ < 1 := inv_lt_one_of_one_lt₀ hs
  exact div_pos (by linarith) (q_sub_inv_pos hq)

theorem nat_mul_qHalfInt_one_le {q : ℝ} (hq : 1 < q) (k : ℕ) :
    (k : ℝ) * qHalfInt q 1 ≤ qHalfInt q k := by
  have hs : 1 ≤ Real.sqrt q := le_of_lt (one_lt_sqrt hq)
  have hpow := nat_mul_sub_inv_le_pow_sub_inv_pow hs k
  have hdiv := div_le_div_of_nonneg_right hpow (le_of_lt (q_sub_inv_pos hq))
  simpa [qHalfInt, pow_one, mul_div_assoc] using hdiv

/-- Quadratic lower bound on the QOU quantum Casimir:
    `([1/2]_q)² · (n + 1)² ≤ qouCasimir q n` for all `n : ℕ` and `q > 1`. -/
theorem qouCasimir_quad_lower {q : ℝ} (hq : 1 < q) (n : ℕ) :
    (qHalfInt q 1) ^ 2 * ((n : ℝ) + 1) ^ 2 ≤ qouCasimir q n := by
  unfold qouCasimir
  have hc1 : 0 < qHalfInt q 1 := qHalfInt_one_pos hq
  have h1 : ((n : ℝ) + 1) * qHalfInt q 1 ≤ qHalfInt q (n + 1) := by
    simpa [Nat.cast_add, Nat.cast_one] using nat_mul_qHalfInt_one_le hq (n + 1)
  have h3 : ((n : ℝ) + 3) * qHalfInt q 1 ≤ qHalfInt q (n + 3) := by
    simpa [Nat.cast_add] using nat_mul_qHalfInt_one_le hq (n + 3)
  have h13 : ((n : ℝ) + 1) * qHalfInt q 1 ≤ ((n : ℝ) + 3) * qHalfInt q 1 := by
    nlinarith
  have hle3 : ((n : ℝ) + 1) * qHalfInt q 1 ≤ qHalfInt q (n + 3) := le_trans h13 h3
  have hpos1 : 0 ≤ ((n : ℝ) + 1) * qHalfInt q 1 := by positivity
  have hmul : (((n : ℝ) + 1) * qHalfInt q 1) * (((n : ℝ) + 1) * qHalfInt q 1) ≤
      qHalfInt q (n + 1) * qHalfInt q (n + 3) :=
    mul_le_mul h1 hle3 hpos1 (le_trans hpos1 h1)
  linarith [show (((n : ℝ) + 1) * qHalfInt q 1) * (((n : ℝ) + 1) * qHalfInt q 1) =
    (qHalfInt q 1) ^ 2 * ((n : ℝ) + 1) ^ 2 by ring]

theorem qouCasimir_pos {q : ℝ} (hq : 1 < q) (n : ℕ) : 0 < qouCasimir q n := by
  have hc : 0 < qHalfInt q 1 := qHalfInt_one_pos hq
  have hlow := qouCasimir_quad_lower hq n
  have hsq : 0 < (qHalfInt q 1) ^ 2 * ((n : ℝ) + 1) ^ 2 := by positivity
  linarith

theorem qouPunctureQDim_pos {q : ℝ} (hq : 1 < q) (n : ℕ) :
    0 < qouPunctureQDim q n := by
  unfold qouPunctureQDim
  have hpow : 1 < q ^ (n + 2) := one_lt_pow₀ hq (by omega)
  have hinv : q⁻¹ ^ (n + 2) ≤ 1 :=
    pow_le_one₀ (by positivity) (le_of_lt (inv_lt_one_of_one_lt₀ hq))
  exact div_pos (by linarith) (q_sub_inv_pos hq)

theorem qouPunctureQDim_zero {q : ℝ} (hq : 1 < q) :
    qouPunctureQDim q 0 = q + q⁻¹ := by
  unfold qouPunctureQDim
  have hne : q - q⁻¹ ≠ 0 := ne_of_gt (q_sub_inv_pos hq)
  have hsq : q ^ 2 - q⁻¹ ^ 2 = (q - q⁻¹) * (q + q⁻¹) := by ring
  rw [show (0 + 2 : ℕ) = 2 from rfl, hsq, mul_div_cancel_left₀ _ hne]

theorem two_lt_qouPunctureQDim_zero {q : ℝ} (hq : 1 < q) :
    2 < qouPunctureQDim q 0 := by
  rw [qouPunctureQDim_zero hq]
  have hq0 : 0 < q := by linarith
  have hpos : 0 < (q - 1) ^ 2 / q := div_pos (sq_pos_of_pos (by linarith)) hq0
  have hid : q + q⁻¹ - 2 = (q - 1) ^ 2 / q := by field_simp; ring
  linarith

private lemma qouPunctureQDim_le_exp {q : ℝ} (hq : 1 < q) (n : ℕ) :
    qouPunctureQDim q n ≤ Real.exp (((n : ℝ) + 2) * Real.log q) / (q - q⁻¹) := by
  unfold qouPunctureQDim
  have hq0 : 0 < q := by linarith
  have hinv_nonneg : 0 ≤ q⁻¹ ^ (n + 2) := by positivity
  have hnum : q ^ (n + 2) - q⁻¹ ^ (n + 2) ≤ Real.exp (((n : ℝ) + 2) * Real.log q) := by
    have hpow : q ^ (n + 2) = Real.exp (((n : ℝ) + 2) * Real.log q) := by
      calc q ^ (n + 2) = (Real.exp (Real.log q)) ^ (n + 2) := by rw [Real.exp_log hq0]
        _ = Real.exp (((n + 2 : ℕ) : ℝ) * Real.log q) := (Real.exp_nat_mul _ _).symm
        _ = Real.exp (((n : ℝ) + 2) * Real.log q) := by push_cast; rfl
    linarith
  exact div_le_div_of_nonneg_right hnum (le_of_lt (q_sub_inv_pos hq))

/-- Uniform geometric Weierstrass majorant for `Z₁(s)` on `[lo, ∞)` (`lo > 0`). -/
private noncomputable def qouMajorant (q lo : ℝ) (n : ℕ) : ℝ :=
  let a := lo * (qHalfInt q 1) ^ 2
  let b := Real.log q
  let B := (b + 1) ^ 2 / (4 * a) + b - 1
  (Real.exp B / (q - q⁻¹)) * (Real.exp (-1)) ^ n

private lemma qouMajorant_summable (q lo : ℝ) : Summable (qouMajorant q lo) := by
  unfold qouMajorant
  have hr0 : 0 ≤ Real.exp (-1) := le_of_lt (Real.exp_pos _)
  have hr1 : Real.exp (-1) < 1 := Real.exp_lt_one_iff.mpr (by norm_num)
  exact (summable_geometric_of_lt_one hr0 hr1).mul_left _

private lemma qouTerm_le_majorant {q lo s : ℝ} (hq : 1 < q) (hlo : 0 < lo)
    (hs : lo ≤ s) (n : ℕ) :
    qouPunctureQDim q n * Real.exp (-s * qouCasimir q n) ≤ qouMajorant q lo n := by
  set a : ℝ := lo * (qHalfInt q 1) ^ 2
  set b : ℝ := Real.log q
  set B : ℝ := (b + 1) ^ 2 / (4 * a) + b - 1
  have hc1 : 0 < qHalfInt q 1 := qHalfInt_one_pos hq
  have ha : 0 < a := by positivity
  have hcas_pos : 0 ≤ qouCasimir q n := le_of_lt (qouCasimir_pos hq n)
  have hcas_quad := qouCasimir_quad_lower hq n
  have hs_cas : -s * qouCasimir q n ≤ -a * ((n : ℝ) + 1) ^ 2 := by
    have h1 : -s * qouCasimir q n ≤ -lo * qouCasimir q n := by nlinarith
    have h2 : -lo * qouCasimir q n ≤ -lo * ((qHalfInt q 1) ^ 2 * ((n : ℝ) + 1) ^ 2) := by
      nlinarith
    linarith [show -lo * ((qHalfInt q 1) ^ 2 * ((n : ℝ) + 1) ^ 2) =
      -a * ((n : ℝ) + 1) ^ 2 by ring]
  have hsq_complete :
      ((n : ℝ) + 2) * b + (-s * qouCasimir q n) ≤ B - (n : ℝ) := by
    have hdiff :
        0 ≤ (B - (n : ℝ)) - (((n : ℝ) + 2) * b - a * ((n : ℝ) + 1) ^ 2) := by
      have h4a : 4 * a ≠ 0 := ne_of_gt (by positivity)
      have hid : (B - (n : ℝ)) - (((n : ℝ) + 2) * b - a * ((n : ℝ) + 1) ^ 2) =
          (2 * a * ((n : ℝ) + 1) - (b + 1)) ^ 2 / (4 * a) := by
        dsimp [B]
        field_simp
        ring
      rw [hid]
      positivity
    linarith
  have hdim := qouPunctureQDim_le_exp hq n
  have hd : 0 < q - q⁻¹ := q_sub_inv_pos hq
  calc qouPunctureQDim q n * Real.exp (-s * qouCasimir q n)
      ≤ (Real.exp (((n : ℝ) + 2) * b) / (q - q⁻¹)) * Real.exp (-s * qouCasimir q n) :=
        mul_le_mul_of_nonneg_right hdim (le_of_lt (Real.exp_pos _))
    _ = Real.exp (((n : ℝ) + 2) * b + (-s * qouCasimir q n)) / (q - q⁻¹) := by
        rw [div_mul_eq_mul_div, ← Real.exp_add]
    _ ≤ Real.exp (B - (n : ℝ)) / (q - q⁻¹) :=
        div_le_div_of_nonneg_right (Real.exp_le_exp.mpr hsq_complete) (le_of_lt hd)
    _ = (Real.exp B / (q - q⁻¹)) * (Real.exp (-1)) ^ n := by
        have hexp : Real.exp (B - (n : ℝ)) = Real.exp B * (Real.exp (-1)) ^ n := by
          rw [sub_eq_add_neg, Real.exp_add, ← Real.exp_nat_mul]
          ring_nf
        rw [hexp, mul_div_right_comm]
    _ = qouMajorant q lo n := rfl

/-- Summability of the QOU puncture partition series for every `q > 1` and `s > 0`. -/
theorem Z1_qou_summable {q s : ℝ} (hq : 1 < q) (hs : 0 < s) :
    Summable (fun n => qouPunctureQDim q n * Real.exp (-s * qouCasimir q n)) :=
  Summable.of_nonneg_of_le
    (fun n => mul_nonneg (le_of_lt (qouPunctureQDim_pos hq n)) (le_of_lt (Real.exp_pos _)))
    (fun n => qouTerm_le_majorant hq hs le_rfl n)
    (qouMajorant_summable q s)

/-- Continuity of `Z₁` for QOU puncture data on every compact window `[lo, hi] ⊂ (0, ∞)`. -/
theorem Z1_qou_continuousOn {q lo hi : ℝ} (hq : 1 < q) (hlo : 0 < lo) :
    ContinuousOn (Z1 (qouPunctureQDim q) (qouCasimir q)) (Set.Icc lo hi) := by
  refine continuousOn_tsum
    (fun n => (by continuity : Continuous fun s : ℝ =>
      qouPunctureQDim q n * Real.exp (-s * qouCasimir q n)).continuousOn)
    (qouMajorant_summable q lo) (fun n s hs => ?_)
  have hnn : 0 ≤ qouPunctureQDim q n * Real.exp (-s * qouCasimir q n) :=
    mul_nonneg (le_of_lt (qouPunctureQDim_pos hq n)) (le_of_lt (Real.exp_pos _))
  rw [Real.norm_of_nonneg hnn]
  exact qouTerm_le_majorant hq hlo hs.1 n

/-- Strict antitonicity of `Z₁` for QOU puncture data across all `(0, ∞)`. -/
theorem Z1_qou_strictAnti_pos {q s t : ℝ} (hq : 1 < q) (hs : 0 < s) (hst : s < t) :
    Z1 (qouPunctureQDim q) (qouCasimir q) t <
      Z1 (qouPunctureQDim q) (qouCasimir q) s := by
  have ht : 0 < t := lt_trans hs hst
  refine Summable.tsum_lt_tsum (i := 0) (fun n => ?_) ?_
    (Z1_qou_summable hq ht) (Z1_qou_summable hq hs)
  · have hcas : 0 < qouCasimir q n := qouCasimir_pos hq n
    have hexp : Real.exp (-t * qouCasimir q n) ≤ Real.exp (-s * qouCasimir q n) :=
      Real.exp_le_exp.mpr (by nlinarith)
    exact mul_le_mul_of_nonneg_left hexp (le_of_lt (qouPunctureQDim_pos hq n))
  · have hcas0 : 0 < qouCasimir q 0 := qouCasimir_pos hq 0
    have hexp0 : Real.exp (-t * qouCasimir q 0) < Real.exp (-s * qouCasimir q 0) :=
      Real.exp_lt_exp.mpr (by nlinarith)
    exact mul_lt_mul_of_pos_left hexp0 (qouPunctureQDim_pos hq 0)

/-- Explicit positive lower bracket `lo > 0` where `1 < Z₁(lo)` for QOU data (`q > 1`). -/
noncomputable def qouPoleLo (q : ℝ) : ℝ :=
  Real.log (q + q⁻¹) / (2 * qouCasimir q 0)

/-- Explicit upper bracket `hi > lo` where `Z₁(hi) < 1` for QOU data (`q > 1`). -/
noncomputable def qouPoleHi (q : ℝ) : ℝ :=
  max (qouPoleLo q + 1)
    ((2 * Real.log q + Real.log (1 + 2 / (q - q⁻¹))) / (qHalfInt q 1) ^ 2)

theorem qouPoleLo_pos {q : ℝ} (hq : 1 < q) : 0 < qouPoleLo q := by
  unfold qouPoleLo
  have h2 : 2 < q + q⁻¹ := by
    have := two_lt_qouPunctureQDim_zero hq
    rwa [qouPunctureQDim_zero hq] at this
  have hlog : 0 < Real.log (q + q⁻¹) := Real.log_pos (by linarith)
  have hcas : 0 < 2 * qouCasimir q 0 := mul_pos (by norm_num) (qouCasimir_pos hq 0)
  exact div_pos hlog hcas

theorem qouPole_Z1_super {q : ℝ} (hq : 1 < q) :
    1 < Z1 (qouPunctureQDim q) (qouCasimir q) (qouPoleLo q) := by
  have hlo : 0 < qouPoleLo q := qouPoleLo_pos hq
  have hterm0 : qouPunctureQDim q 0 * Real.exp (-qouPoleLo q * qouCasimir q 0) ≤
      Z1 (qouPunctureQDim q) (qouCasimir q) (qouPoleLo q) :=
    (Z1_qou_summable hq hlo).le_tsum 0 (fun j _ =>
      mul_nonneg (le_of_lt (qouPunctureQDim_pos hq j)) (le_of_lt (Real.exp_pos _)))
  have h2 : 2 < q + q⁻¹ := by
    have := two_lt_qouPunctureQDim_zero hq
    rwa [qouPunctureQDim_zero hq] at this
  have hqp_pos : 0 < q + q⁻¹ := by linarith
  have hlog : 0 < Real.log (q + q⁻¹) := Real.log_pos (by linarith)
  have hcas0 : qouCasimir q 0 ≠ 0 := ne_of_gt (qouCasimir_pos hq 0)
  have hexp_arg : -qouPoleLo q * qouCasimir q 0 = -Real.log (q + q⁻¹) / 2 := by
    unfold qouPoleLo
    field_simp
  have hexp_gt : (q + q⁻¹)⁻¹ < Real.exp (-qouPoleLo q * qouCasimir q 0) := by
    rw [hexp_arg, ← Real.exp_log hqp_pos, ← Real.exp_neg, Real.exp_log hqp_pos]
    exact Real.exp_lt_exp.mpr (by linarith)
  have hmul : 1 < (q + q⁻¹) * Real.exp (-qouPoleLo q * qouCasimir q 0) := by
    calc (1 : ℝ) = (q + q⁻¹) * (q + q⁻¹)⁻¹ := (mul_inv_cancel₀ (ne_of_gt hqp_pos)).symm
      _ < (q + q⁻¹) * Real.exp (-qouPoleLo q * qouCasimir q 0) :=
          mul_lt_mul_of_pos_left hexp_gt hqp_pos
  rw [qouPunctureQDim_zero hq] at hterm0
  linarith

theorem qouPole_Z1_sub {q : ℝ} (hq : 1 < q) :
    Z1 (qouPunctureQDim q) (qouCasimir q) (qouPoleHi q) < 1 := by
  set d : ℝ := q - q⁻¹
  set M : ℝ := Real.log (1 + 2 / d)
  set c₀ : ℝ := (qHalfInt q 1) ^ 2
  have hd : 0 < d := q_sub_inv_pos hq
  have hc1 : 0 < qHalfInt q 1 := qHalfInt_one_pos hq
  have hc0 : 0 < c₀ := by positivity
  have h1d : 1 < 1 + 2 / d := by
    have : 0 < 2 / d := by positivity
    linarith
  have hM : 0 < M := Real.log_pos h1d
  have hlo : 0 < qouPoleLo q := qouPoleLo_pos hq
  have hhi_pos : 0 < qouPoleHi q :=
    lt_of_lt_of_le (by linarith) (le_max_left _ _)
  have hhi_bound : 2 * Real.log q + M ≤ qouPoleHi q * c₀ := by
    have hle : (2 * Real.log q + M) / c₀ ≤ qouPoleHi q := le_max_right _ _
    exact (div_le_iff₀ hc0).mp hle
  set r : ℝ := Real.exp (-M)
  have hr0 : 0 ≤ r := le_of_lt (Real.exp_pos _)
  have hr1 : r < 1 := Real.exp_lt_one_iff.mpr (by linarith)
  have hgeom : Summable (fun n : ℕ => (r / d) * r ^ n) :=
    (summable_geometric_of_lt_one hr0 hr1).mul_left (r / d)
  have hlogq : 0 < Real.log q := Real.log_pos hq
  have hterm : ∀ n : ℕ,
      qouPunctureQDim q n * Real.exp (-qouPoleHi q * qouCasimir q n) ≤
        (r / d) * r ^ n := by
    intro n
    have hn_lin : ((n : ℝ) + 1) ≤ ((n : ℝ) + 1) ^ 2 := by
      have : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
      nlinarith
    have hcas_lin : c₀ * ((n : ℝ) + 1) ≤ qouCasimir q n :=
      le_trans (mul_le_mul_of_nonneg_left hn_lin (le_of_lt hc0)) (qouCasimir_quad_lower hq n)
    have hexp_le :
        ((n : ℝ) + 2) * Real.log q + (-qouPoleHi q * qouCasimir q n) ≤
          -M * ((n : ℝ) + 1) := by
      have h2n : ((n : ℝ) + 2) * Real.log q ≤ 2 * ((n : ℝ) + 1) * Real.log q := by
        have : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
        nlinarith
      have hcas_neg : -qouPoleHi q * qouCasimir q n ≤
          -(qouPoleHi q * c₀) * ((n : ℝ) + 1) := by nlinarith
      have hhi_neg : -(qouPoleHi q * c₀) * ((n : ℝ) + 1) ≤
          -(2 * Real.log q + M) * ((n : ℝ) + 1) := by
        have : (0 : ℝ) ≤ (n : ℝ) + 1 := by positivity
        nlinarith
      linarith
    calc qouPunctureQDim q n * Real.exp (-qouPoleHi q * qouCasimir q n)
        ≤ (Real.exp (((n : ℝ) + 2) * Real.log q) / d) *
            Real.exp (-qouPoleHi q * qouCasimir q n) :=
          mul_le_mul_of_nonneg_right (qouPunctureQDim_le_exp hq n)
            (le_of_lt (Real.exp_pos _))
      _ = Real.exp (((n : ℝ) + 2) * Real.log q + (-qouPoleHi q * qouCasimir q n)) / d := by
          rw [div_mul_eq_mul_div, ← Real.exp_add]
      _ ≤ Real.exp (-M * ((n : ℝ) + 1)) / d :=
          div_le_div_of_nonneg_right (Real.exp_le_exp.mpr hexp_le) (le_of_lt hd)
      _ = (r / d) * r ^ n := by
          have hrpow : Real.exp (-M * ((n : ℝ) + 1)) = r * r ^ n := by
            dsimp [r]
            rw [show -M * ((n : ℝ) + 1) = -M + (n : ℝ) * (-M) by ring,
                Real.exp_add, Real.exp_nat_mul]
          rw [hrpow, mul_div_right_comm]
  have htsum_le :
      Z1 (qouPunctureQDim q) (qouCasimir q) (qouPoleHi q) ≤
        ∑' n : ℕ, (r / d) * r ^ n :=
    Summable.tsum_le_tsum hterm (Z1_qou_summable hq hhi_pos) hgeom
  have hval : (∑' n : ℕ, (r / d) * r ^ n) = (1 / 2 : ℝ) := by
    rw [tsum_mul_left, tsum_geometric_of_lt_one hr0 hr1]
    have hr_val : r = d / (d + 2) := by
      dsimp [r, M]
      rw [Real.exp_neg, Real.exp_log (by linarith : 0 < 1 + 2 / d)]
      field_simp
    rw [hr_val]
    have hd2 : d + 2 ≠ 0 := ne_of_gt (by linarith)
    have hd_ne : d ≠ 0 := ne_of_gt hd
    field_simp
    ring
  linarith

/-- **Unconditional QOU instance of `LQGEntropyQDimPartitionPole`** for every `q > 1`. -/
theorem qou_lqg_partition_pole_instance {q : ℝ} (hq : 1 < q) :
    LQGEntropyQDimPartitionPole (qouPunctureQDim q) (qouCasimir q)
      (qouPoleLo q) (qouPoleHi q) where
  lo_lt_hi := lt_of_lt_of_le (by linarith) (le_max_left _ _)
  Z1_continuous := Z1_qou_continuousOn hq (qouPoleLo_pos hq)
  Z1_strictAnti := fun a ha b _ hab =>
    Z1_qou_strictAnti_pos hq (lt_of_lt_of_le (qouPoleLo_pos hq) ha.1) hab
  Z1_super := qouPole_Z1_super hq
  Z1_sub := qouPole_Z1_sub hq

/-- **Unconditional resolution of the `LQGEntropyQDimPartitionPole` hypotheses**
    for genuine QOU quantum-group data `([2j + 1]_q, [j]_q[j + 1]_q)` over all
    non-trivial punctures `j ∈ ½ℤ_{>0}` and every substrate parameter `q > 1`. -/
theorem qou_lqg_partition_pole_holds (q : ℝ) (hq : 1 < q) :
    ∃ lo hi : ℝ, 0 < lo ∧
      LQGEntropyQDimPartitionPole (qouPunctureQDim q) (qouCasimir q) lo hi :=
  ⟨qouPoleLo q, qouPoleHi q, qouPoleLo_pos hq, qou_lqg_partition_pole_instance hq⟩

/-- **Global existence and uniqueness on `(0, ∞)`:** for every `q > 1`, there is a
    unique positive critical parameter `s⋆ > 0` solving `Z₁(s⋆) = 1` for the QOU
    puncture partition function, determining a unique positive Immirzi parameter
    `γ = s⋆ / (2π) > 0`. -/
theorem qou_exists_unique_positive_critical (q : ℝ) (hq : 1 < q) :
    ∃! s : ℝ, 0 < s ∧ Z1 (qouPunctureQDim q) (qouCasimir q) s = 1 := by
  letI : LQGEntropyQDimPartitionPole (qouPunctureQDim q) (qouCasimir q)
      (qouPoleLo q) (qouPoleHi q) := qou_lqg_partition_pole_instance hq
  obtain ⟨sStar, ⟨hsIcc, hval⟩, _⟩ :=
    LQGEntropyQDimPartitionPole.exists_unique_critical
      (qdim := qouPunctureQDim q) (casimir := qouCasimir q)
      (lo := qouPoleLo q) (hi := qouPoleHi q)
  have hsPos : 0 < sStar := lt_of_lt_of_le (qouPoleLo_pos hq) hsIcc.1
  refine ⟨sStar, ⟨hsPos, hval⟩, ?_⟩
  rintro t ⟨htPos, htVal⟩
  rcases lt_trichotomy t sStar with hlt | rfl | hgt
  · exfalso
    have := Z1_qou_strictAnti_pos hq htPos hlt
    linarith
  · rfl
  · exfalso
    have := Z1_qou_strictAnti_pos hq hsPos hgt
    linarith

end QOU.GravitySpacetime
