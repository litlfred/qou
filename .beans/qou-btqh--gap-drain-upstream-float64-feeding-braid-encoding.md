---
# qou-btqh
title: 'GAP: drain upstream float64 feeding braid-encoding-audit cross-check (option_b_proton_mass_full_chain + markov-trace-assembly)'
status: todo
type: task
priority: normal
created_at: 2026-09-03T11:07:00Z
updated_at: 2026-09-03T11:07:25Z
---

Split off from qou-6sts (raw-float64 ratchet drain, 2026-09-03). The
braid-encoding-audit witness cannot reach 0 dirty float64 fields by a
producer-side fix, because 6 of its fields ECHO float64 stored upstream:

- `tr_M_cross_check.proton.phase_1_6_closed_form` and
  `.electron.phase_1_6_closed_form` read `tr_M_at_q0` from
  `option-b-proton-mass-full-chain.witness.json` — **float64 in that upstream
  witness** (producer `computations/option_b_proton_mass_full_chain.py`).
- `.markov_trace_assembly_chain` reads `target_value` from
  `markov-trace-assembly-proton.derivation.json` — likewise float64.
- `.axiomatic_content_block` (1.88432) is a hardcoded 6-sig-fig content-block
  quote consumed by an assertion.
- the two assertion metrics comparing those float64 quantities.

Fix at the SOURCE: make `option_b_proton_mass_full_chain.py` and the
markov-trace-assembly producer carry `mpmath.mpf` end-to-end and serialize with
`_precision.fmt`, then re-run braid_encoding_audit.py; the 6 residual fields
should clear to full precision. Do NOT stringify the upstream floats downstream
to fake a ratchet pass (that is the 'float64 input poisons the result' anti-pattern).
Run scripts/precision-gates.sh --changed at each producer. This is a cross-producer
change (2 upstream producers + 1 content-block quote), out of scope for the 6sts
producer-side drain.
