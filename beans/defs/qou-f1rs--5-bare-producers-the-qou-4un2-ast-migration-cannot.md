---
# qou-f1rs
title: '5 bare producers the qou-4un2 AST migration cannot handle: 3 inline dict literals at the write site, 2 with no write call'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T20:19:49Z
updated_at: 2026-10-04T15:16:05Z
parent: qou-5vkl
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


---

## CORRECTED 2026-08-28 -- both of the "class B" entries were mine, not the corpus's

This bean said the 2 class-B producers were reached "through a shape the finder
does not model" and suggested extending the planner. **That diagnosis was a
guess and it is wrong.** Neither file writes a witness at all:

* `computations/derived_masses.py` has **no** `json.dump` / `write_text` to a
  witness. It READS three (`_Q_PINNING_WITNESS`, `_BETA_DECAY_WITNESS`,
  `_FREE_NEUTRON_WITNESS`) and prints a summary to stdout. It entered the
  population because `free-neutron-decay.witness.json` records
  `scriptFile: derived_masses.py` -- naming a **consumer**. The real producer is
  `computations/free-neutron-decay.py`, a bare `json.dump` at line 535.
* `computations/per_irrep_pole_proton_h3.py` has **zero** write calls of any
  kind. It is a 98-line shim that delegates to `per_irrep_pole_atom.run_atom`,
  and `per_irrep_pole_atom.py` does use `WitnessBuilder`. The witness's
  `scriptFile` is the attribution from before the `qou-okl8` consolidation. Its
  own docstring says the two witnesses now record
  `scriptFile: per_irrep_pole_atom.py`.

So the remaining genuine bare producers in that pass were **3, not 5** -- all
class A (inline dict at the write site).

## The finding underneath, which is much larger than these two

Both false positives have the same root cause, and chasing it showed the
**population itself was built the wrong way round**.

The first pass was WITNESS-FIRST: walk every `*.witness.json`, read `scriptFile`,
resolve to a producer. That can only ever see a producer some witness *names*,
so it misses three classes:

1. **A witness with no provenance field at all.** Nothing to resolve, producer
   invisible. **248 of 2842 witnesses (8.7 %) are in exactly this state** -- so
   the scan is blindest to precisely the defect this bean is about.
2. **A witness whose `scriptFile` names the wrong file** (free-neutron-decay).
3. **A witness naming a shim** whose write is delegated (per_irrep_pole_proton_h3).

WRITER-FIRST is the correct construction: walk every `computations/**/*.py`,
keep those with a witness write and no `WitnessBuilder`. It asks the actual
question and depends on no witness field. Measured: it finds **287 more bare
producers, disjoint from the 282 already migrated** -- the first pass
undercounted by ~48 %.

`--scan {writer,witness}` now selects; `writer` is the default and `witness`
exists only to reproduce the first pass.

## Two further planner defects the second pass exposed

* **Payload type was never checked.** `stamp_staleness_metadata` does
  `payload["scriptHash"] = ...`, so a non-dict raises `TypeError` at run time.
  13 producers bind the write payload to a **list** and 8 more to a string /
  bytes / opaque call -- a file that merely READS a witness passes a "mentions
  `.witness.json`" filter while its `write_text` emits markdown or a text
  report. Stamping those 21 would have broken 21 working scripts. Gated by
  `payload_is_dict`.
* **The gate has to be nearest-preceding, not any-binding.** `out = []` (an
  accumulator in an earlier function) then `out = {...}` (the witness) is a
  common idiom here -- 11 of the 13 list-bound payloads look like that. An
  "any binding is a dict" test passes them for the right reason by accident and
  would equally pass the reverse order, where the live value really is a list.

## Live remainder after the second pass

* **30 inline-dict producers** (3 from pass 1 + 27 from pass 2). Still a
  different migration: the literal must be bound to a name first, so it is a
  structural edit per file rather than an insertion.
* **10 non-dict payloads**, correctly excluded. Most are not witness producers
  at all (they write `.md` / text) and should be dropped from the population
  rather than stamped; `doorv_barparity_guardrail.py` (`witness` bound to a
  call) is the one worth a look.

## Method note

The two false positives here, and the two "payload never assigned" false
positives in the verification pass (both were tuple unpacking, which a
`targets[0]` test cannot see), were all **measurement bugs, not corpus
defects**. Every one was found by checking the finding rather than reporting
it. Diagnose before extending the tool.
