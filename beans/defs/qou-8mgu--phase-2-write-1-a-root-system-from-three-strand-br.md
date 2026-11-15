---
# qou-8mgu
title: 'Phase 2: Write §1 A₂ root system from three-strand braiding'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-arch
created_at: 2026-08-04T01:29:46Z
updated_at: 2026-10-10T07:16:26Z
parent: qou-8lxd
---

## COMPLETED — verified 2026-10-10

The section exists with this bean's own title: `eightfold-way.ts` carries
`title: "The $A_2$ root system from three-strand braiding"`, backed by block
`a2-from-three-strands`.

**The section existing is not the derivation holding.** PR #4640's honesty pass
found the chapter conflating two different A2s — the Coxeter type of
`W(A_2) = S_3` permuting *strands* (true by construction, since `B_n` has type
`A_{n-1}`) versus `A_2 = sl_3` acting on the *fibre* (needs `dim V = 3`).
Setting `n = 3` does not make `N = 3`. That gap is `qou-8pl3` / `qou-d7h1`.
