---
# qou-pdgc
title: 'The Hecke oleans were 3 months stale: 3 defs read as AXIOMS and wenzlBridge carried a retracted form'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T17:29:43Z
updated_at: 2026-11-21T15:20:53Z
parent: qou-5vkl
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

## Partial drain, 2026-09-05 — 798 modules attempted, 798 ok

Ran `scripts/lean-direct-cone.sh --all -k -j3` for ~1h40m. Report preserved at
`docs/audits/2026-09-05-lean-corpus-build-survey.tsv`.

| | |
|---|---|
| attempted | **798** of 2669 (30 %) |
| `ok` | **798** |
| errors | **0** |
| `blocked` | 0 |

**Stopped deliberately, not by failure.** The rate fell from ~7 modules/min to
~1.6/min as it moved into heavier modules — extrapolating, the remaining 1871
would take 20+ hours, which is not a sensible way to confirm what 798
consecutive passes already indicate, especially while it was blocking a
higher-value check (`qou-yos9`).

## The sample is biased, and the bias runs the wrong way for the conclusion

`lean_cone_build.py` walks in **topological order**, so the first 798 are the
**shallowest** modules — fewest QOU dependencies. Confirmed by the head of the
report: it starts `QOU.scratch_matrix`, `QOU.qou_canonical_action`,
`QOU.variational_equations`, which are alphabetically last, so this is dependency
order and not a name sweep. Deep modules have strictly more ways to fail, and the
corpus's known "37 modules silently stopped compiling" (from the 2026-04-25 CI
failure) concerns exactly the kind of module not yet reached — nothing under
`QOU/Mathlib/Schensted*` was touched, for instance.

**So this does not license "the corpus compiles".** What it licenses is narrower
and still useful:

- For the shallowest 30 %, the never-built and stale populations measured in
  `qou-pdgc` are a **cold cache**, not broken files. Zero of 798 was a source
  defect.
- The falsifier set when this started — "near-100 % ok means it is compute, not
  repair; stop rather than burn hours" — fired in that direction for this slice,
  and the run was stopped on it as planned.
- A full answer needs the remaining 1871, and specifically the deep ones. That is
  a compute campaign, still not consumed here.

## What the drain did buy, beyond the number

Rebuilding oleans in dependency order repaired the class of defect this bean was
opened for. 15 modules were already refreshed by targeted cone runs earlier in the
session; this added ~780 more. Any `#print axioms` taken against those now reads
source rather than a months-old cache.

## Surfaced at session start (2026-09-06)

A measurement nobody reads is the same defect this bean documents, one level up —
the same reasoning `AGENTS.md` gives for the CI-health watchdog ("a report is only
read by someone in the room"). `scripts/session-start-coord-sweep.sh` now prints
the five stalest modules and the repair command, with the "could not run" case
rendered explicitly as **not a pass**.

Freshness at the time of writing: **616** stale, down from 932 when this bean was
opened — the difference is what the partial drain and the targeted builds have
repaired.

## Targeted deep-tail pass (2026-09-06) — and a classifier that lied twice

The shallow sweep answered "does it compile" for the easiest 30 %. The deep tail
needs the opposite ranking, so `lean-olean-staleness-audit.py --targets N` now
lists **never-built modules by reverse in-degree**: a leaf that fails breaks one
module, one of these breaks everything above it. Direct in-degree deliberately,
not transitive — a transitive closure ranks a few near-universal utilities above
everything else and says nothing useful.

At the time of writing: **1187 never built, 700 imported by at least one other,
487 leaves.** The top of the ranking was built directly; each target's cone
overlaps the next, so 40 targets cover far more than 40 modules.

**Result so far: no source defect found.** Every settled target came back ok.

**Worth recording: my own result classifier was wrong in both directions.** It
labelled `QOU.MathlibExt.FaddeevQuantumDilogarithm` **FAILED** — in-degree 7,
zero QOU dependencies, exactly the profile the targeting was built to catch, so
it read as the finding. It was not. The cone printed `done: up-to-date=1 in 0s`,
with no `ok=` and no `err=`, and my grep required `ok=`; the module had already
been built by an earlier target's cone in the same loop. In the other direction
it labelled `BlochWignerLobachevsky` ok off a progress line whose `done:` was cut
by a 160-character truncation.

Reclassifying from the raw output rather than the label gives 6/6 ok. The general
point is the one `AGENTS.md` makes about not taking agent output at face value,
and it applies to one's own scripts: a status column is a claim, the captured
output is the evidence.

## Completed 2026-09-06 — subject fixed, remainder handed to `qou-8jjo`

This bean's titled subject is resolved: `MarkovTrace.olean` was rebuilt, the three
axiom-stubs became `def`s, the five absent theorems appeared, `wenzlBridge` took
its corrected `q_0` form, and every footprint in that layer now reads source
rather than a months-old cache. Three tools came out of it — the staleness audit,
the `--targets` ranking, and the session-start freshness line.

**Final measurement of the deep-tail probe: 40 of 40 targets built, zero source
defects.** Cones covered 98 modules; top reverse in-degree fell 9 → 4; never-built
1187 → 1089. Across ~840 modules attempted this session (798 shallow + the
targeted pass) **no module failed to compile.**

All five `FAILED` labels in the targeted pass were one classifier bug, not five
findings: `done: up-to-date=N in 0s` has neither `ok=` nor `err=`, and the grep
required `ok=`. Ground truth — does the olean exist — says all 40 built.

The remaining 1089 never-built modules are a standing condition rather than this
bean's task, and are carried by `qou-8jjo` with the method and the do-not-do
(no more `--all` sweeps).

2026-11-21 (lean-build-red drain, issue #8817): closed. Body already records it as completed on 2026-09-06; the rest is carried by qou-8jjo. Today's full QOU lean-direct sweep found no red outside the QOU.lean root, which PR #8878 fixed.
