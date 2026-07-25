import Mathlib.MeasureTheory.Measure.ProbabilityMeasure
import Mathlib.MeasureTheory.Measure.FiniteMeasureExt
import Mathlib.MeasureTheory.Integral.ExpDecay
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.Tactic

/-!
# QOU.MathlibExt.FrechetShohat

Moment-problem infrastructure for the balanced q-Borel kernel-convergence
theorem (`docs/audits/2026-07-25-kernel-convergence-mathlib-gap.md`): the
Stieltjes-moment predicate, moment-sequence determinacy, the Carleman
condition, the unit Schwinger measure `e^{−s}·ds` with its factorial
moments (PROVED), uniqueness of weak limits of probability measures
(PROVED), and the two classical theorems Mathlib does not yet have —
**Fréchet–Shohat** (moment convergence + determinate limit ⇒ weak
convergence) and **Carleman–Stieltjes determinacy** — stated as
content-bearing hypothesis classes (Mathlib-gap markers, §3b-tax; NO
instance in this repo: an instance requires the genuine formalization,
which would itself be an upstream Mathlib contribution).

## Mathlib-gap map (survey 2026-07-25, pin `leanprover/lean4:v4.24.0`)

EXISTS upstream (imported and used here):
- weak-convergence topology on `MeasureTheory.ProbabilityMeasure` +
  `ProbabilityMeasure.tendsto_iff_forall_integral_tendsto`
  (`Mathlib.MeasureTheory.Measure.ProbabilityMeasure`); portmanteau
  characterizations (`…Measure.Portmanteau`); Lévy–Prokhorov
  metrizability (`…Measure.LevyProkhorovMetric`); tightness API
  (`…Measure.Tight`, `TightNormed`);
- separation of finite measures by bounded continuous test functions:
  `MeasureTheory.ext_of_forall_integral_eq_of_IsFiniteMeasure`
  (`Mathlib.MeasureTheory.Measure.FiniteMeasureExt`); characteristic-
  function determinacy `ext_of_charFun`; complex-MGF determinacy
  `ProbabilityTheory.ext_of_complexMGF_eq`;
- moments/mgf: `ProbabilityTheory.moment`, `mgf`,
  `iteratedDeriv_mgf_zero` (`Mathlib.Probability.Moments.*`);
- the Gamma integral: `Real.Gamma_eq_integral`,
  `Real.Gamma_nat_eq_factorial`.

MISSING upstream (the gap this module scaffolds around):
- the Hamburger/Stieltjes moment problem as such (determinacy from
  moment-growth conditions);
- **Carleman's determinacy criterion** (`Σ M_k^{−1/(2k)} = ∞ ⇒`
  determinate) — class `CarlemanDeterminacyStieltjes` below;
- **Fréchet–Shohat / method of moments** — class
  `FrechetShohatStieltjes` below;
- Prokhorov's compactness theorem (tight ⇒ relatively compact) did not
  surface in the pinned olean survey; only the tightness *definitions*
  are present.

The mgf-route determinacy that Mathlib DOES have
(`ext_of_complexMGF_eq`) requires exponential integrability in a
neighbourhood of `0` — strictly stronger than Carleman, and NOT
satisfied uniformly by the q-Borel fibre kernels (the fibre problem is
indeterminate, log-normal/Krein regime; see the audit §3.1), so it
cannot replace the Carleman/Fréchet–Shohat package for the q→1 limit
statement.

References (classical): M. Fréchet, J. Shohat, *A proof of the
generalized second-limit theorem in the theory of probability*, Trans.
AMS 33 (1931) 533–543; P. Billingsley, *Probability and Measure*, 3rd
ed., Wiley 1995, Theorem 30.2; B. Simon, *The classical moment problem
as a self-adjoint finite difference operator*, Adv. Math. 137 (1998)
82–203 (Carleman, Stieltjes case). q→1 confluence literature route:
Di Vizio–Zhang, Ann. Inst. Fourier 59 (2009) 347–392
(`divizio-zhang2009`).

TODO upstream: `Mathlib.Probability.MomentProblem` (new file) — the
predicates and both classical theorems; the Schwinger-measure moment
lemmas belong beside `Mathlib.Probability.Distributions.Exponential`
(`schwingerMeasure` here coincides with `ProbabilityTheory.expMeasure 1`).
-/

namespace QOU.MathlibExt.FrechetShohat

open MeasureTheory Filter Topology
open scoped NNReal ENNReal

/-! ## The moment-problem predicates (definitions — no gap content) -/

/-- `HasStieltjesMoments μ M`: the measure `μ` on `ℝ` is supported on
`[0,∞)` (no mass on `Iio 0`), every monomial `s^k` is integrable, and the
`k`-th moment is `M k`. This is the Stieltjes-side moment-data predicate
of the classical moment problem. -/
def HasStieltjesMoments (μ : Measure ℝ) (M : ℕ → ℝ) : Prop :=
  μ (Set.Iio 0) = 0 ∧
    ∀ k : ℕ, Integrable (fun s : ℝ => s ^ k) μ ∧ ∫ s, s ^ k ∂μ = M k

/-- `StieltjesDeterminate M`: at most one probability measure on `ℝ`
supported on `[0,∞)` has moment sequence `M` — the *determinacy*
property of the Stieltjes moment problem. -/
def StieltjesDeterminate (M : ℕ → ℝ) : Prop :=
  ∀ μ ν : Measure ℝ, IsProbabilityMeasure μ → IsProbabilityMeasure ν →
    HasStieltjesMoments μ M → HasStieltjesMoments ν M → μ = ν

/-- `CarlemanCondition M`: the Carleman series `Σ_k M_k^{−1/(2k)}`
diverges (stated as non-summability, matching
`QOU.Archimedean.BorelProperTimeMoment.carleman_divergence`, which
proves exactly this for `M k = k!`). The `k = 0` term is the harmless
constant `M 0 ^ 0 = 1` under Lean's `1/0 = 0` convention. -/
def CarlemanCondition (M : ℕ → ℝ) : Prop :=
  ¬ Summable (fun k : ℕ => (M k) ^ (-(1 / (2 * (k : ℝ)))))

/-! ## The unit Schwinger measure and its factorial moments (PROVED) -/

/-- The unit Schwinger (proper-time) measure `e^{−s}·ds` on `(0,∞)`,
as a Borel measure on `ℝ`. Coincides with the rate-1 exponential
distribution `ProbabilityTheory.expMeasure 1`. -/
noncomputable def schwingerMeasure : Measure ℝ :=
  (volume.restrict (Set.Ioi 0)).withDensity fun s => ENNReal.ofReal (Real.exp (-s))

private lemma schwinger_density_eq :
    (fun s : ℝ => ENNReal.ofReal (Real.exp (-s)))
      = fun s : ℝ => ((Real.exp (-s)).toNNReal : ℝ≥0∞) := rfl

private lemma schwinger_density_measurable :
    Measurable fun s : ℝ => (Real.exp (-s)).toNNReal :=
  (Real.measurable_exp.comp measurable_neg).real_toNNReal

/-- The Schwinger measure carries no mass left of the origin. -/
theorem schwingerMeasure_Iio_zero : schwingerMeasure (Set.Iio 0) = 0 := by
  rw [schwingerMeasure, withDensity_apply _ measurableSet_Iio,
    Measure.restrict_restrict measurableSet_Iio, Set.Iio_inter_Ioi,
    Set.Ioo_self, Measure.restrict_empty, lintegral_zero_measure]

/-- Total mass one: `∫₀^∞ e^{−s} ds = Γ(1) = 1`. -/
theorem schwingerMeasure_univ : schwingerMeasure Set.univ = 1 := by
  have hint : IntegrableOn (fun s : ℝ => Real.exp (-s)) (Set.Ioi 0) := by
    simpa using exp_neg_integrableOn_Ioi 0 one_pos
  have hI : ∫ s in Set.Ioi (0 : ℝ), Real.exp (-s) = 1 := by
    have h := Real.Gamma_eq_integral (by norm_num : (0 : ℝ) < 1)
    rw [Real.Gamma_one] at h
    simpa using h.symm
  rw [schwingerMeasure, withDensity_apply _ MeasurableSet.univ,
    Measure.restrict_univ,
    ← ofReal_integral_eq_lintegral_ofReal hint
      (Filter.Eventually.of_forall fun s => Real.exp_nonneg _)]
  rw [hI, ENNReal.ofReal_one]

instance : IsProbabilityMeasure schwingerMeasure := ⟨schwingerMeasure_univ⟩

/-- The Schwinger measure as a bundled probability measure on `ℝ` —
the weak-convergence limit object of the balanced q-Borel kernel
family. -/
noncomputable def schwingerProbabilityMeasure : ProbabilityMeasure ℝ :=
  ⟨schwingerMeasure, inferInstance⟩

/-- Every monomial is integrable against the Schwinger measure
(the Gamma integral converges). -/
theorem integrable_pow_schwingerMeasure (k : ℕ) :
    Integrable (fun s : ℝ => s ^ k) schwingerMeasure := by
  rw [schwingerMeasure, schwinger_density_eq,
    integrable_withDensity_iff_integrable_smul schwinger_density_measurable]
  have h0 : (fun s : ℝ => ((Real.exp (-s)).toNNReal : ℝ≥0) • s ^ k)
      = fun s : ℝ => Real.exp (-s) * s ^ (((k : ℝ) + 1) - 1) := by
    funext s
    rw [NNReal.smul_def, Real.coe_toNNReal _ (Real.exp_nonneg _), smul_eq_mul,
      show ((k : ℝ) + 1) - 1 = ((k : ℕ) : ℝ) by ring,
      Real.rpow_natCast]
  rw [h0]
  exact Real.GammaIntegral_convergent (by positivity)

/-- **The factorial moments (proved).** The `k`-th moment of the unit
Schwinger measure is `k!`: `∫ s^k · e^{−s} ds = Γ(k+1) = k!`. Together
with `QOU.Archimedean.BorelProperTimeMoment.moment_eq_factorial` (the
`ds/s`-shifted form) this is the moment-data leg of the balanced-kernel
convergence theorem. -/
theorem integral_pow_schwingerMeasure (k : ℕ) :
    ∫ s, s ^ k ∂schwingerMeasure = (k.factorial : ℝ) := by
  rw [schwingerMeasure, schwinger_density_eq,
    integral_withDensity_eq_integral_smul schwinger_density_measurable]
  have hcong : (fun s : ℝ => ((Real.exp (-s)).toNNReal : ℝ≥0) • s ^ k)
      = fun s : ℝ => Real.exp (-s) * s ^ (((k : ℝ) + 1) - 1) := by
    funext s
    rw [NNReal.smul_def, Real.coe_toNNReal _ (Real.exp_nonneg _), smul_eq_mul,
      show ((k : ℝ) + 1) - 1 = ((k : ℕ) : ℝ) by ring,
      Real.rpow_natCast]
  rw [hcong, ← Real.Gamma_eq_integral (by positivity : (0 : ℝ) < (k : ℝ) + 1)]
  exact_mod_cast Real.Gamma_nat_eq_factorial k

/-- The Schwinger measure realizes the factorial Stieltjes moment data —
the `HasStieltjesMoments` package, fully proved. -/
theorem hasStieltjesMoments_schwinger :
    HasStieltjesMoments schwingerMeasure fun k => (k.factorial : ℝ) :=
  ⟨schwingerMeasure_Iio_zero, fun k =>
    ⟨integrable_pow_schwingerMeasure k, integral_pow_schwingerMeasure k⟩⟩

/-! ## Uniqueness of weak limits (PROVED — the determinate-limit
uniqueness step of Fréchet–Shohat that existing Mathlib does supply) -/

/-- **Weak limits of probability measures on `ℝ` are unique.** Two weak
limits of the same net integrate every bounded continuous function
identically (`tendsto_nhds_unique` in `ℝ`), hence coincide by
`ext_of_forall_integral_eq_of_IsFiniteMeasure`. This is the uniqueness
half of the Fréchet–Shohat conclusion; only the *existence/convergence*
half remains a Mathlib gap.

TODO upstream: `Mathlib.MeasureTheory.Measure.ProbabilityMeasure` — a
`T2Space (ProbabilityMeasure ℝ)` instance would subsume this. -/
theorem tendsto_probabilityMeasure_unique {ι : Type*} {L : Filter ι} [L.NeBot]
    {μs : ι → ProbabilityMeasure ℝ} {μ ν : ProbabilityMeasure ℝ}
    (hμ : Tendsto μs L (𝓝 μ)) (hν : Tendsto μs L (𝓝 ν)) : μ = ν := by
  apply ProbabilityMeasure.toMeasure_injective
  apply ext_of_forall_integral_eq_of_IsFiniteMeasure
  intro f
  exact tendsto_nhds_unique
    (ProbabilityMeasure.tendsto_iff_forall_integral_tendsto.mp hμ f)
    (ProbabilityMeasure.tendsto_iff_forall_integral_tendsto.mp hν f)

/-! ## The two classical theorems — Mathlib-gap hypothesis classes
(§3b-tax; content-bearing; NO instance in this repo)

Both statements below are TRUE classical theorems, not conjectures. They
are carried as hypothesis classes rather than `sorry`-bearing theorems so
that every downstream QOU result stays sorry-free and wears its exact
classical inputs in its type (§3b-cond discipline). Creating an
`instance` requires actually formalizing the classical proof — a genuine
upstream Mathlib contribution, welcomed but out of scope this tranche.
Deriving physics conclusions by fabricating an instance would violate
§Axiomatization-is-NOT-a-Proof. -/

/-- **Carleman–Stieltjes determinacy (classical theorem, Mathlib gap).**
If the moment sequence `M` (of genuine Stieltjes moment data, positive)
satisfies the Carleman condition `Σ_k M_k^{−1/(2k)} = ∞`, the Stieltjes
moment problem for `M` is determinate. Simon, Adv. Math. 137 (1998)
82–203, Cor. 4.5 / Thm. 5.14; Akhiezer, *The Classical Moment Problem*,
1965. `QOU.Archimedean.BorelProperTimeMoment.carleman_divergence` proves
the hypothesis for `M k = k!`; this class carries the theorem itself.

TODO upstream: `Mathlib.Probability.MomentProblem` (new file). -/
class CarlemanDeterminacyStieltjes : Prop where
  determinate : ∀ M : ℕ → ℝ, (∀ k, 0 < M k) →
    CarlemanCondition M → StieltjesDeterminate M

/-- **Fréchet–Shohat / method of moments (classical theorem, Mathlib
gap), Stieltjes form with an explicit limit candidate.** If probability
measures `μs n`, all supported on `[0,∞)` with all moments finite, have
`k`-th moments converging to `M k` for every `k`, and `μ` realizes the
moment data `M`, and `M` is Stieltjes-determinate, then `μs → μ` in the
topology of weak convergence. Fréchet–Shohat, Trans. AMS 33 (1931)
533–543; Billingsley, *Probability and Measure*, 3rd ed., Thm. 30.2.
The uniqueness half is already provable
(`tendsto_probabilityMeasure_unique`); the convergence half needs
tightness-from-moments + Prokhorov/Helly selection, absent from the
pinned Mathlib.

TODO upstream: `Mathlib.Probability.MomentProblem` (new file). -/
class FrechetShohatStieltjes : Prop where
  tendsto_of_moments :
    ∀ (μs : ℕ → ProbabilityMeasure ℝ) (μ : ProbabilityMeasure ℝ) (M : ℕ → ℝ),
      (∀ k : ℕ, Tendsto (fun n => ∫ s, s ^ k ∂(μs n : Measure ℝ)) atTop
        (𝓝 (M k))) →
      (∀ n, (μs n : Measure ℝ) (Set.Iio 0) = 0) →
      (∀ n k, Integrable (fun s : ℝ => s ^ k) (μs n : Measure ℝ)) →
      HasStieltjesMoments (μ : Measure ℝ) M →
      StieltjesDeterminate M →
      Tendsto μs atTop (𝓝 μ)

end QOU.MathlibExt.FrechetShohat
