# `--jobs` multiplies against Lean's own threading — the real cause of the sweep's TIMEOUTs

*2026-09-11 — bean `qou-ed8a`. Closes the cause question left open by #7182.*

## The cause, measured

**Each `lean` process spawns 7–8 OS threads and tries to fill the whole machine.**
The sweep never sets `LEAN_NUM_THREADS`, so Lean sizes its own task pool from
hardware concurrency. Measured live during a reproduction on the H4 cluster:

```
pid 31325: threads=8  QOU/Machinery/HeckeH4WedderburnMulB.lean   198% CPU
pid 31326: threads=7  QOU/Machinery/HeckeH4WedderburnMulA.lean   197% CPU
loadavg 8.10   nproc 4   MemAvailable 10.4 GB   SwapTotal 0
```

So `--jobs N` does **not** mean *N cores*; it means **N processes each trying to
take all 4**. At the default `--jobs 3` that is ~24 threads on 4 cores — roughly
**3× CPU oversubscription**, with each module getting about a third of the machine
instead of the whole of it. A module that needs 459 s with 4 cores then needs
~1400 s with 1.3, and the 1800 s per-module budget is reached. **That is the 3.92×
the Octonion case required.**

And `--jobs 1` — which produced every verdict in #7169 / #7175 / #7182 — gives the
single Lean process all four cores. That is why the "alone" runs were so fast.

## Three hypotheses of mine, all wrong, and why the last one is instructive

| hypothesis | published in | verdict |
|---|---|---|
| 3 jobs share 4 cores, so a core is spare ⇒ contention can't explain it | #7169, #7175 | **wrong arithmetic** — 3 jobs demand ~12 cores, not 3 |
| memory pressure → swap | #7182 | **refuted**: `SwapTotal: 0 kB`; pressure would OOM-kill, reported as a signal death, not TIMEOUT |
| a concurrent `lake build` from the SessionStart hook | this session's chat | **refuted**: the process table during the reproduction shows no `lake`, no competing build — only the sweep's own two `lean` processes |

The instructive one is the first. **Contention was the right answer all along and I
talked myself out of it with a wrong model of `--jobs`** — I computed one job as one
core, found a spare core, and concluded the mechanism was impossible. Then I spent
two further hypotheses looking for an exotic cause because I had excluded the
ordinary one on bad arithmetic. The measurement that settled it (`ps` for `%CPU`,
`ls /proc/<pid>/task`) was available at every step.

## Consequence: the headroom table in the prior audit compares unlike things

`2026-09-08-sweep-timeouts-were-contention.md` tabulates each module's "alone" time
against the 1800 s budget and reads off headroom. Those alone-times are **4-core**
times; the budget was being applied to **~1.3-core** runs. The verdicts (4/4 `ok`,
0 RED) are unaffected — a module that compiles, compiles — but the headroom
percentages are not a like-for-like margin and should not be read as "how close this
module came to its budget". Same caveat for that document's title, already flagged
there as a misnomer.

## The fix

Bound **total** parallelism, not process count. Either

- set `LEAN_NUM_THREADS` so that `jobs × threads ≲ nproc` (e.g. `--jobs 2` with
  `LEAN_NUM_THREADS=2` on a 4-core box), or
- keep `--jobs 1` for the heavy tail and let each module have the machine.

Do **not** raise `--timeout`: that hides a 3× throughput loss rather than fixing it.
And note the earlier recommendation — *charge the budget against CPU time* — is now
positively wrong: under this mechanism the process burns CPU on all its threads, so
a CPU-time budget would fire **sooner**, not later, and would kill healthy modules
faster than the wall-clock one does.

## Durable rule

A TIMEOUT from a multi-job sweep is not evidence about the module, and the reason is
now concrete: **the module was not given the machine the budget was calibrated on.**
Re-run alone before recording anything about it.
