---
# qou-pdgc
title: 'The Hecke oleans were 3 months stale: 3 defs read as AXIOMS and wenzlBridge carried a retracted form'
status: in-progress
type: task
created_at: 2026-09-05T17:29:43Z
updated_at: 2026-09-05T17:29:43Z
---


Found while trying to state the trace identity `qou-kp2z` showed the
`MarkovTrace.lean` module doc had been falsely advertising. The identity is now
proved; this bean is the environment defect the attempt uncovered.

## The measurement

`lean`-direct verifies a file against the **oleans on disk**, not the source
tree. `QOU/HeckeAlgebra/MarkovTrace.olean` was dated 2026-06-10, ~3 months
behind source. Comparing every declaration's source kind against its kind in
that olean:

| source | olean | count |
|---|---|---|
| `noncomputable def` / `def` | **AXIOM** | 3 — `JonesMarkovCoefficient`, `partitions_as_finset`, `markovTraceOnWedderburn` |
| `theorem` | **ABSENT** | 5 |
| `axiom` | `AXIOM` | 2 (correct) |
| `opaque` | `opaque` | 2 (correct) |

and `wenzlBridge` carried `∀ (q : ℝ), markovTraceOnWedderburn x = Σ_λ y_λ(q) …`
— the universally-quantified form source had already **retracted** under bean
`qou-ck1f` as "asserting the negation of what it was for", since the left-hand
side does not mention `q`.

The `def → AXIOM` substitution is the dangerous one. It is silent, and it
inverts the corpus's main hygiene check: `#print axioms` on anything reaching
those constants listed them as axioms. The "baseline" footprint I recorded in
PR #6851 —
`[propext, Classical.choice, Quot.sound, JonesMarkovCoefficient,
markovTraceOnWedderburn, partitions_as_finset, wenzlBridge]` — had four entries
that **do not exist in source**. I was comparing cache states and calling them
proofs.

## The repair, which is one command

`MarkovTrace.lean` also could not be recompiled at all: 21 "has already been
declared" errors. Not a source defect — a BFS over source imports finds no
cycle. The cause was a *second* stale olean: `JonesMarkovWenzl.olean`
(2026-07-02) still carried an `import QOU.HeckeAlgebra.MarkovTrace` that its
source dropped on 2026-08-26 (`22013eb256`). Rebuilding that one module:

    bash scripts/lean-direct-cone.sh QOU.HeckeAlgebra.JonesMarkovWenzl

made `MarkovTrace.lean` compile (exit 0), and **every** kind mismatch above
resolved: the 3 axiom-stubs became `def`s, the 5 absent theorems appeared,
`wenzlBridge` took its corrected `q_0` form, and its footprint became
`[propext, Classical.choice, Quot.sound]`.

## Scope — it is not the Hecke layer

`scripts/lean-olean-staleness-audit.py` (added here) measures it corpus-wide.
On this container, 2026-09-05:

- **2669** source modules
- **957** have an olean at all → **1712 have never been built**
- of those 957, **932 are stale** (olean older than the source's last commit)
- **25** are current — and **15** of those are ones this session built

So under 1 % of the corpus has a compiled artifact matching its source. Every
`lean`-direct "exit 0" outside that 1 % is a statement about a cache. This is
the same underlying condition as the known "Lean CI last ran 2026-04-25 and
failed; 37 modules silently stopped compiling", seen from the artifact side.

## Why the audit compares git dates, not mtimes

`git checkout` stamps every working-tree file with the checkout time, so in a
fresh clone all sources share one date and every restored olean reads as stale
— the audit would fire on all 2669 modules and mean nothing. The last-commit
date is a property of the content, so it survives cloning. Verified in this
container against `git log` for four modules before shipping. "No olean" is
reported as its own state, never as fresh.

## Not done

Rebuilding the other 931 stale modules. That is a long compute job with its own
failures to triage (the 37-module figure above suggests some will not build),
and it should be a deliberate campaign rather than a side effect of this change.
The audit makes the backlog visible and ranked; nothing here consumes it.
