# Ch 5 (`models-of-qous`) — `fit-section-chapter` audit (2026-05-22)

Background-agent audit of every block in the post-restructure Ch 5
against the `fit-section-chapter` QA criterion (one-voice axis).
Dispatched from PR #882 session as part of the user-authorised
"Drain Ch 5 agent backlog only" task.

## Headline

**45 blocks** audited, **34 pass**, **11 fail** (75.6% pass rate).
Three structural patterns emerged — see §Top recommendations below.

## Per-block table

| label | kind | section | verdict | note |
|---|---|---|---|---|
| `sec:models-qou-intro` | prose | sec:physical-interpretation | pass | |
| `def:q-yang-mills-levi` | definition | sec:physical-interpretation | pass | |
| `conj:yang-mills-mass-gap` | conjecture | sec:physical-interpretation | **fail** | Competes with `prop:main-commutative-diagram` for "the main result" framing. Suggested: rename section to "Physical interpretation and headline results" OR split into its own subsection with `rem:gr-substrate-geometry`. |
| `rem:gr-substrate-geometry` | remark | sec:physical-interpretation | pass | |
| `prop:main-commutative-diagram` | proposition | sec:physical-interpretation | pass | |
| `prf:main-commutative-diagram` | proof | sec:physical-interpretation | pass | |
| `sec:archimedean-models-intro` | prose | sec:archimedean-realisations-and-wall | pass | |
| `ex:calabi-yau` | example | sec:archimedean-realisations-and-wall | pass | |
| `ex:ale` | example | sec:archimedean-realisations-and-wall | pass | |
| `ex:brings-surface` | example | sec:archimedean-realisations-and-wall | **fail** | Explicitly the Descartes-universe selection ("the next chapter will select"). Move to `descartes-universe/`. |
| `ex:cosmological-limits` | example | sec:archimedean-realisations-and-wall | **fail** | Physical limits of $q$ (big-bang / heat-death), not an archimedean *model construction*. Cluster with `rem:primordial-vortex` + `rem:geometric-drag`. |
| `ex:instanton` | example | sec:archimedean-realisations-and-wall | pass | |
| `ex:irreducible-connection` | example | sec:archimedean-realisations-and-wall | pass | |
| `rem:seiberg-witten` | remark | sec:archimedean-realisations-and-wall | **fail** | Bring's-surface / blow-up / $\chi=-6$ material. Move to `descartes-universe/`. |
| `rem:primordial-vortex` | remark | sec:archimedean-realisations-and-wall | **fail** | Cosmological / limiting observation. Cluster with `ex:cosmological-limits`. |
| `rem:geometric-drag` | remark | sec:archimedean-realisations-and-wall | **fail** | Mass-residue interpretation. Physics-realisation chapter or mass-formula chapter is a better home. |
| `ex:self-dual-curvature` | example | sec:archimedean-realisations-and-wall | pass | |
| `rem:c-substrate-via-levi` | remark | sec:archimedean-realisations-and-wall | pass | |
| `sec:webster-inner-product` | prose | sec:archimedean-realisations-and-wall | **fail** | Pure notation/definition. Belongs in `notation/` (notation register). |
| `prop:heisenberg-commutator` | proposition | sec:archimedean-realisations-and-wall | pass | |
| `rem:heisenberg-commutator` | remark | sec:archimedean-realisations-and-wall | pass | |
| `ex:reeb-decomposition` | example | sec:archimedean-realisations-and-wall | pass | |
| `rem:observation-archimedean` | remark | sec:archimedean-realisations-and-wall | pass | |
| `def:spatial-realization-functor` | definition | sec:archimedean-realisations-and-wall | pass | |
| `prop:categorical-archimedean-bridge` | proposition | sec:archimedean-realisations-and-wall | pass | |
| `prf:categorical-archimedean-bridge` | proof | sec:archimedean-realisations-and-wall | pass | |
| `rem:physicist-translation` | remark | sec:archimedean-realisations-and-wall | pass | |
| `rem:categorical-action-vs-chern-simons` | remark | sec:archimedean-realisations-and-wall | pass | |
| `prop:mostow-confinement` | proposition | sec:archimedean-realisations-and-wall | pass | |
| `rem:algebraic-geometric-rigidity-pairing` | remark | sec:archimedean-realisations-and-wall | pass | |
| `rem:encounter-literature-bridge` | remark | sec:archimedean-realisations-and-wall | pass | |
| `sec:categorical-reformulation` | prose | sec:non-archimedean-models | **fail** | TODO bullet outline, not non-archimedean content. Delete or rewrite. |
| `sec:enveloping-algebras` | prose | sec:non-archimedean-models | **fail** | TODO outline (Lusztig integral form / PBW basis). Not non-archimedean-specific. |
| `sec:p-adic-fields` | prose | sec:non-archimedean-models | **fail** | TODO outline. 3 of 4 blocks in this section are TODOs. |
| `ex:p-adic-realisation` | example | sec:non-archimedean-models | pass | |
| `sec:witt-vector-lifting` | prose | sec:witt-vector-lifting | pass | |
| `def:witt-vector-lift` | definition | sec:witt-vector-lifting | pass | |
| `prop:skew-poisson-integration` | proposition | sec:witt-vector-lifting | pass | |
| `prf:skew-poisson-integration` | proof | sec:witt-vector-lifting | pass | |
| `rem:witt-lift-qou` | remark | sec:witt-vector-lifting | pass | |
| `sec:finite-fields-intro` | prose | sec:finite-fields | pass | |
| `ex:finite-field-realisation` | example | sec:finite-fields | pass | |
| `sec:finite-fields` | prose | sec:finite-fields | **fail** | TODO bullet outline. Redundant with `sec:finite-fields-intro`. Delete or merge. |
| `sec:jones-polynomials` | prose | sec:finite-fields | pass | |
| `outro-models-of-qous` | prose | sec:models-of-qous-close | pass | |

## Top 3 structural recommendations

### Rec 1 — Split `sec:archimedean-realisations-and-wall` into 3 sub-sections (25 → 3 × ~8)

Suggested cut at `ex:self-dual-curvature` / `rem:c-substrate-via-levi`:

- **Group A: Archimedean witnesses** (intro + `calabi-yau`, `ale`, `instanton`, `irreducible-connection`, `self-dual-curvature`, `reeb-decomposition`).
- **Group B: Categorical → differential bridge** (`c-substrate-via-levi`, `webster-inner-product`, `heisenberg-commutator`+rem, `observation-archimedean`, `spatial-realization-functor`, `categorical-archimedean-bridge`+proof, `physicist-translation`, `categorical-action-vs-chern-simons`).
- **Group C: The wall narrative** (`mostow-confinement`, `algebraic-geometric-rigidity-pairing`, `encounter-literature-bridge`).

Three sections, each within the 3-18 detangler band. Restores the "wall" subsection's prior identity. Witnesses group becomes a clean catalogue uncluttered by the misclassified blocks below.

### Rec 2 — Relocate Descartes-coded blocks to `descartes-universe/`

`ex:brings-surface`, `rem:seiberg-witten`, `rem:primordial-vortex`, `rem:geometric-drag` all carry Bring's-surface / $\chi=-6$ / exceptional-divisor / mass-residue content explicitly flagged as "next chapter" material. Their presence in a *general* archimedean-models catalogue forces the chapter to preview the Descartes/Archimedean-universe chapter, breaking the catalogue framing.

Cross-references this with the §3 chapter-reorg proposal — these 4 blocks form natural seed content for a new Ch 3 "Bring's surface and coordinate systems" if Rec is taken there.

### Rec 3 — Purge or rewrite the 4 TODO-outline prose blocks

`sec:categorical-reformulation`, `sec:enveloping-algebras`, `sec:p-adic-fields`, and `sec:finite-fields` are unfinished bullet outlines. **3 of 4 blocks in `sec:non-archimedean-models` are TODOs** — that section is structurally hollow. Either:

- (a) Rewrite each as a real lead-in paragraph mirroring `sec:archimedean-models-intro`, OR
- (b) Delete and let the example blocks speak for themselves with no section intro.

## Minor pattern

`ex:cosmological-limits` + `rem:primordial-vortex` + `rem:geometric-drag` together form a **"physical / limiting-regime" cluster** orthogonal to the archimedean-model catalogue. If Rec 2 is taken, these three (plus `conj:yang-mills-mass-gap`) could form a fifth subsection "Physical regimes and limits" — or be moved into a physics chapter if one exists.

## Sidecar update

This audit produced a structured per-block verdict + note. The
corresponding `agent`-reviewer entries should be written to each
block's `<block>.qa.json` for `fit-section-chapter`, but this
report intentionally batches the findings into a single doc for
author review rather than per-block sidecar updates. Per
`one-voice-integration-watcher.md` multi-reviewer protocol, the
author or follow-up agent dispatch should write the sidecar
entries from this audit verdict.

## Audit provenance

- **Dispatched from:** PR #882 session, branch `claude/eager-gauss-S36Uk`.
- **Sub-agent task ID:** `aa3174573e8e9d2e5`.
- **Wall-clock:** ~3 minutes.
- **Criterion:** `fit-section-chapter` (one-voice axis, `automated: false`,
  `default_severity: major`).
- **Branch HEAD at audit time:** `2b7a75d8` (after the Ch 5
  structural fixes + chapter-reorg proposal landed).
