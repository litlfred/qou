---
# qou-kjik
title: strong_unified_binding_probe inverts all three AME anchors and its verdict claims 1ppq; mba-step09b cites it as where B_unified lives
status: todo
type: bug
priority: normal
created_at: 2026-09-19T06:32:38Z
updated_at: 2026-11-20T09:55:00Z
---


## Found while scoping `tbl:unified-iterative-correction-table-data` (bean `qou-ypq6`, PR #7439)

Hunting that table's producer, the one live lead was
`content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step09b-per-isotope-binding.md:44-48`,
a correction landed 2026-08-25 (PR #5765):

> `computations.mass_binding_dashboard._row` ... has ZERO occurrences of
> `B_unified` -- the `B_unified` model lives in
> `computations/probes/strong_unified_binding_probe.py`, which emits no witness.

That correction is right that the old pointer was wrong. What it points at
instead is a **different object**, and reading it is the finding.

## The probe's accuracy is an arithmetic identity, not a result

`computations/probes/strong_unified_binding_probe.py` (55 lines, last touched
2026-09-04). Lines 29-32 solve all three weights out of the AME table it is
then scored against:

```python
w_2 = AME_B["D"] / (M_E * a_D(2))
B_3_avg = (AME_B["T"] + AME_B["3He"]) / 2
w_3 = (B_3_avg - M_E * a_D(2) * w_2) / (M_E * a_D(3))
w_4 = (AME_B["4He"] - M_E * (a_D(2) * w_2 + a_D(3) * w_3)) / (M_E * a_D(4))
```

Substituting back into the scoring loop (lines 41-46):

| row | `B_unified` | `err` |
|---|---|---|
| D (A=2) | `= AME_B["D"]` identically | **0 by construction** |
| T, 3He (A=3) | `= B_3_avg` identically | `+/-` half the T-3He split, by construction |
| 4He (A=4) | `= AME_B["4He"]` identically | **0 by construction** |

Three free parameters solved against four data points. The source says so in
its own words -- *"We reverse-evaluate the required sequence to show the exact
scale rule closure"* -- and then the verdict block (lines 49-52) says the
opposite:

> The mass gaps are completely closed. ... to yield 1ppq accuracy for the
> strong sector.

There is no closure and no 1 ppQ. There is `x - x = 0`.

## The two "derived" inputs the verdict credits are never used

`na_stokes_gluonic = 3` and `na_stokes_residual = 2.5` are assigned at lines
20-21, printed at 23-24, and **appear nowhere else in the file**. They do not
enter `w_2`/`w_3`/`w_4` and they do not enter `B_unified`. The verdict
attributes the closure to them specifically ("the exact NA-Stokes generating
function anchors (3 and 2.5) feed the q-difference recursion"). They feed
nothing. Decorative provenance on a tautology is worse than no provenance:
it makes the fit look derived.

## Two smaller defects in the same file

- `mp.mpf(2.5)` (line 21) is `mpf(<float literal>)`, one of the three
  source-level gates in `scripts/precision-gates.sh`. Cosmetic here only
  because the value is never consumed.
- `import json` (line 5) is unused.

## Why this is not the UIC table's producer either

Confirms the `qou-ypq6` negative from the other side. This object is not
`tbl:unified-iterative-correction-table-data`'s:

- **Its D row is 2.2246 MeV (= AME) by construction; the table's D row is
  `-16.45`.** Not a discrepancy to reconcile -- opposite constructions.
- It spans **four** atoms (D, T, 3He, 4He); the table has **seven**
  (D, 4He, 14C, 20Ne, 28Si, 40Ca, 208Pb) and none of T / 3He.
- It has no `B_dedi` column and no per-lambda sum.

So `qou-ypq6` stays open and unaffected; this is a sibling finding, not its
answer.

## What is open, and what is NOT being proposed

Open: (1) whether `mba-step09b`'s Python-API pointer should name this probe at
all, given it is a fit; (2) whether the probe should carry a banner saying its
`err` column is identically zero by construction, or be retired.

**Not proposed here:** deleting or rewriting the probe. Under the 2026-09-07
ASK-THE-OWNER directive this is neither exemption -- it does not increase
precision and the corpus does not already fix the answer -- and
`mba-step09b` sits under the mandatory appendix-sync rule, so an edit there
is a contract change. Measured and recorded; the change is the owner's call.

An honest negative result is worth keeping. The defect is the **verdict text**
and the **citation**, not the existence of an anchor-inversion experiment.

## Ported to the authoritative store 2026-11-20, and re-verified before porting

This bean existed only on the branch of PR #7439, which was closed on 2026-11-15
during the cleanup of PRs left by idle sessions -- its closing comment gives the
reason ("it edits content/ files that have since moved") and invites exactly this:
"If beans qou-5eg1, kjik and tv74 are still wanted, they can be ported to
beans/defs/ separately." The bean store is now the branch-mounted
`cat/cat-harness/beans`, which is gitignored on main, so this is a store write
rather than a repo commit.

Paths in the body above predate the `content/` -> `folio/` tree rename
(2026-09-27) and the `.beans/` -> `beans/defs/` move; read `content/...` as
`folio/...`. The findings themselves were re-checked against main at
`cacbddcffb1` and hold.

The two owner-selected fixes this bean carried are re-landed in
https://github.com/litlfred/qou/pull/8560.

**Re-verified 2026-11-20 against main `cacbddcffb1`**, on a file byte-identical
to the one originally read: `w_2` at `:29`, `B_3_avg`/`w_3` at `:30-31`, `w_4`
at `:32`, the "reverse-evaluate the required sequence" comment at `:26-28`,
`na_stokes_gluonic`/`na_stokes_residual` assigned at `:19-20` and printed at
`:23-24` and occurring nowhere else, **0** importers, **0** occurrences of
`witness`. The banner and the `mba-step09b` re-correction are in #8560; the
probe's code is deliberately untouched.

**Stays open** per rule 13a: whether the appendix should point somewhere else
entirely is unresolved, and nobody has established what it *should* name.
