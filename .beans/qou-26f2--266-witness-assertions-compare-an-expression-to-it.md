---
# qou-26f2
title: 266 witness assertions compare an expression to itself and pass by construction
status: in-progress
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


---

## Drain started 2026-08-25 — triaged by IMPACT, not by count

Draining 266 sites in file order would spend most of the effort on probe
scripts nothing cites. Cross-referenced the 195 files against every content
block's `computation.script` instead:

    195 files carry tautologies
     14 of them back a content block at all
     10 of those back a block claiming `status: "verified"`

**Those 10 are the drain.** Everywhere else the tautology is a defect in a
probe; here it is a defect in a *claim*, because `verified` on the block rests
on `allPassed: true` from an assertion that cannot fail.

| taut | block | producer |
|---|---|---|
| 4 | `conj:schwinger-measure-computational-time` | `probes/r2core_schwinger_measure_explore_probe.py` |
| 3 | `thm:topological-mass` | `mass-from-q-symbolic.py` |
| 2 | `prop:confinement-nf-partial-proof` | `shift_from_nf_basis.py` |
| 1 | `conj:staircase-ew-residual` | `staircase_ew_residual_conjecture.py` |
| 1 | `prop:t-beta-markov-frobenius-collapse` | `qbeta/qbeta_markov_trace_norm_probe.py` |
| 1 | `rem:knot-operator-basis-table` | `photon_operator_table.py` |
| 1 | `rem:per-observable-100x-status-dashboard` | `per_observable_100x_status.py` |
| 1 | `conj:flavor-split-habiro-derivation` | `mn_flavor_split_h4_plancherel.py` |
| 1 | `rem:hecke-operations` | `basis_knot_tables.py` |
| 1 | `prop:bar-involution-invariance` | `audits/brundan_kleshchev_audit.py` |

Progress is checked off below as each lands. The remaining ~250 sites stay open
and are *not* urgent by the same argument: no block's status depends on them.

- [ ] `conj:schwinger-measure-computational-time` (4)
- [ ] `thm:topological-mass` (3)
- [ ] `prop:confinement-nf-partial-proof` (2)
- [ ] `conj:staircase-ew-residual`
- [ ] `prop:t-beta-markov-frobenius-collapse`
- [ ] `rem:knot-operator-basis-table`
- [ ] `rem:per-observable-100x-status-dashboard`
- [ ] `conj:flavor-split-habiro-derivation`
- [ ] `rem:hecke-operations`
- [ ] `prop:bar-involution-invariance`
- [ ] the ~250 with no block dependency — bulk, low priority

## Checker landed

`assertions_are_falsifiable` is live in folio-assistant
(`content/pipeline/qa-checkers-python.ts`, registered `critical` in the
criteria registry and the script sweep). 202 hits corpus-wide, 98% precision /
75% recall against the AST census; it under-reports by design. So this bean's
backlog is now machine-visible and regressions are caught at the gate.
