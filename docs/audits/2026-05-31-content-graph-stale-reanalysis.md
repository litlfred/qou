# Content-graph + stale-state reanalysis — 2026-05-31

A full reanalysis of the QOU content graph (post-PR-#847 / -#1320 / etc.)
plus a stale-state catalogue for the audit and witness layers.  Closes
item 6 of the queue requested 2026-05-31; downstream remediation is
tracked in the per-bucket follow-up sections below.

Also lands one small parser fix in
[`content/pipeline/content-graph-analysis.py`](../../content/pipeline/content-graph-analysis.py)
that brings the analyser into sync with
[`scripts/section-story-audit.ts`](../../scripts/section-story-audit.ts):
both now recognise `Object.freeze({...})` as a section literal (one
section in `braids-and-knots.ts`, +5 blocks).

## Headline numbers

| Metric | Value |
|---|--:|
| Chapters | **30** |
| Sections | **280** |
| Blocks | **2 430** |
| Block edges (uses + interprets + proof + example) | 3 651 |
| Cross-chapter edges | 1 028 |
| Cross-section edges | 1 909 |
| H1 forward references | **503** |
| Content-graph findings (H1–H7) | **666** |
| Audit MDs on disk (`docs/audits/*.md`) | 391 |
| Witness JSONs on disk | ~ 1 200 |
| Dated witnesses (have `computedAt`) | 722 |

## Content-graph findings by heuristic

The detangler-watcher heuristics (per
[`detangler-integration-watcher`](../../.claude/skills/local/detangler-integration-watcher.md)
§Slot D) catalogue the structural debt:

| Heuristic | Count | What it flags |
|---|--:|---|
| **H1 — forward ref** | **503** | A block uses a label that lives in a later section / chapter |
| **H7 — remark / example ratio** | 56 | Section's remark + example density is outside the 2:1 band |
| **H4 — sparse section** | 31 | Section has < 3 blocks |
| **H6 — isolated block** | 30 | Block has no incoming or outgoing edges |
| **H2 — cross-chapter edge** | 24 | Edge crosses a chapter boundary without an explicit bridge |
| **H3 — cross-section edge** | 17 | Edge crosses > 3 sections |
| **H5 — dense section** | 5 | Section has > 18 blocks |

H1 dominates (75% of findings).  This is consistent with the fact that
the substrate-arithmetic layer (mass-theory, predicted-spectra,
particle-interactions) repeatedly references the chapter-cycle's
substrate primitives (Hecke skein, Markov trace, Yekutieli tower, etc.)
which live earlier in the document.  Many H1 references are intended
structural forward-pointers — narrative cross-references rather than
substrate dependencies — and the watcher's discharge bands already
treat them as **wontfix: architectural** when they cross the
substrate / numerical wall.

## Stale audit MDs

| Bucket | Count |
|---|--:|
| All audit MDs | 391 |
| Dated 2026-05 (the active month) | 375 |
| Mentioning a *dissolved* chapter (`algebraic-substrate`, `encounter`) | **9** |
| Tools / dashboards still consuming a stale audit | 0 (none verified) |

The 9 audits referencing dissolved chapters are:

| File | Stale ref |
|---|---|
| `2026-05-01-math-framework-deep-audit.md` | `algebraic-substrate` |
| `2026-05-02-forward-derivation-pre-archimedean.md` | `algebraic-substrate` |
| `2026-05-02-p3-1-policy-options.md` | `algebraic-substrate` |
| `2026-05-02-self-conj-support-reframing.md` | `algebraic-substrate` |
| `2026-05-09-conjecture-closure-tractability.md` | `algebraic-substrate` |
| `2026-05-18-bw-coef-removal-manifest.md` | `encounter` |
| `2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md` | `encounter` |
| `2026-05-22-ch5-fit-section-chapter-audit.md` | `encounter` |
| `derivation-chain-mass-tower.md` | `algebraic-substrate` |

**Recommendation:** these 9 are *historical-record* audits (they document
the state at the time of the dissolution).  Leave them in place but add
a one-line `Status: superseded by PR #731` banner at the head of each.
A follow-up cleanup PR should also relocate them to
`docs/audits/_superseded/` to keep the index navigable.

## Stale witness JSONs

| Bucket | Count |
|---|--:|
| Witnesses with `computedAt` | 722 |
| `computedAt` in 2026-03 | 2 |
| `computedAt` in 2026-04 | 21 |
| `computedAt` in 2026-05 | 699 |

The 2 March witnesses and 21 April witnesses are candidates for
regeneration.  Spot-checking shows they belong to compute axes that
have not been touched recently (probe results, exploratory audits);
their staleness is benign as long as no current block references them
via `computation.witness`.  The witness-pipeline drift detector
(implemented in `computations/run_pipeline.py::_is_stale`)
identifies stale witnesses by comparing the witness `scriptHash` against
the current script version and detecting q₀-shape drift.
**Recommendation:** do not bulk-regenerate; let the pipeline's staleness
check flag the genuine consumers.

## Recommendations

1. **Section splits remain useful.** 5 dense sections (H5) plus 31
   sparse sections (H4) are well within the editorial backlog the
   detangler-watcher already tracks; no new bulk-split effort is
   warranted before each chapter cycle settles.
2. **H1 cleanup is not a project.** Of the 503 forward refs, most are
   intentional cross-references between chapters that share a substrate
   primitive (Hecke skein → mass theory → predicted spectra).  A
   per-chapter sweep that promotes each forward ref into either
   (a) an explicit `\cite{}` or (b) a `tags: ['archimedean-bridge']`
   annotation would close the watcher's backlog without disrupting the
   narrative.
3. **Witness layer is healthy.** 23 March / April witnesses out of 722
   is < 4% staleness; the witness-pipeline drift detector is the right
   tool to surface the actionable ones.
4. **9 historical audits — add `Status: superseded`.** Cheap cleanup;
   improves audit-tree navigability without losing institutional memory.
5. **Parser parity.** Both audit tools now handle `Object.freeze({...})`
   sections.  Future content-pipeline scripts should adopt the same
   `(?:\bsection|Object\.freeze)` regex when extracting sections — the
   `\b` word boundary keeps it from matching `section` as a substring
   of unrelated identifiers (e.g. `intersection(`).

## Reproduce

```bash
# Content-graph analysis (full JSON output)
cd content && python3 pipeline/content-graph-analysis.py --json
# Section-story audit (consumed by witness-pipeline.yml strict gate)
bun run scripts/section-story-audit.ts
# Witness drift detection (per existing CI)
python3 computations/compute_audit_scan.py
```
