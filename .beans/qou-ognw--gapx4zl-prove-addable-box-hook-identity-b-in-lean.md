---
# qou-ognw
title: 'GAP(x4zl): prove addable-box hook identity (B) in Lean -- two-row/one-row brick first'
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T07:46:36Z
updated_at: 2026-08-29T08:29:25Z
---

2026-08-29: one-row brick LANDED (AddableBoxHookOneRow.lean, sorry-free, lean-direct EXIT 0): (B) at mu=(n) collapses to [n+1]_q = q[n]_q + q^-n = qBracket_add at (n,1). So one-row is NOT open content (corpus infra). HONEST: (B) does NOT decompose by row count -- two-row mu=(a,b) needs the THREE-ROW (a,b,1) hook product (new-row addable box). Derived closed forms: hookProd(a,b)=[a+1]![b]!/[a-b+1]; hookProd(a,b,1)=[a+2][b+1][a]![b-1]!/[a-b+1]. Full (B) = q-hook-length-formula identity, clean route is content/partial-fraction via q-JM eigenvalues (QJucysMurphyEigen) + addable/removable interlacing. Multi-session. Audit: docs/audits/2026-08-29-addable-box-hook-identity-B-proof-structure.md.

2026-08-29: per-cell bridge brick LANDED (NormalizedSumTelescopeBridge.one_sub_qsq_pow_eq, sorry-free, lean-direct EXIT 0): 1 - q^(2h) = -(q^h)(q-q^-1)[h]_q -- the exact term-by-term relation converting the Macdonald schurElement denominator (1-Q^h at Q=q^2) into the balanced hookProd_q factor. First Lean step of the convention bridge for the telescope-closure route (qou-3quc). Remaining: chain over cells (foldl) + n-stat identity kappa=Sum h - n - 2 n(lam) + Nat.Partition<->YoungDiagram carrier.
