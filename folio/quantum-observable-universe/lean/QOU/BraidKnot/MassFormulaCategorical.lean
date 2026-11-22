import Mathlib.Tactic
import QOU.HeckeAlgebra.Common

/-!
# QOU.BraidKnot.MassFormulaCategorical

The QOU mass formula `M(K) = ρ(K) · m_e · |tr_M(T_w(K))|` for
the canonical Hecke element `T_w(K)` of knot/nucleus `K`.

## Mathematical content

Per `conj:atom-knot-mass-derivation` in the manuscript:

    M(K) = ρ(K) · m_e · |tr_M(T_w(K))|     (cat units)

where:
- `ρ(K) ∈ ℕ_{≥1}` is the SDP-multiplicity (per Wedderburn
  decomposition, `ρ = ⌊dim_q(λ⋆)⌉` per
  `conj:rho-prefactor-structural`)
- `m_e` is the electron mass (calibration anchor; cat units)
- `|tr_M(T_w)|` is the absolute Markov trace at `q_0`

Conversion to MeV:

    M(K)_MeV = M(K) · M_E_MEV_CODATA

where `M_E_MEV_CODATA = 0.51099895069 MeV` (the only CAL input
in the chain; everything else is derived).

## What this module provides

- `categoricalMass` — the `M = ρ · m_e · |tr_M|` formula at the
  abstract `HeckeElement n` level
- `categoricalMass_pos` — the formula gives a strictly positive
  mass when ρ > 0 and tr_M ≠ 0
- `categoricalMassMeV` — conversion to MeV

## Open Lean port

The Markov trace `markovTrace n` is currently axiomatised
(`QOU.HeckeAlgebra.Common`) — there's no concrete `T_w` element
to apply it to in Lean yet.  This module's content sits at the
schematic level: the FORMULA is type-correct, but plugging in
real `T_w` values awaits the Hoefsmit-machinery port.

## References

- `conj:atom-knot-mass-derivation` (the formula)
- `conj:rho-prefactor-structural` (ρ from Wedderburn)
- `QOU.HeckeAlgebra.Common.markovTrace` (axiomatised tr_M)
- `def:m-e-codata` (m_e MeV calibration)
-/

namespace QOU.BraidKnot.MassFormulaCategorical

open QOU.HeckeAlgebra

/-- The CODATA electron-mass scale in MeV: `m_e = 0.51099895069`.
    The only CAL input in the QOU mass-prediction chain. -/
def m_e_MeV_codata : ℝ := 0.51099895069

/-- The CODATA electron-mass scale is positive. -/
theorem m_e_MeV_codata_pos : 0 < m_e_MeV_codata := by
  unfold m_e_MeV_codata
  norm_num

/-- **Categorical mass formula**: `M(T_w) = ρ · m_e · |tr_M(T_w)|`
    in cat units.  At this abstraction level, `T_w : HeckeElement n`,
    `ρ : ℕ`, and `m_e : ℝ` (the cat-unit electron mass, distinct
    from the MeV-scale one). -/
noncomputable def categoricalMass {n : ℕ} (rho : ℕ) (m_e : ℝ) (T_w : HeckeElement n) : ℝ :=
  rho * m_e * absMarkovTrace n T_w

/-- **Mass is non-negative** (multiplicity, electron mass, and
    `|tr_M|` are all non-negative). -/
theorem categoricalMass_nonneg {n : ℕ} {rho : ℕ} {m_e : ℝ}
    (h_me : 0 ≤ m_e) (T_w : HeckeElement n) :
    0 ≤ categoricalMass rho m_e T_w := by
  unfold categoricalMass
  apply mul_nonneg
  apply mul_nonneg
  · exact_mod_cast Nat.zero_le rho
  · exact h_me
  · exact absMarkovTrace_nonneg n T_w

/-- **Mass is strictly positive** when ρ > 0, m_e > 0, and the
    Markov trace is non-zero. -/
theorem categoricalMass_pos {n : ℕ} {rho : ℕ} {m_e : ℝ}
    (h_rho : 0 < rho) (h_me : 0 < m_e)
    {T_w : HeckeElement n} (h_tr : markovTrace n T_w ≠ 0) :
    0 < categoricalMass rho m_e T_w := by
  unfold categoricalMass absMarkovTrace
  apply mul_pos
  apply mul_pos
  · exact_mod_cast h_rho
  · exact h_me
  · exact abs_pos.mpr h_tr

/-- **Mass conversion cat-units → MeV**: multiply by the CODATA
    electron-mass scale.  Implements
    `M(K)_MeV := M(K)_cat · M_E_MEV_CODATA`. -/
noncomputable def categoricalMassMeV {n : ℕ} (rho : ℕ) (m_e : ℝ) (T_w : HeckeElement n) : ℝ :=
  categoricalMass rho m_e T_w * m_e_MeV_codata

/-- **MeV mass is non-negative**. -/
theorem categoricalMassMeV_nonneg {n : ℕ} {rho : ℕ} {m_e : ℝ}
    (h_me : 0 ≤ m_e) (T_w : HeckeElement n) :
    0 ≤ categoricalMassMeV rho m_e T_w := by
  unfold categoricalMassMeV
  exact mul_nonneg (categoricalMass_nonneg h_me T_w)
    (le_of_lt m_e_MeV_codata_pos)

end QOU.BraidKnot.MassFormulaCategorical
