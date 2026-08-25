---
# qou-xz6t
title: 'Session: §7c stalled-claim takeover (qou-mtcx) + cluster triage + FR split — PR #5113'
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-15T15:07:04Z
updated_at: 2026-08-15T15:07:04Z
---

Branch `claude/mtcx-7c-verify-close-2026-08-15`, PR #5113 (+ policy PR #5108).

**Opened late — recording unclaimed work.** This session did durable work across two repos before a session milestone existed; per AGENTS.md §work-plan that omission is reported, not hidden. Beans touched are listed below.

## Delivered

- **Policy (PR #5108):** standing **stalled-claim takeover** rule — a bean `in-progress` whose backing branch has had no commit for >3h is presumed abandoned and may be taken over. Scoped hard: applies ONLY to a branch backing a *live in-progress bean*, never to the ~4,400 long-idle `claude/*` branches. Guardrails: confirm staleness (no newer PR activity / no in-flight CI), re-claim with a handoff note + the stale branch's last SHA, continue from that tip or main, never force-push a sibling's branch. AGENTS.md §2 + `local/todo-manager` §Stalled-claim takeover.
- **`qou-mtcx` closed** (first application of the policy): stale a week, no live branch, 0 open PRs. All 15 MarkovTraceContext descendants verified — 4 already generic, 4 legitimately ℝ, 7 ports already landed. Compiles ok=5 / ok / ok.
- **`qou-3bcc` closed:** both §3b conjecture classes already generic (`[Ring R]`, `[CommRing R]`); compile ok=1.
- **Triage tables** written into the five empty cluster beans (`oc4v`, `r7qm`, `e4ri`, `xbyp`, `q7cm`) using the canonical folio-assistant content checkers — the gap that let two completed beans sit open.
- **`QChebyshevFunction`:** top CANDIDATE **adjudicated and refuted** — its ℝ is legitimately archimedean (Λ_q is a `Real.rpow` weight; the `N m ≤ X` cut-off is an ordering). Added the missing §7c banner instead of a wrong port; retracted my own CANDIDATE call in `qou-e4ri`.
- **`DepthStratifiedFrobeniusReciprocity`:** genuine MIXED → **split** per §7c. Algebraic half wall-side **FAIL → PASS**; new archimedean sibling holds the decimal variance records. Both compile ok=1.
- **Orphan-gate fix:** prepare-merge caught that the split added a module nothing imported (`lean-orphan-gate` exit 1). Registered in `QOU.lean`; the sibling pulls the algebraic module in transitively, and `QChebyshevFunction` explicitly — so all three are now built, **shrinking** the qou-orph backlog rather than growing it.

## Environment note (useful to the next agent)

Lean is provisioned in this sandbox despite `release.lean-lang.org` returning 403: elan installed from the GitHub release **asset** CDN, compiler vendored via `scripts/lean-toolchain-cache-restore.sh`, Mathlib oleans via `scripts/lean-cache-restore.sh` (6990 mathlib + 942 QOU oleans). Any shell needs only `export PATH="$HOME/.elan/bin:$PATH"`. **Never `lake build`/`env`/`update`** — `.lake/packages/mathlib` has no `.git`, so a dep-resolving lake call would wipe the restore. Use `scripts/lean-direct-cone.sh`.

## Trap recorded

`lean-vacuity-axiom-audit.ts` run **diff-scoped rewrites** `docs/audits/2026-06-17-lean-vacuity-axiom-audit.json` with only the scanned files (−3,743 lines), destroying the corpus record. Reverted here; do not commit that side effect.

## Forward arc — NOT re-beaned (already covered)

The remaining work already has beans; no new ones were created (see the §Check-before-you-create history). Live options, each with the triage table now attached: `qou-q7cm` (2 large MIXED splits), `qou-e4ri` (`JonesMarkovWenzl` 26 codeℝ), `qou-xbyp` (`MagicNumbersFromQ` 24, highest false-positive risk — mass domain legitimately expects real-positive), `qou-oc4v` (2 remaining CANDIDATEs), `qou-r7qm` (smallest), and structurally `qou-kljb` (795 modules never built).
