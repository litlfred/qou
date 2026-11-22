/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.MarkovNormalisation

/-!
# The bond rule and the mirror cancellation (convention D)

The canonical color-weighted atom word carries, between its `A` nucleons,
exactly `A - 1` **bond** letters of the form `σ_g + d · I`:

* `Z - 1` proton-proton bonds, `d = 0`;
* `N - 1` neutron-neutron bonds, `d = -h` with `h = q - q⁻¹`;
* exactly **one** proton-neutron interface, `d = dIface`.

Measured over 16 nuclei (`A = 2 … 10`, worst relative deviation `4.45e-31`,
the compute path's own floor) and symbolically at six nuclei (`n = 6, 9, 12`),
the free-to-atom Markov-trace ratio is the product

  `tr_M^free / tr_M^atom  =  ∏_bonds 1 / (z + d_b)`,  `z = q³/(q²+1)`.

This file proves the **algebra that product form implies** — all of it
unconditionally over a generic field — and states the one trace-level input as
an explicit hypothesis rather than asserting it.

## What is proved here, unconditionally

* `markovZ_sub_h` — `z - h = z̄`, where `z̄ = z(1/q)`. The neutron-neutron bond
  letter lands **exactly** on the bar image of the Markov parameter. This is
  the non-obvious one: it is what makes `q ↦ q⁻¹` act as proton↔neutron
  conjugation on these words.
* `mirrorP_eq` — `P = 12 q⁵ (q²+1) (z + dIface)`: the degree-10 polynomial that
  governs the mirror law is exactly the interface's Markov weight with
  denominators cleared. In particular the leading `12` is `P` evaluated at
  `q = 1`, not a free constant.
* `mirrorP_bar_sub` — `q¹² P(1/q) - P(q) = (q-1)⁵ (q+1)³ (q²+1)²`, so the mirror
  offset vanishes to order **exactly 5** at the classical point.
* `bondFactor_mirror_cancel` — the cancellation itself: for **any** exponents
  `a b : ℕ`, the bond factors `z^a` and `z̄^b` cancel out of the mirror-crossed
  ratio, leaving `(z̄ + d̄) / (z + d)`. This is why the mirror offset is
  independent of the nucleus.

## What is NOT proved here

The trace-level rule

  `tr(x · (σ_g + d·I)) = (z + d) · tr(x)`   for `g` unused by `x`

is **measured, not proved** (bean `qou-g8i1`). It is carried as the single field
of `BondRule` below — a content-bearing hypothesis class in the §3b-cond sense,
never discharged here. Everything above is independent of it: `markovZ_sub_h`,
`mirrorP_eq` and `mirrorP_bar_sub` are identities of rational functions, and
`bondFactor_mirror_cancel` is stated about arbitrary elements, so it holds
whatever the traces turn out to be.

Nothing in this file computes or asserts a physical value.

## Base ring

Generic `[Field R] [CharZero R]` per the §7c convention — this is q-deformation
combinatorics with no archimedean content, and `ℝ` appears nowhere. `CharZero` is required by
`mirrorP_eq` alone, and is carried there rather than on the section variable:
that statement clears denominators of `2`, `3`, `4` and `12`, none of which is
invertible in characteristic `2` or `3`. Every other result here holds over any
field.

## Convention

Convention **D** throughout (`z = q³/(q²+1)`), per the owner ruling of
2026-08-15. `QOU.Braiding.HnMarkovTrace.MarkovTraceTower` still carries the
convention-**C** parameter `1/(√q + 1/√q)` and must **not** be used as the base
for these statements (bean `qou-um5h`).

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] docs/audits/2026-08-19-bar-involution-is-isospin-conjugation.md
-/

namespace QOU.MathlibExt.MarkovBondRule

variable {R : Type*} [Field R]

/-- The convention-D Markov parameter `z = q³/(q²+1)`. -/
noncomputable def markovZ (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- `h = q - q⁻¹`, the coefficient carried by a neutron-neutron bond letter
    (`σ_g - h·I`, whose eigenvalues are those of `σ_g⁻¹`). -/
noncomputable def hq (q : R) : R := q - q⁻¹

/-- The leading flavour split `f = (q-1)²(1 - q⁻⁴)/3` — `Δm/M_N`, the
    proton-neutron mass split (`conj:flavor-split-substrate-mass`). -/
noncomputable def flavorSplit (q : R) : R := (q - 1) ^ 2 * (1 - q⁻¹ ^ 4) / 3

/-- The coefficient of the single proton-neutron interface letter,
    `d = -h(1/2 - f/4)`. -/
noncomputable def dIface (q : R) : R := -(hq q) * (1 / 2 - flavorSplit q / 4)

/-- The degree-10 polynomial governing the mirror law. -/
noncomputable def mirrorP (q : R) : R :=
  q ^ 10 - 2 * q ^ 9 + 7 * q ^ 8 - 2 * q ^ 6 + 4 * q ^ 5 + 4 * q ^ 4
    + q ^ 2 - 2 * q + 1

/-- The bar image of the Markov parameter in closed form:
`z(1/q) = 1 / (q (q² + 1))`. -/
theorem markovZ_inv (q : R) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    markovZ q⁻¹ = 1 / (q * (q ^ 2 + 1)) := by
  have h2' : (1 : R) + q ^ 2 ≠ 0 := by rwa [add_comm]
  have key : (q⁻¹ : R) ^ 2 + 1 = q⁻¹ ^ 2 * (1 + q ^ 2) := by
    field_simp
  have hinv : (q⁻¹ : R) ^ 2 + 1 ≠ 0 := by
    rw [key]
    refine mul_ne_zero (pow_ne_zero _ (inv_ne_zero hq0)) ?_
    rwa [add_comm]
  unfold markovZ
  rw [key]
  field_simp
  ring

/-- **The neutron-neutron bond lands on the bar image of `z`.**

`z - h = z(1/q)` exactly. Under the bar involution `q ↦ q⁻¹` the Markov
parameter `z` and the neutron-neutron bond factor `z - h` are exchanged, which
is precisely the statement that bar acts as proton↔neutron conjugation on the
bond letters. Nothing about this is forced by the shapes involved; it is an
identity special to convention D. -/
theorem markovZ_sub_h (q : R) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    markovZ q - hq q = markovZ q⁻¹ := by
  rw [markovZ_inv q hq0 h2, markovZ, hq]
  field_simp
  ring

/-- **`P` is the interface's Markov weight, denominators cleared.**

`P = 12 q⁵ (q²+1) (z + dIface)`. So `P` is not an independent object: the
degree-10 polynomial, its leading coefficient and the `12` are all read off the
single interface letter. -/
theorem mirrorP_eq [CharZero R] (q : R) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    mirrorP q = 12 * q ^ 5 * (q ^ 2 + 1) * (markovZ q + dIface q) := by
  unfold mirrorP markovZ dIface hq flavorSplit
  field_simp
  ring

/-- **The mirror offset vanishes to order exactly 5.**

`q¹² P(1/q) - P(q) = (q-1)⁵ (q+1)³ (q²+1)²`. The right side is a product of
powers of `q-1`, `q+1` and `q²+1`, with `(q-1)` appearing to the fifth power —
so the offset is `O(h⁵)` at the classical point, and that order is derived
rather than observed. -/
theorem mirrorP_bar_sub (q : R) (hq0 : q ≠ 0) :
    q ^ 12 * mirrorP q⁻¹ - mirrorP q
      = (q - 1) ^ 5 * (q + 1) ^ 3 * (q ^ 2 + 1) ^ 2 := by
  unfold mirrorP
  field_simp
  ring

/-- **The bond factors cancel out of the mirror-crossed ratio.**

Given the product form, a nucleus `(Z,N)` contributes `z^(Z-1)` from its
proton-proton bonds and `z̄^(N-1)` from its neutron-neutron bonds, and its
mirror `(N,Z)` evaluated at `1/q` contributes the *same two factors* with the
roles exchanged. They cancel identically, for **any** exponents — which is why
the mirror offset does not depend on the nucleus.

Stated about arbitrary ring elements so that it is independent of everything
else in this file: `zz` and `zb` stand for the two bond factors and `w`, `wb`
for the interface factor and its bar image. -/
theorem bondFactor_mirror_cancel (zz zb w wb : R) (a b : ℕ)
    (hz : zz ≠ 0) (hzb : zb ≠ 0) (hw : w ≠ 0) (hwb : wb ≠ 0) :
    (1 / (zz ^ a * zb ^ b * w)) / (1 / (zb ^ b * zz ^ a * wb)) = wb / w := by
  have ha : zz ^ a ≠ 0 := pow_ne_zero _ hz
  have hb : zb ^ b ≠ 0 := pow_ne_zero _ hzb
  field_simp

/-- **The one trace-level input, carried as a hypothesis and never discharged.**

`tr` is the Jones–Markov trace, `mul` the algebra multiplication, and `sigmaPlus
g d` the bond letter `σ_g + d·I`. The field says that appending a bond letter at
a generator the element does not use multiplies the trace by `z + d`.

This is **measured, not proved** — 16 nuclei numerically to `4.45e-31`, six
symbolically. The mechanism is multiplicativity of the trace across an unused
generator (the two sides then lie in commuting subalgebras) followed by the
Markov property; formalising that chain is bean `qou-g8i1`.

It is a genuine hypothesis in the §3b-cond sense: the field is a
parameter-quantified equation in the shape of the claim, not a marker, and no
instance is provided. -/
class BondRule (R : Type*) [Field R] (A : Type*) (q : R) where
  /-- The Jones–Markov trace. -/
  tr : A → R
  /-- Algebra multiplication. -/
  mul : A → A → A
  /-- The bond letter `σ_g + d·I` at generator `g`. -/
  sigmaPlus : ℕ → R → A
  /-- `g` is not used by `x`. -/
  Unused : ℕ → A → Prop
  /-- **The bond rule.** -/
  tr_mul_sigmaPlus :
    ∀ (x : A) (g : ℕ) (d : R), Unused g x →
      tr (mul x (sigmaPlus g d)) = (markovZ q + d) * tr x

/-- A proton-proton bond (`d = 0`) contributes exactly `z`, and a
neutron-neutron bond (`d = -h`) contributes exactly `z̄` — the two are bar
images of one another, by `markovZ_sub_h`. Conditional on `BondRule`. -/
theorem bond_pp_nn {A : Type*} {q : R} [BondRule R A q]
    (x : A) (g g' : ℕ) (hx : BondRule.Unused (R := R) (q := q) g x)
    (hx' : BondRule.Unused (R := R) (q := q) g' x)
    (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    BondRule.tr (q := q) (BondRule.mul (R := R) (q := q) x
        (BondRule.sigmaPlus (R := R) (q := q) g 0))
      = markovZ q * BondRule.tr (q := q) x
    ∧ BondRule.tr (q := q) (BondRule.mul (R := R) (q := q) x
        (BondRule.sigmaPlus (R := R) (q := q) g' (-(hq q))))
      = markovZ q⁻¹ * BondRule.tr (q := q) x := by
  constructor
  · have := BondRule.tr_mul_sigmaPlus (R := R) (q := q) x g 0 hx
    simpa using this
  · have := BondRule.tr_mul_sigmaPlus (R := R) (q := q) x g' (-(hq q)) hx'
    rw [this, ← markovZ_sub_h q hq0 h2]
    ring

end QOU.MathlibExt.MarkovBondRule
