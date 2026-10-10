import Mathlib.Data.Real.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidKnot — Catalogue of Taylor coefficients

**Catalogue of Taylor coefficients of `delta_tau_M_surrogate` at
`q = 1`, orders 0..7**, sourced from
`qbeta-c3-multiblock-recursion-attack.witness.json`
(`taylor_coeffs_w_expansion` field).

Orders 0 and 1 are independently proved sorry-free in PR #1764
(`delta_tau_M_surrogate_vanish_at_one` and
`delta_tau_M_surrogate_hasDerivAt_one`). This file CATALOGUES the
values up to order 7 as a named function; only the order-0 and
order-1 reflexive-equality theorems are sorry-free here. Higher
orders are stated as `Ref:`-cited theorems whose `iteratedDeriv`
discharge is deferred (each requires a quotient-rule chain
$n+1$ levels deep).

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
witnessed and return 0 here. -/
def delta_tau_M_surrogate_taylor_witness : ℕ → ℚ
  | 0 => 0
  | 1 => -5/6
  | 2 => 5/6
  | 3 => -41/9
  | 4 => 149/18
  | 5 => -1729/108
  | 6 => 111/4
  | 7 => -3665/81
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

/-- Order-3 witness value: $c_3 = -41/9$. -/
theorem delta_tau_M_surrogate_taylor_witness_3 :
    delta_tau_M_surrogate_taylor_witness 3 = -41/9 := rfl

/-- Order-4 witness value: $c_4 = 149/18$. -/
theorem delta_tau_M_surrogate_taylor_witness_4 :
    delta_tau_M_surrogate_taylor_witness 4 = 149/18 := rfl

/-- Order-5 witness value: $c_5 = -1729/108$. -/
theorem delta_tau_M_surrogate_taylor_witness_5 :
    delta_tau_M_surrogate_taylor_witness 5 = -1729/108 := rfl

/-- Order-6 witness value: $c_6 = 111/4$. -/
theorem delta_tau_M_surrogate_taylor_witness_6 :
    delta_tau_M_surrogate_taylor_witness 6 = 111/4 := rfl

/-- Order-7 witness value: $c_7 = -3665/81$. -/
theorem delta_tau_M_surrogate_taylor_witness_7 :
    delta_tau_M_surrogate_taylor_witness 7 = -3665/81 := rfl

end QOU.BraidKnot
