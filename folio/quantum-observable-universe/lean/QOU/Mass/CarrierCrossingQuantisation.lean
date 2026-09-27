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
* quarter-integer grid — `c(³H)+c(³He) = 15` gives `0.75`, 16.98 % high.

`no_quarter_lattice_point_is_measured` and `quarter_lattice_gap` prove the finer of the
two: every integer `m` keeps `m/4 - 3` at least `161468/1483044 ≈ 0.10887` from the
measured ratio.

**But a Brunnian carrier cannot land on the odd points, and both of those nearest
approaches are odd.** `n₊ = n₋` forces `c = n₊ + n₋` **even**
(`brunnian_crossings_even`), so `c₃ = 7` and `c(³H)+c(³He) = 15` are unreachable. The
live grid is the half-integers, and `even_lattice_gap` puts every point at least
`209293/1483044 ≈ 0.14112` away — **22.01 %**, not 16.98 %. For a *single* Brunnian
`A = 3` carrier `b₃/b₂` is an outright integer
(`single_brunnian_carrier_integer_valued`) and the nearest positive value is `1`, high by
**55.98 %**.

## What has never been searched — and it is not what it looks like

Escaping the gap needs `c₃ ≥ 8`, strictly more than the Borromean's `6`, which
`QOU.Knots.KauffmanTL3` machine-checks is the minimum over nontrivial Brunnian 3-braids.

**It is tempting to conclude that the selection principle itself points the wrong way —
that the corpus selects by minimality and minimality is exactly what excludes the
carrier. That is false, and the temptation is worth recording.** Read
`binding_k_enumerator.py`'s sort key rather than the Lean instances' proxy field:

    candidates.sort(key = (0 if PSD_feasible else 1,
                           markov_residual_to_target,      # <- the criterion
                           L_K))                           # <- a TIEBREAK, third

The principle is **Frobenius-residual minimisation**, which depends on `tr_M` at
`H_{3A}(q₀)` and is therefore `A`-dependent. Length enters only to break ties. The Lean
instances carry `bindingKLengthBounded : bindingKWord.length ≤ 4`, a decidable *proxy*
field, and reading that as the criterion is what makes minimality look load-bearing.

(Named `bindingKMinimalLength` here until 2026-09-07, which was itself the confusion
this paragraph is about: there were TWO fields, a `Prop`-universe `bindingKMinimalLength`
the instance chose and a decidable `bindingKLengthBounded` the class required, and every
instance set the first to the second. The chosen copy is deleted; only the required one
remains, and it is the one this paragraph means.)

So the reason all three nuclei returned `σ_g²` is **truncation, not principle**: the
enumeration ran at `L_K_max = 4` (deuteron) and `3` (³H, ³He), and at that length
essentially nothing survives PSD-feasibility except the shortest even word. The range
where the answer could differ — word length `≥ 8` — **has never been searched**, and it
is roughly a thousand times the size of the search that was run (`4` inter-nucleon
generators, so `~87,000` words to `L = 8` against `84` to `L = 3`).

That is the live next step for `qou-brng`, and it is a compute question with a definite
answer rather than a structural impasse.

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
carrier. Releasing any one reopens it. **The cheapest-looking candidate, `μ = c/2`, is not
in fact cheap** — §2b proves the constant is immaterial (`b₃/b₂` is invariant under
`μ ↦ κμ`), so the hypothesis really in force is `μ ∝ c`, and breaking *that* means
breaking the linearity of `pairEnergy_decomp`, i.e. going at `def:crossing-energy`.

Ground ring: generic `[Field R]` for the identities (AGENTS.md §7c); the lattice results
descend to `ℚ`, where the ordering and `Int.cast` are needed.

Beans `qou-brng`, `qou-w6vh`, `qou-n6im`.
-/
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
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

/-! ## 2b. The hypothesis is `μ ∝ c`, NOT `μ = c/2` -/

omit [CharZero R] in
/-- **Rescaling the multiplicity changes nothing.** `b₃/b₂` is invariant under
`μ ↦ κμ` for any `κ ≠ 0`, so every result below holds for *any* multiplicity
proportional to the crossing count — the `½` of `countChannel` is not load-bearing.

This matters for how the obstruction can be escaped, and it corrects the obvious
guess. The `½` looks like a free convention one could simply drop; it is not, and
dropping it would not help anyway. It is the unique solution of
`BrunnianBindingChannel.pairEnergy_decomp`, the `ring` identity splitting
`n₊q − n₋q⁻¹` into its bar-even and bar-odd parts — and by this lemma any other
constant gives the same `b₃/b₂`.

So the hypothesis actually in force is **linearity**: `μ = κ·c`. Escaping the
lattice needs a *nonlinear* `μ(c)`, and that contradicts `pairEnergy_decomp`
being linear in `(n₊, n₋)`, which it is by construction. The escape route
therefore runs through `def:crossing-energy` itself, not through a convention. -/
theorem bRatio_scale_invariant (κ c₂ c₃ : R) (hκ : κ ≠ 0) :
    bRatio (κ * c₂) (κ * c₃) = bRatio c₂ c₃ := by
  unfold bRatio
  rw [mul_div_mul_left _ _ hκ]

/-- The `½` in particular is not load-bearing: reading `μ = c` rather than `μ = c/2`
gives the identical ratio. -/
theorem muOfCrossings_halving_immaterial (c₂ c₃ : R) :
    bRatio (muOfCrossings c₂) (muOfCrossings c₃) = bRatio c₂ c₃ := by
  unfold muOfCrossings
  rw [div_eq_inv_mul, div_eq_inv_mul, bRatio_scale_invariant _ _ _ (by norm_num)]

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

/-! ## 3b. A Brunnian carrier has an EVEN crossing count, which widens the gap -/

/-- **Brunnian ⇒ even.** `BrunnianBindingChannel.brunnian_signedChannel_zero` empties the
signed channel exactly when `n₊ = n₋`; then `c = n₊ + n₋ = 2n₊` is even. The `A = 2` Hopf
carrier is *not* Brunnian (`lk = 1`, `n₊ = 2`, `n₋ = 0`) — it is the boundary case where
`lk = z = 1` — so this constrains the `A ≥ 3` carriers only, which is where `b₃` lives. -/
theorem brunnian_crossings_even (np nn : ℕ) (h : np = nn) : Even (np + nn) := by
  subst h; exact ⟨np, rfl⟩

/-- **Under parity the grid coarsens to the half-integers, and the gap widens.** With
`c(³H)` and `c(³He)` both even their sum is even, so `μ_triple = (c_H + c_He)/4` is a
*half*-integer, not a quarter-integer: the lattice is `k/2 - 3`. Every point stays at
least `209293/1483044 ≈ 0.14112` from the measured ratio — **22.01 %** of it, up from the
16.98 % that ignoring parity allows.

This is what excludes the two nearest points of `quarter_lattice_gap`: `c₃ = 7` and
`c(³H)+c(³He) = 15` are both **odd**, hence unreachable by Brunnian carriers. -/
theorem even_lattice_gap (k : ℤ) :
    209293 / 1483044 ≤ |(k : ℚ) / 2 - 3 - rMeasured| := by
  obtain ⟨hlo, hhi⟩ := rMeasured_mem_gap
  have hr1 : rMeasured < 1 := by unfold rMeasured; norm_num
  rcases le_or_gt k 7 with h | h
  · have hk : (k : ℚ) ≤ 7 := by exact_mod_cast h
    rw [abs_of_nonpos (by linarith)]
    unfold rMeasured at hlo ⊢
    linarith
  · have hk : (8 : ℚ) ≤ (k : ℚ) := by exact_mod_cast h
    rw [abs_of_nonneg (by linarith)]
    unfold rMeasured at hr1 ⊢
    linarith

/-- **A single Brunnian `A = 3` carrier does worse still.** Then `μ_triple = c₃/2` with `c₃`
even, so `b₃/b₂` is an *integer*: the nearest positive value is `1` at `c₃ = 8`, **55.98 %**
high, and `0` at the Borromean `c₃ = 6` is the degenerate locus. -/
theorem single_brunnian_carrier_integer_valued (n : ℤ) :
    bRatio (muOfCrossings (2:ℚ)) (muOfCrossings (2 * (n:ℚ))) = (n:ℚ) - 3 := by
  rw [bRatio_hopf_pair]
  ring

/-- **The escape requires a non-minimal Brunnian carrier.** Any `c₃` reaching a positive
`b₃/b₂` at all needs `c₃ > 6` — strictly more than the Borromean's crossing number,
which `QOU.Knots.KauffmanTL3` machine-checks is the *minimum* over nontrivial Brunnian
3-braids. With parity (§3b) the next available value is `c₃ = 8`, not `7`.

**The corpus's selection principle is NOT minimality** — see the header's §"What has
never been searched". It is Frobenius-residual minimisation; length is only a tiebreak. -/
theorem positive_b3_forces_above_borromean {c₃ : ℚ}
    (h : 0 < bRatio (muOfCrossings 2) (muOfCrossings c₃)) : 6 < c₃ := by
  rw [bRatio_hopf_pair] at h
  linarith

end QOU.Mass.CarrierCrossingQuantisation
