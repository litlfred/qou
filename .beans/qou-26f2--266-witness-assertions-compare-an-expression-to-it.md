---
# qou-26f2
title: 266 witness assertions compare an expression to itself and pass by construction
status: todo
type: task
created_at: 2026-08-24T23:58:15Z
updated_at: 2026-08-24T23:58:15Z
---


Found 2026-08-24 while resolving `qou-v5fp`, which had flagged
`computations/universal-ilp.witness.json` as "self-certifying — its assertions
compare the script to its own `expected` values". That description was too
generous, and the shape is not local to that producer.

## The measurement

`scripts/tautological-assertion-census.py` (added with this bean). AST, not
regex: parse every `.py` under `computations/`, `scripts/`, `tools/`, find each
`add_assertion` call, and compare the `computed` and `expected` argument ASTs
with `ast.dump`. Identical dump = the assertion holds by construction.

    files parsed          3,253   (0 unparseable)
    add_assertion calls   3,482
    TAUTOLOGICAL            266   (7.6%), across 195 files

Shape of the 266:

| both sides are | count |
|---|---|
| numeric literal | 78 |
| string literal | 76 |
| literal True/False | 44 |
| call on a computed value | 41 |
| computed variable / subscript | 27 |

The literal cases are the clearest: `add_assertion("kernel_ran", computed=1,
expected=1)` asserts `1 == 1`. The computed-variable cases are the most
misleading, because they look like real checks —
`hadron_knot_table.py:257` reads `computed=r["tr_M"], expected=r["tr_M"]` with
`source="hecke_core.build_atom_nf -> nf_tr"`, i.e. it advertises a check of the
Markov trace against a named producer and compares the value to itself.

## Why it matters

`allPassed: true` is what `computation.status: "verified"` rests on. Where the
assertions are tautological, `verified` means the script ran, not that anything
it produced was checked. 215 blocks in this corpus carry
`status: "verified"`.

## What was done here, and what was NOT

Fixed exactly one site, `computations/universal-ilp.py`, as part of `qou-v5fp`.
Its block `def:universal-ilp-algorithm` is demoted to `status: "failed"`.

**That repair is not a template.** It happened to be a case where no honest
`expected` exists yet — which operator each level should select is open — so
the fix was to assert a different, independent property (the reported label
re-parses to its own crossing count). Most of the other 265 will be ordinary
mis-wiring where a real expected value exists and was simply not passed, and
those want the value, not a substitute assertion.

Two traps worth stating, both hit while fixing the one:

1. **Longer tautologies.** "Assert the selection is Frobenius-feasible" and
   "assert it is minimum-crossing among feasible" both looked like real checks
   and are true by construction — `universal_ilp` scans crossing number upward
   and takes the first feasible candidate. Re-running the selection rule
   against itself is the same defect spelled out.
2. **Hardcoding a disputed value.** Tempting and wrong where the corpus's own
   claim is under review.

## Suggested disposition

- [ ] Triage the 266 by shape. The literal-vs-literal ones are
      mechanical; the computed-variable ones need a reading each.
- [ ] Decide whether `witness_base.WitnessBuilder.add_assertion` should
      **refuse** structurally-identical arguments outright. It cannot see the
      AST at runtime, but it can compare values and flag the common case where
      a caller passes the same object twice.
- [ ] A `folio-assistant` QA criterion is the durable fix — this is the same
      family as `lean-no-vacuous-instance-data` and
      `lean-no-definitional-laundering`, one language over. Not created yet.

## Caveat on the count

266 is exact for the rule "same AST for `computed` and `expected`". It
is a **lower** bound on assertions that check nothing: a call passing two
different expressions that happen to evaluate to the same thing by
construction — `expected=len(xs)` beside `computed=len(list(xs))` — is not
counted and is just as vacuous. Re-run the census rather than quoting this
number after the corpus moves.
