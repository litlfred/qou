# Work-plan reorganisation and migration analysis (2026-10-04)

Read-only analyses behind issue #7495, PR #7496 (bean reorganisation, merged) and the
migration epics under milestone `qou-5vkl` (Platform, tooling and hygiene).
**Owner hard rule throughout: no math or physics content is changed.** These files
describe and plan; none of them edits content.

## Round 1: bean store and coordination (inputs to PR #7496)

| file | what it covers |
|---|---|
| `L2_report.md` | the L2 at 1 ppQ programme epic tree |
| `CONJ_report.md` | the open-conjecture umbrella and the register of 182 conjecture blocks |
| `LEAN_report.md` | Lean / Mathlib foundations epics and the Lean critical path |
| `SEI_report.md` | SM, exposition and platform beans; qou vs folio-assistant home |
| `OTH_report.md` | unsorted beans and session logs |
| `ARCH_report.md` | git archaeology: branches, open PRs, duplicates, parent graph, churn |
| `MIG_report.md` | the first migration epic design (stories S1 to S8) |
| `ORPH_report.md`, `ORPH_inventory.tsv` | orphaned content (unbuilt Lean, outside-tree math, branch-only math) |
| `SKILLS-GAPS_report.md` | skills folio-assistant should gain |
| `MERGED_mapping.tsv` | every open bean's proposed action as applied in PR #7496 |

## Round 2: node migration (epics `qou-n4r9`, `qou-ahxm`, `qou-k3er`, `qou-7vh1`, `qou-5lsb`)

| file | what it covers |
|---|---|
| `TARGET_report.md` | what each folio-assistant node kind requires (the yardstick) |
| `TOOLS_report.md` | computations, scripts, workflows to Tool and Process nodes |
| `SKILLS2_report.md` | skills, commands, AGENTS.md sections and owner rulings |
| `LEANNODES_report.md` | Lean as compiled content nodes, by lakefile edits only |
| `CONTENT_report.md` | folio/ conformance, QA sidecar split |
| `REST_report.md` | library, docs, uploads, data and config files |
| `CONTENT_parity_baseline.tsv` | before-state git blob ids of every block's `.ts`, `.md` and `.lean`: the parity check every migration story runs against |
| `*_inventory.tsv` | per-file dispositions behind each report |

Counts are measured at qou `main` 348e299 / afa49febf and folio-assistant `main`
0b7b9e44e unless a file says otherwise. Each `[M]` claim was measured; `[D]` came from a
document; `[B]` from a bean.
