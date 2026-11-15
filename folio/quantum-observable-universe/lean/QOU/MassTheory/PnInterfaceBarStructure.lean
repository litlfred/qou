/-
# Bar structure of the three inter-nucleon interface factors

The canonical atomic braid assigns one factor per nearest-neighbour bond:

* `f_pp = z`               (pure `σ`,    positive crossing)
* `f_nn = z - h`           (pure `σ⁻¹`,  negative crossing)
* `f_pn = z - ε·h`         (a weighted average of the two)

with `z = q³/(q²+1)` (convention D) and `h = q - q⁻¹`.

This file proves, over an arbitrary field, the four facts that were previously
only verified symbolically in
`computations/probes/pn_interface_bar_structure_probe.py`:

1. `barZ` : `z(q⁻¹) = z(q) - h(q)`.  The p-p and n-n factors are **bar
   conjugates of each other** — they are one orbit of the involution
   `q ↦ q⁻¹`, not two independent choices.

2. `strictPn_eq_barSymmetriser` : the `δ = 0` p-n factor `z - h/2` is exactly
   the bar symmetriser `(z(q) + z(q⁻¹))/2`.  The name "uniform bar-invariant
   projection" used by the producers is therefore literal.

3. `pnWeighted_bar_sub` : for a general offset `ε` with bar-image `ε'`,
   the bar defect of the weighted p-n factor is
   `bar(f_pn) - f_pn = -(ε' + ε)·h`.

4. `pnWeighted_barEven_iff` : hence, when `h ≠ 0`, the weighted p-n factor is
   bar-even **iff `ε' = -ε`** — the offset must be bar-**odd**.

Fact 4 is the load-bearing one.  It is why the colour-tube weighting
`ε = δ/4` breaks bar-invariance: `bar δ = -q²·δ`, so `ε' = -q²ε ≠ -ε` unless
`q² = 1`.  And it is why "symmetrise the weight" is the *wrong* repair — a
bar-even offset makes the defect `-2ε·h`, which is worse, not better.

## Scope

Everything here is an identity in the field, with `bar` supplied by the caller
as the value `ε'` rather than as a construction: the point is precisely that
the conclusion depends only on the *relation* between `ε` and its image, not
on how the involution is realised.  No claim is made here about which offset
is physically correct; see the probe and
`prf:interface-knot-markov-z` for that discussion.

Base ring is a generic `Field` per the §7c convention — nothing here needs an
ordering, a square root, or any archimedean construct.

-- Ref: [leitner2026] mass-theory/interface-knot-markov-z-proof.md,
--      §"The three factors are one bar-orbit"
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

-- Declarations here are nested one namespace deeper than the module's
-- parent so this module and QOU.MassTheory.AveragedLetterSpectrum
-- can be imported together: both declared the same fully-qualified
-- name(s), and Lean rejects the second import with "environment already
-- contains" (bean `qou-kfcl`). Nothing imports this module, so the
-- nesting costs no consumer.
namespace QOU.MassTheory.PnInterfaceBarStructure

-- `CharZero` is required, not incidental: every statement here is about an
-- AVERAGE of the two like-flavour factors, so `2` must be invertible.  In
-- characteristic 2 the construction degenerates.  Two of the theorems
-- (`barZ`, `fNN_eq_fPP_bar`) happen not to divide and so do not use it; the
-- unused-section-variable linter is silenced rather than splitting the
-- section, because the hypothesis is part of the setting, not an accident.
set_option linter.unusedSectionVars false

variable {K : Type*} [Field K] [CharZero K]

/-- The Markov parameter in convention D, `z = q³/(q²+1)`. -/
noncomputable def markovZ (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- The Hecke skein parameter, `h = q - q⁻¹`. -/
noncomputable def heckeH (q : K) : K := q - q⁻¹

/-- The p-p bond factor: a positive crossing contributes `z`. -/
noncomputable def fPP (q : K) : K := markovZ q

/-- The n-n bond factor: a negative crossing contributes `z - h`. -/
noncomputable def fNN (q : K) : K := markovZ q - heckeH q

/-- The p-n bond factor with weight offset `ε`:
`(1/2 + ε)·f_pp + (1/2 - ε)·f_nn`. -/
noncomputable def fPN (q ε : K) : K :=
    (1 / 2 + ε) * fPP q + (1 / 2 - ε) * fNN q

/-- **The p-p and n-n factors are bar conjugates.**  `z(q⁻¹) = z(q) - h(q)`,
so the two like-flavour bonds form a single orbit of `q ↦ q⁻¹`. -/
theorem barZ (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    markovZ q⁻¹ = markovZ q - heckeH q := by
  have hqq : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have hq2' : (q⁻¹) ^ 2 + 1 ≠ 0 := by
    have hrw : (q⁻¹) ^ 2 + 1 = (q ^ 2 + 1) / q ^ 2 := by field_simp; ring
    rw [hrw]
    exact div_ne_zero hq2 hqq
  have hrw : (q⁻¹) ^ 2 + 1 = (q ^ 2 + 1) / q ^ 2 := by field_simp; ring
  unfold markovZ heckeH
  rw [hrw]
  field_simp
  ring

/-- `f_nn` is the bar image of `f_pp`. -/
theorem fNN_eq_fPP_bar (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    fNN q = fPP q⁻¹ := by
  unfold fNN fPP
  rw [barZ q hq hq2]

/-- **The `δ = 0` p-n factor is the bar symmetriser.**
`z - h/2 = (z(q) + z(q⁻¹))/2`. -/
theorem strictPn_eq_barSymmetriser (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    markovZ q - heckeH q / 2 = (markovZ q + markovZ q⁻¹) / 2 := by
  rw [barZ q hq hq2]; ring

/-- The weighted-mean form agrees with the explicit shifted form used in the
producers: `f_pn = z - (1/2 - ε)·h`.

At `ε = 0` this is `z - h/2`, the `δ = 0` factor; at `ε = δ/4` it is the
colour-tube-weighted `z - h(1/2 - δ/4)`. -/
theorem fPN_eq (q ε : K) :
    fPN q ε = markovZ q - (1 / 2 - ε) * heckeH q := by
  unfold fPN fPP fNN; ring

/-- **The bar defect of the weighted p-n factor.**

Applying `bar` swaps `f_pp` and `f_nn` (by `fNN_eq_fPP_bar`) and sends the
offset `ε` to `ε'`, so the image is `(1/2 + ε')·f_nn + (1/2 - ε')·f_pp`.  Its
difference from `fPN q ε` is `-(ε' + ε)·h`.

`ε'` is taken as a parameter rather than computed: the conclusion depends only
on the relation between the offset and its image. -/
theorem pnWeighted_bar_sub (q ε ε' : K) :
    ((1 / 2 + ε') * fNN q + (1 / 2 - ε') * fPP q) - fPN q ε
      = -(ε' + ε) * heckeH q := by
  unfold fPN fPP fNN; ring

/-- **The load-bearing statement: bar-even iff the offset is bar-ODD.**

When `h ≠ 0`, the weighted p-n factor is fixed by the involution exactly when
`ε' = -ε`.

Note the direction.  A bar-*even* offset (`ε' = ε`) gives defect `-2ε·h`,
which vanishes only in the trivial case `ε = 0`; symmetrising the weight is
therefore the wrong repair. -/
theorem pnWeighted_barEven_iff (q ε ε' : K) (hh : heckeH q ≠ 0) :
    ((1 / 2 + ε') * fNN q + (1 / 2 - ε') * fPP q) = fPN q ε ↔ ε' = -ε := by
  rw [← sub_eq_zero, pnWeighted_bar_sub, mul_eq_zero]
  constructor
  · rintro (h1 | h2)
    · exact add_eq_zero_iff_eq_neg.mp (neg_eq_zero.mp h1)
    · exact absurd h2 hh
  · intro h
    left
    rw [h]; ring

/-- A bar-**even** offset cannot restore bar-invariance unless it is zero. -/
theorem barEven_offset_insufficient (q ε : K) (hh : heckeH q ≠ 0) :
    ((1 / 2 + ε) * fNN q + (1 / 2 - ε) * fPP q) = fPN q ε ↔ ε = 0 := by
  rw [pnWeighted_barEven_iff q ε ε hh]
  constructor
  · intro h
    have h2 : (2 : K) * ε = 0 := by linear_combination h
    have hne : (2 : K) ≠ 0 := by norm_num
    exact (mul_eq_zero.mp h2).resolve_left hne
  · intro h; rw [h]; ring

end QOU.MassTheory.PnInterfaceBarStructure
