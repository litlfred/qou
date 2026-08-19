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

## RESOLVED 2026-08-19 — site 3 is a FALSE POSITIVE of my own grep

My triage above ranked `_habiro_coefficient_extract.py:171` as *"the one that can
move a number"*. Measured, it cannot — not on that line.

The module calls `canonical_interface_kinds(Z, N, pn_convention="chi_lambda_braid")`,
and under that convention the p-n boundary is labelled **`positive`**, not
`averaged`:

    bring_color_weighted  Z=1 N=1 -> {averaged: 1}
    chi_lambda_braid      Z=1 N=1 -> {positive: 1}
    strict_averaged       Z=1 N=1 -> {averaged: 1}

So the `averaged` branch at :171 never sees a p-n bond in this module's own call
path. Part E fired on a literal it found; the label it should have been looking
for was `positive`.

**This makes the guard's blind spot worse, not better.** A colour-blind
collapse that keeps the word `averaged` is visible to Part E. One that renames
the p-n bond to `positive` is not — and that is the larger of the two defects:
`chi_lambda_braid` is **-17.05%** off canonical per p-n bond, against **+0.0141%**
for `strict_averaged` (measured, `qou-cds4`). Part E is tuned to catch the 0.014%
family and blind to the 17% one.

### Where the real work lives

Not here. The corpus-grep found it already ruled and already scoped: owner ruling
R3 (`docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md`) makes
`bring_color_weighted` canonical, and its §3.5 / tranche **S4** names
`_habiro_coefficient_extract.py` explicitly among the six files that *"need
reading"*. Bean **`qou-cds4`** owns it; I have claimed it and added the magnitude,
which the tranche did not have.

### What remains in THIS bean

Sites 1 and 2 stand as written, and one new item replaces site 3:

1. `closed_form_tau_M.py:238` — documented design. Verify the value layer applies
   delta, then baseline **with the reason recorded**.
2. `closed_form_tau_M.py:502` — reporting fidelity, one collapsed `averaged` count.
3. **NEW — Part E must key on the family, not the string.** It cannot see a
   collapse that relabels rather than merges. Detecting `chi_lambda_braid`-shaped
   loss needs the check to ask *which convention did this call site request*,
   which is an AST question about the `pn_convention` kwarg, not a grep for a
   literal.

Plus the two ergonomics fixes already noted: baseline by enclosing function name
rather than `file:line` (3 entries went stale on an unrelated edit), and require a
reason string per baseline entry.
