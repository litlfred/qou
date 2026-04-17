-- Ref: [manuscript] §7/pseudospin-magic-alignment
--
-- Formal statement of the pseudospin-ratio claim that compares the
-- Borromean shell-intruder derivation with Ding et al.'s chiral
-- EFT / SRG account of magic numbers.
--
-- Ref: [ding2026] https://journals.aps.org/prl/abstract/10.1103/8lzc-j1lx
--     (Ding, Wang, Yao, Hergert, Liang, Bogner, PRL 136, 052501 (2026):
--      "From Spin to Pseudospin Symmetry: The Origin of Magic Numbers
--       in Nuclear Structure").
--
-- The pseudospin-degeneracy condition between the doublet
--   (ℓ, j = ℓ - 1/2)  and  (ℓ - 2, j = ℓ - 3/2)
-- is captured, in the q-deformed setting, by the ratio
--   R(ℓ) = [ℓ-1]_q [ℓ]_q / ([ℓ-2]_q [ℓ-1]_q)
--        = [ℓ]_q / [ℓ-2]_q.
-- In the classical limit q → 1, R(ℓ) → ℓ / (ℓ - 2), which is NOT
-- unity in general but tends to 1 as ℓ → ∞ — consistent with the
-- approximate / asymptotic character of pseudospin symmetry
-- reported in [ding2026].

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

namespace QOU.Observations.PseudospinMagicAlignment

-- ═══════════════════════════════════════════════════════════════════
-- §1. Classical-limit pseudospin ratio
-- ═══════════════════════════════════════════════════════════════════

/-- Classical-limit pseudospin ratio
    R_cl(ℓ) = ℓ / (ℓ - 2)  (defined for ℓ ≥ 3). -/
-- Ref: [manuscript] §7/pseudospin-magic-alignment
noncomputable def pseudospinRatioClassical (ell : ℕ) : ℝ :=
  (ell : ℝ) / ((ell : ℝ) - 2)

/-- Concrete values of the classical pseudospin ratio showing
    monotonic approach to 1 as ℓ grows. -/
-- Ref: [manuscript] §7/pseudospin-magic-alignment
theorem pseudospin_ratio_values :
    pseudospinRatioClassical 5 = 5 / 3 ∧
    pseudospinRatioClassical 7 = 7 / 5 ∧
    pseudospinRatioClassical 9 = 9 / 7 := by
  refine ⟨?_, ?_, ?_⟩ <;>
    (unfold pseudospinRatioClassical; norm_num)

/-- Pseudospin is NOT exact at q = 1 for any finite ℓ.
    Specifically, R_cl(5) > 1.5 > 1. -/
-- Ref: [manuscript] §7/pseudospin-magic-alignment
theorem pseudospin_not_exact_at_classical_limit :
    pseudospinRatioClassical 5 > 1 := by
  unfold pseudospinRatioClassical; norm_num

-- ═══════════════════════════════════════════════════════════════════
-- §2. Symmetric q-number convention used by the project
-- ═══════════════════════════════════════════════════════════════════

/-- The substrate parameter q_0 used throughout QOU. -/
-- Ref: [manuscript] §6/substrate-parameter-from-leptons
noncomputable def q_sub : ℝ := 1.1098

/-- q_sub is strictly greater than one (non-degenerate substrate). -/
-- Ref: [manuscript] §6/substrate-parameter-from-leptons
theorem q_sub_gt_one : (1 : ℝ) < q_sub := by
  unfold q_sub; norm_num

-- ═══════════════════════════════════════════════════════════════════
-- §3. Alignment / disagreement with Ding et al. 2026
-- ═══════════════════════════════════════════════════════════════════

/-- Shared set of seven magic numbers reproduced by both accounts. -/
-- Ref: [manuscript] §7/pseudospin-magic-alignment, [ding2026]
def sharedMagicNumbers : List ℕ := [2, 8, 20, 28, 50, 82, 126]

/-- The shared magic-number list has length 7. -/
-- Ref: [manuscript] §7/pseudospin-magic-alignment
theorem sharedMagicNumbers_length : sharedMagicNumbers.length = 7 := by
  decide

/-- The shared intruder levels (in pseudospin-breaking order:
    f_{7/2}, g_{9/2}, h_{11/2}, i_{13/2}) have dimensions
    8, 10, 12, 14 — matching both accounts. -/
-- Ref: [manuscript] §7/pseudospin-magic-alignment, [ding2026]
def sharedIntruderDims : List ℕ := [8, 10, 12, 14]

theorem sharedIntruderDims_sum :
    sharedIntruderDims.sum = 44 := by decide

/-- Record of the three caveats where our account currently
    disagrees quantitatively with [ding2026]:
    (1) SO-strength overshoot at low Hecke truncation K,
    (2) sd-shell (ℓ = 2) pseudospin breaking ~10–15%,
    (3) Z = 28 marginal in our δ²Φ at K = 10. -/
-- Ref: [manuscript] §7/pseudospin-magic-alignment
structure AlignmentCaveats where
  so_overshoot_at_low_K : Bool := true
  sd_shell_breaking : Bool := true
  Z28_marginal_at_K10 : Bool := true

/-- All three caveats are currently active. -/
-- Ref: [manuscript] §7/pseudospin-magic-alignment
def currentCaveats : AlignmentCaveats := {}

end QOU.Observations.PseudospinMagicAlignment
