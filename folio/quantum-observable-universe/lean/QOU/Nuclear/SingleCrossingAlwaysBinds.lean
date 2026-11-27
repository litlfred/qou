import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

/-!
# No single-crossing interface can unbind at the substrate anchor

`computations/probes/two_nucleon_sector_sign_probe.py` measures that the
framework binds the **diproton** (`+2.5416 MeV`) and the **dineutron**
(`+3.3069 MeV`), where nature has no bound state in either channel. This file
identifies the cause, and shows it is structural rather than a bad parameter
choice.

## The mechanism

The interface scalar of a single crossing is `μ = z + d`, with the Markov
parameter `z = q³/(q²+1)` (convention D) and the admissible interface offset `d`
running over `[-h, 0]` — `d = 0` at `σ`, `d = -h` at `σ⁻¹`, `h = q - q⁻¹`. The
binding is `B = -α·log μ`, so

    B > 0  ⟺  μ < 1.

Since the family is increasing in `d`, its maximum is `μ = z`. So **every**
single-crossing interface binds as soon as `z < 1`, and

    z < 1  ⟺  q³ < q² + 1.

At the substrate anchor `q₀ ≈ 1.10998` that reads `1.3676 < 2.2321` — satisfied
with a wide margin. Unbinding through a single crossing would need
`q > 1.46557…`, the real root of `q³ = q² + 1`; the substrate sits **24 % below**
it, so this is not a near-miss that a small correction could flip.

## What the file proves (sorry-free)

* `markov_z_lt_one` — `z < 1` from `q³ < q² + 1`.
* `h_lt_markov_z` — `h < z` for every `q > 0`, unconditionally (it reduces to
  `q⁴ - 1 < q⁴`). This is what keeps the whole family positive, so `log μ` is
  defined throughout.
* `interface_mem_Ioo` — for `d ∈ [-h, 0]`, `0 < z + d < 1`.
* `single_crossing_binds` — hence `-α · log (z + d) > 0` for `α > 0`: **every**
  admissible single-crossing interface binds.
* `writhe_normalisation_binds_harder` — the writhe grading multiplies `μ` by a
  factor in `(0,1)` when `0 < h < 1`, so the normalised scalar is *smaller* and
  the channel binds *more*. The normalisation cannot rescue the sign.
* `unbinding_needs_large_q` — contrapositive: an unbinding single crossing forces
  `q² + 1 ≤ q³`.

## Scope — this is a scope-(b) exclusion, and a narrow one

**Excluded:** any *single-crossing* interface, at any admissible `d`, with or
without the writhe normalisation, produces a **bound** channel whenever
`q³ < q² + 1`. No choice of `d` — no colour weighting, no isospin projector, no
crossing-sign assignment — can give an unbound two-nucleon channel at the
substrate anchor. The invariant is `μ ≤ z < 1` and it is proved here.

**NOT excluded:** unbinding as such. `computations/probes/stacked_interface_writhe_normalised_probe.py`
shows the writhe-normalised **even negative stacked** powers `σ^{-2}, σ^{-4}, …`
have `μ_eff > 1` and do unbind — those are *not* single crossings, so they lie
outside this theorem. Their magnitudes are 6–9× nature's, so this is a repair
*direction*, not a repair.

Also not excluded: a different `z` convention, a construction where binding is
not `-α·log μ`, or an interface built from something other than the 2-dimensional
`span{1, σ}` subalgebra.

## Why this is worth a theorem rather than a remark

The corpus already records that the Hecke spectral **projectors** cannot unbind
(`InterfaceScalar.mu_sum_eq_one`: `μ₊ + μ₋ = 1` forces both `< 1`). That is the
same conclusion for a *two-element* sub-family. This generalises it to the whole
admissible interval and, more importantly, identifies the *reason* — `z < 1` —
which is a statement about the substrate anchor rather than about projectors. It
converts "the two-nucleon signs come out wrong" from a measurement into an
invariant, which is what tells a later agent not to look for a better `d`.

## Base ring (§7c)

`ℝ` throughout: the content is an ordering statement (`0 < μ`, `μ < 1`) plus
`Real.log`, i.e. archimedean by nature.

-- Ref: [leitner2026] computations/probes/two_nucleon_sector_sign_probe.py
-- Ref: [leitner2026] docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md
-/

namespace QOU.QBeta

open Real

/-- The Markov parameter of convention D. -/
noncomputable def markovZ (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- The Hecke parameter `h = q - q⁻¹`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

theorem markovZ_pos {q : ℝ} (hq : 0 < q) : 0 < markovZ q := by
  have h1 : (0:ℝ) < q ^ 2 + 1 := by positivity
  exact div_pos (by positivity) h1

/-- **`z < 1` is exactly `q³ < q² + 1`.** This is the whole mechanism: the
interface family is capped by `z`, so this inequality decides whether any single
crossing can fail to bind. -/
theorem markovZ_lt_one {q : ℝ} (hq : 0 < q) (h : q ^ 3 < q ^ 2 + 1) :
    markovZ q < 1 := by
  have h1 : (0:ℝ) < q ^ 2 + 1 := by positivity
  rw [markovZ, div_lt_one h1]
  exact h

/-- **The gap between `z` and `h` is exactly `1/(q(q²+1))`.** The `q⁴` terms
cancel identically:

    z - h = q³/(q²+1) - (q²-1)/q = [q⁴ - (q⁴ - 1)] / [q(q²+1)] = 1/[q(q²+1)].

So the bottom of the admissible family sits a computable distance above `0`, for
every `q > 0` — there is no `q` at which the family degenerates. -/
theorem markovZ_sub_heckeH {q : ℝ} (hq : 0 < q) :
    markovZ q - heckeH q = 1 / (q * (q ^ 2 + 1)) := by
  have h1 : (q:ℝ) ^ 2 + 1 ≠ 0 := by positivity
  have hq' : (q:ℝ) ≠ 0 := ne_of_gt hq
  rw [markovZ, heckeH]
  field_simp
  ring

/-- **`h < z` for every `q > 0`, unconditionally**, by the exact gap above. This
keeps the whole admissible family strictly positive, so `log μ` is defined on all
of it. -/
theorem h_lt_markovZ {q : ℝ} (hq : 0 < q) : heckeH q < markovZ q := by
  have hgap : 0 < markovZ q - heckeH q := by
    rw [markovZ_sub_heckeH hq]; positivity
  linarith

/-- **The admissible interface family lies in `(0, 1)`.** `d` runs over
`[-h, 0]`: `d = 0` is `σ`, `d = -h` is `σ⁻¹`. -/
theorem interface_mem_Ioo {q d : ℝ} (hq : 0 < q)
    (hlo : -heckeH q ≤ d) (hhi : d ≤ 0) (hz : q ^ 3 < q ^ 2 + 1) :
    0 < markovZ q + d ∧ markovZ q + d < 1 := by
  refine ⟨?_, ?_⟩
  · have := h_lt_markovZ hq
    linarith
  · have := markovZ_lt_one hq hz
    linarith

/-- **Every admissible single-crossing interface BINDS.** With `B = -α·log μ` and
`α > 0`, `μ < 1` gives `B > 0`. No choice of `d` avoids it. -/
theorem single_crossing_binds {q d α : ℝ} (hq : 0 < q) (hα : 0 < α)
    (hlo : -heckeH q ≤ d) (hhi : d ≤ 0) (hz : q ^ 3 < q ^ 2 + 1) :
    0 < -α * Real.log (markovZ q + d) := by
  obtain ⟨hpos, hlt⟩ := interface_mem_Ioo hq hlo hhi hz
  have hlog : Real.log (markovZ q + d) < 0 := Real.log_neg hpos hlt
  nlinarith

/-- **The writhe normalisation cannot rescue the sign.** It multiplies `μ` by
`(1-h)^(e/2)`, a factor in `(0,1)` when `0 < h < 1` and the exponent is positive;
a smaller `μ` binds *harder*. Stated on the factor directly so it applies to any
positive grading exponent. -/
theorem writhe_normalisation_binds_harder {μ c : ℝ}
    (hμ : 0 < μ) (hμ1 : μ < 1) (hc : 0 < c) (hc1 : c < 1) :
    0 < μ * c ∧ μ * c < 1 := by
  constructor
  · positivity
  · calc μ * c < μ * 1 := mul_lt_mul_of_pos_left hc1 hμ
      _ = μ := mul_one μ
      _ < 1 := hμ1

/-- **A non-negative writhe exponent can never unbind.** The writhe grading sends
`μ ↦ μ · (1-h)^(e/2)` with `0 < 1-h < 1`. For `e ≥ 0` that factor is `≤ 1`, so a
channel already in `(0,1)` stays there.

This is the general form of `writhe_normalisation_binds_harder`, stated on the
real exponent so it applies to a whole grading rather than one factor. -/
theorem nonneg_writhe_cannot_unbind {μ c e : ℝ}
    (hc0 : 0 ≤ c) (hc1 : c ≤ 1) (he : 0 ≤ e)
    (hμ0 : 0 < μ) (hμ1 : μ < 1) :
    μ * c ^ e < 1 := by
  have hpow_le : c ^ e ≤ 1 := Real.rpow_le_one hc0 hc1 he
  have hpow_nn : 0 ≤ c ^ e := Real.rpow_nonneg hc0 e
  calc μ * c ^ e ≤ μ * 1 := by
        exact mul_le_mul_of_nonneg_left hpow_le (le_of_lt hμ0)
    _ = μ := mul_one μ
    _ < 1 := hμ1

/-- **The `T₃` grading provably cannot unbind the `pp` channel.**

The corpus grades the strong-isospin interface by crossing sign — `σ` (positive
writhe) for `pp`, `σ⁻¹` (negative) for `nn` — i.e. by `T₃`
(`QOU.ParticleInteractions.WeakIsospinT3Grading`). A `T₃` grading therefore hands
`pp` a **non-negative** writhe exponent, and by `nonneg_writhe_cannot_unbind` any
non-negative exponent keeps the channel bound.

So the failure is not that the framework picked the wrong magnitude for `pp`: it
picked a sign that makes unbinding **impossible**, whatever the magnitude. Nature
has `a^N_pp = −17.3 fm` — unbound.

The `nn` side is not excluded by this (its `T₃` writhe is negative, the helpful
direction) — but it is quantitatively far off: unbinding `nn` needs `e ≤ −7.74`
at the substrate anchor against the `T₃` assignment's `e = −1`. -/
theorem t3_grading_cannot_unbind_pp {q e : ℝ} (hq : 0 < q)
    (hz : q ^ 3 < q ^ 2 + 1) (hh0 : 0 ≤ 1 - heckeH q) (hh1 : 1 - heckeH q ≤ 1)
    (hT3 : 0 ≤ e) :
    markovZ q * (1 - heckeH q) ^ e < 1 :=
  nonneg_writhe_cannot_unbind hh0 hh1 hT3 (markovZ_pos hq) (markovZ_lt_one hq hz)

/-- **Contrapositive: unbinding needs a large `q`.** If some admissible single
crossing fails to bind, then `q² + 1 ≤ q³` — i.e. `q` is at least the real root
of `q³ = q² + 1` (`≈ 1.46557`). The substrate anchor `q₀ ≈ 1.10998` is 24 % below
that, so this is not a near-miss. -/
theorem unbinding_needs_large_q {q d : ℝ} (hq : 0 < q)
    (hlo : -heckeH q ≤ d) (hhi : d ≤ 0) (hub : 1 ≤ markovZ q + d) :
    q ^ 2 + 1 ≤ q ^ 3 := by
  by_contra hcon
  push_neg at hcon
  obtain ⟨_, hlt⟩ := interface_mem_Ioo hq hlo hhi hcon
  linarith

/-! ### T-blind vs T-odd gradings

The two-nucleon sector needs the symmetric channel (`T = 1`) unbound and the
antisymmetric one (`T = 0`) bound. Whether a grading can *express* that at all is
decided by how it acts on the two channels' ratio. -/

/-- **A T-blind grading cannot discriminate the channels.** If both channels are
scaled by the same factor `c ≠ 0`, their ratio is unchanged — so no common
grading can change which channel is closer to the unbinding threshold.

This is the writhe: the normalisation `(1-h)^(e/2)` depends on the exponent sum,
which is a property of the *word*, not of the Wedderburn block, so both channels
receive it identically and it cancels here. -/
theorem common_factor_cancels_in_ratio {a b c : ℝ} (hc : c ≠ 0) (hb : b ≠ 0) :
    (a * c) / (b * c) = a / b := by
  field_simp

/-- **A reciprocal (T-odd) grading does move the ratio.** If the two channels
receive `t` and `t⁻¹`, the ratio is multiplied by `t²` — strictly monotone in `t`,
so the channels can be reordered.

This is the ribbon twist: `θ_λ = q^{c(λ)}` with `c(λ') = -c(λ)`
(`QOU.BraidKnot.KeystoneModularTwist`), so at `n = 2` the symmetric block gets
`q^{f}` and the antisymmetric block `q^{-f}`. -/
theorem reciprocal_factors_scale_ratio {a b t : ℝ} (ht : t ≠ 0) (hb : b ≠ 0) :
    (a * t) / (b * t⁻¹) = (a / b) * t ^ 2 := by
  field_simp

/-- **The consequence, as an ordering statement.** With `0 < b < a` (the corpus's
forced ordering `μ₋ < μ₊`), a common factor keeps the symmetric channel the
larger one; only a reciprocal grading can lift the ratio further. Stated as the
strict monotonicity that makes the threshold in the probe well-defined. -/
theorem reciprocal_ratio_strictMono {a b : ℝ} (ha : 0 < a) (hb : 0 < b)
    {t u : ℝ} (ht : 0 < t) (htu : t < u) :
    (a / b) * t ^ 2 < (a / b) * u ^ 2 := by
  have hab : 0 < a / b := div_pos ha hb
  have hsq : t ^ 2 < u ^ 2 := by nlinarith
  exact mul_lt_mul_of_pos_left hsq hab

/-- **Non-vacuity at the substrate anchor.** `q₀ ≈ 1.10998` satisfies the
hypothesis with room: `q³ ≈ 1.3676` against `q² + 1 ≈ 2.2321`. Stated on a
rational bracket so it is checkable by `norm_num`. -/
theorem substrate_satisfies_hypothesis :
    (111 / 100 : ℝ) ^ 3 < (111 / 100 : ℝ) ^ 2 + 1 := by norm_num

end QOU.QBeta
