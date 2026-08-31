/-
# Carrier crossing numbers are quantised, and no integer choice reaches `b₃`

`qou-brng` asks where the count channel's multiplicity `μ` comes from, rather than
being fitted. This file answers it for `A ≤ 3` and the answer is a **negative with a
width**: once the pair carrier is fixed, `μ` ranges over a *lattice*, and the measured
`b₃` falls in a gap between two lattice points — nearest miss **16.98 %**.

## Where the multiplicity comes from

`QOU.Mass.CountChannelCarrierLocus` fixes the shape: the count channel carries
`μ = (n₊ + n₋)/2`, i.e. **half the carrier's crossing count**, and `b3_over_b2_eq`
shows the scale cancels, so

    b₃/b₂ = μ_triple/μ_pair - 3 = c₃/c₂ - 3.

Everything below is that identity plus one integrality fact: `c₂` and `c₃` are
**crossing counts of braid words**, hence non-negative integers.

## The assumption that changed, and why the old obstruction is now live

`CountChannelCarrierLocus` records a quantisation argument as **wrong**: half-integer
`μ` cannot reach `3.6411…`, *"but that assumes `μ_pair = 1`; with `μ_pair` free, small
half-integers get arbitrarily close"*. That retraction was correct at the time.

**Owner ruling A of 2026-08-29 supplies the missing assumption.** The deuteron carrier
is the canonical braid closure — the Hopf link, `σ_g²`, `c₂ = 2` — so `μ_pair = 1` is no
longer free. With `c₂` pinned the freedom collapses to the single integer `c₃`, and the
obstruction is back. It is now **conditional on that ruling**, not on a guess.

## What the corpus actually derives, four ways — all of them `b₃ ≤ 0`

| rule, and where it is derived | `c₂` | `c₃` | `b₃/b₂` |
|---|---|---|---|
| min-length enumeration, `binding-k-enumerator` (`σ_g²` for **all three** nuclei) | 2 | 2 | `-2` |
| one clasp per interface — the chain, `z = A-1` | 2 | 4 | `-1` |
| canonical Brunnian carriers (Hopf, Borromean `L6a4`) | 2 | 6 | `0` |
| census volume-match (`6₂`; avg of `8₁₁`, `L6a4`) | 6 | 7 | `-11/6` |

Measured: `b₃/b₂ = +0.6411239316`. Every consistent rule is at or below zero.

Two of these deserve a note. The **enumeration** returns `bindingKWord = [3,3] = σ_3²`
for deuterium, tritium *and* helium-3 alike — the labels `6₂` / `8₁₁` / `L6a4` on those
Lean instances are retained census *names*, not what was enumerated. Its selection
criterion is shortest-PSD-feasible-even-word at `L ≤ 3`, which cannot see `A` at all,
so it can only ever return a constant `μ`. And the **census** row is
`manual-historical-volume-match`, which the atlas registry itself flags as AME-inverted
(*"we picked the knot whose volume is closest to `B_AME/ρ`"*) — circular, and not usable
as a derivation whatever number it gives.

## 🛑 The trap: mixing two carrier assignments manufactures the right sign

Taking `c₂ = 2` from the owner-ruled Hopf deuteron and `c₃ = 7` from the census A = 3
row gives `b₃/b₂ = +1/2` — right sign, 22 % low, and **meaningless**, because the two
numbers come from different assignments. Read either assignment *consistently* and the
result is `0` or `-11/6`. `straddle_manufactures_the_sign` records the arithmetic so the
coincidence is not rediscovered as a result. This is the layer-straddle failure mode of
AGENTS.md §"Never straddle the two layers inside one quantity", one arc over.

## The obstruction

With `c₂ = 2`, `b₃/b₂ = c₃/2 - 3` ranges over the **half-integer** lattice, and if `³H`
and `³He` carry different links the isospin-averaged `μ_triple` puts it on the
**quarter-integer** lattice. The measured `0.6411239316` sits strictly inside a gap in
both:

* half-integer grid — `c₃ = 7` gives `0.5` (22.01 % low), `c₃ = 8` gives `1.0` (55.98 % high);
* quarter-integer grid — `c(³H)+c(³He) = 15` gives `0.75`, **16.98 % high**, the nearest
  approach of any integer carrier assignment.

`no_quarter_lattice_point_is_measured` and `quarter_lattice_gap` prove the finer of the
two: every integer `m` keeps `m/4 - 3` at least `161468/1483044 ≈ 0.10887` from the
measured ratio. The coarser half-integer statement follows since that grid is a subset.

## And the selection principle points the wrong way

Escaping the gap needs `c₃ ≥ 8` — strictly more than the Borromean's `6`. But `6` is
**minimal**: `QOU.Knots.KauffmanTL3` machine-checks that no braid word of length `< 6` is
both Brunnian and nontrivial. So a carrier that could reach `b₃` must be a
**non-minimal** Brunnian representative, while the only selection principle the corpus
derives — shortest PSD-feasible word — returns the minimum by construction. The
principle and the requirement are in direct opposition; that, not the arithmetic, is the
substantive obstacle `qou-brng` now faces.

## Sibling result, landed on `main` the same hour

`be017ea57b` (`qou-brng`, another session) guards the *other* direction on the same
multiplicity: **inverting** the `CoordinationSaturation` plateau for a coordination
number `k` is generic — 27 of 30 (`eps`, target) combinations land inside the plausible
window, so a `k` near 6 or 12 is not the framework predicting a lattice. Taken together
the two close both routes to a multiplicity: **inverting** an anchor for it is a fit,
and **deriving** it from the carrier gives the wrong sign.

They are about different graphs and should not be conflated. Their `k` is a *bounded*
degree; the `chain / coordination z = A-1` row above is the **complete** graph, which
`CoordinationSaturation` already excludes by saturation (it gives `B/A = eps(A-1)/2`,
unbounded, hence no plateau). So this file's chain row re-derives the excluded case
from the crossing side and finds it at `-1`; it is not a second measurement of their `k`.

## Scope

Scope **(b)** on the conjunction, with the invariant named — *integrality of a crossing
count*, given `c₂ = 2`: no integer carrier assignment reproduces `b₃`, and the nearest
approach is 16.98 % away. Scope **(a)** on every ingredient separately. It does **not**
exclude the count channel, the Brunnian mechanism (`brunnian_binding_survives` is
untouched), or `μ = c/2`; it says these four cannot hold *together* with the Hopf pair
carrier. Releasing any one reopens it — the cheapest candidate being `μ = c/2` itself,
since a multiplicity that is not half the crossing count is not lattice-valued.

Ground ring: generic `[Field R]` for the identities (AGENTS.md §7c); the lattice results
descend to `ℚ`, where the ordering and `Int.cast` are needed.

Beans `qou-brng`, `qou-w6vh`, `qou-n6im`.
-/
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Algebra.Order.Field.Basic

namespace QOU.Mass.CarrierCrossingQuantisation

variable {R : Type*} [Field R] [CharZero R]

/-! ## 1. The multiplicity is half the crossing count -/

/-- The count-channel multiplicity of a carrier with crossing count `c`, namely
`(n₊ + n₋)/2 = c/2` (`QOU.Mass.CountChannelCarrierLocus.countChannel`). -/
def muOfCrossings (c : R) : R := c / 2

/-- `b₃/b₂` as a function of the pair and triple multiplicities
(`CountChannelCarrierLocus.b3_over_b2_eq` — the scale has already cancelled). -/
def bRatio (muP muT : R) : R := muT / muP - 3

/-- **`b₃/b₂` is a ratio of crossing counts.** The factor of `½` cancels, so the
multiplicity convention drops out and only `c₃/c₂` survives. No hypothesis on `c₂` is
needed: the cancellation is an identity of `Field` division, degenerate case included. -/
theorem bRatio_of_crossings (c₂ c₃ : R) :
    bRatio (muOfCrossings c₂) (muOfCrossings c₃) = c₃ / c₂ - 3 := by
  unfold bRatio muOfCrossings
  rw [div_div_div_cancel_right₀ (by norm_num : (2:R) ≠ 0)]

/-- **With the owner-ruled Hopf pair carrier (`c₂ = 2`) the whole thing is one
integer.** This is the step the earlier retraction was missing. -/
theorem bRatio_hopf_pair (c₃ : R) :
    bRatio (muOfCrossings 2) (muOfCrossings c₃) = c₃ / 2 - 3 := by
  rw [bRatio_of_crossings (2:R) c₃]

/-! ## 2. The four derived rules -/

/-- Min-length enumeration: `σ_g²` for every nucleus, so `c₃ = 2` and `b₃/b₂ = -2`. -/
theorem enumerated_carrier : bRatio (muOfCrossings (2:ℚ)) (muOfCrossings 2) = -2 := by
  rw [bRatio_hopf_pair]; norm_num

/-- One clasp per interface (the chain, `z = A-1`): `c₃ = 4`, `b₃/b₂ = -1`. -/
theorem chain_carrier : bRatio (muOfCrossings (2:ℚ)) (muOfCrossings 4) = -1 := by
  rw [bRatio_hopf_pair]; norm_num

/-- Canonical Brunnian carriers (Hopf, Borromean `L6a4`): `c₃ = 6`, exactly the
degenerate locus. Agrees with `CountChannelCarrierLocus.canonical_carriers_b3_eq_zero`,
reached here from the crossing counts rather than from `n₊`/`n₋`. -/
theorem borromean_carrier : bRatio (muOfCrossings (2:ℚ)) (muOfCrossings 6) = 0 := by
  rw [bRatio_hopf_pair]; norm_num

/-- Census volume-match read consistently (`c₂ = 6` from `6₂`, `c₃ = 7` from the average
of `8₁₁` and `L6a4`): `-11/6`. Recorded for completeness — the tier is AME-inverted and
is not a derivation. -/
theorem census_carrier_consistent :
    bRatio (muOfCrossings (6:ℚ)) (muOfCrossings 7) = -11/6 := by
  rw [bRatio_of_crossings (6:ℚ) 7]; norm_num

/-- 🛑 **The straddle.** `c₂ = 2` from the owner-ruled Hopf deuteron against `c₃ = 7`
from the census A = 3 row gives the right sign — from two different assignments. Not a
result; recorded so the coincidence is not rediscovered as one. -/
theorem straddle_manufactures_the_sign :
    bRatio (muOfCrossings (2:ℚ)) (muOfCrossings 7) = 1/2 := by
  rw [bRatio_hopf_pair]; norm_num

/-! ## 3. The lattice obstruction -/

/-- The measured `b₃/b₂` from AME2020, exactly:
`b₂ = 2.224566`, `B̄(3) = 8.0999205`, `b₃ = B̄(3) - 3b₂ = 1.4262225`. -/
def rMeasured : ℚ := 950815 / 1483044

/-- The measured ratio sits strictly inside the gap `(1/2, 3/4)` of the
quarter-integer lattice. -/
theorem rMeasured_mem_gap : (1:ℚ)/2 < rMeasured ∧ rMeasured < 3/4 := by
  constructor <;> · unfold rMeasured; norm_num

/-- **No integer carrier assignment reproduces the measured `b₃`.** With `c₂ = 2` and
`μ_triple` the isospin average of two integer crossing counts, `b₃/b₂` lands on the
quarter-integer lattice `m/4 - 3`, which misses `rMeasured` for every `m`. -/
theorem no_quarter_lattice_point_is_measured (m : ℤ) :
    (m : ℚ) / 4 - 3 ≠ rMeasured := by
  intro hEq
  obtain ⟨hlo, hhi⟩ := rMeasured_mem_gap
  rw [← hEq] at hlo hhi
  -- `1/2 < m/4 - 3 < 3/4` forces `14 < m < 15`
  have h14 : (14 : ℚ) < (m : ℚ) := by linarith
  have h15 : (m : ℚ) < 15 := by linarith
  have h14' : (14 : ℤ) < m := by exact_mod_cast h14
  have h15' : m < (15 : ℤ) := by exact_mod_cast h15
  omega

/-- **And it misses by a fixed amount.** Every quarter-integer lattice point stays at
least `161468/1483044 ≈ 0.10887` from the measured ratio — `16.98 %` of it. The nearest
is `m = 15`, i.e. `c(³H) + c(³He) = 15`; the half-integer grid of a *single* `A = 3`
carrier is a sublattice, so it misses by at least as much (in fact `c₃ = 7`, `22.01 %`). -/
theorem quarter_lattice_gap (m : ℤ) :
    161468 / 1483044 ≤ |(m : ℚ) / 4 - 3 - rMeasured| := by
  obtain ⟨hlo, hhi⟩ := rMeasured_mem_gap
  rcases le_or_gt m 14 with h | h
  · have hm : (m : ℚ) ≤ 14 := by exact_mod_cast h
    rw [abs_of_nonpos (by linarith)]
    unfold rMeasured at hlo ⊢
    linarith
  · have hm : (15 : ℚ) ≤ (m : ℚ) := by exact_mod_cast h
    rw [abs_of_nonneg (by linarith)]
    unfold rMeasured at hhi ⊢
    linarith

/-- **The escape requires a non-minimal Brunnian carrier.** Any `c₃` reaching a positive
`b₃/b₂` at all needs `c₃ > 6` — strictly more than the Borromean's crossing number,
which `QOU.Knots.KauffmanTL3` machine-checks is the *minimum* over nontrivial Brunnian
3-braids. So the carrier cannot be a minimal one, while the corpus's only derived
selection principle (shortest PSD-feasible word) returns exactly the minimum. -/
theorem positive_b3_forces_above_borromean {c₃ : ℚ}
    (h : 0 < bRatio (muOfCrossings 2) (muOfCrossings c₃)) : 6 < c₃ := by
  rw [bRatio_hopf_pair] at h
  linarith

end QOU.Mass.CarrierCrossingQuantisation
