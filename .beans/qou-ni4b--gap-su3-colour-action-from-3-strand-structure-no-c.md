---
# qou-ni4b
title: 'GAP: SU(3) colour action on the QOU three-strand Hecke state space — abstract module exists, framework-native action open'
status: in-progress
type: task
priority: normal
created_at: 2026-07-31T19:56:30Z
updated_at: 2026-08-02T17:33:41Z
---

2026-08-02 sharpened status.

This is now strictly the framework-native colour-action gap.

- CLOSED precursor: the abstract colour-action class is already satisfied on the octonion base module `O = C ⊕ C^3` (`sm-colour-stabilizer-action`; `OctonionColourActionBaseModule.lean`). So this is no longer 'octonion fragments only'.
- OPEN content: construct an injective colour action on the framework's own three-strand Hecke / braid-state module, not merely on some faithful module somewhere.
- Required strengthening for real closure: the action should target the QOU three-strand state space and be compatible with its Hecke / braid structure.

Keep this bean separate from qou-d7h1: colour SU(3) acts on the underlying strand state space; flavor SU(3) organizes hadron multiplets.
