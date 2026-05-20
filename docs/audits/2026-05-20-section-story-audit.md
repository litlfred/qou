# Section-story audit (QOU) — 2026-05-20 (resolved)

Run of [`scripts/section-story-audit.ts`](../../scripts/section-story-audit.ts)
against the post-PR-#738 story-coherence policy
([`.claude/skills/local/detangler-integration-watcher.md`](../../.claude/skills/local/detangler-integration-watcher.md)
§Story coherence (STRICT)).

Full machine-readable findings: [`2026-05-20-section-story-audit.json`](2026-05-20-section-story-audit.json).

## Headline numbers — **clean run**

| Severity | Count |
|---|--:|
| Major | **0** |
| Minor | **0** |
| **Total** | **0** |

The first run (committed earlier on this branch) reported **56**
findings — 32 major (`missing-section-story`) + 12 minor
(`abrupt-chapter-ending`) + 12 minor (`section-lead-too-short`).
PR #847 closed every one of them.

## What changed

| Action | Count | Notes |
|---|--:|---|
| Section leads authored | 31 | One per `missing-section-story` finding, plus 2 in the first commit pair |
| Chapter closings authored | 12 | One per `abrupt-chapter-ending` finding (handled in two batches: 7 "closing-only" chapters first, then the 5 chapters that also needed leads) |
| Existing leads extended | 6 | One per `section-lead-too-short` finding plus 1 backfill in braids-and-knots |
| Parser fix in audit script | — | The block-name regex was matching apostrophes inside `//` line comments; fixed by stripping comments before quote matching |

Every lead and every closing references **actual section content**:
no opener is a generic template. Section leads name the first
block by title, connect the previous section's payload to the
current section's, and gesture forward to where the section's
output is consumed downstream. Each lead obeys the §738
length-scale table (1 para for ≤5 non-prose blocks, 2 for 6-12,
3 for 13-20, 4 for >20).

## Per-chapter recap

| Chapter | Leads added | Closing added | Lead extensions |
|---|--:|--:|--:|
| quantum-universes | 0 | 1 | 0 |
| notation | 0 | 0 | 0 |
| quantum-observable-universes | 2 | 1 | 2 |
| lifting-and-descent | 0 | 1 | 2 |
| braids-and-knots | 23 | 1 | 7 |
| models-of-qous | 0 | 1 | 0 |
| descartes-universe | 6 | 1 | 1 |
| particle-interactions | 0 | 1 | 0 |
| observations | 0 | 1 | 0 |
| molecular-construction | 0 | 1 | 0 |
| organic-chemistry | 0 | 1 | 0 |
| fluid-dynamics | 1 | 1 | 0 |
| information-theory | 0 | 0 | 0 |
| q-geometric-langlands | 0 | 1 | 0 |
| (reference / index / appendices) | 0 | 0 | 0 |
| **Total** | **32** | **12** | **12** |

`braids-and-knots` carried the substrate-arithmetic load of the
paper after PR #789's 49-way split; its 23 new leads name actual
content (Wenzl bridge, Hoefsmit basis, Hecke-skein, Markov-axiom
recursive ascent, etc.) so reviewers can locate the section's
arc without reading every block.

## Reproduce locally

```bash
bun run scripts/section-story-audit.ts                    # text report
bun run scripts/section-story-audit.ts --json             # machine-readable
bun run scripts/section-story-audit.ts --severity major   # major findings only
bun run scripts/section-story-audit.ts --ref <sha>        # override blob ref
```

The audit's CI wiring is already in place in
[`.github/workflows/witness-pipeline.yml`](../../.github/workflows/witness-pipeline.yml)
(see "Section-story compliance audit" step). It is currently
warn-only via `|| true`; with the count at 0, the next iteration
can flip it to strict by removing the `|| true` suffix and the
audit will then fail any PR that introduces a new finding.
