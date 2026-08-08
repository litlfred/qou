---
# qou-qbp5
title: 'OBJECTION: F(P1,P2) needs TWO distinct slopes, but C1 at infinity has ONE - is the ''two Stokes multipliers'' target well-posed?'
status: todo
type: task
priority: high
created_at: 2026-08-08T09:05:00Z
updated_at: 2026-08-08T09:05:00Z
---

**Raised 2026-08-08 while doing S2. This may invalidate the S3 target as framed;
resolve BEFORE any further work on `qou-qbs4`.**

## The objection

RSZ (`uploads/0903.0853v3.pdf` p.21, Def 2.3.1 setup; text extracted from the
FlateDecode streams since this sandbox has no pdftotext):

  "Let us fix a formal class, that is, a pure module: M0 := P1 (+) ... (+) Pk.
   Here, each Pi is pure isoclinic of slope mu_i in Q and rank r_i in N and we
   assume that mu_1 < ... < mu_k."

So `P1,...,Pk` are the graded pieces of the **slope filtration** -- one per
**DISTINCT** slope, strictly increasing. `F(P1,P2)` therefore presupposes **two
distinct slopes**.

But C1's Newton polygon at infinity is a **single edge** (2,0)->(0,1) of slope
1/2 -- verified independently this session by computing deg_x of the coefficients
(see `QOU/QBeta/C1NewtonRamification.lean`). One edge = one slope = **pure
isoclinic**, i.e. `k = 1`. A pure module has no extension data to classify:
`F(P1)` is trivial.

Worse (RSZ p.19): for non-integral slope `mu = d/r` in lowest terms -- here
`1/2`, so `d=1, r=2` -- van der Put-Reversat's classification says such a module
is **irreducible**. An irreducible module has no proper filtration at all.

**If this reading is right, C1's infinity singularity carries NO local Stokes
data, and "two Stokes multipliers U in C^2" is a category error at that site.**

## What could rescue the original framing (check each)

1. **The multipliers are GLOBAL, not local at infinity.** C1 is Fuchsian at 0
   (slope 0) and irregular at infinity (slope 1/2). The 0-vs-infinity connection
   datum is the **Birkhoff matrix** -- which is exactly what W2 is named for
   ("the Birkhoff-matrix infinity-side of the C1 module"). Local isoformal
   classification at infinity and the global connection problem are DIFFERENT
   objects; the C^2 may belong to the latter. **This is the most likely
   resolution and should be checked first.**
2. **The slope data is not what the 08-01 audit recorded.** If the polygon at
   infinity actually has two edges (e.g. slopes 0 and 1/2), then k=2 and
   F(P1,P2) is well-posed with r1=r2=1. My computation says one edge, but it
   depends on the valuation convention at infinity -- re-derive independently.
3. **Post-ramification splitting.** After `z = zeta^2` the slope becomes integral
   (1) and the rank-2 piece may split into two rank-1 pieces -- but they would
   share the SAME slope, so k=1 still and F(...) is still trivial. This does NOT
   rescue it on its own; noted so it is not re-proposed.

## Scope discipline

This is an **objection, not a refutation**. I read ~3 pages of a 174-page
monograph; the `r1 = r2 = 1` and `F(P1,P2) = C^2` claims in
`2026-08-01-c1-inf-slope-half-rsz-stokes.md` may rest on context I have not read.
Do NOT write "refuted" anywhere on the basis of this bean. What is warranted is:
**the target needs re-derivation before more effort goes into extracting it.**

## Lit that would settle it

- RSZ §3.3 in full (LOCAL: `uploads/0903.0853v3.pdf`) -- specifically whether the
  Stokes/Birkhoff data at a single irregular point is being conflated with the
  isoformal classification of a multi-slope module.
- **van der Put-Reversat [56]** (pure-module classification; NOT in `uploads/`) --
  needed to confirm the irreducibility claim for slope `d/r` coprime. This is the
  one genuine external ask.
