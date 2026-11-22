---
# qou-wdg1
title: skein mass from linking missing hypotheses
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-22T21:55:07Z
---

File: `content/quantum-observable-universe/lean/QOU/BraidsKnots/skein_mass_from_linking.lean`
The `skein_mass_from_linking` theorem is unprovable. Its class lacks constraints on the data fields and has `*_unconstrained_false` lemmas proving that the conclusion is independent and refutable from the provided data alone.



## Reasons for Scrapping

Duplicate of `qou-zko1` (work-plan reorganisation 2026-10-04). Evidence: same Lean target skein_mass_from_linking; 2 main commits
Content is untouched; only this work item is closed.



Also known as `skml` (its former front-matter header id; the beans CLI uses the filename id `skein_mass_from_linking`). Recorded 2026-10-04.

## 2026-11-22 — id renamed `skein_mass_from_linking` → `qou-wdg1` (bean-hygiene, owner-approved)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. The old id contained underscores, which the tracker's id pattern `[A-Za-z0-9-]+` rejects, so `scripts/check-beans.sh` reported this file as having no id and every `beans` query missed it. Renamed on the owner's approval of qou-w3yy (project-chat card, 2026-11-22 21:53Z). Content unchanged; the old id stays greppable here.
