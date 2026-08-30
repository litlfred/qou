---
# qou-7fvo
title: 'habiro conjugate-orbit staleness guard is itself stale: expects 3 atoms, run produces 5'
status: todo
type: task
priority: normal
created_at: 2026-08-30T06:55:28Z
updated_at: 2026-08-30T06:55:43Z
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
