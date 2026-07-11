---
# 08a2
title: 'EPIC: keystone de-abstraction — hard Mathlib-gap infra (tiered)'
status: in-progress
type: epic
priority: normal
tags:
    - keystone-infra
    - lean
created_at: 2026-06-25T17:06:53Z
updated_at: 2026-07-11T19:58:55Z
---

Make the still-abstracted keystone §3b classes (post #2791/#2797) genuinely faithful. Corpus-grep (2026-06-25) found QOU already has substantial Lean infra (IwahoriHecke/*, MathlibExt/Q*, BraidKnot/Cl3Zeta5OrbitSum, BringTrilog*, BraidLinkTypes, ζ5/Goncharov), so most work is WIRING keystones to existing infra; only geometric-Langlands / motivic-Galois / Jones-polynomial are genuinely research-grade. Cached Mathlib: YoungDiagram, PresentedGroup, RootsOfUnity+IsPrimitiveRoot, Complex.Circle, Nat.Choose.



---
**Tier-1 delivered — #3580** (`YoungTableauStandard.lean`, lean-direct EXIT=0, 2026-07-11): defined the `StandardYoungTableau`/`SkewStandardYoungTableau` types Mathlib lacks + `fDim`/`fDimSkew` counts; `entry_lt_card` + `involutionNumber_pos` + `c8_superexp` corollary genuinely proved. Keystone C8 super-exp lower bound now unconditional modulo exactly 3 cited RSK sorries (branching Σf^λ f^{λ/(2,1)}=k!/3; skew↪straight; Σf^λ=I(k)) — the shared Tier-2 fill also needed by Identity I. Same infra unblocks bean wsxl (#3574).
