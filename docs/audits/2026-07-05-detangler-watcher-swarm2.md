# Detangler-integration-watcher swarm-2 — 2026-07-05

Fresh `detangler-integration-watcher` run against `origin/main`
(HEAD `bbf659f6f6`, 33 chapters / 305 sections / 3002 blocks),
reconciling the four backlog beans **e5tn / flus / foxn / yjxk**
(queued 2026-06-21 at `565be78e`) against the current graph.

Lane: this pass emits `detangler-*` sidecar criteria + this audit
doc only. No content `.md`/`.ts`/`.lean` edits, no bean closures
(human-only, §4a).

## 1. Current graph snapshot

`content/pipeline/content-graph-analysis.py --json` (raw H1–H7):

| Heuristic | Raw count | Curated defect |
|-----------|-----------|----------------|
| H1 forward-ref | 571 | see classifier below |
| H2 cross-chapter-fwd | 29 chapter-pair edges | 0 (all architectural) |
| H4 sparse section | 36 | ~10 real (rest glossary/notation/sim/authors-note — excluded by design) |
| H5 dense section | 27 | 27 candidates > 18 blocks |
| H6 isolated block | 47 | mostly standalone examples (INFO) |
| H7 remark ratio | 53 | info only |

`computations/forward_ref_classifier.py` (the H1 severity gate):

```
LOGICAL DEFECT    1
logical-waived   72  (surreal lift / FOUNDATIONAL_LATE — sanctioned)
storytelling    199  (motivation / interpretation / cite — benign)
structural       47  (appendix / framing chapter — benign)
```

Only the **1 LOGICAL DEFECT** is an actionable forward-ref:

- `fluid-dynamics/prop:two-vortex-channel-algebra`
  → `information-theory/def:van-der-waals-hopf-channel`
  (severity `logical`, L-dependency). NEW since the 2026-06-21
  queue — not one of the three foxn items.

## 2. Bean-by-bean reconciliation

### foxn — forward-ref (3 items) → **all 3 resolved; 1 new**

The three queued LOGICAL forward-refs
(`def:skein-resolution-obstruction`,
`def:embeddable-knot-operator`,
`def:quark-antiquark-production`) no longer classify as `logical`
on current main — resolved (demoted/inverted upstream). The
classifier now reports a single, different logical defect
(`prop:two-vortex-channel-algebra`, §1). foxn's original scope is
clear; the residual is the one new edge (queued here as a
`detangler-*` sidecar on the source block; disposition — promote
target, demote to `interprets`, or `FOUNDATIONAL_LATE` — is an
author/editor call, not a QA-lane fix).

### e5tn — cross-chapter-forward (12 items) → **unchanged; all `wontfix: architectural`**

12 queued items are H2 chapter-pair aggregates (mass-cluster
result-callbacks, Bring foundational coupling, `models-of-qous`
framing). Current H2 = 29 raw edges across the same architectural
pairs; the classifier folds them into `storytelling` /
`structural` / `L-result-callback` (53) — none are new logical
defects. Consistent with the 2026-06-29 triage
(`docs/audits/2026-06-29-e5tn-cross-chapter-forward-triage.md`).
Ready to close (human-only).

### flus — isolated blocks (18 items) → **14 of 18 de-isolated; 4 remain; +43 new H6**

Of the 18 queued isolated blocks, **14 are no longer isolated** on
current main (wired up by the flus de-isolation PRs #2597 / #2614
and sibling work):

> tilting-module-rigidity, cyclotomic-l-value-decomposition,
> gram-matrix-h3-symbolic, interface-knot-markov-z,
> jonquiere-cyclotomic-tate-rationality, n-equals-1-vacuous-magic,
> polynomial-bar-involution, q-plancherel-asymptotic-skeleton,
> skein-bar-antisymmetry, spectrahedral-phase-collapse,
> gauge-conformal-invariance, graded-baer-star-Hq,
> confinement-category, prf:mi-sw-abelianisation-cartan

**4 still isolated** (flus residual):
`prop:knot-operator-transition`, `prop:lr-coefficient-hecke`,
`prop:mass-element-nf`, `prf:observation-energy`.

The current graph carries **47 H6 isolated blocks total**, so **43
are new** relative to the queue — most are standalone `example` /
`remark` blocks (H6 severity INFO, "verify intentionally
standalone"), not defects. flus should be re-scoped to the 4
residual + a triage pass over the 43 new (bulk INFO). The two
data-integrity bugs flus flagged (missing `def:algebraic-primality`,
missing `lem:mi-sw-abelianisation-cartan` statement block) are
content-lane, out of this QA pass.

### yjxk — dense/sparse sections (21 items) → **superseded by current 27 dense + 36 sparse**

The 2026-06-21 snapshot (1 dense + 20 sparse) is stale. Current:

- **27 dense sections** (> 18 blocks) — real split candidates
  incl. `sec:cyclotomic-depth-3-trilog` (31), `sec:substrate-parameter`
  (19), `sec:qou-definition`, `sec:nuclear-stability-decay`,
  `sec:mass-algebraic-markov-gram`, `sec:categorical-mass-eigenspaces`,
  `sec:transfer-beta-decay`, … (full list in this pass's graph JSON).
- **36 sparse sections** (< 3 non-prose) — of which ~26 are
  by-design exclusions (`sec:glossary-*`, `sec:notation-*`,
  `sec:simulations`, `sec:authors-note`, `sec:chapter-overview`,
  `sec:amc-summary`, `sec:*-orphan-reconnect`). ~10 are genuine
  merge candidates (`sec:confinement-selection`,
  `sec:mass-algebraic-consolidated`, `sec:mba-chain-map`,
  `sec:hoefsmit-convergence-magic-shells`,
  `sec:categorical-braiding-hecke-eigenbasis`,
  `sec:hadron-level-knot-table`, `sec:localized-knots`,
  `sec:strangelet-stability`, `sec:tm-general-form`,
  `sec:tm-inductive-construction`).

Section split/merge is Author-assist (never auto-discharge). yjxk
should be re-scoped to the current 27 + ~10 = ~37 candidates; the
per-section `detangler-section-band` sidecar carries the machine
verdict.

## 3. Sidecar emission

`detangler-*` criteria are 8 automated qa-sweep checkers
(`detangler-no-forward-ref`, `-section-band`, `-no-xchapter-fwd`,
`-archimedean-wall`, `-block-tanglement`, `-graph-energy`,
`-topic-coherence`, `-no-dependency-cycle`). 15 of the 20
per-block queue targets already carried all 8 fresh (they resolve
to `n/a` per block — the real detection is graph-level, not
per-block). This pass **emitted the 8 detangler criteria on 6
blocks** that lacked them or are the new residual:

| Block | Section | Reason |
|-------|---------|--------|
| `cyclotomic-l-value-decomposition` | q-geometric-langlands | was 0/8 |
| `gram-matrix-h3-symbolic` | particle-interactions | was 0/8 |
| `interface-knot-markov-z` | mass-theory | was 0/8 |
| `skein-bar-antisymmetry` | climax-volume-mass | was 0/8 |
| `gauge-conformal-invariance` | predicted-spectra | was 0/8 |
| `two-vortex-channel-algebra` | fluid-dynamics | new logical fwd-ref source |

(The per-block checkers return `n/a`; the graph-level verdicts live
in §1–§2 and the beans. Section-level dense/sparse and
cross-chapter findings have no per-block sidecar and stay in the
bean/queue ledger.)

## 4. Residual work (for the beans; human triage)

1. **foxn**: 1 new logical fwd-ref
   (`two-vortex-channel-algebra → van-der-waals-hopf-channel`) —
   promote / demote-to-`interprets` / `FOUNDATIONAL_LATE`.
2. **flus**: 4 residual isolated + triage 43 new H6 (bulk INFO);
   2 data-integrity bugs (missing decl blocks) — content lane.
3. **yjxk**: re-scope to current 27 dense + ~10 real sparse.
4. **e5tn**: ready to close (all architectural).
