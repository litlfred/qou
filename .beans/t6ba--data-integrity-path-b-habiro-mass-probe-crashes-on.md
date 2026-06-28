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

## Progress 2026-06-28 (branch claude/ct80-me-codata-dedup-2026-06-28)

**FIXED** (commit e40c0d2a8a): root cause was a bare
`sp.sympify(entry["a_m"])` / `sp.sympify(denom_str)` in
`evaluate_habiro_sum` — missing the universal `locals={"check_q": u}`
binding that every other consumer of these strings uses. `check_q` is
the coefficient builder's name for the u = q^{1/2} variable; unbound, it
survived `.subs(u, …)` as a free symbol and crashed the `mp.mpf(str())`
cast. Added the binding to both the a_m and denom sympify calls.

Verified: probe no longer crashes; p/n rows compute and agree with the
witness-stored tr_M (✓).

**Observation for follow-up (NOT t6ba):** the input witness
`habiro/habiro-coefficients-atomic.witness.json` has changed since this
bean was filed — it now contains ONLY the p/n entries (both carrying
`check_q`), so the crash now fires on p, not on the A>=3 rows the bean
described. The heavier atoms (D/T/³He) are absent from the input, so the
probe's "sub-1% binding at A=3" check can't run until the input witness
is re-populated with D/T/³He. That re-population is a separate upstream
concern (a sibling regenerated the input witness). Output witness
`path-b-habiro-mass-probe.witness.json` NOT re-emitted here (ad-hoc-env
skew + would lose the D row); canonical CI re-emits.
