---
# qou-fa1x
title: 'folio-assistant: generate-index.ts — drop the Lean column from the definition index (patch from qou #8717)'
status: todo
type: task
priority: normal
tags:
    - cross-repo
    - folio-assistant
    - voice
parent: qou-d4kh
created_at: 2026-11-21T06:40:00Z
updated_at: 2026-11-21T06:40:00Z
---

Owner, 2026-11-21: "Land patch in 8717." This session (W14b) can push only to `litlfred/qou`; `litlfred/folio-assistant` is not configured and no add-repo tool exists. So the patch is parked here for a session that has folio-assistant in scope.

**What.** In `folio-assistant-sci/pipeline/generate-index.ts`, drop the `Lean` column from the definition-index table. The exact diff is in the body of qou PR #8717. Its effect is to replace `| Label | Title | Chapter | Lean |` with `| Label | Title | Chapter |` and to remove the `leanCol` cell.

**Why.** The qou `definition-index.md` on `main` was regenerated with this patch applied locally (#8717). Until the platform generator carries it, any regeneration with the old generator restores the column. That re-adds 7 L1 hits, which the voice ratchet flags and the commit hook warns about.

**Check after landing.** Run `bun run folio-assistant/folio-assistant-sci/pipeline/generate-index.ts --paper quantum-observable-universe` in qou: there should be no `| Lean |` header, and `voice-leak-ratchet.ts` should report no new index-of-definitions entries. Then bump `.folio-assistant-pin`.
