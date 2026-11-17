---
# qou-adwi
title: Corpus has TWO incompatible Planck lengths (factor t_P ~ 10.1); the Lean hardened a prose '~' into '='
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-09T11:10:54Z
updated_at: 2026-10-04T15:15:38Z
parent: qou-10v9
---


Branch: claude/anchor-followups-2026-08-08. Found by the length/metric corpus
sweep, 2026-08-09. Nobody had flagged it.

## The contradiction

    information-theory/discrete-planck-step.md:39-43
        ell_P(q) = hbar_q * t_P = (1 - q^-1) * q/(q-1) = 1
        "The Planck length identically evaluates to 1 over any field."

    information-theory/planck-info-unit.md:1        ell_P(p) ~ hbar_q    ~ 0.0991
    fluid-dynamics/planck-reynolds.md:1             ell_q = (q-1)/q      ~ 0.0991
    fluid-dynamics/p5-counterexample.md:4           separation d measured in units of ell_q

    lean/QOU/InformationTheory.lean:32-34
        localPlanckLength := quantumPlanckConstant       (i.e. = hbar_q EXACTLY)

They differ by a factor t_P = q/(q-1) ~ 10.1 at q0.

## Two separate problems

1. WHICH IS THE PLANCK LENGTH? One chapter says it is identically 1 over any
   field; three other places say it is hbar_q ~ 0.0991. Both cannot be the
   framework's ell_P. Note the "=1" version is an angular Reeb displacement --
   planck-time-interpretation.md calls it exactly that -- so it may be a phase
   rather than a length, in which case the naming is the bug and the two objects
   are different quantities wearing one symbol.

2. THE LEAN HARDENED A PROSE APPROXIMATION. planck-info-unit.md writes
   "ell_P(p) ~ hbar_q" with a TILDE. InformationTheory.lean:32-34 defines
   `localPlanckLength := quantumPlanckConstant`, an EQUALITY. A "~" in prose
   became a definitional "=" in machine-checked content. Anything downstream of
   `localPlanckLength` now silently carries that strengthening.

## Why it is load-bearing right now

Bean qou-mumr (and my session note) cited the "=1" and "(q-1)/q" values in
adjacent paragraphs as if they agreed, and built an argument about computational
distance on top. Corrected there. Any future attempt to convert a framework
length to fm -- the nuclear-radius line, qou-usft -- has to pick one of these
first, and the two differ by an order of magnitude.

## Do not "fix" by picking the convenient one

The right resolution is to determine whether these are the SAME quantity
(one of them wrong) or DIFFERENT quantities (an angular displacement and a
length sharing a symbol). Only then rename or correct. Adjudicating by which
value makes a downstream number work would be exactly the move this corpus
forbids.

## Progress Update (PR litlfred/qou#8231)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8231 (`513987e80ae041a6d8bc835ffbdda5371ccac289`, scriptCommitSha `9bd895c1b028c3d1abf67e3de52aeade9e9e5ccc`)
- **Summary**: Added `unit_product_vs_bare_step_ratio`, `deep_quantum_field_gt_one`, and `deep_quantum_contradicts_classical` in `QOU/InformationTheory.lean`, verified by 80-dps mpmath probe `hyperbolic_planck_oneloop_qint_dilog_probe.py` (`scriptHash: 83d59661279d`).
