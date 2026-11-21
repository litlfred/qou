---
# qou-co63
title: '[TOOLS T10] Upstream generic Lean audits to folio-assistant-sci (folio/pipeline Lean audits; scripts/lean-*…'
status: todo
type: feature
priority: normal
tags:
    - migration
    - tools
    - upstream-fa
created_at: 2026-10-04T16:35:44Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T10. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T10 | Upstream generic Lean audits to `folio-assistant-sci` (`folio/pipeline` Lean audits; `scripts/lean-*` vacuity/axiom/orphan; lean-axiom-guard; lean-content-siblings) | each one exists in sci, takes the root as a parameter, and reproduces qou's current output on qou (same finding set); the qou copy is retired only after that | L | — |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
