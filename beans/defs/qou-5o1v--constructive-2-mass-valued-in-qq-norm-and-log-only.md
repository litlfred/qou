---
# qou-5o1v
title: 'Constructive 2: mass valued in Q(q); norm and log only at comparison'
status: in-progress
type: task
priority: high
tags:
    - constructive
created_at: 2026-11-27T14:50:12Z
updated_at: 2026-11-27T23:53:44Z
parent: qou-dk7p
---

Doc item 2. def:mass-identity uses a norm; binding uses B = alpha ln tr_M (qou-2pnv). Options 2.1 value in Q(q) (recommended); 2.2 algebraic order on Q(q); 2.3 keep. Awaiting owner pick.

## 2026-11-27T23:59Z — owner picked 2.1 (15:18Z); implemented in PR #9840
- def:mass-identity, rem:mass-identity-exists, prop:mass-identity-unique (+proof) restated in R; no norm.
- Lean: BraidKnotOctonion/MassClassRingHom.lean `map_massClass` (braid-class mass natural under ring homs); QOU/Transcendental/MassTheory/MassComparison.lean (comparedMass |φ m|, comparedBinding −α log|φ b|, log product→sum). Sibling frobeniusMass/scalarMass removed.
- Proton ring mass already on main (QOU/Core/MassInRing.lean).
- Remaining: migrate other mass-theory binding prose block by block. Close when #9840 merges.
