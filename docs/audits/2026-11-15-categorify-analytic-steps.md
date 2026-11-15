# Analytic steps that can be isolated or made one instance of an algebraic class

Audit of `litlfred/qou` at main `d9b2b94a6` (2026-11-15). Read only: nothing in the repo was changed.

**Rule being applied (owner, 2026-11-15):** keep analysis in its own named propositions, and prove as much as possible algebraically or categorically.

**Model:** the Bloch–Wigner rigidity work (#7946, `/mnt/project-files/qou-bloch-rigidity/proof-sketch.md`). There, rigidity is stated against an abstract function sheaf with four axioms: Möbius pullback, ∂∂̄ = ∂̄∂, Cauchy–Riemann, and H⁰(ℙ¹, O(−1)) = 0. C^∞ and real-analytic functions are then instances. Other models: Bridge A (#7989, #7993, #7996), where Riemann–Hilbert is a hypothesis structure and Drinfeld–Kohno is a braided-monoidal class, and the Kummer/Čech H² work (#7969).

## How the search was done

- I counted Lean files under `lean/QOU/` that use analytic API: `Tendsto` 86, `HasDerivAt`/`deriv` 119, interval integrals 120, `ContDiff`/`Differentiable`/`Analytic*` 58, `MeasureTheory` 66, `Continuous` 124.
- I ranked files by density of analytic API, read the header of the top ~60, and grouped them by the mathematical step they perform.
- I also grepped the `.md` content blocks for named analytic tools. These had zero `.md` hits: Riemann–Hilbert, identity theorem, dominated convergence, Euler–Maclaurin, mean value theorem. So the analytic content of the corpus lives almost entirely in the Lean library, and in a few archimedean/knot blocks.
- **Limit of the search:** I did not read every proof body. A cluster's "analytic input" is taken from file headers and docstrings, which in this repo are detailed. Costs are my estimates, not measurements.

## Ranking

Ranked by payoff (how much analysis leaves the main line, and how much it reuses work already in flight), then by cost. Items 1–3 share one foundation with #7946. Item 5 is cheap and independent. Item 4 was withdrawn after checking its consumer (see the correction under item 4).

---

### 1. Dilogarithm functional equations as consequences of one "dilog theory" class

- **Where:**
  - `Archimedean/DilogReflection.lean` (`LiTwo_reflection'`, Euler reflection)
  - `MathlibExt/ComplexDilogarithmLanden.lean` (`hasDerivAt_landenCombo`)
  - `MathlibExt/ComplexDilogarithmInversion.lean`
  - `QBeta/FiveTwoAbelFiveTerm.lean` (Abel five-term for Rogers L on (0,1), bean `qou-abel`)
  - `QBeta/FiveTwoRogersReflection.lean`, `QBeta/FiveTwoComplexPentagon.lean`, `QBeta/FiveTwoFlattenedPentagon.lean`
  - `Knot/KummerDilogHalf.lean`
  - Blocks: `conj:dilogarithm-archimedean-limit`, and the "5-sum rule is an extended Bloch statement" bean `qou-xblo`.
- **Analytic input today:** each identity is proved the same way. Show that the combination has derivative 0 on an interval, conclude it is constant, then evaluate the constant by a one-sided limit. The headers themselves note that the derivative cancellation is linear ("the cancellation is linear", FiveTwoAbelFiveTerm).
- **Proposed structure:** a class `DilogTheory F A` (F a field, A an abelian group) consisting of L : F∖{0,1} → A satisfying the five-term relation, plus the two-term symmetries L(x) + L(1−x) = L(1) and L(1/x) = −L(x). That is, a homomorphism out of the Bloch group B(F).
  - Reflection, inversion and Landen are specialisations of the five-term relation, so they become ring manipulations that hold in every instance.
  - The **symbol test** decides which combinations are identities: Σ nᵢ (1−fᵢ) ∧ fᵢ = 0 in Λ²(F^×) ⊗ ℚ. This is algebra in the function field ℚ(x, y).
- **The one analytic proposition per instance:** the five-term relation for that instance (or the derivative-zero lemma it comes from).
- **Instances:**
  - Rogers L on (0,1) (already proved: `FiveTwoAbelFiveTerm`)
  - Bloch–Wigner D on ℂ∖{0,1} (#7946 uses exactly Suslin's five-term)
  - optional, both algebraic: the finite-field 1½-logarithm, and the p-adic dilogarithm
- **Precedent in the repo:** `FiveTwoLevelSevenLadder.lean` already takes `L : R → R` over a ring with the five-term relation as a hypothesis (`numerators_of_five_term`, `char_seven_forces`). So the pattern exists, and only the class is missing.
- **Cost:** medium, about 1 new file of algebra (specialisations) plus re-pointing about 5 files.
- **Risk:** low. The existing analytic proofs remain as the instance proofs.
- **Commits to:** one shared five-term orientation. #7946 found the corpus's `PentagonCoherent` uses the inverted orientation and forces D = 0, so the class must fix Suslin's orientation.

### 2. Ideal-tetrahedron volume = D(z) via rigidity instead of integration (T2)

- **Where:**
  - `Archimedean/MostowIdealTetVolume.lean` (T2, "closed modulo one relocated cited fact", chimney integral)
  - `Archimedean/TetVolAnalytic.lean` (the obtuse case via the identity theorem: analytic continuation off the acute region)
  - `Archimedean/OrthoschemeBaseIntegral.lean`, `Archimedean/OrthoschemePolarReduction.lean`, `Archimedean/HyperbolicVolumeFubini.lean`, `Archimedean/HyperbolicVolumeMeasure.lean`
  - `Archimedean/ObtuseTiling.lean`, `Archimedean/IdealTetObtuseReduction.lean`
- **Analytic input today:** an explicit volume integral over the chimney, Fubini and polar reduction, and an identity-theorem continuation for obtuse tetrahedra.
- **Proposed structure:** let V(z) be the volume of the ideal tetrahedron with cross-ratio z. Then:
  - (i) V is odd under conjugation and under z ↦ 1/z. This is geometric and algebraic.
  - (ii) V satisfies the five-term relation, because the 2–3 move is a decomposition of one polytope two ways. Only finite additivity and isometry invariance of the measure are used.
  - (iii) V is continuous.

  By the Bloch–Suslin rigidity theorem being built in #7946, V = c·D. The constant c is fixed by the regular tetrahedron (V = 3Λ(π/3) = D(e^{iπ/3})).
- **Analytic propositions left:**
  - continuity of V in z
  - finite additivity of hyperbolic volume
  - the rigidity theorem itself (shared with #7946)
- **What goes away:** the chimney integral, Fubini/polar reduction, and the obtuse analytic continuation. Acute and obtuse cases are handled uniformly.
- **Instances:** hyperbolic volume. Any isometry-invariant, finitely additive, continuous valuation on ideal tetrahedra is an instance; that is the scissors-congruence (Dehn–Sydler / Bloch group) reading.
- **Cost:** medium–high. It depends on #7946's rigidity reaching sorry-free (Stage U2 still needs Schwarz reflection and Laurent principal parts, which the sketch says are missing in Mathlib). The 2–3 move as a cross-ratio identity is cheap algebra.
- **Risk:** medium. If rigidity stalls, T2 stays where it is now; nothing is lost.
- **Commits to:** making #7946's rigidity load-bearing for the volume chain.

### 3. Faddeev–Volkov rigidity against a function sheaf on an elliptic curve

- **Where:**
  - `QBeta/CyclicDilogPentagon.lean` (`PentagonRigidity.uniqueUpToScalar`)
  - `QBeta/FaddeevRigidityReduction.lean`, `QBeta/FaddeevUniquenessBoundedCapstone.lean`, `QBeta/PhiBProdUniquenessAssembly.lean`
  - `Mathlib/FaddeevSolutionSet.lean`, `Mathlib/RigidityReductionScope.lean`
  - the PI scaffolds `Mathlib/ArgumentPrinciple.lean` (21 `sorry` mentions), `Mathlib/HadamardFactorization.lean` (10), `Mathlib/EllipticDivisorDegree.lean` (2)
  - Block: `quantum-observable-universes/q-dilogarithm-unique.md`
- **Analytic input today:** the ratio Ψ/Φ of two solutions is doubly periodic. Uniqueness then needs it to be constant: doubly-periodic Liouville, plus the strip-growth bound `hbdd`, or else the argument principle and elliptic divisor degree (PI-1..PI-3).
  - `FaddeevSolutionSet` proves the class `FaddeevPhi` has no regularity, so it is closed under multiplication by any bi-periodic function, even the lattice indicator.
  - `RigidityReductionScope` proves `hratio` is equivalent to the conclusion.
- **Proposed structure:** this is the same shape as #7946, with ℙ¹ replaced by an elliptic curve E = ℂ/Λ.
  - **Algebra:** the solutions of a rank-one difference system (two commuting shifts) form a torsor under the bi-shift-invariant sections.
  - **One axiom on the function sheaf:** global sections on the compact curve are constants, H⁰(E, O) = ℂ. This is the analogue of #7946's H⁰(ℙ¹, O(−1)) = 0.
  - FaddeevSolutionSet's negative result is then the statement that "all functions" is **not** an instance.
- **Instances:**
  - holomorphic functions (`MathlibExt/DoublyPeriodicLiouville.lean`, proved)
  - bounded meromorphic functions (`QBeta/BoundedMeromorphicLiouville.lean`, proved)
  - the algebraic function field of E, where "principal divisors have degree 0" is algebra
- **What goes away:** the argument-principle, Hadamard and divisor-degree scaffolds are no longer on the main line.
- **What stays:** the one analytic fact about the concrete Φ_b: that the ratio of two solutions is a section of the sheaf (today `hbdd`). **This item does not prove `hbdd`.** It relocates the analysis to one membership statement and removes the rest.
- **Cost:** medium (the torsor algebra is short; re-pointing the capstones is the bulk).
- **Risk:** low.
- **Commits to:** one shared "function sheaf on a compact curve" foundation with #7946.

### 4. Jucys–Murphy projectors at q = 1 — CORRECTED 2026-11-15: already isolated, not a candidate

**Correction (measured after the first version of this report).** The first version proposed replacing continuity by specialisation in a local ring. Reading `Mass/KohnoAssembly.lean` shows that the family consuming `JMProjectorContinuity` is the **KZ monodromy representation**, which depends analytically on the coupling. It is not an algebraic family, so there is no local ring to specialise in, and continuity is the natural input. The analytic content is already isolated in two lemmas (`continuousOn_projFamily`, `isIdempotentElem_projFamily`), and the algebra is already separate (`map_jmProjIn`). A related algebraic option, generalising `SeminormalRep` from `NotRootOfUnity` to a separation hypothesis that includes q = 1, would touch an 1800-line file and about 20 importers; it is not cheap and is not proposed here. Nothing else in this report depended on item 4. The original text follows for the record.

Original proposal:

- **Where:** `SchurWeyl/JMProjectorContinuity.lean` (`continuousOn_projFamily`, `isIdempotentElem_projFamily`), consumed by `Mass/KohnoAssembly.lean`, which is on the Drinfeld–Kohno / Bridge A4 line.
- **Analytic input today:**
  - idempotence at the non-generic point q = 1 uses continuity plus density of generic points
  - the rank comparison uses continuity of the family
- **Proposed structure:** the JM–Lagrange polynomial has coefficients in any commutative ring where the differences of the q²-integers [d]_{q²} (|d| ≤ n) are units. Take the local ring of ℤ[q, q⁻¹] at the point, or any such ring.
  - Idempotence and orthogonality are polynomial identities there.
  - The value at q = 1 is the image under the evaluation ring map.
  - No topology or density is needed.
- **Instances:** continuous real/complex families (recovered as a corollary), the formal (q−1)-adic family, and specialisation to finite fields wherever the units condition holds.
- **Cost:** low (one file).
- **Risk:** low.
- **Commits to:** nothing beyond the file. It strengthens Bridge A4.

### 5. Vanishing order and stationarity at q = 1 as algebra: a valuation plus one shared bar involution

- **Where:**
  - `QBeta/BarEvenForcesStationarity.lean` (bar-even ⇒ z′(1) = 0)
  - `Braiding/WeakVertexCouplingNormalisationArchimedean.lean` (`hasDerivAt_sSq_one`, `hasDerivAt_weakVertexTrace_one`, vanishing orders)
  - `QBeta/PhaseFailsLogFunctionalEquation.lean`
  - about 12 files that compute a derivative at q = 1
- **Analytic input today:** `HasDerivAt` at q = 1 over ℝ.
- **Proposed structure:**
  - The objects are rational functions or Laurent polynomials, so "vanishes to order k at q = 1" is the (q−1)-adic valuation on ℚ(q). That valuation exists over any field.
  - Bar-even ⇒ stationary is the statement that for the derivation D = q d/dq and the bar involution ι, D ∘ ι = −ι ∘ D, so at the fixed point q = 1 a bar-even element has D f(1) = 0.
  - Real `HasDerivAt` becomes the instance.
- **Sibling input (Bloch-rigidity thread, 21:03Z):**
  - `BarInvolution` is defined four separate times: `SelectionRules.lean:59`, `KazhdanLusztigBasis.lean:73`, `ThetaQcdFramingCp.lean:73` (class), and `Mathlib/BarGradedCollapse.lean:62`.
  - There are also `HodgeInvolution`, `CatHodgeInvolution`, `DescentInvolution` and `Involution` (SelfDualSES).
  - `Glossary.lean`'s `KahlerDifferentials` is a bare stub, while Mathlib has `Derivation` and `KaehlerDifferential`.
  - Item 5 is the natural place to unify these: one involution structure, and Mathlib's `Derivation` as the differential.
- **Cost:** low for the valuation lemma. Unifying the four `BarInvolution`s is a refactor, so per AGENTS.md "ask first" it needs your go separately.
- **Risk:** low for the lemma. For the refactor, about 4 files plus their importers.

### 6. Beltrami ⇒ steady Euler in an abstract Cartan calculus

- **Where:** `FluidDynamics/BeltramiSteadyEuler.lean` (Parts A–C); blocks `fluid-dynamics/reeb-beltrami-regular-flow.md`, `fluid-dynamics/core-levi-form.md`.
- **Analytic input today:** the Lamb identity (u·∇)u = ∇(|u|²/2) − u × curl u, proved in coordinates with `deriv` (Part A), and again by hand on the ABC flow (Part B).
- **Proposed structure:** the Lamb identity is the Cartan/Koszul identity ∇_u u♭ = ι_u du♭ + ½ d|u|². It holds in any metric Lie algebroid, or in any differential calculus with a Levi-Civita connection.
  - Beltrami (du♭ = λ ⋆u♭) then gives steady Euler by algebra.
  - Part C (left-invariant fields on sl₂) is already pure Lie algebra and would become an instance rather than a separate computation.
- **Instances:** ℝ³ in coordinates, T³ (ABC), and the sl₂ / Γ\PSL₂(ℝ) Reeb model.
- **Cost:** medium–low.
- **Risk:** low.
- **Commits to:** nothing outside fluid dynamics.

### 7. Resurgence: the Borel transform as an algebra isomorphism and the Stokes jump as an automorphism

- **Where:**
  - `Mathlib/BorelLaplace.lean`, `Mathlib/BorelResummation.lean`, `Mathlib/QGevreyOrder.lean`
  - `QBeta/PhiBProdFactorAnalytic.lean`, `QBeta/MonodromyDatumRigidity.lean` (Stokes jump as ratio of continuations)
  - `QBeta/FiveTwoStokesMatrixIdentities.lean`
  - Blocks: `appendix-surreals/borel-partial-resolution.md`
- **Analytic input today:** Laplace integrals, and Gevrey bounds giving convergence of the Borel transform.
- **Proposed structure:**
  - The Borel transform x^{n+1} ↦ ξⁿ/n! is a ring isomorphism from (x·ℂ[[x]], ·) to (ℂ[[ξ]], convolution). This is formal and algebraic.
  - Gevrey-s series form a differential subalgebra.
  - A resummation is a class: a differential-algebra morphism from Gevrey-1 series to germs in a function sheaf that restricts to the identity on convergent series.
  - Stokes automorphisms are then algebra automorphisms (ratios of two instances), so "alien derivations are derivations" becomes algebra.
  - The `MonodromyDatumRigidity` claim that the datum is scale-invariant follows from the automorphism property.
- **Instances:** Borel–Laplace in each non-singular direction θ (analytic). The convergent case is trivial.
- **Cost:** medium–high.
- **Risk:** medium; Écalle's theory is large, so scope it to the rank-one Φ_b case.

### 8. Volume-conjecture squeezes: one Laplace principle, algebraic per-knot data

- **Where:**
  - `Knot/BorromeanVolume.lean`, `Knot/WhiteheadChainVolume.lean`, `Knot/WhiteheadMajorantRate.lean`, `Knot/FigureEightVolumeSqueeze.lean`
  - `Knot/LogSine*.lean`, `Knot/EulerMaclaurinFirst.lean`
  - `MathlibExt/ExponentialGrowthRate.lean` (already isolates the growth-rate step)
  - the `qou-mlgp` / `qou-0yqu` bean family
- **Analytic input today:** for each knot, a Riemann sum of log|2 sin| converging to a Clausen integral, plus a squeeze.
- **Proposed structure:** one class `LaplacePrinciple`: (1/N) log Σ_k exp(N g_N(k/N)) → max g, for positive sums with uniform convergence of g_N.
  - Per knot, what remains is algebraic: the state-sum combinatorics, the critical point from the gluing equation, and the value as a Bloch element (feeding item 1).
  - The 4₁, Borromean and Whitehead squeezes become instances.
- **Cost:** high (the uniform hypotheses differ per knot).
- **Risk:** medium.
- **Payoff:** the next knot costs one algebraic file instead of a squeeze arc.

### 9. Hyperbolic distance from the hyperboloid bilinear form

- **Where:** `Archimedean/HyperbolicMetric.lean`, `Archimedean/HyperbolicGeodesicZAxisUniqueness.lean`, `Archimedean/HyperbolicMetricSeparation.lean`.
- **Analytic input today:** dH is defined as an infimum of path-length integrals. Symmetry, separation and z-axis geodesic uniqueness are proved via FTC and its equality case.
- **Proposed structure:** in the Minkowski model, cosh d(x, y) = −⟨x, y⟩.
  - Symmetry, the isometry group SO⁺(1,3), and the fact that geodesics are plane sections all become linear algebra (reverse Cauchy–Schwarz).
  - One analytic proposition remains: the infimum of path lengths equals arcosh(−⟨x, y⟩).
- **Cost:** medium–high.
- **Payoff:** medium. It is only needed if item 2 is not taken, since item 2 bypasses the metric for volume.

### 10. Drinfeld associator class (route to the Bridge A4 thread rather than a new one)

- **Where:** `KZ/KZHalfMonodromy.lean`, `KZ/KZHexagon.lean`, `KZ/KZ4.lean`, `KZ/KZCorner.lean`, `KZ/FuchsianParam.lean`, `Mass/KZHolonomy/*`.
- **Analytic input today:** solving Fuchsian ODEs, normalising at punctures, and half-monodromy via log branches.
- **Proposed structure:** an associator is a group-like Φ in the completed free algebra satisfying the pentagon and the hexagons. Everything braided follows algebraically from it (Drinfeld). Φ_KZ is one instance, proved by the existing analytic files; rational associators are others.
- **Cost:** high.
- **Overlap:** strong with #7993 (`BraidedMonodromy`). I recommend handing this to that thread, not opening a new one.

### 11. The q → 1 dilogarithm limit (Part A) as a formal expansion

- **Where:** `Archimedean/DilogPartAConvergence.lean`, `Archimedean/DilogPartARiemannSum.lean`, `Archimedean/DilogarithmArchimedeanLimit.lean`, `MathlibExt/CorrectedTrapezoid.lean`, `MathlibExt/TrapezoidRule.lean`, `Knot/EulerMaclaurinFirst.lean`.
- **Proposed structure:**
  - log(x; q)_∞ has the expansion Σ Bₙ ħ^{n−1} Li_{2−n}(x)/n! in ħ = log q. The coefficients come from the Todd operator D/(e^D − 1), which is an identity in a ring of formal difference operators.
  - "Is an asymptotic expansion" is the one analytic class.
  - Euler–Maclaurin's algebraic core is then shared by items 8 and 11.
- **Cost:** medium.
- **Not covered:** Part B (the branch-point limit, bean `qou-jplv`) is genuine analytic number theory and is not a candidate.

---

## Already isolated, or genuinely analytic: leave as they are

- **`MathlibExt/FrechetShohat.lean`, `Archimedean/BalancedKernel*`:** moment determinacy is already a hypothesis class, and the moments are already algebraic.
- **`Mass/KZHolonomy/LinearODE.lean`:** already stated for any complete normed algebra. It is the instance side of a Riemann–Hilbert-type class, not main-line analysis.
- **`Knot/Clausen.lean`, `Archimedean/Lob*.lean`, `MathlibExt/ComplexDilogarithm*.lean` (definitions and derivatives):** these are the instance side of item 1 and stay.
- **`MathlibExt/TaylorRemainder.lean`, `MathlibExt/CorrectedTrapezoid.lean`, `Mathlib/WeierstrassFactorEstimate.lean`:** Mathlib-gap tooling. They become optional if items 3 and 11 are taken.
- **`Archimedean/IdealTetrahedronVolumeConcavity.lean`, `Knot/RivinConcavity.lean`:** concavity is genuinely real-analytic, and the Hessian sign is already the algebraic part.
- **`MobiusRegulator.lean`:** elementary integrals, already framed as a regulator-scheme datum.
- **`Archimedean/DilogPartB*`:** an open Diophantine limit; not a categorification target.
- **Content blocks on Haar / Frobenius integration** (`quantum-observable-universes/frobenius-integration.md` and siblings): already categorical. The integral is the Frobenius/Hopf integral, and `Torsion/MassTraceIdentity.lean` proves it over any braided monoidal category.

## Cross-cutting foundation (if items 1–3 or 5 are taken)

One shared file would carry:
- a function sheaf with Möbius pullback
- a Mathlib `Derivation` with a complex structure J (as the Bloch thread proposes)
- one involution structure
- the compact-curve axiom: H⁰ = constants on E, and H⁰(ℙ¹, O(−1)) = 0

#7946 and items 1, 2, 3 and 5 would all instantiate it. Without it, each item would re-declare its own axioms, which is how the four `BarInvolution` copies arose.


## Status after the owner's pick (2026-11-15, "both groups in parallel")

Built on branch `claude/categorify-analytic-steps-2026-11-15`. All sorry-free, axioms `propext, Classical.choice, Quot.sound`, `lean`-direct exit 0:
- Item 5: `QBeta/BarEvenJet.lean` (generic, plus a Laurent-polynomial instance) and `QBeta/BarEvenJetArchimedean.lean` (the real instance).
- Item 1: `QBeta/DilogTheory.lean` (Rogers and Suslin classes) and `QBeta/DilogTheoryArchimedean.lean` (the `rogers` instance).
- Item 3: `QBeta/FaddeevCompactCurve.lean` (the compact-curve class, `ratio_const`, and the entire instance).

Added after #7946's rigidity theorem landed (21:21Z). The branch merges #7946's branch:
- Item 1, Part B: `blochWigner : SuslinDilogTheory ℂ ℝ`, and `SuslinDilogTheory.eq_mul_blochWigner`, which says every continuous, conjugation-odd instance over ℂ is c·D. Reflection oddness D(1−z) = −D(z) is now proved (`FiveTermProof.blochD_one_sub`, commit 3cbbacd09a), so `blochWigner_anharmonic` holds unconditionally. `reflection_of_continuous` extends it to every continuous conjugation-odd instance.
- Item 2: `Archimedean/IdealTetVolumeRigidity.lean`. Continuity, the Bloch–Wigner symmetries and the five-term (2–3 move) relation give V = (V(i)/D(i))·D on ℂ∖{0,1}, for acute and obtuse shapes alike. These three geometric inputs are hypotheses, not yet proved for the Lean hyperbolic volume. They are the remaining work on this route.
- Item 4 was withdrawn (see the correction above).
