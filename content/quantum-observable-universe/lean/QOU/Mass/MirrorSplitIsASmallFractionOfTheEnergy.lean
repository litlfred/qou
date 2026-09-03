/-
QOU.Mass.MirrorSplitIsASmallFractionOfTheEnergy — the observable is at most a
`1/A` fraction of the quantity the bounds bound, so a two-sided bound would have
to be tight to better than that to say anything.

Arc context (em-linking; beans `qou-o6ml`, `qou-0hdx`). The sibling file
`LowerBoundCannotConstrainADifference.lean` shows that a lower bound on each of
two energies constrains their difference not at all, and names the missing
ingredient: an **upper** bound, which the Freedman–He link bound (Komendarczyk
arXiv:0808.1533v1 eq. (43)) does not supply. With two-sided bounds the difference
is pinned to `[B₁ − U₂, U₁ − B₂]`, an interval whose width is the **sum of the two
slacks** `(U₁ − B₁) + (U₂ − B₂)`.

This file asks the prior question — *would* an upper bound help? — and answers it
without needing a carrier, a flux value, or any acquisition.

The mirror split is a **difference of two large, nearly equal energies**. Under
the same model the sibling file uses (a vertex-transitive carrier, flux by charge:
`Φp` on the `Z` protons and `Φn` on the `N` neutrons, `d = |Z − N| = 1`):

  `ΔE = c·(Φp − Φn)`   against   `E = c·(Z·Φp + N·Φn)`

so if the two fluxes are within a factor `r` of each other, the observable is at
most `(r − 1)/A` of the bounded quantity (`split_fraction_bound`). For the
`A = 3…63` ladder that is a **falling** budget: at `A = 63` with `r = 2` it is
1.6 %, and it gets tighter as `A` grows.

The consequence for the route, stated as the obligation it creates: for the
two-sided interval to be narrower than the split it is meant to explain, the
**combined** relative slack of the two bounds must fall below `(r − 1)/A`
(`interval_narrower_than_split_forces_tight_bounds`). Freedman–He-type bounds are
order-of-magnitude estimates; nothing in this literature is tight to a percent,
and the requirement sharpens with `A` rather than relaxing.

So the upper-bound route is not blocked by acquisition. Measured, and worth
recording because it is the cheaper-looking answer: **no ropelength or
ideal-knot material exists anywhere in this repo** — zero hits across `docs/`,
`computations/`, `content/`, `library/*/sections/` and `library/*/ocr/` (all 542
library directories, both tiers). But acquiring it would not rescue the route,
because the precision requirement above is independent of which upper bound one
obtains.

There is deliberately no separate "the budget tightens with `A`" theorem. One was
written and **removed**: its hypotheses did no work and its proof was
`split_fraction_bound` applied at the larger indices, so it asserted nothing the
main bound does not already say. The `1/A` is visible in `split_fraction_bound`
itself — a second declaration restating it would have been a trivial-true dressed
as monotonicity.

SCOPE — **scope-(a)**, and narrower than it may look. This bounds the observable
as a fraction of the energy *within the same model class* the sibling file
excludes (vertex-transitive carrier, charge-only flux). It says nothing about
eq. (43), which remains a true lower bound; and it assumes the two fluxes are
comparable (`Φn ≤ Φp ≤ r·Φn` with `r` finite). A model in which `Φn → 0`, so the
neutron components carry no flux at all, escapes it — and is not refuted here.

Base ring: an ordering and a multiplication are both genuinely required (the
statements compare products), so a linearly-ordered commutative ring is the right
home per AGENTS.md §7c — not the generic `CommRing` of
`FreedmanHeMirrorSplitChargeBlind.lean`, and not the weaker ordered *additive*
group of `LowerBoundCannotConstrainADifference.lean`.
-/
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.Mass.MirrorSplitIsASmallFractionOfTheEnergy

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **The observable is a `1/A` sliver of the bounded quantity.**

With `Φn ≤ Φp ≤ r·Φn` and `Φn > 0`, the mirror split `Φp − Φn` scaled by the
nucleon count `A = Z + N` is dominated by `(r − 1)` times the total
`Z·Φp + N·Φn`. Read as a fraction: `ΔE / E ≤ (r − 1)/A`.

Stated multiplicatively so no division — and hence no field — is needed. -/
theorem split_fraction_bound (Φp Φn r : R) (Z N : ℕ)
    (hn : 0 < Φn) (hle : Φn ≤ Φp) (hr : Φp ≤ r * Φn) :
    ((Z : R) + (N : R)) * (Φp - Φn) ≤ (r - 1) * ((Z : R) * Φp + (N : R) * Φn) := by
  have hZ : (0 : R) ≤ (Z : R) := Nat.cast_nonneg Z
  have hN : (0 : R) ≤ (N : R) := Nat.cast_nonneg N
  -- the total is at least `A·Φn`, since every component carries at least `Φn`
  have hlow : ((Z : R) + (N : R)) * Φn ≤ (Z : R) * Φp + (N : R) * Φn := by
    have : (Z : R) * Φn ≤ (Z : R) * Φp := mul_le_mul_of_nonneg_left hle hZ
    linarith
  -- and the split is at most `(r − 1)·Φn`
  have hsplit : Φp - Φn ≤ (r - 1) * Φn := by nlinarith
  -- `r ≥ 1`, since `Φn ≤ Φp ≤ r·Φn` with `Φn > 0`
  have hr1 : (1 : R) ≤ r := by nlinarith
  nlinarith [mul_le_mul_of_nonneg_left hlow (sub_nonneg.mpr hr1)]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- The interval `[B₁ − U₂, U₁ − B₂]` has width exactly the **sum of the two
slacks**. Pure ring algebra; isolated so it is checkable on its own. -/
theorem interval_width (B₁ U₁ B₂ U₂ : R) :
    (U₁ - B₂) - (B₁ - U₂) = (U₁ - B₁) + (U₂ - B₂) := by ring

omit [IsStrictOrderedRing R] in
/-- **The obligation a two-sided bound would have to meet.** The interval is
narrower than the split it is meant to explain *exactly when* the combined slack
is — and by `split_fraction_bound` the split is itself at most `(r − 1)/A` of the
energy. So the requirement is a joint relative tightness below `(r − 1)/A`.

An `iff`, not an implication: both directions are wanted, since the point is that
narrowing the interval is *equivalent to* tightening the bounds, with no slack
elsewhere to trade against. -/
theorem interval_narrower_than_split_iff {B₁ U₁ B₂ U₂ split : R} :
    (U₁ - B₂) - (B₁ - U₂) < split ↔ (U₁ - B₁) + (U₂ - B₂) < split := by
  rw [interval_width]

end QOU.Mass.MirrorSplitIsASmallFractionOfTheEnergy
