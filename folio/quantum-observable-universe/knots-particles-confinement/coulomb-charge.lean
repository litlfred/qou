import Mathlib.Data.Real.Basic
import Mathlib.Tactic


/-!
# QOU.Braiding.CoulombCharge — Coulomb charge of a knot composite

The Coulomb charge Q(H) = ½(n₊(β) − n₋(β)) measures the crossing
asymmetry of a knot composite.  It governs the magnitude and sign
of the electromagnetic (Coulomb) correction to the crossing energy.

LaTeX label: `def:coulomb-charge`

## References

- [leitner2026] Ch. 4, §10

**Ground ring**: this Lean sibling is the archimedean specialisation
over `ℝ` (AGENTS.md §7c): the Coulomb correction uses `q⁻¹` and the
half-sum `(n₊ − n₋)/2`, both of which require division.  The
substrate parameter `q : ℝ` is `q ↦ q₀` under `ι : ℤ[q, q⁻¹] → ℝ`.
The underlying combinatorial content (the crossing counts) is generic
to any commutative ring with the same `q`-data.
-/

namespace QOU.Braiding

/-! ## Coulomb Charge -/

/-- **Coulomb charge** of a knot composite with braid word β.

    Q(H) = ½(n₊(β) − n₋(β))

    where n₊, n₋ are the positive and negative crossing counts.

    - Q(H) > 0: net positive crossings, repulsive Coulomb contribution.
    - Q(H) = 0: electromagnetically neutral.
    - Q(H) < 0: net negative crossings, attractive Coulomb contribution. -/
-- Ref: [leitner2026] Ch. 4, §10
structure CoulombCharge where
  /-- Number of positive crossings n₊. -/
  numPositive : ℕ
  /-- Number of negative crossings n₋. -/
  numNegative : ℕ

/-- The Coulomb charge value: Q = (n₊ − n₋) / 2. -/
noncomputable def CoulombCharge.value (C : CoulombCharge) : ℝ :=
  ((C.numPositive : ℝ) - C.numNegative) / 2

/-- A composite is electromagnetically neutral when Q(H) = 0,
    i.e., n₊ = n₋. -/
def CoulombCharge.isNeutral (C : CoulombCharge) : Prop :=
  C.numPositive = C.numNegative

/-- Neutral composites have zero Coulomb charge. -/
-- Ref: [leitner2026] Ch. 4, §10
theorem CoulombCharge.neutral_iff_zero (C : CoulombCharge) :
    C.isNeutral ↔ C.value = 0 := by
  constructor
  · intro h
    simp only [value, isNeutral] at h ⊢
    rw [h, sub_self, zero_div]
  · intro h
    simp only [value, isNeutral] at h ⊢
    have h2 : (2 : ℝ) ≠ 0 := by norm_num
    have h' : ((C.numPositive : ℝ) - C.numNegative) / 2 = 0 := h
    rw [div_eq_zero_iff] at h'
    cases h' with
    | inl hsub =>
      have : (C.numPositive : ℝ) = (C.numNegative : ℝ) := sub_eq_zero.mp hsub
      exact_mod_cast this
    | inr h2z => exact absurd h2z h2

/-- The coefficient of the ANTISYMMETRIC (Coulomb) channel: ½(n₊ + n₋).

    **CORRECTED 2026-08-29 (bean `qou-toul`).** This file previously
    defined `coulombCorrection = value * (q − q⁻¹)`, i.e. it multiplied the
    halved *writhe* `Q` into the antisymmetric channel. That is the swapped
    assignment: by `prop:crossing-energy-decomposition` the antisymmetric
    `sinh` weight is blind to the crossing sign, so its multiplicity is the
    crossing COUNT, and `Q` is the coefficient of the symmetric channel.
    `QOU.Braiding.CrossingEnergy.swapped_decomposition_off_by` states the
    failure quantitatively. -/
noncomputable def CoulombCharge.antisymCoefficient (C : CoulombCharge) : ℝ :=
  ((C.numPositive : ℝ) + C.numNegative) / 2

/-- The Coulomb (antisymmetric) contribution: ½(n₊ + n₋)(q − q⁻¹). -/
-- Ref: [leitner2026] Ch. 4, §10
noncomputable def CoulombCharge.coulombContribution (C : CoulombCharge) (q : ℝ) : ℝ :=
  C.antisymCoefficient * (q - q⁻¹)

/-- The symmetric (strong) contribution: Q(H) · (q + q⁻¹).
    `Q` — the halved writhe — is the coefficient of THIS channel. -/
-- Ref: [leitner2026] Ch. 4, §10
noncomputable def CoulombCharge.strongContribution (C : CoulombCharge) (q : ℝ) : ℝ :=
  C.value * (q + q⁻¹)

/-- The Coulomb contribution vanishes at q = 1 (undeformed limit). -/
-- Ref: [leitner2026] Ch. 4, §10
theorem CoulombCharge.coulombContribution_at_one (C : CoulombCharge) :
    C.coulombContribution 1 = 0 := by
  simp [coulombContribution, inv_one, sub_self, mul_zero]

/-- The Coulomb contribution is antisymmetric under q ↔ q⁻¹. -/
-- Ref: [leitner2026] Ch. 4, §10
theorem CoulombCharge.coulombContribution_antisymmetric
    (C : CoulombCharge) (q : ℝ) (_hq : q ≠ 0) :
    C.coulombContribution q⁻¹ = -C.coulombContribution q := by
  simp [coulombContribution, inv_inv]
  ring

/-- **The Coulomb coefficient is never negative.**

    This is the falsifiable consequence of the corrected assignment, and it
    is why `Q` cannot be read as an electric charge on the strength of this
    decomposition alone: the antisymmetric channel admits no attractive
    sign, so the trichotomy `Q ≶ 0 ↦ repulsive/attractive` that this block
    previously asserted has no representative. -/
theorem CoulombCharge.antisymCoefficient_nonneg (C : CoulombCharge) :
    0 ≤ C.antisymCoefficient := by
  unfold antisymCoefficient
  positivity

/-- The Coulomb coefficient vanishes only for the empty braid word — not on
    the `n₊ = n₋` locus, which annihilates the SYMMETRIC channel instead. -/
theorem CoulombCharge.antisymCoefficient_eq_zero_iff (C : CoulombCharge) :
    C.antisymCoefficient = 0 ↔ C.numPositive = 0 ∧ C.numNegative = 0 := by
  unfold antisymCoefficient
  constructor
  · intro h
    have h2 : (C.numPositive : ℝ) + C.numNegative = 0 := by
      field_simp at h; exact_mod_cast h
    constructor <;> [skip; skip] <;>
      · have hp : (0 : ℝ) ≤ C.numPositive := Nat.cast_nonneg _
        have hn : (0 : ℝ) ≤ C.numNegative := Nat.cast_nonneg _
        first
        | (have : (C.numPositive : ℝ) = 0 := by linarith
           exact_mod_cast this)
        | (have : (C.numNegative : ℝ) = 0 := by linarith
           exact_mod_cast this)
  · rintro ⟨hp, hn⟩; rw [hp, hn]; norm_num


/-! ## The mirror, and why the asserted quark charges are not derivable from it

`def:down-quark` states that the down quark "differs from the up quark only
by crossing orientation", and `down-quark.lean` proves exactly that
(`QOU.Archimedean.quark_crossing_asymmetry`). The declarations below record
what that mechanism forces, and what it therefore cannot deliver.

The obstruction is *mechanism-independent*: only oddness of the charge under
orientation reversal is used, never the particular form `(n₊ − n₋)/2`. The
exact enumeration is
`computations/probes/quark_charge_mirror_obstruction_probe.py`.
-/

/-- Reversing every crossing: the mirror of a braid word. -/
def CoulombCharge.mirror (C : CoulombCharge) : CoulombCharge :=
  { numPositive := C.numNegative, numNegative := C.numPositive }

/-- **`Q` is odd under the mirror.** This is the invariant the whole
    obstruction rests on. -/
theorem CoulombCharge.value_mirror (C : CoulombCharge) :
    C.mirror.value = -C.value := by
  simp only [mirror, value]
  ring

/-- A mirror pair carries equal magnitudes, so its charge ratio is `-1` for
    every crossing count. -/
theorem CoulombCharge.abs_value_mirror (C : CoulombCharge) :
    |C.mirror.value| = |C.value| := by
  rw [value_mirror, abs_neg]

/-- **The asserted pair `(+2/3, −1/3)` is not a mirror pair.**

    The two blocks state a mechanism that forces `Q(d) = −Q(u)` and then
    assert a pair whose ratio is `−2`. No crossing count repairs this: it is
    a statement about the symmetry, not about the counts. -/
theorem asserted_quark_charges_not_mirror_odd :
    ¬ ∃ qu : ℝ, qu = 2 / 3 ∧ -qu = -1 / 3 := by
  rintro ⟨qu, h1, h2⟩
  rw [h1] at h2
  norm_num at h2

/-- **A mirror-odd charge makes the neutron the proton's exact opposite.**

    With the proton `uud` and the neutron `udd`, oddness alone gives
    `Q(n) = −Q(p)`. Nothing about crossing counts, `q`, or the particular
    charge formula enters. -/
theorem neutron_charge_eq_neg_proton_charge (qu qd : ℝ) (hmirror : qd = -qu) :
    qu + 2 * qd = -(2 * qu + qd) := by
  subst hmirror
  ring

/-- **Neutron neutrality forces every quark charge to vanish.**

    So the mechanism cannot hold a neutral neutron beside a charged proton:
    demanding the first makes the second neutral too. The Standard Model
    escapes this because it takes `|Q_u| = 2|Q_d|`, an asymmetry between the
    two orientations that a pure mirror cannot supply. -/
theorem mirror_odd_neutral_neutron_forces_zero (qu qd : ℝ) (hmirror : qd = -qu)
    (hneutral : qu + 2 * qd = 0) : qu = 0 ∧ 2 * qu + qd = 0 := by
  subst hmirror
  constructor <;> linarith


end QOU.Braiding
