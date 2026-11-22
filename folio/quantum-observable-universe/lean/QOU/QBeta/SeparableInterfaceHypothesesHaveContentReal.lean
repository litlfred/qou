import QOU.QBeta.SeparableInterfaceHypothesesHaveContent
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp
import Mathlib.Algebra.Order.Field.Basic

/-!
# The Pauli-lock release survives positivity — the archimedean half

Sibling of `QOU.QBeta.SeparableInterfaceHypothesesHaveContent`, which carries the generic
statements. Split per AGENTS.md §7c: the ordering (`0 < μ`) and the measured asymmetry as a
real numeral are archimedean, so they live here and consume the generic results at
`R := ℝ` rather than specialising them in place.

**What the split buys.** The generic file's three results hold over any commutative ring,
monoid or field — so the finding that `separable_interface_degenerate`'s conclusion is
unconstrained once its antecedent is dropped is *not* an artefact of the real numbers.
This file adds the two things that genuinely need `ℝ`: that the escape stays inside the
physically admissible positive-weight regime, and that the specific measured ratio is one
of the values it reaches.

-- Ref: [leitner2026] quantum-observable-universe/lean/QOU/QBeta/InterfaceScalar.lean
-/

namespace QOU.QBeta.SeparableInterfaceContent

/-- The generic content theorem specialised to the reals; the non-degeneracy hypothesis
`(5 : ℝ) ≠ 6` is discharged by `norm_num`. Recorded so that the ring the corpus actually
reasons over is on the record as an *instance* of the generic result, not a separate claim.

Written in the named-argument form `(R := ℝ)` that AGENTS.md §7c prescribes for the
archimedean sibling. An earlier revision used `@f ℝ _` to dodge `check-sidecars.sh`,
which counted the literal `(R :=` as evidence a file declares a *generic* result and so
reported this correctly-split file as "§7c MIXED". That detector bug is fixed
(`scripts/check-sidecars.sh`, fourth false-positive class), so the workaround is gone and
the prescribed spelling is back. -/
theorem separability_hypotheses_have_content_real :
    ∃ (fSpin fIso : Bool → ℝ) (fSpace : Unit → ℝ),
      fSpin true * fIso false * fSpace () ≠ fSpin false * fIso true * fSpace () :=
  separability_hypotheses_have_content (R := ℝ) (by norm_num)

/-- **The escape survives positivity.**

Over `ℝ` with all four weights strictly positive — the physically admissible regime, since
the interface projector scalars satisfy `μ₊ + μ₋ = 1` with both positive for `q > 0`
(`InterfaceScalar.proj_add_eq_one` and its ordering companions) — every positive ratio is
still attainable. So the release of the conclusion is not an artefact of admitting
negative or zero projector weights, which is the first objection it would meet. -/
theorem distinct_positive_scalars_reach_any_ratio
    (μp μm r : ℝ) (hμp : 0 < μp) (hμm : 0 < μm) (hr : 0 < r) :
    ∃ νp νm : ℝ, 0 < νp ∧ 0 < νm ∧ μp * νm = r * (μm * νp) := by
  refine ⟨1, r * μm / μp, one_pos, div_pos (mul_pos hr hμm) hμp, ?_⟩
  field_simp

/-- The two-nucleon channel asymmetry the corpus measures, `≈ 33.7055`
(`computations/probes/two_nucleon_linking_matrix_channel_blind_probe.py`, which pins it to
four decimals). Carried as a numeral so the theorem below is falsifiable arithmetic rather
than a symbol. -/
noncomputable def measuredChannelAsymmetry : ℝ := 337055 / 10000

/-- **The measured asymmetry is attainable by a separable interface with distinct
scalars.** This is the concrete form of `distinct_positive_scalars_reach_any_ratio`, and it
is why the equal-scalars hypothesis is load-bearing rather than decorative: what it
excludes is not a small correction but the whole measured effect. -/
theorem measured_asymmetry_attainable :
    ∃ νp νm : ℝ, 0 < νp ∧ 0 < νm ∧
      (1 : ℝ) * νm = measuredChannelAsymmetry * (1 * νp) :=
  distinct_positive_scalars_reach_any_ratio 1 1 measuredChannelAsymmetry one_pos one_pos
    (by norm_num [measuredChannelAsymmetry])

end QOU.QBeta.SeparableInterfaceContent
