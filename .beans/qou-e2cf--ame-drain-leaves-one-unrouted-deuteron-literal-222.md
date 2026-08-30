---
# qou-e2cf
title: AME drain leaves ONE unrouted deuteron literal, 2.22452, in 6 tables — 2.1e-5 from the registry, a reconciliation decision not a sweep
status: todo
type: task
created_at: 2026-08-30T03:26:28Z
updated_at: 2026-08-30T03:26:28Z
---


The TARGET class of the AME routing roadmap is drained: 109 literal sites in
53 files now read the registry, and `ame_registry_routing_triage.py` reports
TARGET 0/0 where it reported 109/53. Twenty-seven distinct spellings of four
binding energies collapsed onto four constants; the largest value move was
3.06e-6 relative (2.224573 -> 2.2245662).

WHAT THE DRAIN DELIBERATELY DID NOT TOUCH

One literal survives, and it is the same one every time: `2.22452` for the
deuteron. It is 2.08e-5 relative from AME_B_DEUTERON_MEV_VALIDATION
(2.2245662) -- four times the 5e-6 band the drain treats as "a rounding of
the canonical value". At that distance it is not a rounding, it is a
DIFFERENT NUMBER, and routing it would change a value on the strength of a
guess about where it came from.

It sits in six tables, in every case beside three siblings that DID route:

    delta_lambda_multi_atom_crosscheck.py:94       {'D': mpf('2.22452'), 'T': <reg>, '3He': <reg>, ...}
    rho_k_counit_defect_form.py:67                 same shape
    rho_k_counit_isotope_systematics.py:50         same shape
    deltalambda/..._extensivity_gap_synthesis_probe.py:56   {'D': 2.22452 (raw float64), 'T': <reg>, ...}
    deltalambda/..._binding_cross_isotope_probe.py:75       {"d": "2.22452", "t": <reg>, ...}
    probes/frobenius_gram_delta_lambda_probe.py:71          same shape

So the drain has left six tables that are three-quarters canonical and
one-quarter something else -- which is worse to read than six tables that
were uniformly stale, and is the reason this bean exists rather than a
comment in the diff.

Corpus-wide the literal appears in 55 .py files and 36 witnesses, so the
decision is bigger than these six sites.

THE DECISION TO MAKE (not made here -- it changes a value)
  a. `2.22452` is a stale evaluation (an older AME, or a 6-digit truncation)
     -> route all 55 files, re-run, accept the 2.1e-5 move.
  b. `2.22452` is pinned on purpose for a published comparison, the way
     option_e_canonical_reeb_v5.py pins its stale q0 with an ARCHIVAL note
     -> leave it and ADD that note, so the next drain does not re-ask.
Whoever answers this should say which, in the file, next to the literal.

