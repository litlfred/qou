---
# qou-ns02
title: 'Witness integrity: 1 unparseable, 1 non-object root, 2 anchor-without-value'
status: todo
type: task
created_at: 2026-08-19T20:54:16Z
updated_at: 2026-08-19T20:54:16Z
---


## Found by

`q0_anchor_consistency_audit` on a clean tree, 2026-08-19, while checking
the arc's other work. Four items, all small, all in the
witness-provenance lane:

| item | file | what |
|---|---|---|
| `Q0_PARSE_ERROR` | `computations/_deprecated/qbeta-gb-filtration-residues.witness.json` | malformed JSON — `Expecting value: line 28 column 22`. Under `_deprecated/`, so low priority, but it is the only unparseable witness in the corpus. |
| root not an object | `computations/iterative-knot-builder.witness.json` | **not** deprecated. Every audit that does `body.get(...)` skips it silently. |
| `Q0_VALUE_MISSING` | `computations/atomic-tr-m-mpfr-50dps.witness.json` | declares an anchor with no `q0Value` to check it against |
| `Q0_VALUE_MISSING` | `computations/atomic-tr-m-mpfr-50dps-proton.witness.json` | same |

## Why it is worth doing rather than ignoring

None of these is a wrong number. They are witnesses that **no checker can
read**, which is the same failure shape as the arc's other findings: an
artifact that is skipped reports as clean. The `iterative-knot-builder`
one is the live case — a non-object root means every `q0`, precision and
staleness audit passes over it without a verdict.

The two `atomic-tr-m-mpfr-50dps` pair are more interesting than the count
suggests: one is muon-named and one proton-named, so they are a
deliberate two-layer comparison, and neither records the value it used.
That is exactly the layer-straddle case AGENTS.md warns about, in the one
place it would be hardest to detect by eye.

## Scope

Small. Each is a producer re-run or a one-field fix, except the malformed
JSON, which needs its producer identified first — it may be an
interrupted write rather than a code defect.
