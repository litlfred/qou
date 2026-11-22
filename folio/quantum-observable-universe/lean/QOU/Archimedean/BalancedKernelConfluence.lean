/-
# Balanced q-Borel kernel confluence — the conditional weak-convergence
# theorem (the named analytic gap of the merged conjecture campaign)

The rigorous kernel-convergence statement demanded by
`docs/audits/2026-07-25-qborel-confluence-pos-attack.md` §4 gap 1: from

(i)   per-`n` moment convergence of the balanced q-Borel kernel to
      `(n−1)!` as `q → 1⁺` — proved EXACT (sympy, every order tested;
      `h¹ ≡ 0`, `h²` = the Attack-E target) in the merged probe, taken
      HERE as an explicit hypothesis (`hmom`); its qualitative Lean
      formalization has since landed as
      `BalancedMomentConfluence.tendsto_balancedNormalizerR`, and the
      corollary `balanced_kernel_tendsto_schwinger_of_confluence` there
      discharges `hmom` down to balanced-moment representability;
(ii)  the Fréchet–Shohat method-of-moments theorem — a Mathlib gap,
      carried as the hypothesis class
      `QOU.MathlibExt.FrechetShohat.FrechetShohatStieltjes`;
(iii) Carleman determinacy of `{k!}` — the divergence hypothesis is
      Lean-PROVED (`BorelProperTimeMoment.carleman_divergence`, merged);
      the classical Carleman ⇒ determinate step is a Mathlib gap,
      carried as the class `CarlemanDeterminacyStieltjes`;

it follows that the balanced kernel family converges weakly to the unit
Schwinger measure `e^{−s}·ds`.

PROVED here (sorry-free):

* `carlemanCondition_factorial` — the general `CarlemanCondition`
  predicate instantiated at `M k = k!`, definitionally the merged
  divergence proof (compose-don't-restate).
* `stieltjesDeterminate_factorial` — CONDITIONAL on
  `[CarlemanDeterminacyStieltjes]`: the factorial Stieltjes problem is
  determinate. The only unproved input is the classical Carleman
  theorem; its hypothesis is the Lean-proved divergence.
* `eq_schwingerMeasure_of_factorial_moments` — CONDITIONAL determinacy
  pin: any probability measure on `[0,∞)` with factorial moments IS the
  Schwinger measure. This is the Attack-A "positive + right moments ⇒
  the kernel is `e^{−s}ds`" forcing, now type-carried.
* `balanced_kernel_tendsto_schwinger` — the MAIN conditional theorem:
  under both classes, any sequence of probability measures on `[0,∞)`
  whose `k`-th moments converge to `k!` converges weakly to the
  Schwinger measure. (POS) survives the limit for free — the limit is a
  `ProbabilityMeasure`.
* `bindingKernel_measure_eq_schwinger` — the bridge to the merged
  `BindingKernelSchwingerRepresentation` reduction class: a kernel
  satisfying that class's (open) hypotheses, packaged as a measure with
  the factorial moment data, is FORCED (conditionally on
  `[CarlemanDeterminacyStieltjes]`) to be the Schwinger measure.

NOT proved here (the honest residual, unchanged in kind):
* the two classical theorems themselves (Mathlib gaps — the classes;
  no instance exists or may be fabricated, §Axiomatization is NOT a
  Proof);
* the Lean formalization of the per-`n` balanced moment confluence
  (audit §2; entered as hypothesis `hmom`) — DISCHARGED qualitatively in
  `QOU.Archimedean.BalancedMomentConfluence` (`tendsto_balancedNormalizerR`
  + the `…_of_confluence` corollary): what remains on this leg is the
  (REP) representability hypothesis, not moment convergence;
* the conjecture's own (POS)/(REP) content — that the SUBSTRATE's
  resummation kernel satisfies the moment/positivity hypotheses (audit
  §4 gap 2; at `q ≠ 1` the fibre problem is indeterminate, §3.1, so
  this needs derivation input beyond moments).

Base ring (§7c): wall-side `ℝ` throughout — weak convergence of Borel
measures on `ℝ` is archimedean content by construction.

Literature: the q→1 confluence route outside RSZ is Di Vizio–Zhang
(`divizio-zhang2009`), Ann. Inst. Fourier 59 (2009) 347–392; classical
legs: Fréchet–Shohat (Trans. AMS 33, 1931), Simon (Adv. Math. 137,
1998), Billingsley (3rd ed., Thm. 30.2).

-- Ref: [leitner2026] predicted-spectra, conj:schwinger-measure-computational-time;
--      docs/audits/2026-07-25-qborel-confluence-pos-attack.md §4;
--      docs/audits/2026-07-25-kernel-convergence-mathlib-gap.md;
--      [divizio-zhang2009] q-summation and confluence.
-/

import QOU.MathlibExt.FrechetShohat
import QOU.Archimedean.BorelProperTimeMoment

namespace QOU.Archimedean.BalancedKernelConfluence

open MeasureTheory Filter Topology
open QOU.MathlibExt.FrechetShohat

/-- **Carleman's condition holds for `{k!}`** — the general predicate of
the moment-problem infrastructure, discharged by the merged Attack-A
divergence proof (`BorelProperTimeMoment.carleman_divergence`). Nothing
is re-derived: the instantiation is definitional. -/
theorem carlemanCondition_factorial :
    CarlemanCondition fun k => (k.factorial : ℝ) :=
  QOU.Archimedean.BorelProperTimeMoment.carleman_divergence

/-- **Factorial-moment determinacy, conditional on classical Carleman.**
The Stieltjes moment problem for `{k!}` is determinate. The ONLY
unformalized input is the classical Carleman–Stieltjes theorem (the
`[CarlemanDeterminacyStieltjes]` hypothesis class, a Mathlib gap); its
divergence hypothesis is Lean-proved. -/
theorem stieltjesDeterminate_factorial [CarlemanDeterminacyStieltjes] :
    StieltjesDeterminate fun k => (k.factorial : ℝ) :=
  CarlemanDeterminacyStieltjes.determinate _
    (fun k => by exact_mod_cast k.factorial_pos)
    carlemanCondition_factorial

/-- **The determinacy pin (Attack A forcing, type-carried).** Any
probability measure on `ℝ` supported on `[0,∞)` whose moments are the
keystone-forced factorials IS the unit Schwinger measure — conditional
only on the classical Carleman theorem. -/
theorem eq_schwingerMeasure_of_factorial_moments [CarlemanDeterminacyStieltjes]
    (μ : Measure ℝ) (hprob : IsProbabilityMeasure μ)
    (hm : HasStieltjesMoments μ fun k => (k.factorial : ℝ)) :
    μ = schwingerMeasure :=
  stieltjesDeterminate_factorial μ schwingerMeasure hprob inferInstance hm
    hasStieltjesMoments_schwinger

/-- **The balanced-kernel weak-convergence theorem (MAIN, conditional).**
Let `K n` be the balanced q-Borel kernels along any sequence
`q_n → 1⁺` — probability measures on `[0,∞)` with all moments finite —
and suppose the `k`-th moments converge to `k!` (the audit-§2 balanced
moment confluence, exact at every order in the merged probe, here an
explicit hypothesis pending its own Lean tranche). Then, conditional on
the two classical Mathlib-gap theorems (Fréchet–Shohat + Carleman
determinacy), the kernels converge WEAKLY to the unit Schwinger measure
`e^{−s}·ds`. Positivity of the limit — the archimedean (POS) — is free:
the limit object is a `ProbabilityMeasure`. -/
theorem balanced_kernel_tendsto_schwinger
    [FrechetShohatStieltjes] [CarlemanDeterminacyStieltjes]
    (K : ℕ → ProbabilityMeasure ℝ)
    (hsupp : ∀ n, (K n : Measure ℝ) (Set.Iio 0) = 0)
    (hint : ∀ n k, Integrable (fun s : ℝ => s ^ k) (K n : Measure ℝ))
    (hmom : ∀ k : ℕ, Tendsto (fun n => ∫ s, s ^ k ∂(K n : Measure ℝ))
      atTop (𝓝 (k.factorial : ℝ))) :
    Tendsto K atTop (𝓝 schwingerProbabilityMeasure) :=
  FrechetShohatStieltjes.tendsto_of_moments K schwingerProbabilityMeasure
    (fun k => (k.factorial : ℝ)) hmom hsupp hint
    hasStieltjesMoments_schwinger stieltjesDeterminate_factorial

/-- **Bridge to the merged reduction class.** A binding kernel `Kb`
satisfying the (open) hypotheses of
`BorelProperTimeMoment.BindingKernelSchwingerRepresentation` — positivity
and the keystone-forced factorial `ds/s`-moments — determines, once
packaged as a probability measure with the corresponding Stieltjes
moment data, the unit Schwinger measure: the two open conjecture
hypotheses plus the classical Carleman theorem pin the kernel measure
uniquely. This closes the loop `moments → measure` that the merged
`kernel_moments_eq_schwinger` (moment-level indistinguishability) left
at the moment level. -/
theorem bindingKernel_measure_eq_schwinger [CarlemanDeterminacyStieltjes]
    (Kb : ℝ → ℝ)
    [QOU.Archimedean.BorelProperTimeMoment.BindingKernelSchwingerRepresentation Kb]
    (μKb : Measure ℝ) (hprob : IsProbabilityMeasure μKb)
    (hsupp : μKb (Set.Iio 0) = 0)
    (hintKb : ∀ k : ℕ, Integrable (fun s : ℝ => s ^ k) μKb)
    (hrealize : ∀ k : ℕ, ∫ s, s ^ k ∂μKb
      = ∫ s in Set.Ioi (0 : ℝ), s ^ (k + 1) * Kb s / s) :
    μKb = schwingerMeasure := by
  apply eq_schwingerMeasure_of_factorial_moments μKb hprob
  refine ⟨hsupp, fun k => ⟨hintKb k, ?_⟩⟩
  rw [hrealize k,
    QOU.Archimedean.BorelProperTimeMoment.BindingKernelSchwingerRepresentation.moments
      (Kb := Kb) k]

end QOU.Archimedean.BalancedKernelConfluence
