---
# qou-hmji
title: '[TOOLS T6b] overnight run-*.sh drivers are broken as written — repair or retire?'
status: todo
type: task
tags:
    - migration
    - tools
created_at: 2026-10-05T10:10:28Z
updated_at: 2026-10-05T10:10:28Z
parent: qou-k3er
---

Found while closing T6 (qou-kumy), 2026-10-05. The TOOLS report (docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md, line 84) says these become a **long-run regeneration** process. Measured, none of the three can run as written, so declaring them as Tools would put broken invocations into the KG.

- `computations/run-k8-overnight.sh` and `computations/run-overnight-mac.sh` both call `python3 hecke_characters.py` from `computations/`. That script now lives at `computations/hecke/hecke_characters.py`, so both exit at the first step.
- `computations/run-sage-witnesses.sh` documents itself as `./scripts/run-sage-witnesses.sh` after `./scripts/setup-sage.sh`. Neither path exists. Its three inputs (`computations/sage-{borromean-gA,cgeom,nuclear-braid}.sage`) exist, but none of the three witnesses it promises (`computations/sage-*.witness.json`) is in the tree.
- The `hecke-k*.json` outputs (k6–k11) are committed, but no content block names them as a witness, so the producer manifest (tool-defs/producers.json) does not reach them.

## Owner decision
- **A: repair.** Point the two Hecke drivers at `computations/hecke/`, fix the sage driver's paths, and declare all three as Tools under a long-run-regeneration process with the same approval gate as witness-refresh. No outputs are re-run without approval.
- **B: retire.** Move the three drivers to fsh-guts/deprecated/ (never deleted), and leave their committed outputs as they are.

Default if no answer: nothing changes, and the drivers stay broken where they are.

## Done when
- [ ] owner picks A or B
- [ ] if A: each driver runs to its first step, the process loads in workflow_list, and no witness is rewritten
- [ ] content parity: no change to computations/** outputs, folio/** or *.lean
