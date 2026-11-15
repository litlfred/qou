---
# qou-6gdb
title: raw-float64 in docs/audits/2026-08-26-kernel-defeq-sample.witness.json (2 coverage pcts) — takes the audits-tree ratchet red; not my domain
status: scrapped
type: task
priority: normal
created_at: 2026-08-28T15:50:41Z
updated_at: 2026-08-28T19:05:12Z
---

## What and where

`docs/audits/2026-08-26-kernel-defeq-sample.witness.json` carries two raw
float64 fields:

    /coverage/coverage_of_tree_pct           = 2.3
    /coverage/coverage_of_olean_reachable_pct = 2.5

This is the single NEW-dirty entry taking the **audits-tree raw-float64**
gate red (`witnesses carrying raw float64: 33`, baseline 32). Surfaced by
running `scripts/precision-gates.sh --changed` as the mandated preflight on
an unrelated PR.

## Ownership, and why I did not fix it

Landed with the `qou-0avp` olean-coverage arc (`cdbdc84af` /
`f991249ee`), 2026-08-26. Not my domain -- the HOMFLY branch that found it
touches nothing in that cone. Fixing it means editing that producer, and
**the witness does not record `scriptFile`**, so the producer would have to
be identified first (a second, smaller defect worth fixing at the same time).

## Assessment, stated plainly

Benign in effect: both values are coverage *percentages* -- ratios of olean
counts reported to one decimal -- not physics quantities, and nothing
downstream re-derives them. But the gate is a **ratchet**, and the discipline
is explicit that a baseline drains and never grows. So this should be fixed
at the producer (`mpmath.mpf` from the source, serialize with
`_precision.fmt`), NOT baselined.

Cheap, once the producer is located.


## SCRAPPED — a sibling landed it first, and better. I duplicated their work.

`qou-f64d` fixed this on `main` in `1d52355b9b` while I was fixing it on a
branch. Their version is on main; mine is dropped unmerged.

**Theirs is better, not merely first.** Both of us reached the same diagnosis
independently — the coverage block is hand-authored, `audit-driver.sh` emits
neither field, so there is no producer to fix and the file IS the source. But
on what to write back:

    mine    "2.3"            the rounded value, preserved
    theirs  "2.3482498892"   the exact ratio 53/2257, at 10 places

plus a `_derived_note` in the witness itself recording that both fields are
derived from `modules_scanned` / `qou_modules_total` / `qou_modules_with_olean`,
that no measurement changed, and that the prose's "2.3 %" stays the correct
rounded reading. Mine preserved a lossy presentation; theirs preserves the
ratio and explains itself in the file, where the next reader will actually be.

## The process failure, which is the part worth keeping

**This was mechanical work, and mechanical work has ONE owner.** AGENTS.md is
explicit that the parallel-exploration relaxation covers *open-outcome
research* — an unsolved question where a second route may win — and NOT work
that is merely not-yet-typed. Draining a ratchet is the second kind: one right
answer, one owner.

I had checked for a sibling before starting on the Lean `Knot/` front and
correctly stood down there. I did not run the same check before picking up a
red gate, because a red gate felt like unowned infrastructure rather than
someone's front. It wasn't: `qou-f64d` was already open on it, and
`1224f5e026` ("main is RED on audits-tree raw-float64 — provenance
established, not this branch's") was their in-flight record of exactly the
ownership question I spent a pass re-establishing.

**The check that would have caught it** is the corpus-grep checklist's
`.beans/` path — `grep -rl <topic> .beans/` — which I ran for the *subject*
(kernel-defeq, coverage pct) and which returned only my own bean, because
theirs was still on a branch. What I did not do is look at recent `main`
landings and open sibling branches for the same *symptom*. For a gate that is
red on main right now, that is the higher-yield check: a live red is visible
to every agent running the preflight, so the prior is that someone is already
on it.

## What survives

Nothing to merge. The gate is green on main via their fix. My y_lambda
import-time-dps fix (`ad65db8d49`, PR #5898) is unaffected and is what main
carries — the sibling bean `qou-stlw` records that same finding but landed
only an audit doc, so the two did not collide.
