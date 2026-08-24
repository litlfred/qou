---
# qou-5mao
title: 'pentagon_rt_torus_knot_higgs_probe: 389 raw float64 fields block its witness'
status: completed
type: task
priority: normal
created_at: 2026-08-24T05:06:00Z
updated_at: 2026-08-24T10:47:15Z
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

## 2026-08-24 — drained, 389 → 0, and the witness lands

Done in `a3d8448ba25`. Counted by walking the JSON: **389 → 0** raw float64.
`precision-gates.sh --changed` exits 0, all blocking gates green, raw-float64
ratchet **NEW 0 / REGRESSED 0** — it was `NEW dirty 1`.

Three classes, worth separating because only one of them is what this bean was
opened for:

1. **Witness payload** — `float()` at construction dropped; values carry `mpf`
   and `_fmt_deep` serializes at the write boundary.
2. **Arithmetic** — `ratio = val / float(M_HIGGS_MEV)`, the line AGENTS.md
   names when it says a probe's float64 corrupts *analysis* rather than a
   stored number. It drives the "within 2× of the Higgs" verdict.
3. **Laundering** — `float(mpf(str(val)) / M_HIGGS_MEV)` where `val` was
   *already* `float()`. The `str()` round-trip recovers no precision; it only
   makes the division look exact. Two more `mpf(str(x))` round-trips in the
   best-candidate comparison.

**Conclusion unchanged**: best candidate is still N=7, `(|J_N|·N²)·m_e`, ratio
0.6266838. So the float64 was not distorting *this* verdict — but that could
only be known after draining it, which is the point.

### Two things found by doing it

**The branch's own defect class reproduced itself.** Making the values exact
immediately killed five untouched f-strings formatting a now-`mpf`
`J_N_magnitude` (`TypeError: unsupported format string passed to
mpf.__format__`) — the exact mechanism `qou-geqa` documents, hit from the other
side.

**A comment I wrote on this branch was false.** It claimed `val` and `ratio`
"stay mpf everywhere they are computed with"; `val` arrived as `float()` and
`ratio` was float/float. Corrected in place rather than deleted.

### Anchor stamped (not in the original scope)

`Q0_ANCHOR_MISSING` moved **1880 → 1881** the moment this witness first
existed. The producer hand-builds its dict instead of using `WitnessBuilder`,
so nothing stamped an anchor — and because it had never written a witness, the
omission had never been *observable*. Now carries `q0Anchor: "proton"` +
`q0Value` per AGENTS.md §4. `Q_50_DIGIT_STR` is the proton pin
(`1.1099785827513808…`); the muon pin agrees to 8 digits, so the two are
distinguishable only past the 9th and must never be told apart by eye.
