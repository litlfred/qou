import Mathlib.Data.Real.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidKnot — Catalogue of Taylor coefficients

**Catalogue of Taylor coefficients of `delta_tau_M_surrogate` at
`q = 1`, orders 0..7**, sourced from
`qbeta-c3-multiblock-recursion-attack.witness.json`
(`taylor_coeffs_w_expansion` field).

The values are the **canonical (borromean)** coefficients, the frame of
`delta_tau_M_surrogate` in `QBetaPerBlockChiClosedForms.lean` and of the
witness's `taylor_coeffs_w_expansion` field. The table held the superseded
grouped-frame values for orders 3..7 (`-41/9`, `149/18`, `-1729/108`, `111/4`,
`-3665/81`) until 2026-10-10 (bean `qou-eddc`); orders 0..2 are the same in
both frames.

This file is a CATALOGUE: each theorem below is `rfl` on the table and
proves nothing about the function. Every order is proved separately, as a
statement about `delta_tau_M_surrogate` itself, in
`QBetaPerBlockChiClosedForms.lean`: `delta_tau_M_surrogate_vanish_at_one`,
`delta_tau_M_surrogate_hasDerivAt_one`, and
`delta_tau_M_surrogate_taylor_coeff_2` … `_7`.

LaTeX label: `prop:qbeta-delta-tau-surrogate-taylor-coefficients`

## References
- Witness: `qbeta-c3-multiblock-recursion-attack.witness.json`
- Parent: `qbeta-per-block-chi-closed-forms.lean` (PR #1764)
-/

namespace QOU.BraidKnot

/-- Witness-catalogued Taylor coefficients of
`delta_tau_M_surrogate` at `q = 1`, orders 0..7.

Source: `qbeta-c3-multiblock-recursion-attack.witness.json`
(`taylor_coeffs_w_expansion` field). Values past order 7 are not
catalogued here and return 0. -/
def delta_tau_M_surrogate_taylor_witness : ℕ → ℚ
  | 0 => 0
  | 1 => -5/6
  | 2 => 5/6
  | 3 => -23/9
  | 4 => 77/18
  | 5 => 1349/108
  | 6 => -191/4
  | 7 => 26285/162
  | _ => 0

/-- Order-0 witness value. Independently formally-proved as
`delta_tau_M_surrogate_vanish_at_one` in PR #1764. -/
theorem delta_tau_M_surrogate_taylor_witness_0 :
    delta_tau_M_surrogate_taylor_witness 0 = 0 := rfl

/-- Order-1 witness value. Independently formally-proved as
`delta_tau_M_surrogate_hasDerivAt_one` in PR #1764 (returning
the derivative `−5/6 = c_1 · 1!`). -/
theorem delta_tau_M_surrogate_taylor_witness_1 :
    delta_tau_M_surrogate_taylor_witness 1 = -5/6 := rfl

/-- Order-2 witness value: $c_2 = 5/6$. -/
theorem delta_tau_M_surrogate_taylor_witness_2 :
    delta_tau_M_surrogate_taylor_witness 2 = 5/6 := rfl

/-- Order-3 witness value: $c_3 = -23/9$. -/
theorem delta_tau_M_surrogate_taylor_witness_3 :
    delta_tau_M_surrogate_taylor_witness 3 = -23/9 := rfl

/-- Order-4 witness value: $c_4 = 77/18$. -/
theorem delta_tau_M_surrogate_taylor_witness_4 :
    delta_tau_M_surrogate_taylor_witness 4 = 77/18 := rfl

/-- Order-5 witness value: $c_5 = 1349/108$. -/
theorem delta_tau_M_surrogate_taylor_witness_5 :
    delta_tau_M_surrogate_taylor_witness 5 = 1349/108 := rfl

/-- Order-6 witness value: $c_6 = -191/4$. -/
theorem delta_tau_M_surrogate_taylor_witness_6 :
    delta_tau_M_surrogate_taylor_witness 6 = -191/4 := rfl

/-- Order-7 witness value: $c_7 = 26285/162$. -/
theorem delta_tau_M_surrogate_taylor_witness_7 :
    delta_tau_M_surrogate_taylor_witness 7 = 26285/162 := rfl

end QOU.BraidKnot
