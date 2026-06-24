# Narrative-proof presence audit (2026-06-24)

**Question (author, 2026-06-24):** *Does each lemma/prop/thm in the paper
have a narrative proof in the paper? Is this a QA-sidecar dimension?*

## Answers

**1. No — roughly half of provable blocks have no narrative proof.**
Of **659** provable blocks (`theorem` / `lemma` / `proposition` /
`corollary`), **331 (~50 %)** state the result (often with rich
motivation and a pointer to a sorry-free Lean witness) but contain **no
proof a human reader can follow in prose** in the `.md`. A further **43**
deliberately defer to an external/axiomatic source (e.g.
`thm:jones-markov-trace`, "the proof occupies §3–5 of Jones (1987)") and
are *not* counted as gaps — those are intentional, cited black-boxes.

Spot-checked exemplars that are genuine gaps (statement + interpretation
+ "the Lean proves it sorry-free", but no derivation in prose):
`prop:bar-parity-split`, `prop:electron-period-base`,
`prop:confinement-sdp`.

**2. No — narrative-proof *presence* is not currently a QA-sidecar
dimension.** The `qa-criteria-registry.ts §PROOF` axis (~15 criteria) is
entirely **Lean-side**: `proof-no-bare-sorries`, `proof-lean-compiles`,
`proof-build-green`, `proof-no-axiom-growth`, the vacuity family
(`proof-no-trivial-true`, `proof-no-self-assuming-projection`, …), and
the rater scores. The single narrative-touching criterion,
`proof-narrative-lean-equiv`, is **gated on a `.lean` existing** and
checks *equivalence* between prose and Lean — it never asserts the
positive requirement "a provable block must carry a narrative proof."
So a block with a perfect Lean proof and a statement-only `.md` passes
every existing proof criterion while having no paper proof at all.

## Architecture decision (author, 2026-06-24)

Narrative proofs become a **separate `<root>.proof.md` sidecar file**,
part of the content block, so presence is trackable by file existence
(no prose heuristics). Convention spec:
[`docs/conventions/narrative-proof-sidecar.md`](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/docs/conventions/narrative-proof-sidecar.md).
The audit script now reports the migration split — `.proof.md` sidecar
(target) vs inline-in-`.md` (legacy, to migrate) vs gap. Current state:
**1** sidecar (seed exemplar `prop:electron-period-base`), **341** inline,
**~308** gaps.

## Method

Surfaced by the standalone, registry-independent audit
[`content/pipeline/audit-narrative-proof-presence.ts`](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/pipeline/audit-narrative-proof-presence.ts)
(`bun run content/pipeline/audit-narrative-proof-presence.ts`). A block
counts as having a narrative proof if its `.md` carries a proof cue
("Proof", "we prove/show/establish", induction/construction phrasing,
∎/QED). It is exempt when the narrative defers to an external/axiomatic
source. The heuristic over- and under-flags at the margin (a definitional
proposition needs no proof; a one-line "immediate from X" is a proof);
each flagged block needs a human pass to confirm disposition
(write proof / mark external / demote to `remark`/`definition`).

## Recommended follow-ups

- **Wire `proof-narrative-present` into the QA registry.** This lives in
  the separate `litlfred/folio-assistant` repo (`qa-criteria-registry.ts`
  + a `qa-checkers-proof-narrative.ts`); add it to the `proof` axis so
  `qa-sweep --axis proof` and `/integration-backlog proof` track the
  backlog the same way the Lean criteria are tracked.
- **Drain the 331-block backlog** chapter by chapter (largest first:
  mass-theory, quantum-observable-universes). For each: write the prose
  proof (often a transcription of the existing Lean argument), OR mark it
  external/axiomatic with a `-- Ref:`-style citation, OR demote to
  `remark`/`definition` if it makes no provable claim.

## Full gap list (331 blocks, by chapter)


### mass-theory  (68)
- `lem:feynman-eigenbasis-decomposition` (lemma) — [feynman-eigenbasis-decomposition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/feynman-eigenbasis-decomposition.ts)
- `lem:feynman-markov-identification` (lemma) — [feynman-markov-identification.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/feynman-markov-identification.ts)
- `lem:feynman-trace-collapse` (lemma) — [feynman-trace-collapse.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/feynman-trace-collapse.ts)
- `lem:skein-mass-from-linking` (lemma) — [skein-mass-from-linking.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/skein-mass-from-linking.ts)
- `lem:tmli-constituent-composite-agreement` (lemma) — [tmli-constituent-composite-agreement.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/tmli-constituent-composite-agreement.ts)
- `prop:alpha-basis-knot-delta-q` (proposition) — [alpha-basis-knot-delta-q.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/alpha-basis-knot-delta-q.ts)
- `prop:atom-knot-mass-derivation` (proposition) — [atom-knot-mass-derivation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/atom-knot-mass-derivation.ts)
- `prop:bar-parity-split` (proposition) — [bar-parity-split.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/bar-parity-split.ts)
- `prop:binding-alpha-shift-extension` (proposition) — [binding-alpha-shift-extension.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.ts)
- `prop:binding-genfun-qdifference` (proposition) — [binding-genfun-qdifference.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/binding-genfun-qdifference.ts)
- `prop:calibration-cohomology-alignment` (proposition) — [calibration-cohomology-alignment.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/calibration-cohomology-alignment.ts)
- `prop:chirality-dual-space-derivation` (proposition) — [chirality-dual-space-derivation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/chirality-dual-space-derivation.ts)
- `prop:chirality-writhe-ribbon-derivation` (proposition) — [chirality-writhe-ribbon-derivation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/chirality-writhe-ribbon-derivation.ts)
- `prop:confinement-sdp` (proposition) — [confinement-sdp.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/confinement-sdp.ts)
- `prop:content-scaling-correspondence` (proposition) — [content-scaling-correspondence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/content-scaling-correspondence.ts)
- `prop:delta-max-uniform-bound` (proposition) — [delta-max-uniform-bound.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/delta-max-uniform-bound.ts)
- `prop:demazure-fiber-markov-trace` (proposition) — [demazure-fiber-markov-trace.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/demazure-fiber-markov-trace.ts)
- `prop:electron-period-base` (proposition) — [electron-period-base.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/electron-period-base.ts)
- `prop:feynman-categorical-trace` (proposition) — [feynman-categorical-trace.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/feynman-categorical-trace.ts)
- `prop:feynman-classical-limit` (proposition) — [feynman-classical-limit.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/feynman-classical-limit.ts)
- `prop:flavor-dressed-mass-from-substrate-split` (proposition) — [flavor-dressed-mass-from-substrate-split.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/flavor-dressed-mass-from-substrate-split.ts)
- `prop:force-carrier-intertwining-correspondence` (proposition) — [force-carrier-intertwining-correspondence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/force-carrier-intertwining-correspondence.ts)
- `prop:gb-residue-spectral-sum` (proposition) — [gb-residue-spectral-sum.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/gb-residue-spectral-sum.ts)
- `prop:graded-trace-residue-split` (proposition) — [graded-trace-residue-split.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/graded-trace-residue-split.ts)
- `prop:ground-state-ordering` (proposition) — [ground-state-ordering.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/ground-state-ordering.ts)
- `prop:hecke-convergence-bound` (proposition) — [hecke-convergence-bound.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/hecke-convergence-bound.ts)
- `prop:hoefsmit-V21-cos-symmetrization` (proposition) — [hoefsmit-V21-cos-symmetrization.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/hoefsmit-V21-cos-symmetrization.ts)
- `prop:knot-indexed-convolution-grid` (proposition) — [knot-indexed-convolution-grid.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/knot-indexed-convolution-grid.ts)
- `prop:knot-operator-lp-selection` (proposition) — [knot-operator-lp-selection.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/knot-operator-lp-selection.ts)
- `prop:knot-operator-transition` (proposition) — [knot-operator-transition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/knot-operator-transition.ts)
- `prop:lepton-bring-surface-h3-3channel` (proposition) — [lepton-bring-surface-h3-3channel.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/lepton-bring-surface-h3-3channel.ts)
- `prop:lr-coefficient-hecke` (proposition) — [lr-coefficient-hecke.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/lr-coefficient-hecke.ts)
- `prop:mass-element-nf` (proposition) — [mass-element-nf.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/mass-element-nf.ts)
- `prop:meson-color-tube-uniqueness` (proposition) — [meson-color-tube-uniqueness.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/meson-color-tube-uniqueness.ts)
- `prop:neutron-proton-splitting` (proposition) — [neutron-proton-splitting.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/neutron-proton-splitting.ts)
- `prop:operator-valued-combiner-convergence` (proposition) — [operator-valued-combiner-convergence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/operator-valued-combiner-convergence.ts)
- `prop:partition-sum-proton-residual` (proposition) — [partition-sum-proton-residual.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/partition-sum-proton-residual.ts)
- `prop:pentagon-uv-commutation` (proposition) — [pentagon-uv-commutation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/pentagon-uv-commutation.ts)
- `prop:per-braid-mass-tower` (proposition) — [per-braid-mass-tower.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/per-braid-mass-tower.ts)
- `prop:phi-q-categorical-truncation` (proposition) — [phi-q-categorical-truncation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/phi-q-categorical-truncation.ts)
- `prop:pn-averaging-uniqueness` (proposition) — [pn-averaging-uniqueness.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/pn-averaging-uniqueness.ts)
- `prop:prolonged-periods-fixed-depth` (proposition) — [prolonged-periods-fixed-depth.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/prolonged-periods-fixed-depth.ts)
- `prop:q-beta-c3-hopf-three-fold-markov` (proposition) — [q-beta-c3-hopf-three-fold-markov.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/q-beta-c3-hopf-three-fold-markov.ts)
- `prop:qmn-recursive-memoized` (proposition) — [qmn-recursive-memoized.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/qmn-recursive-memoized.ts)
- `prop:reeb-bundle-complement-equals-volume` (proposition) — [reeb-bundle-complement-equals-volume.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/reeb-bundle-complement-equals-volume.ts)
- `prop:rho-k-h3a-refinement` (proposition) — [rho-k-h3a-refinement.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/rho-k-h3a-refinement.ts)
- `prop:schur-weyl-mass-decomposition` (proposition) — [schur-weyl-mass-decomposition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/schur-weyl-mass-decomposition.ts)
- `prop:skein-generation` (proposition) — [skein-generation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/skein-generation.ts)
- `prop:sl2-prolongation-recurrence` (proposition) — [sl2-prolongation-recurrence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/sl2-prolongation-recurrence.ts)
- `prop:symbolic-character-table` (proposition) — [symbolic-character-table.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/symbolic-character-table.ts)
- `prop:terminal-resolution` (proposition) — [terminal-resolution.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/terminal-resolution.ts)
- `prop:three-halves-structural-factor` (proposition) — [three-halves-structural-factor.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/three-halves-structural-factor.ts)
- `prop:three-parameters-wedderburn` (proposition) — [three-parameters-wedderburn.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/three-parameters-wedderburn.ts)
- `prop:thurston-volume-additivity` (proposition) — [thurston-volume-additivity.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/thurston-volume-additivity.ts)
- `prop:topological-mass-formula` (proposition) — [topological-mass-formula.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/topological-mass-formula.ts)
- `prop:torus-knot-delta-q-writhe` (proposition) — [torus-knot-delta-q-writhe.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/torus-knot-delta-q-writhe.ts)
- `prop:tower-binding-energy` (proposition) — [tower-binding-energy.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/tower-binding-energy.ts)
- `prop:transfer-matrix-level-independence` (proposition) — [transfer-matrix-level-independence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/transfer-matrix-level-independence.ts)
- `prop:vertex-is-exceptional-divisor` (proposition) — [vertex-is-exceptional-divisor.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/vertex-is-exceptional-divisor.ts)
- `prop:vol-through-tau` (proposition) — [vol-through-tau.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/vol-through-tau.ts)
- `prop:volume-perturbation-formula` (proposition) — [volume-perturbation-formula.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/volume-perturbation-formula.ts)
- `prop:volume-tower-decomposition` (proposition) — [volume-tower-decomposition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/volume-tower-decomposition.ts)
- `prop:weak-symmetric-normalization` (proposition) — [weak-symmetric-normalization.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/weak-symmetric-normalization.ts)
- `prop:wedderburn-as-noncomm-fourier` (proposition) — [wedderburn-as-noncomm-fourier.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/wedderburn-as-noncomm-fourier.ts)
- `prop:wedderburn-weight-canonical` (proposition) — [wedderburn-weight-canonical.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/wedderburn-weight-canonical.ts)
- `prop:wenzl-qmn-synergy` (proposition) — [wenzl-qmn-synergy.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/wenzl-qmn-synergy.ts)
- `prop:y-lambda-recipe-from-partition` (proposition) — [y-lambda-recipe-from-partition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/y-lambda-recipe-from-partition.ts)
- `thm:averaging-resonance-rule` (theorem) — [averaging-resonance-rule.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-theory/averaging-resonance-rule.ts)


### quantum-observable-universes  (56)
- `lem:fai-projector-coadjoint-orbit` (lemma) — [fai-projector-coadjoint-orbit.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/fai-projector-coadjoint-orbit.ts)
- `lem:qou-exists-axiom-1` (lemma) — [qou-exists-axiom-1.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/qou-exists-axiom-1.ts)
- `lem:qou-exists-axiom-2` (lemma) — [qou-exists-axiom-2.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/qou-exists-axiom-2.ts)
- `lem:qou-exists-axiom-3` (lemma) — [qou-exists-axiom-3.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/qou-exists-axiom-3.ts)
- `lem:qou-exists-axiom-4` (lemma) — [qou-exists-axiom-4.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/qou-exists-axiom-4.ts)
- `lem:su2-emergence-dagger-unitarity` (lemma) — [su2-emergence-dagger-unitarity.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/su2-emergence-dagger-unitarity.ts)
- `lem:su2-emergence-volume-determinant` (lemma) — [su2-emergence-volume-determinant.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.ts)
- `lem:volume-from-rigidity` (lemma) — [volume-from-rigidity.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.ts)
- `prop:categorical-action-exists` (proposition) — [categorical-action-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-action-exists.ts)
- `prop:categorical-action-unique` (proposition) — [categorical-action-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-action-unique.ts)
- `prop:categorical-dirac-operator-exists` (proposition) — [categorical-dirac-operator-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-dirac-operator-exists.ts)
- `prop:categorical-dirac-operator-unique` (proposition) — [categorical-dirac-operator-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-dirac-operator-unique.ts)
- `prop:categorical-dq-squared` (proposition) — [categorical-dq-squared.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-dq-squared.ts)
- `prop:categorical-fourier-exists` (proposition) — [categorical-fourier-transform-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-fourier-transform-exists.ts)
- `prop:categorical-fourier-unique` (proposition) — [categorical-fourier-transform-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-fourier-transform-unique.ts)
- `prop:categorical-instanton-exists` (proposition) — [categorical-instanton-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-instanton-exists.ts)
- `prop:categorical-instanton-unique` (proposition) — [categorical-instanton-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-instanton-unique.ts)
- `prop:categorical-lagrangian-exists` (proposition) — [categorical-lagrangian-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-lagrangian-exists.ts)
- `prop:categorical-lagrangian-unique` (proposition) — [categorical-lagrangian-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-lagrangian-unique.ts)
- `prop:categorical-laplace-exists` (proposition) — [categorical-laplace-transform-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-laplace-transform-exists.ts)
- `prop:categorical-q-connection-exists` (proposition) — [categorical-q-connection-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-q-connection-exists.ts)
- `prop:categorical-q-connection-unique` (proposition) — [categorical-q-connection-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-q-connection-unique.ts)
- `prop:categorical-q-ext-deriv-exists` (proposition) — [categorical-q-ext-deriv-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-q-ext-deriv-exists.ts)
- `prop:categorical-q-ext-deriv-unique` (proposition) — [categorical-q-ext-deriv-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-q-ext-deriv-unique.ts)
- `prop:categorical-reeb-unique` (proposition) — [categorical-reeb-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-reeb-unique.ts)
- `prop:categorical-self-duality` (proposition) — [categorical-self-duality.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-self-duality.ts)
- `prop:emergence-to-quantum-flat` (proposition) — [emergence-to-quantum-flat.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/emergence-to-quantum-flat.ts)
- `prop:fiber-adjoint-involution` (proposition) — [fiber-adjoint-involution.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/fiber-adjoint-involution.ts)
- `prop:germ-commutator-q-curvature` (proposition) — [germ-commutator-q-curvature.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/germ-commutator-q-curvature.ts)
- `prop:heisenberg-commutator` (proposition) — [heisenberg-commutator-prop.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/heisenberg-commutator-prop.ts)
- `prop:observation-energy` (proposition) — [observation-energy.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/observation-energy.ts)
- `prop:pawlowski-leitner-basis` (proposition) — [pawlowski-leitner-basis.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/pawlowski-leitner-basis.ts)
- `prop:pawlowski-leitner-inner-product` (proposition) — [pawlowski-leitner-inner-product.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/pawlowski-leitner-inner-product.ts)
- `prop:q-codifferential-formula` (proposition) — [q-codifferential-formula-prop.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-codifferential-formula-prop.ts)
- `prop:q-dilogarithm-exists` (proposition) — [q-dilogarithm-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-dilogarithm-exists.ts)
- `prop:q-dilogarithm-unique` (proposition) — [q-dilogarithm-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-dilogarithm-unique.ts)
- `prop:q-exponential-exists` (proposition) — [q-exponential-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-exponential-exists.ts)
- `prop:q-exponential-unique` (proposition) — [q-exponential-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-exponential-unique.ts)
- `prop:q-heat-equation-exists` (proposition) — [q-heat-equation-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-heat-equation-exists.ts)
- `prop:q-heat-equation-unique` (proposition) — [q-heat-equation-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-heat-equation-unique.ts)
- `prop:q-laplacian-spectral-tower` (proposition) — [q-laplacian-spectral-tower.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-laplacian-spectral-tower.ts)
- `prop:q-logarithm-exists` (proposition) — [q-logarithm-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-logarithm-exists.ts)
- `prop:q-logarithm-unique` (proposition) — [q-logarithm-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-logarithm-unique.ts)
- `prop:q-resolvent-exists` (proposition) — [q-resolvent-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-resolvent-exists.ts)
- `prop:q-resolvent-unique` (proposition) — [q-resolvent-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/q-resolvent-unique.ts)
- `prop:qou-canonical-action` (proposition) — [qou-canonical-action.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/qou-canonical-action.ts)
- `prop:spectral-chart-correspondence` (proposition) — [spectral-chart-correspondence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/spectral-chart-correspondence.ts)
- `prop:spin-labels` (proposition) — [spin-labels.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/spin-labels.ts)
- `prop:substrate-radial-coordinate` (proposition) — [substrate-radial-coordinate.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/substrate-radial-coordinate.ts)
- `prop:variational-equations` (proposition) — [variational-equations.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/variational-equations.ts)
- `thm:categorical-reeb-exists` (theorem) — [categorical-reeb-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/categorical-reeb-exists.ts)
- `thm:su2-emergence` (theorem) — [su2-emergence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/su2-emergence.ts)
- `thm:substrate-parameter-exists` (theorem) — [substrate-parameter-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/substrate-parameter-exists.ts)
- `thm:substrate-parameter-unique` (theorem) — [substrate-parameter-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/substrate-parameter-unique.ts)
- `thm:substrate-self-duality` (theorem) — [substrate-self-duality.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/substrate-self-duality.ts)
- `thm:weight-decomposition-exists` (theorem) — [weight-decomposition-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-observable-universes/weight-decomposition-exists.ts)


### particle-interactions  (25)
- `prop:atomic-lp-stability` (proposition) — [atomic-lp-stability.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/atomic-lp-stability.ts)
- `prop:atomic-nf-witness` (proposition) — [atomic-nf-witness.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/atomic-nf-witness.ts)
- `prop:beta-stability` (proposition) — [beta-stability.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/beta-stability.ts)
- `prop:compound-beta-shell-calibration` (proposition) — [compound-beta-shell-calibration.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/compound-beta-shell-calibration.ts)
- `prop:confinement-level-unique` (proposition) — [confinement-level-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/confinement-level-unique.ts)
- `prop:confinement-operator-selection` (proposition) — [confinement-operator-selection.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/confinement-operator-selection.ts)
- `prop:delta-pre-archimedean` (proposition) — [delta-pre-archimedean.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/delta-pre-archimedean.ts)
- `prop:demand-stability` (proposition) — [demand-stability.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/demand-stability.ts)
- `prop:four-term-pair-nucleon` (proposition) — [four-term-pair-nucleon.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/four-term-pair-nucleon.ts)
- `prop:frobenius-positivity-filter` (proposition) — [frobenius-positivity-filter.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/frobenius-positivity-filter.ts)
- `prop:generator-volume-decomposition` (proposition) — [generator-volume-decomposition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/generator-volume-decomposition.ts)
- `prop:gram-weighted-qvalue` (proposition) — [gram-weighted-qvalue.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/gram-weighted-qvalue.ts)
- `prop:hadron-exists` (proposition) — [hadron-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/hadron-exists.ts)
- `prop:hadron-operations-closure` (proposition) — [hadron-operations-closure.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/hadron-operations-closure.ts)
- `prop:hadron-unique` (proposition) — [hadron-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/hadron-unique.ts)
- `prop:knot-particle-correspondence` (proposition) — [knot-particle-correspondence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/knot-particle-correspondence.ts)
- `prop:lp-dual-stability` (proposition) — [lp-dual-stability.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/lp-dual-stability.ts)
- `prop:magic-shell-coupling-kappa` (proposition) — [magic-shell-coupling-kappa.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/magic-shell-coupling-kappa.ts)
- `prop:nuclear-groebner-reduction` (proposition) — [nuclear-groebner-reduction.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/nuclear-groebner-reduction.ts)
- `prop:nuclear-operator-regimes` (proposition) — [nuclear-operator-regimes.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/nuclear-operator-regimes.ts)
- `prop:positron-correction` (proposition) — [positron-correction.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/positron-correction.ts)
- `prop:q-beta-cos-resummation` (proposition) — [q-beta-cos-resummation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/q-beta-cos-resummation.ts)
- `prop:qbeta-counit-closed-form` (proposition) — [qbeta-counit-closed-form.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/qbeta-counit-closed-form.ts)
- `prop:silver-ratio-beta-decay-null` (proposition) — [silver-ratio-beta-decay-null.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/silver-ratio-beta-decay-null.ts)
- `prop:tritium-qvalue-symbolic` (proposition) — [tritium-qvalue-symbolic.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/particle-interactions/tritium-qvalue-symbolic.ts)


### brings-surface  (23)
- `cor:descartes-braid-structure` (corollary) — [descartes-braid-structure.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/descartes-braid-structure.ts)
- `cor:descartes-knot-eigenbasis` (corollary) — [descartes-knot-eigenbasis.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/descartes-knot-eigenbasis.ts)
- `lem:brings-euler-characteristic` (lemma) — [brings-euler-characteristic.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/brings-euler-characteristic.ts)
- `lem:brings-riemann-hurwitz` (lemma) — [brings-riemann-hurwitz.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/brings-riemann-hurwitz.ts)
- `lem:chebyshev-degree-genus` (lemma) — [chebyshev-degree-genus.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/chebyshev-degree-genus.ts)
- `lem:genus-from-hecke-completeness` (lemma) — [genus-from-hecke-completeness.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/genus-from-hecke-completeness.ts)
- `lem:genus-ideal-characterisation` (lemma) — [genus-ideal-characterisation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/genus-ideal-characterisation.ts)
- `lem:mi-sw-abelianisation-cartan` (lemma) — [mi-sw-abelianisation-cartan.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/mi-sw-abelianisation-cartan.ts)
- `lem:yekutieli-leading-coefficient` (lemma) — [yekutieli-leading-coefficient.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.ts)
- `prop:bring-trefoil-cinquefoil-channel` (proposition) — [bring-trefoil-cinquefoil-channel.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/bring-trefoil-cinquefoil-channel.ts)
- `prop:brings-is-qou` (proposition) — [brings-is-qou.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/brings-is-qou.ts)
- `prop:brings-smoothness-resolution` (proposition) — [brings-smoothness-resolution.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/brings-smoothness-resolution.ts)
- `prop:coral-elliptic` (proposition) — [coral-elliptic.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/coral-elliptic.ts)
- `prop:defect-legendrian-knot` (proposition) — [defect-legendrian-knot.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/defect-legendrian-knot.ts)
- `prop:genus-filtration-ideal` (proposition) — [genus-filtration-ideal.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/genus-filtration-ideal.ts)
- `prop:genus-maximal-descent` (proposition) — [genus-maximal-descent.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/genus-maximal-descent.ts)
- `prop:jet-sw-tau-decomposition` (proposition) — [jet-sw-tau-decomposition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/jet-sw-tau-decomposition.ts)
- `prop:mi-sw-abelianisation` (proposition) — [mi-sw-abelianisation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/mi-sw-abelianisation.ts)
- `prop:sw-period-residue-sum` (proposition) — [sw-period-residue-sum.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/sw-period-residue-sum.ts)
- `prop:torus-knot-generators` (proposition) — [torus-knot-generators.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/torus-knot-generators.ts)
- `thm:descartes` (theorem) — [descartes.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/descartes.ts)
- `thm:embeddability-closure` (theorem) — [embeddability-closure.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/embeddability-closure.ts)
- `thm:topological-charge-quantization` (theorem) — [topological-charge-quantization.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/brings-surface/topological-charge-quantization.ts)


### lifting-and-descent  (22)
- `cor:jet-prolongation-C` (corollary) — [jet-prolongation-C.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/jet-prolongation-C.ts)
- `cor:quantum-dilogarithm` (corollary) — [quantum-dilogarithm.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/quantum-dilogarithm.ts)
- `lem:ccg-crossed-module-structure` (lemma) — [ccg-crossed-module-structure.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/ccg-crossed-module-structure.ts)
- `lem:descent` (lemma) — [descent-lemma.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/descent-lemma.ts)
- `lem:descent-cocycle-deviation` (lemma) — [descent-cocycle-deviation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/descent-cocycle-deviation.ts)
- `lem:jet-prolongation-categorical-jet` (lemma) — [jet-prolongation-categorical-jet.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/jet-prolongation-categorical-jet.ts)
- `prop:algebraic-filter-classification` (proposition) — [algebraic-filter-classification.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/algebraic-filter-classification.ts)
- `prop:blowup-yekutieli` (proposition) — [p3-blowup-yekutieli.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/p3-blowup-yekutieli.ts)
- `prop:brane-boundary` (proposition) — [brane-boundary-structure.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/brane-boundary-structure.ts)
- `prop:categorical-jet-prolongation` (proposition) — [categorical-jet-prolongation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/categorical-jet-prolongation.ts)
- `prop:cosimplicial-crossed-groupoid` (proposition) — [cosimplicial-crossed-groupoid.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/cosimplicial-crossed-groupoid.ts)
- `prop:descent-condition` (proposition) — [descent-condition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/descent-condition.ts)
- `prop:descent-eigenspaces` (proposition) — [descent-eigenspaces.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/descent-eigenspaces.ts)
- `prop:euler-char-stability` (proposition) — [euler-char-stability.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/euler-char-stability.ts)
- `prop:global-gluing` (proposition) — [global-gluing.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/global-gluing.ts)
- `prop:jet-prolongation` (proposition) — [jet-prolongation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/jet-prolongation.ts)
- `prop:quantum-characteristic-classes-exists` (proposition) — [quantum-characteristic-classes-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/quantum-characteristic-classes-exists.ts)
- `prop:quantum-characteristic-classes-unique` (proposition) — [quantum-characteristic-classes-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/quantum-characteristic-classes-unique.ts)
- `prop:vacuum-state` (proposition) — [vacuum-state.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/vacuum-state.ts)
- `prop:weak-equiv-invariance` (proposition) — [weak-equiv-invariance.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/weak-equiv-invariance.ts)
- `prop:yekutieli-lifting` (proposition) — [yekutieli-lifting.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/yekutieli-lifting.ts)
- `thm:qu-to-qou` (theorem) — [qu-to-qou.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/lifting-and-descent/qu-to-qou.ts)


### mass-endomorphism  (17)
- `cor:mass-identity-C` (corollary) — [mass-identity-C.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/mass-identity-C.ts)
- `lem:topological-mass-cat-descended` (lemma) — [topological-mass-cat-descended.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/topological-mass-cat-descended.ts)
- `lem:topological-mass-cat-eigenspace` (lemma) — [topological-mass-cat-eigenspace.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/topological-mass-cat-eigenspace.ts)
- `lem:topological-mass-cat-transient` (lemma) — [topological-mass-cat-transient.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/topological-mass-cat-transient.ts)
- `lem:topological-mass-dilogarithm` (lemma) — [topological-mass-dilogarithm.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/topological-mass-dilogarithm.ts)
- `lem:topological-mass-eigenspace-decomp` (lemma) — [topological-mass-eigenspace-decomp.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/topological-mass-eigenspace-decomp.ts)
- `lem:topological-mass-holonomy` (lemma) — [topological-mass-holonomy.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/topological-mass-holonomy.ts)
- `lem:topological-mass-transient-localisation` (lemma) — [topological-mass-transient-localisation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.ts)
- `prop:categorical-chain-convergence-mechanisms` (proposition) — [categorical-chain-convergence-mechanisms.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/categorical-chain-convergence-mechanisms.ts)
- `prop:color-spacetime-s5-factorization` (proposition) — [color-spacetime-s5-factorization.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/color-spacetime-s5-factorization.ts)
- `prop:explicit-central-idempotent` (proposition) — [explicit-central-idempotent.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/explicit-central-idempotent.ts)
- `prop:gb-spectral-sequence` (proposition) — [gb-spectral-sequence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/gb-spectral-sequence.ts)
- `prop:mass-identity-exists` (proposition) — [mass-identity-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/mass-identity-exists.ts)
- `prop:mass-identity-unique` (proposition) — [mass-identity-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/mass-identity-unique.ts)
- `prop:q-hecke-seminormal-character-closure` (proposition) — [q-hecke-seminormal-character-closure.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/q-hecke-seminormal-character-closure.ts)
- `prop:qbeta-c-k-closed-forms` (proposition) — [conj-qbeta-c-k-closed-forms.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/conj-qbeta-c-k-closed-forms.ts)
- `prop:rho-k-graded-expansion` (proposition) — [rho-k-graded-expansion.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/mass-endomorphism/rho-k-graded-expansion.ts)


### observations  (14)
- `lem:nucleon-borromean-topology` (lemma) — [nucleon-borromean-topology.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/nucleon-borromean-topology.ts)
- `lem:pair-skein-mass-formula` (lemma) — [pair-skein-mass-formula.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/pair-skein-mass-formula.ts)
- `prop:algebraic-gns-embedding` (proposition) — [algebraic-gns-embedding.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/algebraic-gns-embedding.ts)
- `prop:brane-tower-q-laplacian-decay` (proposition) — [brane-tower-q-laplacian-decay.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/brane-tower-q-laplacian-decay.ts)
- `prop:crossing-energy-decomposition` (proposition) — [crossing-energy-decomposition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/crossing-energy-decomposition.ts)
- `prop:double-slit-massive-pattern` (proposition) — [double-slit-massive-pattern.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/double-slit-massive-pattern.ts)
- `prop:flavor-split-substrate` (proposition) — [flavor-split-substrate.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/flavor-split-substrate.ts)
- `prop:local-substrate-q` (proposition) — [local-substrate-q.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/local-substrate-q.ts)
- `prop:magic-numbers-from-q` (proposition) — [magic-numbers-from-q.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/magic-numbers-from-q.ts)
- `prop:neutron-prediction-comparison` (proposition) — [neutron-prediction-comparison.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/neutron-prediction-comparison.ts)
- `prop:q-plancherel-asymptotic-skeleton` (proposition) — [q-plancherel-asymptotic-skeleton.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.ts)
- `prop:sdp-regime-switch` (proposition) — [sdp-regime-switch.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/sdp-regime-switch.ts)
- `prop:strangelet-double-beta` (proposition) — [strangelet-double-beta.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/strangelet-double-beta.ts)
- `prop:substrate-consistency-window` (proposition) — [substrate-consistency-window.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/observations/substrate-consistency-window.ts)


### fluid-dynamics  (14)
- `prop:acoustic-horizon-conditions` (proposition) — [acoustic-horizon-conditions.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/acoustic-horizon-conditions.ts)
- `prop:core-levi-form` (proposition) — [core-levi-form.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/core-levi-form.ts)
- `prop:discrete-vortex-spectrum` (proposition) — [discrete-vortex-spectrum.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/discrete-vortex-spectrum.ts)
- `prop:helicity-conservation` (proposition) — [helicity-conservation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/helicity-conservation.ts)
- `prop:kelvin-dispersion-derivation` (proposition) — [kelvin-dispersion-derivation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/kelvin-dispersion-derivation.ts)
- `prop:ns-kummer-specialisation` (proposition) — [ns-kummer-specialisation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/ns-kummer-specialisation.ts)
- `prop:ns-obstruction-computation` (proposition) — [ns-obstruction-computation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/ns-obstruction-computation.ts)
- `prop:ns-obstruction-tower` (proposition) — [ns-obstruction-tower.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/ns-obstruction-tower.ts)
- `prop:q-ns-nonlinear-uniqueness` (proposition) — [p1-nonlinear-uniqueness.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/p1-nonlinear-uniqueness.ts)
- `prop:q-turbulence-spectrum` (proposition) — [q-turbulence-spectrum.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/q-turbulence-spectrum.ts)
- `prop:universality` (proposition) — [p4-universality.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/p4-universality.ts)
- `prop:vorticity-lower-bound` (proposition) — [vorticity-lower-bound.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/vorticity-lower-bound.ts)
- `thm:q-bkm` (theorem) — [q-bkm-criterion.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/q-bkm-criterion.ts)
- `thm:q-ns-wellposedness` (theorem) — [q-ns-wellposedness.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/fluid-dynamics/q-ns-wellposedness.ts)


### predicted-spectra  (10)
- `lem:tilting-module-rigidity` (lemma) — [tilting-module-rigidity.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/predicted-spectra/tilting-module-rigidity.ts)
- `prop:alpha-em-categorical-trace-ratio` (proposition) — [alpha-em-categorical-trace-ratio.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/predicted-spectra/alpha-em-categorical-trace-ratio.ts)
- `prop:cs-evaluation-faithfulness` (proposition) — [cs-evaluation-faithfulness.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/predicted-spectra/cs-evaluation-faithfulness.ts)
- `prop:em-coupling-projection` (proposition) — [em-coupling-projection.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/predicted-spectra/em-coupling-projection.ts)
- `prop:hadron-half-life` (proposition) — [hadron-half-life.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/predicted-spectra/hadron-half-life.ts)
- `prop:integer-stability` (proposition) — [integer-stability.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/predicted-spectra/integer-stability.ts)
- `prop:reidemeister-action-table` (proposition) — [reidemeister-action-table.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/predicted-spectra/reidemeister-action-table.ts)
- `prop:skein-coulomb-enhancement` (proposition) — [skein-coulomb-enhancement.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/predicted-spectra/skein-coulomb-enhancement.ts)
- `prop:skein-finiteness-bound` (proposition) — [skein-finiteness-bound.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/predicted-spectra/skein-finiteness-bound.ts)
- `prop:type-b-folded-crystal-combinatorics` (proposition) — [type-b-folded-crystal-combinatorics.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/predicted-spectra/type-b-folded-crystal-combinatorics.ts)


### molecular-construction  (10)
- `prop:assembly-projector-exists` (proposition) — [assembly-projector-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/molecular-construction/assembly-projector-exists.ts)
- `prop:benzene-threading-emergence` (proposition) — [benzene-threading-emergence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/molecular-construction/benzene-threading-emergence.ts)
- `prop:ch4-lp-dual-binding` (proposition) — [ch4-lp-dual-binding.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/molecular-construction/ch4-lp-dual-binding.ts)
- `prop:co-lp-dual-binding` (proposition) — [co-lp-dual-binding.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/molecular-construction/co-lp-dual-binding.ts)
- `prop:co2-lp-dual-binding` (proposition) — [co2-lp-dual-binding.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/molecular-construction/co2-lp-dual-binding.ts)
- `prop:h2-lp-dual-binding` (proposition) — [h2-lp-dual-binding.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/molecular-construction/h2-lp-dual-binding.ts)
- `prop:ilp-covalent-bond` (proposition) — [ilp-covalent-bond.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/molecular-construction/ilp-covalent-bond.ts)
- `prop:shell-filling-rule` (proposition) — [shell-filling-rule.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/molecular-construction/shell-filling-rule.ts)
- `prop:symmetric-block-domain-weight` (proposition) — [symmetric-block-domain-weight.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/molecular-construction/symmetric-block-domain-weight.ts)
- `prop:tetrahedral-hbond-directions` (proposition) — [tetrahedral-hbond-directions.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/molecular-construction/tetrahedral-hbond-directions.ts)


### quantum-universes  (9)
- `prop:categorical-connection-exists` (proposition) — [categorical-connection-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-universes/categorical-connection-exists.ts)
- `prop:categorical-connection-unique` (proposition) — [categorical-connection-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-universes/categorical-connection-unique.ts)
- `prop:categorical-hodge-star-exists` (proposition) — [categorical-hodge-star-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-universes/categorical-hodge-star-exists.ts)
- `prop:categorical-hodge-star-unique` (proposition) — [categorical-hodge-star-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-universes/categorical-hodge-star-unique.ts)
- `prop:frobenius-pairing-exists` (proposition) — [frobenius-pairing-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-universes/frobenius-pairing-exists.ts)
- `prop:frobenius-pairing-unique` (proposition) — [frobenius-pairing-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-universes/frobenius-pairing-unique.ts)
- `prop:frobenius-relation` (proposition) — [frobenius-relation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-universes/frobenius-relation.ts)
- `prop:positive-definite-dagger` (proposition) — [positive-definite-dagger.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-universes/positive-definite-dagger.ts)
- `prop:quantum-universe-exists` (proposition) — [quantum-universe-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/quantum-universes/quantum-universe-exists.ts)


### climax-volume-mass  (8)
- `cor:non-self-intersection` (corollary) — [non-self-intersection.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/climax-volume-mass/non-self-intersection.ts)
- `lem:mobius-energy-frobenius-kernel` (lemma) — [mobius-energy-frobenius-kernel.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/climax-volume-mass/mobius-energy-frobenius-kernel.ts)
- `lem:nsi-q-deformed-kernel` (lemma) — [nsi-q-deformed-kernel.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/climax-volume-mass/nsi-q-deformed-kernel.ts)
- `prop:knot-operator-energy-exists` (proposition) — [knot-operator-energy-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/climax-volume-mass/knot-operator-energy-exists.ts)
- `prop:knot-operator-energy-unique` (proposition) — [knot-operator-energy-unique.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/climax-volume-mass/knot-operator-energy-unique.ts)
- `prop:mobius-energy` (proposition) — [mobius-energy.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/climax-volume-mass/mobius-energy.ts)
- `prop:skein-crossing-asymmetry` (proposition) — [skein-crossing-asymmetry-prop.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/climax-volume-mass/skein-crossing-asymmetry-prop.ts)
- `prop:vertex-algebra-relations` (proposition) — [vertex-algebra-relations.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/climax-volume-mass/vertex-algebra-relations.ts)


### information-theory  (6)
- `prop:composite-crossing-parity` (proposition) — [composite-crossing-parity.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/information-theory/composite-crossing-parity.ts)
- `prop:hopf-link-symmetric-decomposition` (proposition) — [hopf-link-symmetric-decomposition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/information-theory/hopf-link-symmetric-decomposition.ts)
- `prop:p-vs-np-boundary` (proposition) — [p-vs-np-boundary.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/information-theory/p-vs-np-boundary.ts)
- `prop:phase-transition-boundary` (proposition) — [phase-transition-boundary.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/information-theory/phase-transition-boundary.ts)
- `prop:photon-threading-mass` (proposition) — [photon-threading-mass.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/information-theory/photon-threading-mass.ts)
- `prop:vdw-pskew-isolation` (proposition) — [vdw-pskew-isolation.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/information-theory/vdw-pskew-isolation.ts)


### formal-groups-chapter  (5)
- `thm:grobner-shirshov-basis-exists` (theorem) — [grobner-shirshov-basis-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/fred2005-formal-groups/formal-groups-chapter/grobner-shirshov-basis-exists.ts)
- `thm:reduction-mod-p` (theorem) — [reduction-mod-p.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/fred2005-formal-groups/formal-groups-chapter/reduction-mod-p.ts)
- `thm:skew-poisson-integrates` (theorem) — [skew-poisson-integrates.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/fred2005-formal-groups/formal-groups-chapter/skew-poisson-integrates.ts)
- `thm:strong-multiplicativity` (theorem) — [strong-multiplicativity.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/fred2005-formal-groups/formal-groups-chapter/strong-multiplicativity.ts)
- `thm:unit-root-iff-integrable` (theorem) — [unit-root-iff-integrable.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/fred2005-formal-groups/formal-groups-chapter/unit-root-iff-integrable.ts)


### braids-and-knots  (4)
- `prop:alpha-em-habiro-bar-involution` (proposition) — [alpha-em-habiro-bar-involution.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.ts)
- `prop:lagrange-resolvent-transform` (proposition) — [lagrange-resolvent-transform.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/braids-and-knots/lagrange-resolvent-transform.ts)
- `prop:q-casimir-exists` (proposition) — [q-casimir-exists.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/braids-and-knots/q-casimir-exists.ts)
- `prop:r-matrix-braiding-structure` (proposition) — [r-matrix-braiding-structure.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/braids-and-knots/r-matrix-braiding-structure.ts)


### stochastic-mechanics  (4)
- `prop:phi-q-aj-machinery-identification` (proposition) — [phi-q-aj-machinery-identification.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/stochastic-mechanics/phi-q-aj-machinery-identification.ts)
- `prop:two-filtration-bridge-small-cases` (proposition) — [two-filtration-bridge-small-cases.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/stochastic-mechanics/two-filtration-bridge-small-cases.ts)
- `thm:macroscopic-stability-equivalence` (theorem) — [macroscopic-stability-equivalence.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/stochastic-mechanics/macroscopic-stability-equivalence.ts)
- `thm:quantum-gap-collapse` (theorem) — [quantum-gap-collapse.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/stochastic-mechanics/quantum-gap-collapse.ts)


### q-geometric-langlands  (4)
- `cor:spectral-half-line` (corollary) — [spectral-half-line.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/q-geometric-langlands/spectral-half-line.ts)
- `prop:q-gl-obstruction-calc` (proposition) — [q-gl-obstruction-calc.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/q-geometric-langlands/q-gl-obstruction-calc.ts)
- `prop:q-hecke-eigenvalue` (proposition) — [q-hecke-eigenvalue.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/q-geometric-langlands/q-hecke-eigenvalue.ts)
- `thm:tannaka-krein-isomorphism` (theorem) — [tannaka-krein-isomorphism.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/q-geometric-langlands/tannaka-krein-isomorphism.ts)


### unital-groebner-bases-chapter  (4)
- `lem:generator-choice` (lemma) — [generator-choice-lemma.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/unital-groebner-bases/unital-groebner-bases-chapter/generator-choice-lemma.ts)
- `prop:s-polynomial-decomposition` (proposition) — [s-polynomial-decomposition.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/unital-groebner-bases/unital-groebner-bases-chapter/s-polynomial-decomposition.ts)
- `thm:buchberger` (theorem) — [buchberger.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/unital-groebner-bases/unital-groebner-bases-chapter/buchberger.ts)
- `thm:unital-groebner-decomposition` (theorem) — [main-theorem.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/unital-groebner-bases/unital-groebner-bases-chapter/main-theorem.ts)


### models-of-qous  (3)
- `prop:categorical-archimedean-bridge` (proposition) — [categorical-archimedean-bridge.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/models-of-qous/categorical-archimedean-bridge.ts)
- `prop:main-commutative-diagram` (proposition) — [main-commutative-diagram.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/models-of-qous/main-commutative-diagram.ts)
- `prop:skew-poisson-integration` (proposition) — [skew-poisson-integration.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/models-of-qous/skew-poisson-integration.ts)


### appendix-surreals  (2)
- `prop:borel-partial-resolution` (proposition) — [borel-partial-resolution.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/appendix-surreals/borel-partial-resolution.ts)
- `prop:collatz-contact-boundary` (proposition) — [collatz-contact-boundary.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/appendix-surreals/collatz-contact-boundary.ts)


### organic-chemistry  (2)
- `prop:chain-ring-comparison` (proposition) — [chain-ring-comparison.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/organic-chemistry/chain-ring-comparison.ts)
- `prop:ring-closure-barrier` (proposition) — [ring-closure-barrier.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/quantum-observable-universe/organic-chemistry/ring-closure-barrier.ts)


### introduction  (1)
- `thm:ugb-main` (theorem) — [ugb-main-theorem-statement.ts](https://github.com/litlfred/qou/blob/claude/wonderful-newton-bh1fxt/content/unital-groebner-bases/introduction/ugb-main-theorem-statement.ts)
