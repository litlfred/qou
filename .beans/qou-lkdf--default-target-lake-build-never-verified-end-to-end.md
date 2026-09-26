---
# qou-lkdf
title: 'ANSWERED: the default target BUILDS (4390 jobs, 0 errors) — and its closure still contains 11 sorries'
status: completed
type: task
priority: medium
tags:
    - lean
    - infra
    - ci
    - qou-lkrd
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-09-26T11:03:24Z
---

## ✅ ANSWERED 2026-08-09 — and the green is the less interesting half

Run to completion, in the background, surviving the session. **E1, as written.**

    lake build                    # default target = QOU root's import closure
    → Build completed successfully (4390 jobs).  exit 0

| measured | value |
|---|---|
| branch | `claude/fivetwo-level7-ladder-numerators` @ **`92cba32697`** |
| `origin/main` at the time | **`d8d22890c7`** |
| how far behind | **97 commits** |
| jobs | 4390 |
| errors | **0** |
| declarations using `sorry` | **11** |
| warnings | 394 (167 unused-simp-arg, deprecations, duplicate namespaces) |

⚠ **THIS IS NOT A CLAIM ABOUT `main`.** It is a claim about a branch 97 commits
behind it. Recording the sha is the whole point of this bean's sibling
(`qou-mfst`'s format rule), and the reason is `qou-lkrd`: a measured claim on a
long-lived branch silently ages into a claim about `main` and is then wrong.

### The finding that outlives the green: **green ≠ sorry-free**

The default target exits 0 **while its own import closure contains 11 `sorry`
declarations**, in 7 modules:

| module | count |
|---|---|
| `QOU/BraidKnot/YoungTableauStandard.lean` | 3 |
| `QOU/BraidKnot/Specht.lean` | 2 |
| `QOU/BraidKnot/SpechtClassification.lean` | 2 |
| `QOU/Mathlib/EllipticDivisorDegree.lean` | 1 |
| `QOU/Mathlib/HadamardFactorization.lean` | 1 |
| `QOU/Mathlib/QGevreyOrder.lean` | 1 |
| `QOU/Archimedean/HyperbolicVolumeIndependence.lean` | 1 |

**None is in the 5₂ lane** — no `FiveTwo*`, no `MathlibExt` dilogarithm chain, no
`ImplicitScalar`. Those remain sorry-free and axiom-audited.

This sharpens what `qou-lkrd` left behind. That bean's surviving content was
*"'lake green' has usually meant targeted module builds, not the default
target."* True — and now measured, the default target is green too. But a
reviewer who hears "lake build passes" and infers "the library is proved" is
still wrong, for a **different** reason: `sorry` is a warning, not an error, so it
does not stop the build. Two distinct gaps between "lake green" and "verified",
and closing the first does not close the second.

⚠ Coordination: three of those files — `QGevreyOrder`, `HadamardFactorization`,
`YoungTableauStandard` — are exactly what the sibling on **#4785** described
working on ("3 of the 12 cited sorries in my branch's base"). That lane's gate
(`proof-no-false-cited-sorry`) is aimed at this class. Worth telling them the
count is 11 in the *reachable* closure, which is a smaller and sharper number
than a whole-tree scan.

### What E3 would now be

E3 said "if green, wire it into a gate that says which target it ran". Still
worth doing, and it should report **both** numbers — job count *and* sorry count
— because this run shows the first can be clean while the second is not. A gate
that only checks the exit code would certify a closure containing 11 sorries.

## The original framing (superseded)

## What is open

Every Lean claim in the 5₂ lane is verified by **targeted** builds
(`lake build QOU.QBeta.FiveTwoTransport`, and so on, one target per module).
Nobody has run the **default** target — plain `lake build` — to completion and
seen it green.

An attempt on 2026-08-08 was killed by a container restart at ~7200 log lines
with no verdict. That is the entire state of knowledge: **unknown**, not green
and not red.

## Why this is a distinct bean from qou-lkrd and qou-orph

* `qou-lkrd` claimed the default target was **red** on main with 22 errors in
  two modules. **That claim is now false** — re-measured, both modules build
  clean. It was recorded against a ~194-commit-stale base. Do not quote it.
* `qou-orph` establishes that `lake build` compiles only `QOU.lean`'s import
  closure — 786 of 1644 modules (47.8%, at `origin/main` `ee66f30102`) are never
  built. True, and about the modules **outside** the closure.

Neither answers the question here: **does the closure itself build?** That is
what a reviewer hears when told "lake green", and it is not what has been
verified. The scope lesson survived `qou-lkrd`'s retraction and belongs here.

## Attack vectors

### E1 — Just run it, in the background, and record the result with its base sha
`lake build` from `content/quantum-observable-universe/lean`, backgrounded, with
a generous timeout, logging to a file. The only real requirement is that it
**survives the session** — the last attempt died with the container. Record the
verdict *and* the `origin/main` sha, per `qou-mfst`'s format rule; a bare
"green" ages into a false claim within a day at this repo's merge rate.

### E2 — If red: triage by module, do not wire anything
Failures will be main-side and outside this lane (the closure is mostly other
people's work). Produce a per-module list with the actual error, open a bean per
owner-ish cluster, and **do not fix them from a feature branch** — that is how
you collide with siblings. `qou-lkrd`'s original triage is the template; its
*method* was fine, only its base was stale.

### E3 — If green: wire it into a gate, and make the gate say which target it ran
The point is not the one-off result, it is that "lake green" should stop being
ambiguous. A workflow step running the default target, named so the log
distinguishes it from targeted builds. Note CI auto-triggers are disabled
repo-wide since 2026-06-30 for Actions billing, so it would be
`workflow_dispatch`-only like the other two gates — still worth having as the
thing a human can run and quote.

### E4 — Cheap partial: build the closure of just the touched subtree
If the full default target is too slow to be practical, `lake build QOU` with a
timeout still exercises the closure and gives a partial answer. Report it as
partial — **do not let a timeout read as a pass.** That substitution is this
lane's signature failure mode and it has recurred twelve times.

## Do this first

E1. It is one command, it needs no decisions, and its outcome picks between E2
and E3. The only discipline that matters is not reporting the answer until the
command actually finishes — an empty log is not a pass, and a wrapper's exit
code is not lake's.

## Refs

* `qou-lkrd` (the retracted red claim, and the surviving scope lesson),
  `qou-orph` (the 47.8% outside the closure), `qou-mfst` (record the base sha)
* PRs #4776, #4777, #4701 — all three state their Lean verification as
  *targeted per-module builds*, deliberately

**The 5₂ sum rule remains verified to 80 dps, unproved.**
