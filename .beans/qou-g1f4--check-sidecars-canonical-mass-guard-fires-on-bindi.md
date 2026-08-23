---
# qou-g1f4
title: check-sidecars canonical-mass guard fires on binding_hbarq_rung_forward_test.py (pre-existing on main)
status: todo
type: bug
priority: normal
created_at: 2026-08-23T19:53:43Z
updated_at: 2026-08-23T19:54:40Z
---

scripts/check-sidecars.sh reports:

    canonical-mass status guard: 1 possible deprecated m_p-status citation(s):
      computations/binding_hbarq_rung_forward_test.py:30:
        mass:  m_p/(m_e*Vol(B_3)) = rho_p/hbar_q^2  ~= 258
               (rho_p = linking_weight ~= 2.53, O(1))

PRE-EXISTING, NOT MINE. `git diff origin/main...HEAD` for that file is empty;
it landed in 137e6161d8 "probe(binding): hbar_q-rung forward test -- re-scopes
Lane 2". Recorded rather than fixed because it is out of scope for the branch
that found it (frakv-fibre-workplan) and the right disposition is a judgement
call, not a mechanical edit.

TWO POSSIBLE DISPOSITIONS, and someone who knows the probe should pick:

 1. ALLOWLIST. The line is arguably a legitimate deprecation mention -- it
    writes m_p/(m_e*Vol(B_3)) explicitly as the Vol(B_3)*rho FORM, which is
    exactly the deprecated shape the guard exists to catch, and the probe's
    point is to re-scope Lane 2 rather than to assert a live m_p. If so, add
    the substring to ALLOWLIST_SUBSTR in check-sidecars.sh.
 2. RE-WORD. If the line reads as a live status claim rather than a named
    deprecated form, route it through the canonical_mass facade or mark it
    historical.

WHY IT MATTERS EITHER WAY: while it fires, check-sidecars.sh exits with
"action needed" on EVERY branch that touches anything, so every agent running
the documented pre-commit preflight sees a red they did not cause and must
re-verify by hand that it is not theirs. I did exactly that today. A guard
that cries wolf on every run is the mechanism by which a real hit gets waved
through.
