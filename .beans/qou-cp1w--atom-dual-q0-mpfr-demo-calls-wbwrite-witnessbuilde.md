---
# qou-cp1w
title: atom_dual_q0_mpfr_demo calls wb.write(); WitnessBuilder only has save() — never emitted a witness
status: todo
type: task
priority: normal
created_at: 2026-08-18T16:24:41Z
updated_at: 2026-08-18T16:27:53Z
---

## Evidence (PR #5260)

`computations/atom_dual_q0_mpfr_demo.py:101`

    out_path = wb.write("atom-dual-q0-mpfr-demo")

`WitnessBuilder` exposes `save(extra=None)` and **has never had a `write`
method** — `git log -S"def write"` on
`tools/qou-substrate/python/qou_substrate/witness.py` returns nothing. The
script exits 0 because the call is inside a try/except that prints

    (witness emission skipped: 'WitnessBuilder' object has no attribute 'write')

and continues. So it has never emitted `atom-dual-q0-mpfr-demo.witness.json`,
and no such file is committed.

**Why it matters beyond one broken demo.** This script is the *only* consumer
of `gram_matrix_mp_strings` / `tr_m_mp_strings`, and its own header says it
exists "closing the `gram_matrix_mp has no consumer` gap". The gap is not
closed: the sole consumer is inert. That is a live reason the mp path's
convention-C drift (bean qou-h4ab) went unnoticed for days — nothing exercised
it end-to-end and nothing committed an artifact that would have diffed.

**Fix** is one line (`wb.write(name)` -> `wb.save()`, with the name moved to the
`WitnessBuilder(...)` constructor), but it creates a **new committed witness**
that has never existed. Deliberately not done on #5260: that is a scope
expansion, and the new artifact's contents want their own review — the demo's
own output says "Degenerate H_3 dual (y0~0); pipeline demo", so what it would
assert needs deciding before it is committed, not after.
