---
# qou-s7g0
title: 'GAP: lambda_scale_homflypt_skein_recursion_probe imports a module that does not exist'
status: completed
type: task
priority: normal
created_at: 2026-08-28T15:43:19Z
updated_at: 2026-08-30T17:27:33Z
parent: qou-a1lw
---

computations/probes/lambda_scale_homflypt_skein_recursion_probe.py fails with ModuleNotFoundError: No module named 'lambda_scale_alt_g_skein_polynomial_direct'. Verified: that module exists NOWHERE in the tree; the only occurrences of the name are three docstring mentions inside the failing file itself, describing it as the 'Strategy G predecessor'. Either it was deleted or it was never committed. Its witness carries the OLD-MUON value B and cannot be drained until this is resolved. Found by the B-population sweep, PR #5889.


## 2026-08-30 — CLOSED. Rebuilt from in-repo compute; the muon-B witness drained

`homflypt_borromean_at_az` now lives in `computations/homflypt_engine.py`
(`b4e2be5517`) and the probe imports it from there.

**Derived, not transcribed.** `homflypt_from_braid` refuses `n_strands >= 3` by
design and names its own replacement in the refusal message, so the new function
delegates to `homfly_skein_braid.homfly([1,-2,1,-2,1,-2], 3)`:

    P = v^-2 z^-2 - v^-2 z^2 - 2 z^-2 + 2 z^2 + z^4 + v^2 z^-2 - v^2 z^2

**Convention measured, not assumed.** The engine is in `(v, z)`, the caller asks
for `(a, z)`, and `a = 1/v` is the other live convention. Calibrated against the
probe's OWN inline trefoil `2a^2 - a^4 + a^2 z^2`: the skein route returns
`{(2,0):2, (2,2):1, (4,0):-1}`, identical term-for-term under **a = v**, and
numerically `-2.218075` vs `0.6146987` at `(1.7, 0.35)` separates them.

**Independent check.** The Borromean rings are amphichiral ⇒ `P(v,z) = P(1/v,z)`.
The result satisfies it exactly (`coeff(i,j) == coeff(-i,j)` every term) and
numerically to 18 digits. A wrong braid word or variable map would not be
symmetric — this is a check on the answer, not a restatement of how it was built.

**The drain this bean was blocking:**

    committed  1.1099785955541805752815940796095   muon pin B (CODATA 2018)
    fresh      1.1099785827513808075916690956108   proton, q0Anchor: proton

Verdict unchanged — both PSLQ searches still find no informative relation, which
is the confirmatory negative the probe exists to record.

**Bonus defect, and a general lesson.** The first successful run warned that 2
raw float64 fields would enter the witness (`computed=float(not any_relation)`).
Fixed at the producer, not baselined. **An unrunnable producer hides its
precision defects along with everything else** — this one was invisible to the
NO-FLOAT64 ratchet for as long as it could not execute, so the runnability
backlog and the precision backlog overlap more than either audit reports.
