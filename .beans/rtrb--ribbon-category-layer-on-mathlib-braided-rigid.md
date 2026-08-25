---
# rtrb
title: 'RT-1: RibbonCategory layer (twist θ) on Mathlib BraidedCategory+RightRigidCategory'
status: in-progress
type: task
priority: high
created_at: 2026-08-02T09:20:00Z
updated_at: 2026-08-17T21:46:04Z
---

Parent: rtep. TIER: ACHIEVABLE (~1-2 sessions). Mathlib has BraidedCategory + Right/LeftRigidCategory
but NOT ribbon (no twist/balancing θ_X : X ≅ X with the ribbon axioms θ_{X⊗Y}=(θ_X⊗θ_Y)∘β²,
θ_{Xᘁ}=(θ_X)ᘁ). Define a RibbonCategory class extending Mathlib's, prove the categorical dimension
qDimObj (already defined, KeystoneRibbonMTCInput.lean) is twist-compatible, and derive the
conjugation symmetry d(Xᘁ)=d(X) categorically (matches the corpus qDim_conj). This is the genuine
"toward Mathlib" continuation of KeystoneRibbonMTCInput. Deliverable: RibbonCategory + a proved
categorical lemma (e.g. qDimObj well-behaved under duals/twist). Does NOT close bwse.

2026-08-02 DONE (KeystoneBalancedRibbon.lean, lean-direct exit 0 sorry-free): BalancedCategory class (twist theta + Joyal-Street balancing axiom) on Mathlib BraidedCategory, with the non-vacuity instance ofSymmetric (every SymmetricCategory is balanced with trivial twist). The ribbon/twist layer Mathlib lacks. Next: the dual-compatibility ribbon axiom (theta_{X*}=(theta_X)*) + connect to qDimObj conjugation symmetry.


## 2026-08-17 — half of this bean's "Next" has landed (from another arc)

This bean's closing line reads *"Next: the dual-compatibility ribbon axiom
(theta_{X*}=(theta_X)*) + connect to qDimObj conjugation symmetry."*

**The first half is done**, arrived at independently from the mass side rather
than from this arc. `QOU/BraidKnot/RibbonFromBalanced.lean` (PR #5262):

```lean
class RibbonCategory … extends BalancedCategory C where
  twist_dual : ∀ X : C, twist (Xᘁ) = (twist X)ᘁ

instance ribbonOfSymmetric : RibbonCategory C   -- non-vacuity, θ = 𝟙
```

`lean`-direct exit 0. Added as an **extension**, so `BalancedCategory` and
`KeystoneBalancedRibbon.lean` are untouched — nothing this bean already built
changes shape.

**The second half is NOT done.** `qDimObj` conjugation symmetry (`rtqd`) still
needs `hSpherical` derived in the **braided** case. The symmetric case was
already provable without any ribbon structure, so proving only that is not
progress. Exact reduction and two do-nots are on bean `qou-gzs0`.

**Left `in-progress` and unclaimed.** This bean is 15 days idle, which the
stalled-claim policy would treat as abandoned, but I am not taking it over —
recording the overlap so whoever returns does not rebuild `twist_dual` from
scratch. If you own this arc: the axiom exists, build on it.

**Route note for the successor.** `ribbonOfSymmetric` only elaborates if the
section omits `[BraidedCategory C]` and lets the braiding come from
`SymmetricCategory` — the `KeystonePivotalSpherical` dodge. I first recorded
that dodge as non-transferable and had to retract it; it transfers exactly.
