---
# qou-g7z6
title: Drain the mass-endomorphism sidecar backlog (126/126 stale)
status: todo
type: task
priority: normal
created_at: 2026-08-29T12:04:07Z
updated_at: 2026-08-29T12:04:08Z
---

Surfaced while verifying #6016, not caused by it.

`bun run folio-assistant/content/pipeline/qa-staleness.ts content/quantum-observable-universe/mass-endomorphism`
reports **126 blocks; fresh=0, stale/partial=126** on 2026-08-29. Pre-existing.
#6016 refreshed exactly one sidecar — the block whose `.lean` it renamed — and
reverted the other 127 so a rename PR did not become a chapter sweep.

**Why this is a batch audit run, not idle-pass work.** A chapter-scoped
`qa-sweep` rewrites all 128 sidecars in one go, which AGENTS.md explicitly
sanctions as a single bulk commit ("regenerate N sidecars after checker fix")
— but the idle-backlog policy caps a pass at ≤ 10 sidecars, so this does not
fit there.

**Most of it is not mechanical.** The stale sets are dominated by
agent-reviewed criteria — `da-*` (13 of them), `voice-*`, `proof-rater-*`,
`expo-milnor-clarity`, `milnor-brevity` — which a sweep marks
`[needs-agent]` rather than resolving. The script criteria re-run cheaply; the
agent ones are the actual cost, and whoever takes this should scope that first.

Two measured cautions for whoever does:
- `qa-sweep` / `qa-staleness` take a **directory**; a file path dies `ENOTDIR`.
- Never hand-edit a sidecar to clear staleness.

Unclaimed as of 2026-08-29; opened so it is not lost in a chat transcript.
