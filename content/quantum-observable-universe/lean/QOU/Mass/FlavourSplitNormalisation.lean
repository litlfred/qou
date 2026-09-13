/-
Copyright (c) 2026 litlfred. All rights reserved.

# The `1/4` in `t_pn = 1/2 − δ/4` is a normalisation Jacobian, not a constant

## What this retires

Bean `qou-qqm4` and PR #7285 both list *"the `1/4` is untouched / unexplained"*
as an open derivation target, alongside the `(q−1)²/3` in `δ`.  **For the `1/4`
that framing is wrong, and it was mine.**  The `1/4` is not a free parameter and
there is nothing to derive: it is fixed by the *normalisation convention* of `δ`,
and it changes to `1/2` under a different, equally natural convention.

The corpus defines the substrate flavour split (`prop:flavor-split-substrate`,
`_li_2_q_util.flavor_split_leading`) as

    δ  =  Δm / M_N        with   Δm = m_n − m_p   and   M_N = (m_p + m_n)/2

— normalised by the **mean** nucleon mass.  With that normalisation,
`1/2 − δ/4` is *identically* the proton's mass fraction of the pair
(`tPN_mean_normalised`), and the `4` is exactly `2 × 2`: one factor because
`M_N` is a mean rather than a sum, one because `Δm` is a full difference rather
than a half-split.

## Why this is falsifiable rather than a re-labelling

The three theorems below are not one identity written three ways.  Had `δ` been
normalised by the **sum** `m_p + m_n` — which is what "the pair's mass" most
naturally means — the same physical quantity would read `1/2 − δ/2`
(`tPN_sum_normalised`), and `1/2 − δ/4` would be **wrong**, by the nonzero
residual `Δm / (4(m_p+m_n))` (`quarter_is_wrong_under_sum_normalisation`).

So the content of the `4` is a statement about `M_N`, and it is checkable: read
the normalisation off `flavor_split_leading`'s docstring and the coefficient
follows.  "Derive the `1/4`" is a malformed target; "which mass normalises `δ`"
is the real question, and the corpus answers it.

## What this does NOT retire — and it is the larger half

* **The `(q−1)²/3` in `δ` is untouched.**  That is the substrate content, it is
  derived only at leading order (`prop:flavor-split-substrate`), and its
  subleading correction is explicitly **posited, not derived** —
  `flavor_split_subleading`'s `(1+ℏ_q³)` supplies 76 % of the gap CODATA
  demands and is labelled `posited` in its own docstring.  That remains open.
* **The mass-fraction reading does NOT extend to the like pairs.**
  `BondLetterIdentification.massFraction_like_pair` proves `m/(m+m) = 1/2`,
  which contradicts the production `t_pp = 0` and `t_nn = 1`.  So "the interface
  is weighted by mass fraction" is *not* the mechanism for all three letters —
  it holds at the `pn` interface and fails at the like ones.
* **Why the `pn` interface carries a colour weighting at all** is the
  `bring_color_weighted` convention (canonical by owner ruling R3, 2026-08-15),
  and this file derives none of it.

§7c: pure field identities — no ordering, no `Real.sqrt`, no archimedean
construct.  `CharZero` is **required, not tactic convenience**: every statement
divides by `2` and `4`, so all three are false in characteristic 2.  Sorry-free.

-- Ref: [manuscript] docs/audits/2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md
-/
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.Mass.FlavourSplitNormalisation

variable {R : Type*} [Field R] [CharZero R]

/-- The substrate flavour split as the corpus normalises it: `Δm / M_N` with
`M_N` the **mean** nucleon mass `(m_p + m_n)/2`
(`_li_2_q_util.flavor_split_leading`, `prop:flavor-split-substrate`). -/
noncomputable def deltaMean (mp mn : R) : R := (mn - mp) / ((mp + mn) / 2)

/-- The same split normalised by the **sum** `m_p + m_n` instead — the other
natural reading of "the pair's mass", used here only as the contrast that makes
the coefficient falsifiable. -/
noncomputable def deltaSum (mp mn : R) : R := (mn - mp) / (mp + mn)

/-- **The production `pn` weight is the proton's mass fraction — and the `1/4`
is what the mean-normalisation costs.**

`t_pn = 1/2 − δ/4 = m_p/(m_p+m_n)` identically, for `δ` normalised by the mean.
This is `BondLetterIdentification.tPN_eq_proton_mass_fraction` restated with the
normalisation made explicit, which is the point: the `4` is `2 × 2`, one factor
from `M_N` being a mean and one from `Δm` being a full difference. -/
theorem tPN_mean_normalised (mp mn : R) (h : mp + mn ≠ 0) :
    1 / 2 - deltaMean mp mn / 4 = mp / (mp + mn) := by
  unfold deltaMean
  field_simp
  ring

/-- **Under sum-normalisation the coefficient is `1/2`, not `1/4`.**

The *same* physical weight — the proton's mass fraction — reads `1/2 − δ/2` when
`δ` is normalised by `m_p + m_n`. So the numeral is carried by the convention,
not by the physics. -/
theorem tPN_sum_normalised (mp mn : R) (h : mp + mn ≠ 0) :
    1 / 2 - deltaSum mp mn / 2 = mp / (mp + mn) := by
  unfold deltaSum
  field_simp
  ring

/-- **And `1/4` is positively WRONG under sum-normalisation**, by a residual that
vanishes only when the two masses agree.

This is what makes the two theorems above a statement rather than a
re-labelling: the coefficient is not free to be either, it is determined by which
mass normalises `δ`, and picking the wrong pairing is detectable. -/
theorem quarter_is_wrong_under_sum_normalisation (mp mn : R) (h : mp + mn ≠ 0) :
    1 / 2 - deltaSum mp mn / 4 - mp / (mp + mn) = (mn - mp) / (4 * (mp + mn)) := by
  unfold deltaSum
  field_simp
  ring

/-- The residual above is nonzero exactly when the nucleons are not degenerate —
so on the physical `m_p ≠ m_n` the two conventions are genuinely distinguishable,
and the `1/4` cannot be transplanted between them. -/
theorem normalisations_distinguishable (mp mn : R) (h : mp + mn ≠ 0)
    (hne : mn ≠ mp) :
    1 / 2 - deltaSum mp mn / 4 - mp / (mp + mn) ≠ 0 := by
  rw [quarter_is_wrong_under_sum_normalisation mp mn h]
  refine div_ne_zero (sub_ne_zero_of_ne hne) ?_
  exact mul_ne_zero (by norm_num) h

end QOU.Mass.FlavourSplitNormalisation
