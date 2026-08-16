---
# qou-cuur
title: 'Task-0 audit: no inverted-CODATA value is wired to production; 3 labelling defects + AGENTS.md lambda_A wording'
status: todo
type: task
created_at: 2026-08-16T13:40:48Z
updated_at: 2026-08-16T13:40:48Z
---

Owner directive 2026-08-16: "Delta_lambda from inverted CODATA = NOT ALLOWED",
"it should be excise from production". Audit run on PR #5241. Full writeup:
docs/audits/2026-08-16-colour-level-and-tln-compute.md (TASK 0).

RESULT: **nothing to excise.** No experiment-inverted value is wired to
production as canonical. Traced by CONSUMPTION from the production set (the
definition in .claude/skills/local/production-vs-exploratory-discipline.md),
not by name-matching. Did NOT use the circ-anchor-inverted-roundtrip detector
(bean qou-yfsp measured it ~83% false positive).

The two sites that looked like production wirings and are not:

  1. qbeta-ck-cache.witness.json -> per_observable_100x_status.py (the 100x
     dashboard, genuinely production). The cache IS CODATA-inverted:
     qbeta_utils.c3_target_at is literally (q_codata/Q_N2 - 1)/u**3. But the
     dashboard breaks at the first non-derived tier
     (per_observable_100x_status.py:463-475). Verified the witness rows rather
     than trusting the code: k=2 tier=derived/lean-proved, k=3
     tier=cal-anchored. The inverted c_3 is never read. FIREWALLED.
  2. The fitted Habiro tower (1+46u^4)(1+4u^5)(1-29u^6) still has a live
     definition in m_p_substrate_identity_50dps.py:194-205 (a *_50dps.py file,
     i.e. the production family) with 4 and 29 still hardcoded. But
     habiro_ratio_s5bb has NO call site — dead code, and its docstring says
     "callers must not multiply it into a production mass".

The production Delta_lambda VALUE path (delta_lambda_value_witness.py) is pure
hook-length integer combinatorics, value_only, with an explicit consumer
warning. Clean.

The owner's named shape DOES exist — delta_lambda_empirical_tabulation.py
solves Sigma c_lambda . Delta_lambda = (M_codata - constituent)/m_e. It claims
"NOT consumed by any production prediction pipeline"; I VERIFIED that claim
rather than accepting it, and it holds.

FOLLOW-UP WORK (this is what the bean is for):

  a. AGENTS.md calls linking_weight_family_a a "CODATA-implied FIT". The code
     is 5/2 + (3/4)h^2 — exact, closed-form, parameter-free, no CODATA. It
     does not even hit CODATA (2.533 vs the 2.46 that round-trips m_p, the
     2.89% gap). What is CODATA-implied is the H_4 Wedderburn-count
     INTERPRETATION — a selection-time fit, a real numerology exposure, but a
     DIFFERENT defect from an inverted value and not fixed by excision. As
     written the wording invites a future agent to excise an algebraic
     identity across ~13 consumers incl. qou-mass. NEEDS OWNER RULING on
     whether the directive covers selection-time fitting; the wording should
     be corrected either way.
  b. delta_lambda_two_factor_phase2.py consumes the CODATA-inverted
     Delta_lambda table and carries NONE of its upstream's CLASS-A banner. An
     agent opening it cold cannot tell its inputs are fitted. Add a banner.
  c. delta_lambda_empirical_tabulation's "auditOnly" tag is a STRING FIELD
     POINTING AT A DOC PATH, not a boolean any tool enforces. The protection
     is documentation, not machinery. Consider making it enforceable.

COVERAGE LIMIT worth recording: a fit that was once obtained by inversion and
then HARDCODED as a bare numeric literal is invisible to this audit's method
(name-shape + consumption tracing). The 4 and 29 in the Habiro tower are
exactly that class and were findable only because the audit trail named them.
