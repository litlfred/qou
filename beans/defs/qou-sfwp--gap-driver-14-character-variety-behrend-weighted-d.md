---
# qou-sfwp
title: 'GAP: driver-14 (character-variety Behrend-weighted DT moduli) is external — not a QOU scalar driver'
status: todo
pr: 8199
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T18:31:36Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-frzo
---

## State (2026-08-02, PR #4601)

driver-14 = a categorical construction from the substrate of the Behrend-weighted
DT moduli of the character variety / T[K] BPS Hilbert space (named in #4599).

VERDICT: irreducibly external at both levels — CONFIRMED from an independent
context and formalized (Driver14CharacterVarietyDTMenu.lean, lean-direct exit 0):

- partition level: missing input = single-degree Springer concentration
  H^{2n(λ)}(𝓑_λ)=V_λ; proved external (Rossmann-CC, #4581/#4570/#4574) — substrate
  carries q-Plancherel measure + cancelling fake degree, not the Green-fn/CC datum.
- knot level: missing input = a CHIRALITY-REFINED, set-valued DT count (5₂:{3,4}
  split across S⁺/S⁻). No scalar QOU invariant (Hecke block count, Wedderburn Euler
  total -2, AJ recursion order, + classical crossing/det/tetrahedra/braid/genus)
  reproduces it. Machine-checked.

1ppq hook (derive-then-check, NO fit): the ONE derived partition fragment
Δ_λ=(-1)^{n(λ)}dim V_λ gives B(deuteron)=0.380 MeV, -82.9%; missing C_knot=5.852 is
FITTED, not any DT count. So even a constructed driver-14 is NOT established to move
the deuteron; the Δ_λ-gate and DT-count gap are distinct open problems.

## What is missing (exactly)
A substrate construction of a chirality-graded moduli whose Behrend-weighted point
count is the character-variety DT spectrum — the knot-level twin of the external
single-parity Springer concentration. DT/3d-index categorification literature has
NOT built this (KLW categorify colored Jones, not the 3d-index). Literature frontier.

## Honest next step (only open lever)
Third-knot (3₁/6₁) check of the recorded 2-point coincidence dtMax=recursionOrder+1
(the "+1" = abelian branch of X(S³∖K), imported geometry). If it fails on a third
knot, the coincidence is dead; if it holds, the "+1 abelian branch" is a structural
observation about the DT count's decomposition — still imported geometry, not a
driver construction. Either way it does NOT make driver-14 categorical-from-drivers.

Audit: docs/audits/2026-08-02-driver-14-character-variety-dt-moduli-constructibility.md

## Progress (PR #8199)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/RouteCDTChiralityAndQBridgeTaming.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/route-c-dt-chirality-and-qbridge-taming.witness.json` (`scriptHash: d89ffef0f347`, `scriptCommitSha: d6aa2e9463a3ba079ec1d472e356f34252ece779`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8199 (`1f4bf9af7d58a057599a62f5a8d42748dc742ea8`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8199, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
