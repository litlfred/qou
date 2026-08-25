---
# mlnr
title: 'EPIC: Milnor exposition drain — whole-paper H1–H8 audit+resolve (expo-milnor-clarity) + milnor-brevity'
status: in-progress
type: epic
priority: high
created_at: 2026-07-06T11:10:00Z
updated_at: 2026-07-06T16:55:26Z
---

Owner directive: "do all chapters" — bring every narrative `.md` block up to
the Milnor exposition standard (`expo-milnor-clarity`, hallmarks H1–H8) across
the whole quantum-observable-universe paper, then keep going to completion.

## Mechanism
- Per-chapter (≤22-block batches) `Workflow` audit→resolve swarm; script
  `scratchpad/milnor-drain.js` (persisted). ONE workflow live at a time; NO
  branch switch while a drain workflow runs (branch-contamination rule).
- POSTURE = MERGE-AS-YOU-GO: run → HARD guard-check (revert any .md >200-line
  delta OR .ts edit OR diagram/eqn deletion OR out-of-scope path) → commit →
  validate → PR → Gemini+Copilot review → VERIFY-then-fix each review comment
  (reviewers have misread table row-counts; decline+reply when wrong) → rebase
  → merge (rebase). Batches ≤22 for session-usage-limit resilience.
- Guards in the resolve prompt: NO-DELETE-MATH-CONTENT, NO-NEW-CLAIMS,
  cross-block-consistency.

## Sub-deliverables (done)
- milnor-brevity QA param (companion to clarity): folio-assistant #46
  (registry EXPO domain) + qou #3387 (§5B spec) — MERGED. Audit-only in the
  autonomous drain; deletion pass is human-reviewed.
- Excised appendix-atomic-mass-calculations (redundant to the recursive
  knot-particle atlas): #3393 MERGED.

## Progress (chapters MERGED, 10)
measurement-observation #3334 · quantum-universes #3342 · organic-chemistry
#3356 · small-group-A [introduction+gravity-spacetime+appendix-qvalues+
appendix-nf-witnesses+appendix-knot-operations-archimedean] #3360 ·
appendix-knot-operations #3373 · appendix-surreals-archimedean #3382 ·
appendix-knot-periodic-table #3406 · appendix-transfer-matrices #3416+#3421 ·
**q-geometric-langlands (50/50)** — landed 2026-07-06.

## In progress
*(none — see the correction below)*

**CORRECTION 2026-08-07.** This bean said q-geometric-langlands was
"committed to `claude/milnor-drain-q-geometric-langlands`, awaiting PR and
merge", and that stale line was being read as a gate on main. **It is not.
The work is already in main.** Verified by containment, not by inference:

    git merge-base --is-ancestor <c> origin/main   →  IN MAIN

for all three of `2f102939ae` (witness regen), `a7b0178079` (the "drained
50/50" bean mark) and `d2d8cd18a5` (the drain itself). The merge-base of
`origin/main` and the branch **is the branch tip**, i.e. the branch is an
ancestor of main. It landed 2026-07-06 — a month before this correction —
so no PR is needed and none should be opened.

Caution for whoever measures this next: this repo is checked out **shallow**
(`git rev-parse --is-shallow-repository` → true, 8 grafts). Before deepening,
`git rev-list --count origin/main..<branch>` reported **17721 commits ahead /
119 behind** and `git merge-base` returned empty — pure graft artifacts. Had
that been believed, the conclusion would have been a catastrophically
divergent branch rather than an already-merged one. Deepen first
(`git fetch --deepen=3000 origin main <branch>`), then measure.

Note also that the branch carries three commits **outside** the drain scope
(Demazure/Wenzl Option-C evaluator, qou-mass Composite 4 + Toroidal Harmonic
scaffolding). They are in main too; flagged only so the drain's scope is not
misread from the branch contents.

## Remaining queue (≤22-block batches) — next up: climax-volume-mass
climax-volume-mass(62/3)
· molecular-construction(73/4) · stochastic-mechanics(74/4) ·
appendix-surreals(92/5) · fluid-dynamics(94/5) · braids-and-knots(103/5) ·
lifting-and-descent(116/6) · mass-endomorphism(116/6) · brings-surface(161/8)
· information-theory(165/8) · observations(249/12) · particle-interactions
(268/13, yield borromean-quark) · predicted-spectra(279/13) ·
quantum-observable-universes(309/15) · mass-theory(699/32, highest
overreach-risk — tiny batches, careful review).

SKIP: glossary / notation / index-of-definitions / amc (excised).

## Ledger
scratchpad/milnor-campaign.md (fuller state); this bean is the durable
top-level tracker.
