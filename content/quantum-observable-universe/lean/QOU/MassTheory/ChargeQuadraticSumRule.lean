import Mathlib.Tactic

/-!
# QOU.MassTheory.ChargeQuadraticSumRule — what a quadratic-in-charge EM term can and cannot say

Bean `qou-bn8e`. The corpus derives the charge structure of the neutron–proton
electromagnetic self-energy difference
(`QOU.MassTheory.NeutronProtonEMSign`), using the interaction invariant
`Σ_{i<j} qᵢqⱼ` alone and leaving one coupling free. This file asks what the
**general** quadratic-in-charge functional on a three-strand carrier permits,
and finds two things the single-invariant treatment cannot see.

## Two invariants, not one

The symmetric quadratics in `(q₁, q₂, q₃)` form a **two**-dimensional space. A
basis is the *self* term `Σ qᵢ²` and the *interaction* term `Σ_{i<j} qᵢqⱼ`; the
total charge enters as `Q² = Σqᵢ² + 2Σqᵢqⱼ`, not independently. So the general
functional is

  `E = A · Σqᵢ² + B · Σ_{i<j} qᵢqⱼ`.

Using `Σqᵢqⱼ` alone is the choice `A = 0` — the standard renormalisation
convention, in which each quark's own field energy is absorbed into its mass. It
is a **choice**, it is not derived, and `NeutronProtonEMSign` does not flag it.

## 1. The nucleon datum cannot separate `A` from `B`

`chargeSelf` and `chargeInter` differ between proton and neutron by **the same
amount**, `1/3` each (`pn_self_gap`, `pn_inter_gap`). Hence
`E(p) − E(n) = (A + B)/3` (`pn_energy_gap`): the nucleon splitting constrains
only the **sum**. Bean `qou-bn8e` previously recorded that "one scalar remains";
that was wrong — two remain, and one datum fixes one combination of them.

The corpus's **sign** result is unaffected and in fact generalises: the gap is
positive whenever `A + B > 0`, a weaker hypothesis than `B > 0`, and both
couplings are positive for a Coulomb-like energy.

## 2. Coleman–Glashow is automatic — parameter-free

Because the strange and down quarks carry the **same** charge `−1/3`, the octet's
seven baryons occupy only **three** distinct charge configurations
(`sigmaPlus_config_eq_proton`, `xiZero_config_eq_neutron`,
`xiMinus_config_eq_sigmaMinus`). Three configurations and two couplings leave
exactly one relation, and it holds identically in `A` and `B`
(`coleman_glashow`):

  `(mₙ − m_p) − (m_Σ⁻ − m_Σ⁺) + (m_Ξ⁻ − m_Ξ⁰) = 0`.

That is the Coleman–Glashow relation, obtained here with **no fitted quantity**:
it does not depend on the couplings, on `q`, or on any length scale. Measured, it
holds to `0.064 MeV` — `0.80 %` of its largest term and inside the combined PDG
error on the hyperon masses.

**This is the first parameter-free consequence the EM sector yields on this
branch**, and it is a genuine prediction rather than a postdiction of a number:
any EM self-energy that is quadratic in the strand charges satisfies it, so a
measured violation would refute the whole class at once.

## What this does NOT do

It does **not** derive either coupling, so `qou-bn8e`'s target — the magnitude —
is untouched. It says the magnitude question needs a **second** measured
splitting to separate `A` from `B`, and that the Σ triplet supplies one (its
configuration difference is `(2/3, −1/3)`, not proportional to the nucleon's
`(1/3, 1/3)`).

It also does not claim the EM self-energy *is* quadratic in the charges. That is
the hypothesis under test; Coleman–Glashow holding is evidence for it, and the
relation is what makes the hypothesis falsifiable.

Everything is over `ℚ` — charges and couplings are rational, no archimedean
construct appears (§7c).

-- Ref: [manuscript] prop:neutron-proton-mass-splitting
-/

namespace QOU.MassTheory.ChargeQuadraticSumRule

/-- Up-quark charge. -/
def qU : ℚ := 2 / 3
/-- Down-quark charge. -/
def qD : ℚ := -1 / 3
/-- Strange-quark charge — **equal to the down**, which is why the octet
collapses to three charge configurations. -/
def qS : ℚ := -1 / 3

/-- The *self* invariant `Σ qᵢ²`. -/
def chargeSelf (a b c : ℚ) : ℚ := a * a + b * b + c * c

/-- The *interaction* invariant `Σ_{i<j} qᵢqⱼ` — the one the corpus uses. -/
def chargeInter (a b c : ℚ) : ℚ := a * b + a * c + b * c

/-- The general quadratic-in-charge energy: `A` on the self term, `B` on the
interaction term. -/
def energy (A B a b c : ℚ) : ℚ := A * chargeSelf a b c + B * chargeInter a b c

/-- Total charge is not an independent invariant: `Q² = Σqᵢ² + 2Σqᵢqⱼ`. -/
theorem totalCharge_sq (a b c : ℚ) :
    (a + b + c) ^ 2 = chargeSelf a b c + 2 * chargeInter a b c := by
  simp only [chargeSelf, chargeInter]; ring

/-! ### The nucleon datum is degenerate -/

/-- Proton `uud` and neutron `udd` differ in the **self** invariant by `1/3`. -/
theorem pn_self_gap : chargeSelf qU qU qD - chargeSelf qU qD qD = 1 / 3 := by
  simp only [chargeSelf, qU, qD]; norm_num

/-- …and in the **interaction** invariant by `1/3` as well — the same amount. -/
theorem pn_inter_gap : chargeInter qU qU qD - chargeInter qU qD qD = 1 / 3 := by
  simp only [chargeInter, qU, qD]; norm_num

/-- **The nucleon splitting constrains only `A + B`.** Both invariants move by
`1/3`, so the two couplings enter only through their sum and no measurement of
this one difference can separate them. -/
theorem pn_energy_gap (A B : ℚ) :
    energy A B qU qU qD - energy A B qU qD qD = (A + B) / 3 := by
  simp only [energy, chargeSelf, chargeInter, qU, qD]; ring

/-! ### The octet has only three charge configurations -/

/-- `Σ⁺ = uus` carries the proton's charge configuration. -/
theorem sigmaPlus_config_eq_proton :
    chargeSelf qU qU qS = chargeSelf qU qU qD ∧
      chargeInter qU qU qS = chargeInter qU qU qD := by
  constructor <;> norm_num [chargeSelf, chargeInter, qU, qD, qS]

/-- `Ξ⁰ = uss` carries the neutron's. -/
theorem xiZero_config_eq_neutron :
    chargeSelf qU qS qS = chargeSelf qU qD qD ∧
      chargeInter qU qS qS = chargeInter qU qD qD := by
  constructor <;> norm_num [chargeSelf, chargeInter, qU, qD, qS]

/-- `Ξ⁻ = dss` carries `Σ⁻ = dds`'s. -/
theorem xiMinus_config_eq_sigmaMinus :
    chargeSelf qD qS qS = chargeSelf qD qD qS ∧
      chargeInter qD qS qS = chargeInter qD qD qS := by
  constructor <;> norm_num [chargeSelf, chargeInter, qU, qD, qS]

/-! ### The sum rule -/

/-- **Coleman–Glashow, parameter-free.** For *every* pair of couplings `(A, B)`,

  `(E(n) − E(p)) − (E(Σ⁻) − E(Σ⁺)) + (E(Ξ⁻) − E(Ξ⁰)) = 0`.

Three charge configurations and two couplings leave exactly one relation, and
this is it. Nothing here depends on the couplings, on `q`, or on a length scale,
so any EM self-energy quadratic in the strand charges satisfies it — and a
measured violation refutes that whole class. Measured residual: `0.064 MeV`,
`0.80 %` of the largest term, inside the combined PDG error. -/
theorem coleman_glashow (A B : ℚ) :
    (energy A B qU qD qD - energy A B qU qU qD)
      - (energy A B qD qD qS - energy A B qU qU qS)
      + (energy A B qD qS qS - energy A B qU qS qS) = 0 := by
  simp only [energy, chargeSelf, chargeInter, qU, qD, qS]; ring

/-- The Σ triplet is **not** degenerate the way the nucleon is: its configuration
difference is `(2/3, −1/3)`, which is not proportional to the nucleon's
`(1/3, 1/3)`. So `Σ⁺ − Σ⁻` together with `p − n` does separate `A` from `B`. -/
theorem sigma_gap_independent :
    chargeSelf qU qU qS - chargeSelf qD qD qS = 2 / 3 ∧
      chargeInter qU qU qS - chargeInter qD qD qS = -1 / 3 := by
  constructor <;> norm_num [chargeSelf, chargeInter, qU, qD, qS]

/-- Made precise: the two configuration-difference vectors are linearly
independent, so the two splittings determine `A` and `B` separately. The
determinant `(1/3)(−1/3) − (1/3)(2/3) = −1/3` is nonzero. -/
theorem pn_sigma_determinant_ne_zero :
    (chargeSelf qU qU qD - chargeSelf qU qD qD)
        * (chargeInter qU qU qS - chargeInter qD qD qS)
      - (chargeInter qU qU qD - chargeInter qU qD qD)
        * (chargeSelf qU qU qS - chargeSelf qD qD qS) ≠ 0 := by
  simp only [chargeSelf, chargeInter, qU, qD, qS]; norm_num

end QOU.MassTheory.ChargeQuadraticSumRule
