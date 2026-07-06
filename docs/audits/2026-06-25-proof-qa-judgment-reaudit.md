# Proof-QA judgment + rater re-audit (follow-up to PR #2775)

**Date:** 2026-06-25 · **Branch:** `claude/proof-qa-judgment-reaudit-2026-06-25` · **Predecessor:** [PR #2775](https://github.com/litlfred/qou/pull/2775) (merged `db52522`)

PR #2775 drained the deterministic proof-QA false positives and **invalidated** the 1,680 unreliable 2026-06-22 `qa-agent-drain` judgment + rater verdicts → `n/a` *pending canonical re-sweep*. The canonical `qa-sweep` (folio-assistant) is out of session scope (403), so this PR performs the per-block agent re-audit directly: each of the **360 blocks** was read (`.md` claim + resolved Lean) by a sub-agent that recorded an **evidence-cited** verdict per criterion via [`scripts/reaudit_verdict.py`](../../scripts/reaudit_verdict.py), superseding the placeholder.

## Final verdict distribution (all 360 re-audited)

| criterion | pass | fail | warn | n/a |
|---|--:|--:|--:|--:|
| proof-statement-integrity | 111 | 129 | 0 | 11 |
| proof-no-self-assuming-projection | 80 | 88 | 0 | 17 |
| proof-no-unused-hypotheses | 228 | 12 | 0 | 11 |
| proof-no-false-premise | 239 | 2 | 0 | 11 |
| proof-rater-goal-plausibility | 333 | 0 | 11 | 10 |
| proof-rater-strategy-clarity | 153 | 0 | 93 | 5 |
| proof-rater-novelty | 186 | 0 | 60 | 5 |

**144 distinct blocks carry a genuine judgment fail** — real formalization debt. The dominant defect is the **context-class self-assuming projection** (a `class …Context` whose fields *are* the manuscript conclusions, with `theorem foo := ⟨ctx.claim_i, …⟩` projecting them — AGENTS.md §3b-cond rule-5), alongside degenerate `Nonempty`/`: True` weakenings, bespoke `axiom`s restating the claim, and bare/uncited `sorry`. The 2026-06-22 batch often had the right *verdict* for the wrong (templated) *reason*; verdicts are now evidence-cited per block.

### Rubric

| criterion | PASS | FAIL |
|---|---|---|
| statement-integrity | Lean faithfully encodes the `.md` claim; no `sorry`/`admit`/`native_decide` masking; no degenerate weakening | proves weaker/different (`Nonempty` via trivial instance, `: True`, projection); `sorry`/unexpected axioms |
| no-self-assuming-projection | derives the conclusion | returns a hypothesis/structure field that *is* the conclusion |
| no-unused-hypotheses | every binder used | a hypothesis/`[instance]` binder never referenced |
| no-false-premise | premises satisfiable | a premise contradictory ⇒ vacuously true |
| rater-{goal-plausibility,strategy-clarity,novelty} | score ≥ 0.66 | score < 0.66 ⇒ `warn` |

`n/a` when no Lean resolves. A fresh Opus re-audit is **not more authoritative** than the canonical checker — best-effort interim until `folio-assistant`'s `qa-sweep` runs. All verdicts reversible via git.

### Notable non-verdict findings (flagged for author)

- `p3-blowup-yekutieli.lean` — `class BlowupYekutieli` declared **twice** (stray `-- Ref:` between bodies) → won't compile.
- `terms-2-6-higher-operations` — Lean fields **contradict** the `.md` (which refutes the cup-product / tower route).
- `q-gl-obstruction-calc` — `.md` says intrinsic curvature non-zero; Lean field asserts `F_intr = 0` (mismatch).
- `conj:borromean-baryon-mass-formula` — headline uses the **purged** `λ_scale·Vol(𝓑₃)/ℏ_q²` construct (mass-formula guardrail).
- `cor:knot-factor-amphicheiral` — encodes the empirically-refuted `a = 1−h²` (false on 4₁) ⇒ false-premise.
- `prop:shell-filling-rule` — `ShellFillingRuleContext` is **uninhabitable** (a class field forces `∀ other:ℕ, other ≤ singly_occupied`).
- several `axiom`-masked theorems (`q-exponential-taylor`, `markov-trace-antipode`, `wigner-coefficient-derivation`, `hecke-markov-transition`'s unsound `totalTrace`).

## Genuine judgment fails — catalogue (144 blocks)

| block | failing criteria |
|---|---|
| `cor:descartes-knot-eigenbasis` | statement-integrity |
| `cor:habiro-expansion-atomic` | statement-integrity |
| `cor:knot-factor-amphicheiral` | false-premise, statement-integrity, unused-hypotheses |
| `cor:lr-tensor-character-bridge` | statement-integrity, unused-hypotheses |
| `lem:bond-order-eq-jet-degree` | statement-integrity |
| `lem:brings-euler-characteristic` | self-assuming-projection, statement-integrity |
| `lem:brings-riemann-hurwitz` | self-assuming-projection, statement-integrity |
| `lem:chebyshev-degree-genus` | statement-integrity |
| `lem:fai-projector-coadjoint-orbit` | self-assuming-projection, statement-integrity |
| `lem:feynman-markov-identification` | self-assuming-projection, statement-integrity |
| `lem:mobius-energy-frobenius-kernel` | self-assuming-projection, statement-integrity |
| `lem:nsi-q-deformed-kernel` | self-assuming-projection, statement-integrity |
| `lem:pair-skein-mass-formula` | self-assuming-projection, statement-integrity |
| `lem:skein-mass-from-linking` | self-assuming-projection, statement-integrity |
| `lem:su2-emergence-dagger-unitarity` | self-assuming-projection, statement-integrity |
| `lem:su2-emergence-volume-determinant` | self-assuming-projection, statement-integrity |
| `lem:tmli-constituent-composite-agreement` | self-assuming-projection, statement-integrity |
| `lem:topological-mass-cat-descended` | self-assuming-projection, statement-integrity |
| `lem:topological-mass-cat-eigenspace` | self-assuming-projection, statement-integrity |
| `lem:topological-mass-cat-transient` | self-assuming-projection, statement-integrity |
| `lem:topological-mass-dilogarithm` | self-assuming-projection, statement-integrity |
| `lem:topological-mass-holonomy` | self-assuming-projection, statement-integrity |
| `lem:topological-mass-transient-localisation` | self-assuming-projection, statement-integrity |
| `lem:yekutieli-leading-coefficient` | self-assuming-projection, statement-integrity |
| `prop:algebraic-gns-embedding` | statement-integrity |
| `prop:alpha-shift-torus-knot` | self-assuming-projection |
| `prop:atomic-lp-stability` | self-assuming-projection, statement-integrity |
| `prop:benzene-threading-emergence` | self-assuming-projection, statement-integrity |
| `prop:binding-genfun-qdifference` | statement-integrity |
| `prop:blowup-yekutieli` | statement-integrity |
| `prop:borromean-h4-categorical-derivation` | statement-integrity |
| `prop:borromean-hopf-energy-crossover` | statement-integrity |
| `prop:brane-tower-q-laplacian-decay` | self-assuming-projection, statement-integrity |
| `prop:centered-hecke-variance-positive` | self-assuming-projection |
| `prop:ch4-lp-dual-binding` | self-assuming-projection, statement-integrity |
| `prop:chi-lambda-w0-sign-weighting` | statement-integrity |
| `prop:chirality-from-frobenius-self-pairing` | self-assuming-projection, statement-integrity |
| `prop:co-lp-dual-binding` | self-assuming-projection, statement-integrity |
| `prop:co2-lp-dual-binding` | self-assuming-projection, statement-integrity |
| `prop:confined-knot-binding` | self-assuming-projection, statement-integrity |
| `prop:confinement-categorical` | statement-integrity, unused-hypotheses |
| `prop:confinement-frobenius-reciprocity` | self-assuming-projection, statement-integrity |
| `prop:confinement-operator-selection` | self-assuming-projection |
| `prop:confinement-phase-stratification` | self-assuming-projection, statement-integrity |
| `prop:confinement-sdp` | statement-integrity |
| `prop:confinement-universality` | self-assuming-projection |
| `prop:corrected-markov-trace` | self-assuming-projection, statement-integrity |
| `prop:crystal-basis-resolves-mass-tower-open-problems` | statement-integrity |
| `prop:demand-stability` | self-assuming-projection, statement-integrity |
| `prop:double-slit-massive-pattern` | statement-integrity |
| `prop:e-infinity-page-identifications` | self-assuming-projection, statement-integrity |
| `prop:explicit-central-idempotent` | statement-integrity, unused-hypotheses |
| `prop:fiber-adjoint-involution` | statement-integrity |
| `prop:fibre-functor-atlas` | self-assuming-projection, statement-integrity |
| `prop:force-carrier-intertwining-correspondence` | statement-integrity, unused-hypotheses |
| `prop:four-term-pair-nucleon` | self-assuming-projection, statement-integrity |
| `prop:frobenius-pairing-exists` | statement-integrity |
| `prop:frobenius-positivity-filter` | self-assuming-projection, statement-integrity |
| `prop:graded-markov-trace-from-gs-filtration` | self-assuming-projection, statement-integrity |
| `prop:gram-determinant-plancherel-ratio` | statement-integrity |
| `prop:ground-state-ordering` | self-assuming-projection, statement-integrity |
| `prop:h2-lp-dual-binding` | self-assuming-projection, statement-integrity |
| `prop:hecke-markov-transition` | statement-integrity |
| `prop:hecke-satisfies-blitvic-hypothesis` | self-assuming-projection, statement-integrity, unused-hypotheses |
| `prop:hoefsmit-V21-cos-symmetrization` | unused-hypotheses |
| `prop:hook-weight-derivation` | self-assuming-projection, statement-integrity |
| `prop:ilp-covalent-bond` | statement-integrity |
| `prop:inductive-gb-reduction` | self-assuming-projection, statement-integrity |
| `prop:jet-prefix-gb-filtration` | self-assuming-projection, statement-integrity |
| `prop:jet-sw-tau-decomposition` | statement-integrity |
| `prop:jucys-murphy-central-elements-qou` | self-assuming-projection, statement-integrity |
| `prop:knot-factor-spectral-form` | statement-integrity |
| `prop:knot-operator-selection` | self-assuming-projection, statement-integrity |
| `prop:lp-dual-stability` | self-assuming-projection, statement-integrity |
| `prop:lr-coefficient-hecke` | statement-integrity |
| `prop:magic-A-binding-formula` | statement-integrity |
| `prop:markov-trace-antipode-polynomial-symmetry` | statement-integrity |
| `prop:markov-trace-frobenius-selection` | statement-integrity, unused-hypotheses |
| `prop:mass-categorical-descent` | self-assuming-projection, statement-integrity |
| `prop:mass-endomorphism-tower` | statement-integrity |
| `prop:meson-scale-independence` | statement-integrity |
| `prop:metallic-character-knot` | self-assuming-projection, statement-integrity |
| `prop:neutron-proton-splitting` | self-assuming-projection, statement-integrity |
| `prop:neutron-qvalue-symbolic` | self-assuming-projection |
| `prop:noble-gas-characterization` | self-assuming-projection, statement-integrity |
| `prop:nuclear-operator-regimes` | statement-integrity |
| `prop:nucleon-ordering-factorization` | self-assuming-projection |
| `prop:observation-energy` | self-assuming-projection, statement-integrity |
| `prop:operator-selection-lp` | self-assuming-projection, statement-integrity |
| `prop:p-bandwidth-bound` | self-assuming-projection, statement-integrity |
| `prop:partition-sum-proton-residual` | statement-integrity |
| `prop:per-nucleon-shift-additive-linearity` | self-assuming-projection, statement-integrity |
| `prop:phi-q-aj-machinery-identification` | self-assuming-projection, statement-integrity |
| `prop:photon-threading-mass` | self-assuming-projection, statement-integrity |
| `prop:physical-units-gap-linear` | statement-integrity |
| `prop:positive-definite-dagger` | self-assuming-projection, statement-integrity |
| `prop:positron-correction` | self-assuming-projection |
| `prop:q-codifferential-formula` | statement-integrity |
| `prop:q-exponential-taylor` | statement-integrity |
| `prop:q-game-of-life` | statement-integrity |
| `prop:q-gl-obstruction-calc` | self-assuming-projection, statement-integrity |
| `prop:q-plancherel-asymptotic-skeleton` | self-assuming-projection, statement-integrity |
| `prop:q-turbulence-spectrum` | self-assuming-projection, statement-integrity |
| `prop:qbeta-c-k-closed-forms` | statement-integrity |
| `prop:qbeta-delta-tau-surrogate-taylor-coefficients` | statement-integrity |
| `prop:quantum-observable-universe-exists` | statement-integrity |
| `prop:quantum-universe-exists` | statement-integrity |
| `prop:reeb-operations-per-planck` | self-assuming-projection, statement-integrity |
| `prop:rigid-monoidal-structural-gap-invariance` | unused-hypotheses |
| `prop:sdp-regime-switch` | self-assuming-projection, statement-integrity |
| `prop:shell-closure-stability` | self-assuming-projection |
| `prop:shell-filling-rule` | false-premise, statement-integrity |
| `prop:six-term-per-derivation-weights` | self-assuming-projection, statement-integrity |
| `prop:skein-crossing-asymmetry` | self-assuming-projection, statement-integrity |
| `prop:sorting-color-energy` | self-assuming-projection, statement-integrity |
| `prop:spectrahedral-phase-collapse` | unused-hypotheses |
| `prop:spectral-sequence-h3-explicit` | self-assuming-projection, statement-integrity |
| `prop:strangelet-crossing-energy` | self-assuming-projection |
| `prop:substrate-consistency-window` | statement-integrity |
| `prop:surreal-rate-calculus` | statement-integrity, unused-hypotheses |
| `prop:symbolic-character-table` | self-assuming-projection, statement-integrity |
| `prop:symmetric-point-channel-collapse` | statement-integrity |
| `prop:tau-leptonic-universality` | statement-integrity |
| `prop:terms-2-6-higher-operations` | self-assuming-projection, statement-integrity |
| `prop:three-parameters-wedderburn` | statement-integrity |
| `prop:toffoli-transfer-matrix` | self-assuming-projection, statement-integrity |
| `prop:transfer-matrix-identities` | self-assuming-projection, statement-integrity |
| `prop:tritium-qvalue-symbolic` | self-assuming-projection |
| `prop:unit-modulus-eigenvalue` | statement-integrity |
| `prop:vol-through-tau` | self-assuming-projection, statement-integrity |
| `prop:volume-perturbation-formula` | self-assuming-projection, statement-integrity |
| `prop:wedderburn-bratteli-recursion` | statement-integrity |
| `prop:wedderburn-trace-identity` | self-assuming-projection, statement-integrity |
| `prop:wigner-coefficient-derivation` | statement-integrity |
| `prop:zeta8-witness-level2-su2` | statement-integrity, unused-hypotheses |
| `thm:frobenius-antipode-unifies-chirality-and-tower` | self-assuming-projection, statement-integrity |
| `thm:ns-singularity-descartes` | self-assuming-projection |
| `thm:parity-regime-selection` | self-assuming-projection |
| `thm:q-ns-wellposedness` | self-assuming-projection, statement-integrity |
| `thm:qou-obstruction-reduction` | self-assuming-projection, statement-integrity |
| `thm:qu-to-qou` | statement-integrity |
| `thm:quantum-peter-weyl` | self-assuming-projection, statement-integrity |
| `thm:six-term-mass-formula-complete` | self-assuming-projection, statement-integrity |
| `thm:substrate-self-duality` | statement-integrity |

## Rater warns (score < 0.66) — 121 blocks

| block | rater warns |
|---|---|
| `conj:bigbang-heatdeath` | novelty |
| `conj:bohr-radius-categorical` | goal-plausibility |
| `conj:borromean-baryon-mass-formula` | goal-plausibility |
| `conj:diophantine-birthday` | novelty |
| `conj:infinitesimal-observability` | novelty |
| `conj:n-v-tower-depth-ninety` | goal-plausibility |
| `conj:p-vs-np-qou` | novelty, strategy-clarity |
| `cor:habiro-expansion-atomic` | novelty |
| `cor:knot-factor-amphicheiral` | novelty |
| `lem:brings-euler-characteristic` | novelty, strategy-clarity |
| `lem:brings-riemann-hurwitz` | novelty, strategy-clarity |
| `lem:chebyshev-degree-genus` | novelty |
| `lem:fai-projector-coadjoint-orbit` | novelty, strategy-clarity |
| `lem:feynman-markov-identification` | strategy-clarity |
| `lem:genus-from-hecke-completeness` | novelty |
| `lem:genus-ideal-characterisation` | novelty |
| `lem:mobius-energy-frobenius-kernel` | novelty, strategy-clarity |
| `lem:nsi-q-deformed-kernel` | novelty, strategy-clarity |
| `lem:pair-skein-mass-formula` | strategy-clarity |
| `lem:skein-mass-from-linking` | strategy-clarity |
| `lem:su2-emergence-dagger-unitarity` | novelty, strategy-clarity |
| `lem:su2-emergence-volume-determinant` | novelty, strategy-clarity |
| `lem:tmli-constituent-composite-agreement` | strategy-clarity |
| `lem:topological-mass-cat-descended` | novelty, strategy-clarity |
| `lem:topological-mass-cat-eigenspace` | novelty, strategy-clarity |
| `lem:topological-mass-cat-transient` | novelty, strategy-clarity |
| `lem:topological-mass-dilogarithm` | novelty, strategy-clarity |
| `lem:topological-mass-holonomy` | novelty, strategy-clarity |
| `lem:topological-mass-transient-localisation` | novelty, strategy-clarity |
| `lem:yekutieli-leading-coefficient` | novelty, strategy-clarity |
| `prop:a-8-partition-function-identity` | novelty |
| `prop:atomic-lp-stability` | strategy-clarity |
| `prop:benzene-threading-emergence` | strategy-clarity |
| `prop:blowup-yekutieli` | strategy-clarity |
| `prop:borromean-h4-categorical-derivation` | novelty |
| `prop:brane-tower-q-laplacian-decay` | strategy-clarity |
| `prop:categorical-laplace-exists` | strategy-clarity |
| `prop:categorical-reeb-unique` | strategy-clarity |
| `prop:ch4-lp-dual-binding` | strategy-clarity |
| `prop:chirality-from-frobenius-self-pairing` | novelty, strategy-clarity |
| `prop:cl2-pentagon-and-faddeev-partial` | novelty |
| `prop:co-lp-dual-binding` | strategy-clarity |
| `prop:co2-lp-dual-binding` | strategy-clarity |
| `prop:confined-knot-binding` | novelty, strategy-clarity |
| `prop:confinement-frobenius-reciprocity` | strategy-clarity |
| `prop:confinement-phase-stratification` | strategy-clarity |
| `prop:confinement-universality` | strategy-clarity |
| `prop:content-scaling-correspondence` | novelty, strategy-clarity |
| `prop:corrected-markov-trace` | novelty, strategy-clarity |
| `prop:crossed-module-euler-characteristic` | novelty |
| `prop:cyclotomic-strand-doubling` | novelty |
| `prop:demand-stability` | strategy-clarity |
| `prop:double-slit-massive-pattern` | strategy-clarity |
| `prop:e-infinity-page-identifications` | strategy-clarity |
| `prop:em-coupling-projection` | novelty |
| `prop:fiber-adjoint-involution` | strategy-clarity |
| `prop:fibre-functor-atlas` | novelty, strategy-clarity |
| `prop:force-carrier-intertwining-correspondence` | strategy-clarity |
| `prop:four-term-pair-nucleon` | strategy-clarity |
| `prop:frobenius-pairing-exists` | novelty, strategy-clarity |
| `prop:frobenius-positivity-filter` | strategy-clarity |
| `prop:h2-lp-dual-binding` | strategy-clarity |
| `prop:hecke-satisfies-blitvic-hypothesis` | novelty |
| `prop:ilp-covalent-bond` | strategy-clarity |
| `prop:inductive-gb-reduction` | strategy-clarity |
| `prop:jet-prefix-gb-filtration` | goal-plausibility, strategy-clarity |
| `prop:knot-operator-selection` | strategy-clarity |
| `prop:knot-operator-transition` | goal-plausibility |
| `prop:lp-dual-stability` | strategy-clarity |
| `prop:mass-endomorphism-tower` | goal-plausibility |
| `prop:meson-scale-independence` | strategy-clarity |
| `prop:metallic-character-knot` | strategy-clarity |
| `prop:neutron-qvalue-symbolic` | strategy-clarity |
| `prop:noble-gas-characterization` | strategy-clarity |
| `prop:nuclear-operator-regimes` | strategy-clarity |
| `prop:nucleon-ordering-factorization` | strategy-clarity |
| `prop:observation-energy` | novelty, strategy-clarity |
| `prop:p-bandwidth-bound` | novelty, strategy-clarity |
| `prop:parallel-fibre-noninteraction` | novelty |
| `prop:partition-sum-proton-residual` | strategy-clarity |
| `prop:per-nucleon-shift-additive-linearity` | strategy-clarity |
| `prop:phi-q-aj-machinery-identification` | novelty, strategy-clarity |
| `prop:photon-threading-mass` | novelty, strategy-clarity |
| `prop:positive-definite-dagger` | novelty, strategy-clarity |
| `prop:positron-correction` | strategy-clarity |
| `prop:q-codifferential-formula` | novelty, strategy-clarity |
| `prop:q-exponential-taylor` | novelty |
| `prop:q-game-of-life` | novelty, strategy-clarity |
| `prop:q-gl-obstruction-calc` | novelty, strategy-clarity |
| `prop:q-plancherel-asymptotic-skeleton` | strategy-clarity |
| `prop:q-turbulence-spectrum` | novelty, strategy-clarity |
| `prop:qbeta-c-k-closed-forms` | goal-plausibility, novelty, strategy-clarity |
| `prop:qbeta-delta-tau-surrogate-taylor-coefficients` | novelty |
| `prop:quantum-observable-universe-exists` | novelty, strategy-clarity |
| `prop:quantum-universe-exists` | novelty, strategy-clarity |
| `prop:reeb-operations-per-planck` | novelty |
| `prop:rj-canonical-inner-product` | novelty |
| `prop:sdp-regime-switch` | strategy-clarity |
| `prop:shell-filling-rule` | goal-plausibility, strategy-clarity |
| `prop:six-term-per-derivation-weights` | strategy-clarity |
| `prop:skein-crossing-asymmetry` | novelty, strategy-clarity |
| `prop:sorting-color-energy` | strategy-clarity |
| `prop:substrate-consistency-window` | novelty, strategy-clarity |
| `prop:surreal-rate-calculus` | strategy-clarity |
| `prop:symbolic-character-table` | strategy-clarity |
| `prop:tau-leptonic-universality` | strategy-clarity |
| `prop:terms-2-6-higher-operations` | goal-plausibility, strategy-clarity |
| `prop:torus-knot-genus-four-unique` | novelty |
| `prop:tritium-qvalue-symbolic` | strategy-clarity |
| `prop:vdw-pskew-isolation` | novelty |
| `prop:vol-through-tau` | strategy-clarity |
| `prop:volume-perturbation-formula` | goal-plausibility, strategy-clarity |
| `prop:wigner-coefficient-derivation` | strategy-clarity |
| `thm:parity-regime-selection` | strategy-clarity |
| `thm:pontryagin-dual-coxeter-character` | goal-plausibility, novelty |
| `thm:q-ns-wellposedness` | strategy-clarity |
| `thm:qou-obstruction-reduction` | novelty, strategy-clarity |
| `thm:quantum-peter-weyl` | strategy-clarity |
| `thm:six-term-mass-formula-complete` | strategy-clarity |
| `thm:substrate-self-duality` | novelty, strategy-clarity |
| `thm:tannaka-krein-isomorphism` | strategy-clarity |

