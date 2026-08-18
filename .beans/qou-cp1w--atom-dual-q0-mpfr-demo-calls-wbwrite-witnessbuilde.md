---
# qou-cp1w
title: atom_dual_q0_mpfr_demo calls wb.write(); WitnessBuilder only has save() — never emitted a witness
status: todo
type: task
priority: normal
created_at: 2026-08-18T16:24:41Z
updated_at: 2026-08-18T20:39:34Z
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


---

## CORRECTION — there is nothing to decide, and the one-line fix is not a fix

I wrote above that the fix "creates a new committed witness whose contents want
their own review". I had not looked at what those contents would be. They are
**all None**:

    feasible = None   y0_star = None   primal_obj = None
    dual_obj = None   duality_gap = None
    inputs are 50-dps strings (no float64): None

`solve_atom_dual_q0_mpfr()` returns an empty result because the
`clarabel-operator-selection-lp` MPFR backend is not built in this sandbox, and
the script prints its "NO-FLOAT64 path (50-dps strings -> clarabel-MPFR)"
banner regardless.

**So `wb.write()` -> `wb.save()` does NOT make this emit a witness.** Two lines
later:

    wb.add_assertion("strong_duality_gap_small",
                     computed=abs(float(res.get("duality_gap", 1))), ...)

`duality_gap` is present with value `None`, so `float(None)` raises TypeError —
caught by the same broad `except Exception` that was swallowing the `write`
AttributeError. Fixing the API typo just swaps one silently-swallowed exception
for another.

**The actual defect is the swallowing**, not the typo. Every call in that block
is guarded (`if hasattr(wb, "set_description")`, `if hasattr(wb, "add_data")`,
…) and the whole thing sits in a bare `except Exception` that prints and
continues. That is why a method name that never existed survived: nothing could
fail loudly. A demo whose backend is absent should say so, not print a
NO-FLOAT64 banner over a table of Nones and exit 0.

**Revised scope** (still not done here, but now for a stated reason rather than
a deferred judgement call):

  1. Make the missing backend an explicit, loud skip — detect it before the
     banner and say "MPFR backend unavailable; not run", exit non-zero or emit
     nothing deliberately.
  2. Narrow the `except Exception` so a genuine emission bug surfaces.
  3. Only then fix `write` -> `save`, and only where `res` is populated —
     i.e. in an environment that has the backend built.

Ordering matters: doing (3) first in an environment without the backend commits
an all-None witness asserting `strong_duality_gap_small`, which is worse than
emitting nothing.
