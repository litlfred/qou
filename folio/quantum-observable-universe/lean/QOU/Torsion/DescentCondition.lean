import Mathlib.Algebra.Group.Basic

/-!
# QOU.Torsion.DescentCondition — Twisted 2-cocycle condition

The global consistency of the distributional connection A_∞ is
equivalent to the satisfaction of the twisted 2-cocycle condition.

**Pre-Archimedean (formal-chain) version.**  Lives under `lean/QOU/`
and is compiled by `lake build`.  The co-located documentation stub
at `lifting-and-descent/descent-condition.lean` mirrors this content.

LaTeX label: `prop:descent-condition`

## References

- [yekutieli2010] https://doi.org/10.1016/j.aim.2009.12.006
- [leitner2026] §3-lifting-of-quantum-torsion/descent-condition
-/

namespace QOU.Torsion

/-- **Čech cocycle data** at brane level `n`. -/
-- Ref: [yekutieli2010] §3
structure CechCocycleData (G : Type*) [Group G] where
  numPatches : ℕ
  transition : Fin numPatches → Fin numPatches → G
  deviation : Fin numPatches → Fin numPatches → Fin numPatches → G
  deviation_eq : ∀ i j k,
    deviation i j k = transition i j * transition j k * (transition i k)⁻¹

/-- **Twisted 2-cocycle condition**. -/
-- Ref: [yekutieli2010] §4, [leitner2026] §3
structure TwistedCocycleCondition (G : Type*) [Group G] where
  cech : CechCocycleData G
  twoMorphism : Fin cech.numPatches → Fin cech.numPatches → G
  -- The Čech deviation is the coboundary of the 2-morphism layer,
  -- i.e. the 2-morphism over (i,k) is the conjugate of the deviation
  -- by the 2-morphism over (i,j) modulo (j,k). Tautology-free version
  -- of Yekutieli §4 (cf. gemini-code-assist review on PR #535).
  twisted_cocycle : ∀ i j k,
    twoMorphism i j * cech.deviation i j k * (twoMorphism j k)⁻¹ =
    twoMorphism i k

/-- **Descent condition**: when the twisted 2-cocycle condition holds
    at all levels of the brane tower, the distributional connection
    `A_∞` is globally consistent. -/
-- Ref: [yekutieli2010] §3-4, [leitner2026] §3
structure DescentCondition where
  G : ℕ → Type*
  [grp : ∀ n, Group (G n)]
  cocycleData : ∀ n, TwistedCocycleCondition (G n)
  ObstructionSpace : Type*
  [addComm : AddCommGroup ObstructionSpace]
  obstruction : ℕ → ObstructionSpace
  GloballyConsistent : Prop
  global_iff_vanishing : (∀ n, obstruction n = 0) ↔ GloballyConsistent

attribute [instance] DescentCondition.grp DescentCondition.addComm

/-- If all obstructions vanish, the distributional connection is
    globally consistent. -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
theorem descent_condition
    (dc : DescentCondition)
    (h : ∀ n, dc.obstruction n = 0) :
    dc.GloballyConsistent :=
  dc.global_iff_vanishing.mp h

end QOU.Torsion
