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
