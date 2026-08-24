---
# qou-2wtx
title: cross_check_trM_cw_seminormal_leg completes in 996s and FAILS (worst 1.91e+00) where its committed witness says allPassed — the 300s budget hid a pass-to-fail regression
status: todo
type: task
created_at: 2026-08-24T18:49:51Z
updated_at: 2026-08-24T18:49:51Z
---

## The measurement

`cross_check_trM_cw_seminormal_leg.py` was the **seventh** TIMEOUT in the q0-muon
staleness sweep. Measured with a generous budget, it does **not** time out —
it **completes in 996 s (16.6 min), exit 1**:

    triton    A=3  |Δ|/ref=1.20e+00  FAIL  [1s]
    helium-3  A=3  |Δ|/ref=9.55e-01  FAIL  [1s]
    helium-4  A=4  |Δ|/ref=1.91e+00  FAIL  [995s]

    worst |Δ|/ref = 1.91e+00  (FAIL)
    witness -> cross-check-trM-cw-seminormal.witness.json  allPassed: False

**The committed witness says `allPassed: True`.** So the producer no longer
reproduces its own committed result, and the direction is **pass → fail**.

## The magnitude, and why it is not rounding

The witness was last *regenerated* by `6647e7e4ed`, whose message records
**"all 6 atoms 1ppQ-confirmed (worst 7.28e-49)"**. Today's worst is
**1.91e+00** — forty-nine orders of magnitude. The two commits that touched the
witness since (`d106e6bad9`, `4101909790`) only stamped provenance; they did not
recompute values.

## Candidate cause — NAMED, NOT ESTABLISHED

The producer's code changed after the witness was last regenerated:

| commit | date | what |
|---|---|---|
| `6647e7e4ed` | 2026-07-18 | witness regenerated, worst 7.28e-49 |
| `9df06e0fbe` | 2026-07-18 | `mp.fsum` for the tr_M sum |
| **`34b2a75d43`** | **2026-08-23** | **`fix(qou-fl9i)`: raise 822 sub-canonical `mp.dps` sites to `set_compute_dps()`** |

A precision change five weeks after the last regeneration is the obvious
suspect. **It is a suspect, not a finding** — I have not bisected it, and my
container also runs `mpmath 1.4.1` against the sweep's recorded `1.3.0`, which
is a second untested candidate. Do not record either as the cause without
measuring.

Also unrepeated: this is **one run**. Confirm reproducibility before acting.

## Why this matters beyond one producer

**The sweep's budget is what hid it.** At the 300 s per-producer budget this
producer returns TIMEOUT; it needs 996 s. So the verdict that looked like "too
slow to measure" was concealing a live **pass → fail regression** in a
cross-check between two independent routes to `tr_M`.

That sharpens `qou-uz7q`'s conclusion. I closed that bean's step 2 as "the two
fast ones need no budget; the four long ones need a long-compute plan." This
case adds the missing half: **the cost of a too-low budget is not merely
`UNMEASURED` — it can be a hidden regression.** A budget that lets a 996 s
producer finish would have surfaced this weeks ago.

**And the population growth is what surfaced it at all.** This producer only
entered scope because main's `4101909790` ("label 229 witnesses from their own
payload") stamped its witness muon, which is the same event behind the 47 → 142
denominator growth in `qou-6q7q`. The two findings are one event seen twice.

## Cross-links

- `qou-dau6` / `qou-3zby` — the same *family* (`cross_check_trM_1ppb`), a
  **different script**, and a different diagnosis (C/D convention straddle +
  muon/proton pin mismatch). Not assumed to be the same cause here.
- `qou-uz7q` — the TIMEOUT-verdict work this came out of.
- `qou-6q7q` — the population growth that brought it into scope.
