---
# qou-6q7q
title: 'Re-measure 3 in-scope paths after rebase: they moved on main while the sweep ran'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T13:37:53Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-trd0
---

## The claim that needs qualifying

PR #5519 says its verdicts are measured **on main**. The branch is behind
main, so that is true of the tree the sweep ran against, not of main today.
Measured rather than assumed: of the **111** in-scope paths (55 producers +
their witnesses), **108 are byte-identical to current `origin/main`** and their
verdicts transfer unchanged. **3 do not:**

| path | kind | moved on main by |
|---|---|---|
| `computations/audits/q0-anchor-consistency-audit.witness.json` | witness | `59b27bfc6d` |
| `computations/probes/binding_qgaussian_ell1_ceiling_measurement.py` | **producer** | `bc96793e5d` |
| `computations/probes/flavor_split_alpha_bond_dilog_probe.py` | **producer** | `bc96793e5d` |

This branch has **zero** commits touching any of the three — all three moved
under it.

## Why the two producers matter more than the count suggests

`bc96793e5d` is *"q0 literals: migrate the 5 unblocked sites"* — it changes
where those producers read q₀ from. That is exactly the class of change that
can move a staleness verdict, so these are not incidental drift: an
`UNCHANGED` measured against the pre-migration producer says nothing about the
migrated one.

## The cheap fix, enabled by the checkpointing

Do **not** rebase mid-sweep — it invalidates the run in flight. After the sweep
completes: rebase, delete just these three producers' entries from
`docs/audits/2026-08-23-q0-muon-staleness-sweep.json`, and re-run with
`--resume`. The other 52 are skipped, so re-measurement costs only what those
producers cost. Selective re-measurement is free precisely because verdicts are
now per-producer records rather than one end-of-run dump.

## Standing hazard

Main moves during a multi-hour sweep. Any verdict file should record the commit
it was measured at, so this comparison is mechanical next time rather than
reconstructed by hand. Related to `qou-cdjd` (the run records nothing about
what it ran against — there, the environment; here, the tree).

## Re-measured at main +98 (was +88): still exactly 3, the same 3

Ten further commits landed on `main` and the in-scope drift did **not** grow —
same three paths, same attribution. So the "108 of 111 transfer" figure is not
decaying commit-by-commit; the exposure is concentrated in the q0-literal
migration (`bc96793e5d`) rather than accumulating from ordinary traffic.

Worth re-running this check at rebase time rather than trusting it then — but
it means the sweep's currency is holding up better than the raw
commits-behind number (98) suggests. Commits-behind is the wrong metric here;
in-scope-paths-changed is the right one, and it is 3.


---

## Re-measured after the rebase — and 2 of the 3 were never in scope

Re-ran this bean's own check against current `origin/main`, post-rebase.

**The two producers this bean singles out are not in the sweep at all.**
`binding_qgaussian_ell1_ceiling_measurement` and
`flavor_split_alpha_bond_dilog_probe` do not appear **anywhere** in
`2026-08-23-q0-muon-staleness-sweep.json` — not in `results`, not in `skipped`,
which holds exactly one unrelated entry. The sweep is `measured: 47, total: 47`.

So this bean's sharpest argument —

> an UNCHANGED measured against the pre-migration producer says nothing about
> the migrated one

— **describes a verdict that does not exist.** There is no entry to invalidate
and nothing to re-measure for either. The prescribed fix ("delete just these
three producers' entries and re-run with `--resume`") is inapplicable to two of
the three for the simple reason that they have no entries.

**The cause is a set conflation.** The "111 in-scope paths" set is *producers in
the muon population and their witnesses*; the sweep measured a **different,
smaller** set of 47. Drift in the first set does not imply a stale verdict in
the second, and this bean treated them as the same set.

**Do not read my own re-run count as a comparable number either.** I recovered
94 paths from the sweep JSON's own keys; the bean counted 111 by a broader
definition. 94 vs 111 is two different denominators, not a shrinking set.

## What actually remains: one producer

| path | status |
|---|---|
| `computations/audits/q0-anchor-consistency-audit.witness.json` | **real** — differs from main; its producer *is* in `results`, verdict `SUBSTANTIVE` |
| `computations/probes/binding_qgaussian_ell1_ceiling_measurement.py` | not in the sweep — no verdict exists |
| `computations/probes/flavor_split_alpha_bond_dilog_probe.py` | not in the sweep — no verdict exists |

The rebase also absorbed the two producers' file-level drift (my branch now
carries main's versions), so even the tree-level difference this bean opened on
is gone for them.

One further path differs from main — `parabolic-cylinder-channel-mixing-probe.witness.json`
— which is **this branch's own commit** (`qou-ircb`), not drift.

So the re-measurement scope is **1 producer, not 3**, and it is running via the
`--resume` path this bean prescribed — which is the part of the plan that does
work, and the checkpointing is what makes it cost one producer instead of 47.


## The sweep's DENOMINATOR is not stable — 47 → 142 in one day

Re-running with `--resume` to re-measure the one genuinely-drifted producer did
something I did not expect: the record now reads **`measured: 55 / 142`**, not
`/ 47`. `--resume` is working correctly — it skipped the 46 retained entries —
but the **target set itself grew from 47 to 142**.

**Mechanism, read from the harness rather than guessed.** `targets()` scans
`computations/**/*.witness.json` at *run time* and selects on
`q0Anchor == "muon"` plus the muon value prefix. So the in-scope set is a
function of **how many witnesses currently carry a muon stamp** — not of how
much work exists.

**Attribution, verified on an instance rather than inferred.** One of the
newly-in-scope producers is `cross_check_trM_cw_seminormal_leg.py`; its witness
`cross-check-trM-cw-seminormal.witness.json` was last touched by
**`4101909790` — *"q0: label 229 witnesses from their own payload"***. Main
labelled 229 previously-unstamped witnesses; every muon one among them entered
this selector.

So the growth is not drift and not churn: **labelling work on main enlarges this
sweep's population by construction.** The better main gets at stamping, the more
this audit has to measure.

## This is the bean's own standing hazard, with a magnitude

This bean already says:

> Main moves during a multi-hour sweep. Any verdict file should record the
> commit it was measured at, so this comparison is mechanical next time rather
> than reconstructed by hand.

That is exactly right, and now has a number against it: **the denominator moved
47 → 142 in a single day.** Two consequences worth stating plainly:

1. **"47 / 47 measured" was only ever true relative to one tree.** It is not a
   completion figure and must not be quoted as one. The same applies to any
   percentage derived from it.
2. **A verdict file needs its `tree_commit` beside its counts, not just in the
   environment block.** The sweep does record `environment.tree_commit` — good —
   but the *tally* does not carry it, so a reader comparing two tallies has no
   way to see they were computed over different populations.

## Status

The re-run is left going: it is checkpointed per producer, so nothing is lost if
it dies, and the partial record self-describes with `partial: true`. It will hit
the four confirmed long producers from `qou-uz7q` and burn a timeout on each;
that is expected, not a fault.


## RESOLVED — the one real path re-measures `UNCHANGED`

`--resume` re-measured `computations/audits/q0_anchor_consistency_audit.py`:
**verdict `UNCHANGED`, no `changed_fields`.** The committed witness reproduces
exactly when the producer is re-run on this tree, so there is no stale verdict
to correct. Combined with the scope correction above (the other two paths were
never in the sweep), **this bean's re-measurement work is done: 1 path, and it
came back clean.**

**I expected the opposite and said so.** My stated expectation was that it would
move again, since its prior verdict was `SUBSTANTIVE` with `Q0_OK 669 → 695` and
main has been landing q0 labelling work all session. It did not. The rebase is
why: it brought main's regenerated copy, so the committed artifact was already
current for this tree.

## The file still differs from main — and that is NOT staleness

`q0-anchor-consistency-audit.witness.json` differs from `origin/main`:

| count | main | mine | delta |
|---|---|---|---|
| `Q0_OK` | 953 | 947 | **−6** |
| `Q0_ANCHOR_MISSING` | 1645 | 1644 | −1 |

**My first explanation was wrong and is retracted.** I assumed this was my own
`parabolic_cylinder` stamp change (muon → proton) shifting the counts. That
accounts for **at most 1**, not 7.

The actual cause: **this branch is 79 commits behind main**, and main has kept
labelling witnesses throughout. `Q0_OK` being *higher* on main is the signature —
main has stamped ~6 more since my rebase point. My copy is correct **for my
tree**; main's is correct for **its** tree; both reproduce where they live, which
is exactly what `UNCHANGED` reports.

**Second independent illustration of the population point**, from the opposite
direction to the 47 → 142 finding: comparing counts across two trees without
naming the tree is meaningless, and here it would have produced a false
staleness report. That is precisely why `tree_commit` now sits beside the tally
(`75a0dce00d`).

## Sweep status

Left at **62 / 142, `partial: true`** — my outer `timeout 900` killed it, not a
fault. Checkpointed, so `--resume` continues from there. Its `TIMEOUT` count has
reached **7**, one beyond `qou-uz7q`'s six; per that bean's result a `TIMEOUT`
verdict is not evidence of a slow producer, so the seventh needs the same
measurement before anyone treats it as one.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8396, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
