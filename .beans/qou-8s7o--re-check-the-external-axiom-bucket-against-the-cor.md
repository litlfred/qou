---
# qou-8s7o
title: Re-check the External axiom bucket against the corpus, not against docstrings (57 entries)
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T01:10:32Z
updated_at: 2026-08-26T02:59:53Z
---

Generalization of qou-mame (PR #5807).

docs/audits/2026-06-03-lean-axiom-tractability-triage.md sorts 58 axioms into an 'External / cited / deep' bucket described as 'not a feasible session-scale goal'. That bucket was populated by READING EACH AXIOM'S OWN DOCSTRING.

One entry has now been checked against the corpus instead: lobachevsky_pi_div_four_eq_half_catalan, an 'External transcendental identity', proved sorry-free in ~20 lines using QOU.Knot.clausen_eq_series which was already in the tree. Its docstring's claim ('needs Mathlib's full polylogarithm machinery ... none of which is currently upstream') was false in both halves and had survived at least two revisits.

Sample of 1, so the base rate is unknown -- but the SELECTION was not adversarial (it was picked because a user directive pointed at it), which is weak evidence the bucket is not uniformly correct.

Method that worked, for whoever takes this:
1. For each axiom, extract the mathematical ingredients its docstring names as missing.
2. grep the corpus for each: content/**/*.lean (QOU/MathlibExt/ is a 54-file Mathlib-gap staging area), then the .lake mathlib OLEANS by symbol name (strings -n 6 on the .olean; the SOURCE tree is not present in a restored container, only oleans).
3. Never conclude 'absent' from one import cone. That is the error this bean exists to catch.
