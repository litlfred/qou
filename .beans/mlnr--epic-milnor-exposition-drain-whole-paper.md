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

## Progress (chapters MERGED, 9)
measurement-observation #3334 · quantum-universes #3342 · organic-chemistry
#3356 · small-group-A [introduction+gravity-spacetime+appendix-qvalues+
appendix-nf-witnesses+appendix-knot-operations-archimedean] #3360 ·
appendix-knot-operations #3373 · appendix-surreals-archimedean #3382 ·
appendix-knot-periodic-table #3406 · appendix-transfer-matrices #3416+#3421.

## In progress
appendix-surreals (93/93) — committed to claude/milnor-drain-appendix-surreals, awaiting PR and merge.

## Remaining queue (≤22-block batches)
fluid-dynamics(94/5) · braids-and-knots(103/5) ·
lifting-and-descent(116/6) · mass-endomorphism(116/6) · brings-surface(161/8)
· information-theory(165/8) · observations(249/12) · particle-interactions
(268/13, yield borromean-quark) · predicted-spectra(279/13) ·
quantum-observable-universes(309/15) · mass-theory(699/32, highest
overreach-risk — tiny batches, careful review).

SKIP: glossary / notation / index-of-definitions / amc (excised).

## Ledger
scratchpad/milnor-campaign.md (fuller state); this bean is the durable
top-level tracker.
