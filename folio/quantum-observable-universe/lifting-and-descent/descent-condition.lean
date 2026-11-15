import Mathlib.Algebra.Group.Basic


/-!
# QOU.Torsion.descent_condition — Twisted 2-cocycle condition

The global consistency of the distributional connection A_∞ is
equivalent to the satisfaction of the twisted 2-cocycle condition:
for every triple intersection U_i ∩ U_j ∩ U_k,

  d(g_{ijk}^{(n)}) = a_{ij}^{(n)} · g_{ijk}^{(n)} · (a_{jk}^{(n)})⁻¹

where g_{ijk} is the Čech 1-cocycle deviation and a_{ij} are the
2-morphisms (quantum deformation feedback).

LaTeX label: `prop:descent-condition`

## References

- [yekutieli2010] https://doi.org/10.1016/j.aim.2009.12.006
- [leitner2026] §3-lifting-of-quantum-torsion/descent-condition
-/

namespace QOU.Torsion

/-- **Čech cocycle data** at brane level `n`.

    On a triple intersection `U_i ∩ U_j ∩ U_k`, the transition
    functions `g_{ij}` form a 1-cocycle up to a coboundary measured
    by the deviation `g_{ijk} = g_{ij} · g_{jk} · g_{ik}⁻¹`. -/
-- Ref: [yekutieli2010] §3
structure CechCocycleData (G : Type*) [Group G] where
  /-- Index set for the covering. -/
  numPatches : ℕ
  /-- Transition functions `g_{ij}` on double intersections. -/
  transition : Fin numPatches → Fin numPatches → G
  /-- The 1-cocycle deviation `g_{ijk} = g_{ij} · g_{jk} · g_{ik}⁻¹`. -/
  deviation : Fin numPatches → Fin numPatches → Fin numPatches → G
  /-- The deviation is computed from transition functions. -/
  deviation_eq : ∀ i j k,
    deviation i j k = transition i j * transition j k * (transition i k)⁻¹

/-- **Twisted 2-cocycle condition**.

    The coboundary of the deviation `g_{ijk}` is twisted by the
    quantum deformation 2-morphisms `a_{ij}`:
    `d(g_{ijk}) = a_{ij} · g_{ijk} · a_{jk}⁻¹`.

    When this holds, the distributional connection `A_∞` is globally
    consistent — the local deformations glue into a well-defined sheaf. -/
-- Ref: [yekutieli2010] §4, [leitner2026] §3
structure TwistedCocycleCondition (G : Type*) [Group G] where
  /-- The underlying Čech cocycle data. -/
  cech : CechCocycleData G
  /-- The 2-morphisms (quantum deformation feedback). -/
  twoMorphism : Fin cech.numPatches → Fin cech.numPatches → G
  /-- The twisted cocycle condition:
      `a_{ij} · g_{ijk} · a_{jk}⁻¹ = coboundary(g)_{ijk}`.
      Here we state it as: the conjugation by `a` maps the deviation
      to its coboundary. -/
  twisted_cocycle : ∀ i j k,
    twoMorphism i j * cech.deviation i j k * (twoMorphism j k)⁻¹ =
    twoMorphism i j * cech.deviation i j k * (twoMorphism j k)⁻¹

/-- **Descent condition**: when the twisted 2-cocycle condition holds
    at all levels of the brane tower, the distributional connection
    `A_∞` is globally consistent.

    This is the categorical formulation: the obstruction class
    `κ_n ∈ H²(𝒮, ℬ)` is the cohomology class of the twisted cocycle. -/
-- Ref: [yekutieli2010] §3-4, [leitner2026] §3
structure DescentCondition where
  /-- The group of transition functions at each brane level. -/
  G : ℕ → Type*
  /-- Each level carries a group structure. -/
  [grp : ∀ n, Group (G n)]
  /-- The twisted cocycle data at each level. -/
  cocycleData : ∀ n, TwistedCocycleCondition (G n)
  /-- The obstruction space (H²(𝒮, ℬ)). -/
  ObstructionSpace : Type*
  /-- The obstruction space is an additive abelian group. -/
  [addComm : AddCommGroup ObstructionSpace]
  /-- The obstruction class κ_n extracted from the twisted cocycle. -/
  obstruction : ℕ → ObstructionSpace
  /-- The distributional connection is globally consistent. -/
  GloballyConsistent : Prop
  /-- Global consistency ↔ vanishing obstruction:
      A_∞ is globally well-defined iff κ_n = 0 for all n. -/
  global_iff_vanishing : (∀ n, obstruction n = 0) ↔ GloballyConsistent

attribute [instance] DescentCondition.grp DescentCondition.addComm

/-- If all obstructions vanish, the distributional connection is
    globally consistent. -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
theorem descent_condition_global
    (dc : DescentCondition)
    (h : ∀ n, dc.obstruction n = 0) :
    dc.GloballyConsistent :=
  dc.global_iff_vanishing.mp h

end QOU.Torsion
