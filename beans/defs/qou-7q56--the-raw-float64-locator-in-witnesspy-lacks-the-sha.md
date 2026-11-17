---
# qou-7q56
title: the raw-float64 LOCATOR in witness.py lacks the shadow rule its own GATE has -- it now cries wolf on a correctly-drained witness
status: in-progress
pr: 8290
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T23:35:32Z
updated_at: 2026-11-17T08:47:00Z
parent: qou-9nnz
---

Found 2026-08-15 while draining `canonical-mass-table-extended` under `qou-xwet`.

## Two implementations of one rule, and they disagree

The same witness, measured two ways:

| checker | says |
|---|---|
| `witness_raw_float64_audit.count_raw_floats` (the GATE) | **0** raw float64 |
| `qou_substrate.witness._raw_float_paths` (the LOCATOR) | **33** raw float64 |

The gate is right. `canonical_mass_table_extended.py` now emits every numeric
column as a float PLUS a full-precision `_str` companion at OUTPUT_DPS=60, which
is exactly the shadow rule `qou-ftuv` established: an f64 beside a `_str`
carrying >17 significant digits is a shadow, not a defect. The ratchet reports
`24 -> 0` for the file.

`_raw_float_paths` (`tools/qou-substrate/python/qou_substrate/witness.py:505`)
yields EVERY float unconditionally. It implements none of the three exemptions
the gate does: no shadow rule, no `LP_DUAL_F64_FIELDS` carve-out, no
`float64-integrator` tier.

## Why this is worth fixing rather than tolerating

`_check_raw_float64`'s own docstring draws the division deliberately — *"The
audit gate is what ENFORCES ... this is what LOCATES"* — so a locator being
broader than a gate is defensible in principle. It is not defensible here:

1. **It now fires on a clean file, every run.** Any producer that adopts the
   shadow rule earns a permanent 33-path warning. That is the classic path to
   agents learning to scroll past `⚠`.
2. **Its remedy text is actively wrong for the shadowed case.** It says *"do NOT
   stringify the float"* — but emitting the `_str` companion is precisely the
   sanctioned fix. An agent who obeys the warning will undo a correct drain.
3. **`QOU_WITNESS_STRICT_FLOAT64=1` turns the disagreement into a hard failure.**
   The docstring recommends that mode *"in CI and when draining"* — i.e. exactly
   when someone is doing the right thing. A correctly-drained producer raises.

## The fix, and the reason I did not just make it

Teach `_raw_float_paths` the same three exemptions. The obstacle is that the
authoritative implementation lives in `computations/witness_raw_float64_audit.py`
while the locator is in the `qou-substrate` package, so the package cannot import
it without an upside-down dependency. Copy-pasting the predicate creates two
copies of a rule that already exists twice — which is the present bug.

Options, in the order I would try them:
  1. Move `_is_full_precision_shadow` / `_sig_digits` / the carve-out constants
     INTO `qou_substrate` (they are witness-format concerns, and the package is
     where witness format lives), and have the audit import them. One home.
  2. Failing that, have the locator's message say what it cannot see — e.g.
     "N raw float64 (shadow rule NOT applied; confirm against
     witness_raw_float64_audit before acting)" — so the wrong remedy stops being
     the headline.

Not done in PR #5165: `qou_substrate` has 309 in-repo importers and this is a
shared-package refactor, not a rider on a mass-table fix. Option 2 alone is small
enough to be safe if option 1 stalls.

## Progress 2026-11-17 (PR #8290)

Implemented the full-precision `*_str` shadow rule, `LP_DUAL_F64_FIELDS` carve-out, `_EPHEMERAL_META_FIELDS` timing carve-out, `float64-integrator` / deprecated `float64` tier carve-outs, and exact integral float handling in `qou_substrate.witness._raw_float_paths` (with unit tests in `tools/qou-substrate/tests/test_declared_tolerance_literal.py`) on PR #8290 (`1c907342f24ac048c99eb24f30832b0b87b024b0`).
