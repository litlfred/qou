---
# qou-o0pa
title: 'nucleon_h3_marshalling_divergence_probe fails on main: the grouped pin is inverted AND its two arms now confound d-dropping with ordering'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T08:35:25Z
updated_at: 2026-10-04T15:15:46Z
parent: qou-9nnz
---

Found while adding a deliberate/actionable split to
`audits/self_built_braid_word_audit.py`. I attempted the fix, it half-worked,
and the half that failed is the interesting part — so this is reported, not
repaired.

## 1. The pin is inverted (certain)

`nucleon_h3_marshalling_divergence_probe.py` pins its marshalled arm with
`intra_order="grouped"` (added 2026-09-06, bean `qou-y2o7`), reasoning that the
borromean default "would swing `marshalled` to 0.629/0.475 against a
1.146/0.988 target".

**That target no longer exists.** `habiro/habiro-coefficients-atomic.witness.json`
was regenerated to the canonical ordering in **`a4909014a5`** — the SAME
option-B commit the pin was reacting to. Measured against the live target:

    p  grouped    1.14575969245730087    rel 0.821
    p  borromean  0.629328402202921918   rel 6.37e-51
    n  grouped    0.987743688115809572   rel 1.08
    n  borromean  0.475133517155682213   rel 2.39e-50

So the pin makes the probe compare GROUPED against a CANONICAL target, and it
**fails its own assertions on `main`** ("3 assertions, FAILURES"). Reproduced
with `origin/main`'s own copy of the probe — this is not branch-local.

## 2. Removing the pin is NOT sufficient — the arms are confounded

I removed it. The marshalled arm then matches to **1e-51**, and the probe
**still fails**, because the *other* arm now diverges:

    d-preserving  1.14575969245730087   rel vs habiro = 0.821

The d-preserving arm traces `chain`, built at line 140 as
`[(c,d,0) for ... g0] + [(c,d,1) for ... g1]` — GROUPED — through the
monotone-only `T.chi_all_lambda`. So after unpinning, one arm is canonical and
the other grouped.

**That is worse than it looks.** The probe's subject is whether dropping `d`
changes the trace, which requires both arms to share a word and differ only in
`d`. Grouped-vs-borromean across the two arms confounds `d`-dropping with
ordering, so neither the pinned nor the unpinned state measures what the probe
claims to.

A real fix rebuilds `chain` in borromean order so both arms share it — a
substantive change to what the probe computes, on a sibling's regression guard,
which is why I reverted rather than shipping it.

## A wrong claim I nearly shipped

My unpinning commit carried a comment saying `chain` is "unrelated to the intra
ORDER". That is false — the chain IS that arm's ordering, and it is exactly why
the probe still failed. Caught by running it rather than by reading the diff.

## Detector status

`self_built_braid_word_audit` reports this site **ACTIONABLE 1**, which is
correct: it is an undeclared grouped word whose guard is broken, not a
deliberate historical choice. I deliberately did NOT mark it deliberate — the
marker would have silenced a real defect.

## REBUILT — both arms canonical, 3/3 assertions pass (2026-09-07)

Both defects fixed:

1. **The inverted pin** removed. `compute_tau_M_nucleon_H3` now called at its
   default, which matches the live target to 6.37e-51 (p) / 2.39e-50 (n).
2. **The ordering confound** fixed. `chain` now comes from
   `atom_braid_word_3A` instead of being hand-built grouped. Measured safe:
   same 11 crossings, identical `(c, d)` multiset, **identical census**
   (p `{sigma:6, averaged:2, sigma_inv:3}`, n `{sigma:5, averaged:2,
   sigma_inv:4}`) — only the ORDER differs. Traced through
   `chi_all_lambda_any`, since the monotone-only kernel refuses the canonical
   word outright.

`self_built_braid_word_audit` now reports **ACTIONABLE 0, DELIBERATE 0** — and
by the site becoming genuinely canonical, not by declaring it deliberate.

## STILL OPEN: the probe is weaker than its title

Both arms are now the SAME computation, because `qou-qu2w` removed the
marshalling from `compute_tau_M_nucleon_H3`. The "marshalled" arm no longer
marshals, so the divergence in the title cannot be detected by it.

**That vacuity is not from this rebuild.** It arrived with `qou-qu2w`, and a
sibling had already re-pointed the assertions on 2026-09-06 from "assert the
defect (== 2.157)" to "assert the fix holds" for exactly that reason. What was
broken — and is now fixed — was the ordering confound on top of it.

**What restoring a real guard needs.** Marshal explicitly through
`marshal_to_chi_lambda_braid` rather than through a helper that no longer does.
It IS still callable on the canonical word (returns 11 pairs). The obstacle is
a convention mismatch: it emits `(sign, gen)`, this probe uses `(c, d, gen)`,
and my first bridge attempt produced `unsupported crossing c=-1.0 at gen=2`.
Resolving that is a small piece of work with a real trap — guessing at another
module's convention inside a regression guard is how a probe ends up asserting
something it does not measure — so it is left for someone who can check the
marshaller's contract rather than infer it.

Left OPEN for that reason.

## GUARD RESTORED — 5/5, and my "vacuous" claim was overstated

I said restoring a real marshalled arm needed "someone who can check the
marshaller's contract rather than infer it". That was checkable by reading its
source, so I read it. The contract is explicit:

    marshal_to_chi_lambda_braid -> [(sign, gen_1based)]
        FOR hecke_characters.chi_lambda_braid, NOT for chi_all_lambda*

Feeding it to the wrong kernel is what produced `unsupported crossing c=-1.0`
on my first attempt. With the right consumer and `precision="mpfr_50dps"` it
works, and the loss is real:

    p  d-preserving 0.629328402202921918   MARSHALLED 0.807031394861838756  ratio 1.28237
    n  d-preserving 0.475133517155682213   MARSHALLED 0.535061853071076283  ratio 1.12613

Added as a THIRD arm, additively. **5 assertions, all passed.**

## Correcting myself

I described the probe as "weaker than its title" and "a tautology" once
production stopped marshalling. That overstates it. The production-agreement
check IS a real regression guard — `compute_tau_M_nucleon_H3` could be
re-pointed back through the lossy path, and then it fires. What it could not do
is MEASURE the loss. Those are different deficiencies and I conflated them.

The three arms now guard three separate things, all on the same canonical word:

  * d-preserving       -> reproduces the habiro target (~1e-50)
  * marshalled current -> production's ROUTING has not regressed
  * marshalled explicit-> the marshaller is STILL lossy (0.282 p / 0.126 n)

The last one is new and is what makes the title honest again. A collapse toward
0 would mean the marshaller stopped dropping `d`; a large jump would mean the
crossing census changed.
