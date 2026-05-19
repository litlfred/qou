# I12 cluster A — namespaced-decl audit regex fix

**Goal**: clear the 18 `*.unique` block flags from the I12
`sibling_no_decl` bucket via a one-decision audit-regex fix.

**Author PR**: #782 (`claude/i12-a-audit-regex-unique-decls-2026-05-19`)

## Scope map

| PR | head | scope vs #782 |
|----|------|---------------|
| **#782** (mine) | `claude/i12-a-audit-regex-unique-decls-2026-05-19` | audit-regex fix + 2 URI updates → +57 audit `ok` |
| #781 | `claude/show-mass-sweep-table-2xEBG` | mass-table canonical alignment, 11 legacy artifacts removed — **independent** (file overlap = 0) |
| #780 | `claude/d2a-followup-morse-wall-lean-fill` | morse-wall Lean sorry fill + residue witness — independent |
| #777 | `claude/track-a-b-per-isotope-and-rho-xi` | precision docs v7 — independent |
| #774 | `claude/iw-meta-tighten-guarded-off-heuristic` | i3 audit heuristic — **adjacent infra** (different audit, no overlap) |
| #772 | `claude/210x-scale-gap-root-cause` | ρ_K·m_e scale-gap audit — independent |
| #761 | `claude/combine-all-open-prs` | meta-combine PR — superset, watch for rebase needs |
| #738 | `claude/detangler-story-coherence` | detangler scope/section coherence — independent |
| #736 | `claude/post-dissolution-cleanup-V01` | orphan conjecture wiring + bibliography — independent |
| Copilot #650 / #646 / #411 / #31 | various | long-running, independent |

## Coordination actions

| ts (UTC) | event | sibling | action |
|----------|-------|---------|--------|
| 2026-05-19T00:53Z | open PR | — | #782 opened with regex fix + URI updates |
| 2026-05-19T00:55Z | heads-up | #781 | posted coordination comment ([#781 comment-4483547064](https://github.com/litlfred/qou/pull/781#issuecomment-4483547064)) — flagged the benign stale-probe-audit re-emit collision; no rebase action requested |
| 2026-05-19T00:55Z | subscribe | #782 | subscribed to own PR for CI / review events |

## Audit movement (this PR)

| bucket | before | after | delta |
|--------|-------:|------:|------:|
| `ok` | 606 | 663 | **+57** |
| `sibling_no_decl` | 215 | 158 | −57 |
| `grep_no_match` | 122 | 122 | 0 |
| `lake_root_missing_grep_hit` | 1 | 1 | 0 |

The +57 (vs the 18 *.unique targets) reflects that the namespaced-decl
regex pattern was repo-wide: 39 additional content blocks across
multiple chapters were silently flagged for the same regex bug.

## Open follow-ups

- Watch #781 → if it lands first, no rebase needed (no overlap); if
  #782 lands first, #781 may see benign `stale-probe-audit` drift
  on `total_fields_audited` (small additive count, no substantive
  divergence).
- Next backlog batch (post-#782): the I12 audit now stands at
  663 / 944 ok. Remaining 281 non-`ok` (158 `sibling_no_decl` +
  122 `grep_no_match` + 1 residual) — re-triage to find the next
  cheap-batch.
