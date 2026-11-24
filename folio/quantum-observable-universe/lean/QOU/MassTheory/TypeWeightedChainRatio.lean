/-
# Weighting bonds by TYPE does not escape the `b₃` exclusion

The merged `BrunnianTripleExhaustion` exhausts the A = 3 count-channel carrier
space, and names the one free ingredient: `def:crossing-energy` assigns **one
weight to every crossing**, which is what makes `μ` a bare count. The obvious
escape is to let the weight depend on the bond. **Production already does that,
and it does not help.**

## What production actually weights with

`canonical_braid_crossings.d_for_ctype` is the single owner of the Hecke shift a
crossing type denotes: `sigma ↦ 0`, `sigma_inv ↦ -h`, `averaged ↦ -h/2`, mapping
to the bond types `pp ↦ 0`, `nn ↦ -h`, `pn ↦ -h/2`. So `μ` in production is not
`c` but a **type-weighted** count `n_pp·w_pp + n_pn·w_pn + n_nn·w_nn` — the
uniformity this file's predecessor identified as free is *already* relaxed
there, one axis over.

The bond set is the **chain**, which `QOU.Mass.StrandLayoutForcesChain` proves is
forced by the strand layout rather than chosen.

## The arithmetic-mean relation, and what it buys

A chain on three nucleons depends on which one sits in the middle, so `μ(A = 3)`
is arrangement-dependent per isotope: `³H` gives `-3h/2` as `p-n-n` but `-h` as
`n-p-n`. **The isospin average is not**, and `avgTriple_order_independent_iff`
says exactly when:

    w_pp + w_nn = 2 w_pn .

Production satisfies it **exactly** (`0 + (-h) = 2·(-h/2)`), so `B̄(3)` is
well-defined even though neither isotope's chain is. Note this is **strictly
weaker** than `ChainBondOrderDependence.orderIndependent_iff`'s
`L_pp = L_pn = L_nn`, which production *fails* — the three weights are `0`,
`-h/2`, `-h` and all differ. That result is about each arrangement; this one is
about their average, which is what `b₃` consumes.

## And the same relation pins the ratio

`b₃/b₂` sees only `μ_triple/μ_pair`. On the mean locus `μ_triple = 2 w_pn` and
`μ_pair = w_pn`, so the ratio is **`2` identically** — independent of the weights
and of `h` (`ratio_eq_two_of_mean`, `bRatio_eq_neg_one_of_mean`). Hence

    b₃/b₂ = 2 - 3 = -1 ,

against the measured `+0.6411239316`: **wrong sign, 256 % off, and no choice of
`q₀` moves it because `h` cancels.**

That is the same `-1` the *uniform* chain gives. Weighting by type changes `μ`
from a count into a weighted count and leaves the one number `b₃` can see exactly
where it was.

## Scope

Scope **(b)** on type-weighted chain carriers, invariant named: on the
arithmetic-mean locus the triple/pair ratio is `2`, so `b₃/b₂ = -1` for **every**
such weighting. Scope **(a)** elsewhere — in particular a weighting *off* that
locus is not excluded here, but it buys an arrangement-dependent `B̄(3)`, which
is a defect of its own (a nucleus has no middle).

**Relocation, which is why this file exists.** The exclusion in
`BrunnianTripleExhaustion` is of the **crossing-energy** channel. The
seven-channel taxonomy (`docs/audits/2026-08-31-binding-channel-taxonomy.md`)
shows production ships a *trace-ratio* channel that is neither extensive nor
bond-additive, so that exclusion does **not** by itself bind production. This
file closes the gap for the type-weighted bond count; the shipped `(1 - ∏f)`
channel is still outside both.

Ground ring: generic `[Field R] [CharZero R]` — the result is an identity in the
weights, using no ordering and no archimedean structure (§7c). `CharZero` is
needed only because the isospin average divides by two, which is division by zero
in characteristic 2; the proofs use `linear_combination` rather than `linarith`
for the same reason.

Beans `qou-brng`, `qou-48is`.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

namespace QOU.Mass.TypeWeightedChainRatio

variable {R : Type*} [Field R] [CharZero R]

/-- The chain multiplicity of `²H`: one `pn` bond. -/
def muPair (wpn : R) : R := wpn

/-- `A = 3` chain multiplicity with the heavier-unlike nucleon at an end —
`³H` as `p-n-n` gives `{pn, nn}`, `³He` as `p-p-n` gives `{pp, pn}` — isospin
averaged. -/
def muTripleMiddleHeavy (wpp wpn wnn : R) : R := (wpp + wnn + 2 * wpn) / 2

/-- `A = 3` chain multiplicity with the *like* pair split — `³H` as `n-p-n` gives
`{pn, pn}`, `³He` as `p-n-p` gives `{pn, pn}` — isospin averaged. -/
def muTripleMiddleLight (wpn : R) : R := 2 * wpn

/-- **The isospin average is arrangement-independent exactly on the
arithmetic-mean locus.** Per isotope the chain does depend on which nucleon is in
the middle; averaging `³H` against `³He` cancels that iff `w_pp + w_nn = 2w_pn`.
Production satisfies it exactly (`0`, `-h/2`, `-h`). -/
theorem avgTriple_order_independent_iff (wpp wpn wnn : R) :
    muTripleMiddleHeavy wpp wpn wnn = muTripleMiddleLight wpn
      ↔ wpp + wnn = 2 * wpn := by
  unfold muTripleMiddleHeavy muTripleMiddleLight
  rw [div_eq_iff (by norm_num : (2:R) ≠ 0)]
  constructor
  · intro h; linear_combination h
  · intro h; linear_combination h

/-- **On that locus the triple/pair ratio is `2`, identically.** No dependence on
the weights, and none on `h` — so no anchor or convention can move it. -/
theorem ratio_eq_two_of_mean {wpp wpn wnn : R} (hmean : wpp + wnn = 2 * wpn)
    (hne : wpn ≠ 0) : muTripleMiddleHeavy wpp wpn wnn / muPair wpn = 2 := by
  unfold muTripleMiddleHeavy muPair
  rw [div_div, div_eq_iff (mul_ne_zero (by norm_num : (2:R) ≠ 0) hne)]
  linear_combination hmean

/-- **Hence `b₃/b₂ = -1` for every type weighting on the mean locus** — the same
value the uniform chain gives, against a measured `+0.6411239316`. Weighting by
type is not an escape. -/
theorem bRatio_eq_neg_one_of_mean {wpp wpn wnn : R} (hmean : wpp + wnn = 2 * wpn)
    (hne : wpn ≠ 0) :
    muTripleMiddleHeavy wpp wpn wnn / muPair wpn - 3 = -1 := by
  rw [ratio_eq_two_of_mean hmean hne]; ring

/-- Production's own weights, in units of `h`: `pp = 0`, `pn = -1/2`, `nn = -1`
(`d_for_ctype`). They sit on the locus. -/
theorem production_weights_on_mean_locus :
    (0 : ℚ) + (-1) = 2 * (-1/2) := by norm_num

/-- So production's type-weighted chain gives exactly `-1`. -/
theorem production_bRatio_eq_neg_one :
    muTripleMiddleHeavy (0 : ℚ) (-1/2) (-1) / muPair (-1/2) - 3 = -1 :=
  bRatio_eq_neg_one_of_mean production_weights_on_mean_locus (by norm_num)

/-! ## The colour-weighted `pn` interface — the one weighting left, also excluded -/

/-- **An all-`pn` chain gives ratio `2` for ANY `pn` weight, with no locus
condition at all.** The `middle-light` arrangement (`n-p-n` and `p-n-p`) has only
`pn` bonds, so the weight cancels entirely between numerator and denominator.

This is the sharpest form of the obstruction: on that arrangement `b₃/b₂ = -1`
*whatever* the `pn` interface is — colour-weighted, `δ`-dependent, anything. -/
theorem allPn_ratio_eq_two {wpn : R} (hne : wpn ≠ 0) :
    muTripleMiddleLight wpn / muPair wpn = 2 := by
  unfold muTripleMiddleLight muPair
  field_simp

/-- `d_for_ctype "averaged_weighted"` is `-h(1/2 - δ/4)`, with `δ` the substrate
flavour split `(m_n - m_p)/M_N`. In units of `h`, that is the `pn` weight below;
`pp` and `nn` are untouched by the colour weighting. -/
def wpnColour (δ : R) : R := -(1/2 - δ/4)

/-- **The colour-weighted interface sits OFF the arithmetic-mean locus, by exactly
`δ/2`.** So the preceding theorems do not cover it — which is why it needed its
own treatment rather than a remark. -/
theorem colourWeighted_off_locus (δ : R) :
    2 * wpnColour δ - ((0 : R) + (-1)) = δ / 2 := by
  unfold wpnColour; ring

/-- On the locus exactly when `δ = 0` — and `δ` is a nucleon mass-difference
ratio, so it is not. -/
theorem colourWeighted_on_locus_iff (δ : R) :
    (0 : R) + (-1) = 2 * wpnColour δ ↔ δ = 0 := by
  unfold wpnColour
  constructor
  · intro h; linear_combination -2 * h
  · intro h; linear_combination -h / 2

/-- **The `middle-heavy` ratio under colour weighting is `(4 - δ)/(2 - δ)`.** -/
theorem colourWeighted_ratio_middleHeavy {δ : R} (hδ : 2 - δ ≠ 0)
    (hne : wpnColour δ ≠ 0) :
    muTripleMiddleHeavy 0 (wpnColour δ) (-1) / muPair (wpnColour δ)
      = (4 - δ) / (2 - δ) := by
  have h2w : 2 * wpnColour δ ≠ 0 := mul_ne_zero (by norm_num) hne
  unfold muTripleMiddleHeavy muPair
  rw [div_div, div_eq_div_iff h2w hδ]
  unfold wpnColour
  ring

/-- **Reaching the measured `b₃/b₂` would need `δ > 1`.** Solving
`(4 - δ)/(2 - δ) = 3 + rMeasured` gives `δ = 4867718/3916903 ≈ 1.2427` — and
`δ = (m_n - m_p)/M_N > 1` would need the neutron-proton mass difference to exceed
the whole nucleon mass. The physical value is `≈ 0.0013757`, so the required
figure is **903× too large and unphysical besides**. -/
theorem colourWeighted_target_forces_delta_gt_one :
    (1 : ℚ) < 4867718 / 3916903 ∧
      (4 - (4867718 : ℚ) / 3916903) / (2 - 4867718 / 3916903)
        = 3 + 950815 / 1483044 := by
  constructor <;> norm_num

end QOU.Mass.TypeWeightedChainRatio
