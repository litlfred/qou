# The sweep's TIMEOUTs were CPU contention, not pathological modules

*2026-09-08 — beans `qou-ed8a`, `qou-g5sp`. Follow-up to #7124 / #7157.*

## Result

The full-library sweep (#7124) recorded **4 TIMEOUT** modules and **16 SKIPPED**
behind them. Re-run **alone**, they compile.

| module | full sweep (`--jobs 3`) | alone (`--jobs 1`) |
|---|---|---|
| `QOU.Archimedean.PauliWitness.Witness12B` | TIMEOUT @1800 s | **ok, 1471 s** |
| `QOU.Machinery.HeckeH4BlockMap211` | TIMEOUT @1800 s | **ok, 1049 s** |
| `QOU.Machinery.HeckeH4BlockMap31` | TIMEOUT @1800 s | *running* |
| `QOU.MathlibExt.OctonionDerivationsUpperBound` | TIMEOUT @1800 s | *queued* |

Both completed runs report `1 ok, 0 RED, 0 TIMEOUT + 0 UNVERIFIED, 0 skipped`.

## Two corrections this forces

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
sibling measured as SIGSEGV"*. `HeckeH4BlockMap211` compiles clean in 1049 s — no
signal, no error. The sibling's SIGSEGV measurement may well be right about
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

Do not raise `--timeout`; that treats the symptom. Either drop to `--jobs 1` for the
tail, or charge the budget against CPU time rather than wall-clock. Until then, a
TIMEOUT from a multi-job sweep is **not** evidence about the module — re-run it alone
before recording anything about it, exactly as this did.
