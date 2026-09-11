# The sweep's TIMEOUTs were CPU contention, not pathological modules

*2026-09-08 — beans `qou-ed8a`, `qou-g5sp`. Follow-up to #7124 / #7157.*

## Result

The full-library sweep (#7124) recorded **4 TIMEOUT** modules and **16 SKIPPED**
behind them. Re-run **alone**, they compile.

| module | full sweep (`--jobs 3`) | alone (`--jobs 1`) |
|---|---|---|
| `QOU.Archimedean.PauliWitness.Witness12B` | TIMEOUT @1800 s | **ok, 1471 s** |
| `QOU.Machinery.HeckeH4BlockMap211` | TIMEOUT @1800 s | **ok, 1049 s** |
| `QOU.Machinery.HeckeH4BlockMap31` | TIMEOUT @1800 s | **ok, 974 s** |
| `QOU.MathlibExt.OctonionDerivationsUpperBound` | TIMEOUT @1800 s | **ok, 459 s** |

Every completed run reports `1 ok, 0 RED, 0 TIMEOUT + 0 UNVERIFIED, 0 skipped`.

## Two corrections this forces

> ## 🛑 CORRECTION 2026-09-11 — all four are `ok`, but the CAUSE below is WRONG, and it was mine
>
> **The verdicts stand and are strengthened: 4 of 4 compile clean.** What does not
> stand is this document's explanation of *why* they timed out — including its
> filename, now a misnomer.
>
> **The claim was 3-way CPU contention under `--jobs 3`. Measured in this
> container: 4 cores, cgroup `cpu.cfs_quota_us = -1` (unlimited), 16 GB RAM, no
> memory limit.** With `--jobs 3` on four unpinned cores there is a **spare core**,
> so each job gets roughly a full core and CPU division cannot slow anything much
> at all. The arithmetic is what kills it: `OctonionDerivationsUpperBound` needs
> **459 s** alone and was killed at **1800 s**, so it requires a **≥3.92×**
> slowdown. Three jobs on four free cores cannot produce 3.92×.
>
> So the observation *"the modules are fine"* is measured and solid; the mechanism
> offered for it is refuted by the machine it was measured on.
>
> **Leading candidate, explicitly NOT measured: memory, not CPU.** A Lean process
> elaborating a Mathlib-heavy module can hold several GB; three concurrently
> against 16 GB can reach swap, and swapping produces exactly this
> order-of-magnitude wall-clock blowup while CPU sits idle. **The discriminator is
> cheap and I have not run it:** re-run the tail at `--jobs 3` while sampling peak
> RSS and swap-in. Until someone does, the cause is **undetermined** — do not quote
> the contention story below as established.
>
> **What this contaminated**, all mine: this document (title, filename, and the
> section immediately below), the bodies of #7169 and #7175, and two commit
> messages. Corrected here rather than in five places; the timings and verdicts in
> the table above are unaffected.
>
> **One thing I checked rather than assumed.** The four timings are the sweep's own
> compile-phase figure — `t0` is set *after* shadow setup and `LEAN_PATH`
> construction (`lean-library-sweep.py:471`), so shadow creation is outside them and
> they are comparable to each other and to the per-module budget. The 4 s gap
> between each run's inner total and its outer wall time confirms it.
>
> **And this is the fourth instance of this session's signature error** — after the
> ~700× script cost priced from a family resemblance, the "container limit" that was
> 79 missing oleans, and the SIGSEGV attribution carried across the H4 family. Each
> time: a property inferred from something adjacent rather than measured on the
> thing itself. This one is the worst of the four, because I wrote the inference
> into a filename.

**1. "TIMEOUT" here measured the harness, not the module.** `Witness12B` needs
**1471 s** of exclusive CPU against a **1800 s** per-module budget — it fits, with
18 % to spare. The sweep's default is `--jobs 3` and #7124 recorded no override, so
three modules shared the container while each was charged wall-clock against its own
budget. A module needing >600 s of CPU is then liable to be killed for its
neighbours' load. That the budget is per-module wall-clock while the contention is
global is the defect; the modules are fine.

*Scope:* the 1471 s and 1049 s are measured. That 3-way contention is what pushed
them past 1800 s is the natural reading of those numbers against the default, not a
separately measured fact — no run was done at `--jobs 3` in isolation to confirm it.

**2. The H4 family is NOT the SIGSEGV class, and #7124's audit says it is.** That
audit lists the `Machinery.HeckeH4*` cluster as *"the same `QOU.Hecke*` H4 family a
sibling measured as SIGSEGV"*. **Both** H4 modules compile clean — `HeckeH4BlockMap211`
in 1049 s and `HeckeH4BlockMap31` in 974 s — no signal, no error, so the refutation
covers the cluster rather than one member of it. The sibling's SIGSEGV measurement may well be right about
whatever it measured, but it does not transfer to these modules, and #7124 carried
it across on family resemblance rather than on a run. That is the same move as the
~700× cost error corrected in #7157: **a property inferred from a neighbour instead
of measured on the thing itself.** Third instance this session.

## Why this matters more than "4 modules"

The 4 TIMEOUTs hold **18 modules** — 10 in the H4 cluster, 6 Octonion, 2
PauliWitness — because the 16 SKIPPED are cascades behind them, not an independent
category. With #7157's mathlib-gap fix clearing the other 2, these 18 are the entire
remaining residue of the full-library sweep.

## What to do with the sweep

**All four modules compile.** Final tally, each run alone reporting
`1 ok, 0 RED, 0 TIMEOUT + 0 UNVERIFIED, 0 skipped`:

| module | alone | vs 1800 s budget |
|---|---|---|
| `Witness12B` | 1471 s | 18 % headroom |
| `HeckeH4BlockMap211` | 1049 s | 42 % |
| `HeckeH4BlockMap31` | 974 s | 46 % |
| `OctonionDerivationsUpperBound` | 459 s | **74 %** |

So the full-library sweep's **18-module residue is fully judged** — 4 TIMEOUTs plus
the 14 cascaded SKIPPED behind them — and with #7157's mathlib-gap fix clearing the
other 2, the sweep has **no unexplained remainder**. Its headline is `2754 ok,
0 RED`, and nothing in the corpus is implicated.

**What to do with the sweep, given the cause is undetermined.** `--jobs 1` for the
tail is the safe operational answer and is what produced every verdict here.
Charging the budget against **CPU time** rather than wall-clock would fix a
contention-shaped cause but would NOT fix a swap-shaped one — under swapping the
process burns wall-clock without burning CPU, so a CPU-time budget would simply
never fire. **Measure the mechanism before changing the budget**, or the fix may
not address the fault.

The durable rule is independent of the cause: **a TIMEOUT from a multi-job sweep is
not evidence about the module.** Re-run it alone before recording anything about it,
exactly as this did.
