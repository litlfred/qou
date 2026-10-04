---
# qou-a2d7
title: 'Assess: is prop:qou-is-ccc real math or definitional restatement'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T18:08:46Z
updated_at: 2026-10-04T15:11:53Z
parent: qou-ddmn
---

MEASURED. `prop:qou-is-ccc` -> Lean `QOU.qou_is_ccc` at content/quantum-observable-universe/lean/QOU/JetHorizon.lean:306. Proof term is `⟨H.degree_zero_vanishes, H.degree_one_leaks, H.degree_two_leaks⟩` — three field projections of the `structure JetHorizon` (same file, :57), whose fields ARE the three conclusions. Zero derivation. .ts carries validation: "not_checked". Docstring is honest: says CCC-2 (boundary-data inheritance, the only non-definitional leg) 'is not yet formalised here' and that the previous (chain, h_adj, hH) hypotheses were UNUSED (Copilot, PR #776). The .md is also honest — penrose-ccc.md lists 4 explicit differences from Penrose and says 'The underlying mechanism, however, differs'; qou-is-ccc-proof.md has a 'Limitations of the claim' para. VERDICT: definitional restatement, correctly caveated in prose, oversold by the proposition TITLE.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
