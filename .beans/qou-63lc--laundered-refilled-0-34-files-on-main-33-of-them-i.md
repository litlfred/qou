---
# qou-63lc
title: LAUNDERED refilled 0 -> 34 files on main, 33 of them in the last 3 days
status: todo
type: bug
created_at: 2026-09-03T04:20:34Z
updated_at: 2026-09-03T04:20:34Z
---


## The measurement

`computations/f64_into_mpmath_audit.py` on `origin/main` (2026-09-03):

    LAUNDERED — mpf(str(<f64>)): 34 file(s), 38 site(s). These are defects.

**It was ZERO earlier the same day.** The last site
(`em_selfenergy_coupling_target_probe.py:65`) was drained in `01de469085`,
merged to main in #6282 (`e2f6a1a76d`), and the audit printed
`LAUNDERED — none.` immediately after.

### When the 34 arrived

    first-added date    files
    2026-08-01              1
    2026-08-31             16
    2026-09-01             13
    2026-09-02              4

**33 of 34 landed in the last three days.** 23 of 34 are in
`computations/probes/`.

### Verified real, not a detector artifact

Checked a sample by hand rather than trusting the count — twice today a
detector in this repo has mis-fired on me:

    computations/probes/adding_crossings_cannot_break_the_degeneracy_probe.py:127
        mp.mp.dps = 40
        _Q = mp.mpf(str(Q0))

    constants.Q  = 1.1099785827513808   <class 'float'>
    mpf(str(Q))  = 1.1099785827513808              17 real digits
    q_at(40)     = 1.109978582751380807591669095610768879874

At `dps = 40` that is **23 fabricated zeros** presented as significant. The fix
is one line at the import — `q_at(mp.dps)` — exactly as in `01de469085`.

### Why this is the specific pattern a standing directive exists for

AGENTS.md §"PROBES ARE NOT EXEMPT" (STRICT, **owner directive 2026-08-18**):

> A probe is a `computations/` script and is covered by every gate above. The
> reasoning *"no witness by design, so precision does not matter"* is **wrong
> and is banned** — it inverts the actual risk. A witness is a number that gets
> re-derived; a probe conclusion is an **argument** that gets written into a
> bean, an audit doc, a PR body and a content block, where nothing re-derives
> it.

That directive's own history: *"added 2026-08-18 after an agent shipped eight
probes on the L2 binding axis with `float(G.h)`"*. The new files are named
`all_pairs_bonds_and_saturation_probe`, `binding_lp_with_inter_nucleon_bonds_probe`,
`four_body_term_and_the_h12_collapse_probe`, `isospin_grading_restores_the_sign_probe`
— **the binding axis again, two weeks later.**

### Scope and what is NOT claimed

- **NOT** claimed that any probe's *conclusion* is wrong. Whether a given
  conclusion moves under exact arithmetic is per-file and untested here.
- **NOT** fixed. 34 files is a sweep, not a ride-along on an unrelated PR.
- The one-line fix is known and mechanical; what it needs is an owner deciding
  whether to sweep, and someone re-running each probe afterwards to see whether
  any conclusion moves.

### How it was found

Incidentally, running `precision-gates.sh --changed` as the pre-commit preflight
on an unrelated `qou-cds1` commit. The gate is doing its job; nothing on my
branch is implicated (neither new file appears in any red section). Worth noting
that the gate is `workflow_dispatch`-only per the 2026-06-30 Actions directive,
so **nothing runs it on a push** — these 34 landed without it firing once.
