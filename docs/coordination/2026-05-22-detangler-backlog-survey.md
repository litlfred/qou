# Detangler backlog survey — 2026-05-22 watcher session

**Branch:** `claude/amazing-hopper-c0MLc`
**Watcher:** `local/detangler-integration-watcher`
**Session start:** 2026-05-22T14:46:17Z (main HEAD at start: `236d742f`)
**Session refresh:** 2026-05-22T14:54:58Z (main HEAD after PR #879 merge: `07e272f4` — docs-only, out-of-scope per Slot B)

## Scope

The detangler watcher ran §5l Resume protocol against a fresh queue
(no `reviewed_up_to` pointers). Backlog discovery (Slot G) ran two
specialists in parallel:

1. `content/pipeline/content-graph-analysis.py --proposals` →
   136 reorganisation proposals.
2. `content/pipeline/block-density-audit.py <paper>` across all
   four paper packages → 1858 density findings (R1 / R2 / R3
   classification).

This doc surveys the four candidate work clusters and records the
recommended dispatch + per-cluster author asks. **No code surgery
has landed yet on this branch** — the survey is the deliverable.
Follow-up branches will execute each cluster's discharge band.

## Graph baseline snapshot (main HEAD `07e272f4`)

| Heuristic | Count | Preview-excluded | Comment |
|---|---:|---:|---|
| H1 forward-refs | 685 | 685 | 0 sourced from `intro` / `notation` |
| H2 cross-chapter | 20 | 20 | includes 3 known architectural-accepts (see [2026-05-19-detangler-architectural-acceptances.md](2026-05-19-detangler-architectural-acceptances.md)) |
| H3 cross-section | 15 | — | within 3-section span |
| H4 sparse sections | 33 | — | many appendix / index / glossary singletons |
| H5 dense sections | 18 | — | top: `sec:topological-mass-spectrum` (33), `sec:descartes-condition` (28) |
| H6 isolated blocks | 6 | — | candidates for `prose` / cross-link |
| H7 remark-ratio | 42 | — | drift outside 2:1 band |

## Cluster 1 — Move-earlier batch (P28–P37)

10 cross-chapter / intra-chapter move proposals; collectively
eliminate ~80 H1 forward references. **None are auto-discharge**
per Slot E — every move is cross-chapter and rewires `uses[]`
across the categorical / archimedean wall, so all require Slot F
ask.

| # | Block | Current chapter | Target chapter | Fwd-refs fixed | Wall-direction |
|---:|---|---|---|---:|---|
| P28 | `prop:operator-selection-lp` | particle-interactions | braids-and-knots `sec:hoefsmit-convergence-atomic` | 14 | post-wall → pre-wall |
| P29 | `prop:gb-spectral-sequence` | braids-and-knots | lifting-and-descent `sec:mass-brane` | 12 | pre-wall → bridge |
| P30 | `thm:topological-mass` | braids-and-knots | lifting-and-descent `sec:archimedean-lifting` | 8 | pre-wall → bridge |
| P31 | `thm:markov-trace-factorization` | particle-interactions | braids-and-knots `sec:phi-q-markov-schur-weyl-tower` | 8 | post-wall → pre-wall |
| P32 | `def:atomic-braid` | particle-interactions | braids-and-knots `sec:skein-particle-generation` | 8 | post-wall → pre-wall |
| P33 | `prop:confinement-sdp` | particle-interactions | braids-and-knots `sec:alpha-k-procedure` | 7 | post-wall → pre-wall |
| P34 | `def:motivic-substrate` | braids-and-knots | lifting-and-descent `sec:yekutieli-lifting` | 7 | pre-wall → bridge |
| P35 | `conj:gb-depth-period-correspondence` | braids-and-knots | braids-and-knots `sec:archimedean-realization-kashaev` | 7 | **intra-chapter** (only one in batch) |
| P36 | `prop:sw-period-thimble-equivalence` | descartes-universe | braids-and-knots `sec:kashiwara-jones-quantum-dilog` | 6 | post-wall → pre-wall |
| P37 | `prop:lagrange-resolvent-transform` | descartes-universe | braids-and-knots `sec:braid-involutions` | 6 | post-wall → pre-wall |

**Architectural-wall observation.** 7 of 10 moves go post-wall →
pre-wall (particle-interactions or descartes-universe → braids-and-knots).
The 2026-05-19 acceptances doc records that forward edges in the
opposite direction (braids → descartes) are wontfix-architectural
(substrate → consumer is canonical). These reverse-direction moves
would shift canonical homes of definitions to the pre-wall chapter,
which is structurally legitimate (definitions stay generic-`R`,
consumers stay archimedean) — but every one of them needs an
architectural check: does the moved block's own `uses[]` chain
remain valid in the new home (no backward archimedean dependencies)?

**Recommendation (Slot F batch).** Surface as a single 4-option
ask: (a) execute all 10 as proposed, (b) execute only intra-chapter
P35, (c) execute only the 3 bridge-chapter moves (P29/P30/P34 →
lifting-and-descent) — the structurally cleanest target, (d) per-move
review. Default = (c) — bridge-chapter is the safest target.

## Cluster 2 — R3 large embedded tables

433 density findings; concentrated in ~10 host blocks:

| Host block | Chapter | Tables | Top size |
|---|---|---:|---:|
| `recursive-atom-knot-atlas` | appendix-knot-periodic-table | 12+ | 92 rows |
| `definition-index` | index-of-definitions | 3+ | 274 rows |
| `amc-natural-elements-table` | appendix-atomic-mass-calculations | 1 | 92 rows |

**Per Slot E auto-discharge criterion** the extracts are mechanical
*if* each split produces a stable `tbl:` block with no R1 hit on
either side and `bun run validate` exits clean. But every extract
adds:

1. A new `.ts` + `.md` sibling pair (`kind: "table"`).
2. A blocks[] entry in the chapter manifest.
3. A cross-ref replacement in the host `.md`.

For `recursive-atom-knot-atlas` (4926 lines of .md, 12+ tables),
that's ~36 new files + 12 cross-refs + 12 manifest entries — large
enough that the "mechanical sweep" exception applies (single bulk
commit > 50 files acceptable for uniform changes per AGENTS.md
§"Exception: batch audit-job runs").

**Recommendation.** Execute on a dedicated follow-up branch
`claude/detangler-r3-table-extracts-2026-05-22` so the bulk-extract
commit doesn't muddy this branch's survey. Start with
`amc-natural-elements-table` (single table — smallest case,
proof-of-concept).

## Cluster 3 — R1 topic-mix in `particle-interactions`

426 multi-topic findings concentrate in the **particle-interactions**
chapter: most blocks score 3-8 keyword hits for `braids-and-knots`
or `descartes-universe` and only 0-2 for the home chapter. The
audit detector reports e.g.:

> `operator-selection-lp` | particle-interactions | braids-and-knots | Block has 3 keyword hits for 'braids-and-knots' but only 0 for its home chapter…
>
> `transfer-matrix-operator` | particle-interactions | braids-and-knots | Block has 8 keyword hits for 'braids-and-knots' but only 0…
>
> `nuclear-groebner-reduction` | particle-interactions | descartes-universe | Block has 7 keyword hits for 'descartes-universe' but only 0…

**Architectural question (Slot F):** is the particle-interactions
chapter:

- **(a) Correctly scoped** — chapter blocks compose categorical
  + archimedean primitives from earlier chapters into nuclear-
  physics observables; keyword "leakage" is expected because every
  block legitimately references pre-wall (Hecke, braids) and
  post-wall (mass tables, Brings surface) machinery? Then the 426
  R1 findings are detector artefacts, not real topic-mixing.
- **(b) Over-broad** — many blocks really do belong in
  braids-and-knots (transfer matrices, GB reduction) or
  descartes-universe (mass derivations); the chapter accreted
  material that should be redistributed?
- **(c) Mixed** — some genuine R1 (operator-selection-lp moves to
  braids — overlaps with cluster-1 P28!); some artefact (
  `gram-weighted-qvalue` legitimately spans both axes).

**Cluster-1 ↔ cluster-3 overlap.** P28 (move `operator-selection-lp`)
and P31 / P32 / P33 (move other particle-interactions blocks to
braids) **already address** part of the cluster-3 finding via the
move route. If cluster-1's batch ask is answered as (a) execute-all
or (c) bridge-only-but-include-P31/32/33, cluster-3's R1 count
drops accordingly. **The two clusters should be answered together.**

**Recommendation.** Defer cluster-3 to after cluster-1 lands —
re-audit R1 from the new graph baseline. The residual R1 (if any)
becomes its own discharge cycle.

## Cluster 4 — Split-dense (P1–P18)

18 sections > 18 blocks. Per Slot F template, every split needs a
per-new-section story draft. Below are draft story summaries for
the 5 highest-impact sections, sufficient for batch author approval:

### P15 — `sec:topological-mass-spectrum` (33 blocks → 3-way split)

| New section | Story (1-sentence) | Approx block count |
|---|---|---:|
| `sec:topological-mass-spectrum-foundations` | Topological mass formula, the Wedderburn decomposition, and the Markov trace as the pairing that turns a knot into a mass; reader has the Hecke algebra in hand, leaves with `|tr_M(β)|` as the mass primitive. | 11 |
| `sec:topological-mass-spectrum-evidence` | Categorical and numerical evidence: the Brings-surface period integrals, the SW-3-root rational integrand, and the algebraic-volume specialisation — turning the formula into testable predictions. | 11 |
| `sec:topological-mass-spectrum-spectrum` | The knot-particle spectrum that the formula generates: pre-stability table, magic-shell stabilisation, and the periodic table demand. Sets up §descartes-condition (next section). | 11 |

### P13 — `sec:descartes-condition` (28 blocks → 3-way split)

| New section | Story | Blocks |
|---|---|---:|
| `sec:descartes-condition-statement` | The Descartes condition, the lepton-mass spectrum it produces, and the categorical reason it must hold (Brings discriminant locus). | 9 |
| `sec:descartes-condition-derivation` | Algebraic derivation: Brings substructure, Lagrange resolvent transform, and the figure-eight-knot specialisation. | 10 |
| `sec:descartes-condition-numerics` | Numerical specialisation at `q_0`, lepton mass comparisons with CODATA, and the Δ-skein bridge to baryon masses. | 9 |

### P11 — `sec:classical-limit` (25 blocks → 2-way split)

| New section | Story | Blocks |
|---|---|---:|
| `sec:classical-limit-construction` | KLR → KL decategorification functor, the motivic substrate, and the procedure for taking `q → 1` while preserving the canonical basis. | 13 |
| `sec:classical-limit-statistics` | Where the categorical substrate recovers Pauli / Bose-Einstein: braid-action specialisation, particle-statistics emergence, and the gauge-group classical limit. | 12 |

### P18 — `sec:beta-decay-observations` (25 blocks → 2-way split)

| New section | Story | Blocks |
|---|---|---:|
| `sec:beta-decay-categorical` | Categorical β-decay mechanism: skein-step inventory, parity-violation skein, and the canonical decay-channel set. | 12 |
| `sec:beta-decay-predictions` | Numerical predictions at `q_0`: Q_β values, lifetime predictions vs ENSDF, and CP-violation evidence. | 13 |

### P17 — `sec:mass-predictions` (24 blocks → 2-way split)

| New section | Story | Blocks |
|---|---|---:|
| `sec:mass-predictions-method` | Mass-prediction methodology: chain-of-derivation, atomic-mass calculator interface, and the per-isotope braid-word inventory. | 12 |
| `sec:mass-predictions-comparison` | CODATA comparisons: per-element status, residual-error analysis, and the 100× target dashboard interpretation. | 12 |

**Remaining 13 splits (P1–P10, P12, P14, P16):** drafted on
request; the pattern above scales.

**Recommendation.** Surface as ONE consolidated Slot F batch ask
that links to this doc; user replies with a per-section approval
table (accept-draft / accept-with-rewrite / re-split-differently /
defer). Execute on a dedicated follow-up branch
`claude/detangler-section-splits-2026-05-22` because each split
modifies the chapter manifest substantially and would dwarf this
survey doc.

## Recommended dispatch sequence

1. **This branch (survey doc — landed here)**: capture state + asks.
2. **Cluster 1 batch ask** → answered → execute on
   `claude/detangler-moves-bridge-batch-2026-05-22`.
3. **Cluster 2 R3 sweep** → execute on
   `claude/detangler-r3-table-extracts-2026-05-22` (deferrable;
   purely mechanical).
4. **Cluster 4 split-batch ask** → answered → execute on
   `claude/detangler-section-splits-2026-05-22`.
5. **Cluster 3 R1 re-audit** → run after cluster 1 lands; only the
   residual goes to its own discharge cycle.

This survey-first sequence follows the AGENTS.md guidance to
combine related work and minimise their creation: each follow-up
PR is dedicated to one cluster, so review burden per PR stays
low. Survey doc lands first so the asks are durable across
sessions.

## Architectural acceptances carried forward

From [`2026-05-19-detangler-architectural-acceptances.md`](2026-05-19-detangler-architectural-acceptances.md),
still in force:

1. Ch 17 `app:knot-operations` — 100% cross-section ratio (reference appendix).
2. 29 forward edges Braids → Descartes (canonical substrate → consumer direction).
3. `prop:sw-3root-rational-integrand` → `rem:color-tube-cubic` (descartes-native cubic).

These are NOT re-questioned in this survey.

## Queue state (post-survey)

| Cluster | Queue status |
|---|---|
| 1 (moves) | 10 items added as `status: needs-author`, all `severity: major` |
| 2 (R3 tables) | survey-only; concrete items added when sweep branch starts |
| 3 (R1 topic-mix) | 1 architectural-question item; blocked on cluster-1 outcome |
| 4 (splits) | 18 items added as `status: needs-author`, 5 with draft stories |

`todos/detangler-integration-watcher-queue.json` is the source of
truth; this doc is the human-readable narrative.

## Subscribed PRs (this session)

| PR | Title | Detangler-scope? |
|---:|---|---|
| #878 | canonical-watcher Wenzl-LR consumer docstring | No |
| #879 | 210× scale-gap audit third pass | No (merged this session, out-of-scope) |
| #880 | proof-integration-watcher MCP PATH fix | No |

PRs #818 + #872 subscribe attempts returned "Could not subscribe"
(likely transient gateway issue or PR archive state); retry on
next watcher session.
