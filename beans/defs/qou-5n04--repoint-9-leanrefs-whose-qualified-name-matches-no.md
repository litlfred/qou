---
# qou-5n04
title: Repoint 9 lean.refs whose qualified name matches no declaration
status: todo
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:43:52Z
updated_at: 2026-11-22T10:49:15Z
parent: qou-uwyf
---

Found by the triviality-probe triage (qou-y1qu), record docs/audits/2026-11-22-triviality-decl-not-found-triage.md §3. Nine blocks name a ref whose fully qualified name no file declares, although a same-named declaration in another namespace, or a module of that name, exists: def:braid-group (QOU.BraidGroup), prop:q-jacobiator (QOU.q_jacobiator; declared QOU.Elaboration.q_jacobiator), thm:qu-to-qou (QOU.Torsion.YekutieliTriple.qu_to_qou; sibling declares QOU.qu_to_qou), def:brane-boundary (QOU.Torsion.Descent.BraneBoundary), def:yekutieli-triple (QOU.LiftingDescent.CosimplicialCrossedGroupoid.YekutieliTriple), def:hecke-mass-element (QOU.Torsion.HeckeMassElement, a module), def:two-row-stratum (QOU.BraidKnot.TwoRowStratum, a module), prop:confinement-sdp (declared QOU.Interactions.ConfinementSDP), cor:mass-identity-C (declared QOU.Torsion.MassIdentityC). The ref-resolution audit counts them as resolving because it matches module paths and short names; that is a second gap in the audit. Repointing is a per-block choice (which declaration carries the block's statement); ask the owner per AGENTS.md.



2026-11-22: the same short-name matching shows in docs/audits/2026-11-21-lean-ref-target-audit.json, which assigns QOU.MassIdentity.exists to KeystoneJucysMurphyTwist.lean and MassIdentity.unique / CategoricalAction.unique to QBetaPerBlockChiClosedForms.lean (files that declare other exists/unique). Triage record §7.


## 2026-11-22 — PR #9005 (issue #9004)
Repointed 9 refs (6 from the triage list, 3 more found by the stricter ref audit). The triage list's qu-to-qou, brane-boundary and yekutieli-triple are VALID module-path refs, so they are unchanged; the probe learned that form in folio-assistant-sci#213 (resolveByModulePath). The ref audit now requires a qualified-name match (new row class grep_other_namespace): 0 rows; 1317/1324 ok, the 7 others are tracked (qou-02q4, qou-mhzl). The ref-target-audit short-name mismatch (MassIdentity.exists/unique, CategoricalAction.unique pointing at other files) is the same defect class and is closed by that rule. Status: in review, PR #9005.
