---
# qou-2wtx
title: cross_check_trM_cw_seminormal_leg completes in 996s and FAILS (worst 1.91e+00) where its committed witness says allPassed — the 300s budget hid a pass-to-fail regression
status: todo
type: task
priority: normal
created_at: 2026-08-24T18:49:51Z
updated_at: 2026-08-24T19:32:43Z
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


---

## BISECTED — and my third hypothesis was wrong too

`git bisect run` over 4445 revisions between the last good witness regeneration
and HEAD, using the 2-second A=3 case as the test:

> **first bad commit: `2c35a52e08` — *"tnjb: finish the remaining 16 — the
> 'environment limit' was solvable"*** (2026-08-08)

**It is a pure witness-regeneration commit.** 19 files, all `*.witness.json`
plus `q0_anchor_manifest.json` and the migration script itself. **No producer
source changed** — which is why all three of my source-level suspects missed.

## The mechanism, verified end to end

The producer's own docstring, line 30:

> *reference is loaded from `markov/markov-peel-atomic-tr-m.witness.json`*

read at line 76. And `computations/markov/markov-peel-atomic-tr-m.witness.json`
is **one of the 19 files `2c35a52e08` rewrote** (80 lines changed).

So: **the tnjb migration regenerated the reference the cross-check compares
against, and the cross-check was never re-run to match.** It has been failing
since 2026-08-08 — sixteen days.

## This is NOT a bad commit — it is a missed downstream

`2c35a52e08` did the right thing: `tnjb`'s scope is witnesses whose recorded q₀
their producer can no longer reproduce, and regenerating those is a correction.
What was missed is that one of them is a **reference input to a cross-check**,
so regenerating it silently moved the goalposts for a consumer that nobody
re-ran. Blame the dependency edge, not the commit.

## Three hypotheses, three refutations, one bisect

| # | hypothesis | how it died |
|---|---|---|
| 1 | mpmath 1.4.1 vs the sweep's 1.3.0 | downgraded and re-ran — byte-identical |
| 2 | `34b2a75d43`, the `mp.dps` → `set_compute_dps()` change to this very file | ran the pre-commit file — identical |
| 3 | the C → D Markov-convention migration in `gram.py` | bisect landed elsewhere entirely |

All three were named on **plausibility and proximity**; none survived contact
with a measurement. The bisect cost roughly ten minutes and answered what an
hour of reading the diff could not. **When a cheap decisive test exists, run it
before naming a suspect at all.**

## Why it stayed hidden for 16 days

The producer needs **996 s**; the sweep's per-producer budget is **300 s**, so
its verdict was `TIMEOUT` — which reads as "too slow to measure" and is in fact
"a live pass → fail regression nobody has looked at". That is the concrete cost
of the budget, and it is the strongest argument in `qou-uz7q` for raising it —
stronger than any of the timing evidence there.

## Fix

Re-run `cross_check_trM_cw_seminormal_leg` and commit the regenerated witness —
**if** the new numbers are the correct ones. That question is open and is not
mine to settle here: `|Δ|/ref` of 1.20, 0.955 and 1.91 are enormous for a
cross-check between two routes to `tr_M`, so the regenerated peel reference and
the seminormal leg now disagree structurally. Someone has to decide **which leg
is right** before either is blessed. Do not simply regenerate the witness to
make the red go away.


---

## Option 3 — hunting the O(1) term. Four hypotheses tested, four refuted.

Full failure list, including the two small atoms the 90-second runs never reached:

| atom | Z | N | A | s | a | i | **cw** | legB/legA |
|---|---|---|---|---|---|---|---|---|
| neutron | 0 | 1 | 1 | 5 | 2 | 4 | **0** | 1.070 |
| deuteron | 1 | 1 | 2 | 11 | 4 | 7 | **1** | 1.481 |
| helium-3 | 2 | 1 | 3 | 18 | 6 | 10 | **1** | 1.955 |
| triton | 1 | 2 | 3 | 16 | 6 | 12 | **1** | 2.200 |
| helium-4 | 2 | 2 | 4 | 23 | 8 | 15 | **1** | 2.910 |

**1. Constant normalisation — REFUTED.** The ratio is not constant.

**2. Missing q-power per strand — REFUTED.** `ratio^(1/A)` = 1.070, 1.217, 1.301,
1.250, 1.306; `ratio^(1/3A)` = 1.023 … 1.093. Neither is constant. `q₀ = 1.110`,
`q₀³ = 1.368` are near enough to tempt and not near enough to be true.

**3. The colour-weighted p–n seam — REFUTED, and this was my leading
hypothesis.** The **neutron classifies ZERO crossings as `cw`** — `a_cw`/`b_cw`
and δ never enter its computation — and it is still **7 % wrong**. Worse for the
hypothesis: **`cw` count is exactly 1 for every bound atom**, independent of Z,
N and A. So the composition-dependence I reported last turn (triton 2.200 vs
helium-3 1.955 at equal A) **cannot** come from seam count; there is only ever
one seam. I named the seam because the producer's docstring flags it as
CRITICAL — proximity again, not mechanism.

**4. The `i` (σ⁻¹) count — REFUTED.** It is the only structural count that
orders correctly (4, 7, 10, 12, 15 against 1.070, 1.481, 1.955, 2.200, 2.910),
which is exactly why it needed testing rather than adopting: `ratio/i` runs
0.267 → 0.183 and `ratio^(1/i)` runs 1.017 → 1.074. Monotone, not a law.

## Stop fitting — the method is wrong

Five points and several plausible structural counts is a numerology generator,
not a diagnosis. Every one of the four above was a curve through the end-to-end
ratio. **The end-to-end ratio cannot identify the defect**; only a term-by-term
comparison of the two legs' ingredients can.

## The observation that reframes it

The re-pin moved leg A's neutron value by **8 significant figures**
(`0.92323329718…` → `0.92323322991…`), while leg B differs by **7 %**. An
un-changed leg B would therefore have been ~7 % off *before* `2c35a52e08` too,
and the assertion would already have been red. It was green.

**So leg B must have changed at that commit as well** — and `2c35a52e08` touched
exactly one non-witness file: `q0_anchor_manifest.json`, **+17 stems**. Adding a
stem changes what `q_parameter` resolves for producers in leg B's cone. That is
a mechanism that would move *both* legs, and it is the first hypothesis in this
list that is not a curve fit.

**Next, and it is a measurement not an argument:** compute leg B's neutron value
at `2c35a52e08^` and at `2c35a52e08`. If it moves, the manifest entries are the
carrier and the fix is a scope question about those 17 stems. If it does not
move, the bisect's "first bad" is an artifact of leg A alone and the 7 % predates
the window entirely — which would mean this cross-check has been wrong for far
longer than sixteen days.

The neutron is the right probe: A=1, 11 crossings, **no `cw`**, runs in under a
second.
