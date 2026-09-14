---
# qou-381n
title: 'SCREEN: 46 Lean files carry numeric literals citing a producer whose witness no longer matches its source — 1 confirmed (JetOrderIndependence), 45 unverified'
status: todo
type: task
created_at: 2026-09-14T20:56:23Z
updated_at: 2026-09-14T20:57:17Z
---


## The claim

A Lean file that documents its constants as coming from a `computations/` script
is making a **provenance claim**, and nothing in this corpus checks it. When the
producer changes, the Lean keeps the old numbers and keeps the old sentence, and
everything still looks right: the theorems typecheck, the file compiles,
`#print axioms` is clean. Only the claim is false.

Measured on main `6229029329`:

```
corpus Lean files (excluding .lake)  : 3856
  ... carrying a numeric literal     : 2086
live producers under computations/   : 4434
witnesses carrying a scriptHash      : 3121

CANDIDATES (distinct lean/producer pairs) :  46      = 2.2% of 2086
  ... confirmed defects                   :   1
  ... unverified                          :  45
```

## The one confirmed instance, and how it hid

`QOU/Archimedean/JetOrderIndependence.lean` documents

```
jetJacobianBase = !![1/4, -1, 55/16; 1/2, 0, -1/16; 1, 0, 0]
```

as *"witnessed from the framework's own canonical Markov traces
(`computations/jet_order_pivots.py`)"*. Running that producer today gives
`!![1/4, 0, 11/4; 1/2, 1, 1/4; 1, 0, 0]` — elimination determinant **`−11/4`,
not the `1/16` the Lean carries**, LU pivots `(1/4, 1, −11)` rather than
`(1/4, 2, 1/8)`. Two of three rows moved; `Borromean` and the whole `h^0` column
did not. Producer drift, not import-cone: `scriptHash` `1eadd3f17d76` against
the witness's `380671554d5b`, witness dated 2026-06-08.

**Nothing is wrong, and that is the point.** `−11/4 ≠ 0` exactly as `1/16 ≠ 0`,
so jet-order independence still holds and every theorem in the file is still
true. The exposure is provenance alone.

**That file had been verified three separate times** — 2026-08-22, 2026-09-08,
2026-09-14 (`qou-1n7g`) — and none of the three caught it, including mine.
All three checked the **shape** of the discharge (is there a fabricated
instance?) and none re-ran the producer. Detail in `qou-xc8t`.

## Why nothing else covers this

The three nearest audits are each scoped away from it:

| audit | scope |
|---|---|
| `assertion_on_literal_audit.py` | Python witness assertions, not Lean |
| `hardcoded_literal_audit.py` | `rglob("*.py")`, and about CODATA constants |
| `lean_ref_resolution_audit.py` | `rglob("*.ts")`, resolution not values |

**Every literal audit in this corpus is Python-scoped** — the same shape as
`convention-c-producer-audit.py` walking only `*.py` while the Lean Markov-
parameter surface went uncounted for weeks. Candidate row for the
detector-blindness taxonomy, and it is a *scope* row, not a spelling one.

## The screen

[`computations/audits/lean_literal_producer_drift_screen.py`](computations/audits/lean_literal_producer_drift_screen.py).
Reports a Lean file when BOTH (1) it carries a rational or decimal literal and
(2) it names a `computations/` producer whose committed witness records a
`scriptHash` that no longer matches that producer's source. Read-only; writes
no witness and no file. `--selftest` PASSES by pinning the one confirmed
positive and **fails** if the screen stops reporting it — a calibration an audit
asserts about itself cannot discover its own blind spot.

**It is a screen, not a verdict, and condition 2 is weak.** AGENTS.md records
~700 self-stale witnesses corpus-wide of which essentially none is safe to
refresh, so a self-stale citation is the normal state. What the screen buys is
the *intersection*: a provenance claim, over numbers, whose source has moved.

Limits, stated so they are not rediscovered: association is by stem
(`<a-b-c>.witness.json` ↔ `<a_b_c>.py`), a producer with no witness is
invisible, `scriptHash` is a whole-file hash so comment-only edits drift it, and
**it cannot see import-cone drift** — a producer byte-stable while a module it
calls changed is not flagged (use `witness_import_cone_staleness_audit.py`).

**A defect found in the screen itself, recorded because it is the recurring
class.** The first draft did not exclude `.lake/` and reported *"11869 Lean
files scanned"* — **8013 of them Mathlib's own source**. The candidate count was
unaffected (no Mathlib file cites a `computations/*.py`) but every denominator
was inflated ~3×. Caught only by checking that the known positive appeared,
which required reading the head of the output rather than the tail.

## What I did NOT do

- **No hit was investigated beyond the one already known.** 45 are unverified.
- **Nothing is wired.** The screen exits 0 regardless; it is in no gate. Making
  it blocking needs a triage pass first, and most hits are probably benign.
- **No Lean literal was changed**, and none should be on the strength of a hit.
  Adopting a producer's current numbers assumes the producer is what is right;
  it may be what regressed. `qou-xc8t` enumerates that decision with options.

## Options

**A. Triage the 45** — read each hit's literals against a fresh producer run,
record a verdict per site in a committed ledger (the `lean-vacuity-review-ledger`
pattern). *Costs*: 45 producer runs, some expensive. *Risks*: none, it is
measurement. *Commits to*: keeping the ledger fresh as producers move.

**B. Wire it as an advisory line in `precision-gates.sh`** after A. *Costs*:
one line plus the scan's runtime (~90 s). *Risks*: a noisy advisory trains
readers to ignore advisories. *Commits to*: keeping the count near zero.

**C. Leave the screen committed and unwired** (the `qou-36i2` precedent — the
detector is on main, the wiring is gated). *Costs*: nothing. *Risks*: a detector
nobody invokes is documentation. *Commits to*: nothing.

**D. Do nothing further.** The 46 stay unmeasured and the next agent finds the
next one the way this one was found — by accident, three verifications in.

**Default is C**, which is where this bean leaves it.

**Recommendation, my judgement and not a finding: A, then decide B on what A
finds.** If most of the 45 are benign the class is not worth a gate and C is the
honest end state; if several are real then the provenance claim is systematically
unreliable and that is worth knowing before the next reader trusts one. A is
pure measurement and needs no permission — I stopped here for turn length, not
because it is gated.

## Blast radius

Confined to *what a reader believes about where a constant came from*. No
theorem, witness or content block changes on any hit. The reason it matters is
that these docstrings are exactly what a reviewer checks a Lean constant against
— the sentence is doing the work an audit would otherwise do, and on at least
one file it has been wrong for three months.
