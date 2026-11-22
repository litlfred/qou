import QOU.LiftingDescent.CosimplicialCrossedGroupoid


/-!
# QOU.LiftingDescent.ccg_crossed_module_structure

The brane-tower cosimplicial crossed groupoid carries a crossed
module at each level, packaging the pair `(SU_qₙ(2), 𝒪_M^×)` together
with the boundary `∂(a) = a · 𝟏` and the conjugation action
`g · a = g a g⁻¹`.

This sibling file extracts the per-level `CrossedModule` from the
`crossedMod` field of `CosimplicialCrossedGroupoid`.  The Peiffer
identity is discharged by the structure's `peiffer` field.

LaTeX label: `lem:ccg-crossed-module-structure`

## References

- [yekutieli2014-descent] Combinatorial Descent Data for Gerbes, §1
  (Def 1.2, crossed groupoid; Rem 1.3, crossed module)
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU.LiftingDescent

/-- **Crossed-module structure at each level of the brane-tower CCG.**

    At every level `n`, the cosimplicial crossed groupoid yields a
    `CrossedModule` whose carriers package the level-`n` analogues
    of `SU_qₙ(2)` and `𝒪_M^×`.  The Peiffer identity is part of the
    `CrossedModule` structure and is therefore automatic. -/
-- Ref: [yekutieli2014-descent] Def 1.2 (crossed groupoid; one object = crossed module, Rem 1.3)
-- Ref: [leitner2026] §3, Lemma: CCG crossed-module structure
theorem ccg_crossed_module_structure
    {M : Type*} (ccg : CosimplicialCrossedGroupoid M) (n : ℕ) :
    Nonempty CrossedModule :=
  ⟨ccg.crossedMod n⟩

/-- The per-level crossed module is exactly `ccg.crossedMod n` and
    inherits Peiffer for free from the `CrossedModule` structure. -/
-- Ref: [yekutieli2014-descent] Def 1.2 (crossed groupoid; one object = crossed module, Rem 1.3)
theorem ccg_crossed_module_peiffer
    {M : Type*} (ccg : CosimplicialCrossedGroupoid M) (n : ℕ) :
    ∀ (g : (ccg.crossedMod n).G) (x : (ccg.crossedMod n).N),
      (ccg.crossedMod n).boundary ((ccg.crossedMod n).action g x)
        = g * (ccg.crossedMod n).boundary x * g⁻¹ :=
  (ccg.crossedMod n).peiffer

end QOU.LiftingDescent
