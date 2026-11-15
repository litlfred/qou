/-
# Which bar-odd offsets are available to the p-n bond, and what does not pick one

`QOU.MassTheory.PnInterfaceBarStructure` establishes the criterion: the weighted
p-n interface factor `f_pn = z - (1/2 - ε)·h` is `q`-bar-even **iff the offset
`ε` is bar-ODD**.  The canonical bring-color-weighted offset `ε = δ/4` is not:
`δ` is bar-odd only up to the weight `q²` (`bar δ = -q²·δ`).

The obvious repair is to absorb that weight — `ε = q·δ·E/4` with `E` bar-even is
bar-odd for **every** such `E` (`weightForm_barOdd`).  This file is about what
that frame can and cannot reach, because the answer turned out to bear on
whether "which `E`?" is the right question at all.

## What is proved here

1. `weightForm_barOdd` — the repair works for any bar-even `E`, with no
   further hypothesis.  The class is therefore as large as the bar-even
   functions, and the criterion alone selects nothing inside it.

2. `weightForm_cubic_factor` — `(q-1)³` divides every member of the class whose
   `E` is regular at `q = 1`, because `δ` itself vanishes to third order.  So a
   regular-`E` repair can only ever move `f_pn` by `O((q-1)³)` from the
   strict-averaged factor `z - h/2`.  This is the constraint that does the work
   below.

3. `bond_barInvariant_iff_barOdd` — the criterion is not an accident of the
   trace.  The p-n **bond element** `σ + d·1` of the Hecke algebra is invariant
   under the Kazhdan–Lusztig bar (`σ ↦ σ⁻¹` together with `q ↦ q⁻¹`) exactly
   when `ε` is bar-odd.  Bar-evenness of the *factor* is the shadow of
   bar-invariance of the *bond*; and the p-p and n-n bonds `σ`, `σ⁻¹` are not
   individually invariant but are exchanged, which is the algebra-level source
   of `QOU.Hecke.ClosedForm.fPP_bar_eq_fNN`.

4. `geomMean_sq`, `geomMean_offset`, `geomMean_offset_barOdd` — there is a
   second structurally-derived bar-even p-n factor besides the strict average.
   The two like-flavour factors are a bar orbit `(z, bar z) = (z, z/q⁴)`; their
   **arithmetic** mean is `z - h/2` (offset `ε = 0`), and their **geometric**
   mean is `√(z·bar z) = z/q²`, which is also bar-even and corresponds to the
   bar-odd offset `ε = -(q²-1)/(2(q²+1))`.

5. `geomMean_offset_needs_double_pole` — and that second candidate is **outside**
   the frame.  Its offset is `O(q-1)`, not `O((q-1)³)`, so by (2) no regular
   `E` reaches it: the required `E = -6q³/((q-1)²(q²+1)²)` is bar-even but has a
   double pole at `q = 1`, witnessed here by `(q-1)²·E` evaluating to `-3/2`
   rather than to `0`.

## What this means for the search

The frame `ε = q·δ·E/4` presupposes that the p-n offset is a *reweighting of the
colour-tube split `δ`*, and (2) says everything it can produce stays within
`O((q-1)³)` of the strict average — the same size as the canonical convention
itself.  The one other candidate the bond structure actually supplies is a
hundredfold larger and of the opposite sign, and (5) says it cannot be written
in that frame.

So "which bar-even `E`?" is not a question the criterion answers, and none of
confluence at `q = 1`, the Markov bond form, or the convex-weight bound
`|ε| ≤ 1/2` narrows it either — see
`computations/probes/pn_offset_bar_odd_class_probe.py`, which checks each.
Selecting an `E` from an isotope anchor would be a fit, not a derivation, and is
not done here.  The question that *does* have a structural route is the prior
one: whether the p-n bond interpolates its two neighbours arithmetically (the
Markov trace is linear) or geometrically (the closed form is a product over
bonds).  That is left open.

## Scope

Every statement is an identity in a field of characteristic zero.  As in
`PnInterfaceBarStructure`, the bar image of a quantity is supplied by the caller
as a *value* rather than constructed as an involution: the conclusions depend
only on the relations between a quantity and its image, not on how the
involution is realised.  `CharZero` is genuine content — the offsets are
half-weights and the flavour split carries a `1/3`, so `2`, `3` and `12` must be
invertible.

No claim is made here that any offset is physically correct.

## Base ring: why `Field` here, and what it would take to weaken it

`[Field K] [CharZero K]` is stronger than the base ring the owner fixed on
2026-08-26 (`R = ℤ[q,q⁻¹][Φ_d(q)⁻¹ : d ≥ 2]`, carried as the property
`IsQGeneric`).  Recorded deliberately, with what a migration would need, since
that drain is an active tranche and this file is new inventory for it:

* `markovZ` needs `(q²+1)⁻¹`, and `q² + 1 = Φ₄(q)` — so it is **already** a unit
  under `IsQGeneric`.  Same for every `q⁻ⁿ`.
* What `IsQGeneric` does **not** give is `2⁻¹` and `3⁻¹`: the offsets are half
  weights and `δ` carries a `1/3`.  A migration needs `Invertible (2 : R)` and
  `Invertible (3 : R)` alongside it, plus `NoZeroDivisors` for the
  `mul_eq_zero` step in `bond_barInvariant_iff_barOdd`.
* The `q = 1` reasoning survives the move and is the reason to want it.  That
  ruling inverts `Φ_d` only for `d ≥ 2`, so `Φ₁(q) = q - 1` stays a non-unit and
  `q = 1` remains a point of `Spec R` — which is exactly where
  `weightForm_cubic_factor` and the pole statements live.  Over a field one
  reasons about that point by evaluation; over `R` the same facts are the
  divisibility statements they are already written as, so nothing here is
  *proved* by the field structure.

Not done in this PR: the ruling landed the same day, its migration is owned
elsewhere, and the sibling `PnInterfaceBarStructure` is `[Field K] [CharZero K]`
too — moving one of the pair and not the other makes both harder to migrate.

-- Ref: [leitner2026] mass-theory/interface-knot-markov-z-proof.md,
--      §"The three factors are one bar-orbit"
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination

namespace QOU.MassTheory.PnOffset

set_option linter.unusedSectionVars false

variable {K : Type*} [Field K] [CharZero K]

/-- The Markov parameter in convention D, `z = q³/(q²+1)`. -/
noncomputable def markovZ (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- The Hecke skein parameter, `h = q - q⁻¹`. -/
noncomputable def heckeH (q : K) : K := q - q⁻¹

/-- The proven leading flavour split, `δ = (q-1)²·(1 - q⁻⁴)/3`. -/
noncomputable def flavorDelta (q : K) : K := (q - 1) ^ 2 * (1 - (q ^ 4)⁻¹) / 3

/-- The weighted p-n interface factor with offset `ε`:
`f_pn = (1/2 + ε)·z + (1/2 - ε)·(z - h) = z - (1/2 - ε)·h`. -/
noncomputable def fPN (q ε : K) : K := markovZ q - (1 / 2 - ε) * heckeH q

/-! ## §1. The repair class `ε = q·δ·E/4` -/

/-- **Absorbing the weight makes the offset bar-odd, for every bar-even `E`.**

`bar q = q⁻¹`, `bar δ = -q²·δ` (`PnInterfaceBarStructure`, `ClosedForm.flavorDelta_bar`)
and `bar E = E` by hypothesis, so the bar image of `ε = q·δ·E/4` is
`q⁻¹·(-q²·δ)·E/4 = -ε`.

The bar images are supplied as the substituted values; the statement is the
resulting identity.  Note there is **no** hypothesis on `E` beyond bar-evenness
having already been used to write `E` on both sides: the criterion of
`pnWeighted_barEven_iff` selects nothing within this class. -/
theorem weightForm_barOdd (q δ E : K) (hq : q ≠ 0) :
    q⁻¹ * (-(q ^ 2) * δ) * E / 4 = -(q * δ * E / 4) := by
  field_simp

/-- **Every member of the class with `E` regular at `q = 1` vanishes to third
order there**, because `δ` does.

`δ` carries the factor `(q-1)²` explicitly and a further `(q-1)` inside
`1 - q⁻⁴ = (q⁴-1)/q⁴`; pulling all three out leaves a cofactor in which `q = 1`
may be substituted freely.  Consequently a regular-`E` repair moves `f_pn` from
the strict-averaged `z - h/2` by `O((q-1)³)` — the same order as the canonical
`δ/4` it is meant to replace.  This is what excludes the geometric-mean
candidate of §3 from the class. -/
theorem weightForm_cubic_factor (q E : K) (hq : q ≠ 0) :
    q * flavorDelta q * E / 4
      = (q - 1) ^ 3 * (q * (q + 1) * (q ^ 2 + 1) * E / (12 * q ^ 4)) := by
  unfold flavorDelta
  field_simp
  ring

/-! ## §2. The criterion is a Kazhdan–Lusztig bar-invariance of the bond -/

/-- Constant term of the p-n bond element `σ + d·1` whose Markov trace is
`f_pn`: from `f_pn = z + d` and `f_pn = z - (1/2 - ε)·h`, `d = -(1/2 - ε)·h`. -/
noncomputable def bondConst (h ε : K) : K := -(1 / 2 - ε) * h

/-- `f_pn` is the trace `z + d` of the bond, as
`QOU.Hecke.ClosedForm.interfaceFactor_eq_bond_expectation` has it for the
like-flavour bonds. -/
theorem fPN_eq_markovZ_add_bondConst (q ε : K) :
    fPN q ε = markovZ q + bondConst (heckeH q) ε := by
  unfold fPN bondConst
  ring

/-- **Bar defect of the bond.**

The Kazhdan–Lusztig bar sends `σ ↦ σ⁻¹ = σ - h` and `q ↦ q⁻¹`, so
`bar(σ + d·1) = σ + (d' - h)·1` where `d'` is the bar image of the constant.
Its difference from the original constant is `(1 - ε - ε')·h`, using `bar h = -h`
(`ClosedForm.heckeH_bar`).  Invariance is `d' - h = d`, i.e. this difference
equalling `h`. -/
theorem bondConst_bar_sub (h ε ε' : K) :
    bondConst (-h) ε' - bondConst h ε = (1 - ε - ε') * h := by
  unfold bondConst
  ring

/-- **The p-n bond is KL-bar-invariant exactly when the offset is bar-odd.**

So the bar-evenness of the interface *factor* is not a property of the trace: it
is the shadow of an invariance of the bond *element*, and the two statements
carry the same content.  Requires `h ≠ 0`, i.e. `q² ≠ 1` — at the classical
point every bond is invariant for trivial reasons. -/
theorem bond_barInvariant_iff_barOdd (h ε ε' : K) (hh : h ≠ 0) :
    bondConst (-h) ε' - bondConst h ε = h ↔ ε' = -ε := by
  rw [bondConst_bar_sub]
  constructor
  · intro hEq
    have hz : -(ε + ε') * h = 0 := by linear_combination hEq
    rcases mul_eq_zero.mp hz with hs | hz'
    · have hsum : ε + ε' = 0 := by linear_combination -hs
      linear_combination hsum
    · exact absurd hz' hh
  · intro hEq
    rw [hEq]
    ring

/-- **The like-flavour bonds are a bar orbit, not two fixed points.**

`σ` is the offset-`1/2` member of the family and `σ⁻¹` the offset-`(-1/2)` one;
their bond constants are `0` and `-h`, and the bar defect of each is `h` in
magnitude but neither satisfies the invariance criterion — instead the bar
carries each onto the other.  Stated as the failure of
`bond_barInvariant_iff_barOdd` at `ε' = ε = 1/2`: the defect is `0`, not `h`.

This is the algebra-level source of `QOU.Hecke.ClosedForm.fPP_bar_eq_fNN` /
`fNN_bar_eq_fPP`. -/
theorem likeFlavour_bond_not_barInvariant (h : K) (hh : h ≠ 0) :
    bondConst (-h) (1 / 2) - bondConst h (1 / 2) ≠ h := by
  rw [bondConst_bar_sub]
  intro hEq
  exact hh (by linear_combination -hEq)

/-! ## §3. The second derived candidate, and why the class misses it -/

/-- **The geometric mean of the bar orbit is `z/q²`**: `(z/q²)² = z·(z - h)`.

`f_pp = z` and `f_nn = z - h = z/q⁴` are a single bar orbit
(`ClosedForm.markovZ_bar_eq_shift`), so their product is the bar-norm `z²/q⁴`
and its square root `z/q²` is bar-even.  It is therefore an admissible p-n
factor by the criterion — a second structurally-derived candidate alongside the
arithmetic mean `z - h/2`. -/
theorem geomMean_sq (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    (markovZ q / q ^ 2) ^ 2 = markovZ q * (markovZ q - heckeH q) := by
  unfold markovZ heckeH
  field_simp
  ring

/-- **The offset realising the geometric mean** is
`ε = -(q²-1)/(2(q²+1))`. -/
theorem geomMean_offset (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    fPN q (-((q ^ 2 - 1) / (2 * (q ^ 2 + 1)))) = markovZ q / q ^ 2 := by
  unfold fPN markovZ heckeH
  field_simp
  ring

/-- That offset is bar-odd, as the criterion requires: substituting `q ↦ q⁻¹`
returns its negative. -/
theorem geomMean_offset_barOdd (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    -(((q⁻¹) ^ 2 - 1) / (2 * ((q⁻¹) ^ 2 + 1)))
      = -(-((q ^ 2 - 1) / (2 * (q ^ 2 + 1)))) := by
  have hqq : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have hq2' : (1 : K) + q ^ 2 ≠ 0 := by rwa [add_comm]
  field_simp
  ring

/-- **The `E` that would reach the geometric mean.** -/
theorem geomMean_via_weightForm (q : K) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    q * flavorDelta q * (-(6 * q ^ 3) / ((q - 1) ^ 2 * (q ^ 2 + 1) ^ 2)) / 4
      = -((q ^ 2 - 1) / (2 * (q ^ 2 + 1))) := by
  unfold flavorDelta
  field_simp
  ring

/-- **…and it has a double pole at `q = 1`, so the class does not contain it.**

Clearing the candidate pole leaves `-6q³/(q²+1)²`, a quantity regular at
`q = 1`.  Together with `geomMean_pole_residue_at_one` (its value there is
`-3/2`, not `0`) this says the pole is genuine and of order exactly two: it does
not cancel.  With `weightForm_cubic_factor` — every regular `E` gives an offset
divisible by `(q-1)³` — that is the sharp statement that the geometric-mean
candidate is unreachable inside `ε = q·δ·E/4`, and hence that the frame is
narrower than the set of bar-even p-n factors it was meant to parametrise. -/
theorem geomMean_pole_residue (q : K) (hq1 : q - 1 ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    (q - 1) ^ 2 * (-(6 * q ^ 3) / ((q - 1) ^ 2 * (q ^ 2 + 1) ^ 2))
      = -(6 * q ^ 3) / (q ^ 2 + 1) ^ 2 := by
  have h1 : (q - 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq1
  field_simp

/-- The residue at the classical point is `-3/2`, hence nonzero: the pole is
genuine and of order exactly two. -/
theorem geomMean_pole_residue_at_one :
    -(6 * (1 : K) ^ 3) / ((1 : K) ^ 2 + 1) ^ 2 = -(3 / 2) := by
  norm_num

/-! ## §4. Arithmetic or geometric? The product-over-bonds argument is unsound -/

/-- **The product of the two like-flavour factors, in closed form.**

`f_pp · f_nn = (q/(q²+1))²`, which is `(z/q²)²` — consistent with `geomMean_sq`,
and the reason the geometric mean is `z/q²` in the first place. -/
theorem fPP_mul_fNN_eq (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    markovZ q * (markovZ q - heckeH q) = (q / (q ^ 2 + 1)) ^ 2 := by
  unfold markovZ heckeH
  field_simp
  ring

/-- **The product of the FACTORS is not the trace of the product of the BONDS,
and misses it by at least `3/4` at every `q`.**

This is the statement that decides the arithmetic-vs-geometric question, so it
is worth being explicit about what the two sides are.

* The two like-flavour bonds are the Hecke elements `σ` (p-p, `d = 0`) and
  `σ - h·1 = σ⁻¹` (n-n, `d = -h`) — see `bondD` and
  `QOU.Hecke.ClosedForm.interfaceFactor_eq_bond_expectation`.  They are
  **mutually inverse**, so their product in the algebra is the identity, whose
  Markov-trace expectation is `τ(1) = 1` (the normalisation that
  `f_k = z + d_k` already assumes).
* Their two *factors* are `f_pp` and `f_nn`, and this theorem says
  `1 - f_pp·f_nn` is a square plus `3/4`.  So over any ordered field
  `f_pp·f_nn ≤ 1/4`, never `1`, and the two sides differ by a factor of at
  least four.

Hence the Markov trace is **not** multiplicative on these bonds — it could not
be, since a bond and its inverse would have to have reciprocal traces — and the
closed form's product over bonds is a product of *traces*, not the trace of a
*product*.

**The consequence for the fork.**  The case for the geometric mean was that the
closed form is a product, so the multiplicative midpoint of two neighbouring
factors is the natural interpolation.  That argument takes a geometric mean at
the level of *factors* while borrowing its motivation from a multiplicative
structure that exists only at the level of *elements* — and the two levels are
not connected here, by this theorem.  At the element level the multiplicative
midpoint of `σ` and `σ⁻¹` is the identity, with trace `1`, which is not the
geometric mean `z/q²` of the factors (`0.497` at the proton pin) nor anything
else in the family.

The arithmetic mean has no such gap: the Markov trace is **linear**, so
`(f_pp + f_nn)/2` is exactly the trace of `(σ + σ⁻¹)/2`, the skein symmetriser
that `QOU.BraidKnot.interface_knot_markov_z_bar_symmetric` is already stated
about, and `arithMean_bondConst_eq_midpoint` records that its bond constant is
the midpoint of the other two.

**Scope.**  This is a statement about which of the two candidate interpolations
has algebraic backing, not a derivation of the physical offset.  It removes the
structural argument for the geometric mean; it does **not** establish that
`ε = 0` is correct, and the colour-tube correction `δ/4` sits on top of the
arithmetic mean either way. -/
theorem one_sub_fPP_mul_fNN (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    1 - markovZ q * (markovZ q - heckeH q)
      = ((q ^ 2 - 1) / (2 * (q ^ 2 + 1))) ^ 2 + 3 / 4 := by
  unfold markovZ heckeH
  field_simp
  ring

/-- The same identity in the form that gives the bound directly:
`1/4 - f_pp·f_nn` is a square, so `f_pp·f_nn ≤ 1/4` over any ordered field,
with equality exactly at `q² = 1`. -/
theorem quarter_sub_fPP_mul_fNN (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    1 / 4 - markovZ q * (markovZ q - heckeH q)
      = ((q ^ 2 - 1) / (2 * (q ^ 2 + 1))) ^ 2 := by
  unfold markovZ heckeH
  field_simp
  ring

/-- **The arithmetic mean's bond constant is the midpoint of the other two.**

The p-p bond has `d = 0` and the n-n bond `d = -h`; the `ε = 0` p-n bond has
`d = -h/2`, their midpoint.  Since the trace is linear this is the whole
content of "arithmetic mean" at the element level: the bond is
`σ - (h/2)·1 = (σ + σ⁻¹)/2`. -/
theorem arithMean_bondConst_eq_midpoint (h : K) :
    bondConst h 0 = (0 + -h) / 2 := by
  unfold bondConst
  ring

end QOU.MassTheory.PnOffset
