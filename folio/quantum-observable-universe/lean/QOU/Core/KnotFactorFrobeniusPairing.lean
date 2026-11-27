import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# QOU.Conjectures.KnotFactorFrobeniusPairing — binding as a Markov-trace defect

The **binding** carrier of `conj:knot-factor-frobenius-pairing`
(`folio/quantum-observable-universe/mass-theory/knot-factor-frobenius-pairing.md`):

  `B_bulk(Z, N) = E₀ · (|tr_M(W_free)| − |tr_M(W_atom)|)`.

## Re-scoped 2026-11-22 (owner card "3: Both, inside reconcile work")

This carrier used to be a class whose one field, `binding_eq_defect`, asserted
`binding = E₀ · (traceMag wFree − traceMag wAtom)` for an abstract `binding`
function.  That is not a conjecture a proof could close: `binding` had no other
definition, so the field *was* its definition, and the trivial model satisfied
it by `ring`.  The model term is now a `def`, and what remains is a comparison
claim — whether `bindingDefect` matches the AME2020 binding energies — which is
made in the mass-binding dashboard (`B_can⁰` in `mass_binding_dashboard.py`),
not in Lean.

Recorded beside it is the log form `bindingLog`, which the dashboard also scores
(`B_sym`), with the one structural fact that separates the two: when the free
word is a connected sum its trace multiplies (`tr(W₁ # W₂) = tr W₁ · tr W₂` for a
multiplicative trace), the log form is additive over the summands
(`bindingLog_mul`), and the difference form is not.

The braid-level half (Markov trace = pairing with a central knot factor) is a
theorem: `QOU.BraidKnot.KnotFactorFrobeniusPairing`, `QOU.Hecke.KnotFactor`.

LaTeX label: `conj:knot-factor-frobenius-pairing`

## References

- [leitner2026] §"Knot-factor Frobenius pairing"
- [jones1985] https://www.jstor.org/stable/2007074
-/

namespace QOU.Conjectures

/-- **The difference form of the binding model term**:
    `E₀ · (|tr(W_free)| − |tr(W_atom)|)`.  A definition; its agreement with
    measured binding energies is a comparison point, not a Lean statement. -/
noncomputable def bindingDefect (E0 trFree trAtom : ℝ) : ℝ :=
  E0 * (|trFree| - |trAtom|)

/-- **The log form of the binding model term**: `E₀ · log(|tr(W_free)| / |tr(W_atom)|)`. -/
noncomputable def bindingLog (E0 trFree trAtom : ℝ) : ℝ :=
  E0 * Real.log (|trFree| / |trAtom|)

/-- **The log form is additive over a connected-sum free word.**  If the free
    trace is a product `a · b` of nonzero factor traces, the log binding splits
    as the two factors' log masses minus the atom's. -/
theorem bindingLog_mul (E0 a b trAtom : ℝ) (ha : a ≠ 0) (hb : b ≠ 0) (hc : trAtom ≠ 0) :
    bindingLog E0 (a * b) trAtom
      = E0 * (Real.log |a| + Real.log |b| - Real.log |trAtom|) := by
  unfold bindingLog
  rw [abs_mul, Real.log_div (mul_ne_zero (abs_ne_zero.mpr ha) (abs_ne_zero.mpr hb))
    (abs_ne_zero.mpr hc), Real.log_mul (abs_ne_zero.mpr ha) (abs_ne_zero.mpr hb)]

/-- **The difference form is not additive over a connected sum.**  At factor
    traces `a = b = 1/2` and atom trace `1/8`, the difference binding of the
    product is not the sum of the factors' differences against half the atom. -/
theorem bindingDefect_not_additive :
    bindingDefect 1 ((1/2) * (1/2)) (1/8)
      ≠ bindingDefect 1 (1/2) (1/16) + bindingDefect 1 (1/2) (1/16) := by
  unfold bindingDefect
  norm_num [abs_of_pos]

end QOU.Conjectures
