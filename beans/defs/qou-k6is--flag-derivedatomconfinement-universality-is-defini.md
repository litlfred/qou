---
# qou-k6is
title: 'FLAG: DerivedAtom.confinement_universality is definitional (polarization argument discarded)'
status: todo
type: task
tags:
    - quark-state
created_at: 2026-11-15T08:17:22Z
updated_at: 2026-11-15T08:17:22Z
parent: qou-qs0e
blocking:
    - qou-qs2u
---

From qou-qs2u, PR #7825. QOU/Interactions/DerivedAtom.lean:126-158 defines crossingCoeffsWithPol ct _ := crossingCoeffs ct and then proves independence of the polarization by simp. It is true by definition and says nothing about the gamma-gamma chain. Not edited (owner ask rule). Options: scope it as a definitional remark, or route it through the flavour-extraction map once that exists.
