---
# qou-odkf
title: 'ctype coverage guard is RED on main: 3 new family-blind sites, 3 stale baselines, and InterfaceKind cannot express the weighted family at all'
status: todo
type: bug
priority: normal
created_at: 2026-08-19T21:03:40Z
updated_at: 2026-08-19T21:04:44Z
---

Measured on origin/main 5b158ef06c, 2026-08-19.
`python3 computations/test_ctype_consumer_coverage.py` FAILS (3), with 3 stale
baseline entries alongside.

    FAIL (3):
      _habiro_coefficient_extract.py:171
      closed_form_tau_M.py:238
      closed_form_tau_M.py:502
    note: baseline entries no longer needed (line numbers moved):
      closed_form_tau_M.py:181, _habiro_coefficient_extract.py:166,
      closed_form_tau_M.py:445

Parts A/A2/B/C/D all pass; the deuteron word still reports
`{averaged: 4, averaged_weighted: 1, sigma: 11, sigma_inv: 7}`, so the
canonical builder is intact. This is Part E only.

## The three are NOT one defect — the guard cannot tell them apart

    computations/closed_form_tau_M.py:136
      InterfaceKind = Literal["positive", "negative", "averaged"]

There is a SECOND ctype vocabulary in the corpus, three-valued, which
structurally cannot express `averaged_weighted`. Its docstring is explicit and
honest about it:

  "For LABEL purposes returned here, the p-n kind is `averaged` (same as
   strict_averaged); the delta-aware factor is applied at the value-computation
   layer, not in the labels."

Against that design the three sites split three ways:

1. `closed_form_tau_M.py:238` (`interface_factor`) — the documented design.
   The label layer is deliberately colour-blind and delta is applied downstream.
   Not a defect PROVIDED the value layer really applies delta. VERIFY that, then
   baseline the site with the reason recorded, not silently.

2. `closed_form_tau_M.py:502` (`interface_kind_counts`) — reporting fidelity.
   It reports a single `averaged` count, collapsing weighted and unweighted into
   one number. Same shape as the `type_breakdown: {"averaged": 5}` defect fixed
   in `build_atomic_braid_recipe_d_chain.py` (PR #5029), which was also "only a
   label" until it was the thing a reader trusted.

3. `_habiro_coefficient_extract.py:171` — the one that may be real. It calls
   `canonical_interface_kinds(..., pn_convention="chi_lambda_braid")` and then
   BUILDS THE VALUE from the labels: `expr = expr * (z - h/2)` for `averaged`.
   There is no downstream delta layer on that path, so the label collapse is the
   value collapse. Whether that is wrong depends on whether `chi_lambda_braid`
   is the intended convention there; under `bring_color_weighted` it is not.

## What this says about the guard

Part E greps for a literal equality against `'averaged'`. That finds the shape
and cannot see the intent, so it fires identically on a documented two-layer
design and on a genuine value collapse. It also keys its baseline on FILE:LINE,
which is why three entries went stale on an unrelated edit.

Two changes worth making, in order:
  - baseline by enclosing function name rather than line number;
  - require a reason string per baseline entry, so a suppressed site records
    WHY it is colour-blind. A silent baseline is how site 1 and site 3 come to
    look the same.

## Next step

Resolve site 3 first — it is the only one that can move a number. Sites 1 and 2
are a docs/reporting fix and a guard-ergonomics fix respectively.
