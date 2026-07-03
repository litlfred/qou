/-
  Borromean trace-convention split: convention D ≠ convention C, exactly.

  Two Markov-trace conventions evaluate the Borromean braid
  `β_Bor = (σ₁σ₂⁻¹)³` on `H_3(q)` to DIFFERENT values:

  * **Convention D** — the Borromean single-pipeline / `BorromeanMarkovTrace`
    closed form `tr_D = (4 + h² − 3h⁴ − h⁶)/(h² + 4)`, `h = q − q⁻¹`, which
    PROBE 4 (PR #3200) identified as the SU(2)/Temperley–Lieb (Jones)
    Markov decomposition (`y₃ = [4]/[2]³`, `y₂₁ = 1/[2]²`, `y_{(1³)} = 0`).
  * **Convention C** — the corpus-canonical Jones–Markov trace (axioms
    M1–M3 with `z = 1/(√q + 1/√q)`, `markov_trace_canonical.tr_M_word`),
    which equals the Wenzl-bridge z-trace `Σ_λ y_λ^W χ^λ` EXACTLY (probe
    route 3).

  Working over `t = √q` (so both conventions are rational functions of `t`):

      tr_C(t) = (1 − t − t² + t³ − 4t⁴ + 2t⁵ + 4t⁶ − t⁷ + 6t⁸ − t⁹ − 6t¹⁰
                 − t¹¹ − 4t¹² + 2t¹³ + 4t¹⁴ + t¹⁵ + t¹⁶ − t¹⁷ − t¹⁸) / t⁹
      tr_D(t) = (−t²⁴ + 3t²⁰ − 2t¹⁶ + 4t¹² − 2t⁸ + 3t⁴ − 1) / (t¹⁶ + 2t¹² + t⁸)

  This file proves, sorry-free:
  1. `trD_t_eq_trM_borromean` — the t-form of D equals the corpus
     `trM_borromean (t² − t⁻²)` (ties this file to the proved closed form);
  2. `conventionD_ne_conventionC_at_two` — `tr_D(2) ≠ tr_C(2)` (exact
     rationals, `norm_num`);
  3. `conventionD_ne_conventionC` — hence the two conventions are NOT the
     same function of t: the trace-convention split is a theorem, not a
     numerical observation.  At the substrate q₀ the gap is ≈ 1.9554e-4
     (probe witness) — immaterial at the current 2.3× binding scale,
     material below 0.1 %.

  PROVENANCE of tr_C's closed form: derived by exact CAS computation, by
  THREE independent routes agreeing on the identical rational function —
  (i) `markov_trace_canonical.tr_M_word` with the Hecke `σ⁻¹ = σ − h`
  expansion, (ii) `markov_trace_recursive` on the signed word, (iii) the
  symbolic Wenzl bridge `Σ_λ y_λ^W χ^λ(β_Bor)` (Hoefsmit matrices).  See
  `computations/probes/probe_convention_d_vs_c_borromean.py` and its
  witness.  A Lean derivation of tr_C from the M1–M3 axioms themselves
  (parallel to `BorromeanMarkovTrace`) is queued as the follow-up task;
  THIS file's theorems are about the explicit rational functions and are
  fully machine-checked as such.

  Registry: docs/audits/2026-06-09-binding-trace-convention-split.md
  (convention D addendum + D ≟ C answer).

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import QOU.BraidsAndKnots.BorromeanMarkovTrace

namespace QOU.BraidsAndKnots

/-! ## `R[t]` layer — the two numerators/denominators over a generic ring -/

section CommRing
variable {R : Type*} [CommRing R]

/-- Numerator of the canonical (convention C / Wenzl z-trace) Markov trace
of `β_Bor`, as a polynomial in `t = √q`. CAS-derived by three agreeing
routes (see file header provenance). -/
def trC_borromean_num (t : R) : R :=
  1 - t - t^2 + t^3 - 4*t^4 + 2*t^5 + 4*t^6 - t^7 + 6*t^8 - t^9 - 6*t^10
    - t^11 - 4*t^12 + 2*t^13 + 4*t^14 + t^15 + t^16 - t^17 - t^18

/-- Denominator of convention C at `β_Bor`: `t⁹`. -/
def trC_borromean_den (t : R) : R := t^9

/-- Numerator of the pipeline (convention D / TL-Jones) trace of `β_Bor`
in `t = √q`: the `trM_borromean_num (t² − t⁻²)` numerator after clearing
`t`-powers. -/
def trD_borromean_num (t : R) : R :=
  -t^24 + 3*t^20 - 2*t^16 + 4*t^12 - 2*t^8 + 3*t^4 - 1

/-- Denominator of convention D in `t`: `t¹⁶ + 2t¹² + t⁸ = t⁸(t⁴+1)²`. -/
def trD_borromean_den (t : R) : R := t^16 + 2*t^12 + t^8

/-- The D-denominator factors as `t⁸·(t⁴+1)²` — pure `ring`. -/
theorem trD_borromean_den_factor (t : R) :
    trD_borromean_den t = t^8 * (t^4 + 1)^2 := by
  unfold trD_borromean_den
  ring

end CommRing

/-! ## Archimedean (`ℚ`) layer — quotient forms, the bridge to
`trM_borromean`, and the split theorem -/

/-- Convention C (canonical Jones–Markov / Wenzl z-trace) at `β_Bor`,
quotient form over `ℚ` in `t = √q`. -/
noncomputable def trC_borromean (t : ℚ) : ℚ :=
  trC_borromean_num t / trC_borromean_den t

/-- Convention D (TL/Jones pipeline) at `β_Bor`, quotient form over `ℚ`
in `t = √q`. -/
noncomputable def trD_borromean (t : ℚ) : ℚ :=
  trD_borromean_num t / trD_borromean_den t

/-- The C-denominator `t⁹` is nonzero for `t ≠ 0`. -/
theorem trC_borromean_den_ne_zero {t : ℚ} (ht : t ≠ 0) :
    trC_borromean_den t ≠ 0 := by
  unfold trC_borromean_den
  positivity

/-- The D-denominator `t⁸(t⁴+1)²` is nonzero for `t ≠ 0`. -/
theorem trD_borromean_den_ne_zero {t : ℚ} (ht : t ≠ 0) :
    trD_borromean_den t ≠ 0 := by
  rw [trD_borromean_den_factor]
  have h1 : (t : ℚ)^4 + 1 > 0 := by positivity
  positivity

/-- **Bridge to the corpus closed form.** For `t ≠ 0`, the t-form of
convention D equals `trM_borromean (t² − t⁻²)` — the Lean-proved
`BorromeanMarkovTrace` quotient form at `h = q − q⁻¹ = t² − t⁻²`.
So `trD_borromean` here IS the corpus pipeline object, re-parameterised. -/
theorem trD_t_eq_trM_borromean {t : ℚ} (ht : t ≠ 0) :
    trD_borromean t = trM_borromean (t^2 - (t^2)⁻¹) := by
  unfold trD_borromean trM_borromean trD_borromean_num trD_borromean_den
    trM_borromean_num trM_borromean_den
  have ht2 : (t : ℚ)^2 ≠ 0 := pow_ne_zero 2 ht
  have hden : (t : ℚ)^16 + 2*t^12 + t^8 ≠ 0 := by
    have := trD_borromean_den_ne_zero ht
    unfold trD_borromean_den at this
    exact this
  have hden2 : ((t:ℚ)^2 - (t^2)⁻¹)^2 + 4 ≠ 0 := by
    have h4 : ((t:ℚ)^2 - (t^2)⁻¹)^2 + 4 > 0 := by positivity
    exact ne_of_gt h4
  field_simp
  ring

/-- **The split witness point.** At `t = 2` the two conventions give
different exact rationals: `tr_C(2) = −236413/512` while
`tr_D(2) = −13746641/73984`. -/
theorem conventionD_ne_conventionC_at_two :
    trD_borromean 2 ≠ trC_borromean 2 := by
  unfold trD_borromean trC_borromean trD_borromean_num trD_borromean_den
    trC_borromean_num trC_borromean_den
  norm_num

/-- **Convention D ≠ convention C.** The pipeline (TL/Jones) trace and the
canonical (Wenzl z-trace) Markov trace of `β_Bor` are NOT the same
function of `t = √q`: they differ at `t = 2` (where both denominators
are nonzero), hence differ as rational functions. The trace-convention
split registered in the 2026-06-09 audit addendum is a theorem. -/
theorem conventionD_ne_conventionC :
    ¬ ∀ t : ℚ, t ≠ 0 → trD_borromean t = trC_borromean t := by
  intro hall
  exact conventionD_ne_conventionC_at_two (hall 2 (by norm_num))

end QOU.BraidsAndKnots
