import QOU.AlgebraicSubstrate.DominationTowers
import QOU.Archimedean.HyperbolicVolumeTranscendence

/-!
# QOU.AlgebraicSubstrate.OhtsukiKappaDependence — real κ data on the graded tower

Bean `qou-7jok`, partial. `DominationTowers.grade_pos_iff_leading_vanishes`
says the Ohtsuki grade separates relation from non-relation. This file feeds it
the **actual** 4₁ coefficients and records what they show.

## The data

From [`qbeta-ohtsuki-kappa-vs-ck-direct-comparison.witness.json`](../../../../computations/qbeta/qbeta-ohtsuki-kappa-vs-ck-direct-comparison.witness.json)
(`tier: numerical-exact`, closed forms independently reproduced there):

| level | value | closed form |
|---|---|---|
| `κ₀` | `2.029883…` | `Vol(4₁) = 2·Cl₂(π/3) = 6Λ(π/3)` |
| `κ₁` | `0.554216472404899…` | `11√3·π/108` |
| `κ₂` | `0.731081807488100…` | `2π²/27` |

## The finding: the tail is algebraically DEPENDENT, the head is not

`kappa_4_1_relation` proves, sorry-free,

  `288·κ₁² = 121·κ₂`,

an exact relation over `ℚ`. This is not a coincidence to be explained — it is
forced. Every `κₙ` lies in `ℚ(√3)·π^⌈n/2⌉ ⊂ ℚ(√3)(π)`, a field of
**transcendence degree 1 over `ℚ`** (`√3` is algebraic; only `π` is
transcendental). So *any two* tail coefficients are algebraically dependent, by
the same transcendence-degree argument that forces the `tr_M` jets to be
dependent (`TowerHeightAttack §4`). `288x² − 121y` is simply the minimal
witness at levels 1, 2.

**And that is exactly why the route is viable rather than dead.** The
asymmetry is the point:

* the **tail** `κ₁, κ₂, …` is arithmetic — a known field, computable, and
  algebraically dependent;
* the **head** `κ₀ = Vol(4₁)` is *not known* to lie in `ℚ(√3)(π)` at all. Its
  irrationality is open (`conj:single-volume-irrationality`).

The grading reads the head; the tail is where the computable constraints live.
`ohtsuki_4_1_grade_zero` records the first consequence: the 4₁ tower sits at
grade `0`, because `Vol(4₁) ≠ 0`.

## What this does NOT do

`qou-7jok` asks for the **joint** tower over `4₁`, `5₂`, `𝓑₃`. Only the `4₁`
coefficients exist in the corpus — the witness above is `4₁`-specific and no
`κₙ` for `5₂` or `𝓑₃` was found. A single-knot tower cannot exhibit a relation
*among the three volumes*, so the joint construction remains blocked on data,
not on machinery. Nothing here is evidence for or against
`conj:hyperbolic-volume-transcendence`.

Two further caveats, both real:

1. `𝔙₀` is the **complex** volume `Vol + i·CS`; the real-volume statement needs
   the real part extracted, which the `ℝ`-valued tower here elides.
2. Each knot's Ohtsuki expansion is taken at *its own* root of unity, so the
   three towers are not a priori coefficients in one common `ℏ`.

## References

* [garoufalidis-zagier-2024] quantum modularity, the `Φ(ℏ)` expansion.
* [ramis-sauloy-zhang2013] q-difference Newton-polygon slopes.
-/

namespace QOU.AlgebraicSubstrate

open QOU.Archimedean

/-! ## §1  The relation, formally -/

/-- **The relation is formal.** For any `s` with `s² = 3` and any `p`, the pair
`(11sp/108, 2p²/27)` satisfies a rational relation — nothing about `π` or `√3`
beyond `√3² = 3` is used. Stated denominator-cleared so it holds over any
commutative ring. -/
theorem kappa_relation_formal {R : Type*} [CommRing R] (s p : R) (hs : s ^ 2 = 3) :
    288 * (11 * s * p) ^ 2 * 27 = 121 * (2 * p ^ 2) * 108 ^ 2 := by
  linear_combination (940896 * p ^ 2) * hs

/-! ## §2  The 4₁ Ohtsuki coefficients -/

/-- `κ₁(4₁) = 11√3·π/108 ≈ 0.554216472404899`. -/
noncomputable def kappa1_4_1 : ℝ := 11 * Real.sqrt 3 * Real.pi / 108

/-- `κ₂(4₁) = 2π²/27 ≈ 0.731081807488100`. -/
noncomputable def kappa2_4_1 : ℝ := 2 * Real.pi ^ 2 / 27

/-- **`288·κ₁² = 121·κ₂`** — an exact rational relation among the 4₁ Ohtsuki
tail coefficients. Verified symbolically against the witness closed forms. -/
theorem kappa_4_1_relation : 288 * kappa1_4_1 ^ 2 = 121 * kappa2_4_1 := by
  have hs : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have h : (11 * Real.sqrt 3 * Real.pi) ^ 2 = 363 * Real.pi ^ 2 := by
    rw [mul_pow, mul_pow, hs]; ring
  unfold kappa1_4_1 kappa2_4_1
  rw [div_pow, h]
  ring

/-- The same statement as an annihilator: `288x² − 121y` kills `(κ₁, κ₂)`, so
the tail coefficients are **algebraically dependent over `ℚ`**. -/
theorem kappa_tail_annihilated : 288 * kappa1_4_1 ^ 2 - 121 * kappa2_4_1 = 0 :=
  sub_eq_zero_of_eq kappa_4_1_relation

/-- Both tail coefficients are non-zero, so the dependence is not the trivial
one — `288x² − 121y` genuinely relates two non-degenerate quantities. -/
theorem kappa1_4_1_pos : 0 < kappa1_4_1 := by
  unfold kappa1_4_1
  have h3 : 0 < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hpi : 0 < Real.pi := Real.pi_pos
  positivity

theorem kappa2_4_1_pos : 0 < kappa2_4_1 := by
  unfold kappa2_4_1
  have hpi : 0 < Real.pi := Real.pi_pos
  positivity

/-! ## §3  The head sits at grade zero -/

/-- **The 4₁ tower has grade `0`.** Its leading coefficient is `Vol(4₁) ≠ 0`, so
by `grade_pos_iff_leading_vanishes` the grade cannot be positive — and grade `0`
is exactly the "no relation" reading.

This is the machinery of `DominationTowers` running on real data: the head is
read by the grade, the (dependent, arithmetic) tail is not. -/
theorem ohtsuki_4_1_grade_zero {κ : ℕ → ℝ} (h : κ 0 = vol_4_1) :
    ohtsukiVal κ = 0 := by
  have hne : κ 0 ≠ 0 := by rw [h]; exact vol_4_1_ne_zero
  by_contra hcon
  exact hne ((grade_pos_iff_leading_vanishes κ).mp
    (lt_of_le_of_ne (by simp) (Ne.symm hcon)))

/-- Contrapositive on real data: were a polynomial relation to hold among the
leading parts, the combined tower would have to leave grade `0`. With only the
`4₁` tower available this is a statement about one knot, not the three-knot
relation `qou-7jok` needs. -/
theorem relation_would_lift_4_1_grade {κ : ℕ → ℝ} (h : ohtsukiVal κ = 0) :
    κ 0 ≠ 0 :=
  no_relation_of_grade_zero h

end QOU.AlgebraicSubstrate
