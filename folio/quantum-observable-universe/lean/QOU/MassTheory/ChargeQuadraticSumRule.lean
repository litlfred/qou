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

## 2. Coleman–Glashow is implied — but it is NOT new, and NOT a prediction here

**Retracted claim (2026-08-29).** An earlier version of this file presented the
Coleman–Glashow relation as "the first parameter-free consequence the EM sector
yields on this branch" and as "a genuine prediction". Both are wrong, and the
corpus already said so.

`QOU/Eightfold/ColemanGlashowIdentity.lean` proves the relation sorry-free
(`coleman_glashow_identity`) from a **weaker** premise than this file's: EM
self-energy constant on a U-spin multiplet, with *three* free shifts `a, b, c`
at charge `+1, 0, −1`. The block `eightfold-way/u-spin-coleman-glashow.md`
records the same measured residual this file quotes — `−0.064 MeV`, `0.8 %` of
the largest splitting — and states the epistemics plainly: *"Reproducing
Coleman–Glashow would therefore be no evidence for this framework, or for any
other."* The quadratic-charge ansatz here is a **specialisation** of that
three-parameter family, so CG follows a fortiori and adds nothing.

## 2a. What the ansatz actually does on the octet: it saturates, so it predicts nothing

The sharper statement, and the one that is this file's own, is negative.
The octet's *observable* EM content is two-dimensional: the three splittings
`p−n`, `Σ⁺−Σ⁻`, `Ξ⁰−Ξ⁻` obey CG, leaving two independent, and an overall shift
of `a, b, c` moves all eight masses together and is absorbed into the strong
parameters. In terms of `(A, B)` those two observables are

  `a − b = (A + B)/3`,   `b − c = (A − 2B)/3`,

a linear map of determinant `−1/3 ≠ 0` (`octet_em_map_det_ne_zero`), hence a
**bijection** onto the whole two-dimensional space
(`octet_em_pattern_surjective`, which exhibits `A = 2u + v`, `B = u − v`).

Two consequences, both unwelcome and both worth stating:

* **The ansatz excludes no octet EM pattern.** Whatever the three splittings
  had come out to, some `(A, B)` reproduces them. So it makes no falsifiable
  octet prediction — not CG, not anything else.
* **`A` and `B` are exactly determined by the octet data, i.e. fitted.** The
  bijection is the obstruction, not a route: any derivation of the couplings
  must come from outside the octet.

## What this does NOT do

It does **not** derive either coupling, so `qou-bn8e`'s target — the magnitude —
is untouched. It says the magnitude question needs a **second** measured
splitting to separate `A` from `B`, and that the Σ triplet supplies one (its
configuration difference is `(2/3, −1/3)`, not proportional to the nucleon's
`(1/3, 1/3)`) — but supplying one *fits* the couplings rather than deriving
them, which is exactly the move `qou-bn8e` refuses.

It also does not claim the EM self-energy *is* quadratic in the charges, and —
correcting this file's earlier wording — Coleman–Glashow holding is **not**
evidence for that hypothesis. By `octet_em_pattern_surjective` the ansatz
reproduces every octet EM pattern, so CG could not have come out otherwise; a
test no candidate can fail discriminates nothing. `u-spin-coleman-glashow.md`
reaches the same verdict from the weaker U-spin premise. The hypothesis is
untested by the octet, and testing it needs data the octet does not contain.

Everything is over `ℚ` — charges and couplings are rational, no archimedean
construct appears (§7c).

-- Ref: [leitner2026] prop:neutron-proton-mass-splitting
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

/-- **Coleman–Glashow holds for the ansatz — as an implication, not as a result
of this file.** For every pair of couplings `(A, B)`,

  `(E(n) − E(p)) − (E(Σ⁻) − E(Σ⁺)) + (E(Ξ⁻) − E(Ξ⁰)) = 0`.

Kept only so the specialisation is visibly consistent with the corpus. The
relation is already proved from a strictly weaker premise in
`QOU/Eightfold/ColemanGlashowIdentity.lean` (`coleman_glashow_identity`, three
free U-spin shifts, any commutative ring), and `u-spin-coleman-glashow.md`
already records the `−0.064 MeV` residual. Do **not** cite this declaration as
evidence for the quadratic-charge ansatz: by `octet_em_pattern_surjective` the
ansatz reaches every octet EM pattern, so it could not have failed CG. -/
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

/-! ### Saturation: the ansatz has no octet predictive content -/

/-- The EM shift of the `Q = +1` U-spin multiplet (`p`, `Σ⁺`). -/
def emPlus (A B : ℚ) : ℚ := energy A B qU qU qD

/-- The EM shift of the `Q = 0` U-spin multiplet (`n`, `Ξ⁰`). -/
def emZero (A B : ℚ) : ℚ := energy A B qU qD qD

/-- The EM shift of the `Q = −1` U-spin multiplet (`Σ⁻`, `Ξ⁻`). -/
def emMinus (A B : ℚ) : ℚ := energy A B qD qD qS

/-- The two independent observable EM splittings, in closed form:
`a − b = (A + B)/3` and `b − c = (A − 2B)/3`. -/
theorem octet_em_gaps (A B : ℚ) :
    emPlus A B - emZero A B = (A + B) / 3 ∧
      emZero A B - emMinus A B = (A - 2 * B) / 3 := by
  constructor <;>
    simp only [emPlus, emZero, emMinus, energy, chargeSelf, chargeInter, qU, qD, qS] <;> ring

/-- The map `(A, B) ↦ (a − b, b − c)` has determinant `-1/3`, so it is
invertible. -/
theorem octet_em_map_det_ne_zero :
    (1 / 3 : ℚ) * (-2 / 3) - (1 / 3) * (1 / 3) ≠ 0 := by norm_num

/-- **The ansatz excludes no octet electromagnetic pattern.** For *any* target
pair `(u, v)` of the two independent splittings there are couplings reproducing
it, exhibited as `A = 2u + v`, `B = u − v`.

This is the file's real octet result, and it is negative: a class that reaches
every pattern forbids none, so the quadratic-charge ansatz makes no falsifiable
prediction on the baryon octet — Coleman–Glashow included. It also shows `A`
and `B` are *fitted* by the octet rather than constrained by it, which is why
`qou-bn8e` cannot be closed from this data. -/
theorem octet_em_pattern_surjective (u v : ℚ) :
    ∃ A B : ℚ, emPlus A B - emZero A B = u ∧ emZero A B - emMinus A B = v := by
  refine ⟨2 * u + v, u - v, ?_, ?_⟩ <;>
    simp only [emPlus, emZero, emMinus, energy, chargeSelf, chargeInter, qU, qD, qS] <;> ring

/-- And the couplings are uniquely determined, so the octet fixes them exactly:
two data, two parameters, no slack left over. -/
theorem octet_em_pattern_unique {A B A' B' : ℚ}
    (h1 : emPlus A B - emZero A B = emPlus A' B' - emZero A' B')
    (h2 : emZero A B - emMinus A B = emZero A' B' - emMinus A' B') :
    A = A' ∧ B = B' := by
  simp only [emPlus, emZero, emMinus, energy, chargeSelf, chargeInter, qU, qD, qS] at h1 h2
  constructor <;> linarith


/-- **Left-inverse coupling recovery and full `Σ⁺ - Σ⁻` splitting (`qou-bn8e`).**
The inverse formulas `2 * (emPlus A B - emZero A B) + (emZero A B - emMinus A B) = A`
and `(emPlus A B - emZero A B) - (emZero A B - emMinus A B) = B` recover `(A, B)` identically,
and the full `Σ⁺ - Σ⁻` gap is `emPlus A B - emMinus A B = (2 * A - B) / 3`. -/
theorem octet_em_left_inverse_and_sigma_span (A B : ℚ) :
    2 * (emPlus A B - emZero A B) + (emZero A B - emMinus A B) = A ∧
      (emPlus A B - emZero A B) - (emZero A B - emMinus A B) = B ∧
      emPlus A B - emMinus A B = (2 * A - B) / 3 := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp only [emPlus, emZero, emMinus, energy, chargeSelf, chargeInter, qU, qD, qS] <;> ring

end QOU.MassTheory.ChargeQuadraticSumRule
