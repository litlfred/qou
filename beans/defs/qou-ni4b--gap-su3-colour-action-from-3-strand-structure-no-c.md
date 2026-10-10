---
# qou-ni4b
title: 'GAP: SU(3) colour action on the QOU three-strand Hecke state space — abstract module exists, framework-native action open'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-07-31T19:56:30Z
updated_at: 2026-10-10T07:15:39Z
parent: qou-8lxd
---

2026-08-02 sharpened status.

This is now strictly the framework-native colour-action gap.

- CLOSED precursor: the abstract colour-action class is already satisfied on the octonion base module `O = C ⊕ C^3` (`sm-colour-stabilizer-action`; `OctonionColourActionBaseModule.lean`). So this is no longer 'octonion fragments only'.
- OPEN content: construct an injective colour action on the framework's own three-strand Hecke / braid-state module, not merely on some faithful module somewhere.
- Required strengthening for real closure: the action should target the QOU three-strand state space and be compatible with its Hecke / braid structure.

Keep this bean separate from qou-d7h1: colour SU(3) acts on the underlying strand state space; flavor SU(3) organizes hadron multiplets.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
