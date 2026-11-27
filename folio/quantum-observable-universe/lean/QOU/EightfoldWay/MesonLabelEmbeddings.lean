/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/

import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import QOU.EightfoldWay.MesonRatioSelectionStatus

/-!
# Where the quark labels enter, and why no tested embedding gives `m_K² / m_π² = 12`

Status module for bean `qou-mk34` (epic `qou-myts`, compute accuracy C5).
Mathematics only: no measured number appears in any statement below.

The pion carries quark labels `(3, 3)` and the kaon `(3, 5)`. The corpus reads the strong
core of `m_K² / m_π²` as `[3]_q [4]_q`, whose classical value is `12`.

1. `classical_ratio_ne_p34`: a polynomial reading `N / D` whose classical ratio is
   `N(1) = r · D(1)` with `r ≠ 12` cannot equal `[3]_q [4]_q` as an identity in `q`.
   This generalises `MesonRatioSelectionStatus.unit_ratio_reading_ne_p34` (the case `r = 1`).
2. The classical kaon-to-pion ratio for four ways of letting the labels enter:
   - labels as exponents of the clasp generators (the corpus definition): ratio `1`
     (`MesonRatioSelectionStatus.clasp_reading_pion_eq_kaon`);
   - labels as `sl₂` colour dimensions of the two strands, `n₁ n₂`: ratio `15 / 9 = 5 / 3`;
   - labels summed to a strand count `n₁ + n₂`: ratio `8 / 6 = 4 / 3`;
   - the Hecke-algebra dimension `(n₁ + n₂)!` on that strand count: ratio `8! / 6! = 56`.
   None is `12` (`label_embedding_ratios_ne_twelve`).
3. `half_sum_product_eq_twelve`: the half-sums `(n₁ + n₂) / 2` are `3` (pion) and `4` (kaon),
   so `12` does appear, but as the **product** `3 · 4` of a pion number and a kaon number,
   not as a kaon-to-pion ratio. Reading `m_K² / m_π²` as that product is the `sl₂` fusion
   reading `dim (V₃ ⊗ V₄)`, which the corpus already records as a post-hoc spin assignment.

4. `no_meson_total_ratio_twelve`: for any two mesons with labels in `{3, 5, 7}`, no ratio of
   label sums or label products is `12`.

**Scope.** This excludes the four embeddings listed (scope (a), not a structural exclusion of
every possible definition of `K` and `π`). The row stays labelled **Selected**.
-/

set_option autoImplicit false

namespace QOU.EightfoldWay
namespace MesonLabelEmbeddings

open Polynomial
open MesonRatioSelectionStatus (p34 p34_eval_one)

variable {K : Type*} [Field K]

/-- **A reading with classical ratio `r ≠ 12` is not `[3]_q [4]_q`.**
If `N(1) = r · D(1)`, `D(1) ≠ 0` and `r ≠ 12`, then `q⁵ N ≠ q⁵ [3]_q [4]_q · D`. -/
theorem classical_ratio_ne_p34 (r : K) (hr : r ≠ 12) (N D : K[X])
    (hND : N.eval 1 = r * D.eval 1) (hD : D.eval 1 ≠ 0) :
    X ^ 5 * N ≠ p34 K * D := by
  intro h
  have h1 := congrArg (eval 1) h
  rw [eval_mul, eval_mul, p34_eval_one, eval_pow, eval_X, one_pow, one_mul, hND] at h1
  have h0 : (r - 12) * D.eval 1 = 0 := by linear_combination h1
  rcases mul_eq_zero.mp h0 with h | h
  · exact hr (sub_eq_zero.mp h)
  · exact hD h

/-- Pion and kaon quark labels. -/
def pionLabels : ℕ × ℕ := (3, 3)
def kaonLabels : ℕ × ℕ := (3, 5)

/-- **The four classical ratios.** Colour dimensions `15 / 9`, strand counts `8 / 6`,
Hecke dimensions `8! / 6!`, and the exponent reading `1`: none is `12`. -/
theorem label_embedding_ratios_ne_twelve :
    ((kaonLabels.1 * kaonLabels.2 : ℕ) : ℚ) / (pionLabels.1 * pionLabels.2 : ℕ) = 5 / 3 ∧
      ((kaonLabels.1 + kaonLabels.2 : ℕ) : ℚ) / (pionLabels.1 + pionLabels.2 : ℕ) = 4 / 3 ∧
      ((kaonLabels.1 + kaonLabels.2).factorial : ℚ) / (pionLabels.1 + pionLabels.2).factorial
        = 56 ∧
      (5 / 3 : ℚ) ≠ 12 ∧ (4 / 3 : ℚ) ≠ 12 ∧ (56 : ℚ) ≠ 12 ∧ (1 : ℚ) ≠ 12 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    norm_num [kaonLabels, pionLabels, Nat.factorial]

/-- **Twelve appears only as a product.** The half-sums are `3` and `4`, and their product is
`12`; their kaon-to-pion ratio is `4 / 3`. -/
theorem half_sum_product_eq_twelve :
    (pionLabels.1 + pionLabels.2) / 2 = 3 ∧ (kaonLabels.1 + kaonLabels.2) / 2 = 4 ∧
      (pionLabels.1 + pionLabels.2) / 2 * ((kaonLabels.1 + kaonLabels.2) / 2) = 12 := by
  decide

/-- Labels allowed for a quark strand: `{3, 5, 7}` (the generation labels). -/
def IsGenLabel (n : ℕ) : Prop := n = 3 ∨ n = 5 ∨ n = 7

/-- **No ratio of meson totals is 12.** For any two mesons with quark labels in `{3, 5, 7}`,
neither the label sums nor the label products stand in ratio `12`: the largest sum ratio is
`14 / 6` and the largest product ratio is `49 / 9`. So `12` cannot be a kaon-to-pion
(or any meson-to-meson) ratio of label totals. -/
theorem no_meson_total_ratio_twelve (a b c d : ℕ)
    (ha : IsGenLabel a) (hb : IsGenLabel b) (hc : IsGenLabel c) (hd : IsGenLabel d) :
    a + b ≠ 12 * (c + d) ∧ a * b ≠ 12 * (c * d) := by
  unfold IsGenLabel at ha hb hc hd
  rcases ha with rfl | rfl | rfl <;> rcases hb with rfl | rfl | rfl <;>
    rcases hc with rfl | rfl | rfl <;> rcases hd with rfl | rfl | rfl <;>
    exact ⟨by norm_num, by norm_num⟩

end MesonLabelEmbeddings
end QOU.EightfoldWay
