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
system (Platter–Hammer–Meißner, `nucl-th/0409040`). This file turns that
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

`mu4_target_exceeds_n3lo_bound` certifies the numeric claim behind the
GAP-9 probe: the corpus target `μ₄ = −4.591` (in units of `B(D) = 2.224566 MeV`)
exceeds `34 ×` the N³LO four-nucleon estimate of `0.300 MeV`
(Jurgenson–Navrátil–Furnstahl, `arXiv:0905.1873`, which measures the SRG-induced
four-body force at `λ = 2 fm⁻¹` as "about 50 keV net" and quotes the N³LO
long-range estimate as "of order a few hundred keV").

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

section NumericCertification

/-- **The GAP-9 magnitude claim, certified.** The corpus target `μ₄ = −4.591`
in units of `B(D) = 2.224566 MeV` is `10.213 MeV`, which exceeds `34 ×` the
N³LO four-nucleon estimate of `0.300 MeV`. Over `ℝ`, as a numeric statement must
be; this is a certification of the probe's arithmetic, not a structural theorem. -/
theorem mu4_target_exceeds_n3lo_bound :
    (34 : ℝ) * 0.300 < 4.591 * 2.224566 := by norm_num

/-- The same target as a fraction of `B(⁴He) = 28.295662 MeV`: it exceeds `35 %`
of the total binding energy — three orders above the `~1 %` the N³LO four-nucleon
force is estimated to supply. -/
theorem mu4_target_exceeds_35_percent_of_B4He :
    (0.35 : ℝ) * 28.295662 < 4.591 * 2.224566 := by norm_num

end NumericCertification


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

end QOU.MassTheory.TjonSimplexForm
