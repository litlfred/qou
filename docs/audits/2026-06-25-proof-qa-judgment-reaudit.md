# Proof-QA judgment + rater re-audit (follow-up to PR #2775)

**Date:** 2026-06-25
**Branch:** `claude/proof-qa-judgment-reaudit-2026-06-25`
**Predecessor:** [PR #2775](https://github.com/litlfred/qou/pull/2775) (merged `db52522`)
drained the deterministic proof-QA false positives and **invalidated** the
1,680 unreliable judgment + rater verdicts from the 2026-06-22 `qa-agent-drain`
batch → `n/a` *pending canonical re-sweep*.

## This pass

The canonical `qa-sweep` (folio-assistant) is out of session scope (403), so
this performs the per-block agent re-audit directly: for each of the **360
blocks** whose 4 judgment + 3 rater criteria were invalidated, a sub-agent reads
the `.md` claim + the resolved Lean (sibling or `lean.ref` library decl) and
records a considered verdict, superseding the `n/a` placeholder.

Unlike the 2026-06-22 batch (templated — e.g. "contains sorryAx" notes on
sorry-free files), each verdict here cites block-specific evidence.

### Criteria + rubric

| criterion | PASS | FAIL |
|---|---|---|
| `proof-statement-integrity` | Lean statement faithfully encodes the `.md` claim; no `sorry`/`admit`/`native_decide` masking; no degenerate weakening | Lean proves a weaker/different claim (`Nonempty` via trivial instance, `: True`, self-projection); or unexpected axioms / `sorryAx` |
| `proof-no-self-assuming-projection` | proof derives the conclusion | proof just returns a hypothesis/structure field that *is* the conclusion (`:= ctx.foo`) |
| `proof-no-unused-hypotheses` | every binder is used | a hypothesis/instance binder is never referenced in the body |
| `proof-no-false-premise` | premises are satisfiable | a premise is contradictory ⇒ vacuously true |
| `proof-rater-goal-plausibility` | score ∈ [0,1] — is the goal well-posed and substantive? | (`< 0.66` = open) |
| `proof-rater-strategy-clarity` | score — is there a clear proof strategy? | (`< 0.66` = open) |
| `proof-rater-novelty` | score — does it add something beyond a restatement? | (`< 0.66` = open) |

`n/a` when no Lean resolves (6 blocks).

Tool: [`scripts/reaudit_verdict.py`](../../scripts/reaudit_verdict.py) (append a
fresh agent verdict; disjoint batches → parallel-safe).

## Caveat

A fresh Opus agent re-audit is **not more authoritative** than the canonical
checker; this is a best-effort interim re-audit until `folio-assistant`'s
`qa-sweep` can run. Verdicts are evidence-cited and reversible via git.

## Genuine judgment fails (114 blocks) — formalization debt catalogue

Blocks where the re-audit found the Lean does not faithfully derive the `.md` claim (self-assuming projection / degenerate weakening / sorry-stub). Evidence in each sidecar's latest verdict note.

| block | failing criteria |
|---|---|
| `cor:descartes-knot-eigenbasis` | statement-integrity |
| `cor:habiro-expansion-atomic` | statement-integrity |
| `cor:knot-factor-amphicheiral` | statement-integrity, unused-hypotheses, false-premise |
| `cor:lr-tensor-character-bridge` | statement-integrity, unused-hypotheses |
| `lem:bond-order-eq-jet-degree` | statement-integrity |
| `lem:brings-euler-characteristic` | statement-integrity, self-assuming-projection |
| `lem:brings-riemann-hurwitz` | statement-integrity, self-assuming-projection |
| `lem:chebyshev-degree-genus` | statement-integrity |
| `lem:fai-projector-coadjoint-orbit` | statement-integrity, self-assuming-projection |
| `lem:feynman-markov-identification` | statement-integrity, self-assuming-projection |
| `lem:mobius-energy-frobenius-kernel` | statement-integrity, self-assuming-projection |
| `lem:nsi-q-deformed-kernel` | statement-integrity, self-assuming-projection |
| `lem:pair-skein-mass-formula` | statement-integrity, self-assuming-projection |
| `lem:skein-mass-from-linking` | statement-integrity, self-assuming-projection |
| `lem:su2-emergence-dagger-unitarity` | statement-integrity, self-assuming-projection |
| `lem:su2-emergence-volume-determinant` | statement-integrity, self-assuming-projection |
| `lem:tmli-constituent-composite-agreement` | statement-integrity, self-assuming-projection |
| `lem:topological-mass-cat-descended` | statement-integrity, self-assuming-projection |
| `lem:topological-mass-cat-eigenspace` | statement-integrity, self-assuming-projection |
| `lem:topological-mass-cat-transient` | statement-integrity, self-assuming-projection |
| `lem:topological-mass-dilogarithm` | statement-integrity, self-assuming-projection |
| `lem:topological-mass-holonomy` | statement-integrity, self-assuming-projection |
| `lem:topological-mass-transient-localisation` | statement-integrity, self-assuming-projection |
| `lem:yekutieli-leading-coefficient` | statement-integrity, self-assuming-projection |
| `prop:alpha-shift-torus-knot` | self-assuming-projection |
| `prop:benzene-threading-emergence` | statement-integrity, self-assuming-projection |
| `prop:binding-genfun-qdifference` | statement-integrity |
| `prop:blowup-yekutieli` | statement-integrity |
| `prop:borromean-h4-categorical-derivation` | statement-integrity |
| `prop:centered-hecke-variance-positive` | self-assuming-projection |
| `prop:ch4-lp-dual-binding` | statement-integrity, self-assuming-projection |
| `prop:chi-lambda-w0-sign-weighting` | statement-integrity |
| `prop:chirality-from-frobenius-self-pairing` | statement-integrity, self-assuming-projection |
| `prop:co-lp-dual-binding` | statement-integrity, self-assuming-projection |
| `prop:co2-lp-dual-binding` | statement-integrity, self-assuming-projection |
| `prop:confined-knot-binding` | statement-integrity, self-assuming-projection |
| `prop:confinement-categorical` | statement-integrity, unused-hypotheses |
| `prop:confinement-frobenius-reciprocity` | statement-integrity, self-assuming-projection |
| `prop:confinement-operator-selection` | self-assuming-projection |
| `prop:confinement-phase-stratification` | statement-integrity, self-assuming-projection |
| `prop:confinement-sdp` | statement-integrity |
| `prop:confinement-universality` | self-assuming-projection |
| `prop:corrected-markov-trace` | statement-integrity, self-assuming-projection |
| `prop:crystal-basis-resolves-mass-tower-open-problems` | statement-integrity |
| `prop:demand-stability` | statement-integrity, self-assuming-projection |
| `prop:double-slit-massive-pattern` | statement-integrity |
| `prop:e-infinity-page-identifications` | statement-integrity, self-assuming-projection |
| `prop:explicit-central-idempotent` | statement-integrity, unused-hypotheses |
| `prop:fiber-adjoint-involution` | statement-integrity |
| `prop:fibre-functor-atlas` | statement-integrity, self-assuming-projection |
| `prop:force-carrier-intertwining-correspondence` | statement-integrity, unused-hypotheses |
| `prop:four-term-pair-nucleon` | statement-integrity, self-assuming-projection |
| `prop:frobenius-pairing-exists` | statement-integrity |
| `prop:frobenius-positivity-filter` | statement-integrity, self-assuming-projection |
| `prop:graded-markov-trace-from-gs-filtration` | statement-integrity, self-assuming-projection |
| `prop:gram-determinant-plancherel-ratio` | statement-integrity |
| `prop:ground-state-ordering` | statement-integrity, self-assuming-projection |
| `prop:h2-lp-dual-binding` | statement-integrity, self-assuming-projection |
| `prop:hecke-markov-transition` | statement-integrity |
| `prop:hecke-satisfies-blitvic-hypothesis` | statement-integrity, self-assuming-projection, unused-hypotheses |
| `prop:hoefsmit-V21-cos-symmetrization` | unused-hypotheses |
| `prop:hook-weight-derivation` | statement-integrity, self-assuming-projection |
| `prop:ilp-covalent-bond` | statement-integrity |
| `prop:inductive-gb-reduction` | statement-integrity, self-assuming-projection |
| `prop:jet-prefix-gb-filtration` | statement-integrity, self-assuming-projection |
| `prop:jet-sw-tau-decomposition` | statement-integrity |
| `prop:jucys-murphy-central-elements-qou` | statement-integrity, self-assuming-projection |
| `prop:knot-factor-spectral-form` | statement-integrity |
| `prop:knot-operator-selection` | statement-integrity, self-assuming-projection |
| `prop:lp-dual-stability` | statement-integrity, self-assuming-projection |
| `prop:lr-coefficient-hecke` | statement-integrity |
| `prop:magic-A-binding-formula` | statement-integrity |
| `prop:markov-trace-antipode-polynomial-symmetry` | statement-integrity |
| `prop:markov-trace-frobenius-selection` | statement-integrity, unused-hypotheses |
| `prop:mass-categorical-descent` | statement-integrity, self-assuming-projection |
| `prop:mass-endomorphism-tower` | statement-integrity |
| `prop:meson-scale-independence` | statement-integrity |
| `prop:metallic-character-knot` | statement-integrity, self-assuming-projection |
| `prop:neutron-qvalue-symbolic` | self-assuming-projection |
| `prop:noble-gas-characterization` | statement-integrity, self-assuming-projection |
| `prop:nuclear-operator-regimes` | statement-integrity |
| `prop:nucleon-ordering-factorization` | self-assuming-projection |
| `prop:observation-energy` | statement-integrity |
| `prop:p-bandwidth-bound` | statement-integrity, self-assuming-projection |
| `prop:partition-sum-proton-residual` | statement-integrity |
| `prop:per-nucleon-shift-additive-linearity` | statement-integrity, self-assuming-projection |
| `prop:phi-q-aj-machinery-identification` | statement-integrity, self-assuming-projection |
| `prop:photon-threading-mass` | statement-integrity, self-assuming-projection |
| `prop:physical-units-gap-linear` | statement-integrity |
| `prop:positive-definite-dagger` | statement-integrity, self-assuming-projection |
| `prop:positron-correction` | self-assuming-projection |
| `prop:q-codifferential-formula` | statement-integrity |
| `prop:q-exponential-taylor` | statement-integrity |
| `prop:q-game-of-life` | statement-integrity |
| `prop:q-gl-obstruction-calc` | statement-integrity, self-assuming-projection |
| `prop:q-plancherel-asymptotic-skeleton` | statement-integrity, self-assuming-projection |
| `prop:q-turbulence-spectrum` | statement-integrity, self-assuming-projection |
| `prop:qbeta-c-k-closed-forms` | statement-integrity |
| `prop:qbeta-delta-tau-surrogate-taylor-coefficients` | statement-integrity |
| `prop:quantum-observable-universe-exists` | statement-integrity |
| `prop:quantum-universe-exists` | statement-integrity |
| `prop:reeb-operations-per-planck` | statement-integrity, self-assuming-projection |
| `prop:rigid-monoidal-structural-gap-invariance` | unused-hypotheses |
| `prop:shell-closure-stability` | self-assuming-projection |
| `prop:six-term-per-derivation-weights` | statement-integrity, self-assuming-projection |
| `prop:skein-crossing-asymmetry` | statement-integrity, self-assuming-projection |
| `prop:sorting-color-energy` | statement-integrity, self-assuming-projection |
| `prop:spectral-sequence-h3-explicit` | statement-integrity, self-assuming-projection |
| `prop:surreal-rate-calculus` | statement-integrity, unused-hypotheses |
| `prop:symbolic-character-table` | statement-integrity, self-assuming-projection |
| `prop:symmetric-point-channel-collapse` | statement-integrity |
| `prop:terms-2-6-higher-operations` | statement-integrity, self-assuming-projection |
| `prop:three-parameters-wedderburn` | statement-integrity |
| `prop:toffoli-transfer-matrix` | statement-integrity, self-assuming-projection |
| `prop:transfer-matrix-identities` | statement-integrity, self-assuming-projection |
| `prop:tritium-qvalue-symbolic` | self-assuming-projection |
| `prop:unit-modulus-eigenvalue` | statement-integrity |
| `prop:vol-through-tau` | statement-integrity, self-assuming-projection |
| `prop:volume-perturbation-formula` | statement-integrity, self-assuming-projection |
| `prop:wedderburn-bratteli-recursion` | statement-integrity |
| `prop:wedderburn-trace-identity` | statement-integrity, self-assuming-projection |
| `prop:wigner-coefficient-derivation` | statement-integrity |
| `prop:zeta8-witness-level2-su2` | statement-integrity, unused-hypotheses |
| `thm:frobenius-antipode-unifies-chirality-and-tower` | statement-integrity, self-assuming-projection |
| `thm:ns-singularity-descartes` | self-assuming-projection |
| `thm:parity-regime-selection` | self-assuming-projection |
| `thm:q-ns-wellposedness` | statement-integrity, self-assuming-projection |
| `thm:qu-to-qou` | statement-integrity |
| `thm:quantum-peter-weyl` | statement-integrity, self-assuming-projection |
| `thm:substrate-self-duality` | statement-integrity |
