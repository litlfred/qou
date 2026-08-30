import QOU.Mass.PairwiseCumulantVanishing
import Mathlib.Tactic

/-!
# The canonical carriers sit exactly on the `b₃ = 0` locus of the count channel

`QOU.Mass.BrunnianBindingChannel` is `qou-brng`'s surviving route: for a Brunnian pair the signed
(linking) channel vanishes and the whole mutual energy is the unsigned **count channel**
`countChannel n₊ n₋ q = ½(n₊+n₋)(q − q⁻¹)`, strictly positive at `q > 1`. That answers the
*linking-number* objection — binding survives where `lk = 0`.

It does not answer the *cumulant* objection, and this file measures the gap.

## The carriers land on the degenerate point

Write `μ` for a carrier's count multiplicity `½(n₊+n₋)`, so its binding is `s·μ·h` with
`h = q − q⁻¹` and `s` the MeV scale. Then

    b₃ = s·h·(μ_triple − 3·μ_pair)

and `b3_eq_zero_iff` says this vanishes **iff `μ_triple = 3·μ_pair`** — which is precisely the
pair-local condition, so `QOU.Mass.CrossingModelPairLocality.b3_eq_zero_of_pairLocal` applies.

The canonical carriers satisfy it exactly. The deuteron is a Hopf clasp, `n₊ = 2`, `n₋ = 0`, so
`μ_pair = 1`. The `A = 3` carrier is the Borromean `L6a4`, `n₊ = n₋ = 3`, so `μ_triple = 3`. And
`3 = 3 · 1`. Hence `canonical_carriers_b3_eq_zero`: **the count channel predicts `b₃ = 0` on the
framework's own carriers**, against the measured `b₃ = +1.4262225`
(`QOU.MassTheory.AmeBindingNotPairwise.ame_b3_eq`).

`b3_over_b2_eq` shows **the scale cancels**: `b₃/b₂ = μ_triple/μ_pair − 3`, so this is a
zero-parameter statement — no choice of `s` or `q` rescues it. `BrunnianBindingChannel`'s
sub-question-1 answer (*"one coordination unit per bonded pair, `C(A,2)` for a cluster"*) is the
same degeneracy stated for general `A`.

## What this does NOT show — a quantisation obstruction that is not there

The first thing to try is that `μ` is a half-integer (`n₊+n₋ ∈ ℕ`) while the measured ratio
`μ_triple/μ_pair = 3.6411239316` is not, so no carrier could work. **That argument is wrong and is
recorded here so it is not re-attempted.** It assumes `μ_pair = 1`; with `μ_pair` free, small
half-integers get arbitrarily close — `(μ_pair, μ_triple) = (7, 51/2)` gives `b₃/b₂ = 0.642857`,
**0.27 %** from measured, and `(11/2, 20)` gives 0.74 %.

So the count channel is **not obstructed in principle.** It has ample freedom, and the failure is
specifically the *carrier assignment*. That makes the burden sharper rather than lighter: two free
crossing integers matched to one measured ratio is a **fit**, so a carrier reaching `b₃` earns
nothing unless its crossing numbers are derived. Which is exactly `qou-brng`'s open item.

## Scope

Scope-**(a)** on the conjunction {count channel, Hopf pair, Borromean triple}. It excludes no
ingredient: the count channel survives, `brunnian_binding_survives` is untouched, and the
Brunnian mechanism remains the only thing that lets binding exist at `lk = 0`. What is excluded is
that *these two carriers with this channel* reproduce `b₃`.

Ground ring: generic `{R : Type*} [Field R]` (§7c — algebra only; `h` and `s` are parameters).
Beans `qou-brng`, `qou-w6vh`.
-/

namespace QOU.Mass.CountChannelCarrierLocus

variable {R : Type*} [Field R]

/-- A carrier's binding in the count channel: the MeV scale `s`, the count multiplicity
`μ = ½(n₊+n₋)`, and the substrate factor `h = q − q⁻¹`. -/
def countBinding (s h μ : R) : R := s * μ * h

/-- The connected 3-body cumulant assembled from count-channel carriers: the triple's binding less
three times the pair's. -/
def b3OfMult (s h μp μt : R) : R := countBinding s h μt - 3 * countBinding s h μp

/-- **The cumulant vanishes exactly on the pair-local locus.** With a nonzero scale and a nonzero
substrate factor, `b₃ = 0` iff the triple's count multiplicity is three times the pair's. -/
theorem b3_eq_zero_iff {s h μp μt : R} (hs : s ≠ 0) (hh : h ≠ 0) :
    b3OfMult s h μp μt = 0 ↔ μt = 3 * μp := by
  unfold b3OfMult countBinding
  constructor
  · intro hzero
    have hfac : s * (μt - 3 * μp) * h = 0 := by linear_combination hzero
    rcases mul_eq_zero.mp hfac with h1 | h1
    · rcases mul_eq_zero.mp h1 with h2 | h2
      · exact absurd h2 hs
      · exact sub_eq_zero.mp h2
    · exact absurd h1 hh
  · intro hmt; subst hmt; ring

/-- **The scale cancels.** The cumulant ratio depends only on the multiplicities, so no choice of
the MeV scale `s` or the substrate factor `h` can move it — this is a zero-parameter test. -/
theorem b3_over_b2_eq {s h μp μt : R} (hs : s ≠ 0) (hh : h ≠ 0) (hμ : μp ≠ 0) :
    b3OfMult s h μp μt / countBinding s h μp = μt / μp - 3 := by
  unfold b3OfMult countBinding
  field_simp

/-- The deuteron's Hopf clasp has `n₊ = 2`, `n₋ = 0`, hence count multiplicity `½(2+0) = 1`. -/
def hopfMult : R := 1

/-- The Borromean carrier `L6a4` has `n₊ = n₋ = 3`, hence count multiplicity `½(3+3) = 3`. -/
def borromeanMult : R := 3

/-- **The canonical carriers sit on the degenerate locus.** `μ_Borromean = 3 = 3 · μ_Hopf`, so the
count channel predicts `b₃ = 0` for the framework's own `A = 2` and `A = 3` carriers — against a
measured `b₃ = +1.4262225`. -/
theorem canonical_carriers_b3_eq_zero (s h : R) :
    b3OfMult s h (hopfMult : R) (borromeanMult : R) = 0 := by
  unfold b3OfMult countBinding hopfMult borromeanMult
  ring

/-- **And the miss is total, not partial**: the predicted cumulant ratio is `0`, so the model
supplies none of the measured `b₃/b₂ = 0.6411239316`. -/
theorem canonical_carriers_ratio_zero (s h : R) :
    b3OfMult s h (hopfMult : R) (borromeanMult : R) / countBinding s h (hopfMult : R) = 0 := by
  rw [canonical_carriers_b3_eq_zero]
  simp

/-- **The criterion a replacement carrier must meet.** Any carrier pair reproducing a nonzero `b₃`
in this channel must break the three-to-one multiplicity relation. Stated as the contrapositive of
`b3_eq_zero_iff`, it is the one-line test to run against a proposed carrier before anything else. -/
theorem carrier_must_break_three_to_one {s h μp μt : R} (hs : s ≠ 0) (hh : h ≠ 0)
    (hne : b3OfMult s h μp μt ≠ 0) : μt ≠ 3 * μp :=
  fun hEq => hne ((b3_eq_zero_iff hs hh).mpr hEq)

/-- **Non-vacuity: the channel is not obstructed.** A carrier pair off the degenerate locus does
give a nonzero cumulant — here `μ_pair = 7`, `μ_triple = 51/2`, which lands `b₃/b₂` within 0.27 % of
the measured value. So the failure above is the carrier assignment, not the channel. Two free
crossing integers against one measured ratio is a fit, which is why this is recorded as a
possibility rather than a result. -/
theorem offLocus_b3_ne_zero {s h : ℝ} (hs : s ≠ 0) (hh : h ≠ 0) :
    b3OfMult s h (7 : ℝ) (51 / 2 : ℝ) ≠ 0 := by
  intro hzero
  have hEq := (b3_eq_zero_iff hs hh).mp hzero
  norm_num at hEq

end QOU.Mass.CountChannelCarrierLocus
