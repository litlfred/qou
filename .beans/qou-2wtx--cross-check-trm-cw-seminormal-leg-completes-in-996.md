---
# qou-2wtx
title: cross_check_trM_cw_seminormal_leg completes in 996s and FAILS (worst 1.91e+00) where its committed witness says allPassed — the 300s budget hid a pass-to-fail regression
status: todo
type: task
priority: normal
created_at: 2026-08-24T18:49:51Z
updated_at: 2026-08-24T18:59:21Z
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


---

## Reproduced — and BOTH named suspects are now REFUTED

The bean above listed three things to close before acting. Two are closed and
the third killed my own hypothesis.

**1. "One run, unrepeated" — closed.** Re-ran the fast A=3 cases: identical,
`triton 1.20e+00 FAIL`, `helium-3 9.55e-01 FAIL`. The failure reproduces.

*Method note worth reusing:* helium-4 alone is 995 of the 996 s, while triton
and helium-3 take **1 s each and also fail**. So every hypothesis below was
testable in ~2 seconds instead of ~17 minutes. When a long producer fails on a
cheap case too, test on the cheap case.

**2. mpmath version — REFUTED.** Downgraded to the sweep's recorded `1.3.0`,
re-ran, restored `1.4.1`. Output **byte-identical** (`1.20e+00` / `9.55e-01`).
The environment is exonerated.

**3. `34b2a75d43` — REFUTED, and it was my leading suspect.** It *does* touch
this producer directly (3 insertions, 1 deletion):

```diff
-mp.mp.dps = 50
+import _path_bridge
+from _precision import set_compute_dps
+set_compute_dps()
```

Restored the pre-commit file and ran: **identical**, `1.20e+00` / `9.55e-01`.

The arithmetic said so before the test did, and I should have weighted it
harder: `set_compute_dps()` *raises* precision (50 → 65), and a precision change
moves a cross-check by ~1e-50, not by **191 %**. **A 1.91e+00 relative
discrepancy is structural, not numerical.** I named a precision commit as the
suspect because it was the most recent change to the file, which is proximity,
not mechanism.

## Where it actually has to be

The producer is unchanged in effect; the environment is exonerated. So the cause
is in a **dependency** that changed between the last witness regeneration
(`6647e7e4ed`, 2026-07-18, worst 7.28e-49) and now. Commit counts in the import
cone since that point:

| module | commits since `6647e7e4ed` |
|---|---|
| `mass_at_3A_proper.py` | 22 |
| `pyhecke/gram.py` | 18 |
| `wedderburn_jones_markov.py` | 8 |
| `hecke_core_legacy.py` | 3 |

**Candidate, explicitly untested:** an O(1) relative shift is the signature of a
**convention change**, and the C → D Markov-parameter migration
(`z = √q/(q+1)` → `z = q³/(q²+1)`) is exactly that shape and was live across this
window. `pyhecke/gram.py` — which carries `z` — has 18 commits in it. Do not
record that as the cause without bisecting; I have now named two suspects on
plausibility and both were wrong.

**Next step is a bisect over the cone, not more reasoning.** The 2-second A=3
case makes it affordable: ~5 steps over 18 `gram.py` commits.
