# Balanced-kernel weak convergence — the Mathlib-gap map + conditional theorem scaffold

**Date:** 2026-07-25 · **Bean:** qou-5rxw · **PR:** #4250 (tranche home)
**Tier:** AUDIT + Lean scaffold — scope-(a), NO FIT, nothing wired; the
target conjecture stays a conjecture. No content block touched.

**Target.** The named analytic gap of the merged conjecture campaign
([`2026-07-25-qborel-confluence-pos-attack.md` §4 gap 1](2026-07-25-qborel-confluence-pos-attack.md)):
the rigorous kernel-convergence theorem

$$
K_q \;\Rightarrow\; e^{-s}\,ds \qquad (q \to 1^+,\ \text{weak convergence}),
$$

assembled from (i) per-$n$ moment convergence of the balanced q-Borel
kernel to $(n-1)!$ (proved exact, sympy, in the merged probe), (ii) the
Fréchet–Shohat method-of-moments theorem, (iii) Carleman determinacy of
$\{k!\}$ (whose divergence hypothesis is already Lean-proved in
[`BorelProperTimeMoment.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorelProperTimeMoment.lean)).

## 1. Mathlib-gap map (survey against the pinned toolchain `leanprover/lean4:v4.24.0`)

Survey method: the sandbox carries restored Mathlib *oleans* only (no
source tree), so the map was built from the olean module inventory +
declaration-name string extraction, not `grep` over source. The
`lean`-direct compiles below are the positive confirmation that every
"EXISTS" row actually resolves.

| Ingredient | Status | Where (Mathlib module / declaration) |
|---|---|---|
| Weak-convergence topology on probability measures | **EXISTS** | `Mathlib.MeasureTheory.Measure.ProbabilityMeasure` — `ProbabilityMeasure.tendsto_iff_forall_integral_tendsto` |
| Portmanteau characterizations | **EXISTS** | `Mathlib.MeasureTheory.Measure.Portmanteau` (`tendsto_iff_forall_integral_tendsto`, open/closed liminf-limsup forms) |
| Lévy–Prokhorov metrizability | **EXISTS** | `Mathlib.MeasureTheory.Measure.LevyProkhorovMetric` (`levyProkhorovDist_metricSpace_probabilityMeasure`) |
| Tightness (definitions + normed-space criteria) | **EXISTS** | `Mathlib.MeasureTheory.Measure.Tight`, `TightNormed` (`IsTightMeasureSet` + `iff` lemmas) |
| Prokhorov compactness (tight ⇒ relatively compact) | **MISSING** (not surfaced in the pinned olean survey; only the tightness *definitions* are present) | — |
| Separation of finite measures by bounded continuous functions | **EXISTS** | `Mathlib.MeasureTheory.Measure.FiniteMeasureExt` — `ext_of_forall_integral_eq_of_IsFiniteMeasure` |
| Characteristic-function determinacy | **EXISTS** | `Mathlib.MeasureTheory.Measure.CharacteristicFunction` — `ext_of_charFun` |
| MGF-route determinacy | **EXISTS** | `Mathlib.Probability.Moments.ComplexMGF` — `ext_of_complexMGF_eq` (needs exponential integrability near $0$ — strictly stronger than Carleman; unusable at the fibre, §3.1 indeterminacy) |
| Moments / mgf API | **EXISTS** | `Mathlib.Probability.Moments.Basic`, `MGFAnalytic` (`moment`, `centralMoment`, `mgf`, `iteratedDeriv_mgf_zero`) |
| Gamma integral (factorial moments) | **EXISTS** | `Mathlib.Analysis.SpecialFunctions.Gamma.Basic` (`Real.Gamma_eq_integral`, `Real.Gamma_nat_eq_factorial`, `Real.GammaIntegral_convergent`) |
| Exponential distribution | **EXISTS** (but no moment lemmas) | `Mathlib.Probability.Distributions.Exponential` (`ProbabilityTheory.expMeasure`) |
| Hamburger/Stieltjes moment problem (any determinacy-from-growth) | **MISSING** | — |
| **Carleman determinacy criterion** | **MISSING** | scaffolded here as class `CarlemanDeterminacyStieltjes` |
| **Fréchet–Shohat / method of moments** | **MISSING** | scaffolded here as class `FrechetShohatStieltjes` |

## 2. What landed (2 new files, both `lean`-direct exit 0, sorry-free)

### [`QOU/MathlibExt/FrechetShohat.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/FrechetShohat.lean) — the Mathlib-gap infra (imports Mathlib only, QOU-free signatures)

**PROVED (7 declarations, sorry-free):**

- `schwingerMeasure` — the unit Schwinger measure $e^{-s}\,ds$ on
  $(0,\infty)$ as a Borel measure on $\mathbb{R}$ (`withDensity` over
  `volume.restrict (Ioi 0)`; coincides with
  `ProbabilityTheory.expMeasure 1`).
- `schwingerMeasure_Iio_zero` — no mass on $(-\infty,0)$.
- `schwingerMeasure_univ` + `IsProbabilityMeasure` instance +
  `schwingerProbabilityMeasure` — total mass $\Gamma(1) = 1$.
- `integrable_pow_schwingerMeasure` — every monomial integrable (Gamma
  integral converges).
- `integral_pow_schwingerMeasure` — the factorial moments
  $\int s^k e^{-s}\,ds = \Gamma(k+1) = k!$ (the moment-data leg, proved).
- `hasStieltjesMoments_schwinger` — the full `HasStieltjesMoments`
  package for $M_k = k!$.
- `tendsto_probabilityMeasure_unique` — **uniqueness of weak limits** of
  probability measures on $\mathbb{R}$ (via
  `ext_of_forall_integral_eq_of_IsFiniteMeasure` + `tendsto_nhds_unique`)
  — the uniqueness half of Fréchet–Shohat, provable from existing
  Mathlib.

**Definitions (no gap content):** `HasStieltjesMoments`,
`StieltjesDeterminate`, `CarlemanCondition` (stated to match
`carleman_divergence` definitionally).

**SCAFFOLDED — the two classical theorems as content-bearing hypothesis
classes (§3b-tax; NO instance; 0 sorries):**

- `CarlemanDeterminacyStieltjes` — Carleman condition ⇒ Stieltjes
  determinacy (Simon 1998, Cor. 4.5/Thm. 5.14; Akhiezer 1965).
- `FrechetShohatStieltjes` — moment convergence + determinate limit
  data ⇒ weak convergence (Fréchet–Shohat 1931; Billingsley 3rd ed.,
  Thm. 30.2), stated with an explicit limit candidate (avoiding the
  Helly/Prokhorov existence leg in the statement).

Both are TRUE classical theorems, not conjectures — carried as classes
rather than `sorry`+`-- Ref:` so every downstream QOU result stays
sorry-free and wears its exact classical inputs in its type (parent
directive, §3b-cond style). Creating an instance requires the genuine
formalization (an upstream Mathlib contribution); fabricating one would
violate §Axiomatization-is-NOT-a-Proof. Both carry `TODO upstream:`
tags (`Mathlib.Probability.MomentProblem`, new file) per the
MathlibExt-curator convention.

### [`QOU/Archimedean/BalancedKernelConfluence.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedKernelConfluence.lean) — the QOU-side conditional theorem (composes the merged machinery, no restatement)

**PROVED (5 theorems, sorry-free, conditional on the named classes):**

- `carlemanCondition_factorial` — the general predicate discharged
  **definitionally** by the merged
  `BorelProperTimeMoment.carleman_divergence` (compose, don't restate).
- `stieltjesDeterminate_factorial` `[CarlemanDeterminacyStieltjes]` —
  $\{k!\}$ is Stieltjes-determinate; the only unformalized input is the
  classical Carleman theorem, whose hypothesis is Lean-proved.
- `eq_schwingerMeasure_of_factorial_moments` — the Attack-A determinacy
  pin, type-carried: positive + factorial moments ⇒ IS $e^{-s}ds$.
- `balanced_kernel_tendsto_schwinger`
  `[FrechetShohatStieltjes] [CarlemanDeterminacyStieltjes]` — **the
  main conditional theorem**: any sequence of probability measures on
  $[0,\infty)$ with all moments finite whose $k$-th moments tend to
  $k!$ converges weakly to `schwingerProbabilityMeasure`. (POS)
  survives the limit for free (the limit object is a
  `ProbabilityMeasure`).
- `bindingKernel_measure_eq_schwinger` — bridge to the merged
  `BindingKernelSchwingerRepresentation` reduction class: its (open)
  hypotheses + classical Carleman force the kernel **measure** to be
  Schwinger — closing the `moments → measure` loop that the merged
  `kernel_moments_eq_schwinger` left at the moment level.

**Hypothesis honesty.** The per-$n$ balanced moment convergence (audit
§2 — exact sympy, $h^1 \equiv 0$, $h^2$ = the Attack-E target) enters
`balanced_kernel_tendsto_schwinger` as the explicit hypothesis `hmom`,
NOT as a proved Lean fact: its formalization (per-$n$ sinh-product
bounds) is a separate tranche. Nothing in these files creates a class
instance, wires a production script, or touches a content block.

### Aggregator

Both modules registered in
[`QOU.lean`](../../content/quantum-observable-universe/lean/QOU.lean)
(after `QOU.Archimedean.BorelProperTimeMoment`).

## 3. Status counts

| Category | Count |
|---|---|
| Proved sorry-free (unconditional) | 10 (7 in `FrechetShohat` + `carlemanCondition_factorial` + 2 private density lemmas) |
| Proved sorry-free (conditional on gap classes) | 4 (`stieltjesDeterminate_factorial`, `eq_schwingerMeasure_of_factorial_moments`, `balanced_kernel_tendsto_schwinger`, `bindingKernel_measure_eq_schwinger`) |
| Mathlib-gap hypothesis classes (no instance, content-bearing) | 2 (`CarlemanDeterminacyStieltjes`, `FrechetShohatStieltjes`) |
| Cited sorries | **0** (the gaps are carried in types, not `sorry`s) |
| Verification | `lean`-direct exit 0 per file (olean-restore + manual dep-cone build of `QDifferenceConfluentObstruction` → `BorelProperTimeMoment`; `lake build` deliberately avoided per the wipe gotcha) |

## 4. Literature route note (Di Vizio–Zhang)

RSZ (Astérisque 355) explicitly defers $q \to 1$ confluence (§1.1.3);
the literature theorem for the *kernel-level* confluence is
**Di Vizio–Zhang**, *On q-summation and confluence*, Ann. Inst. Fourier
59(1):347–392 (2009) — registered key `divizio-zhang2009`. The
moment-route package scaffolded here (Fréchet–Shohat + Carleman) is the
*probabilistic* assembly of the same limit and is what the Lean can
carry near-term; the Di Vizio–Zhang analytic route (q-Gevrey
$\to$ Gevrey summation morphisms) would give the stronger
function-level confluence and remains the citation for the analytic
statement. **Missing reference keys** (for the parent to register in
`content/schema/references.ts` — not invented here):
Fréchet–Shohat 1931 (Trans. AMS 33, 533–543), Billingsley *Probability
and Measure* 3rd ed. 1995, Simon 1998 (Adv. Math. 137, 82–203 — already
cited textually in the merged `BorelProperTimeMoment.lean` header).

## 5. Coordination — PI-program pointer (same genre, no overlap)

The pentagon-infra PI-program (epic `qou-lbth`, bean `qou-n4pv`, PR
#4140 lineage; scaffold audits
[`2026-07-20-pi1-hadamard-scaffold.md`](2026-07-20-pi1-hadamard-scaffold.md),
[`2026-07-20-pi2-elliptic-divisor-scaffold.md`](2026-07-20-pi2-elliptic-divisor-scaffold.md))
is the same *genre* of work — a named classical theorem absent from
Mathlib, surveyed (HAS/MISSING map), scaffolded around, and roadmapped
for an upstream build. **Non-overlap:** PI needs **Hadamard
factorization** (entire-function theory, the `Analysis/Complex`
Jensen/Nevanlinna cone) to pin `phiBProd` among elliptic multiples; this
tranche needs **Fréchet–Shohat + Carleman** (measure theory / moment
problem, the `MeasureTheory.Measure.*` weak-convergence cone) —
different theorems, different Mathlib cones, no shared bricks. The
scoping style (gap table + honest verification status + hypothesis-class
carriers) deliberately mirrors PI-1's.

## 6. Discipline

- **Corpus-grep (all four paths).** `Fréchet|Shohat|Carleman|moment
  problem|weak convergence` over `docs/audits/`, `content/`,
  `computations/`, `docs/coordination/`: the only prior statements are
  the merged Attack-A/B docs (which *name* this gap) and the
  channel-rotation-askey indeterminate remark — no prior formalization
  or closure. The gap declared here is the same gap those audits named,
  now scaffolded, not a new "open" declaration.
- **NO FIT / nothing wired.** No numeric content at all; no instance
  created; no production script touched; no content block touched.
- **Anti-laundering.** The two classes carry classical-theorem
  *statements*; no instance exists, so nothing downstream can silently
  treat the gaps as closed. All conditional theorems wear the classes
  in their signatures (§3b-cond).
- **Render-QA:** the preflight grep battery was run by hand on this doc
  (balanced `$`/`$$`/braces; no `\operatorname`; no markdown-list line
  opening with `+`/`-`/`*` inside display math; no inline align-family
  environments). The pipeline render was not run in this sandbox — this
  doc was **not machine-validated**.

## 7. Cross-references

- Parent gap statement: [`2026-07-25-qborel-confluence-pos-attack.md` §4](2026-07-25-qborel-confluence-pos-attack.md)
- Merged moment/Carleman/falsifier machinery: [`BorelProperTimeMoment.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorelProperTimeMoment.lean) + [`2026-07-25-borel-propertime-attack-a-e.md`](2026-07-25-borel-propertime-attack-a-e.md)
- New files: [`FrechetShohat.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/FrechetShohat.lean), [`BalancedKernelConfluence.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedKernelConfluence.lean)
- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- PI-program (same Mathlib-gap genre): [`2026-07-20-pi1-hadamard-scaffold.md`](2026-07-20-pi1-hadamard-scaffold.md), epic `qou-lbth`
