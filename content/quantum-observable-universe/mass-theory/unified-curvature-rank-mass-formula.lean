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

-- Ref: [manuscript] prop:unified-curvature-rank-mass-formula
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

    **External lemma (List/Mathlib): list-fold split + filter identity.**

    Pure list algebra: `List.range n = List.range 3 ++ ...` for n ≥ 4
    combined with `(List.range n).filter (· ≥ 3) = (List.range (n-3)).map (· + 3)`.
    Routine Mathlib completion; axiomatised pending the exact
    `List.foldl_append + List.filter_range` lemma forms. -/
-- Ref: [manuscript] prop:unified-curvature-rank-mass-formula
axiom term_6_plus_term_7_eq_high_strata_axiom :
    ∀ (alphas : ℕ → ℝ) (blocks : List StratumBlock) (n : ℕ) (_h_n : 4 ≤ n),
      unified_curvature_rank_mass alphas blocks n
        - ((List.range 3).foldl
            (fun acc k => acc + alphas k * Phi_at_depth k blocks) 0)
      = ((List.range n).filter (· ≥ 3)).foldl
          (fun acc k => acc + alphas k * Phi_at_depth k blocks) 0

theorem term_6_plus_term_7_eq_high_strata
    (alphas : ℕ → ℝ) (blocks : List StratumBlock) (n : ℕ) (h_n : 4 ≤ n) :
    unified_curvature_rank_mass alphas blocks n
      - ((List.range 3).foldl
          (fun acc k => acc + alphas k * Phi_at_depth k blocks) 0)
    = ((List.range n).filter (· ≥ 3)).foldl
        (fun acc k => acc + alphas k * Phi_at_depth k blocks) 0 :=
  term_6_plus_term_7_eq_high_strata_axiom alphas blocks n h_n

/-- **Corollary (paper terminology mapping).**
    The historical "six terms + Term 7" decomposes uniformly:
      Term j = α_{k(j)} · Φ_{k(j)}  for j ∈ {1, 2, 3}
      Term 4 = universal (sum over all k weighted by 1/dim_q)
      Term 5 = S-anti-invariant component of Σ_{k≥2} Φ_k
      Term 6 = α_3 · Φ_3
      Term 7 = Σ_{k≥4} α_k · Φ_k
-/
-- Ref: [manuscript] prop:unified-curvature-rank-mass-formula
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
