---
# qou-bimg
title: Dense triton Magnus probe is 87x slower than the sparse route that already reproduces it
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T09:03:15Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-trd0
---


## Measured 2026-09-13, both on H₉, same word, same q₀

    triton_magnus_omega2_sign_probe.py            30/30 partitions   ~40 min
    he4_magnus_omega2_sign_sparse_probe.py --gate 30/30 partitions   27.5 s

**~87×.** And they agree to **rel diff 9.08e-60** — the gate exists precisely to
check the sparse route against the committed dense datum, so this is not a
proposal to trust new code: the sparse path is already the corpus's own
correctness reference for this number, and it is the faster one.

## Why it matters more than a wall-clock figure

The dense probe's resume cache **stamps on a hash of the whole source file**
(deliberately — `qou-z3q9`, after a patched run served 14/30 rows computed by
the unpatched code). Correct, but it means **any** edit to that probe, a
comment included, costs a full 30/30 recompute. During `qou-q2q7` that turned
two rounds of docstring corrections into ~80 minutes of pure recompute. The
cost is not the run, it is the tax on every future edit.

`qou-4383` independently found `atomic_tr_m_helium4.py` and
`binding_combiner_markov_peel_fallback.py` over 1200 s, and `qou-za3q` recorded
that "the sparse probe was already ahead of the dense ones". This is the same
pattern with the replacement already written and gated.

## What the work is

Not a rewrite. `he4_magnus_omega2_sign_sparse_probe.pairing_for_word(gens, n)`
is already n-generic — the gate calls it with `n = 9`. The task is to have the
dense probes' aggregation call it, keep every existing witness field
(`P_total`, `P_total_wenzl`, `per_partition[]`, both sign-vs-A arms), and prove
byte-equality of the results against the committed witnesses before swapping.

## Cheap first, if the swap looks risky

The germ/Ω₂ build could keep its own stamp while the **per-partition rows** key
on `(λ, q, word)` only — then a docstring edit stops invalidating 30 partitions
of arithmetic that did not change. Narrower than the file hash and still
immune to the `qou-z3q9` failure, since the row key names everything the row
depends on.

## Do not

Widen the cache stamp back to `(q, n)`. That is the exact PRESENT-vs-CURRENT
defect `qou-z3q9` closed, and it made an "is the output identical?" check
circular.

Parents / siblings: `qou-4383` (slow producers), `qou-za3q` (which recorded the
sparse advantage), `qou-q2q7` (where the tax was paid), `qou-z3q9` (the stamp).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8396, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-13: "docs(qou-q2q7,qou-za3q,qou-bimg): close the naming half, tick three sibling-done items, open the perf bean"). The work may be partly or fully done. Read the bean before you close it.
