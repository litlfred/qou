---
# qou-1f1w
title: '[LEANNODES L3] First full build and known-red baseline'
status: todo
type: feature
priority: normal
tags:
    - migration
    - leannodes
    - needs-owner
created_at: 2026-10-04T16:35:47Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-ahxm
---

From the LEANNODES migration analysis (2026-10-04), story L3. Full report: docs/audits/2026-10-04-workplan-and-migration/LEANNODES_report.md.

| L3 | First full build and known-red baseline | Sharded run; status JSON, known-red list and elaborated census recorded; cache contributed with traces; library census unchanged | L | L2, `qou-wumn`/`z9bx`/`lb0f` |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.

**2026-10-05 — L3 baseline measured locally (lean-verifier subagent).** Branch `claude/lean-l3-baseline-2026-10-05`. Files: `docs/audits/2026-10-05-lean-blocks-known-red-baseline.{json,md}`.
- **Method.** 966 modules compiled with lean-direct (`-DautoImplicit=false -s 65536`) against `lake-cache/qou-v4-24-0` @ `a792c46d01b` and mathlib-gap @ `d7e3ae8c662`. First, the 76 library modules in the targets' cone were rebuilt from current source, chosen because their Lake trace source-hash had changed. All 76 built green. No lake, no CI.
- **Result.** QOUBlocks 872 green / 30 red. UGBBlocks 22/0. Fred2005Blocks 12/0. QOUAudits 24/6. Nothing skipped or timed out, and there are **0 environment gaps**.
- **The 30 QOUBlocks reds share one cause.** `FrobeniusHopfData` now takes `[BraidedCategory C]`, and its content-block consumers were not ported. Each is green against the stale snapshot and red against current source. They are real defects, not fixed here: the fix means editing `folio/` content.
- **The 6 QOUAudits reds are not library defects.** 3 are dated audit records whose classes were removed by later repairs. 2 are concatenation fragments, which cannot work as standalone modules; that is an L2 glob membership question. 1 is a probe that is red by construction.
- **Tooling gap.** `lean-content-sweep.sh`, `lean-library-sweep.py`, `lean-shadow-verify.sh` and `lean-restore-gap-oleans.sh` still glob `content/`. The cache tarball also stores `content/` paths, so restore it with `tar --transform 's,^content/,folio/,'`.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
