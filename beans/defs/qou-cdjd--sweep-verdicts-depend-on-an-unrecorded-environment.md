---
# qou-cdjd
title: 'Sweep verdicts depend on an unrecorded environment: mpmath absent made 55 producers unrunnable and the harness did not say so'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T13:14:20Z
updated_at: 2026-10-04T15:24:40Z
parent: qou-5vkl
---

## What happened

This container came up without `mpmath`. Every one of the 55 producers dies on
its import line, so the sweep measured nothing — and reported 23 of 23 as
`UNCHANGED/ASSERT-FAIL` in 54 seconds, including `alpha_5_lp_dual_crystal`,
which needs more than 420s to run. The tell was the runtime, not the verdict.

Two distinct defects, only one of which is now fixed:

1. **FIXED (`eec749e9be`)** — `CRASH` was unreachable. `produced` was
   `bool(moved) or canon(wp) is not None`, and `canon(wp)` reads the *committed*
   witness, present on disk regardless of what the run did. So a producer that
   wrote nothing fell through to `UNCHANGED`: "reproduces its committed
   artifact; the anchor move is the ONLY thing that will change it". `produced`
   is now an mtime delta.

2. **OPEN (this bean)** — the verdict file records nothing about the
   environment that produced it. A `--out` from a container missing `mpmath`,
   or missing `pyhecke_native`, is indistinguishable from one where every
   producer ran. Verdicts are only comparable across containers if the file
   says what it ran against.

## Proposed fix

Stamp the `--out` file with an environment block — Python version and the
resolved versions of `mpmath`, `sympy`, `numpy`, `pyhecke_native` — and refuse
to start when a module every producer imports is missing, rather than
attributing the resulting silence to the corpus. `witness.py` already records
`environment` per witness; the sweep should record it once per run.

## Evidence this is not hypothetical

The four verdicts re-measured after installing `mpmath` agree 4/4 with the
reclaimed container's independent run (`SUBSTANTIVE/ASSERT-FAIL`, `TIMEOUT`,
`UNCHANGED +1 sibling`, `SUBSTANTIVE`). The uniform `UNCHANGED` was entirely an
artifact of the environment, and nothing in the output said so.

The failure mode is asymmetric: a corpus-wide "nothing is pre-existing stale"
is precisely the conclusion PR #5519 exists to establish, so this bug fails
towards the answer that gets believed.

In-progress in Round 102 PR litlfred/qou#8453.
