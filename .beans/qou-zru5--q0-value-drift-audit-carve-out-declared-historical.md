---
# qou-zru5
title: 'q0_value_drift_audit: carve out DECLARED historical pins, and exempt retired witnesses from the NEW check'
status: in-progress
type: task
priority: high
created_at: 2026-09-14T07:59:16Z
updated_at: 2026-09-14T07:59:16Z
---

`q0_value_drift_audit` is RED on 4 NEW findings and all four are false positives, but
BOTH obvious remedies delete the gate. Measured 2026-09-14 (queue §27):

    _deprecated/alpha-high-precision.witness.json       q_0                        -0.0769 ppb
    probes/…_D_eigenvalue_no_pin_produces_probe         data.D_spectrum_at_retired.q0   -0.0798
    probes/two_blocks_publish…at_different_pins_probe   data.figures_at_retired.q0      -0.0798
    probes/two_blocks_publish…at_different_pins_probe   data.figures_at_frozen_A.q0     -0.0769

Each value matches the pins probe's own `PINS` dict exactly — `retired`, `retired`,
`frozen_A`, `frozen_A`. That probe's entire subject is evaluating one identity at
several pins and reporting their separation, so the pins ARE the measurement.

## Why the easy fixes are wrong, with numbers

**Add `retired`/`frozen_A` to the anchor set.** 201 of the 206 STALE rows sit at the
pre-ruling anchor A (-0.077..-0.080 ppb), so this reclassifies 98% of the gate's
content. It would not drain the backlog, it would delete it.

**Exclude `_deprecated/`.** This is the only one of six family gates with no
`_deprecated` handling, so it looks like a consistency fix. But 179 of the 329
BASELINED stale keys (54%) are in `_deprecated/` — the audit's convention is that
they are scanned and baselined, and removing them rewrites the accounting.

Both are drain-by-exclusion.

## The two fixes that are not

1. **A CHECKED per-field declaration.** A producer says which historical pin a field
   records; the audit resolves that pin and VERIFIES the value matches before
   carving it out. Unlike `precision_tier: float64-integrator` (a bare assertion),
   a declaration that names a pin cannot launder an arbitrary value — declare
   `retired` on something that is not the retired pin and it still reports.
2. **Exempt `_deprecated/` from the NEW check only, never from the census.** A
   retired witness cannot regress because nobody re-runs it; a NEW finding there is
   always the anchor moving under a frozen file, not someone's change. Counts and
   baseline stay exactly as they are, so no drain.

## Interaction with qou-fd0e (do not conflate)

`qou-fd0e` argues the gate's zero point is inverted — `Q_CANONICAL = _resolved("muon")`
while the 2026-08-15 ruling made the proton pin canonical. That is an owner-ruling
question, still live in the source, and NOT this bean. Both fixes here hold under
either polarity: a deliberately recorded historical pin should be carved out however
the zero point is chosen.

## Also observed, not fixed

Collects with `HERE.rglob("*.witness.json")` where all five sibling gates use
`git ls-files`, so an untracked witness in a working tree can change a blocking
gate's verdict.
