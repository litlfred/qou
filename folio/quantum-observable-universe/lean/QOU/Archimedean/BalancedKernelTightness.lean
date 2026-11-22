/-
# Balanced q-Borel kernel tightness — the Markov leg, PROVED
# (REP attack 2: archimedean (REP) without fibre uniqueness)

The tightness leg of the balanced-kernel weak-convergence campaign
(`docs/audits/2026-08-01-rep-tightness-archimedean.md`, bean qou-ry7x):
the explicit positive kernels with exactly the balanced moments
(Attack B §3, `2026-07-25-qborel-confluence-pos-attack.md`) form a
q-indexed family whose SECOND moment `N^bal_q(3) = q^{−1/2}(1+q)` is
convergent (→ 2! = 2) as q → 1⁺, hence uniformly bounded — and a
uniformly bounded second moment gives uniform tail control by Markov's
inequality: the family is TIGHT in Mathlib's `IsTightMeasureSet` sense.

PROVED here (sorry-free — no new hypothesis is introduced by this leg):

* `tail_measureReal_le` — the Markov second-moment tail bound: a finite
  measure with `∫ s² ∂μ ≤ C` has `μ.real {s | R ≤ |s|} ≤ C/R²`
  (via Mathlib's `mul_meas_ge_le_integral_of_nonneg`).
* `measure_compl_closedBall_le` — the same bound in `ℝ≥0∞` against the
  complement of the compact window `[−R, R]`.
* `isTightMeasureSet_of_integral_sq_le` — a family of probability
  measures on `ℝ` with a single uniform second-moment bound is TIGHT
  (Mathlib `IsTightMeasureSet`, via
  `isTightMeasureSet_of_tendsto_measure_compl_closedBall`).
* `bddAbove_of_tendsto` (= `Filter.Tendsto.bddAbove_range`, composed) +
  `isTightMeasureSet_of_tendsto_integral_sq` — a CONVERGENT second-moment
  sequence is bounded, so a family whose second moments converge (the
  balanced family: `N^bal_{q_n}(3) → 2`, the k = 2 leg of the
  Lean-proved moment confluence) is tight. Tightness is *nearly free*:
  no tail estimate on the kernels themselves is ever needed.

CONDITIONAL composition (the named gap surface, STRICTLY SMALLER than
assuming Fréchet–Shohat wholesale as `BalancedKernelConfluence` does):

* class `ProkhorovSelectionReal` (Mathlib gap, content-bearing, NO
  instance) — Prokhorov/Helly selection: a tight sequence of probability
  measures on `ℝ` has a weakly convergent subsequence. The pinned
  Mathlib has the tightness *definitions* (`IsTightMeasureSet`,
  `TightNormed`) and Lévy–Prokhorov *metrizability*, but not the
  compactness theorem (survey re-confirmed on the pinned oleans;
  `2026-07-25-kernel-convergence-mathlib-gap.md`).
* class `MomentPassageStieltjes` (Mathlib gap, content-bearing, NO
  instance) — moments pass to weak limits when every moment converges
  (uniform integrability of `s^k` from the bounded `s^{2k}` moment;
  Billingsley 3rd ed., Thm. 25.12 + proof of Thm. 30.2).
* `subseq_limit_eq_schwinger` — EVERY subsequential weak limit of a
  family on `[0,∞)` whose moments converge to `{k!}` IS the unit
  Schwinger measure: moment passage identifies the limit's moments,
  and the merged determinacy pin
  (`BalancedKernelConfluence.eq_schwingerMeasure_of_factorial_moments`,
  conditional only on `[CarlemanDeterminacyStieltjes]` with its
  divergence hypothesis Lean-PROVED) forces the limit. No fibre
  uniqueness is used anywhere — the fibre problem is indeterminate at
  `q ≠ 1` (Attack B §3.1); determinacy enters only at the archimedean
  limit sequence `{k!}`.
* `exists_subseq_tendsto_schwinger` — the composed conditional: under
  the three classes, the balanced family (moments → `{k!}`) HAS a
  subsequence converging weakly to the Schwinger measure, and (by
  `subseq_limit_eq_schwinger`) every convergent subsequence has the
  same limit. Tightness — the only analytic input — is the PROVED leg.

NOT proved here (the honest residual):
* the three classical theorems themselves (the classes; no instance
  exists or may be fabricated — §Axiomatization is NOT a Proof);
* the (REP-1) identification of the substrate's OWN kernel with a
  member of the constructed family (a parallel tranche's target).

Base ring (§7c): wall-side `ℝ` throughout — tightness / weak
convergence of Borel measures on `ℝ` is archimedean content by
construction.

Probe: computations/probes/rep_tightness_probe.py (exact second-moment
identity `N^bal(3) = 2 + (√q−1)²/√q`, monotone uniform bound, Markov
tails of both explicit kernels, uniform tightness certificate; 60 dps).

-- Ref: [leitner2026] predicted-spectra, conj:schwinger-measure-computational-time;
--      docs/audits/2026-08-01-rep-tightness-archimedean.md;
--      docs/audits/2026-07-25-qborel-confluence-pos-attack.md §3-§4;
--      Prokhorov: Yu. V. Prokhorov, Theory Probab. Appl. 1 (1956) 157-214,
--      Thm 1.12; Billingsley, Convergence of Probability Measures, 2nd ed.,
--      Thm 5.1; moment passage: Billingsley, Probability and Measure, 3rd
--      ed., Thm 25.12 + Thm 30.2.
-/

import Mathlib.MeasureTheory.Measure.Tight
import Mathlib.MeasureTheory.Measure.TightNormed
import QOU.MathlibExt.FrechetShohat
import QOU.Archimedean.BalancedKernelConfluence

namespace QOU.Archimedean.BalancedKernelTightness

open MeasureTheory Filter Topology
open QOU.MathlibExt.FrechetShohat
open QOU.Archimedean.BalancedKernelConfluence

/-! ## The Markov second-moment tail bound (PROVED) -/

/-- **Markov tail bound from the second moment.** A finite Borel measure
on `ℝ` with second moment `∫ s² ∂μ ≤ C` puts mass at most `C/R²` outside
`(−R, R)`: `μ.real {s | R ≤ |s|} ≤ C/R²`. This is
`mul_meas_ge_le_integral_of_nonneg` applied to `f = s²` at level `R²`. -/
theorem tail_measureReal_le {μ : Measure ℝ} [IsFiniteMeasure μ]
    (hint : Integrable (fun s : ℝ => s ^ 2) μ)
    {C R : ℝ} (hC : ∫ s, s ^ 2 ∂μ ≤ C) (hR : 0 < R) :
    μ.real {s : ℝ | R ≤ |s|} ≤ C / R ^ 2 := by
  have hsub : {s : ℝ | R ≤ |s|} ⊆ {s : ℝ | R ^ 2 ≤ s ^ 2} := by
    intro s hs
    have h1 : R ≤ |s| := hs
    have h2 : R ^ 2 ≤ |s| ^ 2 := by nlinarith [hR.le, abs_nonneg s]
    simpa [sq_abs] using h2
  have hmarkov :
      R ^ 2 * μ.real {s : ℝ | R ^ 2 ≤ s ^ 2} ≤ ∫ s, s ^ 2 ∂μ :=
    mul_meas_ge_le_integral_of_nonneg
      (Filter.Eventually.of_forall fun s : ℝ => sq_nonneg s) hint (R ^ 2)
  have hmono : μ.real {s : ℝ | R ≤ |s|} ≤ μ.real {s : ℝ | R ^ 2 ≤ s ^ 2} :=
    measureReal_mono hsub (measure_ne_top μ _)
  have hR2 : (0 : ℝ) < R ^ 2 := by positivity
  rw [le_div_iff₀ hR2]
  calc μ.real {s : ℝ | R ≤ |s|} * R ^ 2
      ≤ μ.real {s : ℝ | R ^ 2 ≤ s ^ 2} * R ^ 2 :=
        mul_le_mul_of_nonneg_right hmono hR2.le
    _ = R ^ 2 * μ.real {s : ℝ | R ^ 2 ≤ s ^ 2} := mul_comm _ _
    _ ≤ ∫ s, s ^ 2 ∂μ := hmarkov
    _ ≤ C := hC

/-- The Markov tail bound in `ℝ≥0∞`, against the complement of the
compact window `[−R, R] = Metric.closedBall 0 R` — the shape consumed by
Mathlib's tightness API. -/
theorem measure_compl_closedBall_le {μ : Measure ℝ} [IsFiniteMeasure μ]
    (hint : Integrable (fun s : ℝ => s ^ 2) μ)
    {C R : ℝ} (hC : ∫ s, s ^ 2 ∂μ ≤ C) (hR : 0 < R) :
    μ (Metric.closedBall (0 : ℝ) R)ᶜ ≤ ENNReal.ofReal (C / R ^ 2) := by
  have hsub : (Metric.closedBall (0 : ℝ) R)ᶜ ⊆ {s : ℝ | R ≤ |s|} := by
    intro s hs
    simp only [Set.mem_compl_iff, Metric.mem_closedBall, Real.dist_eq,
      sub_zero, not_le] at hs
    exact hs.le
  calc μ (Metric.closedBall (0 : ℝ) R)ᶜ
      ≤ μ {s : ℝ | R ≤ |s|} := measure_mono hsub
    _ = ENNReal.ofReal (μ.real {s : ℝ | R ≤ |s|}) := by
        rw [measureReal_def, ENNReal.ofReal_toReal (measure_ne_top μ _)]
    _ ≤ ENNReal.ofReal (C / R ^ 2) :=
        ENNReal.ofReal_le_ofReal (tail_measureReal_le hint hC hR)

/-! ## Tightness from a uniform second-moment bound (PROVED) -/

/-- **Uniform second moment ⇒ tight.** A family of Borel probability
measures on `ℝ` with a single bound `∫ s² ∂(μs i) ≤ C` for every `i` is
tight: the compact windows `[−R, R]` catch mass `≥ 1 − C/R²` of every
member simultaneously (Markov), and `C/R² → 0`. -/
theorem isTightMeasureSet_of_integral_sq_le {ι : Type*}
    (μs : ι → Measure ℝ) [∀ i, IsProbabilityMeasure (μs i)]
    (hint : ∀ i, Integrable (fun s : ℝ => s ^ 2) (μs i))
    {C : ℝ} (hC : ∀ i, ∫ s, s ^ 2 ∂(μs i) ≤ C) :
    IsTightMeasureSet (Set.range μs) := by
  refine isTightMeasureSet_of_tendsto_measure_compl_closedBall
    (x := (0 : ℝ)) ?_
  have hupper : ∀ᶠ r : ℝ in atTop,
      (⨆ μ ∈ Set.range μs, μ (Metric.closedBall (0 : ℝ) r)ᶜ)
        ≤ ENNReal.ofReal (C / r ^ 2) := by
    filter_upwards [eventually_gt_atTop (0 : ℝ)] with r hr
    refine iSup₂_le ?_
    rintro μ ⟨i, rfl⟩
    exact measure_compl_closedBall_le (hint i) (hC i) hr
  have hzero :
      Tendsto (fun r : ℝ => ENNReal.ofReal (C / r ^ 2)) atTop (𝓝 0) := by
    have hdiv : Tendsto (fun r : ℝ => C / r ^ 2) atTop (𝓝 0) :=
      Tendsto.div_atTop tendsto_const_nhds
        (tendsto_pow_atTop (two_ne_zero))
    simpa using ENNReal.tendsto_ofReal hdiv
  exact tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hzero
    (Filter.Eventually.of_forall fun r => zero_le _) hupper

/-- A convergent real sequence is bounded above — the uniform-bound step
for a family whose second moments converge (Mathlib's
`Filter.Tendsto.bddAbove_range`, unpacked to an explicit bound). -/
theorem exists_forall_le_of_tendsto {f : ℕ → ℝ} {L : ℝ}
    (h : Tendsto f atTop (𝓝 L)) : ∃ C : ℝ, ∀ n, f n ≤ C := by
  obtain ⟨C, hC⟩ := h.bddAbove_range
  exact ⟨C, fun n => hC ⟨n, rfl⟩⟩

/-- **Convergent second moments ⇒ tight (the balanced-kernel form).**
A sequence of Borel probability measures on `ℝ` whose second moments
converge (for the balanced family: `∫ s² ∂K_n = N^bal_{q_n}(3) → 2! = 2`
— an exact identity, `N^bal(3) = 2 + (√q−1)²/√q`) is tight. Tightness of
the constructed family is thus *nearly free*: bounded second moment +
Markov, no kernel-specific tail estimate. -/
theorem isTightMeasureSet_of_tendsto_integral_sq
    (μs : ℕ → Measure ℝ) [∀ n, IsProbabilityMeasure (μs n)]
    (hint : ∀ n, Integrable (fun s : ℝ => s ^ 2) (μs n))
    {L : ℝ} (h : Tendsto (fun n => ∫ s, s ^ 2 ∂(μs n)) atTop (𝓝 L)) :
    IsTightMeasureSet (Set.range μs) := by
  obtain ⟨C, hC⟩ := exists_forall_le_of_tendsto h
  exact isTightMeasureSet_of_integral_sq_le μs hint hC

/-! ## The two remaining classical inputs — Mathlib-gap hypothesis
classes (§3b-tax; content-bearing; NO instance in this repo)

Both are TRUE classical theorems, carried as classes so every downstream
result stays sorry-free and wears its exact classical inputs in its type
(the `FrechetShohat.lean` discipline). Creating an `instance` requires
genuinely formalizing the classical proof (an upstream Mathlib
contribution); fabricating one to unlock physics would violate
§Axiomatization-is-NOT-a-Proof. Together with the PROVED tightness above
these two classes are strictly FINER than the monolithic
`FrechetShohatStieltjes` class: tightness (its analytic core) is now
discharged, and what remains is selection + moment passage. -/

/-- **Prokhorov/Helly selection (classical theorem, Mathlib gap).** A
tight sequence of Borel probability measures on `ℝ` has a subsequence
converging in the topology of weak convergence. Direct half of
Prokhorov's theorem (Prokhorov 1956, Thm 1.12; Billingsley, *Convergence
of Probability Measures*, 2nd ed., Thm 5.1). The pinned Mathlib carries
the tightness definitions (`IsTightMeasureSet`) and the Lévy–Prokhorov
metrizability of weak convergence, but not the compactness theorem.

TODO upstream: `Mathlib.MeasureTheory.Measure.Prokhorov` (new file). -/
class ProkhorovSelectionReal : Prop where
  exists_subseq_tendsto :
    ∀ μs : ℕ → ProbabilityMeasure ℝ,
      IsTightMeasureSet (Set.range fun n => (μs n : Measure ℝ)) →
      ∃ φ : ℕ → ℕ, StrictMono φ ∧ ∃ μ : ProbabilityMeasure ℝ,
        Tendsto (fun n => μs (φ n)) atTop (𝓝 μ)

/-- **Moment passage to weak limits (classical theorem, Mathlib gap).**
If probability measures on `[0,∞)`, with all moments finite and each
`k`-th moment converging to `M k`, converge weakly to `μ`, then `μ`
realizes the moment data `M`. Classical proof: for each `k` the bounded
`2k`-th moments give uniform integrability of `s ↦ s^k`, so the moment
functional passes to the weak limit (Billingsley, *Probability and
Measure*, 3rd ed., Thm 25.12, and the proof of Thm 30.2). This is the
"moments of the limit" half of Fréchet–Shohat, separated from selection.

TODO upstream: `Mathlib.Probability.MomentProblem` (new file). -/
class MomentPassageStieltjes : Prop where
  hasStieltjesMoments_limit :
    ∀ (μs : ℕ → ProbabilityMeasure ℝ) (μ : ProbabilityMeasure ℝ)
      (M : ℕ → ℝ),
      (∀ n, (μs n : Measure ℝ) (Set.Iio 0) = 0) →
      (∀ n k, Integrable (fun s : ℝ => s ^ k) (μs n : Measure ℝ)) →
      (∀ k : ℕ, Tendsto (fun n => ∫ s, s ^ k ∂(μs n : Measure ℝ)) atTop
        (𝓝 (M k))) →
      Tendsto μs atTop (𝓝 μ) →
      HasStieltjesMoments (μ : Measure ℝ) M

/-! ## The composed conditional — every subsequential limit is the
Schwinger measure (REP for the constructed family, no fibre uniqueness) -/

/-- **Subsequential-limit identification (conditional).** Let `μs` be
probability measures on `[0,∞)` with all moments finite and `k`-th
moments converging to `k!`. Then — conditional on moment passage and the
classical Carleman theorem (whose divergence hypothesis for `{k!}` is
Lean-PROVED, `carlemanCondition_factorial`) — every weakly convergent
subsequence of `μs` has limit exactly the unit Schwinger measure
`e^{−s}·ds`. Fibre-level uniqueness is never invoked: determinacy enters
only for the archimedean limit sequence `{k!}`. -/
theorem subseq_limit_eq_schwinger
    [MomentPassageStieltjes] [CarlemanDeterminacyStieltjes]
    {μs : ℕ → ProbabilityMeasure ℝ}
    (hsupp : ∀ n, (μs n : Measure ℝ) (Set.Iio 0) = 0)
    (hint : ∀ n k, Integrable (fun s : ℝ => s ^ k) (μs n : Measure ℝ))
    (hmom : ∀ k : ℕ, Tendsto (fun n => ∫ s, s ^ k ∂(μs n : Measure ℝ))
      atTop (𝓝 (k.factorial : ℝ)))
    {φ : ℕ → ℕ} (hφ : StrictMono φ) {ν : ProbabilityMeasure ℝ}
    (hν : Tendsto (fun n => μs (φ n)) atTop (𝓝 ν)) :
    ν = schwingerProbabilityMeasure := by
  have hmomφ : ∀ k : ℕ,
      Tendsto (fun n => ∫ s, s ^ k ∂(μs (φ n) : Measure ℝ)) atTop
        (𝓝 (k.factorial : ℝ)) :=
    fun k => (hmom k).comp hφ.tendsto_atTop
  have hν_mom : HasStieltjesMoments (ν : Measure ℝ)
      (fun k => (k.factorial : ℝ)) :=
    MomentPassageStieltjes.hasStieltjesMoments_limit
      (fun n => μs (φ n)) ν _ (fun n => hsupp (φ n))
      (fun n k => hint (φ n) k) hmomφ hν
  have hmeas : (ν : Measure ℝ) = schwingerMeasure :=
    eq_schwingerMeasure_of_factorial_moments (ν : Measure ℝ)
      inferInstance hν_mom
  exact ProbabilityMeasure.toMeasure_injective hmeas

/-- **The composed conditional theorem (REP attack 2, MAIN).** The
balanced kernel family — probability measures on `[0,∞)` with all
moments finite and moments converging to `{k!}` — is TIGHT (proved: the
`k = 2` moment convergence alone suffices, via Markov), hence under
Prokhorov selection a weakly convergent subsequence EXISTS, and under
moment passage + classical Carleman its limit — and the limit of every
other convergent subsequence (`subseq_limit_eq_schwinger`) — IS the unit
Schwinger measure. Archimedean (REP) holds for the constructed family
without any fibre-level uniqueness input. -/
theorem exists_subseq_tendsto_schwinger
    [ProkhorovSelectionReal] [MomentPassageStieltjes]
    [CarlemanDeterminacyStieltjes]
    (μs : ℕ → ProbabilityMeasure ℝ)
    (hsupp : ∀ n, (μs n : Measure ℝ) (Set.Iio 0) = 0)
    (hint : ∀ n k, Integrable (fun s : ℝ => s ^ k) (μs n : Measure ℝ))
    (hmom : ∀ k : ℕ, Tendsto (fun n => ∫ s, s ^ k ∂(μs n : Measure ℝ))
      atTop (𝓝 (k.factorial : ℝ))) :
    ∃ φ : ℕ → ℕ, StrictMono φ ∧
      Tendsto (fun n => μs (φ n)) atTop (𝓝 schwingerProbabilityMeasure) := by
  have htight :
      IsTightMeasureSet (Set.range fun n => (μs n : Measure ℝ)) :=
    isTightMeasureSet_of_tendsto_integral_sq _ (fun n => hint n 2) (hmom 2)
  obtain ⟨φ, hφ, ν, hν⟩ :=
    ProkhorovSelectionReal.exists_subseq_tendsto μs htight
  have hid : ν = schwingerProbabilityMeasure :=
    subseq_limit_eq_schwinger hsupp hint hmom hφ hν
  exact ⟨φ, hφ, hid ▸ hν⟩

end QOU.Archimedean.BalancedKernelTightness
