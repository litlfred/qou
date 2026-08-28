---
# qou-f1rs
title: '5 bare producers the qou-4un2 AST migration cannot handle: 3 inline dict literals at the write site, 2 with no write call'
status: todo
type: task
priority: normal
created_at: 2026-08-28T20:19:49Z
updated_at: 2026-08-28T20:20:27Z
---

## Context

`scripts/migrate_bare_producer_provenance.py` stamps provenance on the bare
producers by inserting, immediately before the write statement:

    WitnessBuilder.stamp_staleness_metadata(
        <payload>, script_path=__file__, q0_anchor=<None|False>)

It planned 282 of the 287 and applied them. These 5 are the remainder, held
back deliberately rather than force-fitted.

## The 5, by cause

### A. Payload is an inline dict literal at the write site (3)

    computations/bar_pairing_binding_observable.py
    computations/codata_truncation_audit.py
    computations/audits/witness_producer_executes_audit.py

Shape:

    out.write_text(json.dumps({ ... }))

There is no variable to stamp. Fixing one means binding the literal to a name
first:

    payload = { ... }
    WitnessBuilder.stamp_staleness_metadata(payload, script_path=__file__, ...)
    out.write_text(json.dumps(payload))

That is a real edit to the producer's structure rather than an insertion, so it
is three hand edits, not a pass. `bar_pairing_binding_observable.py` writes
TWO witnesses (a `legacy` path and an `out` path), so it needs both sites done
and is the least trivial of the three.

### B. No `json.dump` / `write_text` call the AST can find (2)

    computations/derived_masses.py
    computations/per_irrep_pole_proton_h3.py

Not yet diagnosed. Both contain the string `json.dump` in `code_only`'d source
-- that is how they entered the population -- so the write is presumably
reached through a shape the finder does not model (a helper it calls, a write
inside a comprehension or a `try`, or an assignment rather than a bare `Expr`).

Worth diagnosing before hand-editing: if it is a *shape*, the finder should
learn it and the fix is one more case in the planner rather than two manual
edits. The BinOp case earlier in this migration was exactly that, and modelling
it recovered 78 files.

**`per_irrep_pole_proton_h3.py` is a special case regardless**: it is one of the
two producers bean `qou-okl8` is about (two producers writing one witness name
with different schemas), and `_check_producer_takeover` guards it. Read that
bean before touching it -- a naive stamp could interact with the takeover guard.

## Why this is not urgent

The guard merged in #5883 already prevents a re-run of any of these five from
DELETING provenance a downstream pass added, because it keys on the file rather
than the producer. What is missing is only that they do not yet emit their own.
So this is drain, not containment.

## Next step

1. Diagnose the 2 in class B: is it one unmodelled shape, or two one-offs? If
   one shape, extend the planner instead of hand-editing.
2. Hand-edit the 3 in class A, `bar_pairing_binding_observable.py` last since
   it has two write sites.
3. Re-run the planner; it should report 0 remaining.
