---
# qou-9br4
title: 'GAP: rho-k-co-casimir-extended witness is stale on main — needs a ~45min re-run'
status: todo
type: task
priority: normal
created_at: 2026-08-15T20:24:06Z
updated_at: 2026-08-15T20:24:42Z
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
