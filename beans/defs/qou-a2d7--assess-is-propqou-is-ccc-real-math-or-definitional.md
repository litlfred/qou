---
# qou-a2d7
title: 'Assess: is prop:qou-is-ccc real math or definitional restatement'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T18:08:46Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-ddmn
---

MEASURED. `prop:qou-is-ccc` -> Lean `QOU.qou_is_ccc` at folio/quantum-observable-universe/lean/QOU/JetHorizon.lean:306. Proof term is `⟨H.degree_zero_vanishes, H.degree_one_leaks, H.degree_two_leaks⟩` — three field projections of the `structure JetHorizon` (same file, :57), whose fields ARE the three conclusions. Zero derivation. .ts carries validation: "not_checked". Docstring is honest: says CCC-2 (boundary-data inheritance, the only non-definitional leg) 'is not yet formalised here' and that the previous (chain, h_adj, hH) hypotheses were UNUSED (Copilot, PR #776). The .md is also honest — penrose-ccc.md lists 4 explicit differences from Penrose and says 'The underlying mechanism, however, differs'; qou-is-ccc-proof.md has a 'Limitations of the claim' para. VERDICT: definitional restatement, correctly caveated in prose, oversold by the proposition TITLE.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8448)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/CuspLatticeUncertaintyTruncationDigitSlopeJetHorizonProjectionSubstrateModelScalarTrace.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_4kgh_5u0i_a2d7_aawz_nnyn_probe.witness.json` (`Commit 1` = `03aab630aaf498438c097ced372d1b9624239334`, `HEAD` = `9712a8a7c54237632ba55faa0a1e31fdd3332e05`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8448, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
