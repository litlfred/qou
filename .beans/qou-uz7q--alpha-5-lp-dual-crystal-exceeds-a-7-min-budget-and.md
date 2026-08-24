---
# qou-uz7q
title: alpha_5_lp_dual_crystal exceeds a 7-min budget and lacks the required progress logging — but editing it drifts scriptHash for zero payload change
status: todo
type: task
priority: normal
created_at: 2026-08-23T08:55:10Z
updated_at: 2026-08-24T17:11:01Z
---

Surfaced by the #5519 staleness sweep. `computations/alpha/alpha_5_lp_dual_crystal.py`
is TIMEOUT at a 420 s per-producer budget — twice, at 300 s and at 420 s.

## Genuinely long, not hung
Static read: the dominant structure is `for sub in combinations(eigs, ell)`
(line 133) over the cells of partitions with `height == 6` (line 183) — a
combinatorial enumeration, so a long wall time is expected rather than
suspicious.

## It lacks the progress logging AGENTS.md requires
Only 3 flush/print sites in 426 lines. The long-compute discipline requires any
> 5 min script to emit a progress line every ~10 s or ~5 % of work, with wall
elapsed + ETA. Because it does not, **I cannot say how far it got before the
budget expired, or what its true runtime is** — which is precisely the cost the
discipline exists to prevent.

## Why I did NOT just add the logging
Adding a print statement changes the file, which changes `scriptHash` — a
whole-file hash. AGENTS.md is explicit that a comment- or logging-only edit
drifts `scriptHash` while the recomputed payload is byte-identical, and that for
a LONG-COMPUTE producer the right move is to claim it as a bean rather than
spend the pass recomputing numbers that cannot change. Editing this file would
therefore manufacture staleness in the exact audit this branch exists to measure,
and would then demand an expensive re-run to clear the drift it caused.

## What closing this actually needs
1. Measure its true runtime with a generous budget, on its own, teed to a log
   (`python3 -u ... 2>&1 | tee`), so the number is known rather than bounded.
2. THEN decide: if it is minutes, raise the sweep budget and move on. If it is
   hours, it needs a long-compute plan before it can be regenerated in EITHER
   #5519 or #5500 — and the logging should be added in the same pass as the
   re-run, so the scriptHash drift is paid for exactly once.

Until (1), its staleness is UNMEASURED. That is not the same as UNCHANGED, and
it must not be reported as either.

## CORRECTION to my own count — "3 print sites in 426 lines" is wrong

Measured: **20** print sites, at lines 152, 166, 253–256, 286, 292, 296, 299,
302, 303, 306, 310, 316–318, 341, 353, 421. I wrote 3. The producer is not
silent, and I should not have said so without counting.

**The conclusion survives, on a different and narrower basis.** Two things are
actually true, and they are the ones that matter:

1. **No timing anywhere.** `grep -cE "elapsed|ETA|time\.time|perf_counter"` →
   **0**. AGENTS.md's long-compute rule asks for periodic progress *including
   wall elapsed + ETA*; prints without timing cannot tell you whether a run is
   at 5 % or 95 %. That requirement is unmet regardless of the print count.
2. **The expensive region is the silent one.** Prints at 292–318 sit inside the
   stratum/atom loops, so that section does report. But the q-sweep at
   **321–338** (`for q_v in q_sweep_q` × `for atom in atoms`) emits nothing
   until line **341**, after it finishes. A timeout landing inside that nest —
   which is where a q-sweep's cost lives — produces no output at all.

So: "violates the logging rule" holds; "carries only 3 print sites" does not,
and the difference is not cosmetic. The first is a claim about *where and what*
it logs, which I checked; the second was a number I asserted without measuring
and which anyone opening the file would have caught.

## The decision is unchanged

Do **not** add logging now. `scriptHash` is a whole-file hash, so a
logging-only edit drifts it while the payload stays byte-identical —
manufacturing staleness inside the audit that exists to measure it. Add the
timing in the same pass as the eventual re-run, paying the drift once. That
reasoning never depended on the print count.

## This is a class, not one producer

All four TIMEOUT producers, measured:

| producer | lines | print sites | timing refs |
|---|---|---|---|
| `alpha_5_lp_dual_crystal` | 426 | 20 | **0** |
| `binding_via_interface_knot` | 361 | 7 | 3 |
| `block_swap_binding` | 192 | 17 | 3 |
| `he3_tritium_cosh_asymmetry_diagnosis` | 130 | 14 | **0** |

Two of four carry no timing at all. Four of 33 measured producers (12 %) are
TIMEOUT, i.e. unmeasured — and the sweep cannot say how close any of them came
to finishing, which is the decision it would need to inform a budget raise.


---

## Step 1 EXECUTED — and the premise does not survive it

This bean's step 1 was *"measure its true runtime with a generous budget, on its
own, teed to a log, so the number is known rather than bounded."* Done, and
read-only: the whole `computations/` witness tree is snapshotted and restored
around every run, because producers write **sibling** witnesses.

| producer | sweep verdict | measured |
|---|---|---|
| `alpha/alpha_5_lp_dual_crystal` | TIMEOUT at 300 s **and** 420 s | **9 s**, exit 0 |
| `he3_tritium_cosh_asymmetry_diagnosis` | TIMEOUT | **1 s**, exit 0 |
| `binding_via_interface_knot` | TIMEOUT | **> 1800 s**, exit 124 — genuinely long, still **UNMEASURED** |
| `block_swap_binding` | TIMEOUT | in flight |
| `qbeta/qbeta_c3even_exact_sseries_probe` | TIMEOUT | in flight |
| `qbeta/qbeta_c4even_exact_sseries_probe` | TIMEOUT | in flight |

**So this bean's headline — "Genuinely long, not hung" — is refuted for its own
subject.** `alpha_5_lp_dual_crystal` runs in 9 seconds. The static reasoning
that produced that heading (a `combinations(eigs, ell)` enumeration, therefore
long) was plausible and wrong; the combinatorial structure is there, it is just
not expensive at these sizes. **A static read of the code is not a runtime
measurement**, and this bean asserted one from the other.

Two consequences:

1. **The step-2 decision is moot for these two.** There is no budget to raise —
   they finish inside any budget. The sweep's TIMEOUT verdicts are **not
   producer runtimes** and must not be read as such.
2. **`> 1800 s` is still not a runtime.** `binding_via_interface_knot` hit a
   30-minute wall with no completion; per this bean's own standard that is
   UNMEASURED, not "half an hour". Do not quote 1800 s as its cost.

## I checked the obvious catch, and then killed my own explanation

**The catch:** a 9-second run that quietly fell back to a float64 solver would
be *cheaper work*, not *faster work*, and would prove nothing. It did not — the
run recorded `backend: clarabel-mpfr`, `precision_bits: 167`, the same
full-precision path the committed witness carries. The speed is real.

**The explanation that died:** the sweep's recorded environment lists no
`clarabel`, and the pip package is installed now — an inviting story for a slow
fallback path. It is wrong. `_find_clarabel_lp_bin` resolves a **compiled Rust
binary** (`tools/hecke-engine/target/release/clarabel-operator-selection-lp`),
not the Python package, so that diff explains nothing and is not offered as a
cause. The environments do differ (`mpmath 1.3.0` → `1.4.1`), which is a fact I
can state without attributing the timeout to it.

**So the mechanism behind the six TIMEOUTs is unknown.** Candidates I can name
but have not tested: concurrency inside the sweep harness, or a per-run
environment difference. What is established is only that the verdicts do not
measure producer cost.

## A separate blocker, bigger than the timing question

`alpha_5_lp_dual_crystal`'s own guard printed on the run:

> ⚠ raw-float64: `alpha-5-lp-dual-crystal.witness.json`: **101** raw float64
> field(s) would enter the witness

The committed `raw-float64-baseline.json` records **78** for that file, and
`witness_raw_float64_audit.py`'s docstring is explicit: *"a baselined witness
whose count **increases** fails."*

**NOT yet a confirmed regression, and the reason matters.** The two numbers come
from **different functions on different objects**: the producer-side 101 is
`witness.py::_raw_float_paths` counting paths *before* serialization; the
baseline 78 is `witness_raw_float64_audit.py::count_raw_floats` counting the
*committed JSON*. Comparing them directly is a category error, which is why it
is written here as a question rather than a finding. The decisive test is the
audit itself run against a regenerated witness — pending, because it needs a
tree-touching run and a producer batch was in flight.

If it does confirm, it reorders this bean: the blocker on this producer is
**precision, not budget**, and #5500 cannot regenerate it cleanly either way.

## Process note against myself

I ran `alpha_5` twice while the five-producer batch was running. Both use
whole-tree snapshot/restore, so concurrent runs can restore each other's
intermediate state. Nothing was corrupted (`dirty=0` after each), but that was
careless and should not be repeated — serialise tree-touching runs.


## The qbeta pair: cost located, and the obvious fix is not available

Both remaining TIMEOUTs are the exact-`s`-series probes. The running one names
its own expensive phase before it stalls:

    exact sympy series to O(s^9) (log R and u) ...

so the cost is **symbolic algebra**, not a numeric loop. Upstream of that line
sit `sp.simplify` at 62, 75 and 104 and `sp.cancel` at 76 — the class
`local/compute-audit` exists to route ("where is `sympy.simplify`").

**Stated as a candidate, not a cause.** What is observed is that the run sits in
the series phase and that three `simplify` calls precede it. Nothing here is
profiled, so do not record `simplify` as the hot spot without measuring it —
that inference is the same shape as this bean's original "combinatorial,
therefore long", which was wrong.

**"Just lower the series order" does not work, and it is the first thing anyone
will propose.** The order is not a tuning knob:

| probe | `KC` | `NS = 2·KC + 2` |
|---|---|---|
| `qbeta_c3even_exact_sseries_probe` | 3 — *"extract through c_3 (s^6); c_4 needs s^8"* | 8 |
| `qbeta_c4even_exact_sseries_probe` | 4 — *"extract through c_4 (s^8)"* | 10 |

Both are module-level constants with no argparse, and `KC` **is the quantity
the probe extracts**. Lowering it does not make the probe cheaper — it makes it
answer a smaller question. Any long-compute plan has to attack the symbolic
route (targeted `cancel`/`together`/`radsimp` instead of blanket `simplify`, or
an exact-rational route that avoids the series), not the order.

**Expectation, not a measurement:** `c4even` runs at `NS = 10` against
`c3even`'s `NS = 8`, and exact-series cost grows steeply with order, so if
`c3even` exceeds 30 min then `c4even` should be worse. Recorded so the eventual
number can be checked against it rather than rationalised after the fact.
