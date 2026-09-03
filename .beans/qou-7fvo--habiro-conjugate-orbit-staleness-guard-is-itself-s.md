---
# qou-7fvo
title: 'habiro conjugate-orbit staleness guard is itself stale: expects 3 atoms, run produces 5'
status: completed
type: task
priority: normal
created_at: 2026-08-30T06:55:28Z
updated_at: 2026-08-30T09:08:54Z
---


## What it is

`computations/probes/habiro_frobenius_conjugate_orbit_probe.py` carries a
**staleness guard** — an assertion whose stated purpose is to trip if the
Habiro coefficients or the p=2 collapse arithmetic drift:

```
# Staleness guard: at p=2 the representative collapses to the rational
# integer C, so the norm is forced to C^2. These are the constants bean
# `qou-lrnd` corrected the corpus to on 2026-08-23. If either the
# coefficients or this arithmetic drift, these trip rather than going quiet.
```

It has gone quiet in the one way the comment did not anticipate: **the guard
itself went stale.** Its hardcoded `expected` lists three atoms; the run
produces five.

```
computed  {p: [8,64], n: [2,4], D: [192,36864], T: [384,147456], 3He: [1536,2359296]}
expected  {p: [8,64], n: [2,4], D: [192,36864]}
```

Tritium and ³He were added to the atom set after the guard's dict was written,
and the dict was never extended. The two new entries are not *wrong* — they
follow the same `norm = C²` law (384² = 147456, 1536² = 2359296) — so the
right fix is almost certainly to extend the expected dict, not to change the
arithmetic. That is an author call, which is why this is a bean and not an
edit.

## Not caused by this branch, and not caught by any gate

Confirmed by controlled test: `main`'s own copy of the probe, run from a
`main` worktree, fails the identical assertion. My branch had not touched this
file before draining two unrelated tautologies in it.

**The committed witness says `passed: true` for this assertion.** So the
corpus carries a green record for a check that fails on a clean re-run of
`main`. That is the `qou-a31p` shape — except a31p's flips were suspected
regeneration artefacts, and this one reproduces identically on both branches,
so it is a genuine drift the committed witness is hiding.

Nothing catches it: the failed-assertion ratchet in `precision-gates.sh` is
**advisory, not blocking** (a31p), and nothing re-runs the producer.

## Related but distinct

`qou-iph3` ("habiro-frobenius probe: deprecated input, hidden failing test")
is **completed** and covers `habiro_frobenius_probe.py` — the *first* probe.
This is the conjugate-orbit probe, which that file's own header explains was
written as a second probe rather than an edit. Different file, different
defect.

## RESOLVED 2026-08-30

Fixed by separating the two jobs the guard's own comment names, which were
tangled into one assertion.

The comment says: "at p=2 the representative collapses to the rational integer
C, so the norm is forced to C^2. These are the constants bean `qou-lrnd`
corrected the corpus to. If either the coefficients or this arithmetic drift,
these trip rather than going quiet." That is two claims:

* **the arithmetic** — `norm = C^2`, a mathematical identity that holds for
  any atom and cannot go stale as atoms are added;
* **the constants** — the drift detection, whose authority is `qou-lrnd`'s
  deliberate correction of three specific values.

They were asserted as a single dict comparison, so adding atoms to the corpus
broke the *arithmetic* check by way of the *constants* dict being short. The
guard stopped checking anything and reported a count mismatch instead.

Now:

    p2_norm_is_square_of_collapse_constant_all_atoms   5 of 5   (the identity)
    p2_rep_is_collapse_constant_and_norm_is_its_square 3 of 3   (the qou-lrnd pin)

The law assertion covers every atom with an exact p=2 row, so a sixth atom
extends coverage automatically instead of silently shrinking it. The witness
now records all five constants, plus which are pinned and which are not.

## Why the new constants were NOT pinned

T = 384 (147456) and 3He = 1536 (2359296) do satisfy the same law, and it was
tempting to just extend the dict. That would be **fitting**: their authority
would be "this is what the run printed", where the existing three carry an
author's deliberate correction behind them. They are recorded under
`p2_constants_not_yet_pinned` for an author to adopt, and the identity check
covers them meanwhile.

## Note on the red going green

`p2_rep_is_collapse_constant_and_norm_is_its_square` failed on `main` and
passes here, which deserves the scrutiny. It was failing on a **count
mismatch**, not on detected drift — it was never comparing T or 3He against
anything, it was failing to compare at all. Restricting it to the scope it was
written for makes it report the true thing it was built to report, and the new
law assertion checks strictly more than before, not less. No pinned constant
changed.
