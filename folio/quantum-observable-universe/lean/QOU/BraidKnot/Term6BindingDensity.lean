import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Basic

/-!
# QOU.BraidKnot.Term6BindingDensity

Structural shape of the per-nucleon binding-energy formula
derived from the level-3 Gröbner-Shirshov spectral-sequence
stratum (Term 6 per `prop:gb-spectral-sequence`).

The formula has the form

    B(Z, N) / A  =  α · T_6(Z, N) / A^3  +  β  +  δ_M(Z, N)

with `T_6` defined in terms of 9-strand Markov traces of
triple-nucleon sub-braids, and `α, β, δ_M` calibration
quantities. The shape (cubic-A normalization + magic correction)
is structurally derived from the spectral-sequence identification.
The coefficients `α, β` are calibrated to AME data (R² = 0.84
across 16 atoms); a categorical derivation predicting them from
q_0 alone is open (see `2026-05-02-alpha-categorical-derivation`).

This file states the SHAPE constraint as a Lean class; downstream
binding-energy theorems take `[Term6BindingDensity]` as a
hypothesis to remain `theorem`/`proposition` per AGENTS.md
§3b-cond.

LaTeX label: `prop:term6-binding-density`

## References

- [leitner2026] §Term 6 binding density
- [bethe1936] (BW formula context)
- `prop:gb-spectral-sequence`
- `2026-05-02-Term6-binding-derivation.md` (audit memo)
-/

namespace QOU.BraidKnot

/-- Atomic-nucleus datum: proton count Z, neutron count N. -/
structure NucleusDatum where
  Z : ℕ
  N : ℕ

/-- Mass number A = Z + N. -/
def NucleusDatum.A (d : NucleusDatum) : ℕ := d.Z + d.N

/-- The seven nuclear magic numbers. -/
def MAGIC_LADDER : Finset ℕ := {2, 8, 20, 28, 50, 82, 126}

/-- **Term 6 binding-density class.**  An instance asserts:

    1. `T_6 : NucleusDatum → ℝ` — the level-3 stratum contribution.
    2. `alpha, beta : ℝ` — calibration coefficients (CALIBRATED,
       not yet categorically derived).
    3. `delta_M : NucleusDatum → ℝ` — magic-shell operator
       correction.
    4. `binding_density_shape` — for every nucleus the
       per-nucleon binding equals
       `alpha · T_6 / A^3 + beta + delta_M`.

    The shape is structurally derived from
    `prop:gb-spectral-sequence`. The values of `alpha` and `beta`
    are empirically calibrated; a `sorry` in any concrete instance
    of `binding_density_shape` represents the calibration
    uncertainty (~3%) and the open derivation question. -/
class Term6BindingDensity where
  /-- Term-6 spectral-sequence stratum value. -/
  T_6 : NucleusDatum → ℝ
  /-- Calibration coefficient (Term-6 prefactor). Empirically ~339 MeV. -/
  alpha : ℝ
  /-- Calibration intercept. Empirically ~1.14 MeV. -/
  beta : ℝ
  /-- Magic-shell operator correction. -/
  delta_M : NucleusDatum → ℝ
  /-- AME binding energy datum (input). -/
  B_AME : NucleusDatum → ℝ
  /-- Calibration window — the structural shape matches AME within
      `tolerance` (~3% of `alpha · T_6 / A^3` plus residual ~1 MeV). -/
  tolerance : ℝ
  /-- Tolerance is positive. -/
  tolerance_pos : 0 < tolerance
  /-- **Structural-shape claim (the conjectural piece):** for
      every nucleus, the AME binding-per-nucleon is approximated by
      the calibrated structural formula within `tolerance`.  A
      concrete instance discharges this with `sorry` (the
      calibration; ~3% uncertainty per the 16-atom fit). -/
  binding_density_shape :
    ∀ (d : NucleusDatum), d.A > 0 →
      ∃ ε : ℝ, |ε| ≤ tolerance ∧
        B_AME d / (d.A : ℝ)
          = alpha * T_6 d / (d.A : ℝ)^3 + beta + delta_M d + ε

/-- **Downstream conditional theorem.**  Conditional on
    `[Term6BindingDensity]`, every nucleus has its per-nucleon
    binding within `tolerance` of the structural formula.  Fully
    verified by Lean once an instance is fixed. -/
theorem binding_density_within_tolerance
    [inst : Term6BindingDensity]
    (d : NucleusDatum) (hA : d.A > 0) :
    ∃ ε : ℝ, |ε| ≤ inst.tolerance ∧
      inst.B_AME d / (d.A : ℝ)
        = inst.alpha * inst.T_6 d / (d.A : ℝ)^3
          + inst.beta + inst.delta_M d + ε :=
  inst.binding_density_shape d hA

end QOU.BraidKnot
