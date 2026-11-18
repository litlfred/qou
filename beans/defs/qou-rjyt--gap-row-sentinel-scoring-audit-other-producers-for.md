---
# qou-rjyt
title: 'GAP-row sentinel scoring: audit other producers for the 0.0-means-no-prediction pattern'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-19T13:31:33Z
updated_at: 2026-10-04T15:19:35Z
parent: qou-5vkl
---

Found in `mass_table_ppb.py` (fixed, commit 863a5aee91): rows with no
prediction were assigned `err_pct = err_ppb = 0.0` instead of `None`,
and the accuracy counters then scored that sentinel. Every one of the
six atoms it reported "within 1 ppb" was a GAP row; the true count of
predictions within 1 ppb is zero. `mean |err|` was diluted 6/16, from
6.7996% down to 4.2497%.

The pattern is generic and cheap to grep for: a float-zero default on a
quantity that is *undefined* rather than zero, feeding a threshold
counter or a mean. Two signatures to look for across `computations/`:

  * `... if <cond> else 0.0` on an error / residual / ppb quantity
  * a summary loop over ALL rows rather than the scored subset
    (`ok = rows` was literally the line here)

Worth a sweep because the same shape also plants raw float64 in the
witness -- which is how this one surfaced. Anything the raw-float64
audit reports as a bare `0.0` in an error column is a candidate.

NOT yet checked: `binding_link_volumes.py`, `magic_A_formula.py`,
`per_atom_rho_deviation.py`, `canonical_mass_table_extended.py`, and the
`sweeps/` producers all carry err_pct-style columns.
