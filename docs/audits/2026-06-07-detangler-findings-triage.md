# Detangler findings triage (2026-06-07)

Follow-up to the detangler audit-counting-bug fixes (PRs #1949, #1955,
#1961, #1963). Those made the detangler metrics trustworthy; this doc
triages the **genuine** remaining findings into concrete actions for
author review. No paper content is reordered or relocated by this doc —
it is a proposal.

## 1. mass-theory graph-energy reorder proposal

45 blocks in `mass-theory` fail `detangler-graph-energy` (energy ≥ 100):
they sit early in the chapter manifest but `uses[]` blocks defined far
later, forcing the reader to skip ahead. Of the 32 with computable
forward dependencies, a single-block relocation (move the block to just
after its latest dependency) is **safe** only when no earlier block
depends on it — otherwise the move trades one forward edge for another
and the tangle is genuine (needs splitting an edge or merging blocks).

**Method:** for each flagged block compute its manifest position `p`,
the position of its latest same-chapter `uses[]` target `maxDep`, and
the position of its earliest dependent `minDependent`. A move to just
after `maxDep` is SAFE iff `minDependent > maxDep`.

### 1a. SAFE single-block moves (12) — low risk, recommended

| block | pos | → move after | in-degree |
|---|---|---|---|
| `conj:hoefsmit-scattering-pipeline` | 71 | 420 | 1 |
| `rem:kashiwara-jones-alternation-interpretation` | 174 | 457 | 0 |
| `conj:categorical-linking-operation` | 204 | 475 | 0 |
| `conj:dim-master-pentagon` | 208 | 474 | 0 |
| `conj:poincare-lefschetz-borromean` | 214 | 474 | 0 |
| `prop:two-filtration-bridge-general` | 63 | 289 | 1 |
| `rem:geometric-invariant-piecewise` | 209 | 419 | 0 |
| `rem:two-tier-scaling-pq` | 17 | 194 | 1 |
| `conj:kashaev-density-equals-sdp-multiplicity` | 211 | 372 | 0 |
| `rem:markov-chain-fluctuations` | 159 | 302 | 0 |
| `conj:p-from-braid-mirror` | 212 | 352 | 0 |
| `prop:rigid-monoidal-structural-gap-invariance` | 179 | 314 | 0 |

These relocate cleanly: each is used by nothing earlier than its target
slot, so moving it down the manifest removes its forward edges without
creating new ones. Mechanical manifest edit (reorder the slug in
`mass-theory.ts` `sections[].blocks[]`); no prose change.

### 1b. CONFLICTS (20) — genuine tangles, need author judgment

These have a dependent sitting at/before the dependency, so no single
move fixes them. Examples:

| block | pos | dep at | earliest dependent at | nature |
|---|---|---|---|---|
| `prop:pentagon-uv-commutation` | 39 | 271 | 213 | used at 213, uses to 271 → straddles |
| `prop:frobenius-s-classification` | 23 | 300 | 24 | used immediately after, uses to 300 |
| `lem:tmli-constituent-composite-agreement` | 3 | 153 | 4 | foundational + forward-reaching |
| `prop:jet-tower-convergence` | 226 | 366 | 39 | used at 39, uses to 366 |
| `prop:gram-determinant-plancherel-ratio` | 52 | 353 | 342 | long straddle |

The `pentagon-uv-commutation` case (energy 810, the worst) is
illustrative: it is *used by* a block at position 213 but *uses*
`lem:vhat-pair-commutation-trace` at 271. No reorder satisfies both.
Resolution options (author call): (a) split the proposition into a
statement (early) + a proof/derivation (late, near the lemma); (b) drop
the `prop → rem:quantum-bloch-group` edge (a proposition depending on a
remark is itself a convention violation — remarks interpret props, not
vice versa); (c) accept the forward edge as inherent to the chapter's
narrative structure.

## 2. topic-coherence triage (23 → 4 relocate, 19 accept)

The refined `topic-coherence` check (PR #1961) flags load-bearing
logical blocks whose prose reads as another chapter's topic. Most are
**ACCEPT**: `observations` / `information-theory` / `fluid-dynamics` are
cross-cutting layers — a block reporting a measured value *of* a braid
construction legitimately lives in `observations`.

### RELOCATE candidates (4) — pure theory in a cross-cutting chapter

| block | home | → suggested | reason |
|---|---|---|---|
| `prop:trace-locality-meets-gs-non-locality` | observations | braids-and-knots | pure Hecke / Gröbner–Shirshov reconciliation; no empirical content |
| `prop:hecke-satisfies-blitvic-hypothesis` | observations | braids-and-knots | pure non-commutative-probability theory |
| `def:skein-resolution-obstruction` | information-theory | braids-and-knots | quantum-computational obstruction infrastructure |
| `prop:blowup-yekutieli` | fluid-dynamics | lifting-and-descent | Yekutieli descent cohomology, not a fluid result |

Relocation is content surgery (moves the file, updates the chapter
manifest, may shift `uses[]` resolution) — deferred to explicit author
approval per block.

### ACCEPT (19)

The remaining 19 are by-design cross-topic: empirical-prediction
propositions in `observations` (e.g. `prop:neutron-proton-mass-splitting`,
`prop:strangelet-*`, `prop:gravity-spectral-prefactor`), computational
applications in `information-theory` (`prop:toffoli-*`,
`prop:photon-threading-mass`), and foundational definitions
(`def:substrate-parameter-planck`). They reference another chapter's
vocabulary in service of their home chapter's job.

## 3. other-axis counting-bug audit (task 3)

Audited the voice / python / q-usage / proof / canonical / compute /
bibliography checkers for the same over-counting class fixed in the
detangler axis. **All clean except one** (fixed in this PR):
`checkCanonicalCalibrationCount` counted `calibration:`/`anchor:`
declarations via a global regex over concatenated `.md` + `.ts` with no
de-duplication, so an anchor declared in both files double-counted and
could push a legitimate 3-calibration block to a false fail. Fixed by
counting distinct anchor declarations.

## Recommended next actions

1. Apply the 12 SAFE mass-theory moves (§1a) — mechanical, low-risk.
2. Decide §1b conflicts case-by-case (split / drop-edge / accept).
3. Approve the 4 relocations (§2) per block.
