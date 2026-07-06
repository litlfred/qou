# Stub triage — trivial `: True` siblings + `proof-no-placeholder-stub` QA fails (2026-07-02)

Four-agent read-only triage over the 65 blocks flagged by
[`docs/audits/2026-07-02-lean-proof-progress-qa-table.md`](2026-07-02-lean-proof-progress-qa-table.md)
(20 trivial-stub provable siblings + 48 `proof-no-placeholder-stub` sidecar
fails). Verdicts follow AGENTS.md §1a honest dispositions + the 2026-06-14
no-shadowing STRICT rule. Branch: `claude/lean-proof-progress-table-gchfqu`
(PR #3222). Beans: `qsb2` (apply), `qsb3` (sidecar refresh).

## Headline

Every `proof-no-placeholder-stub` fail entry dates from one heuristic batch
review (**2026-06-22T02:50Z**, commit `b4ea0407`), and every flagged `.lean`
was rewritten afterwards (mostly the 2026-06-30 honest-disposition pass,
commit `9001bfe5`, plus this branch's 2026-07-02 `-- Ref:` additions). All
sidecar `field_hash.lean` values have drifted — the criterion's detector
(literal `placeholder stub` marker, `lean-vacuity-axiom-audit.ts:1132`)
no longer fires on any current file. So the criterion itself is **stale on
all 48**; the residual issues found are `proof-statement-integrity`-class
(self-assuming projections), not placeholder stubs.

## Aggregate verdicts

| Verdict | Count | Remedy |
|---|--:|---|
| ALREADY-HONEST — stale sidecar | 29 | `qa-sweep --only proof-no-placeholder-stub` refresh (bean `qsb3`) |
| SHADOW-STUB-DELETE | 19 | delete trivial sibling `.lean`; `lean.ref` resolves to the real library decl (applied on this branch) |
| Self-assuming projection (§3b-cond item-5) residuals | 13 | restructure class to carry hypotheses, derive conclusion (bean `qsb2`) |
| NEEDS-REAL-STATEMENT | 6 | state the real proposition + cited `sorry` (bean `qsb2`) |
| NEEDS-PROOF (genuinely provable) | 1 | `prop:transfer-matrix-identities` — explicit 2×2 matrix identities over `ℤ[q^±1]`, provable by `Matrix.ext` + `field_simp; ring` |
| DEMOTE-TO-CONJECTURE | 0 | — |

## Shadow-stubs deleted (19)

All were `theorem <name> : True := trivial` (or equivalent) siblings whose
block `lean.ref` resolves to a real library formalization once the sibling
stops shadowing candidate-2/grep-fallback resolution:

| Sibling stub (chapter/stem) | Real formalization |
|---|---|
| particle-interactions/confinement-lp | `lean/QOU/Interactions/ConfinementLP.lean:92` (sorry-free) |
| particle-interactions/confinement-topological | `lean/QOU/Interactions/GramIndefinite.lean:180` (cited sorry) |
| observations/flavor-split-substrate | `lean/QOU/HadronicMass.lean:742` (sorry-free, norm_num CODATA bound) |
| mass-endomorphism/gb-spectral-sequence | `lean/QOU/BraidKnot/GBSpectralSequence.lean:74` (proved conditional-class) |
| mass-endomorphism/q-hecke-seminormal-character-closure | `lean/QOU/BraidKnot/QHeckeSeminormalCharacterClosure.lean:33` (projection — secondary fix in qsb2) |
| fluid-dynamics/observability-q-independent | `lean/QOU/GaugeFieldFluidDynamics.lean:763` (sorry-free; mis-named file, grep-fallback) |
| information-theory/horizon-conformal-invariance | `lean/QOU/JetHorizon.lean:211` |
| information-theory/qou-is-ccc | `lean/QOU/JetHorizon.lean:250` |
| q-geometric-langlands/cyclotomic-l-value-decomposition | `lean/QOU/BraidKnot/CyclotomicLValueDecomposition.lean:44` (proved) |
| q-geometric-langlands/q-hecke-eigenvalue | `lean/QOU/QGeometricLanglands.lean:286` (§3b-cond derivation) |
| stochastic-mechanics/joint-galois-braid-discharged | `lean/QOU/AlgebraicSubstrate/JointGaloisBraidDischarged.lean:37` |
| stochastic-mechanics/joint-galois-braid-figure-8-verified | `lean/QOU/AlgebraicSubstrate/JointGaloisBraidFigure8.lean:38` |
| stochastic-mechanics/two-filtration-bridge-small-cases | `lean/QOU/AlgebraicSubstrate/TwoFiltrationBridgeSmallCases.lean:38` |
| braids-and-knots/trace-locality-meets-gs-nonlocality | `lean/QOU/Observations/TraceLocalityMeetsGsNonLocality.lean:34` (content-bearing class) |
| appendix-surreals/b1-figure-8-row-theorem | `lean/QOU/AppendixSurreals/B1Figure8RowTheorem.lean:30` |
| appendix-surreals/b1-soft-sharpness-theorem | `lean/QOU/AppendixSurreals/B1SoftSharpnessTheorem.lean:36` |
| appendix-surreals/b1-torus-knot-rows-theorem | `lean/QOU/AppendixSurreals/B1TorusKnotRowsTheorem.lean:35` |
| appendix-surreals/borel-partial-resolution | `lean/QOU/AppendixSurreals/BorelPartialResolution.lean:19` (proved by rfl) |
| appendix-surreals/depth-2-identification-bloch-suslin | `lean/QOU/AppendixSurreals/Depth2IdentificationBlochSuslin.lean:36` |

NOT deleted: `mass-endomorphism/hecke-baer-star-generic.lean` — the sibling
is substantive (BaerStarRing class, 2 cited axioms, proved sketch theorem);
its trivial flag is a stray `example : True := trivial` and the ref'd
library decl is itself a projection. Queued in qsb2 as an M-effort fix.

## Residual dishonesty worklist (bean `qsb2`)

**NEEDS-REAL-STATEMENT (6):** `lem:mobius-energy-frobenius-kernel`,
`lem:nsi-q-deformed-kernel`, `thm:q-ns-wellposedness` (worst — class field
`wellposed_active` IS the conclusion), `prop:q-turbulence-spectrum`,
`lem:skein-mass-from-linking`, `lem:tmli-constituent-composite-agreement`.

**NEEDS-PROOF (1):** `prop:transfer-matrix-identities` — the matrices are
explicit in `beta-decay-transfer-matrix.md` (`T(c,d) = [[c(q−q⁻¹)+d, c],[c, d]]`);
identities (i) `T_pp·T_nn = 1` and (ii) `T_pn² = ([2]_q²/4)·1` are concrete
`M₂` computations.

**Projection residuals (13):** `prop:demand-stability`,
`prop:confinement-universality`, `prop:brane-tower-q-laplacian-decay`,
`prop:q-plancherel-asymptotic-skeleton`, `prop:strangelet-crossing-energy`,
`prop:substrate-consistency-window` (near-tautological window encoding),
`prop:shell-filling-rule` (the exact `holds:Prop + impl_*` anti-pattern),
`lem:fai-projector-coadjoint-orbit` (genuinely provable over
`Matrix (Fin 2) ℝ`), `prop:observation-energy` (def-not-theorem),
`prop:q-gl-obstruction-calc` (arithmetic core already PROVED in
`QGeometricLanglands.lean:304–384` — re-point or compose),
`lem:tm-transient-localisation` (over-quantified — add the
`h_disjoint_factorisation` hypothesis), `lem:feynman-markov-identification`
(hypothesis ≡ conclusion in clause (ii)),
`prop:hecke-baer-star-generic` (stray example + library projection).
Worked exemplars of the target shape: the molecular-construction quartet
(`h2/ch4/co2-lp-dual-binding`, `benzene-threading-emergence`) and
`prop:sdp-regime-switch` ("Disposition (derived, not projected)").

## Stale-sidecar refresh list (bean `qsb3`, 29 blocks)

brings-surface: brings-euler-characteristic, brings-riemann-hurwitz.
mass-endomorphism: topological-mass-cat-descended, -cat-transient,
-dilogarithm, -holonomy. mass-theory: geom-yekutieli-alignment,
ground-state-ordering, hook-weight-derivation, mass-categorical-descent.
particle-interactions: atomic-nf-witness, confinement-frobenius-reciprocity,
four-term-pair-nucleon, frobenius-positivity-filter, inductive-gb-reduction,
lp-dual-stability, neutron-qvalue-symbolic, nucleon-ordering-factorization,
parity-regime-selection, positron-correction, tritium-qvalue-symbolic.
observations: centered-hecke-variance-positive, pair-skein-mass-formula,
sdp-regime-switch. molecular-construction: benzene-threading-emergence,
ch4-lp-dual-binding, co2-lp-dual-binding, h2-lp-dual-binding.
information-theory: reeb-operations-per-planck.

(The remaining flagged blocks also carry hash-drifted sidecars; the
projection residuals above should be fixed *before* their sidecars are
refreshed so the sweep re-reviews the corrected Lean.)

## Critical-distance note

Several "honest" verdicts are honest *in form*: context classes such as
`TritiumQvalueContext.qvalue_branching` and `BorromeanQuark.qvalue_ansatz`
put the physically load-bearing ansatz in the hypothesis class, so the
sorry-free theorems verify algebra downstream of an unproved ansatz — valid
under §3b-cond, but the proved mathematical content is thinner than the
block titles suggest.
