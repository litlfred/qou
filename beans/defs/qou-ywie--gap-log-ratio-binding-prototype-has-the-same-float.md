---
# qou-ywie
title: 'GAP: log_ratio_binding_prototype has the same float64 defect as qou-vsqh, in the log channel'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-31T04:26:46Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

## Second instance of `qou-vsqh`, in the log channel

Found while building the channel taxonomy (`qou-ge9f`).

`computations/log_ratio_binding_prototype.py` has the **identical** defect #6338
fixed in `derived_bond_graph_binding`:

    from q_parameter import Q as q0        # the FLOAT64 Q, not Q_50_DIGIT_STR
    import math ; ... math.log(...)        # float64 accumulation
    float(...)  x5

Measured across all six live binding-channel producers:

| producer | `math.log/sqrt/exp` | `float()` | q import |
|---|---|---|---|
| `binding_canonical` | 0 | 17 | `Q_MP`, `HA_MP` ✓ |
| `derived_bond_graph_binding` | 1* | 1* | `Q_50_DIGIT_STR` ✓ (fixed, #6338) |
| **`log_ratio_binding_prototype`** | **1** | **5** | **`Q` (float64)** ✗ |
| `derive_binding_chain_cooperative` | 0 | 10 | `Q_MP` ✓ |
| `binding_link_volumes` | 0 | 13 | — |
| `magic_A_formula` | 0 | 1 | — |

(* the remaining hits in `derived_bond_graph_binding` are in the explanatory
comment #6338 added, not in code.)

**Why it matters here specifically.** This is the *log-ratio* channel — the one
the taxonomy identifies as one of only two extensive candidates, and the one whose
binding is an accumulation of `A−1` logarithms. Accumulation is exactly what
float64 degrades, and it is exactly what the saturation verdict is read off.

**Fix**, same shape as #6338: read `Q_50_DIGIT_STR`, derive `h = q − 1/q`, replace
`math.log` with `mp.log` and `sum` with `mp.fsum`, serialize with `_precision.fmt`,
re-run and refresh `log-ratio-binding-prototype.witness.json`. Expect the physics
numbers not to move and the derivation residual to.

Not fixed in the taxonomy PR: it is a producer + witness change and wants its own.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8391, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
