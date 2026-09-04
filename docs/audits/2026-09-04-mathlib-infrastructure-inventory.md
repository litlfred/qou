# Mathlib-infrastructure inventory for the eightfold / hyperbolic-volume arc

**Date:** 2026-09-04
**Branch:** `claude/lean-prove-assertions-2026-09-04`
**Epic:** `qou-8lxd` (eightfold way / SM derived from QOU)
**Scope:** the *Mathlib-infrastructure* half of the arc's gap inventory. A sibling
agent owns the complementary *citation* half (`-- Ref:` sources). This document does
not touch citations.

**Pinned Mathlib measured against:** `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`
(2025-10-14), toolchain `leanprover/lean4:v4.24.0`. Both copies on disk
(`/home/user/qou/.lake/packages/mathlib` and
`content/quantum-observable-universe/lean/.lake/packages/mathlib`) are at that same
revision — verified with `git log -1 --format=%H` in each. **Everything below was
grepped against that tree, not recalled.** Where a claim could not be measured it is
labelled *unmeasured*.

---

## Why the second half of this audit is load-bearing

This session already made the error this document exists to catch. An audit asserted
that Mathlib had no hyperbolic-geometry API and that `library/` held nothing on the
subject; the owner corrected it. The retraction now sits at
`content/quantum-observable-universe/lean/QOU/Eightfold/HyperbolicVolumeFormType.lean:150-165`
and is correct. **But the same false sentence is still live in two other places**
(§F1, §F2 below), and five further "Mathlib lacks X" claims turn out to be wrong,
stale, or measured by a command that does not measure what it says.

So a "Mathlib lacks X" note in this corpus is **not** evidence. Re-measure the
specific claim in the file you are editing.

---

## Tier definitions

| tier | meaning |
|---|---|
| **HAVE** | Mathlib has it at the pin. The declaration and file are named. Where the corpus claims otherwise, the claim is flagged by `file:line` as a defect to fix. |
| **BUILD** | Not in Mathlib, but constructible in `QOU/MathlibExt/` (or in place) from what Mathlib already carries. A 2-3 line construction sketch and a rough size are given. |
| **UPSTREAM** | Genuinely missing from Mathlib and general enough to belong there rather than here. Whether a Mathlib PR or issue exists is **unchecked** — this audit ran offline and did not browse. |
| **RESEARCH** | No infrastructure closes it. The mathematics is open. What is open is stated. |

## Counts

| tier | count | note |
|---|---|---|
| **HAVE** | 10 | 7 of them contradict a live corpus claim |
| **BUILD** | 5 | all five unbeaned before today |
| **UPSTREAM** | 14 | 11 already tracked by an existing bean; 3 newly identified |
| **RESEARCH** | 5 | 4 already beaned; none is an infrastructure gap |
| **false / stale "Mathlib lacks X" claims** | 8 | actionable now; §F |

**Sorry/axiom/opaque baseline for the six audited directories**, measured with a
comment-stripping AST-lite scanner (`scratchpad/leanscan.py`, strips `--` and nested
`/- -/` before matching, so prose like "sorry-free" is not counted):

| directory | files | `sorry` | `axiom` | `opaque` |
|---|---|---|---|---|
| `QOU/Eightfold/` | 26 | 0 | 0 | 0 |
| `QOU/EightfoldWay/` | 2 | 0 | 0 | 0 |
| `QOU/QuantumObservableUniverse/` | 24 | 0 | 0 | 0 |
| `QOU/BringsSurface/` | 8 | 0 | 0 | 0 |
| `QOU/MassTheory/` | 145 | 0 | 0 | 0 |
| `QOU/MathlibExt/` | 149 | 0 | **5** | 0 |
| `QOU/Archimedean/` (hyperbolic layer) | 141 | 0 | **1** | **4** |

A naive `grep -c sorry` over these directories returns 105 and is **entirely prose** —
the corpus discusses `sorry` constantly in docstrings ("machine-proved sorry-free",
"a `sorry` on a refutable statement"). Do not quote a raw grep here.

The workarounds are therefore concentrated, not diffuse: **5 SDP axioms, 1 Weierstrass
axiom, 3 Weierstrass opaques, and 1 Bloch–Wigner opaque.** Every one is analysed below.

### Note: there are THREE extension trees, not one

The brief named `QOU/MathlibExt/` as "the corpus's own record of what it thinks Mathlib
is missing". It is one of three:

| tree | files | character |
|---|---|---|
| `QOU/MathlibExt/` | 149 | general-purpose Mathlib-shaped lemmas |
| `QOU/Mathlib/` | **211** | Roth/Schensted/SYT/Borel programme + `NonAbelianStokes`, `KazhdanLusztigBasis`, `LPDuality`, `SDPDuality` |
| `QOU/Infra/` | 4 | `Polylogarithm`, `BorelRank`, … |

`QOU/Mathlib/` is the larger of the two and carries the *harder* gaps. An inventory
that reads only `MathlibExt/` sees under 40 % of the surface. Measured:
`find <dir> -name '*.lean' | wc -l`.

---

## HAVE — Mathlib has it

### H1. The hyperbolic metric on ℍ² — **and the corpus says it does not**

**Mathlib:** `Mathlib/Analysis/Complex/UpperHalfPlane/Metric.lean` (341 lines).
`instance : Dist ℍ`; `dist_eq : dist z w = 2 * arsinh (dist (z:ℂ) w / (2 * √(z.im * w.im)))`
— the Poincaré distance; `cosh_dist`, `sinh_half_dist`, `tanh_half_dist`;
`metricSpaceAux : MetricSpace ℍ`; hyperbolic `center z r` and ball comparisons;
and the isometries `isometry_real_vadd`, `isometry_pos_mul`, `isometry_vertical_line`,
plus `ModularGroup.S` acting by isometries (`Metric.lean:324`).
Alongside: `Manifold.lean` gives `ChartedSpace ℂ ℍ` and `IsManifold 𝓘(ℂ) ω ℍ`;
`MoebiusAction.lean` (389 lines) gives the `GL(2,ℝ)⁺` and `SL(2,R)` actions.

**Measured:** `grep -n '^\(noncomputable \)\?\(def\|instance\|theorem\)' Metric.lean`;
`grep -rn 'Isometry' UpperHalfPlane/*.lean`; `wc -l UpperHalfPlane/*.lean` (1376 total).

**Corpus claim contradicted:** `QOU/Archimedean/HyperbolicVolumeMeasure.lean:12-13` —
*"a complex domain with an `SL₂` action, carrying **no Riemannian metric**, no volume
form, no geodesics."* One-third false. "No volume form" and "no geodesics" are correct
(`grep -rln 'geodesic' Mathlib/` returns two unrelated combinatorics files; no measure
on ℍ). The metric is there, together with the very generator — inversion — that file
names as the missing one on its own `H³` side. See §F1.

**What it does *not* give:** ℍ³. The genuinely-3-dimensional statement stands.

### H2. Differential forms and the exterior derivative — on a normed space

**Mathlib:** `Mathlib/Analysis/Calculus/DifferentialForm/Basic.lean` (231 lines).
An `n`-form is `ω : E → E [⋀^Fin n]→L[𝕜] F` with `E`, `F` arbitrary normed spaces over
a `NontriviallyNormedField 𝕜`. Carries `extDeriv`, `extDerivWithin`, linearity
(`extDeriv_add`, `extDeriv_smul`), congruence lemmas, `extDeriv_apply`, and
**`extDeriv_extDeriv` — `d ∘ d = 0`**.

**Measured:** `grep -rn 'exteriorDerivative\|extDeriv' Mathlib/ --include=*.lean`;
`sed -n '1,68p'` on the file for the variable block and module docstring.

Its own TODO (lines 34-38) says: *"same for manifolds (**not defined yet**)"*. So the
abstraction exists, at normed-space level, and the manifold version is explicitly
future work — see **B3**.

**Corpus claims contradicted:** `QOU/Mathlib/NonAbelianStokes.lean:10` — *"Mathlib has
differential forms (`Mathlib.Geometry.Manifold.MFDeriv`, etc.)"*. Wrong module in both
directions: `MFDeriv` is the manifold *derivative*, not forms; and the file that does
have forms is not cited. See §F3.
`QOU/Eightfold/ContactDistributionRank.lean:97-98` — *"no differential forms on
manifolds at all"* is **correct as scoped** but omits the normed-space layer, which is
exactly what its own worked example (`M = ℝ²`) needs. See §F7.

### H3. Riemannian manifolds and path length

**Mathlib:** `Mathlib/Geometry/Manifold/Riemannian/{Basic,PathELength}.lean`, plus
`Mathlib/Geometry/Manifold/VectorBundle/Riemannian.lean` and
`Mathlib/Topology/VectorBundle/Riemannian.lean`. Provides
`class IsRiemannianManifold I M : Prop` ("the distance is the infimum of lengths of
paths"), `ContMDiffRiemannianMetric`, `riemannianMetricVectorSpace`, and
`EmetricSpace.ofRiemannianMetric`.

**Measured:** `find Mathlib -iname '*riemann*'`;
`grep -rn 'RiemannianMetric\|IsRiemannianManifold' Mathlib/`.

**What it does not give:** no Riemannian *volume measure*, no curvature (`grep -rln
'curvature' Mathlib/` → one hit, `MeasureTheory/Measure/Doubling.lean`, unrelated), no
geodesics as a named object.

**Relevance:** `QOU/Archimedean/HyperbolicMetric.lean:131` defines
`noncomputable def dH (x y : E) : ℝ≥0∞` as an infimum of path lengths — the same
construction Mathlib's `IsRiemannianManifold` + `PathELength` packages. See **B5**.

### H4. Coxeter systems — the Hecke prerequisite

**Mathlib:** `Mathlib/GroupTheory/Coxeter/{Basic,Length,Inversion,Matrix}.lean`,
**1612 lines** total (516 / 344 / 483 / 269, `grep -c ''`). `CoxeterMatrix`,
`CoxeterSystem`, `simple`, `wordProd`, `lift` (the universal property),
`simple_induction`, plus length and inversion theory.

**Corpus:** correctly cited by `QOU/MathlibExt/IwahoriHeckeAlgebra.lean:8-11`, which
also uses `CoxeterSystem` as a *positive control* for its own negative measurement —
good practice worth copying.
**Stale claim:** `docs/audits/2026-05-30-atom-braid-categorical-proof-feasibility.md:25`
says *"Even Mathlib's `CoxeterSystem` order-accessor API is in flux."* Dated
2026-05-30; at this pin it is 1612 lines across four files. See §F8.

### H5. Exterior powers of a module

**Mathlib:** `Mathlib/LinearAlgebra/ExteriorPower/{Basic,Pairing}.lean` (`⋀[R]^n M`,
`exteriorPower.ιMulti`, `exteriorPower.map`, `alternatingMapLinearEquiv`),
`Mathlib/LinearAlgebra/ExteriorAlgebra/{Basic,Grading,OfAlternating}.lean`,
`Mathlib/LinearAlgebra/Alternating/{Basic,Curry,DomCoprod}.lean`, and
`Mathlib/Algebra/Category/ModuleCat/ExteriorPower.lean`.

**Corpus claim partly contradicted:** `QOU/Eightfold/ContactDistributionRank.lean:97` —
*"Mathlib has no exterior-power-of-an-object API"*. True for an object of an abstract
monoidal category; false for modules and for `ModuleCat`. See §F7.

**Not there:** a wedge *product* `Λ^p × Λ^q → Λ^{p+q}` as a named operation
(`grep -rn 'wedge' LinearAlgebra/Alternating/*.lean` → nothing).

### H6. Gram matrices (partial)

**Mathlib:** `Mathlib/Analysis/InnerProductSpace/GramMatrix.lean` — `Matrix.gram 𝕜 v`,
`posSemidef_gram`, `posDef_gram_iff_linearIndependent`, `isHermitian_gram`,
`submatrix_gram`. Requires `RCLike 𝕜` and an `Inner`.

**Corpus:** `QOU/MathlibExt/GramNondegenerate.lean:13` says *"Mathlib does not have
this"* — and is **correct as scoped**: its subject is an arbitrary bilinear form over
an arbitrary field, connected to `Submodule.orthogonalBilin`, which `Matrix.gram` does
not cover. But the file rolls its own `gramMatrix B v` without naming `Matrix.gram`
anywhere. Low-priority reuse opportunity, not a defect; no bean.

### H7. Volume forms on a real inner product space

**Mathlib:** `Mathlib/Analysis/InnerProductSpace/Orientation.lean` —
`Orientation.volumeForm : E [⋀^Fin n]→ₗ[ℝ] ℝ`, `volumeForm_robust`,
`abs_volumeForm_apply_le`, `volumeForm_neg_orientation`, and the
`abs_volumeForm_apply_of_pairwise_orthogonal` bound. Ten-plus lemmas.

Relevant to `QOU/QuantumObservableUniverse/{VolumeForm,VolumeFormDegree}.lean`, which
work at the categorical level and correctly do not claim a Mathlib gap.

### H8. Covering maps and arithmetic ramification

**Mathlib:** `Mathlib/Topology/Covering.lean` (`IsCoveringMap`, `IsCoveringMapOn`, and
lifting lemmas), `Mathlib/NumberTheory/RamificationInertia/{Basic,Galois,Unramified}.lean`,
`Mathlib/RingTheory/Valuation/RamificationGroup.lean`.

**Corpus claim upheld:** `QOU/BringsSurface/CoveringDegreeRamification.lean:92` —
*"Mathlib has no branched-covering API"*. Correct. `IsCoveringMap` is the *unbranched*
notion, and `RamificationInertia` is arithmetic (Dedekind domains), not topological.
No Riemann–Hurwitz: `grep -rn 'Hurwitz' Mathlib/` returns only Hurwitz *zeta*
functions. Verdict stands; recorded so nobody "corrects" it on a `Covering.lean` hit.

### H9. Fourier series on the circle — **and a filler says these are missing**

**Mathlib:** `Mathlib/Analysis/Fourier/AddCircle.lean` — `fourierCoeff`,
`hasSum_fourier_series_L2`, `hasSum_fourier_series_of_summable`,
`has_pointwise_sum_fourier_series_of_summable`, and Parseval
(`tsum_sq_fourierCoeff`). Also `PoissonSummation.lean`, `Inversion.lean`,
`FourierTransform.lean`.

**Corpus claim contradicted:** `QOU/Archimedean/ClausenFunctionMathlibFiller.lean:33-34`
— *"Periodicity / antisymmetry lemmas (sketch — full proofs awaiting **Fourier-series
infrastructure in Mathlib**)"*. The infrastructure is there; and the `Cl₂` periodicity
and antisymmetry lemmas do not need it anyway (they follow termwise from `sin`
periodicity and oddness over the file's own `tsum` definition). See §F4. Note the file
elsewhere records that two harder facts were closed in 2026-07 *"no Fourier identities
needed"* — the header lags its own changelog.

### H10. Young diagrams, root systems, semisimplicity

**Mathlib:** `Mathlib/Combinatorics/Young/{YoungDiagram,SemistandardTableau}.lean`;
`Mathlib/LinearAlgebra/RootSystem/` (16 files: `Defs`, `CartanMatrix`, `Base`,
`WeylGroup`, `Reduced`, `GeckConstruction`, …); `isSemisimpleRing` (9 files);
`Mathlib/Analysis/InnerProductSpace/GramSchmidtOrtho.lean`;
`Mathlib/LinearAlgebra/Matrix/PosDef.lean` (`Matrix.PosSemidef`, eigenvalue API).
`Combinatorics.Partition` appears in 52 files.

**Not there:** `StandardYoungTableau` (`grep` → 0), hook-length (0), RSK (0), Specht
(0). The corpus builds all four in `QOU/Mathlib/` — see **U9**.

---

## BUILD — constructible here from what Mathlib has

### B1. Give `BlochWigner_unit_circle` its body — it already exists in-tree

**Site:** `QOU/Archimedean/BlochWignerUnitCircle.lean:67`
`noncomputable opaque BlochWigner_unit_circle (_θ : ℝ) : ℝ`.

**Object stood in for:** the Bloch–Wigner dilogarithm restricted to unit-circle shape
parameters, `D(e^{iθ}) = Cl₂(θ)` — the carrier for `Vol(4₁) = 2·Cl₂(π/3)` and
`Vol(𝓑₃) = 8·Cl₂(π/2)`.

**Construction:** `noncomputable def BlochWigner_unit_circle (θ : ℝ) : ℝ := Cl_2 θ`.
That is not a proposal — it is already written, sorry-free, at
`QOU/Archimedean/BlochWignerMathlibFiller.lean:60`, over `Cl_2` at
`ClausenFunctionMathlibFiller.lean:80`. **~5 lines**, plus import surgery.

**Why the seal is stale.** The `opaque`'s own docstring (lines 58-62) says the body is
*"sealed pending the canonical Clausen-function integration (Phase 3 research-grade
closure)"*. That closure landed: the sibling filler records `Cl₂` derivative,
series↔integral bridge, continuity and boundary lemmas **CLOSED 2026-07-19**, and the
duplication formula **CLOSED 2026-07-26**, all sorry-free in `QOU/Knot/Clausen.lean`
(`hasDerivAt_clausen:87`, `clausen_eq_series:441`, `continuous_Cl_2:112`,
`Cl_2_two_pi_sub:451`, `Cl_2_pi_div_three_pos:490`).

**And it is an FQN collision.** Both files open `namespace QOU.Archimedean`
(`BlochWignerUnitCircle.lean:53`, `BlochWignerMathlibFiller.lean:53`), so both declare
`QOU.Archimedean.BlochWigner_unit_circle` — the `qou-kfcl` defect class. It is
currently dodged by **commenting the real definition out**:
`QOU/Archimedean.lean:30` imports `BlochWignerUnitCircle`, and
`QOU/Archimedean.lean:36` is `-- import QOU.Archimedean.BlochWignerMathlibFiller`.
So the sealed stub is live and the proved definition is disabled.

**Consumer:** `QOU/Archimedean/EmCouplingBringZeroMode.lean` (which at line 241 already
quotes the filler's `:= Cl_2 θ` body as the intended one).

**Bean:** `qou-tc8y`.

### B2. Lie-algebra-valued 1-forms on a normed space

**Site:** `QOU/Mathlib/NonAbelianStokes.lean:47` — `LieValuedOneForm`, an abstract
carrier for `Ω¹(M; 𝔤)` with no model.

**Construction:** with `[NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] [LieRing 𝔤]
[LieAlgebra ℝ 𝔤]`, a 𝔤-valued 1-form on a normed space `E` is literally
`E → E [⋀^Fin 1]→L[ℝ] 𝔤` — Mathlib's `DifferentialForm` target `F` is an **arbitrary**
normed space (`Basic.lean:48-53`), so no new type is needed. `extDeriv` then applies
verbatim, and the covariant differential `d_α β = dβ + [α ∧ β]` is a definition on top
of it. **~100-200 lines** for the carrier, the bracket-wedge, and `d_α`.

**What it does NOT close:** the multiplicative line/surface integral. Mathlib has no
holonomy, no parallel transport, no path-ordered exponential (`grep -rln
'holonomy\|parallel transport\|ParallelTransport\|pathOrdered' Mathlib/` → **0 files**).
That half is **R2**.

**Why it is still worth doing:** the file's own worked example is `M = ℝ²` (line 107),
which is a normed space, so this replaces an abstract `Prop`-carrier — flagged as
self-certifying in bean `qou-ewc4` — with a real object, on exactly the case the file
cares about.

**Bean:** `qou-ghc6`.

### B3. Differential `k`-forms on a manifold

**Site:** nothing in the corpus can state `Θ ∧ dΘ` or the hyperbolic volume form as a
form. `QOU/Eightfold/{ContactDistributionRank,HyperbolicVolumeFormType}.lean` are
honest about this and work entirely in `ℕ` arithmetic as a result.

**Construction:** a `C^r` `k`-form on `M` is a `ContMDiffSection` (Mathlib:
`Geometry/Manifold/VectorBundle/SmoothSection.lean:325`) of the bundle whose fibre at
`x` is `ContinuousAlternatingMap ℝ (TangentSpace I x) F (Fin k)`. The fibre type,
the bundle constructions (`VectorBundle/Hom.lean`, `Topology/VectorBundle/Constructions.lean`)
and the pointwise exterior derivative (H2) all exist; the work is assembling the bundle
and transporting `extDeriv` chart-wise. **~300-600 lines**, the largest BUILD here.

**Upstreamable too**, and Mathlib knows it: `DifferentialForm/Basic.lean:34-38` lists
manifold forms as TODO and asks for a Zulip design discussion first. Classified BUILD
rather than UPSTREAM because an in-repo version unblocks the arc now and the upstream
route is gated on that discussion.

**Bean:** `qou-jvua`.

### B4. Retype `IdealTetrahedron` over Mathlib's `UpperHalfPlane`

**Site:** `QOU/MathlibExt/IdealTriangulation.lean:66-70`
`structure IdealTetrahedron where shape : ℂ ; im_pos : 0 < shape.im`.
That is `Mathlib.Analysis.Complex.UpperHalfPlane.ℍ`, spelled out.

**Measured:** `UpperHalfPlane` occurs in **2** QOU files and in **zero** QOU
declarations — both hits are audit prose (`Archimedean/HyperbolicVolumeMeasure.lean:9`,
`Eightfold/HyperbolicVolumeFormType.lean:137`). Meanwhile **62** QOU files carry a
hand-rolled `im_pos` / `0 < _.im` (`grep -rln 'im_pos\|0 < .*\.im' QOU/ | wc -l`).

**What retyping buys:** `UpperHalfPlane.im_pos`, `ne_zero`, `normSq_pos`, the
`positivity` extensions (`evalUpperHalfPlaneIm`, `evalUpperHalfPlaneCoe`), the
`{x : ℝ // 0 < x}` and `ℝ`-translation actions, and — the substantive one — the
`SL(2,R)` Möbius action and the hyperbolic metric of H1, which is the natural home for
shape-parameter transformations `z ↦ 1/(1−z) ↦ 1 − 1/z`. **Small-to-medium**; mostly
mechanical, but it touches a load-bearing structure so it needs a real `lean`-direct
pass. Do it *after* B1, which is free.

**Bean:** `qou-m8xt`.

### B5. Re-base `HyperbolicMetric.dH` on `Riemannian/PathELength`

**Site:** `QOU/Archimedean/HyperbolicMetric.lean:131` — `dH` as an infimum of path
lengths, hand-rolled; the file carries three of the hyperbolic layer's open metric
obligations (existing bean: *"GAP: hyperbolic dH metric axioms — symmetry, triangle,
separation"*).

**Construction:** Mathlib's `Riemannian/PathELength.lean` + `EmetricSpace.ofRiemannianMetric`
+ `IsRiemannianManifold` package exactly "the distance is the infimum of path lengths",
including the measurability and integrability plumbing (`JacobianOneDim`,
`MeasurePreserving` on `Icc`) that the symmetry/triangle proofs need. **Medium.**

This is a *method* proposal for an already-beaned gap, not a new gap: the existing bean
records what is unproved, this records that upstream API now exists to prove it against.

**Bean:** `qou-sd8y`.

---

## UPSTREAM — genuinely missing from Mathlib

PR/issue status is **unchecked** for every row: this audit ran offline.
"Already beaned" cites an existing bean title verbatim.

| # | missing from Mathlib | measurement | status |
|---|---|---|---|
| **U1** | polylogarithm / `Li₂` / Bloch–Wigner / Clausen | `polylog` **0 files**; `dilog` 1 hit, a docstring in `Analysis/SpecialFunctions/Integrals/LogTrigonometric.lean:12`; `Clausen` 3 hits, all false positives (author "Claus Clausen"; Clausen–Scholze condensed math); `Lobachevsky`, `Bloch` **0** | already beaned: *"Add the missing Mathlib: complex dilogarithm (continuation + reflection + inversion), upstreamable"* |
| **U2** | Iwahori–Hecke algebra | `Hecke` in **1** Mathlib file — `NumberTheory/FLT/Basic.lean:39`, a docstring about Hecke *operators*. Prerequisite `CoxeterSystem` present (H4) | already beaned: *"Infra: IwahoriHecke + Specht modules in Mathlib"*, *"SW-1"*, *"T2C"* |
| **U3** | Artin braid groups | no `BraidGroup`; the 4 `*braid*` filename hits are braided **monoidal categories** | already beaned: *"T2: Artin braid group B_n via PresentedGroup"* |
| **U4** | Temperley–Lieb, Kauffman bracket, Markov trace, Jones polynomial, knots | `TemperleyLieb` **0**, `markovTrace` **0**, `skein` **0**, `Knot` **0**, `Jones polynomial` **0** | already beaned: *"GAP/INFRA: Mathlib knot theory — Jones polynomial, connected sum, Markov-trace multiplicativity"* |
| **U5** | Kazhdan–Lusztig basis | `Kazhdan` **0 files** | corpus carries `QOU/Mathlib/KazhdanLusztigBasis.lean`; no *upstream* bean found |
| **U6** | pivotal / spherical / ribbon / fusion categories | `Pivotal` **0**, `Spherical` **0**, `Ribbon` **0**, `FusionCategory` **0**, `quantum dimension` **0**. Mathlib has `Monoidal/Rigid/` and `Monoidal/Braided/` only; `rightDualIso` exists (`Rigid/Basic.lean:541`) with `rightDualIso_id` as its only lemma — matching `MathlibExt/PivotalCategory.lean:291` exactly | already beaned: *"RT-1: RibbonCategory layer…"*, *"SphericalCategory…"*, *"GAP: qDimObj…needs a pivotal structure Mathlib lacks"* |
| **U7** | SDP / conic duality, strict complementarity, Slater | `semidefinite program` **0**, `strict complementarity` **0**, `KKT` **0**, `duality gap` **0**, `LinearProgram` **0**; `Analysis/Convex/` has no optimisation layer. This is what the **5 `MathlibExt` SDP axioms** stand on (`SDP.lean:286`, `SDPRankEquality.lean:204,648`, `SDPRealUniqueness.lean:188,586`) | already beaned: `qou-apcl` (verdict CONFIRMED per `docs/audits/2026-08-31-individuating-the-fourteen-infra-blocked-verdicts.md:95`) |
| **U8** | hyperbolic 3-space, ideal tetrahedra, Mostow | `*hyperbolic*` filename **0**; no ℍ³ | already beaned: `qou-5gai` (epic, tiers H1–H5) |
| **U9** | RSK, hook-length, Specht modules, standard Young tableaux | `RSK` **0**, `RobinsonSchensted` **0**, `hookLength` **0**, `Specht` **0**, `SemistandardYoungTableau` present but no *standard* variant | already beaned: *"Infra: IwahoriHecke + Specht modules in Mathlib"*, *"F1-infra"*. ~200 files already built in `QOU/Mathlib/Schensted*`+`SYT*` — the single largest upstreamable body in the corpus |
| **U10** | numerical quadrature | `trapezoid`/`simpson`/`quadrature` **0 files**, matching `MathlibExt/TrapezoidRule.lean:4` | no upstream bean found; low arc-relevance |
| **U11** | Weierstrass ℘ and elliptic functions | `℘` **0**, `weierstrassP` **0**, `EllipticFunction`/`DoublyPeriodic` **0**. `AlgebraicGeometry/EllipticCurve/Weierstrass.lean` is the **Weierstrass equation** (algebraic), a different object; `Topology/ContinuousMap/Weierstrass.lean` is approximation. Backs the 3 opaques + 1 axiom in `Archimedean/WeierstrassProjection.lean:42,49,57,87` | already beaned: *"Measure closeability of the 4 analysis axioms (Lobachevsky-Catalan, Weierstrass, 2x parallelogram contour)"* |
| **U12** | contact structures and contact forms | `contact structure` **0**, `ContactForm` **0**, `Contact` **0**; `symplectic` only as `LinearAlgebra/SymplecticGroup.lean`, a matrix group with **no symplectic form** (`SymplecticForm` **0**). The expectation stated in the brief is confirmed | **no bean** — created today |
| **U13** | Hodge star | `Hodge` appears **once** in all of Mathlib, at `ModelTheory/Fraisse.lean:60`, citing the model theorist **W. Hodges**. `hodgeStar` **0** | no upstream bean (the corpus's *q*-Hodge-star bean is a different object) |
| **U14** | holonomy / parallel transport / path-ordered exponential | `holonomy`, `Holonomy`, `parallel transport`, `ParallelTransport`, `pathOrdered` — **0 files each** | see **R2**; no upstream bean |

Also measured absent, and worth recording because a reader may assume otherwise:
**Stokes' theorem** exists only as the divergence theorem
(`MeasureTheory/Integral/DivergenceTheorem.lean`, `Analysis/BoxIntegral/DivergenceTheorem.lean`);
there is no differential-forms Stokes. And the **centre of a group algebra** has no API
(`MonoidAlgebra` + `center` → 0 hits), confirming `MathlibExt/GroupAlgebraCenter.lean:27`.

---

## RESEARCH — no infrastructure closes these

### R1. The triangulation → manifold volume bridge
`QOU/MathlibExt/ManifoldVolumeBridge.lean` states it as a class with **no instance**,
which is the correct representation of an open problem. The corpus can prove things
about `IdealTriangulation.volume = Σ D(zᵢ)`; it cannot say `Vol(S³ ∖ K) = …` because
the left-hand side has no referent. Closing it needs Thurston hyperbolisation plus
Mostow rigidity — theorems, not libraries. `IdealTriangulation.lean:33-44` says so
explicitly and should not be softened. Already tracked (`qou-8mtd`, `qou-b84o`).

### R2. Non-abelian multiplicative surface integration (Yekutieli)
The *carrier* is buildable (**B2**); the *theorem* — `MI₁(α; ∂σ) = MI₂(d_α β; σ)` — is
a 2015 research monograph and there is no Mathlib holonomy to build it on (**U14**).
`QOU/Mathlib/NonAbelianStokes.lean` estimates 3000–5000 LoC; this audit does not
dispute that but notes the estimate is unmeasured. Already tracked (`qou-ewc4`).

### R3. The volume conjecture
Kashaev / coloured-Jones asymptotics equalling `Vol(S³∖K)`. Named at
`MathlibExt/IdealTriangulation.lean:47` (Ohtsuki 2016). Open mathematics; the
`library/` holds **214** section files on it (see below). Already tracked.

### R4. The extensive many-body binding term (Δ_λ magnitude)
The arc's flagship open item, `qou-brng`. Four sorry-free formalize-first results prune
the scaling from four directions; the coefficient is open. **Not** an infrastructure
gap — no Mathlib addition touches it. Already tracked; listed here only so it is not
misfiled as infra.

### R5. Which branched covering Bring's surface carries
`QOU/BringsSurface/CoveringDegreeRamification.lean` proves that degree 3 with six
branch points forces cyclic ℤ/3 monodromy, contradicting the `S₃` the same corpus
sentence asserts. Resolving it is an authoring decision plus a geometry question, not
infrastructure. Already surfaced in that file's own header.

---

## F — false or stale "Mathlib lacks X" claims, actionable now

Each is quoted, measured, and given the corrected form.

### F1. `QOU/Archimedean/HyperbolicVolumeMeasure.lean:12-13`

> "that one hit is the **2-dimensional modular-forms** upper half plane — a complex
> domain with an `SL₂` action, carrying **no Riemannian metric, no volume form, no
> geodesics**."

**One of the three is false.** `Analysis/Complex/UpperHalfPlane/Metric.lean` (341
lines) gives ℍ the hyperbolic distance, `MetricSpace`, and its isometry generators
including `ModularGroup.S` — the inversion whose absence this same file laments on its
own `H³` side (lines 55-60). "No volume form" and "no geodesics" hold.
**Corrected form:** *"…carrying the hyperbolic **metric** (`Metric.lean`: `Dist ℍ`,
`dist_eq`, `isometry_real_vadd`/`isometry_pos_mul`/`ModularGroup.S`) and a
`ChartedSpace ℂ`/`IsManifold` structure, but no volume measure and no geodesics — and
in dimension **two**, which is what makes it not a route to `H³`."*
The dimension argument is the real one and survives intact; the metric claim is
surplus and wrong. **Bean `qou-6eik`.**

### F2. Bean `qou-5gai` — the same sentence, verbatim

> "carrying **no Riemannian metric, no volume form, no geodesics**. It is not a
> hyperbolic-geometry library and does not generalise to `H³`. So the gap is total,
> not partial."

Same defect, in the epic that governs the whole H1–H5 tier plan — so it is the version
an agent is most likely to read. **And the corpus already knows better**: sibling bean
`qou-b84o` (2026-08-31) says *"`Mathlib/Analysis/Complex/UpperHalfPlane/` is the
2-dimensional hyperbolic plane, built for modular forms — **`Metric.lean` gives it the
hyperbolic metric**, and nothing extends to `ℍ³`"*. Two beans, opposite claims, the
correct one newer and quieter. The conclusion ("does not generalise to `H³`") is right
in both. Folded into **bean `qou-6eik`** with F1, since it is one edit pass.

### F3. `QOU/Mathlib/NonAbelianStokes.lean:10` (and `:295`)

> "Mathlib has differential forms (`Mathlib.Geometry.Manifold.MFDeriv`, etc.) but
> **not** Lie-algebra-valued forms or the multiplicative line / surface integral."

**Wrong in both directions.** `MFDeriv` is the manifold *derivative*; it is not
differential forms, and Mathlib has **no** manifold forms at all. The file that does
have forms — `Analysis/Calculus/DifferentialForm/Basic.lean` — is not cited, and its
target `F` is an arbitrary normed space, so Lie-valued forms on a normed space are
directly expressible (**B2**). What is genuinely absent is the *multiplicative* integral
(**U14**), which is the half the sentence gets right.
**Bean `qou-ipsl`.**

### F4. `QOU/Archimedean/ClausenFunctionMathlibFiller.lean:33-34`

> "Periodicity / antisymmetry lemmas (sketch — full proofs awaiting **Fourier-series
> infrastructure in Mathlib**)."

`Analysis/Fourier/AddCircle.lean` has `hasSum_fourier_series_L2`,
`hasSum_fourier_series_of_summable`, the pointwise version, and Parseval. Separately,
these particular lemmas do not need Fourier theory: over the file's own `tsum`
definition they follow termwise from `sin` periodicity and oddness. The file's later
changelog even records the *harder* facts closing *"no Fourier identities needed"* —
so the header contradicts its own body. **Bean `qou-u4mx`.**

### F5. `QOU/Archimedean/BlochWignerUnitCircle.lean:58-62`

> "sealed pending the canonical Clausen-function integration (Phase 3 research-grade
> closure)."

Stale: that closure landed 2026-07-19 and 2026-07-26. **The fix is B1** (give it the
body), so this is not tracked separately — bean `qou-tc8y`.

### F6. `QOU/MathlibExt/BraidGroup.lean:8-9`

> "**Mathlib has no braid groups.** Verified by search: **no file matching `*braid*`
> anywhere in `Mathlib/`**."

The **conclusion is correct** — there is no `BraidGroup`. The **stated measurement is
false**: `find Mathlib -iname '*braid*'` returns four hits
(`CategoryTheory/GradedObject/Braiding.lean`,
`CategoryTheory/Monoidal/DayConvolution/Braided.lean`,
`CategoryTheory/Monoidal/Braided/`, `CategoryTheory/Monoidal/Rigid/Braided.lean`), all
braided monoidal categories. Low severity, but a reader who re-runs the quoted command
gets a different answer than the file promises and may distrust the verdict.
**Bean `qou-l25z`.**

### F7. `QOU/Eightfold/ContactDistributionRank.lean:97-98`

> "Mathlib has **no exterior-power-of-an-object API** and **no differential forms on
> manifolds at all**, so every declaration below is about `ℕ`."

Half-right, and the half that is wrong is the load-bearing half for the file's own
route. Exterior powers **do** exist for modules (`⋀[R]^n M`, `LinearAlgebra/ExteriorPower/`)
and for `ModuleCat` — what is absent is `Λ^k` of an object in an *abstract monoidal
category*, which is the file's actual subject and should be said. "No differential forms
on manifolds" is correct as scoped but omits the normed-space layer (H2), which covers
the file's own `dim M = 3` model case. **Bean `qou-4tsl`.**

### F8. `docs/audits/2026-05-30-atom-braid-categorical-proof-feasibility.md:25`

> "Even Mathlib's `CoxeterSystem` order-accessor API is in flux."

Dated 2026-05-30. At this pin, `GroupTheory/Coxeter/` is **1612 lines across four
stable files** with the universal property (`lift`), `wordProd`, length and inversion
theory. The rest of that bullet ("no KLR algebras, no Hoefsmit, no Kashiwara crystals,
no Type-B folding") re-measures as correct. **Bean `qou-t88s`.**

---

## Appendix: `library/` coverage of the arc's topics

Re-measured 2026-09-04 over **576** document directories, both the `sections/` tier and
the `ocr/` tier that a `sections/`-only grep misses (case-sensitive
`grep -rl "<term>" library/*/sections/` and `library/*/ocr/`):

| topic | `sections/` docs | `ocr/` docs |
|---|---|---|
| dilogarithm | 822 | 30 |
| Kashaev | 454 | 21 |
| Hecke algebra | 381 | 17 |
| Thurston | 306 | 19 |
| volume conjecture | 214 | 7 |
| gluing equation | 188 | 0 |
| Bloch-Wigner | 135 | 0 |
| Markov trace | 128 | 0 |
| ideal tetrahedra | 116 | 7 |
| Neumann-Zagier | 88 | 3 |
| Temperley-Lieb | 72 | 2 |
| Lobachevsky | 46 | 2 |
| contact structure | 16 | 4 |
| Hodge star | 6 | 0 |

These run 10–40 % below the figures quoted in
`Eightfold/HyperbolicVolumeFormType.lean:157-162` (dilogarithm 849, Kashaev 548, volume
conjecture 381, Thurston 321, ideal tetrahedra 178). The method differs — that pass was
presumably case-insensitive and/or counted differently — and the **conclusion is
identical and unaffected**: the library is saturated with this material, and the
"`library/` holds nothing" claim the owner corrected was badly wrong. Recorded so the
two figures are not read as a contradiction. State your method when quoting either.

The two thin rows are the honest ones: **contact structure (16+4)** and **Hodge star
(6)** are the topics where the library genuinely is sparse, and they are the two the
original mistaken search actually used as its vocabulary.

---

## Beans filed by this audit

All parented to epic `qou-8lxd`. Every title was existence-checked against `.beans/`
before creation (`beans create` is not idempotent and dedupes on nothing).

| bean | tier | subject |
|---|---|---|
| `qou-tc8y` | BUILD | give `BlochWigner_unit_circle` its `Cl_2` body; resolve the FQN collision |
| `qou-ghc6` | BUILD | Lie-valued 1-forms on a normed space from `DifferentialForm`/`extDeriv` |
| `qou-jvua` | BUILD | differential `k`-forms on a manifold as `ContMDiffSection` |
| `qou-m8xt` | BUILD | retype `IdealTetrahedron` over `UpperHalfPlane` |
| `qou-sd8y` | BUILD | re-base `HyperbolicMetric.dH` on `Riemannian/PathELength` |
| `qou-vspi` | UPSTREAM | contact structures and contact forms |
| `qou-6eik` | FALSE | "UpperHalfPlane carries no Riemannian metric" — 2 sites |
| `qou-ipsl` | FALSE | `NonAbelianStokes.lean:10` credits Mathlib with manifold forms via `MFDeriv` |
| `qou-u4mx` | FALSE | `Cl_2` lemmas "awaiting Fourier-series infrastructure" |
| `qou-l25z` | STALE | `BraidGroup.lean:8` "no file matching `*braid*`" — four do |
| `qou-4tsl` | HALF-FALSE | "no exterior-power-of-an-object API" |
| `qou-t88s` | STALE | "`CoxeterSystem` order-accessor API is in flux" (2026-05-30) |

**Deliberately NOT beaned:**
* **HAVE items carrying no wrong claim** (H3, H7, H10) — nothing to act on.
* **UPSTREAM items already tracked** — U1 (dilogarithm), U2 (Iwahori–Hecke), U3 (braid
  groups), U4 (knot theory / TL / Markov trace), U6 (pivotal / ribbon / spherical),
  U7 (SDP duality, `qou-apcl`), U8 (hyperbolic 3-space, `qou-5gai`), U9 (RSK / Specht),
  U11 (Weierstrass ℘). Their existing beans are cited by title in §UPSTREAM.
* **U5** (Kazhdan–Lusztig), **U10** (quadrature), **U13** (Hodge star), **U14**
  (holonomy) — genuinely absent from Mathlib and with no *upstream* bean found, but all
  four are either low arc-relevance (U10, U13) or subsumed by a RESEARCH item that is
  already beaned (U5 by the in-repo `QOU/Mathlib/KazhdanLusztigBasis.lean` work; U14 by
  `qou-ewc4`). Filing four more would add noise, not signal. Named here so a later agent
  can pick any of them up.
* **RESEARCH items** R1-R5 — all already beaned (`qou-8mtd`, `qou-b84o`, `qou-ewc4`,
  `qou-brng`, and R5 in its own file header).
* **H6** — `MathlibExt/GramNondegenerate.lean` could reuse `Matrix.gram` for the
  `RCLike` case, but its claim is correct as scoped and nothing is wrong. Reuse
  opportunity, not a defect.

## Method notes

* Mathlib was grepped at `/home/user/qou/.lake/packages/mathlib/Mathlib`. The second
  copy under `content/quantum-observable-universe/lean/.lake/packages/mathlib` is the
  **same revision** (`git log -1 --format=%H` identical in both), so results transfer.
* `sorry`/`axiom`/`opaque` counts come from a comment-stripping scanner, not from
  `grep`. A raw `grep -c sorry` over the six audited directories returns 105, **all of
  it prose**; the true count is 0. Do not quote a raw grep for this.
* Every "Mathlib has no X" verdict above names the command that produced it. Where a
  command's result differs from what a corpus file claims the same command returns, the
  discrepancy is recorded rather than silently corrected (§F6 is the clearest case).
* **Not measured:** whether any Mathlib PR or issue exists for the UPSTREAM rows. This
  audit ran offline and did not browse. Every UPSTREAM row is *unchecked* on that axis.
* **Not measured:** whether any of the five `MathlibExt` SDP axioms or the Weierstrass
  axiom could be weakened to a conditional class rather than an axiom. That is a
  separate review and is not attempted here.
* No `.lean` file was edited. This session was read-only on Lean by instruction.
