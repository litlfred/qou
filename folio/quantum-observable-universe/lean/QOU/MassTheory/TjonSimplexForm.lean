import QOU.MassTheory.UrsellSlotAlignment
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination
import Mathlib.Data.Real.Basic

/-!
# The Tjon line in simplex form: saturation alone forces a negative `μ₄`

**Why a large negative four-body moment is not evidence of a four-body force.**

Pionless EFT explains the empirical Tjon correlation between `B(³H)` and
`B(⁴He)` by the *absence* of a four-nucleon force at leading order: one
SU(4)-symmetric three-nucleon parameter suffices to renormalise the four-nucleon
system (Platter–Hammer–Meißner, `[platter2005tjon]`, `nucl-th/0409040`; there
`B_d = 2.22` and `B_t = 8.48 MeV` give `B_α = 29.5 MeV` against the
Coulomb-corrected experimental `29.0 ± 0.1`). This file turns that
statement into arithmetic on the residual-simplex ansatz
`M(A) = ∑ₖ μₖ · C(A,k)` of `QOU.MassTheory.UrsellSlotAlignment`, and draws the
consequence the Δ_λ programme needs.

The central identity is `tjon_deviation_eq_mu4`:

  `M(4) − (4·M(3) − 6·M(2))  =  μ₄`

so `4·M(3) − 6·M(2)` is exactly the two-point ("no four-body parameter")
prediction for `M(4)`, and **`μ₄` is precisely the deviation from it**. This is
the Tjon line written in the simplex basis: `mu4_eq_zero_iff_tjon` says the
prediction is exact iff `μ₄ = 0`.

The consequence is `mu4_neg_of_below_tjon`: if the four-body point falls *below*
the two-point prediction — which is what **saturation** does — then `μ₄ < 0`,
with no four-body interaction anywhere in the derivation. So a negative `μ₄` is
what a saturating, non-pairwise-additive binding curve produces when it is
expanded in a `C(A,k)` basis that has no saturation mechanism of its own. Its
sign carries no four-body information.

`additive_higher_moments_vanish` is the contrapositive baseline: exact pairwise
additivity forces `μ₃ = μ₄ = 0`, so every nonzero high moment measures
*non-additivity*, not a `k`-body force.

**On the name.** Throughout this file `μ₄` is called the "four-body moment"
because that is the standing name for the `k = 4` simplex coefficient, and the
docstrings are careful to deny the physical reading each time. It is worth
saying once, plainly, why the denial is needed: with three moments fitted to
three anchors (`A = 2, 3, 4`) the system is exactly determined, so
`μ₄ := M(4) − 4M(3) + 6M(2)` is a **definition** carrying zero residual
freedom. Writing `μ₄` is another way of writing "the amount by which `M(4)`
exceeds the two-point prediction" and nothing more; it acquires no physical
content from the index it is written under. This is the corpus rule *defined
residual ≠ derived decomposition* applied to this file's own vocabulary.
Narrative twin: `rem:tjon-universality-external`.

The numeric claim behind the GAP-9 probe (the corpus target `μ₄ = −4.591`, in
units of `B(D) = 2.224566 MeV`, against the N³LO four-nucleon estimate "of order a
few hundred keV" of `[jurgenson2009srg]`) is **not** stated in Lean. It compares
measured MeV values, and the owner ruled on 2026-11-21 that such comparisons stay
out of Lean; it lives in `computations/deltalambda/mu4_vs_nuclear_4n_force_bound_probe.py`
and its witness.

`§UniversalLimitCrossCheck` at the foot of the file adds the external check that
the framing above needs: the field's own parameter-free four-body answer
(`[hammer2007fourbody]`) is **not** on the `μ₄ = 0` baseline, and the simplex
basis assigns it a `μ₄` larger than the nuclear one.

Base ring: **generic** `[CommRing R]` (§7c) for the identities; the sign lemma
adds only an ordering. The one numeric certification is over `ℝ`, as it must be.

Companion probes: `computations/deltalambda/mu4_vs_nuclear_4n_force_bound_probe.py`
and `computations/deltalambda/gap10_tjon_correlation_probe.py`.

**Scope.** These are theorems about the simplex bookkeeping and one certified
numeric inequality. They do **not** show `ρ_grad` is wrong, they do **not** show
the block-trace operator is right, and they do **not** establish that nuclear
binding saturates — that is an empirical input, cited, not proved here.
-/

namespace QOU.MassTheory.TjonSimplexForm

open QOU.MassTheory.UrsellSlotAlignment

section Identities

variable {R : Type*} [CommRing R]

/-- The two-point ("no four-body parameter") prediction for `M(4)`, built from
`M(2)` and `M(3)` alone. -/
def tjonPredict (μ₂ μ₃ μ₄ : R) : R :=
  4 * Mval μ₂ μ₃ μ₄ 3 - 6 * Mval μ₂ μ₃ μ₄ 2

/-- **The Tjon line in simplex form.** The deviation of `M(4)` from the two-point
prediction is *exactly* `μ₄` — nothing else contributes. -/
theorem tjon_deviation_eq_mu4 (μ₂ μ₃ μ₄ : R) :
    Mval μ₂ μ₃ μ₄ 4 - tjonPredict μ₂ μ₃ μ₄ = μ₄ := by
  simp only [tjonPredict, Mval_two, Mval_three, Mval_four]
  ring

/-- **The prediction is exact iff there is no four-body moment.** This is the
formal content of "no four-body parameter is required": `M(4)` is determined by
`M(2)` and `M(3)` precisely when `μ₄` vanishes. -/
theorem mu4_eq_zero_iff_tjon (μ₂ μ₃ μ₄ : R) :
    μ₄ = 0 ↔ Mval μ₂ μ₃ μ₄ 4 = tjonPredict μ₂ μ₃ μ₄ := by
  have hd := tjon_deviation_eq_mu4 μ₂ μ₃ μ₄
  constructor
  · intro h; linear_combination hd + h
  · intro h; linear_combination h - hd

/-- **Exact pairwise additivity kills every higher moment.** If `M(A)` is `c`
times the edge count `C(A,2)` at `A = 2,3,4`, then `μ₃ = μ₄ = 0`. Hence a
nonzero high moment measures *non-additivity*, never by itself a `k`-body
force. -/
theorem additive_higher_moments_vanish (c μ₂ μ₃ μ₄ : R)
    (h2 : Mval μ₂ μ₃ μ₄ 2 = c)
    (h3 : Mval μ₂ μ₃ μ₄ 3 = 3 * c)
    (h4 : Mval μ₂ μ₃ μ₄ 4 = 6 * c) :
    μ₃ = 0 ∧ μ₄ = 0 := by
  rw [Mval_two] at h2
  rw [Mval_three] at h3
  rw [Mval_four] at h4
  subst h2
  have hμ₃ : μ₃ = 0 := by linear_combination h3
  subst hμ₃
  exact ⟨rfl, by linear_combination h4⟩

end Identities

section Sign

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Saturation alone forces `μ₄ < 0`.** If the four-body point falls below the
two-point prediction — which is exactly what a saturating binding curve does —
then the four-body moment is negative. No four-body interaction appears anywhere
in this derivation, so the *sign* of `μ₄` carries no four-body information. -/
theorem mu4_neg_of_below_tjon {μ₂ μ₃ μ₄ : R}
    (h : Mval μ₂ μ₃ μ₄ 4 < tjonPredict μ₂ μ₃ μ₄) : μ₄ < 0 := by
  have hd := tjon_deviation_eq_mu4 μ₂ μ₃ μ₄
  linarith [hd, h]

/-- The converse direction, recorded so the equivalence is visible: a negative
four-body moment *is* the statement that `M(4)` undershoots the two-point
prediction. Together with the previous lemma this makes "below Tjon" and
"`μ₄ < 0`" the same fact, not two pieces of evidence. -/
theorem below_tjon_of_mu4_neg {μ₂ μ₃ μ₄ : R} (h : μ₄ < 0) :
    Mval μ₂ μ₃ μ₄ 4 < tjonPredict μ₂ μ₃ μ₄ := by
  have hd := tjon_deviation_eq_mu4 μ₂ μ₃ μ₄
  linarith [hd, h]

end Sign



section SignBlindness

variable {K : Type*} [Field K]

/-- The fractional Tjon deviation of a ladder `(M₂, M₃, M₄)`. -/
def fracTjon (M₂ M₃ M₄ : K) : K := (M₄ - (4 * M₃ - 6 * M₂)) / M₄

/-- **The fractional Tjon deviation is BLIND to a global sign flip.** Negating the
whole ladder negates the numerator and the denominator alike, so the score is
unchanged.

This is not a curiosity — it is a trap, and it caught this session. The score was
used to argue that the operator "matches nature's sign", and separately that the
match was "fake because the operator's ladder is globally negative". **Both
arguments are vacuous**: a quantity invariant under the flip can neither confirm
nor refute the sign convention. Only the *ladder growth* discriminates, and that
is likewise sign-blind, which is why it survived when the sign claims did not. -/
theorem fracTjon_neg (M₂ M₃ M₄ : K) :
    fracTjon (-M₂) (-M₃) (-M₄) = fracTjon M₂ M₃ M₄ := by
  unfold fracTjon
  have h : (-M₄) - (4 * (-M₃) - 6 * (-M₂)) = -(M₄ - (4 * M₃ - 6 * M₂)) := by ring
  rw [h, neg_div_neg_eq]

/-- The normalised ladder is sign-blind for the same reason, which is why the
flatness finding survives the convention correction while the sign claims do
not. -/
theorem ladder_ratio_neg (M₂ M_A : K) :
    (-M_A) / (-M₂) = M_A / M₂ := neg_div_neg_eq M_A M₂

end SignBlindness


section UniversalLimitCrossCheck

/-!
### `μ₄ = 0` and "no four-body force" are **not** the same statement

The file's framing above is that a large `μ₄` is a simplex-basis artifact rather
than four-body physics. That framing is *strengthened*, not merely illustrated,
by the field's own parameter-free answer, and this section proves the point
rather than asserting it.

Hammer–Platter solve the four-boson Yakubovsky equations **with no four-body
parameter at all** and report that, away from threshold, the four-body ground
state is related to the deepest three-body state by a factor of `5`
(`[hammer2007fourbody]` §III.B). So `M(4) = 5·M(3)` is a ratio produced by a
calculation that contains no four-body input.

Say it that way and no further. "No four-body parameter is needed to renormalise
at leading order" is **not** "no four-body force exists": `[jurgenson2009srg]`
puts the four-nucleon force at tens to a few hundred keV — small, not zero. And
the authors themselves flag that their universality rests on the RG analysis of
their ref. [12], which Yamashita et al. dispute (§I, p. 3) — though that dispute
explicitly *exempts* the nuclear case, "⁴He atoms and nucleons (where this
sensitivity is absent)", which is the case at issue here. The argument below
needs only the weak reading, so it takes only the weak reading.

`universal_ratio_forces_mu4` computes what the simplex basis assigns to that
calculation: `μ₄ = 9·μ₂ + μ₃`, which is **positive and large** — at the nuclear
`(μ₂, μ₃) = (1, 0.8128)` it is `9.81`, some `2.6 ×` the value the nuclear data
themselves produce. A quantity that is large in a calculation carrying no
four-body input at all is not measuring a four-body input.

`tjon_baseline_lt_four_ratio` sharpens this into an exclusion: on the `μ₄ = 0`
baseline the ratio `M(4)/M(3)` is *strictly below 4* for any positive `μ₂`, so
the universal ratio `5` is **outside the baseline's reachable range entirely**
(`universal_ratio_not_in_tjon_baseline`). The two notions of "no four-body
parameter" — the EFT's (no new coupling in a nonlinear Yakubovsky solution) and
the simplex's (`μ₄ = 0` in a linear inclusion–exclusion form) — are therefore
provably inequivalent, and the external result may be cited as motivation for
the baseline but never as a derivation of it.

Companion probe: `computations/deltalambda/tjon_external_cross_check_probe.py`,
which also re-derives the AME2020 inputs from `library/mass_1.mas20.txt` rather
than from transcribed literals.
-/

section BaselineBounds

variable {R : Type*} [CommRing R]

/-- The gap between `M(4)` and twice `M(3)`. Pure bookkeeping, recorded because
it is what lets a measured ladder be read back as a sign statement about `μ₃`. -/
theorem four_sub_two_mul_three (μ₂ μ₃ μ₄ : R) :
    Mval μ₂ μ₃ μ₄ 4 - 2 * Mval μ₂ μ₃ μ₄ 3 = 2 * μ₃ + μ₄ := by
  simp only [Mval_three, Mval_four]
  ring

/-- **What the simplex basis assigns to a calculation carrying no four-body
input.** If a ladder realises the universal four-to-three ratio `M(4) = 5·M(3)`,
then its four-body moment is `μ₄ = 9·μ₂ + μ₃` — determined entirely by the
*lower* moments, with no four-body input anywhere. -/
theorem universal_ratio_forces_mu4 (μ₂ μ₃ μ₄ : R)
    (h : Mval μ₂ μ₃ μ₄ 4 = 5 * Mval μ₂ μ₃ μ₄ 3) : μ₄ = 9 * μ₂ + μ₃ := by
  simp only [Mval_three, Mval_four] at h
  linear_combination h

end BaselineBounds

section BaselineOrder

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **The `μ₄ = 0` baseline is strictly below ratio 4.** For any positive `μ₂`
the two-point prediction satisfies `M(4) < 4·M(3)`, whatever `μ₃` is. The bound
does not constrain `μ₃` at all: the gap is exactly `−6·μ₂`. -/
theorem tjon_baseline_lt_four_ratio {μ₂ : R} (μ₃ : R) (hμ₂ : 0 < μ₂) :
    Mval μ₂ μ₃ 0 4 < 4 * Mval μ₂ μ₃ 0 3 := by
  simp only [Mval_three, Mval_four]
  linarith

/-- **The universal ratio is unreachable on the baseline.** A ladder with `μ₄ = 0`,
positive `μ₂` and positive `M(3)` cannot satisfy `M(4) = 5·M(3)`. Hence the EFT's
"no four-body parameter at leading order" and the simplex's `μ₄ = 0` are
inequivalent conditions, and a nonzero `μ₄` cannot be read as four-body physics
on the strength of the former. -/
theorem universal_ratio_not_in_tjon_baseline {μ₂ μ₃ : R} (hμ₂ : 0 < μ₂)
    (hM₃ : 0 < Mval μ₂ μ₃ 0 3) :
    Mval μ₂ μ₃ 0 4 ≠ 5 * Mval μ₂ μ₃ 0 3 := by
  have h4 := tjon_baseline_lt_four_ratio (R := R) μ₃ hμ₂
  intro h
  rw [h] at h4
  linarith

/-- **A ladder flatter than ratio 2 has a negative three-body moment.** Recorded
because the corpus block-trace operator measures `M(4) < 2·M(3)` under both bond
conventions, which by `four_sub_two_mul_three` pins `2·μ₃ + μ₄ < 0` — a
diagnosis of the operator's ladder, not of nature's. -/
theorem two_mu3_add_mu4_neg_of_flat {μ₂ μ₃ μ₄ : R}
    (h : Mval μ₂ μ₃ μ₄ 4 < 2 * Mval μ₂ μ₃ μ₄ 3) : 2 * μ₃ + μ₄ < 0 := by
  have hd := four_sub_two_mul_three μ₂ μ₃ μ₄
  linarith

end BaselineOrder

section ExternalNumerics

/-- The nuclear ladder sits *below* the universal ratio: with the corpus's
AME-derived `ρ_strong = (1, 3.8128, 13.0316)` one has `M(4) < 5·M(3)`, i.e.
`B(⁴He)/B(³H) ≈ 3.42` against the zero-range universal `5`. Nuclear binding is
not in the universal regime — finite-range effects shift it, exactly as the
source states. -/
-- Ref: [hammer2007fourbody] https://doi.org/10.1140/epja/i2006-10301-8
theorem ame_ratio_below_universal : (13.0316 : ℝ) < 5 * 3.8128 := by norm_num

/-- And the corpus block-trace operator is flatter still — flatter even than the
pairwise ratio `2`, using the complete-graph ladder `M(3) = 1.78578`,
`M(4) = 2.11435` of the GAP-10 witness. With `ame_ratio_below_universal` this
orders the three: operator `1.18` < nature `3.42` < universal `5`, so the
external number widens the ladder gap rather than closing it. -/
theorem operator_ladder_below_pairwise : (2.11435 : ℝ) < 2 * 1.78578 := by norm_num

end ExternalNumerics

end UniversalLimitCrossCheck

end QOU.MassTheory.TjonSimplexForm
