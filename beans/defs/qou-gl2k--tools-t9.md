---
# qou-gl2k
title: '[TOOLS T9] Regenerate-and-diff process for the Lean content producers gen-gluing-lean.py and gen-hecke-corner-column.py'
status: in-progress
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:44Z
updated_at: 2026-10-05T10:19:17Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T9. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T9 | Regenerate-and-diff process for the Lean content producers `gen-gluing-lean.py` and `gen-hecke-corner-column.py` | regenerated `GeneratedGluing.lean` is byte-identical to the committed file; process modelled on `atomic-mass-drift-check.bpmn` | S | — |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


2026-10-05 — implemented on claude/tools-t9-lean-regen-2026-10-05.
- scripts/check-generated-lean.py regenerates both texts in memory and writes nothing. Exit 0 identical, 1 drift (with a unified diff), 2 unknown (a generator could not run; never a pass).
- Measured on main 6ac75615f0 + #7514: GeneratedGluing.lean, all 19 knot blocks, BYTE-IDENTICAL to gen-gluing-lean.py output (the 52-line header and the closing end are hand-written and excluded). HeckeCompletion.lean BokutShiaoCornerDepth3 (§4ae) verbatim equal to gen-hecke-corner-column.py 3. About 9 s.
- NOT checked, by design: §4ad (BokutShiaoCorner) was hand-written first, and the script's docstring says it was checked by re-deriving, not by text. The two differ on 964 lines.
- Failure paths tested: a SnapPy stub gives exit 2; a one-space edit in a scratch worktree gives exit 1 with the diff.
- Tool lean-regenerate-check (satisfies lean-generation); process processes/content/lean-regenerate-and-diff.bpmn (strict; drift goes to the author as a userTask). loadProcessModel parses it (7 nodes); discoverTools(qou) = 206, 0 failures.
- Content parity: index sha over computations/folio/lean unchanged.
- Needs SnapPy (pip install snappy) for the gluing half; without it the check says unknown.
