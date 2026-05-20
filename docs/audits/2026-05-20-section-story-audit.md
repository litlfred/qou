# Section-story audit (QOU) — 2026-05-20

First run of [`scripts/section-story-audit.ts`](../../scripts/section-story-audit.ts)
against the post-PR-#738 story-coherence policy
([`.claude/skills/local/detangler-integration-watcher.md`](../../.claude/skills/local/detangler-integration-watcher.md)
§Story coherence (STRICT)).

Full machine-readable findings: [`2026-05-20-section-story-audit.json`](2026-05-20-section-story-audit.json).

## Headline numbers

| Severity | Count |
|---|--:|
| **Major** | 31 |
| Minor | 20 |
| **Total** | 51 |

| Finding kind | Count |
|---|--:|
| `missing-section-story` | 31 |
| `abrupt-chapter-ending` | 12 |
| `section-lead-too-short` | 8 |
| `generic-section-name` | 0 |
| `missing-chapter-intro` | 0 |
| `section-lead-block-title-list` | 0 |

The 3 zero-count kinds confirm previous detangler-cleanup tranches
(PR #731, PR #789) successfully retired their respective patterns:
no chapter is missing an intro, no section is named generically
(`-part-N`, `-extras`, `-misc-N`), and no lead reads as a block-title list.
The remaining work is **content addition** (write the missing leads),
not **structural cleanup**.

## Per-chapter major findings

| Chapter | `missing-section-story` | Notes |
|---|--:|---|
| `quantum-observable-universes` | 2 | `sec:q-resolvent-wick`, `sec:q-special-functions` |
| `braids-and-knots` | **20** | Biggest concentration; 20 of 49 sections lack a lead |
| `descartes-universe` | 1 | `sec:diophantine-arithmetic` |
| `particle-interactions` | 1 | `sec:reeb-categorical-foundations` |
| `observations` | 5 | Five physical-prediction sections |
| `molecular-construction` | 1 | `sec:nucleon-substrate-braids` |
| `fluid-dynamics` | 0 | clean |
| `information-theory` | 0 | clean |
| `q-geometric-langlands` | 1 | `sec:tannaka-krein-foundation` |
| Other chapters | 0 | clean |

`braids-and-knots` dominates the major-findings list — it carries the
substrate→knots reasoning load for the paper. After PR #789's
49-way split it has well-named sections, but most lack the prose lead
that motivates each section's blocks.

## Per-chapter abrupt-endings (minor)

12 chapters end on a `remark` / `example` / `definition` rather than a
closing `prose` block (gestures forward, summarises, or hands off to
the next chapter). Per #738 §3, these are minor — the chapter is still
coherent, but a one-paragraph close would tighten the arc. Most
candidates can be addressed by promoting an existing trailing remark
to `prose` (one of the cheaper fix patterns).

## How to use this report

1. **The audit is read-only.** No drafts are produced — story content
   is editorial, and per #738 §Auto-discharge safety net "auto-fix a
   missing chapter intro without surfacing the draft is forbidden".
2. **Pick a target.** Most efficient sweep is one chapter at a time;
   start with `braids-and-knots` (20 major findings) or a smaller
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
```

Exit code = major finding count (capped at 255), so the audit can be
wired into CI as a soft quality gate.
