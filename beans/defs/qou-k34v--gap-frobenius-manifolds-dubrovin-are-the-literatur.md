---
# qou-k34v
title: 'GAP: Frobenius manifolds (Dubrovin) are the literature for the metric-from-pairing step and are uncited'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T19:08:39Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-ddmn
---

MEASURED: 'Frobenius manifold' and 'Dubrovin' return ZERO hits across content/ (.md and .ts). That is the existing mathematical theory of precisely the object qou-dygk needs at step 2 — a manifold whose every tangent space carries a Frobenius algebra whose nondegenerate invariant pairing IS a flat metric, with the compatibility worked out. The corpus builds the Frobenius pairing correctly (FrobeniusPairingCategorical.lean) and then has nowhere to vary it, while the literature for varying it is unread. Cheapest useful next step in the whole gravity arc: read Dubrovin's lectures before writing any new Lean for step 2.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8462, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Still holds by content grep ("Frobenius manifold" / "Dubrovin" absent from folio content). Not re-measured in `library/`. Citation gap only. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).

## 2026-11-21 — superseded-premise check (owner instruction 2026-11-21, physics-scope sibling)

Checked against `docs/coordination/owner-rulings.md` on main: no superseded premise found (L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, one-term trace, trefoil-as-electron, c₂ = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory).
