---
# 2ti7
title: Drain 382 broken content-sibling .lean orphans (compile sweep 2026-06-28)
status: todo
type: task
created_at: 2026-06-28T16:49:39Z
updated_at: 2026-06-28T16:49:39Z
---


## Context

Surfaced by the 2026-06-28 content-sibling compile sweep (PR #2974).
382 of 926 content-block `.lean` siblings (outside the `lean/` library
tree) genuinely fail `lean`-direct on `main` — pre-existing breakage
that escaped CI because these files are outside the `lake build QOU`
target.

- **Findings doc:** `docs/audits/2026-06-28-content-sibling-compile-sweep.md`
- **Genuine list (382, `file ||| first-error`):**
  `docs/audits/2026-06-28-content-sibling-compile-sweep.genuine.txt`
- **CI now prevents new drift** via `lean-content-siblings.yml` +
  `scripts/lean-verify-siblings.sh` (diff-scoped; the 382 are not
  retroactively blocked).

## Attack order
1. Shared `unexpected token 'section'; expected 'lemma'` template family
   first (one fix → many files).
2. Densest chapters: `mass-theory` (72) + `quantum-observable-universes`
   (63) = 135/382.
3. Elaboration-error tail (`failed to synthesize`, `Function expected`,
   `unknown tactic`, …) per-file.

Verify a fix with: `scripts/lean-verify-siblings.sh <file.lean>` (exit 0).
