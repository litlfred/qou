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

## 2026-08-22 — item 2 RE-SCOPED: my Vol=0 premise was refuted by a sibling
Item 2 above said "retire/flag the 6₂ deuteron assignment ... to the canonical Vol=0 closure."
The premise is WRONG. The sibling adjudication `qou-e5jf` (PR #5350, audit
docs/audits/2026-08-21-deuteron-knot-assignment-adjudication.md) reached UNDETERMINED — none of the
three candidates admissible — and refutes my braid-closure argument on three measured grounds:
(1) the canonical mass word is NOT a braid word (5 of 23 letters are averaged crossings, ℂ-linear
combinations in H₆(q)), so "closure is a computation, not a choice" fails at the deuteron;
(2) arity — every live construction of the mass word closes to a 3-COMPONENT link, while 6₂/trefoil
are knots and Hopf is 2-component, and component count is permutation-fixed; (3) the trefoil σ₁³ is
the pn-channel SUBWORD of the 6₂ word, not the atom (I mistook a part for the whole).

What survives: 6₂ is inadmissible by PROVENANCE, on a stronger ground than the tier label I cited —
`computations/mass_table_ppb.py` L18-21 states it outright (line range verified on main; note the
phrase wraps as "AME-driven / fitting", so a one-line grep for it returns a false negative): "that IS a form of AME-driven fitting
(we picked the knot whose volume is closest to B_AME/ρ)". Circular, inadmissible under the anti-fit
rule regardless of the +1.09% agreement.

Re-scoped owner call: flag 6₂ as AME-inverted / not derived — do NOT retarget it to Vol=0 (that
would swap one inadmissible assignment for another). Still owner-gated (live prediction).
My audit 2026-08-21-deuteron-w3-knot-identity-adjudicated.md now carries the retraction banner.

## 2026-08-22 — item 2 EXECUTED (owner-authorised): 6₂ flagged, NOT retargeted
Owner authorised the flag in session. Applied to the live atlas registry
(content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md):
 • deuteron record: added a **Provenance ⚠** row — 6₂ is AME-inverted (producer's own admission,
   mass_table_ppb.py L18-21) so the +1.09% is circular; and the closure claim is asserted-not-computed
   (mass word is not a braid word; arity mismatch — closes to a 3-component link, 6₂ is a knot).
   Cites the sibling adjudication (UNDETERMINED, all three candidates inadmissible).
 • "Closure = K_{6_2}" qualified as **asserted, not computed**; the Prediction row marked **not a
   prediction** (the knot was selected by matching that quantity).
 • `manual-historical-volume-match` tier row (which already names D, T AND ³He): added the same
   AME-inversion admission + citation, so all three entries carry the flag consistently rather than
   leaving D flagged and its two siblings silent.
Deliberately NOT done: retargeting 6₂ to any other knot (Vol=0 included) — no alternative assignment
is established; the flag records undetermined status, it does not pick a winner.
Gates: relative links verified to resolve; render-QA preflight clean (balanced $/braces, no
\operatorname, no crash-class unicode); qa-sweep run — sidecar md+ts in sync, 0 stale criteria.
Both items of this bean are now executed; ready for owner close.
