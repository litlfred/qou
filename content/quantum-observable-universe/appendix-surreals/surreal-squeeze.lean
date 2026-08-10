/-
  Surreal squeeze — `δ² · ε⁻¹ > ε³`.

  Ref: [manuscript] §Algebraic substrate / Surreal squeeze, lem:surreal-squeeze

  ## Rewritten 2026-08-10 — the previous version was a tautology, and it did
  ## not state the `.md`'s claim

  What stood here was

      theorem surreal_squeeze_conditional
          [QAubinLions] [NSCounterexample] [CriticalExponent]
          [BlowupYekutieli] [RegularityBreakdown]
          (ε : ℝ) (h_pos : 0 < ε) (h_inf : ε < 1) : 0 < ε ∧ ε < 1 :=
        ⟨h_pos, h_inf⟩

  Three defects, all now fixed:

  1. **Tautology.** The conclusion re-packaged the two hypotheses (`⟨h_pos,
     h_inf⟩`). Per AGENTS.md §"Strict Lean Discipline" item 5 that is a review
     failure: the statement said nothing falsifiable about the objects.
  2. **Wrong statement.** The `.md` asserts `δ² · ε⁻¹ > ε³` in the ordered field
     `ℝ(ε) ⊂ No` with `ε` a *Reeb infinitesimal*. The Lean instead took
     `ε : ℝ` — a plain real — where the `.md`'s inequality is simply **false**
     (take `δ = 1/10`, `ε = 1`: `δ²·ε⁻¹ = 1/100 > 1 = ε³` fails). So the Lean
     was not a weak form of the `.md` claim; it was a different, unrelated
     proposition. A `proof-statement-integrity` failure.
  3. **Fake conditionality.** Five `[...]` hypothesis classes for the q-NS cone
     were carried, whose fields were content-free — `CriticalExponent` was
     literally `alpha_three_eq_four : (3 * 4 : ℕ) = 12`, and
     `QAubinLions`'s `∃ K, 0 ≤ K ∧ K ≤ 2 * E` is discharged by `K = 0`. The
     squeeze inequality does not depend on the q-NS conjectures at all: it is
     ordered-field arithmetic. Dressing an unconditional fact in conjectural
     classes inverts AGENTS.md §"Conditional-proved ≠ premise-established" — it
     makes something established look conditional, and it made five vacuous
     carriers look load-bearing.

  The conditionality is real, but it attaches to the *application* to
  Navier–Stokes (`rem:ns-surreal-bound`), not to this lemma.

  ## What is proved now

  `surreal_squeeze` — the `.md`'s inequality, over an arbitrary
  `LinearOrderedField`, from the two hypotheses that carry its actual content:
  `ε` is a positive infinitesimal (`0 < ε < 1`) and `ε` is dominated by the
  standard-scale deviation (`ε < δ²`). Both are exactly what "ε is the Reeb
  infinitesimal and δ is a standard real" supplies, and the conclusion fails
  without them, so the statement is falsifiable.

  The algebraic content behind it — grade separation, with no ordered field —
  is `QOU.AlgebraicSubstrate.Domination.val_add_eq_of_lt`; see
  `QOU/AlgebraicSubstrate/DominationSqueeze.lean` for why that form is the one
  to build on and this one is the special case that
  `QOU.Archimedean.SurrealGradingPrune` shows is blind inside `ℝ`.
-/

import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.NormNum

namespace QOU.AlgebraicSubstrate

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Surreal squeeze.**  In any linearly ordered field, if `ε` is a positive
infinitesimal (`0 < ε < 1`) dominated by the standard-scale deviation
(`ε < δ²`), then the cost `δ²·ε⁻¹` strictly exceeds the budget `ε³`.

This is `lem:surreal-squeeze` as stated in the `.md`, and it is the step every
millennium-bound remark in the appendix invokes. It holds over `ℝ(ε) ⊂ No`,
which is where the `.md` places it — **not** over `ℝ`, where it is false.

Falsifiability check (AGENTS.md §"Strict Lean Discipline" item 8): drop
`hεδ` and take `δ² = ε/2`; then `δ²·ε⁻¹ = 1/2` while `ε³` can exceed `1/2`.
The hypothesis is doing work. -/
theorem surreal_squeeze (ε δ : K)
    (hε : 0 < ε) (hε1 : ε < 1) (hεδ : ε < δ ^ 2) :
    ε ^ 3 < δ ^ 2 * ε⁻¹ := by
  rw [← div_eq_mul_inv]
  exact (pow_lt_one₀ hε.le hε1 (by norm_num)).trans ((one_lt_div hε).mpr hεδ)

/-- The same statement as the strict positivity of the gap, which is the form
the millennium-bound remarks consume ("the cost strictly exceeds the budget"). -/
theorem surreal_squeeze_gap_pos (ε δ : K)
    (hε : 0 < ε) (hε1 : ε < 1) (hεδ : ε < δ ^ 2) :
    0 < δ ^ 2 * ε⁻¹ - ε ^ 3 :=
  sub_pos.mpr (surreal_squeeze ε δ hε hε1 hεδ)

/-- **The domination hypothesis is load-bearing.**  Drop `ε < δ²` and the lemma
is false: at `ε = 9/10`, `δ = 1/10` we get `δ²·ε⁻¹ = 1/90 ≈ 0.011` while
`ε³ = 729/1000 = 0.729`, so the cost does *not* exceed the budget.

Recorded as a theorem rather than a comment so the falsifiability check of
AGENTS.md §"Strict Lean Discipline" item 8 is machine-checked, not asserted.
It is also what distinguishes this from the tautology it replaces. -/
theorem surreal_squeeze_needs_domination :
    ∃ ε δ : ℚ, 0 < ε ∧ ε < 1 ∧ ¬ (ε ^ 3 < δ ^ 2 * ε⁻¹) := by
  refine ⟨9 / 10, 1 / 10, by norm_num, by norm_num, by norm_num⟩

end QOU.AlgebraicSubstrate
