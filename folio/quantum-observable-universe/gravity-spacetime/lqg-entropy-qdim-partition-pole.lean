import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic

/-!
# Horizon entropy as the `q`-dimension partition-function pole

§3b-cond axiomatisation of `conj:lqg-entropy-qdim-partition-pole`.

The block recasts the LQG horizon-entropy state count algebraically: the
per-puncture `q`-dimension partition function

  `Z₁(s) = Σ_{j ∈ ½ℕ} [2j+1]_q · exp(-s · τ(C_q(V_j)))`

(indexed here by `n = 2j`) has a critical value `s⋆` with `Z₁(s⋆) = 1`,
the horizon generating function `Σ_n Z₁ⁿ = (1 - Z₁)⁻¹` poles there, and
`γ = s⋆ / 2π` is the Barbero–Immirzi parameter.

**Replaces an empty carrier.** This file previously held

    class LQGEntropyQDimPartitionPole where
      -- axiomatisation stub

with **zero fields** — a `proof-no-empty-prop-carrier` critical under
AGENTS.md §3b-tax: any `instance := ⟨⟩` discharged it, so a downstream
`[LQGEntropyQDimPartitionPole]` hypothesis constrained nothing.

**Non-degenerate per §3b-cond item 5.** The class carries *analytic
hypotheses* on `Z₁` — continuity, strict antitonicity, and the crossing
of `1` between the window endpoints. It does **not** carry the pole.
`exists_unique_critical` **derives** existence and uniqueness of `s⋆`
from them, by the intermediate value theorem plus injectivity of a
strictly antitone function. The open content of the conjecture is that
the actual LQG `q`-dimension data satisfies those hypotheses; no such
instance is provided.

**Window as parameters, not a fixed interval.** `lo`/`hi` are class
parameters rather than a hardcoded `[0,1]`. An earlier draft fixed the
window to `[0,1]`, which compiles but silently excludes the physically
expected value: the standard Immirzi parameter `γ ≈ 0.237` corresponds
to `s⋆ = 2πγ ≈ 1.49 > 1`. An instance must state its own window.

**Base ring (§7c).** `ℝ` throughout, and deliberately: this is the
archimedean layer — `Real.exp`, the ordering used by IVT and by
`StrictAntiOn`, and `Real.pi` in the Immirzi normalisation.

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

end QOU.GravitySpacetime
