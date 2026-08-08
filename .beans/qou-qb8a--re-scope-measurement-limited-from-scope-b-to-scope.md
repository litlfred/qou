---
# qou-qb8a
title: 'Re-scope "measurement-limited => not framework-closable" from scope-(b) to scope-(a)'
status: completed
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


---

# DONE (2026-08-08) — re-scoped in both docs

docs/precision-goals.md "Consequence for the roadmap" (line ~367) and
docs/coordination/2026-08-02-1ppq-lever-map-post-q0-gate.md (line ~54) both
re-scoped from (b) to (a). Numbers unchanged; only the scope was wrong, as this
bean specified.

Both now state: verification below sigma_exp is measurement-limited (TRUE);
extracting c_3 FROM a measured Q_beta is measurement-limited (TRUE); re-pinning
q_0 cannot move them (TRUE, swing is 2.4% of the residual) -- BUT the 1248 ppb
prediction error is the c_3 truncation, a framework quantity, with q_0's
measurement uncertainty contributing ~0.16 ppb (four orders below), so no proved
invariant excludes a derived-c_3 route. Plus: a better neutron measurement
TIGHTENS sigma_exp and makes the target proportionally HARDER.

Extra point found while editing and recorded in precision-goals: the original
escape clause "unless a substrate-q_0 derivation lands" points at a route the
owner PERMANENTLY GATED on 2026-08-02 (qou-eic1). With that route forbidden the
blanket phrasing read as UNFIXABLE -- exactly the over-narrowing the
refuted-scope discipline exists to prevent.

MeasurementLimitedFloor.lean untouched, as this bean specified -- it is sorry-free
and honest in its own docstring ("Nothing here claims the premise").

The listed dead ends stay dead, now labelled scope-(a): fixed-order /
anchor-invariant resummation, geometric q_0, ratio-based W_lambda.
