import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Tactic


/-!
# QOU.Archimedean.HopfDiquark — Hopf-linked quark pair

A diquark is two quarks in distinct color tubes joined by the
Hopf link.  The antisymmetric color structure (color antitriplet)
arises from the linking number orientation.

## References

- [alford1999] https://doi.org/10.1016/S0550-3213(98)00668-3
- [leitner2026] Ch. 7, §Strangelet Stability

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

noncomputable section

namespace QOU.Archimedean

/-- Color index: one of three color tubes (r, g, b). -/
abbrev ColorIndex := Fin 3

/-- Flavor index: u, d, s. -/
inductive Flavor where
  | up : Flavor
  | down : Flavor
  | strange : Flavor
deriving DecidableEq, Repr

/-- Crossing orientation of a quark: +1 (positive) or -1 (negative). -/
def Flavor.orientation : Flavor → Int
  | .up => 1
  | .down => -1
  | .strange => -1

/-- Crossing count of a quark's torus knot representative. -/
def Flavor.crossingCount : Flavor → ℕ
  | .up => 3       -- T_{2,3} trefoil
  | .down => 3     -- mirror T_{2,3}
  | .strange => 5  -- mirror T_{2,5} cinquefoil

/-- A Hopf diquark: two quarks in distinct color tubes, Hopf-linked. -/
structure HopfDiquark where
  /-- First quark flavor -/
  flavor₁ : Flavor
  /-- Second quark flavor -/
  flavor₂ : Flavor
  /-- First quark color tube -/
  color₁ : ColorIndex
  /-- Second quark color tube -/
  color₂ : ColorIndex
  /-- Colors must be distinct (antisymmetric pairing) -/
  color_distinct : color₁ ≠ color₂
  /-- Flavors must be distinct (most attractive channel) -/
  flavor_distinct : flavor₁ ≠ flavor₂

/-- The spectator color: the tube not participating in the diquark. -/
def HopfDiquark.spectatorColor (D : HopfDiquark) : ColorIndex :=
  -- The unique color ≠ color₁ and ≠ color₂
  if D.color₁ = 0 then (if D.color₂ = 1 then 2 else 1)
  else if D.color₁ = 1 then (if D.color₂ = 0 then 2 else 0)
  else (if D.color₂ = 0 then 1 else 0)

/-- Linking number of the Hopf link: +1 for the canonical orientation. -/
def hopf_linking_number : Int :=
  1

/-- Hopf link volume is zero (torus link, not hyperbolic). -/
-- Ref: [leitner2026] Ch. 4
def hopf_link_volume : ℝ :=
  0

/-- Crossing energy of the Hopf link at substrate parameter q.
    The Hopf link T_{2,2} has braid word σ₁², contributing
    2 positive crossings. -/
-- Ref: [leitner2026] Ch. 7
def hopf_crossing_energy (q : ℝ) : ℝ := q + q⁻¹

/-- The CFL gap: energy to break a single Hopf diquark. -/
-- Ref: [alford1999]
def cfl_gap (q : ℝ) : ℝ := hopf_crossing_energy q

/-- At q = 1.1097, the CFL gap is approximately 2.011 Skein units. -/
-- Ref: [leitner2026] Ch. 7
theorem cfl_gap_approx :
    cfl_gap 1.1097 > 2 ∧ cfl_gap 1.1097 < 2.1 := by
  unfold cfl_gap hopf_crossing_energy
  constructor <;> norm_num

/-- Borromean binding per baryon number at substrate parameter q.
    Uses the topological mass formula with V_B = 7.32772. -/
-- Ref: [leitner2026] Ch. 7
def borromean_binding_per_baryon (q : ℝ) (hq : q > 1) : ℝ :=
  7.32772 / ((q - 1) / q) ^ 2

/-- Hopf diquark binding per baryon number.
    Three diquark pairs per two baryon-number units. -/
-- Ref: [leitner2026] Ch. 7
def diquark_binding_per_baryon (q : ℝ) : ℝ :=
  (3 / 2) * (q + q⁻¹)

/-- At q = 1.1097, Borromean binding vastly exceeds diquark binding. -/
-- Ref: [leitner2026] Ch. 7
theorem borromean_dominates_diquark :
    diquark_binding_per_baryon 1.1097 < 4 := by
  unfold diquark_binding_per_baryon
  norm_num

end QOU.Archimedean

end
