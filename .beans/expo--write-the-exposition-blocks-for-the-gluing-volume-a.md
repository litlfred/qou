---
# expo
title: 'Write the exposition blocks for the gluing / volume / surreal-transfer arc'
status: todo
type: task
priority: high
tags:
    - content
    - exposition
    - hyperbolic-volume
parent: m015
created_at: 2026-08-10T05:00:00Z
updated_at: 2026-08-10T05:00:00Z
---

**The arc has proved results with no paper presence.** That is the opposite of the usual
gap and worth closing deliberately.

Checked 2026-08-10: **no content block cites any of these modules** —
`FiveTwoComplexPentagon`, `KummerRadial`, `KummerUnitCircle`, `KummerDilogHalf`,
`IdealTetLawOfSines`, `RivinConcavity`, `MathlibExt/IdealTriangulation`,
`FiveTwoVolumeConstant`, `FigureEightTriangulation`, `FlatTetrahedra`,
`GeneratedGluing`, `HyperrealLimitTransfer`.

Material wanting exposition, all of it Lean-proved and sorry-free:

- the **5₂ saddle sum rule** (proved; was "verified to 80 dps, unproved")
- **Kummer's identity** for general `z`, and the law of sines for the ideal tetrahedron
- **Rivin concavity** — `Λ″ = −cot`, the Hessian, strict concavity on the line
- the **ideal-triangulation volume functor**, `rotate_angles` / `volume_rotate`
- **27 shape fields** with minimal polynomials and discriminants, and **312 generated
  Lean proofs** of edge gluing equations across 19 manifolds (bean `glnl`)
- the **flat-shape result**: the edge equations do **not** detect hyperbolicity;
  positivity does (bean `m015`, `QOU/Knot/FlatTetrahedra.lean`)
- the **ℝ\* limit transfer** and the two-valued-birthday defect (beans `hypr`, `bday`)

## ⚠ Precedent that shapes how to do this

`content/quantum-observable-universe/mass-theory/thurston-volume-additivity.md` already
asserted *"Flat tetrahedra contribute zero volume"* and *"Torus knots … hyperbolic volume
vanishes identically"* — while its Lean sidecar **axiomatised both**. Prose ran **ahead**
of the formalisation and the sidecar papered over the gap with an `axiom` plus a false
blocker note. Both are now discharged.

So when writing these blocks: **wire `lean.ref` to the real theorem as you write the
prose**, not afterwards. A block whose sidecar axiomatises its own claim is worse than no
block, because `status: "verified"` then means nothing.

## Scope discipline to carry into every block

Say plainly, in each block, that none of this establishes any triangulation is a
triangulation *of* a knot complement (Thurston hyperbolisation + Mostow rigidity, needing
hyperbolic 3-manifolds neither Mathlib nor QOU has), and that no volume conjecture is
touched. Route 75 gate G6 is the wording to reuse.

**And say that the mathematics is not new.** Thurston, Neumann–Zagier, Neumann–Reid,
`snap`, Garoufalidis–Goerner–Zickert — see bean `ptlm`. What is new is the corpus's
formalisation and gating, which is worth exposition on its own terms and must not be
dressed up as a mathematical contribution.
