---
# qou-qbp5
title: 'OBJECTION: F(P1,P2) needs TWO distinct slopes, but C1 at infinity has ONE - is the ''two Stokes multipliers'' target well-posed?'
status: completed
type: task
priority: high
created_at: 2026-08-08T09:05:00Z
updated_at: 2026-08-08T11:35:00Z
---

**Raised 2026-08-08 while doing S2. This may invalidate the S3 target as framed;
resolve BEFORE any further work on `qou-qbs4`.**

## The objection

RSZ (`library/arxiv-0903.0853v3/0903.0853v3.pdf` p.21, Def 2.3.1 setup; text extracted from the
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

- RSZ §3.3 in full (LOCAL: `library/arxiv-0903.0853v3/0903.0853v3.pdf`) -- specifically whether the
  Stokes/Birkhoff data at a single irregular point is being conflated with the
  isoformal classification of a multi-slope module.
- **van der Put-Reversat [56]** (pure-module classification; NOT in `library/`) --
  needed to confirm the irreducibility claim for slope `d/r` coprime. This is the
  one genuine external ask.

## CONFIRMED 2026-08-08 by RSZ's own text — and it is worse than the objection

Read §3.3 in full. Three direct quotes settle it.

**1. §3.3 is only about INTEGRAL slopes.** Its title:

    "3.3. EXPLICIT DESCRIPTION OF F(P1,...,Pk) IN THE CASE OF INTEGRAL SLOPES"

C1's slope is 1/2. Not integral. §3.3 does not apply to it at all.

**2. The "level d" is the SLOPE DIFFERENCE, not a denominator.** RSZ p.38,
Example 3.3.3, deriving the very recurrence we formalized:

    "... where we denoted d := mu_2 - mu_1 in N the level of the above
     inhomogeneous equation."

So `d` is the gap between two consecutive slopes of the filtration, and it is a
NATURAL NUMBER because §3.3 assumes integral slopes. The 08-01 audit's
"slope 1/2 => level d = 2 (the denominator of the slope)" is a **misreading**.
There is no level without two slopes.

**3. Dimension count confirms k=1 is trivial.** Theorem 3.3.5: `F(P1,...,Pk)` is
an affine space of dimension `sum_{i<j} r_i r_j (mu_j - mu_i)`. With `k = 1` the
sum is empty: **dimension 0**. A single-slope module has no isoformal moduli.

**4. The correct reference for non-integral slopes exists and is NOT in uploads:**

    "A generalisation of Birkhoff-Guenther normal form to the case of arbitrary
     slopes has recently been obtained by Virginie Bugeaud [14]."

## Consequence

The chain "C1 has slope 1/2 => level d=2 => q-Borel B_{q,2} => F(P1,P2) = C^2 =>
two Stokes multipliers" is **not RSZ's**. Each link misreads a §3.3 that is
explicitly restricted to integral slopes, and the pivotal one (`d` = denominator
vs `d` = slope difference) inverts the meaning of the central parameter.

**This is a mis-citation, not a mathematical refutation.** C1's infinity residual
may well be genuinely wild and interesting; what is wrong is the mapping onto
§3.3. The right frame for a single non-integral slope is Bugeaud [14], or the
global 0-vs-infinity Birkhoff connection problem (rescue 1, still live and now
the most likely home of any C^2).

## What this does NOT invalidate

- **S0** (`qou-qbk1`): the level-`d` kernel is correctly formalized for arbitrary
  `d` from the recurrence RSZ states. The math stands; only the claim that
  `d = 2` is C1's level is withdrawn.
- **S2's Newton work** (`qou-qbr3`): the polygon, the edge, the characteristic
  equation and the proved non-removability of `sqrt(q-1)` are computed from the
  operator itself and are independent of RSZ's framing.
- **S1's arithmetic** (`qou-qbg2`): `ramified_qBorel_budget` (m^2 = m(m-1) + m)
  is a true theorem. But **its INTERPRETATION is withdrawn** -- see that bean.

## Bugeaud [14] OBTAINED — and it does NOT rescue the framing

Owner uploaded it 2026-08-08 (commit 733a88b8):
`library/crmath-2011-349-19-20-1037-0/CRMATH_2011__349_19-20_1037_0.pdf`. Identity metadata-verified from the
PDF's own `/Title`, `/Author` and `dc:description` (the body text is a
font-subset encoding and does not extract, but the metadata is plain):

  Virginie Bugeaud, "Classification analytique et theorie de Galois locales des
  modules aux q-differences a pentes non entieres",
  C. R. Acad. Sci. Paris, Ser. I, 349 (2011) 1037-1039, doi 10.1016/j.crma.2011.09.002

Exactly RSZ's [14]. Registered in `content/schema/references.ts` as `bugeaud2011`.

**Its section bookmarks settle the last open possibility:**

  1 Introduction
  2 Classification analytique isoformelle a DEUX PENTES
  3 Operateurs de Stokes
  4 Groupe de Galois formel

So the non-integral generalisation is **still a two-slope theory**. Combined with
RSZ §3.3 (integral, also two-slope) this closes the gap: **no version of the
apparatus -- integral or ramified -- supplies Stokes data for a module that is
pure isoclinic at the point in question.** Bugeaud lifts the integrality
restriction, not the two-slope requirement.

**Status of the three candidate rescues from the original objection:**

1. **Global 0-vs-infinity (Birkhoff) rather than local at infinity** -- STILL LIVE,
   and now the only survivor. C1 is Fuchsian at 0 and irregular at infinity; a
   connection datum between two singular points is a different object from the
   local isoformal class at one of them, and W2 is literally named for the
   Birkhoff matrix. **This is where any C^2 must come from, if anywhere.**
2. **The polygon actually has two edges** -- would need the 08-01 slope data to be
   wrong. My independent computation says one edge. Cheap to re-derive; do that
   before trusting rescue 1.
3. **Post-ramification splitting** -- DEAD, as recorded: same slope, k=1 still.

**Remaining lit gap:** none for this question. RSZ and Bugeaud are both local and
both need two slopes. If rescue 1 is pursued, the relevant literature is the
q-analogue of the Birkhoff connection problem, not §3.3.

## CLOSED 2026-08-08 — objection UPHELD, written up

Full write-up: `docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md`. RSZ's own
text (§3.3 title; `d := mu_2 - mu_1` p.38; Thm 3.3.5 dim 0 at k=1; p.21 Def 2.3.1)
plus Bugeaud [14]'s two-slope §2 close it. Mis-citation, not refutation of the
physics. Dependent beans qbg2/qbr3/qbq6/qbs4 marked void.
