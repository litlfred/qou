---
# qou-5mao
title: 'pentagon_rt_torus_knot_higgs_probe: 389 raw float64 fields block its witness'
status: todo
type: task
created_at: 2026-08-24T05:06:00Z
updated_at: 2026-08-24T05:06:00Z
---


## Why this exists

`pentagon_rt_torus_knot_higgs_probe.py` crashed before `json.dump` for as long
as the corpus has had it — so **no witness for it has ever been committed**. The
crash is now fixed (`TypeError: unsupported format string passed to
mpf.__format__`, then a second one at the serializer), and the producer exits 0.

**Its witness is still withheld deliberately.** Running it emits **389 raw
float64 fields**, which the raw-float64 ratchet flags as `NEW dirty 1`. Per
AGENTS.md that must be fixed at the producer — never by baselining the file.

## The work

The producer `float()`s at construction throughout, not just at display:

    line 137-141   float(q.real), float(q.imag), float(j.real), float(j.imag), float(magnitude)
    line 157-158   float(mag * M_E_MEV), float(log_mag * M_E_MEV)
    line ~229      ratio = val / float(M_HIGGS_MEV)      <- a COMPUTATION, not display

That last one is the class AGENTS.md names explicitly: *"`hf = float(G.h)`
followed by arithmetic against it is a computation, not a display, and is a
defect."* Carry `mpf` end to end and let the `_fmt_deep` helper (added in the
crash fix, already at the write boundary) do the conversion at OUTPUT_DPS.

## Scope note — why this is not part of the crash fix

Two different jobs. Making the producer *run* is a 3-line print fix plus a
boundary serializer. De-float64-ing it is a numerical-discipline pass over ~20
sites that changes what the numbers are carried as. Bundling them would have
either shipped 389 float64 fields into the corpus or turned a crash fix into an
unreviewable numerics change.

Once drained, commit the witness — it will be that producer's first.
