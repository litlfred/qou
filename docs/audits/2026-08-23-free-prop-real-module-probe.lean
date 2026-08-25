-- Against the REAL modules: these carriers are imported, not restated, so no
-- transcription can flatter them.
import QOU.Habiro.FlowSolution
import QOU.Mathlib.HeckeAlgebra

namespace RealProbe

-- 1. `QOU.Habiro.HabiroFlowSolution` -- three free `Prop` fields plus a
--    conjunction of them. Discharged with no mathematics.
instance : QOU.Habiro.HabiroFlowSolution :=
  ⟨True, True, True, ⟨trivial, trivial, trivial⟩⟩

theorem habiro_conditional_is_unconditional [QOU.Habiro.HabiroFlowSolution]
    (P : Prop) (hP : P) : P := hP

example (P : Prop) (hP : P) : P := habiro_conditional_is_unconditional P hP

-- 2. `QOU.Mathlib.HeckeAlgebra.IwahoriHeckeAlgebra` -- the sharper case. Its
--    three DEFINING relations (Hecke, braid, far-commutativity) are free
--    `Prop` fields, each merely asserted. So an "algebra" in which every
--    braid generator is ZERO -- satisfying none of the three -- inhabits it.
instance degenerate : QOU.Mathlib.HeckeAlgebra.IwahoriHeckeAlgebra ℤ 3 (1 : ℤ) where
  carrier := ℤ
  carrier_addCommGroup := inferInstance
  one := 1
  mul := (· * ·)
  sigma := fun _ => 0          -- every generator is 0
  hecke_relation := True
  hecke_holds := trivial
  braid_relation := True
  braid_holds := trivial
  far_commute := True
  far_commute_holds := trivial

-- The instance above TYPE-CHECKS. So a structure in which every braid
-- generator is `0` -- which satisfies none of the three relations the
-- docstrings name -- is an `IwahoriHeckeAlgebra`. The class does not encode
-- the Hecke presentation; it merely names three propositions and asserts them.
theorem hecke_conditional_is_unconditional
    [QOU.Mathlib.HeckeAlgebra.IwahoriHeckeAlgebra ℤ 3 (1 : ℤ)]
    (P : Prop) (hP : P) : P := hP

-- Resolved from `degenerate`, so the hypothesis contributes nothing.
example (P : Prop) (hP : P) : P := hecke_conditional_is_unconditional P hP

end RealProbe
