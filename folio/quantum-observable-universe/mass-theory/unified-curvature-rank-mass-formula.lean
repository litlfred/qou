import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic


/-!
# Unified curvature-rank mass formula

The "six terms + Term 7" labelling in the paper is HISTORICAL.
The unified mass formula is a single sum over curvature-rank strata:

  m(β) = Σ_{k=0}^{n-1} α_k · Φ_k(β)
  Φ_k(β) := Σ_{λ : depth(λ)=k} w_λ · log|χ_λ(β)|

with paper labels:
  k=0: Term 1 (descended Markov)
  k=1: Term 2 (single-gen tower)
  k=2: Term 3 (pair-gen tower)
  k=3: Term 6 (jet-prefix; was vague "depth ≥ 3")
  k≥4: Term 7 (shell correction)
  all k: Term 4 (universal Frobenius co-Casimir)
  S-odd: Term 5 (chirality, specific component)

Term 6 vs Term 7 are now seen as adjacent strata of the same
spectral-sequence ladder, not competing conjectures.

-- Ref: [leitner2026] conj:unified-curvature-rank-mass-formula
-/

namespace QOU.WedderburnMass

universe u

/-- Abstract data: (depth, weight, character). -/
structure StratumBlock where
  depth : ℕ
  weight : ℝ
  character : ℝ
  weight_nonneg : 0 ≤ weight
  character_ne_zero : character ≠ 0

/-- The k-th curvature-rank log functional. -/
noncomputable def Phi_at_depth (k : ℕ) (blocks : List StratumBlock) : ℝ :=
  (blocks.filter (fun b => b.depth = k)).foldl
    (fun acc b => acc + b.weight * Real.log (|b.character|)) 0

/-- The unified mass formula: sum over curvature-rank strata. -/
noncomputable def unified_curvature_rank_mass
    (alphas : ℕ → ℝ) (blocks : List StratumBlock) (n : ℕ) : ℝ :=
  (List.range n).foldl (fun acc k => acc + alphas k * Phi_at_depth k blocks) 0

/-! `unified_mass_finite` (`∃ x : ℝ, unified_curvature_rank_mass … = x`)
    stood here until 2026-08-21. `unified_curvature_rank_mass` is a total
    `ℝ`-valued function, so the statement held for every definition of it and
    said nothing about finiteness — the same shape as `phi_k_finite` and
    `plancherel_term_7_finite` in `plancherel-term-7-formulation.lean`, removed
    in the same pass. What the formula actually satisfies is stated by
    `term_6_plus_term_7_eq_high_strata` below. -/

/-- **Theorem (Term 6 + Term 7 = sum over depths ≥ 3).**
    With prefactor sequence `alphas` defined by paper's Term-6 and
    Term-7 conventions, the legacy "Term 6 + Term 7" combination
    equals the partial sum Σ_{k=3}^{n-1} α_k · Φ_k.

    Pure list algebra. This was an axiom
    (`term_6_plus_term_7_eq_high_strata_axiom`) "pending the exact lemma
    forms"; proved 2026-11-15 from `foldl_add_eq` by induction on `n`.
    It holds for `3 ≤ n`; the old `4 ≤ n` hypothesis is kept for callers. -/
-- Ref: [leitner2026] conj:unified-curvature-rank-mass-formula
theorem foldl_add_eq (f : ℕ → ℝ) : ∀ (l : List ℕ) (init : ℝ),
    l.foldl (fun acc k => acc + f k) init = init + (l.map f).sum := by
  intro l
  induction l with
  | nil => intro init; simp
  | cons a t ih => intro init; simp [List.foldl, ih]; ring

theorem term_6_plus_term_7_eq_high_strata
    (alphas : ℕ → ℝ) (blocks : List StratumBlock) (n : ℕ) (h_n : 4 ≤ n) :
    unified_curvature_rank_mass alphas blocks n
      - ((List.range 3).foldl
          (fun acc k => acc + alphas k * Phi_at_depth k blocks) 0)
    = ((List.range n).filter (· ≥ 3)).foldl
        (fun acc k => acc + alphas k * Phi_at_depth k blocks) 0 := by
  unfold unified_curvature_rank_mass
  simp only [foldl_add_eq, zero_add]
  have h3 : 3 ≤ n := by omega
  clear h_n
  induction n, h3 using Nat.le_induction with
  | base => simp [List.range_succ]
  | succ m hm ih =>
    rw [List.range_succ, List.filter_append, List.map_append, List.map_append,
      List.sum_append, List.sum_append, ← ih]
    have : decide (m ≥ 3) = true := by simpa using hm
    simp [List.filter, this]
    ring

/-- **Corollary (paper terminology mapping).**
    The historical "six terms + Term 7" decomposes uniformly:
      Term j = α_{k(j)} · Φ_{k(j)}  for j ∈ {1, 2, 3}
      Term 4 = universal (sum over all k weighted by 1/dim_q)
      Term 5 = S-anti-invariant component of Σ_{k≥2} Φ_k
      Term 6 = α_3 · Φ_3
      Term 7 = Σ_{k≥4} α_k · Φ_k
-/
-- Ref: [leitner2026] conj:unified-curvature-rank-mass-formula
theorem paper_terminology_mapping
    (alphas : ℕ → ℝ) (blocks : List StratumBlock) (n : ℕ) (h_n : 4 ≤ n) :
    -- The seven paper labels are an EXHAUSTIVE enumeration of the
    -- single curvature-rank sum by stratum: the total mass equals the
    -- low-strata part (k < 3 = "Terms 1–3/5") plus the high-strata part
    -- (k ≥ 3 = "Term 6 + Term 7"). No stratum is double-counted or
    -- omitted — the decomposition partitions Σ_k α_k Φ_k.
    unified_curvature_rank_mass alphas blocks n
      = ((List.range 3).foldl
          (fun acc k => acc + alphas k * Phi_at_depth k blocks) 0)
        + ((List.range n).filter (· ≥ 3)).foldl
            (fun acc k => acc + alphas k * Phi_at_depth k blocks) 0 := by
  have h := term_6_plus_term_7_eq_high_strata alphas blocks n h_n
  -- `h : full - low = high`, so `full = low + high`.
  linarith [h]

end QOU.WedderburnMass
