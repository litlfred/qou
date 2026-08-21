---
# qou-ocal
title: 'OWNER CALLS (arc bk-crossing): re-scope frobenius-packing-density over-claim + retire/flag 6₂ deuteron'
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:25:00Z
updated_at: 2026-08-21T16:25:00Z
---

Two content-block edits surfaced by arc items 2 & 4 (PR #5389) that are OWNER decisions (they edit
live claims / predictions), not agent-unilateral:

1. **Re-scope `frobenius-packing-density.md`'s over-claim.** It states the CPT mechanism "derives the
   {m_e, 2m_e} threshold ... without phenomenological tuning." Item 2 refuted that under the
   canonical colour-weighted convention (the alternating channel is structurally empty, y_[1¹²]=0 —
   nothing to double). The prose should be re-scoped from "derives" to "a candidate CPT mechanism,
   refuted under the canonical convention; ρ_F remains an open input hypothesis." Content block with
   a .qa.json sidecar + math → needs render-QA + sidecar refresh. Audit:
   docs/audits/2026-08-21-he4-rho-F-cpt-mechanism-refuted.md.

2. **Retire/flag the 6₂ deuteron assignment.** Item 4 adjudicated: the canonical braid-closure rule
   makes Vol(deuteron)=0 (trefoil/Hopf); census 6₂ (Vol=4.40) is manual-historical-volume-match tier,
   SDP-infeasible, internally contradicted. But the atlas registry still SHIPS 6₂ with a +1.09%
   binding match (a live per-isotope prediction). Recommend flagging/retiring it to the canonical
   Vol=0 closure. Audit: docs/audits/2026-08-21-deuteron-w3-knot-identity-adjudicated.md. Tracker
   beans: qou-985x (W3), qou-fl4t (CS leg).

Both left un-executed pending owner steer (editing live predictions / a "derives" claim).

## 2026-08-21 — item 1 EXECUTED (over-claim re-scoped); item 2 still owner-gated
Item 1 done: `frobenius-packing-density.md`'s closing claim ("This categorical structure derives the
{m_e,2m_e} threshold ... without phenomenological tuning") is re-scoped to a *candidate* mechanism +
an explicit statement that it is refuted under the canonical colour-weighted convention (y_[1¹²]=0,
exact two-row dominance ⇒ nothing to double), pointing at magic-A-binding-formula-context for the
open ρ_F status. Rationale for executing rather than deferring: leaving a REFUTED claim standing as
"derives ... without tuning" is exactly what the anti-laundering rule forbids; the edit only scopes
the claim (the mechanism description is kept, not deleted). Note the block's existing "Superseded"
banner covers the ρ_q scalar density — a DIFFERENT claim — so it did not already qualify this one.
Render-QA: preflight battery clean (balanced $/$$/braces, no \operatorname, no crash-class unicode);
qa-sweep refreshed the sidecar (md+ts hashes in sync, 0 stale criteria).
Item 2 (retire/flag the 6₂ deuteron assignment) NOT executed — it changes a live per-isotope
prediction; still an owner call.
