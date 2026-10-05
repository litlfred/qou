---
# qou-4dj1
title: '[TOOLS T7] compute-QA process (precision-gates, staleness-gates, lp-dual, float64, word-provenance, witness-staleness…'
status: in-progress
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:43Z
updated_at: 2026-10-05T11:28:35Z
parent: qou-k3er
blocked_by:
    - qou-4rhu
---

From the TOOLS migration analysis (2026-10-04), story T7. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T7 | `compute-QA` process (precision-gates, staleness-gates, lp-dual, float64, word-provenance, witness-staleness audits as Tools) | each workflow YAML reduced to a dispatch of the process with a `# bpmn-node:` back-reference; gate verdicts identical on `main` before and after; verdict files written to `qa-reports`, not committed | M | T5 |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


2026-10-05 — implemented on claude/tools-t7-compute-qa-2026-10-05. Done-when, item by item:
1. EACH WORKFLOW REDUCED TO A DISPATCH OF THE PROCESS — done. All 21 gate steps in witness-staleness, lp-dual-gate, probe-float64-gate and word-provenance-gate now run `python3 scripts/compute-qa.py --gate <id>`, each with a `# bpmn-node:` comment naming its activity in processes/tools/compute-qa.bpmn (strict; 5 parallel gate groups, then publish, then verdict). Setup steps (pip, MPFR build, bun, setup-folio-assistant) are unchanged. The LP backend heredoc moved verbatim to scripts/lp-dual-backend-check.py.
2. GATE VERDICTS IDENTICAL ON MAIN, BEFORE vs AFTER — done. Before: the raw commands in a worktree at origin/main. After: the runner in a worktree at the branch. All 17 no-setup gates have identical exit codes. Output is byte-identical except that 4 gates print the scratch worktree's path in one warning line. The 2 diff gates match on the same file list. lp-dual gates were measured with the job's PYTHONPATH on both sides. Red on main both before and after: q0-anchor-flip, import-time-dps, never-raises-dps, float64-padding, q0-value-drift. Pre-existing, unchanged, and NOT this story's to fix.
   Not measured locally: lp-dual-backend (needs the MPFR LP binary built) and authors-note-coverage (needs the platform checkout). Their commands are unchanged.
3. VERDICTS TO qa-reports, NOT COMMITTED — HALF done. Each gate writes test/results/compute-qa/<gate>.json (now gitignored), which is the layout `bun run qa:publish` reads. But qou has NO qa-reports branch, and creating one is story S3 (qou-4rhu), so no workflow publishes yet. Blocked on qou-4rhu.
Tools: 21 compute-qa-<gate> Tools, generated from the runner's table via tool-defs/compute-qa-gates.json (--check-tool-defs). discoverTools(qou) = 227, 0 failures.
Content parity: no change under computations/, folio/, *.lean or any witness.
Trap worth knowing: several of these audits WRITE their audit witness files as a side effect. Run them in a worktree (as here) or restore afterwards; never commit what they rewrite.
