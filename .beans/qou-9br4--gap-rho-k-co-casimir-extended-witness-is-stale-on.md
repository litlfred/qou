---
# qou-9br4
title: 'GAP: rho-k-co-casimir-extended witness is stale on main — needs a ~45min re-run'
status: completed
type: task
priority: normal
created_at: 2026-08-15T20:24:06Z
updated_at: 2026-08-16T03:15:55Z
---

`computations/rho-k-co-casimir-extended.witness.json` on `main` carries 4 raw
float64 fields and is the sole RED on `scripts/precision-gates.sh` (raw-float64
ratchet, "REGRESSED 3 -> 4"). It is NOT a new leak: commit `29b209ce9` already
fixed the producer to serialise the four `compute_wall_sec` telemetry fields as
strings. The witness was simply never re-run, so its recorded `scriptHash`
(`6b46797533d4`) no longer matches the producer (`aa4e42c6f2da`).

WHY THIS NEEDS A BEAN RATHER THAN AN IDLE-PASS FIX. The re-run must reach
helium-4 (Z=2, N=2, A=4, n=12; 77 partitions), which the committed witness
itself records at 2533 s — ~42 min, and the producer saves incrementally, so a
run killed before helium-4 writes a FIVE-atom witness over the committed six.
Committing that would drop an atom: a regression dressed as a fix.

Attempted twice on 2026-08-15 from PR #5106 (as a rider, since the RED blocked
that branch's preflight). Both attempts reached helium-4 and both were killed by
infrastructure, never by the compute:
  1. `nohup ... &` inside a Bash tool call — the detached child was torn down
     with its launching wrapper.
  2. Relaunched under `setsid` via the harness background runner — killed by a
     container restart ~20 min in.

MONITORING TRAP, recorded because it cost real time: `pgrep -c -f
rho_k_co_casimir` MATCHES ITS OWN COMMAND LINE (the pattern appears in the
monitoring command), so it returns >= 1 whether or not the job is alive. It
reported "still running" for 76 minutes after the process was already dead.
Use `pgrep -af "python3 .*rho_k_co_casimir"` and read the log's mtime instead.

WHAT A FIX LOOKS LIKE. Run `python3 -u computations/rho_k_co_casimir_extended.py
2>&1 | tee /tmp/rho_k.log` somewhere that survives ~45 min uninterrupted; confirm
the resulting witness has six atoms, zero raw floats, and a `scriptHash` matching
the producer; then re-run `scripts/precision-gates.sh` to confirm the ratchet is
green and commit both the witness and the refreshed audit witness.

The payload numbers cannot change — only the four telemetry fields go float ->
string — so there is no scientific content at risk, only the gate.

---

## The two kills were probably NOT infrastructure — and the remedy is already on main

Cross-filed from `qou-5qwb`, which chased the same witness from the other end.
This bean records both attempts as "killed by infrastructure, never by the
compute". A third attempt from this session, instrumented, says otherwise.

**Measured at helium-4, 2026-08-15:**

| observation | reading |
|---|---|
| CPU time unchanged across a 6-second sample, both workers | not computing |
| both workers in `futex_do_wait` | blocked, not busy |
| RSS **4.8 GB + 5.1 GB** of a 16 GB box | two workers holding ~10 GB |
| `khugepaged` at 80 % | kernel thrashing |
| killing the run | freed ~5 GB immediately |

**Cause.** The largest partition of 12 is **dim 7700** (λ = (5,3,2,1,1)), and
`hoefsmit_matrices_numpy` stores generators DENSE: `7700² × 8 B × 11 =
5.22 GB` per worker. `n_workers = min(cpu_count(), len(parts))` therefore asks
for **~20 GB on a 16 GB box**. It does not slow down — it hangs, and from
outside that is indistinguishable from a container restart.

So attempt 2 "killed ~20 min in" is at least as consistent with an OOM /
thrash as with a restart. Worth ruling out before spending a fourth 45 minutes.

**Remedy, already merged (PR #5104, on `main`).** The producer now takes
`--workers N` / `$RHO_K_WORKERS`:

    python3 -u computations/rho_k_co_casimir_extended.py --workers 1 2>&1 | tee /tmp/rho_k.log

It is a **cap**: absent the flag the behaviour is byte-for-byte what it was, so
nothing else changes. One worker needs ~6 GB rather than ~20 GB and fits
comfortably; the cost is wall time on the parallel section.

**Two confirmations for this bean's own warnings.** The `pgrep` self-match
trap recorded above bit this session independently — same 45-minute false
"still running". And the five-atom-over-six partial-write risk is real and
worse than described: a gutted witness scores **zero raw floats**, so the
raw-float64 ratchet reads it as a *perfect drain*. `witness_shape_guard.py`
(PR #5089) now catches exactly that; run it before committing any regenerated
witness.

**Not claimed:** that `--workers 1` will finish. It removes the memory wall
this session measured; whether the remaining ~45 min survives the container is
still open, and that part of this bean stands.

**Ownership.** This item is `qou-9br4`'s, and this session is not running the
compute — only handing over the diagnosis. `qou-5qwb` and `qou-bk0q` (the
dense-storage waste, with a validated prototype) are the supporting analysis.

### UPDATE — the memory wall is gone; `--workers` is no longer needed for this

PR #5152 landed the P22 auto-switch in `hoefsmit_numpy.chi_numpy`: above
**dim 1200** the generators are held by structure (diagonal + symmetric pairs)
instead of dense. The He-4 blocking partition is dim 7700, so it now routes
structured.

Measured peak RSS on the structured path, and the scaling checks out against
the accumulator-only prediction (2 x dim^2 x 8 B):

| dim | predicted | measured delta | dense generators alone |
|---|---|---|---|
| 1485 | ~35 MB | 52 MB | 194 MB |
| 2376 | ~90 MB | 81 MB | 497 MB |

Extrapolated to dim 7700:

    dense generators      5.22 GB   <- what hung it
    structured generators 2.71 MB
    accumulator + temp    0.95 GB   (unavoidable: M is dense dim x dim)
    ------------------------------------------------
    per worker           ~0.95 GB   x4 workers ~3.8 GB of 16 GB

So the default `cpu_count()` pool should now fit comfortably, and the run is
also expected to be FASTER at that dim (structured wins above the crossover:
0.70x at dim 1485, 0.84x at 2376).

**Revised recommendation:** just run it normally —

    python3 -u computations/rho_k_co_casimir_extended.py 2>&1 | tee /tmp/rho_k.log

`--workers 1` remains available and still correct if a machine is tighter, but
it is no longer the thing standing between this bean and a finished witness.

**Still not claimed:** that the run completes. Wall time (~40 min) and container
survival are untouched by any of this, and that is the part of this bean that
stands. Correctness of the switch is verified — rel_diff exactly 0.0 below the
threshold and 1.26e-16 above, against the pre-switch dense path.

---

## Attempt 3 (this session, 21:12–22:32Z) — independently reproduces the section above

Ran a third attempt before seeing the cross-file from `qou-5qwb`. It reached the
same conclusion from the same evidence, which is worth recording as an
independent confirmation rather than as a competing account.

| pid | elapsed | CPU time | %CPU | RSS |
|---|---|---|---|---|
| main | 1:20:30 | 11:38 | **14.4 %** | **6.97 GB** |
| worker | 1:21:53 | 4:31 | 5.5 % | 3.58 GB |
| worker | 1:19:37 | 1:29 | 1.8 % | 1.37 GB |
| worker | 1:18:20 | 0:06 | 0.1 % | 90 MB |

~12 GB resident on a 16 GB box at 14 % CPU; killing it freed 14.4 GB. Same
signature, same verdict: **starved, not slow**.

**Correcting my own entry.** I first wrote that the cause "was me", for running
this alongside a `lake build`, a 1.6 GB cache extract and two `qa-sweep` runs.
That is at most half right and the weaker half. The section above has the real
mechanism — `hoefsmit_matrices_numpy` stores generators dense, so
`7700² × 8 B × 11 = 5.22 GB` **per worker** at `λ = (5,3,2,1,1)`, and the
default `n_workers` asks for ~20 GB regardless of what else is running. My
co-tenancy made an already-doomed allocation fail sooner. The producer would
have thrashed on an idle box too.

**Consequence for the "do not attempt a fourth" line above.** That was written
before `--workers 1` (PR #5104) was known to this session. It is superseded: a
fourth attempt IS worth one shot, under the section above's conditions —
`--workers 1`, idle box, ~45–60 min — because the memory wall the first three
hit is removed rather than merely waited out. What is still unproven is whether
the remaining wall time survives the container.

**One addition to the partial-write warning.** The five-atom-over-six risk is
worse than either entry first said, and the cross-file has it right: a gutted
witness scores **zero raw floats**, so the raw-float64 ratchet reads it as a
*perfect drain*. Run `witness_shape_guard.py` (PR #5089) before committing any
regenerated witness — the ratchet alone will not catch a truncation.

**A liveness note both entries should carry.** Elapsed time cannot distinguish
slow from starved. A healthy run sits near 100 % CPU; the three failures all
sat under 15 %. Check CPU time, not the clock — and never
`pgrep -c -f rho_k_co_casimir`, which self-matches (it cost this session 76
minutes of false "still running", independently of the same trap recorded
above).

---

## Attempt 4 (`--workers 1`, 23:36–23:40Z) — the memory wall IS gone; container lifetime is now the ONLY blocker

First attempt under the `--workers 1` cap from PR #5104. Killed at ~4 min by a
**container restart**, not by the compute — and this time there is positive
evidence of health at the moment it died, which is what makes the run worth
recording despite finishing nothing.

| | attempts 1–3 (default workers) | attempt 4 (`--workers 1`) |
|---|---|---|
| main-process %CPU | **14.4 %** | **99.8 %** |
| main-process RSS | **6.97 GB** | **120 MB** |
| aggregate RSS | ~12 GB / 16 GB | well under |
| CPU time over a 25 s sample | flat | **3:42 → 4:07** |
| how it ended | starved / thrash | container restart |

`--workers 1` does exactly what `qou-5qwb` predicted: 120 MB against 6.97 GB, a
**58×** reduction in main-process footprint, and the process pegged at ~100 %
CPU doing real work instead of parked in `futex_do_wait`. The dense-generator
allocation (`7700² × 8 B × 11` per worker) is no longer the binding constraint.

**So the two failure modes are now cleanly separated**, and only one is left:

* **Memory starvation — SOLVED.** Measured, not inferred. Do not spend further
  time on it.
* **Container lifetime — OPEN, and now the whole problem.** The helium-4 leg
  needs ~45 min of wall time; this container lasted ~4 min into it. Nothing in
  the producer can fix that.

**What a fifth attempt needs** is therefore not a code change but a *host* that
survives ~45–60 min: a session that will not be restarted, or a runner outside
the ephemeral container. Relaunching inside a short-lived container is not
"trying again", it is re-running a known-failing experiment.

### A third variant of the pgrep trap, worse than the two already recorded

This bean already warns off `pgrep -c -f rho_k_co_casimir`. The trap is broader
than that phrasing: **the Bash tool wrapper embeds the full command string in
its own argv**, so *any* `pgrep -f <pattern>` matches the wrapper as well as the
target. It bit twice more in one session — `ps -p $(pgrep -f … | head -1)`
returned the **wrapper** (6 MB RSS, 0.0 % CPU, no CPU accumulation) and read as
a dead or hung job while the real compute sat next to it at 99.8 %.

Reliable forms:

    pgrep -x python3                                    # match the executable
    pgrep -af 'python3 -u computations/rho_k' | grep -v 'bash -c'
    ps -o pid=,time=,%cpu=,rss= -p <explicit pid>       # best: take the pid once, reuse it

Had the wrapper reading been trusted, this attempt would have been recorded as
another starvation failure — the exact opposite of what it shows.

### The partial-write hazard is subtler than "five atoms over six"

The cross-file above warns that a truncated witness scores zero raw floats. The
in-flight state observed here is worse than that description: the producer
**preserves the six-atom structure and rewrites atoms in place**, so mid-run the
file had *all six atoms present*, five freshly recomputed and helium-4 **stale
from the previous run**, with the raw-float count already down 4 → 1.

An atom-count check therefore **passes** on this state. Committing it would have
mixed a fresh five-atom computation with a stale helium-4 while looking complete
and nearly-drained. The reliable gate is `witness_shape_guard.py` plus a
zero-raw-float count *and* confirmation the producer exited — never the atom
count alone.


---

## ⚠ CORRECTION + claimed 2026-08-16 (`claude/anchor-followups-2026-08-08`, PR #5124)

**"The payload numbers cannot change" is wrong, and it is the load-bearing
sentence of this bean.** This is not a telemetry-only refresh. It is a
**convention C → D regeneration with real physics movement**, already measured
in [`docs/audits/2026-08-15-rho-k-co-casimir-stale-convention-c-needs-d-refresh.md`](../docs/audits/2026-08-15-rho-k-co-casimir-stale-convention-c-needs-d-refresh.md):

| atom | committed (C) | fresh run (D) |
|---|---|---|
| deuteron `\|tr_M\|` | 0.3883 | **0.5751** |
| tritium `\|tr_M\|` | 0.1041 | **0.2293** |
| deuteron `ρ_K^pred` | `9464.879…` | **`6390.441…`** |

The witness was computed 2026-08-10 on the convention-C `tr_M` table; on
2026-08-14 `canonical-mass-table-extended` rebuilt that table **C → D**. The
four raw-float64 fields are the *symptom*; the stale convention is the disease.
Anyone running this on the bean's own wording would see the physics move and
either stop, or — worse — commit it as "telemetry only".

**Why it is mine:** this is an excise-convention-C item that was filed as a
raw-float64 gate item, so it never reached the campaign. Also resolves a crossed
wire — [#5124 (comment)](https://github.com/litlfred/qou/pull/5124#issuecomment-5305295130)
and my 22:37 reply each recorded the *other* party as taking it, so nobody was.

**Run conditions.** Launched in background from this branch. `gmpy2` installed
first — the audit found mpmath was on its pure-Python backend, and
`mpmath.libmp.BACKEND` is now `gmpy`. **No explicit `--workers`**, deliberately:
passing it sets `_explicit_workers` and *disables* the `_mem_cap` clamp, so
auto-detect is the safer setting on this 14 GiB / 4-core box even though
`--workers 1` is the proven-safe one.

The five-atom-clobber hazard this bean documents is **closed** by `aa4eb8832`
(`_carry_forward`): a did-not-compute result can no longer displace a computed
one. Commit gate unchanged and unrelaxed — six atoms, zero raw floats,
`scriptHash` matching the producer, and confirmation the process exited — or the
witness gets restored and nothing is committed.
