/-
# The A=4 (⁴He) magnitude via the interface operator + s5-so3 geometric W_λ is a
# BRACKET, not a closure: the two canonical 0-fit reweightings straddle the AME target
# but neither hits it, and the normalized-measure bound does NOT exclude the target —
# WALL(scope-(a)), NOT a structural (b) exclusion.

Option-E PROBE 2 (the A=4 interface operator + `conj:s5-so3-fiber-action`), forward,
0-fit.  #4378 (`HeliumBrunnianDeficitMeasured`) measured `τ_L₄ > 1` for the genuine
4-component Brunnian link, so `c₄ = E₀·(1 − τ_L₄) < 0` is sign-COMPATIBLE with the
derived `μ₄ = −4.591 < 0`: the A=4 SIGN is settled and the MAGNITUDE became the live,
open test.  This file records the forward, 0-fit magnitude finding.

**The s5-so3 fiber action supplies a NORMALIZED color-tube weight.**  Per
`brings-surface/inter-nucleon-channel-color-tube.md` the color-tube weight `W_λ` from the
`S₅ ↔ SO(3)` fiber action is **normalised to `Σ_λ W_λ = 1`**, and the genuine geometric
(Beasley–Witten / WRT(S³/2I)) measure is `W_geom_λ = d_q(λ)²/D²`, `D² = Σ d_q²`
(`WLambdaMTCLocalizationObligation.lean` C1: `Σ W_geom = 1`, "NOT `[n]_q!`").

**The structural invariant (this file).**  A normalized non-negative measure `W`
(`Σ W_i = 1`, `W_i ≥ 0`) reweighting per-block characters `x_i` gives a WEIGHTED
AVERAGE, hence `|Σ_i W_i x_i| ≤ max_i |x_i|` (`normalized_reweight_abs_le_bound`).  So
the s5-so3 interface magnitude at the energy scale `E₀` is bounded by `E₀·max_λ|χ_λ|`.

**The A=4 forward measurement (0-fit, `s5so3_geometric_wlambda_a4_helium_probe.py` on the
canonical b0vf `H₁₂` per-block character table `chi-helium-4-h12-at-q0-50dps`).**
With `E₀ = m_e/(q₀(q₀−1)) ≈ 4.18598 MeV` and `max_λ|χ_λ| = 63.62` (at `λ=(6,3,3)`):

| object | value (MeV) | vs `B(⁴He)=28.296` | vs `|μ₄|=4.591` |
|---|---|---|---|
| production `E₀·Σ_λ y_λ|χ_λ|` (undershoot) | `0.24275` | `0.0086×` | `0.053×` |
| geometric `E₀·Σ_λ W_geom_λ|χ_λ|` (overshoot) | `60.32647` | `2.132×` | `13.14×` |
| bound `E₀·max_λ|χ_λ|` | `266.3285` | `9.412×` | `58.01×` |

The reweight ratio `r_geom = (Σ W_geom|χ|)/(Σ y|χ|) = 248.5` (the A=3 analog was `47.4`,
#4392 — the geometric measure concentrates on the super-exponentially large `d_q²` middle
blocks even more strongly at `n=12`).

**Reading.**  The two canonical 0-fit reweightings BRACKET both AME targets
(`0.243 < 4.591 < 60.33` and `0.243 < 28.296 < 60.33`) but NEITHER equals a target.  The
normalized-measure bound `E₀·max|χ| = 266 MeV` is ABOVE both targets, so the target lies
strictly inside the achievable span — it is **reachable in principle by some normalized
`W`**, hence this is **NOT a scope-(b) structural exclusion**.  An EXACT hit requires an
intermediate weight lying between production and geometric that is not fixed by either
canonical form — i.e. a **tuned weight = FIT**, declined.  So the s5-so3 interface
operator does **not** supply the A=4 magnitude as-is: **WALL(scope-(a))**, mirroring the
now-completely-bracketed A=3 magnitude.  `μ₄`/`B(⁴He)` are never inverted; nothing wired;
`free_parameters = 0`.

Base ring (§7c): `ℝ` for the numeric bracket facts (archimedean ordering / `abs`).  The
abstract bound lemma is stated over `ℝ` as well since it is an `abs`/`≤` statement; it
uses no field-specific structure beyond an ordered field with `abs`.

-- Ref: [leitner2026] computations/deltalambda/s5so3-geometric-wlambda-a4-helium.witness.json
   (forward 0-fit; B(⁴He)_AME & |μ₄| targets only, never inverted).
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors", Invent. Math. 92 (1988) 349-383.
-/
import Mathlib.Tactic
import Mathlib.Algebra.Order.BigOperators.Group.Finset

namespace QOU.MassTheory.GeometricWLambdaA4Helium

open Finset

/-! ### The structural invariant: a normalized reweighting is bounded by the max block -/

/-- **Weighted-average bound.**  Let `W : ι → ℝ` be a non-negative measure
(`0 ≤ W i`) that sums to one (`∑ W i = 1`), and let `x : ι → ℝ` be per-block values with
`|x i| ≤ B` for every `i`.  Then the reweighted total is bounded by `B`:

  `|∑ i, W i * x i| ≤ B`.

This is the structural reason the s5-so3 interface magnitude `E₀·Σ_λ W_λ χ_λ` (any
normalized color-tube weight `W`, geometric or otherwise) is bounded by `E₀·max_λ|χ_λ|`:
a normalized reweighting produces a weighted AVERAGE, never exceeding the largest block. -/
theorem normalized_reweight_abs_le_bound
    {ι : Type*} [Fintype ι] (W x : ι → ℝ) (B : ℝ)
    (hW : ∀ i, 0 ≤ W i) (hsum : ∑ i, W i = 1) (hbound : ∀ i, |x i| ≤ B) :
    |∑ i, W i * x i| ≤ B := by
  calc |∑ i, W i * x i|
      ≤ ∑ i, |W i * x i| := Finset.abs_sum_le_sum_abs _ _
    _ = ∑ i, W i * |x i| := by
          refine Finset.sum_congr rfl (fun i _ => ?_)
          rw [abs_mul, abs_of_nonneg (hW i)]
    _ ≤ ∑ i, W i * B := by
          refine Finset.sum_le_sum (fun i _ => ?_)
          exact mul_le_mul_of_nonneg_left (hbound i) (hW i)
    _ = (∑ i, W i) * B := by rw [Finset.sum_mul]
    _ = B := by rw [hsum, one_mul]

/-- **Non-negativity of the bound follows** (when the index set is nonempty): with
`|x i₀| ≤ B` and `0 ≤ |x i₀|`, `B` is non-negative.  A convenience corollary used to keep
`B = E₀·max|χ|` on the correct (positive) side of the target comparisons below. -/
theorem bound_nonneg {ι : Type*} (x : ι → ℝ) (B : ℝ) (i₀ : ι)
    (hbound : ∀ i, |x i| ≤ B) : 0 ≤ B :=
  le_trans (abs_nonneg (x i₀)) (hbound i₀)

/-! ### The A=4 forward-measured endpoints (ℝ, 0-fit; targets only, never inverted) -/

/-- Production reweighting `E₀·Σ_λ y_λ|χ_λ(⁴He)|` at the canonical `H₁₂` table — the
UNDERSHOOT endpoint (`≈ 0.24275 MeV`). -/
noncomputable def prodMagnitude : ℝ := 0.24275

/-- Genuine geometric reweighting `E₀·Σ_λ W_geom_λ|χ_λ(⁴He)|`, `W_geom = d_q²/D²`
(Beasley–Witten, `Σ = 1`) — the OVERSHOOT endpoint (`≈ 60.32647 MeV`, forward 0-fit). -/
noncomputable def geomMagnitude : ℝ := 60.32647

/-- The normalized-measure bound `E₀·max_λ|χ_λ|` (`≈ 266.3285 MeV`): the largest value ANY
normalized color-tube reweighting can produce (`normalized_reweight_abs_le_bound`). -/
noncomputable def maxCharBound : ℝ := 266.3285

/-- AME ⁴He total binding, `B(⁴He) ≈ 28.29566 MeV` — a TARGET, never inverted. -/
noncomputable def B4He : ℝ := 28.29566

/-- The derived A=4 4-body simplex residual magnitude `|μ₄| ≈ 4.591048 MeV`
(`AdditiveResidualSimplex`, forward AME−model) — a TARGET, never inverted. -/
noncomputable def absMu4 : ℝ := 4.591048

/-! ### The bracket: both targets sit strictly between the two canonical 0-fit endpoints -/

/-- **Both canonical 0-fit reweightings BRACKET the full ⁴He binding target.**  The
production reweighting undershoots (`0.243 < 28.296`) and the geometric reweighting
overshoots (`28.296 < 60.326`): `B(⁴He)` lies strictly between the two 0-fit endpoints. -/
theorem bracket_B4He : prodMagnitude < B4He ∧ B4He < geomMagnitude := by
  unfold prodMagnitude B4He geomMagnitude; constructor <;> norm_num

/-- **Both canonical 0-fit reweightings BRACKET the 4-body residual target** too:
`0.243 < 4.591 < 60.326`.  The same two endpoints straddle `|μ₄|`. -/
theorem bracket_absMu4 : prodMagnitude < absMu4 ∧ absMu4 < geomMagnitude := by
  unfold prodMagnitude absMu4 geomMagnitude; constructor <;> norm_num

/-- **The geometric reweighting does NOT equal either target** (it overshoots both):
`geomMagnitude ≠ B(⁴He)` and `geomMagnitude ≠ |μ₄|`. -/
theorem geom_ne_targets : geomMagnitude ≠ B4He ∧ geomMagnitude ≠ absMu4 := by
  unfold geomMagnitude B4He absMu4
  constructor <;> norm_num

/-- **The production reweighting does NOT equal either target** (it undershoots both). -/
theorem prod_ne_targets : prodMagnitude ≠ B4He ∧ prodMagnitude ≠ absMu4 := by
  unfold prodMagnitude B4He absMu4
  constructor <;> norm_num

/-! ### NOT a (b) exclusion: the normalized-measure bound is ABOVE both targets -/

/-- **The normalized-measure bound does NOT exclude the targets.**  `E₀·max|χ| = 266 MeV`
is strictly greater than both `B(⁴He) = 28.296` and `|μ₄| = 4.591`, so the weighted-average
bound `normalized_reweight_abs_le_bound` does NOT forbid a normalized reweighting from
reaching the target.  Therefore the A=4 magnitude gap is **NOT a scope-(b) structural
exclusion** — the target is reachable in principle by SOME normalized `W`. -/
theorem targets_within_bound : B4He < maxCharBound ∧ absMu4 < maxCharBound := by
  unfold B4He absMu4 maxCharBound
  constructor <;> norm_num

/-! ### Capstone: WALL(scope-(a)) — bracketed but not closed, and not excluded -/

/-- **(CAPSTONE) The s5-so3 interface reweighting BRACKETS but does not CLOSE the A=4
magnitude, and does not EXCLUDE it — WALL(scope-(a)).**

For each AME target `t ∈ {B(⁴He), |μ₄|}` the forward, 0-fit computation establishes,
simultaneously:

* **bracket** — `prodMagnitude < t < geomMagnitude`: the two canonical reweightings
  (production `y_λ`, geometric `d_q²/D²`) straddle the target;
* **no closure** — `geomMagnitude ≠ t`: the canonical geometric endpoint overshoots,
  it does not land on the target;
* **not excluded** — `t < maxCharBound`: the normalized-measure bound
  (`normalized_reweight_abs_le_bound`) lies above the target, so no invariant forbids
  reaching it.

Hence the A=4 magnitude is **open at scope-(a)**: the s5-so3 interface operator does not
supply it as-is (this construction alone), but the target is reachable in principle — an
EXACT hit needs an intermediate, TUNED weight (a FIT), which the anti-fit discipline
declines.  This mirrors the completely-bracketed A=3 magnitude.  No `μ₄`/`B(⁴He)`
inversion; nothing wired. -/
theorem a4_magnitude_bracketed_not_closed_not_excluded :
    -- full ⁴He binding
    (prodMagnitude < B4He ∧ B4He < geomMagnitude) ∧ geomMagnitude ≠ B4He ∧ B4He < maxCharBound ∧
    -- 4-body residual
    (prodMagnitude < absMu4 ∧ absMu4 < geomMagnitude) ∧ geomMagnitude ≠ absMu4 ∧ absMu4 < maxCharBound :=
  ⟨bracket_B4He, geom_ne_targets.1, targets_within_bound.1,
   bracket_absMu4, geom_ne_targets.2, targets_within_bound.2⟩


/-! ### Convex-interpolation mixing fractions for the two AME targets (`qou-9nq9`) -/

/-- The unique mixing parameter `θ*(t)` such that
`(1 - θ) * prodMagnitude + θ * geomMagnitude = t`. -/
noncomputable def mixingFraction (t : ℝ) : ℝ :=
  (t - prodMagnitude) / (geomMagnitude - prodMagnitude)

/-- **Exact convex-combination identity and distinctness of target fractions (`qou-9nq9`).**
For any target `t`, `(1 - mixingFraction t) * prodMagnitude + mixingFraction t * geomMagnitude = t`,
and the mixing fractions required by `B4He` and `absMu4` both lie strictly in `(0, 1)` and are
distinct (`mixingFraction absMu4 < mixingFraction B4He`), so no single convex combination of
production and geometric weights can match both targets simultaneously. -/
theorem mixingFraction_identity_and_target_separation (t : ℝ) :
    (1 - mixingFraction t) * prodMagnitude + mixingFraction t * geomMagnitude = t ∧
      0 < mixingFraction absMu4 ∧
      mixingFraction absMu4 < mixingFraction B4He ∧
      mixingFraction B4He < 1 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold mixingFraction prodMagnitude geomMagnitude
    ring
  · unfold mixingFraction prodMagnitude geomMagnitude absMu4
    norm_num
  · unfold mixingFraction prodMagnitude geomMagnitude absMu4 B4He
    norm_num
  · unfold mixingFraction prodMagnitude geomMagnitude B4He
    norm_num

end QOU.MassTheory.GeometricWLambdaA4Helium
