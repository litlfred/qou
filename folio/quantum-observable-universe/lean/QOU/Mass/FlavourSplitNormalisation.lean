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
* **Why the `pn` interface carries a colour weighting at all** is the
  `bring_color_weighted` convention (canonical by owner ruling R3, 2026-08-15),
  and this file derives none of it.  What the section below *does* narrow is the
  **sign** of that weighting, from a numeral to a choice between two named
  weightings.

## 🛑 Correction to an earlier version of this file — the like-pair "defect" is void

An earlier version of this docstring recorded, as an open defect:

> *"The mass-fraction reading does NOT extend to the like pairs.
> `BondLetterIdentification.massFraction_like_pair` proves `m/(m+m) = 1/2`,
> which contradicts the production `t_pp = 0` and `t_nn = 1`."*

**That objection reads the weight in the wrong frame and is withdrawn.**  The
mass fraction is not a rule producing `t` *from* the flavours; it is the weight
in a convex combination *of the two like-pair letters*.  The corpus already said
so — `computations/probes/pn_interface_bar_structure_probe.py` fact 3 records
`f_pn = w_p·f_pp + w_n·f_nn` with `w_p + w_n = 1`, and answers the like-pair
question directly: *"a like-flavour bond has no mean to tilt — averaging `f_pp`
with itself returns `f_pp` for any weights summing to one."*
`crossInterp_like_pair` below is that sentence as a theorem, and it makes the
three letters one rule rather than two.  My grep for the `1/4` had not reached
that probe.

## What the two weights ARE — and the sign is a choice, not a numeral

The same identity that fixes the `4` identifies both weights as **crossed** mass
fractions: the weight on the `pp` letter is the **neutron's** fraction and the
weight on the `nn` letter is the **proton's** (`wPP_mean_normalised`,
`tPN_mean_normalised`).  So the production letter is, with no `δ`, no `1/4` and
no normalisation convention in it,

    σ_pn  =  ( m_n·σ  +  m_p·σ⁻¹ ) / (m_p + m_n) .

The like pairs fix the per-nucleon endpoints `t_p = 0`, `t_n = 1`, and those
admit two interpolations — `direct` (each endpoint by its own mass) and `cross`
(each by the other's).  They differ by exactly `δ/2`
(`direct_sub_cross_eq_deltaMean_half`), agree on the like pairs, and production
selects `cross`.  Nothing in `d_for_ctype` or `prop:pn-averaging-uniqueness`
derives that choice — `direct` is the `δ ↦ −δ` reflection and satisfies the same
bar-invariance and normalisation hypotheses — so this converts an unexplained
numeral into an unexplained **choice between two named weightings**, which is a
smaller open item, not a closed one.  Probe:
`computations/qbeta/pn_letter_is_cross_mass_weighted_probe.py` (5/5), which also
measures where the two are separable: the `A = 3` mirror ratio is `q⁻⁴` under
**both** (the `pn` factor cancels), so the whole discriminator is the deuteron,
where `b_pn` moves by `h·δ/2` — `2.83e-4` relative at the proton-pinned `q₀`.

§7c: pure field identities — no ordering, no `Real.sqrt`, no archimedean
construct.  `CharZero` is **required, not tactic convenience**: the
normalisation statements divide by `2` and `4`, so they are false in
characteristic 2.  Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md
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

/-- **And the weight on the `pp` letter is the NEUTRON's mass fraction.**

`pn_interface_bar_structure_probe` fact 3 writes the canonical interface as
`f_pn = w_p·f_pp + w_n·f_nn` with `w_p = 1/2 + δ/4`.  Together with
`tPN_mean_normalised` (`w_n = 1/2 − δ/4 = m_p/(m_p+m_n)`) this says each
like-pair letter is carried by the mass fraction of **the other** nucleon:

    σ_pn = (m_n·σ + m_p·σ⁻¹)/(m_p + m_n) .

An identity, not a derivation — see the docstring. -/
theorem wPP_mean_normalised (mp mn : R) (h : mp + mn ≠ 0) :
    1 / 2 + deltaMean mp mn / 4 = mn / (mp + mn) := by
  unfold deltaMean
  field_simp
  ring

omit [CharZero R] in
/-- The two weights are convex: they sum to `1` for any nonzero total mass. -/
theorem crossWeights_sum_one (mp mn : R) (h : mp + mn ≠ 0) :
    mn / (mp + mn) + mp / (mp + mn) = 1 := by
  field_simp
  ring

/-- The two interpolations of the like-pair endpoint values `t_p`, `t_n` between
a nucleon of mass `ma` carrying `ta` and one of mass `mb` carrying `tb`:
`directInterp` weights each endpoint by **its own** mass, `crossInterp` by **the
other's**.  Production's `pn` letter is `crossInterp`. -/
noncomputable def directInterp (ma mb ta tb : R) : R := (ma * ta + mb * tb) / (ma + mb)

/-- See `directInterp`. -/
noncomputable def crossInterp (ma mb ta tb : R) : R := (mb * ta + ma * tb) / (ma + mb)

/-- **The production `pn` weight is the CROSS interpolation**, exactly: with
`t_p = 0` (the `pp` letter is `σ`) and `t_n = 1` (the `nn` letter is `σ⁻¹`),
`crossInterp m_p m_n 0 1 = m_p/(m_p+m_n) = 1/2 − δ/4`. -/
theorem crossInterp_eq_tPN (mp mn : R) (h : mp + mn ≠ 0) :
    crossInterp mp mn 0 1 = 1 / 2 - deltaMean mp mn / 4 := by
  rw [tPN_mean_normalised mp mn h]
  unfold crossInterp
  ring_nf

/-- **The direct interpolation is the `δ ↦ −δ` reflection** — it gives
`1/2 + δ/4`, the neutron's fraction, and is the alternative production does not
take. -/
theorem directInterp_eq_reflected (mp mn : R) (h : mp + mn ≠ 0) :
    directInterp mp mn 0 1 = 1 / 2 + deltaMean mp mn / 4 := by
  rw [wPP_mean_normalised mp mn h]
  unfold directInterp
  ring_nf

/-- **The two differ by exactly `δ/2`.**  So the choice between them is the sign
of the colour tilt and nothing else. -/
theorem direct_sub_cross_eq_deltaMean_half (mp mn : R) (h : mp + mn ≠ 0) :
    directInterp mp mn 0 1 - crossInterp mp mn 0 1 = deltaMean mp mn / 2 := by
  rw [directInterp_eq_reflected mp mn h, crossInterp_eq_tPN mp mn h]
  ring

/-- **Both interpolations fix a like pair**, for any masses and any endpoint
value — because a like pair averages a letter with itself.  This is the theorem
form of `pn_interface_bar_structure_probe`'s *"a like-flavour bond has no mean to
tilt"*, and it is what retires the "mass fraction fails at the like pairs"
objection recorded in an earlier version of this file's docstring: the three
letters are one rule, not two. -/
theorem crossInterp_like_pair (m t : R) (hm : m ≠ 0) : crossInterp m m t t = t := by
  have h2 : m + m ≠ 0 := by rw [← two_mul]; exact mul_ne_zero (by norm_num) hm
  unfold crossInterp
  rw [div_eq_iff h2]
  ring

/-- The same for `directInterp` — the two agree on like pairs and differ only at
the unlike one. -/
theorem directInterp_like_pair (m t : R) (hm : m ≠ 0) : directInterp m m t t = t := by
  have h2 : m + m ≠ 0 := by rw [← two_mul]; exact mul_ne_zero (by norm_num) hm
  unfold directInterp
  rw [div_eq_iff h2]
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
