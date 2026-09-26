---
# qou-bvk7
title: Convention-C derived TRACE VALUES in live witnesses — invisible to both convention-C witness detectors
status: todo
type: task
created_at: 2026-08-16T12:49:41Z
updated_at: 2026-08-16T12:49:41Z
---

Parent: qou-cdx1. Surfaced while resolving qou-uabo; distinct from qou-pvem,
which is about the STRUCTURAL population (3+-row y_lambda, float64-noise
sub-class).

## The gap

`scripts/convention-c-witness-audit.py` has two tests:

  structural  a nonzero `y_lambda` on a 3-or-more-row partition
  symbolic    a half-integer power of q in a weight EXPRESSION

Both key on **weights**. Neither can see a witness that records a **derived
trace value** computed under convention C — `tr_M` is a number, with no
partition structure and no surviving square root.

## What turned it up

`qou-uabo`'s resolution cites `term6-full-pole-sum.witness.json` as "the
canonical one". It carries

    .data.atoms[2].tr_M_at_q0_polynomial = 0.3882864240747888
    .data.atoms[2].tr_M_polynomial.value_at_q0 = 0.38828642407478884856154551860407

`0.3883` is the **convention-C** deuteron `|tr_M|`; under D the same quantity is
`0.5751` (measured — docs/audits/2026-08-15-rho-k-co-casimir-stale-convention-c-
needs-d-refresh.md). The witness audit does **not** flag this file.

That caveat was written 2026-05-03, three months before the 2026-08-09 ruling, so
"canonical" there meant "canonical Markov trace as opposed to Schur-Weyl
weighted" — a distinction orthogonal to C-vs-D. It has since been read as
convention-canonical, which it never was.

## Measured, and DELIBERATELY NOT YET A COUNT

`grep -rl "0\.38828642" --include=*.witness.json` outside `_deprecated/` returns
**14 files**. That is a text match, not a verdict, and this campaign has three
published counts today that were wrong for exactly that reason. **Three sampled:**

| witness | field | reading |
|---|---|---|
| `deuteron-real-sdp` | `.data.tr_M_beta_D` | genuinely the deuteron trace |
| `applied-uniqueness-mass-table` | `.data.canonical_tr_M_q0_values.deuteron`, `.data.rows[2].tr_M_q0` | genuinely the trace — and **named `canonical`** |
| `cal4-disguise-hunt` | `.data.findings[33].value` | ambiguous; a hunt hit may legitimately quote a C value |

So the class is real and at least two live witnesses carry a convention-C trace
value, one asserting canonicity in its own field name. **The other eleven need
per-file reading before any number is published.**

## Why it matters more than the count

A block quoting `0.3883` and declaring one of these witnesses would pass the
witness-substitution axis (the value IS in the declared witness), pass the
convention-C witness audit (no 3-row weight, no sqrt), and pass R9/R10/R11 (those
read producers, not artifacts). Four gates, none of which can see it.

## Suggested approach

Do NOT add `0.38828642` as a fingerprint — that is the decimal-fingerprint
strategy this campaign already retired for being only as complete as someone's
memory. The general form is: a witness recording a `tr_M`-named field whose value
matches the C evaluation of that quantity at q0 and not the D one. That is
checkable against `closed_form_tau_M` without a list, the same way
`convention-c-producer-audit` moved from grep to AST.
