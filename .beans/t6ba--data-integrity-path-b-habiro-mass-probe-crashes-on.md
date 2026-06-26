---
# t6ba
title: 'Data-integrity: path_b_habiro_mass_probe crashes on A>=3 (unsubstituted check_q free symbol)'
status: todo
type: task
created_at: 2026-06-26T14:55:05Z
updated_at: 2026-06-26T14:55:05Z
---

## Problem (2026-06-26, PR #2849)

`computations/probes/path_b_habiro_mass_probe.py` (Path-3 Habiro single-trace
mass probe) **crashes on the `A>=3` rows** (tritium / ³He):

```
ValueError: could not convert string to float: '-74.0*check_q - 74.0'
  at evaluate_habiro_sum → a_m_poly.subs(u, u_val_sym).evalf(...)
```

A free symbol `check_q` survives in the stored Habiro coefficient polynomial for
the heavier atoms — it is never substituted before `mpf()` conversion. The
committed witness `path-b-habiro-mass-probe.witness.json` `{p, n, D}` rows are
clean (p −0.65%, n −0.56%, D anchor), so the regression is isolated to the
`A>=3` coefficient path.

## Task

Trace where `check_q` enters the `a_m` polynomial for `A>=3` (likely an
un-substituted substrate symbol in the Hoefsmit/coefficient builder), substitute
it (or fix the symbol plumbing), and re-emit the witness with clean T/³He rows.
Confirm the sub-1% binding claim holds (or doesn't) at `A=3` under the
single-prefactor `α_M` model.

## Refs

- Synthesis doc: `docs/audits/2026-06-26-t2t3-trace-invariance-status-synthesis.md` §"Item 3"
- Producer: `computations/probes/path_b_habiro_mass_probe.py`
- Witness: `computations/probes/path-b-habiro-mass-probe.witness.json`
