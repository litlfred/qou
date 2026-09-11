---
# qou-ywie
title: 'GAP: log_ratio_binding_prototype has the same float64 defect as qou-vsqh, in the log channel'
status: completed
type: task
priority: normal
created_at: 2026-08-31T04:26:46Z
updated_at: 2026-09-11T14:36:57Z
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


## 2026-09-11 — CLOSED. Fix landed, verified by running it, witness reproduces exactly.

Pulled off the `qou-bstl` completion-candidate queue. The bean's last line said
*"Not fixed in the taxonomy PR: it is a producer + witness change and wants its
own."* It got its own: `c4cb60b0922` — *"log_ratio_binding_prototype float64 —
67 -> 0 drained, and the refresh exposes a 68-day-stale witness whose assertion
was passing because of it"*.

**Verified at the source, not on the commit message.** The producer now does
exactly what this bean's `**Fix**` paragraph prescribed:

    :92   from q_parameter import Q_50_DIGIT_STR
    :98   q0 = mp.mpf(Q_50_DIGIT_STR)
    :117  mp.mpf(r["tr_M_atom"]...)      # was float() on a 50-digit string
    :121  L = mp.log(tf / ta)            # was math.log

`grep` for `math.log`, `import math`, bare `sum(` and `float(` returns **three
hits, all in comments** describing the defect in the past tense. Zero in code.

**Runs clean:** exit 0, full output block, the log-ratio spread reported
(0.6118–1.63× all-pairs against the linear channel's 19.34–3999.0×).

**And the witness reproduces byte-identically on substantive content.** `git
status computations/` is empty after the run, and the file's mtime and
`computedAt` are unchanged.

🛑 That last fact nearly became a false finding of mine. A producer that prints
`Witness: <path>` while writing nothing looks exactly like the silent-producer
class (`qou-li9a`, `qou-9d6h`), and I was one step from filing it. It is not:
`WitnessBuilder.save()` is **content-diff-aware** by design — its docstring says
*"if the on-disk witness already exists and differs from the new one ONLY in
ephemeral meta fields (commitSha, scriptCommitSha, computedAt, durationMs), the
on-disk file is PRESERVED unchanged"*, to break the CI drift loop. So an
unchanged mtime after a re-run is the **strongest** available reproduction
result, not a missing write. Worth knowing before diffing any witness re-run in
this corpus.

`allPassed: False` in the committed witness is the honest exposure the fix
commit names — a 68-day-stale assertion that had been passing *because* of the
float64 — not a regression introduced here.

The bean's own reason this mattered stands and is now on exact arithmetic: this
is the **log-ratio** channel, one of only two extensive candidates, whose binding
is an accumulation of `A−1` logarithms — the thing float64 degrades, and the
thing the saturation verdict is read off.

**qou-ywie closes.**
