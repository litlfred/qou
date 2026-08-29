---
# qou-1jny
title: convention-C detector counts a deliberate C-vs-D switch as actionable (he4_body_order probe)
status: todo
type: task
priority: normal
created_at: 2026-08-29T16:35:51Z
updated_at: 2026-08-29T16:36:16Z
---

## What this is

`scripts/convention-c-producer-audit.py` classifies the Markov-parameter
binding at `computations/probes/he4_body_order_shortfall_location_probe.py:102`
as ACTIONABLE, in the "probes / exploratory" bucket. Measured on main
2026-08-29 it is not a defect: the enclosing function takes a `convention`
parameter and branches,

    if convention == "D": return markov_z(q)          # q**3 / (q**2 + 1)
    if convention == "C": return mp.sqrt(q) / (q + 1)

i.e. it is a deliberate C-vs-D comparison helper, the same class the audit
already recognises in its 63-site "deliberately C-named — labelled
comparisons, not defects" bucket. The docstring says the difference is
"never wired".

## Why it matters (small, but it is the count everyone quotes)

ACTIONABLE is the number the convention-C drain arc reports as remaining
work. It reads 9 on main today. One of those 9 is this false positive, and
7 of the rest are registry-blocked on `qou-cds1`. So the count overstates
the drainable surface by more than it looks: the genuinely drainable
figure is ~0-1, not 9.

## Fix

Register the site in the audit's deliberate-comparison registry (the same
mechanism `qou-ze9n` used for `markov_reduction_h3_to_h4_verify`, landed in
PR #5754), so it moves out of ACTIONABLE and into the labelled-comparison
bucket. Do NOT edit the probe — the C branch is load-bearing for the
comparison it exists to make.

## Caution

Verify by RUNNING the audit, not by reading it. This detector has a
documented history of blind spots in both directions
(`docs/audits/2026-08-15-detector-blindness-taxonomy.md`, thirteen
spellings), and the file already carries one entry annotated
"[detector false positive -- MEASURED, not argued]" for a different site
in the same probe family.
