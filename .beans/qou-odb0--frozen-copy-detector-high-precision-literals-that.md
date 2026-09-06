---
# qou-odb0
title: 'Frozen-copy detector: high-precision literals that drifted from the witness they were copied from'
status: completed
type: task
priority: normal
created_at: 2026-09-06T12:46:56Z
updated_at: 2026-09-06T13:03:18Z
---

## The blind spot, and it is in an existing audit rather than absent

`computations/audits/witness_value_copy_audit.py` already covers the class I
set out to build — a script hardcoding a value another producer computed. It is
a good audit and it has 271 live findings. **The corpus-grep checklist is what
stopped me duplicating it.**

But it matches source literal against witness value by **exact string
equality** (`if sig_digits(lit) < MIN_SIG or lit not in idx: continue`, line
292), and that is the right design for what it does: an exact match is what
proves the literal *is* a copy rather than a coincidence.

Read its own statement of the harm:

> **Staleness.** The producer is re-run, the witness changes, and the copy does
> not. The two silently disagree from then on, with nothing to detect it.

**The moment that happens the copy stops matching exactly, and the exact-match
lookup goes blind to it.** So it sees copies that are still fresh — the ones
that are not yet a problem — and loses each one at the moment it becomes one. A
copy that already drifted is in neither the findings nor the clean set.

Measured on the worked case: none of the three `N3_WITNESS_*` literals in
`qbeta_habiro_integrality_kill_test` appears in any witness in the tree, so
that audit reported nothing about them for the month they were stale against
three failing cross-checks (`qou-l4q3`).

## The complement: key on the NAME, not the value

`computations/audits/drifted_witness_copy_audit.py`. A name does not change
when the value it refers to does, so it survives the drift the value does not.
Two checks, strongest first:

1. **`DECLARED_SOURCE_MISSING`** — when a comment names a *specific*
   `.witness.json`, ask **that file**. Needs no index at all. This is a claim
   about *provenance* being wrong rather than a value being stale, and neither
   audit's index can see it, since both ask "does any witness carry this"
   instead of "does the named one".
2. **`DRIFTED`** — otherwise, look the literal up in the same exact index; if
   no witness carries it, the name's claim is unbacked.

## Result on the corpus

| class | count |
|---|---|
| `DECLARED_SOURCE_MISSING` | **12** |
| `DRIFTED` | **0** |

**`DRIFTED` being empty is a result, not a broken detector.** The instance it
was written from is fixed, and `--selftest` fires on it, so the class is
demonstrably live. Two spot-checks of the twelve, both confirmed against the
named file:

- `mp_dk_decisive_test.py:60` — *"The stale muon-pin q₀ **recorded in**
  `proton-brane-tower-correction-probe.witness.json`"*. That witness does not
  carry it. The value is *deliberately* stale (the test is about a superseded
  pin); the **provenance claim** is what has broken.
- `phi_q_regularization_probe.py:132-133` — *"From
  `mass-formula-6term-mpfr-50dps.witness.json`"*. Not there; the nearest
  carrier is the probe's own witness.

## These are CANDIDATES; the verdict is an agent's

A comment can name a witness for context rather than as the value's source. The
audit establishes something narrow and checkable — *the named file does not
carry this value* — and whether that matters is a judgement, the same posture
as the vacuity audit's ledger.

## Three defects in my own detector, all found by running it

1. **Own-witness exemption, inherited without thinking.** I copied the
   sibling's rule that a literal in the producer's own witness is a
   self-regression check. Here it is wrong: the name or comment *declares an
   external source*, which is exactly what makes it checkable. It was hiding
   the case where a declared source carries nothing at all.
2. **Precision-of-rendering read as drift.** 3 of the first 5 findings were one
   number at two output widths. The guard has to accept **both** truncation and
   rounding — a rounding test alone rejects a clean prefix (rounding 30 digits
   to 28 carries the last digit), and a prefix test alone rejects the rounded
   case. My first version had only the rounding half and my own selftest caught
   it.
3. **Negative literals invisible.** The index is built from unsigned matches,
   so a signed lookup missed every negative constant — including
   `N3_WITNESS_C3`, one of the three the audit exists for.
