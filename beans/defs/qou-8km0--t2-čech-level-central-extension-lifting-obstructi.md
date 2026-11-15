---
# qou-8km0
title: 'T2: Čech-level central-extension lifting obstruction (torsor over a cover)'
status: completed
type: task
priority: high
created_at: 2026-10-12T19:23:37Z
updated_at: 2026-10-12T19:48:14Z
parent: qou-533l
---

Tier T2 of qou-533l.

**Goal.** Čech level: a central extension of sheaves of groups 1 -> A -> E -> G -> 1 on a space or site, a G-torsor given by a Čech 1-cocycle on a cover, and the obstruction to lifting it to an E-torsor as a Čech 2-cocycle in A. Prove "lifts on that cover iff the 2-cocycle is a Čech coboundary", reusing T1's algebra pointwise on overlaps.

**Missing from Mathlib.** Mathlib has CechNerve, hypercovers, and NonabelianCohomology.H1 (H¹ over a family; its TODO is exactly this obstruction class). It has no Čech H² of sheaves. Start from NonabelianCohomology.H1, i.e. `Mathlib.CategoryTheory.Sites.NonabelianCohomology.H1`, and check how much of its 1-cochain API can carry the obstruction.

**Discipline.** Generic, sorry-free, and no iff as a field.

## 2026-10-12: T2a done (constant coefficients); T2b remains
`QOU/MathlibExt/CechCentralExtensionObstruction.lean` is sorry-free and generic. Lean-direct `-DautoImplicit=false -s 65536` exits 0; axioms are only `[propext, Classical.choice, Quot.sound]`. Given a G-valued Čech 1-cocycle g on an index set I, and lifts x through a central extension A -> E -> G:
- `cechObstruction_cocycle`: c i j k * c i k l = c j k l * c i j l.
- `cechObstruction_lift_change`: different lifts change c by a Čech coboundary.
- `exists_cocycle_lift_iff`: g lifts to an E-valued Čech cocycle iff c = a i j * a j k / a i k.

**Scope.** Constant coefficients: one group element per double overlap, i.e. a constant sheaf with connected overlaps. This is the torsor-gerbe case (Yekutieli exa:27).

**T2b, next.** Make the coefficients a presheaf of groups on the cover (sections over U_ij, with restriction maps), so x, g and c are sections rather than elements. Mathlib's `Sites.NonabelianCohomology.H1` has the 1-cochain machinery to build on.

## 2026-10-12: T2b done (presheaf coefficients); T2 core complete
`QOU/MathlibExt/PresheafCentralExtensionObstruction.lean` builds on Mathlib's `Sites.NonabelianCohomology.H1` cochain style. It is sorry-free with no warnings; lean-direct exits 0; axioms are only [propext, Classical.choice, Quot.sound].
- New: `TwoCochain`, and `PresheafCentralExtension` (ι injective, range ι = ker π, central, 𝒜 commutative, on every section group; π NOT assumed surjective).
- Hypothesis: γ lifts on overlaps to a 1-cochain ξ. This is the analogue of Yekutieli's "class is defined", which the corpus omits.
- `obstruction` (natural in T), `obstruction_cocycle`, and `exists_lift_iff`: γ lifts to an 𝓔-cocycle iff the obstruction = α_ij α_jk α_ik⁻¹ for a 1-cochain α of 𝒜.

**Residuals, carried to T3:**
- (a) Presheaf-level independence of the choice of ξ. T2a has it for constant coefficients; it is a straightforward port.
- (b) Passage to a Grothendieck topology (colimit over covers, refinement).
- (c) Gerbes proper.
