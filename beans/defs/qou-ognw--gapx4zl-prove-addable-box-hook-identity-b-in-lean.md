---
# qou-ognw
title: 'GAP(x4zl): prove addable-box hook identity (B) in Lean -- two-row/one-row brick first'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T07:46:36Z
updated_at: 2026-11-17T12:24:25Z
parent: qou-59vq
---

2026-08-29: one-row brick LANDED (AddableBoxHookOneRow.lean, sorry-free, lean-direct EXIT 0): (B) at mu=(n) collapses to [n+1]_q = q[n]_q + q^-n = qBracket_add at (n,1). So one-row is NOT open content (corpus infra). HONEST: (B) does NOT decompose by row count -- two-row mu=(a,b) needs the THREE-ROW (a,b,1) hook product (new-row addable box). Derived closed forms: hookProd(a,b)=[a+1]![b]!/[a-b+1]; hookProd(a,b,1)=[a+2][b+1][a]![b-1]!/[a-b+1]. Full (B) = q-hook-length-formula identity, clean route is content/partial-fraction via q-JM eigenvalues (QJucysMurphyEigen) + addable/removable interlacing. Multi-session. Audit: docs/audits/2026-08-29-addable-box-hook-identity-B-proof-structure.md.

2026-08-29: per-cell bridge brick LANDED (NormalizedSumTelescopeBridge.one_sub_qsq_pow_eq, sorry-free, lean-direct EXIT 0): 1 - q^(2h) = -(q^h)(q-q^-1)[h]_q -- the exact term-by-term relation converting the Macdonald schurElement denominator (1-Q^h at Q=q^2) into the balanced hookProd_q factor. First Lean step of the convention bridge for the telescope-closure route (qou-3quc). Remaining: chain over cells (foldl) + n-stat identity kappa=Sum h - n - 2 n(lam) + Nat.Partition<->YoungDiagram carrier.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress 2026-11-17 (Round 66 — PR #8340)

- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/AddableCellRatioFakeDegreeTwoRowBallotWeightTensorPowerCharacterOrbitTrace.lean` (Lean 4.24.0, `0` `sorry`, `0` `axiom`, `0` warnings, `0` directory-mode static vacuity & borrowed-name advisories).
- 80-dps `mpmath` numerical witness stamped in `computations/probes/addable-cell-ratio-fake-degree-two-row-ballot-weight-tensor-power-character-orbit-trace.witness.json` (`scriptHash = 0309390e769d`, `scriptCommitSha = c43b700db42337a2547c8ff1e2a1665156dd27ea`, `HEAD = d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).
- PR: https://github.com/litlfred/qou/pull/8340 (`ready: d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).
