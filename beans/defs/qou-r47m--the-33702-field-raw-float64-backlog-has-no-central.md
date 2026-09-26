---
# qou-r47m
title: The 33,702-field raw-float64 backlog has no central fix — measured, and it refutes the assertion-API lever
status: completed
type: task
priority: normal
created_at: 2026-09-06T10:59:23Z
updated_at: 2026-09-06T11:10:40Z
---

## The finding, stated as a negative

`computations/raw-float64-baseline.json` tolerates **33,702 raw-float64 fields
across 1,015 witnesses** (after this session's drain of 1,091 → 1,015 /
35,225 → 33,702). The obvious question is whether one central change drains a
large fraction of it. **Measured: no.** No lever above ~10 % exists, and the
two candidates that looked like levers are both refuted below.

Producer: [`computations/audits/raw_float64_backlog_structure.py`](computations/audits/raw_float64_backlog_structure.py);
witness `computations/audits/raw-float64-backlog-structure.witness.json`.

## Refuted candidate 1 — the assertion API is 1.6 %, not a lever

`WitnessBuilder.add_assertion` writes `expected` / `computed` / `tolerance` on
every assertion, and `_tolerance_literal` already serializes the tolerance leg
losslessly. It is tempting to read that as "extend the same mechanism to the
other two legs and a large block of the backlog drains".

The reading collapses once the population is counted the way the audit itself
counts it. `witness_raw_float64_audit._count(obj, integral_is_exact=True)`
**excludes integral floats** — they are exact in binary64 and are reported as a
separate metric, not as dirt. Of the assertion legs, **556 of 765 `expected`
and 291 of 607 `computed` are integral**, so most of what a naive scan counts
there is not in the backlog at all.

    under .assertions[]        589 fields   1.59 % of 36,945 non-integral leaves

## Refuted candidate 2 — `_tolerance_literal` cannot generalise to `expected`

`_tolerance_literal` serializes a **declared** tolerance as the author's own
literal and **refuses computed ones**. Its 5-significant-digit cut is justified
in its docstring by an **empty bin at 6** — the cut sits where no member lives,
so it is a cluster boundary rather than a threshold chosen to hit a target.

`expected` has no such boundary. Measured, non-integral, by significant digits:

    1:9  2:20  3:29  4:36  5:19  6:4  7:10  8:25  9:8  10:3
    11:7 12:7  13:2  15:3  16:17 17:10

Smeared across the whole range with no empty bin. Extending the mechanism would
mean picking a threshold with no empirical justification — exactly what that
docstring declines to do. **The mechanism is correct where it is and must not be
generalised on the analogy alone.**

## What the backlog actually is

    solver-output field names   3,801   10.29 %

float64 because scipy and Clarabel are float64. Not a serialization slip; not
fixed by carrying `mpf` to the boundary. Closing these means changing the solve,
not the write.

By producer bucket (files / fields):

| bucket | files | fields |
|---|---|---|
| C. imports mpmath AND `fmt`, still dirty | 463 | 15,189 |
| A. no mpmath at all | 181 | 8,600 |
| unresolved producer (resolver limit, not a defect class) | 297 | 8,181 |
| B. mpmath, no `fmt` | 74 | 1,732 |

**C is the cheap class and the place to start.** Those producers already have
both halves imported, so specific fields slip at the serialization boundary —
which is the shape of both fixes landed on 2026-09-06 (`mass_endomorphism`,
`habiro_exact_mass_endomorphism`). **A is expensive**: the computation itself is
f64, so fixing it moves recorded numbers and needs a re-derivation, not a
re-serialization.

## Consequence

The ratchet's design — tolerate what is there, never grow, drain as producers
are touched — is the **correct** response to a backlog of this shape, not a
stopgap awaiting a bulk pass. An agent looking for a bulk pass should read this
bean instead of repeating the search.

Two figures to not repeat: I reported **4,414 distinct leaf names** mid-session;
the producer measures **4,192**. And the 1.6 % figure is only correct with
integrals excluded — counting them gives a different population and inflates
every name ranking.


## 🛑 Correction, made before this bean's first commit — the bucket table was inverted

The first version of this bean (and of the producer) reported bucket **C** —
producers that already import both `mpmath` and `_precision.fmt`, i.e. the
*cheap* class — as **463 files / 15,189 fields, 45 % of the backlog**, and told
the reader to start there.

**It is 81 files / 2,054 fields, 6.1 %.** The mass is in bucket **B**.

Cause: `binds_fmt` asked `"_precision import" in src` — a **substring**, which
`from _precision import set_compute_dps` satisfies while binding only the dps
setter and never the serializer. **377 producers** were filed as "already has
both halves, so this is only a boundary slip" when they have no serializer at
all. The predicate is now an AST walk requiring the name to be *bound*
(`ImportFrom` from a `_precision` module with an alias `fmt` or `*`, or any
`.fmt` attribute access), with a `--selftest` whose second case is exactly the
line that misfiled the 377 — so a future narrowing cannot silently pass.

This is AGENTS.md's detector-blindness class verbatim — keying on how an author
*spelled* something rather than on what it binds — committed inside an audit
whose entire subject is a precision detector.

**Corrected table** (files / fields, from `computations/raw-float64-baseline.json`):

| bucket | files | fields | share |
|---|---|---|---|
| **B. imports mpmath, does NOT bind `fmt`** | 456 | 14,867 | 44.1 % |
| A. no mpmath at all | 181 | 8,600 | 25.5 % |
| unresolved producer (resolver limit, not a defect class) | 297 | 8,181 | 24.3 % |
| C. imports mpmath AND binds `fmt`, still dirty | 81 | 2,054 | 6.1 % |

**The correction improves the campaign's prospects rather than worsening them.**
B is the more tractable half: the arithmetic is already in mpmath and only the
*write* is missing, so routing it through `fmt` is mechanical, where C's
remaining dirt is a per-field slip in a producer that already knows the
discipline.

**But B is a CANDIDATE class, not a guaranteed-cheap one.** `import mpmath` at
the top of a file does not establish that the *dirty leaf* was computed in
`mpf` — a producer can carry one quantity in `mpf` and compute another in
`float`. Confirm per producer before claiming a fix is a re-serialization.

Everything above the correction — the 1.6 % assertion-API refutation, the
`_tolerance_literal` non-generalisation, the 10.3 % solver share, and the
verdict that no central fix exists — is **unaffected**: none of it depends on
the bucket predicate.

Two figures not to repeat: **4,414** distinct leaf names (the producer measures
**4,192**), and bucket C at 463/15,189.
