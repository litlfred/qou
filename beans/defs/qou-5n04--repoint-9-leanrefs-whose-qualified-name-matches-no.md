---
# qou-5n04
title: Repoint 9 lean.refs whose qualified name matches no declaration
status: todo
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:43:52Z
updated_at: 2026-11-22T10:08:12Z
parent: qou-uwyf
---

Found by the triviality-probe triage (qou-y1qu), record docs/audits/2026-11-22-triviality-decl-not-found-triage.md §3. Nine blocks name a ref whose fully qualified name no file declares, although a same-named declaration in another namespace, or a module of that name, exists: def:braid-group (QOU.BraidGroup), prop:q-jacobiator (QOU.q_jacobiator; declared QOU.Elaboration.q_jacobiator), thm:qu-to-qou (QOU.Torsion.YekutieliTriple.qu_to_qou; sibling declares QOU.qu_to_qou), def:brane-boundary (QOU.Torsion.Descent.BraneBoundary), def:yekutieli-triple (QOU.LiftingDescent.CosimplicialCrossedGroupoid.YekutieliTriple), def:hecke-mass-element (QOU.Torsion.HeckeMassElement, a module), def:two-row-stratum (QOU.BraidKnot.TwoRowStratum, a module), prop:confinement-sdp (declared QOU.Interactions.ConfinementSDP), cor:mass-identity-C (declared QOU.Torsion.MassIdentityC). The ref-resolution audit counts them as resolving because it matches module paths and short names; that is a second gap in the audit. Repointing is a per-block choice (which declaration carries the block's statement); ask the owner per AGENTS.md.



2026-11-22: the same short-name matching shows in docs/audits/2026-11-21-lean-ref-target-audit.json, which assigns QOU.MassIdentity.exists to KeystoneJucysMurphyTwist.lean and MassIdentity.unique / CategoricalAction.unique to QBetaPerBlockChiClosedForms.lean (files that declare other exists/unique). Triage record §7.
