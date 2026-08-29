---
# qou-rq9n
title: Five q-NS conjecture carriers carry a FABRICATED trivial-zero instance
status: todo
type: milestone
priority: normal
created_at: 2026-08-29T19:45:34Z
updated_at: 2026-08-29T19:45:34Z
---

`lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean` declares five `Prop`
carriers named after open fluid-dynamics problems and supplies an
**unconditional global instance for each**, discharging every one with zero:

    instance ns_counterexample_canonical : NSCounterexample where
      exists_singularity_time := fun _ _ => <0, le_refl 0>

The file introduces the block as the "canonical instance bundle ... via the
trivial-zero discharger", so this is a recorded design decision, not a slip.
The defect is what it does downstream.

## Why this is the exact shape the `cj*` beans exist to prevent

The 23 `cj*` beans each say: *"The sorry IS the conjecture (per AGENTS.md
3b) -- do NOT fabricate an instance (audit-dodge)."* These five ALREADY HAVE
the fabricated instance. Not one of the 23 names any of them.

## Measured on main, 2026-08-29

- File UNTOUCHED since 2026-08-24 (`git log --since` returns nothing).
- Bound as `[C]` hypotheses in **5 / 5 / 5 / 4 / 5** files respectively.
- `lean-vacuity-review-ledger.json`: **0 entries** for any of the five, and
  0 for `PvsNPQou`. The ledger is not out of scope here -- it covers 187
  files, **144 of them under `/lean/QOU/`**. In scope and missed.
- My `vacuous-prop-carrier-probe.py --check` ratchet: exit 0, all 23
  self-contained carriers in baseline, these five among them.

## Why no shipped criterion fires

AGENTS.md 3b-tax cites THIS FILE as the exemplar of doing it right --
"parameter-quantified inequality in the *shape* of the claim". That is
accurate. The shape is right and the content is absent, and nothing tests
the difference: fields are not `True`, nothing projects them, no `sorry`,
docstring property-count matches field-count. See
docs/audits/2026-08-24-shape-of-claim-is-not-content.md.

## Disposition -- AUTHORIAL, do not "fix" mechanically

Demoting the instances alone leaves carriers that still assert nothing. The
fix is to encode what the q-Aubin-Lions compactness claim, the blow-up rate
bound and the critical exponent actually say. That is mathematics.

Children: one per carrier.
