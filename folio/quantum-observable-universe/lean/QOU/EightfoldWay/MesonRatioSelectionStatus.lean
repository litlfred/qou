/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/

import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import QOU.EightfoldWay.MesonThreeByFourCharacterization

/-!
# Why the `(3, 4)` reading of `m_K² / m_π²` stays a selection (`§7c` generic)

Status module for beans `qou-mk34` / `qou-5ipv` (epic `qou-myts`, compute accuracy C5).
Mathematics only: no measured number appears in any statement below.

The corpus reads the strong core of `m_K² / m_π²` as `[3]_q [4]_q`. The pair `(3, 4)` was found
by scanning `q`-integer products (`docs/audits/2026-11-20-mk-mpi-derivation-status.md`).
`MesonThreeByFourCharacterization` already shows that the gluon-clasp words of the pion
`(3, 3)` and the kaon `(3, 5)` collapse to the same element at `q = 1`. This file turns that
collapse into the statement the brief asks for, at the level of identities in `q`:

1. `p34` is `q⁵ [3]_q [4]_q` with negative powers cleared; `p34_eval_eq_qInt` ties it to
   `qIntBal`, and `p34_eval_one` gives its classical value `12`.
2. `clasp_reading_pion_eq_kaon`: for **every** function `f` on **every** monoid in which the
   two generators are involutions (the `q = 1` specialization `H₃(1) = K[S₃]`), `f` takes the
   same value on the pion and kaon clasp words.
3. `unit_ratio_reading_ne_p34`: no polynomial reading `N / D` whose value at `q = 1` is `1`
   can equal `[3]_q [4]_q` as an identity in `q` (needs only `(11 : K) ≠ 0`).
4. `claspHecke21_trace_ratio_ne_qInt34_at_one`: the concrete case, the `S^{(2,1)}` traces.

**Scope (what this does and does not exclude).** It excludes every reading of the ratio
as a ratio of values of the clasp words that is polynomial in `q` and specializes at `q = 1`
through `H₃(1)`. It does not exclude a reading that chooses a channel (for instance
`dim_q (V₂ ⊗ Sym²_q W₃*) = [3]_q [4]_q`, proved in `MesonThreeByFourCharacterization`):
such a reading is consistent, but the choice of channel is a premise, not a consequence of
the meson braid words. That premise is what keeps the row labelled **Selected**.
-/

set_option autoImplicit false

namespace QOU.EightfoldWay
namespace MesonRatioSelectionStatus

open Polynomial
open QOU.QInteger (qIntBal)
open QOU.Eightfold.HyperbolicMesonClaspAndDiquarkSplit (claspHecke21)
open MesonThreeByFourCharacterization
  (qIntBal_small_laurent involutive_odd_clasp_eq_sq claspHecke21_pion_eq_kaon_at_one)

variable {K : Type*} [Field K]

/-- `q⁵ · [3]_q [4]_q` as a polynomial: `(q⁴ + q² + 1)(q⁶ + q⁴ + q² + 1)`. -/
noncomputable def p34 (K : Type*) [Field K] : K[X] :=
  (X ^ 4 + X ^ 2 + 1) * (X ^ 6 + X ^ 4 + X ^ 2 + 1)

/-- The classical (`q = 1`) value of `[3]_q [4]_q` is `3 · 4 = 12`. -/
theorem p34_eval_one : (p34 K).eval 1 = 12 := by
  simp only [p34, eval_mul, eval_add, eval_pow, eval_X, eval_one]
  norm_num

/-- `p34` is `q⁵ [3]_q [4]_q` wherever the balanced `q`-integers are defined. -/
theorem p34_eval_eq_qInt (q : K) (hq : q ≠ 0) (hqdiff : q - q⁻¹ ≠ 0) :
    (p34 K).eval q = q ^ 5 * (qIntBal q 3 * qIntBal q 4) := by
  obtain ⟨-, -, h3, h4, -⟩ := qIntBal_small_laurent q hq hqdiff
  rw [h3, h4]
  simp only [p34, eval_mul, eval_add, eval_pow, eval_X, eval_one]
  field_simp

/-- **Every function of the clasp words agrees on pion and kaon at `q = 1`.**
For any monoid `A` with involutive generators `s₁, s₂` and any `f : A → B`, the pion clasp
word `s₁³ s₂³ s₁ s₂` and the kaon clasp word `s₁³ s₂⁵ s₁ s₂` have the same `f`-value. -/
theorem clasp_reading_pion_eq_kaon {A B : Type*} [Monoid A] (f : A → B)
    (s₁ s₂ : A) (hs1 : s₁ ^ 2 = 1) (hs2 : s₂ ^ 2 = 1) :
    f (s₁ ^ 3 * s₂ ^ 3 * s₁ * s₂) = f (s₁ ^ 3 * s₂ ^ 5 * s₁ * s₂) := by
  have hπ := involutive_odd_clasp_eq_sq s₁ s₂ hs1 hs2 1 1
  have hK := involutive_odd_clasp_eq_sq s₁ s₂ hs1 hs2 1 2
  norm_num at hπ hK
  rw [hπ, hK]

/-- **No unit-at-`q = 1` reading equals `[3]_q [4]_q` identically.**
If `N, D ∈ K[q]` satisfy `N(1) = D(1) ≠ 0` (as every ratio of values of the clasp words does,
by `clasp_reading_pion_eq_kaon`), then `q⁵ N ≠ q⁵ [3]_q [4]_q · D`, i.e. `N / D ≠ [3]_q [4]_q`
as an identity in `q`. Only `(11 : K) ≠ 0` is used (`12 - 1 = 11`). -/
theorem unit_ratio_reading_ne_p34 (h11 : (11 : K) ≠ 0) (N D : K[X])
    (hND : N.eval 1 = D.eval 1) (hD : D.eval 1 ≠ 0) :
    X ^ 5 * N ≠ p34 K * D := by
  intro h
  have h1 := congrArg (eval 1) h
  rw [eval_mul, eval_mul, p34_eval_one, eval_pow, eval_X, one_pow, one_mul, hND] at h1
  -- h1 : D(1) = 12 * D(1), so 11 * D(1) = 0
  have h0 : (11 : K) * D.eval 1 = 0 := by linear_combination -h1
  rcases mul_eq_zero.mp h0 with h | h
  · exact h11 h
  · exact hD h

/-- **The concrete case: the `S^{(2,1)}` clasp traces at `q = 1`.**
The kaon trace is not `[3]_1 [4]_1 = 12` times the pion trace (both traces are `-1`). -/
theorem claspHecke21_trace_ratio_ne_qInt34_at_one (h11 : (11 : K) ≠ 0) :
    (claspHecke21 (1 : K) 3 5).trace ≠ (p34 K).eval 1 * (claspHecke21 (1 : K) 3 3).trace := by
  obtain ⟨heq, htr⟩ := claspHecke21_pion_eq_kaon_at_one (K := K)
  rw [← heq, htr, p34_eval_one]
  intro h
  exact h11 (by linear_combination h)

end MesonRatioSelectionStatus
end QOU.EightfoldWay
