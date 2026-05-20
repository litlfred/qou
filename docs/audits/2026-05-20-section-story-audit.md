# Section-story audit (QOU) — 2026-05-20

First run of [`scripts/section-story-audit.ts`](../../scripts/section-story-audit.ts)
against the post-PR-#738 story-coherence policy
([`.claude/skills/local/detangler-integration-watcher.md`](../../.claude/skills/local/detangler-integration-watcher.md)
§Story coherence (STRICT)).

Full machine-readable findings: [`2026-05-20-section-story-audit.json`](2026-05-20-section-story-audit.json).

This report reflects the post-Copilot-review version of the audit (PR
#847): fluid-dynamics now correctly reported with 1 major finding (a
prior version of this report claimed 0); `section-lead-too-short` now
covers all bands including ≤5; the `abrupt-chapter-ending` detail
string was corrected from "not a closing prose / remark" to "not a
closing prose block"; unresolved block kinds are conservatively treated
as non-prose so a parse failure surfaces as a finding rather than
silently passing.

## Headline numbers

| Severity | Count |
|---|--:|
| **Major** | 32 |
| Minor | 24 |
| **Total** | 56 |

| Finding kind | Count |
|---|--:|
| `missing-section-story` | 32 |
| `abrupt-chapter-ending` | 12 |
| `section-lead-too-short` | 12 |
| `generic-section-name` | 0 |
| `missing-chapter-intro` | 0 |
| `section-lead-block-title-list` | 0 |
| `missing-chapter-manifest` | 0 |

The 4 zero-count kinds confirm previous detangler-cleanup tranches
(PR #731, PR #789) and PR #738's policy adoption have already retired
their respective patterns: every chapter loads cleanly, every chapter
has an opening narrative, no section is named generically (`-part-N`,
`-extras`, `-misc-N`), and no existing lead reads as a block-title
list. The remaining work is **content addition** (write the missing
leads), not **structural cleanup**.

## Per-chapter findings

| Chapter | `missing-section-story` | `abrupt-chapter-ending` | `section-lead-too-short` |
|---|--:|--:|--:|
| `braids-and-knots` | **23** | 1 | 7 |
| `descartes-universe` | 6 | 1 | 1 |
| `quantum-observable-universes` | 2 | 1 | 2 |
| `fluid-dynamics` | 1 | 1 | 0 |
| `lifting-and-descent` | 0 | 1 | 2 |
| `models-of-qous` | 0 | 1 | 0 |
| `molecular-construction` | 0 | 1 | 0 |
| `observations` | 0 | 1 | 0 |
| `organic-chemistry` | 0 | 1 | 0 |
| `particle-interactions` | 0 | 1 | 0 |
| `q-geometric-langlands` | 0 | 1 | 0 |
| `quantum-universes` | 0 | 1 | 0 |

`braids-and-knots` dominates the major-findings list — it carries the
substrate-to-knots reasoning load for the paper. After PR #789's
49-way split it has well-named sections, but most lack the prose lead
that motivates each section's blocks.

## How to use this report

1. **The audit is read-only.** No drafts are produced — story content
   is editorial, and per #738 §Auto-discharge safety net "auto-fix a
   missing chapter intro without surfacing the draft is forbidden".
2. **Pick a target.** Most efficient sweep is one chapter at a time;
   start with `braids-and-knots` (23 major findings) or a smaller
   chapter to validate the pattern.
3. **For each `missing-section-story`:** open the section's chapter
   manifest, insert a 1- to 4-paragraph prose block at the front of
   `blocks[]`, and author the new prose `.md`. Lead length scales with
   section size per the §738 table:

   | Non-prose blocks | Paragraphs | Roles |
   |---|---|---|
   | ≤ 5 | 1 | opener (where we are + question this section settles) |
   | 6–12 | 2 | + structural moves |
   | 13–20 | 3 | + stakes / consumer |
   | > 20 | 4 | + subtleties / scope |

4. **For each `abrupt-chapter-ending`:** add (or promote) a closing
   prose block to the last section.

## Reproduce locally

```bash
bun run scripts/section-story-audit.ts                    # text report
bun run scripts/section-story-audit.ts --json             # machine-readable
bun run scripts/section-story-audit.ts --severity major   # major findings only
bun run scripts/section-story-audit.ts --ref <sha>        # override blob ref
```

When run in CI, the `--ref` defaults to `$GITHUB_SHA` or `$GITHUB_REF_NAME`
so the blob URLs in the report point at the exact revision audited.
Exit code = major finding count (capped at 255), so the audit can be
wired into CI as a soft quality gate.
