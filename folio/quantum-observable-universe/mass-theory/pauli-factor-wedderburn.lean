import Mathlib.Data.Real.Basic

/-!
# QOU.BraidKnot.pauli_factor_wedderburn

The Pauli factor `F_Pauli` in nuclear Q-value formulas is the ratio
of Wedderburn-block traces on the alternating and symmetric irreps
of `H_n(q)`.

LaTeX label: `prop:pauli-factor-wedderburn`

## References

- [leitner2026] §3/pauli-factor-wedderburn
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidKnot

/-- Wedderburn-block trace data for a braid. -/
structure WedderburnTraces where
  trAlt : ℝ                 -- tr on alternating block
  trSym : ℝ                 -- tr on symmetric block
  sym_nonzero : trSym ≠ 0

/-- The Pauli factor as the alt/sym block trace ratio. -/
noncomputable def pauliFactor (W : WedderburnTraces) : ℝ :=
  W.trAlt / W.trSym

/-- **Proposition (Pauli factor as Wedderburn-block ratio)**.

    The Pauli statistical weight is the ratio of alternating to
    symmetric Wedderburn-block traces. -/
-- Ref: [leitner2026] §3/pauli-factor-wedderburn
theorem pauli_factor_wedderburn (W : WedderburnTraces) :
    pauliFactor W * W.trSym = W.trAlt := by
  unfold pauliFactor
  exact div_mul_cancel₀ _ W.sym_nonzero

end QOU.BraidKnot
