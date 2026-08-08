---
# qou-h03q
title: 'AUTHOR CALL: strangelet binding-component sign convention (8/q > 6/q drops the minus)'
status: todo
type: task
created_at: 2026-08-08T13:48:24Z
updated_at: 2026-08-08T13:48:24Z
---

`content/quantum-observable-universe/observations/strangelet-crossing-energy.md`
claim 3 writes the per-baryon binding component as

    E_bind(uds) = 8 q^-1  >  6 q^-1 = E_bind(udd)

`def:crossing-energy` assigns a negative crossing the weight `-q^-1`, so 8
negative crossings contribute `-8 q^-1`, and the ordering by *signed* energy is
`-8 q^-1 < -6 q^-1`. The block's magnitude comparison reaches the correct
physical conclusion (strange matter is more strongly bound), so this is a
presentation/convention question, not an error — which is why it was left
untouched during the decomposition-correction sweep.

Two things for the author to settle: (a) whether a "binding component" is
defined as the magnitude or as the signed contribution, and (b) whether claim 3
should mention `n+` at all, since it currently compares only negative-crossing
counts while claim 2 (as corrected) has `n+ = n-`.

The Lean fields `uds_binding` / `udd_binding` encode the positive-magnitude form
`8 * q^-1` and would follow whichever convention is chosen.

Surfaced by `docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md`.
