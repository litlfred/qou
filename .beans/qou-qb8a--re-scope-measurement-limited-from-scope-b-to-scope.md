---
# qou-qb8a
title: 'Re-scope "measurement-limited => not framework-closable" from scope-(b) to scope-(a)'
status: todo
type: task
priority: normal
created_at: 2026-08-08T08:10:00Z
updated_at: 2026-08-08T08:10:00Z
---

`docs/precision-goals.md` (~line 368) and `docs/coordination/2026-08-02-1ppq-lever-map-post-q0-gate.md`
state that Q_beta / m_n / Delta_pn are "measurement-limited by a next-gen neutron
Q_beta measurement" and that "the 5 L2 mass/Q_beta misses are no longer
framework-closable". Per AGENTS.md §"Before declaring refuted", that is a
scope-(b) structural exclusion written without a proved invariant supporting it.

What is actually established (and correct):
- Verification below sigma_exp = 779.7 ppb needs a better measurement. TRUE.
- Extracting c_3 FROM a measured Q_beta is measurement-limited (dq*/dQ_beta ~ -0.54). TRUE.

What is NOT established:
- That the 1248 ppb prediction error cannot be improved by framework compute.
  The residual is the c_3 truncation, a framework quantity. Under the proton pin,
  q0's measurement uncertainty contributes ~0.06 ppb x 2.60 ~ 0.16 ppb to Q_beta
  -- four orders below the residual. A categorical derivation of c_3 is not
  excluded by any proved invariant.

Also note a better neutron measurement TIGHTENS sigma_exp and makes the L2 target
HARDER (target = sigma_exp/100), so "waiting for the measurement" does not close L2.

Action: re-word both docs to scope-(a) ("the cal-anchored extraction route is
measurement-limited; a derived-c_3 route is not excluded"). Do NOT delete the
numbers -- they stand; only the scope was wrong. The supporting Lean
(QOU/QBeta/MeasurementLimitedFloor.lean) is sorry-free and honest in its own
docstring ("Nothing here claims the premise") -- it needs no change.

Analysis: docs/audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md §4.
