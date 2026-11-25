---
# qou-au0d
title: 'Merge-manager handover 2026-11-25: queue state'
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T16:25:54Z
updated_at: 2026-11-25T16:26:00Z
parent: qou-s028
---

Merge-manager session (owner grant 2026-11-24 21:15Z, extended to 2026-11-25T22:00Z; rows in docs/coordination/owner-rulings.md). Handover state at 2026-11-25 ~16:30Z.

## Merged (all verified on head; verify-merge-replay clean)
#9401 79e3a9ce2, #9403 c8e2e7595, #9402 5b2617361 (merge commit), #9404 cf1cff868 (merge commit), #9407 327f01818, #9410 ea057313d, #9412 4c79c3302, #9398 1e75378ad, #9419 1e3e8e78e, #9423 d4e0018da, #9421 d5b4067b0, #9415 15fd9d90a (merge commit), #9427 d2ddd71a7, #9425 3fef80728 (merge commit), #9429 7e85fc395, #9430 9228a12ed, #9431 52f9f88df (merge commit).

## Queue: PR -> status -> blocker
- #9432 (handoff-envelope rule, docs) -> not yet verified -> waits for cat-harness#1405 to merge (outside the qou-only grant).
- #9400 (Lean v4.35 upgrade) -> draft -> author still working.
- #9405 (hook fix) -> draft -> author.
- #9420, #9424, #9426, #9428 -> drafts -> authors.
- PDF rebuild -> pending since #9430/#9431 touched folio/ -> held until the coordinator's gh-pages site publish reports done. Then: bash scripts/build-paper-pdf.sh && bash scripts/publish-paper-pdf.sh --pdf build/paper/main.pdf (needs folio-assistant/cat-harness-tools/scripts/install-tex.sh and the full scripts/setup-folio-assistant.sh).
- Older swarm PRs (#84xx/#83xx/#82xx, #8350/#8333/#8290) -> not merging: either restatements of existing theorems (`rw [X, sub_self]`) or ~3000 commits behind with conflicts in rewritten producers.

## Traps found this session (for the next merge manager)
- The GitHub merge endpoint returned 500 on rebase for linear PRs (#9425, #9431) and 500/502 on merge-commit; a retry minutes later succeeded. After any 5xx, re-read main ~30 s before retrying (a 5xx can land late, per the coordinator on #9396).
- A PR head containing merge-from-main gives 405 on rebase; use a merge commit (lossless).
- Run `bun run folio-assistant/cat-harness-tools/pipeline/gen-block-jsonld.ts --check --paper quantum-observable-universe` before merging any PR touching folio/ blocks (coordinator rule 2026-11-25). The platform clone must match .folio-assistant-pin (re-run scripts/setup-folio-assistant.sh after a re-pin), or the check reports ~3850 false stale nodes.
- Shadow tree for lean-library-sweep is at /home/user/lean-shadow (container-local; lost with the container).
