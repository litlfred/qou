---
# qou-eao2
title: 'M1 [Mathlib4 Infra]: Polylogarithms, Bloch–Wigner 5-Term Relation & Bloch–Suslin Groups B₂(ℂ)/B₃(ℂ)'
status: todo
type: feature
priority: high
tags:
    - lean
    - mathlib-gap
    - polylogarithm
    - bloch-suslin
created_at: 2026-11-19T08:19:49Z
updated_at: 2026-11-20T17:37:12Z
parent: qou-dxbw
---

## Scope & Audit Metrics (`M1_DILOG_BLOCH_SUSLIN`)

- **Source Witness:** `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`
- **Mathlib4 Target Surface:** Mathlib.Analysis.SpecialFunctions.Polylogarithm (Li_2, Faddeev quantum dilog), Bloch–Wigner D_2(z) 5-term pentagon relation, PreBlochGroup / BlochGroup B_2(C) & B_3(C), scissors congruence, and Borel regulator
- **Cross-Linked Existing Beans:** `mlgp`, `qou-o41q`, `qou-mlbg`, `qou-gkco`, `qou-tc8y`, `qou-c8p8`, `qou-rtxm`
- **Uninstantiated / Toy Carriers:** **37** (`31` uninstantiated `class`es, `6` uninstantiated `structure`s, `0` `TOY_ONLY_INSTANCE`) across `28` `.lean` files
- **Total `Prop` Fields:** `57`  |  **Downstream Theorem/Def Consumers:** `44`
- **Standalone `axiom` / `opaque` Declarations in Cluster:** `0` `axiom`, `8` `opaque`

---

## Concrete Mathlib4 / QOU Build Plan

1. **Complex Polylogarithm & Analytic Continuation (`QOU/MathlibExt/ComplexDilogarithm.lean` $\to$ upstreamable Mathlib module):** Formalize $\mathrm{Li}_2(z) = -\int_0^z \frac{\log(1-t)}{t}\,dt$ on $\mathbb{C} \setminus [1, \infty)$ with reflection ($z \leftrightarrow 1-z$), inversion ($z \leftrightarrow z^{-1}$), and duplication identities.
2. **Bloch–Wigner $D_2(z)$ & 5-Term Pentagon Identity:** Connect `BlochWigner_lob` (`QOU/Archimedean/BlochWignerLobachevsky.lean`) to complex $\mathrm{Im}\,\mathrm{Li}_2(z) + \arg(1-z)\log|z|$ and prove the 5-term relation, discharging `Cl_2_PentagonHolds`, `HasPentagonRelation ℂ`, and `RogersPair`.
3. **Concrete `PreBlochGroup ℂ` / `BlochGroup ℂ` & $B_3(\mathbb{C})$ Quotient Instances:** Instantiate `HasBlochGroup ℂ`, `BlochWignerFiveTerm`, `Depth2IdentificationContext`, and Woronowicz $q$-exponential pentagon (`WoronowiczLeftCalculus`) over concrete rings/fields.

---

## Top Priority Uninstantiated / Toy Carriers (Ranked by Consumer Count)

| Status | Kind | Carrier (`class` / `structure`) | Consumers | Prop Flds | Data Flds | Location (`folio/quantum-observable-universe/...`) |
|---|---|---|---:|---:|---:|---|
| `UNINST` | `structure` | `QOU.Archimedean.BlochQuotient.RogersPair` | 7 | 5 | 2 | `predicted-spectra/bloch-group-quotient-construction.lean:94` |
| `UNINST` | `class` | `QOU.AlgebraicSubstrate.GBDepthPeriodCorrespondence.GBDepthPeriodCorrespondence` | 4 | 2 | 0 | `mass-theory/gb-depth-period-correspondence.lean:56` |
| `UNINST` | `structure` | `QOU.WedderburnMass.DepthGradedFrobeniusModule` | 4 | 1 | 3 | `mass-theory/quantum-dilogarithm-stratified.lean:30` |
| `UNINST` | `class` | `QOU.BraidKnot.PentagonUVCommutation.WoronowiczLeftCalculus` | 3 | 3 | 7 | `braids-and-knots/pentagon-uv-commutation-woronowicz.lean:77` |
| `UNINST` | `class` | `QOU.Archimedean.FiveTwoTriangulation` | 3 | 3 | 0 | `lean/QOU/Archimedean/BlochWignerLobachevsky.lean:626` |
| `UNINST` | `class` | `QOU.Archimedean.BlochWignerInjective` | 3 | 1 | 0 | `predicted-spectra/bring-hyperbolic-knot-bloch-decomposition.lean:286` |
| `UNINST` | `class` | `QOU.Archimedean.SubstantiveFillers.Cl_2_PentagonHolds` | 2 | 2 | 0 | `lean/QOU/Archimedean/ThreeSubstantiveMathlibFillers.lean:117` |
| `UNINST` | `class` | `QOU.QPochhammer.AlgebraicGeometricEquivalence` | 2 | 2 | 2 | `mass-theory/algebraic-geometric-dilog-equivalence.lean:195` |
| `UNINST` | `class` | `QOU.BraidKnot.ZHabiroRogersSaddle` | 2 | 1 | 1 | `lean/QOU/BraidKnot/QuantumDilogarithm.lean:200` |
| `UNINST` | `class` | `QOU.LiftingDescent.TmDivisorChartInputs` | 2 | 1 | 0 | `lean/QOU/LiftingDescent/tm_dilogarithm_evaluation.lean:79` |
| `UNINST` | `class` | `QOU.QuantumBloch.PentagonUvCommutationContext` | 1 | 5 | 7 | `lean/QOU/QuantumBloch/pentagon_uv_commutation.lean:16` |
| `UNINST` | `class` | `QOU.BraidKnot.BringTrilogDepth3Witness` | 1 | 4 | 5 | `lean/QOU/BraidKnot/BringTrilogDepth3Witness.lean:55` |
| `UNINST` | `class` | `QOU.Archimedean.NaStokesPartBOrdering` | 1 | 3 | 3 | `lean/QOU/Archimedean/DilogNaStokesOrdering.lean:76` |
| `UNINST` | `class` | `QOU.AppendixSurreals.QouInfraDischargesGoncharovZeta5` | 1 | 1 | 0 | `lean/QOU/AppendixSurreals/QouInfraDischargesGoncharovZeta5.lean:90` |
| `UNINST` | `class` | `QOU.Torsion.QuantumDilogarithmContext` | 1 | 1 | 4 | `lean/QOU/Torsion/quantum_dilogarithm.lean:40` |
| `UNINST` | `class` | `QOU.Archimedean.BringHyperbolicDecomposition` | 1 | 1 | 0 | `predicted-spectra/bring-hyperbolic-knot-bloch-decomposition.lean:129` |
| `UNINST` | `class` | `QOU.Archimedean.UpstreamAdditions.ComplexLiTwoUnitCircleClassical` | 1 | 1 | 0 | `predicted-spectra/upstream-mathlib-additions.lean:233` |
| `UNINST` | `class` | `QOU.Archimedean.UpstreamAdditions.Cl_2_DoubleAngle` | 1 | 1 | 0 | `predicted-spectra/upstream-mathlib-additions.lean:284` |
| `UNINST` | `class` | `QOU.BraidKnot.PhiQAJMachineryIdentification.Li2QRegulator` | 1 | 1 | 1 | `stochastic-mechanics/phi-q-aj-machinery-identification.lean:200` |
| `UNINST` | `class` | `QOU.AppendixSurreals.Depth2IdentificationBlochSuslin.Depth2IdentificationContext` | 1 | 0 | 6 | `lean/QOU/AppendixSurreals/Depth2IdentificationBlochSuslin.lean:18` |

---

## Standalone `axiom` / `opaque` Declarations in `M1_DILOG_BLOCH_SUSLIN` (Sample up to 15)

- `opaque QOU.BraidKnot.phi_q_residual` (`lean/QOU/BraidKnot/QuantumDilogarithm.lean:52`)
- `opaque QOU.BraidKnot.li2_q_residual` (`lean/QOU/BraidKnot/QuantumDilogarithm.lean:87`)
- `opaque QOU.LiftingDescent.MI` (`lean/QOU/LiftingDescent/tm_dilogarithm_evaluation.lean:57`)
- `opaque QOU.LiftingDescent.lnq` (`lean/QOU/LiftingDescent/tm_dilogarithm_evaluation.lean:62`)
- `opaque QOU.LiftingDescent.z` (`lean/QOU/LiftingDescent/tm_dilogarithm_evaluation.lean:66`)
- `opaque QOU.AlgebraicSubstrate.GBDepthPeriodCorrespondence.GroupLikeDepth` (`mass-theory/gb-depth-period-correspondence.lean:31`)
- `opaque QOU.AlgebraicSubstrate.GBDepthPeriodCorrespondence.GoncharovPeriodFiltration` (`mass-theory/gb-depth-period-correspondence.lean:36`)
- `opaque QOU.AlgebraicSubstrate.HqBiFiltration.BiFiltration` (`mass-theory/hq-bi-filtration.lean:50`)

## 2026-11-20 — W7 slice (PR #8541, session_01VQDpPfKSC33hwjyKMw3EHV)

- **Done:** `Cl_2_DoubleAngle` is inhabited. `QOU/Archimedean/ClausenDoubleAngleSeries.lean` proves `Cl₂(2θ) = 2Cl₂(θ) − 2Cl₂(π−θ)` for **every** real θ, from the series by an odd/even split, with no dilogarithm. The interval version `QOU.Knot.Cl_2_duplication` only covered (0, π). The class docstring that called a tsum proof "blocked" is corrected.
- **Still open:** `ComplexLiTwoUnitCircleClassical` (Im Li₂(e^{iθ}) = Cl₂(θ)), the pentagon / Bloch–Wigner 5-term relation, and the Bloch group. The bean stays `todo`.

## 2026-11-20 (later) — Li₂ on the unit circle (PR #8597)

- `ComplexLiTwoUnitCircleClassical` is now inhabited: `Im Li₂(e^{iθ}) = Cl₂(θ)` is proved via `Complex.im_tsum`. `blochWigner_unit_circle_eq_Cl_2` is unconditional.
- **Finding:** `Cl_2_PentagonHolds` (`ThreeSubstantiveMathlibFillers.lean:117`) is vacuous. Its `closure : (Fin 5 → ℝ) → Prop` is class *data*, so `closure := fun _ => False` inhabits it. Do not instantiate it that way. The real 5-term relation needs Li₂ off the unit disk (analytic continuation), which is the remaining M1 work.

## 2026-11-20 (evening) — CORRECTION, and the pentagon is inhabited (PR pending, branch claude/cl2-pentagon-honest-2026-11-20)

**I wrote above that "the real 5-term relation needs Li₂ off the unit disk (analytic continuation), which is the remaining M1 work". That was wrong, and I did not check before writing it.** The corpus already has:
- `QOU.MathlibExt.cLiTwoExt`: Li₂ continued to ℂ ∖ [1,∞), agreeing with the series on the closed disc off the cut (`cLiTwoExt_eq_cLiTwo_of_norm_le_one`);
- `QOU.Archimedean.FiveTermProof.blochD`, with the five-term relation **proved** (`fiveSum_eq_zero`, PR #7946), plus inversion, reflection and Bloch–Suslin rigidity (`DilogTheoryArchimedean`).

The same wrong claim appears in my PR #8597 comment on #8526 and in my chat report. The epic `qou-dxbw` M1 build-plan items 1–2 (Li₂ continuation, D₂ five-term) are therefore already done. Only the Bloch-group items remain.

**Now done:** `Cl_2_PentagonHolds` is restated with its closure condition as a definition (the five unit-circle points are Suslin's five arguments) rather than a free field. It is inhabited from `fiveSum_eq_zero` via the new `blochD_exp : D(e^{iθ}) = Cl₂(θ)`. Library sweep: 26 ok, 0 RED; axioms clean.
