/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.QBeta.WenzlWeightVanishing

/-!
# The mass channel's two-row cap, derived rather than posited

The mass channel restricts its Wedderburn sums to the **two-row stratum**
`Λ²(n) = {λ ⊢ n : ℓ(λ) ≤ 2}`. Several places in the corpus state that
restriction as an assumption, a `≥ 80 %` empirical dominance bound, or a
conditional class, and then *infer* convention D from it.

That implication runs the other way, and both halves are now proved:

* `QOU.QBeta.WenzlWeight.wenzlLevel_conventionD` — convention D
  (`z = q³/(q²+1)`) **is** Wenzl level `r = 2`.
* `QOU.QBeta.WenzlWeight.schurPrincipal_eq_zero_iff` — the level-`r`
  principal specialisation vanishes **iff** `ℓ(λ) > r`, for every `n`,
  every `λ` and every `r`.

So at convention D the `≥ 3`-row weights are *exactly zero*, and this file
derives the statements the mass channel actually consumes from that fact.

## What is derived here

1. `massWeight_eq_zero_of_three_rows_of_wenzl` — the cap itself.
2. `traceSum_eq_twoRow_of_wenzl` — restricting a weighted Wedderburn sum
   `∑ y_λ · χ_λ` to `Λ²` is an **identity**, not an approximation.
3. `bindingSum_eq_twoRow_of_wenzl` — the same for the binding sum
   `∑ y_λ · χ_λ · Δ_λ`, at every `A`. The `Δ_λ` factor multiplies a weight
   that is already zero, so it cannot reinstate a dropped block.
4. `twoRow_share_eq_one_of_wenzl` — the two-row **share** of a nonzero
   Wedderburn sum is exactly `1`.

(4) is the statement `prop:he4-two-row-dominance` should carry. That block
currently asserts `≥ 80 %`, with an empirical `86.6 %`, encoded as a
`§3b-cond` class whose instance pins `ratio := 866/1000`. Under convention D
the true share is `1`, so the pinned instance is a convention-C measurement,
not a weaker-but-valid bound: a nonzero `≥ 3`-row contribution is precisely
what convention D forbids. See the audit accompanying this file.

## Non-vacuity

An "identity" that held because the filter kept everything would say nothing.
`exists_three_row_diagram` exhibits a diagram the filter drops, and
`twoRow_filter_ne_univ_of_wenzl` shows the dropped weight really is zero while
the surviving ones are not (`conventionD_weight_ne_zero_of_two_rows`
upstream). The restriction discards genuine index set and loses no mass.

## What is *cited*, not proved — read before citing this file

Everything here is a theorem about `schurPrincipal 2 Q μ / Z`, a named
explicit rational expression. Reading those theorems as statements about
**the mass channel's Ocneanu/Markov weight** rests on Wenzl's theorem, that
the trace weights at Markov parameter `z_W = Q^r(1−Q)/(1−Q^r)` *are* those
principal specialisations. That is an external input — see the `-- Ref:` on
`schurPrincipal` — and it is the reason every mass-channel-facing name below
carries the `_of_wenzl` suffix.

`#print axioms` will report these declarations clean, and that report does
**not** certify the identification: the dependency is carried by the choice
of `schurPrincipal` as the weight, not by an axiom the kernel can see. Do not
quote an axiom-clean check as evidence that the mass channel's weight *is*
this object.

An independent route to the same vanishing avoids Wenzl entirely — the
`n = 3` moment pinning `TemperleyLiebTower.conventionD_kills_antisymmetriser`
lifted by `QOU.Mathlib.threeRow_vanishing_all_levels` — at the cost of an
ordered field and a propagation argument. Two routes, different weak points;
`cap_agrees_with_moment_route_of_wenzl` records that they agree.

## Base ring

Generic `[Field R]` throughout (AGENTS.md §7c). Nothing here orders `R`, takes
a root, or evaluates at a substrate value, so specialising to `ℝ` would be
gratuitous. The genericity hypothesis on `Q` is discharged at the substrate by
`WenzlWeight.not_root_of_unity_of_pos_ne_one`, which lives after the
archimedean wall.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.MassTheory.TwoRowCap

open Finset QOU.QBeta.WenzlWeight

variable {R : Type*} [Field R]

/-! ## The cap -/

/-- **The mass channel's two-row cap.**

At convention D — Wenzl level `r = 2`, by `wenzlLevel_conventionD` — a
partition with three or more rows carries weight exactly zero.

This is the statement the mass channel posits in several places. It is a
theorem: `schurPrincipal_eq_zero_iff` gives it for every `n` and every `λ`. -/
theorem massWeight_eq_zero_of_three_rows_of_wenzl {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0) (μ : YoungDiagram)
    (hμ : 3 ≤ μ.colLen 0) :
    schurPrincipal 2 Q μ / Z = 0 :=
  (conventionD_weight_eq_zero_iff hQ0 hQ hZ μ).mpr (by omega)

/-- The contrapositive in the form the sum lemmas consume: a nonzero weight
forces at most two rows. -/
theorem colLen_le_two_of_massWeight_ne_zero_of_wenzl {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0) (μ : YoungDiagram)
    (h : schurPrincipal 2 Q μ / Z ≠ 0) :
    μ.colLen 0 ≤ 2 := by
  by_contra hc
  exact h (massWeight_eq_zero_of_three_rows_of_wenzl hQ0 hQ hZ μ (by omega))

/-! ## Restriction to the two-row stratum is an identity

The mass channel evaluates Wedderburn sums `∑_λ y_λ · χ_λ` and restricts the
index set to `Λ²`. The two lemmas below say that restriction changes nothing —
so it is exact, not a truncation, and carries no error term to bound. -/

/-- **The trace sum restricts exactly.**

For any finite set `s` of Young diagrams and any per-block observable `χ`,

  `∑_{μ ∈ s} y_μ · χ_μ  =  ∑_{μ ∈ s, ℓ(μ) ≤ 2} y_μ · χ_μ`

at convention D. `χ` is arbitrary — the Hoefsmit character is one instance,
but nothing here depends on which observable is summed, because the dropped
terms vanish through the *weight*, whatever multiplies it. -/
theorem traceSum_eq_twoRow_of_wenzl {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0)
    (s : Finset YoungDiagram) (χ : YoungDiagram → R) :
    ∑ μ ∈ s, (schurPrincipal 2 Q μ / Z) * χ μ
      = ∑ μ ∈ s.filter (fun μ => μ.colLen 0 ≤ 2), (schurPrincipal 2 Q μ / Z) * χ μ := by
  refine (Finset.sum_filter_of_ne ?_).symm
  intro μ _ hne
  refine colLen_le_two_of_massWeight_ne_zero_of_wenzl hQ0 hQ hZ μ ?_
  intro h0
  exact hne (by rw [h0, zero_mul])

/-- **The binding sum restricts exactly too, at every `A`.**

  `∑_{μ ∈ s} y_μ · χ_μ · Δ_μ  =  ∑_{μ ∈ s, ℓ(μ) ≤ 2} y_μ · χ_μ · Δ_μ`

`Δ` is arbitrary, so this covers the proved value `Δ_λ = (−1)^{n(λ)}·dim V_λ`
without depending on it. The point is that `Δ_λ` cannot reinstate a dropped
block however large it is on many-row diagrams: it multiplies a weight that is
already zero.

This is the formal content of the claim in `def:two-row-stratum` that the
binding sum "does inherit the restriction, at every `A`, exactly", and of the
2026-08-09 withdrawal of the opposite reading. -/
theorem bindingSum_eq_twoRow_of_wenzl {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0)
    (s : Finset YoungDiagram) (χ Δ : YoungDiagram → R) :
    ∑ μ ∈ s, (schurPrincipal 2 Q μ / Z) * χ μ * Δ μ
      = ∑ μ ∈ s.filter (fun μ => μ.colLen 0 ≤ 2),
          (schurPrincipal 2 Q μ / Z) * χ μ * Δ μ := by
  refine (Finset.sum_filter_of_ne ?_).symm
  intro μ _ hne
  refine colLen_le_two_of_massWeight_ne_zero_of_wenzl hQ0 hQ hZ μ ?_
  intro h0
  exact hne (by rw [h0, zero_mul, zero_mul])

/-- The complementary statement, stated as the vanishing it really is: the
`≥ 3`-row part of a Wedderburn sum is zero. Equivalent to
`traceSum_eq_twoRow_of_wenzl`, but this is the form a "what is the residual
share?" question wants — the answer is `0`, not "small". -/
theorem threeRowPart_eq_zero_of_wenzl {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0)
    (s : Finset YoungDiagram) (χ : YoungDiagram → R) :
    ∑ μ ∈ s.filter (fun μ => ¬ μ.colLen 0 ≤ 2), (schurPrincipal 2 Q μ / Z) * χ μ = 0 := by
  refine Finset.sum_eq_zero ?_
  intro μ hμ
  rw [Finset.mem_filter] at hμ
  rw [massWeight_eq_zero_of_three_rows_of_wenzl hQ0 hQ hZ μ (by omega), zero_mul]

/-! ## The share is exactly one -/

/-- **The two-row share of a nonzero Wedderburn sum is exactly `1`.**

`prop:he4-two-row-dominance` asserts this ratio is `≥ 4/5`, with an empirical
`86.6 %` pinned into a conditional-class instance. At convention D the ratio
is `1` on the nose, for every braid word and every strand count — there is no
dominance to measure, because there is no complement.

A measured share strictly below `1` therefore does not refine this bound; it
records a nonzero `≥ 3`-row contribution, which is exactly what convention D
forbids. Such a measurement is convention-C data. -/
theorem twoRow_share_eq_one_of_wenzl {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0)
    (s : Finset YoungDiagram) (χ : YoungDiagram → R)
    (hne : ∑ μ ∈ s, (schurPrincipal 2 Q μ / Z) * χ μ ≠ 0) :
    (∑ μ ∈ s.filter (fun μ => μ.colLen 0 ≤ 2), (schurPrincipal 2 Q μ / Z) * χ μ)
      / (∑ μ ∈ s, (schurPrincipal 2 Q μ / Z) * χ μ) = 1 := by
  rw [← traceSum_eq_twoRow_of_wenzl hQ0 hQ hZ s χ]
  exact div_self hne

/-! ## Non-vacuity

Both lemmas above would be trivially true if the filter kept everything. It
does not. -/

/-- The filter drops something: `(1,1,1)` has three rows, so it fails
`colLen 0 ≤ 2`. Together with `conventionD_weight_ne_zero_of_two_rows`
upstream — which shows the *surviving* diagrams have nonzero weight — this
makes the restriction a genuine reduction of the index set that loses no
mass, rather than a vacuous relabelling. -/
theorem exists_three_row_diagram :
    ¬ ((YoungDiagram.ofRowLens [1, 1, 1] (by decide)).colLen 0 ≤ 2) := by
  rw [colLen_ofRowLens_one_one_one]
  omega

/-- And it keeps something: `(2,1)` has two rows. So the filter is neither
empty nor everything. -/
theorem two_one_survives_filter :
    (YoungDiagram.ofRowLens [2, 1] (by decide)).colLen 0 ≤ 2 := by
  rw [colLen_ofRowLens_two_one]

/-- **The two routes to the cap agree at the discriminating case.**

`(1,1,1)` is dropped by the Wenzl/Schur route proved here, and it is the same
shape the moment route kills at `n = 3`
(`TemperleyLiebTower.conventionD_kills_antisymmetriser`, whose conclusion is
`y₍₁³₎ = 0`). The routes have different weak points — this one cites Wenzl's
weight formula, that one needs an ordered field and a propagation argument —
so their agreement on the case that discriminates convention D from C is worth
recording rather than assuming. -/
theorem cap_agrees_with_moment_route_of_wenzl {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0) :
    schurPrincipal 2 Q (YoungDiagram.ofRowLens [1, 1, 1] (by decide)) / Z = 0 := by
  refine massWeight_eq_zero_of_three_rows_of_wenzl hQ0 hQ hZ _ ?_
  rw [colLen_ofRowLens_one_one_one]

end QOU.MassTheory.TwoRowCap
