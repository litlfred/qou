-- Against the REAL modules: these carriers are imported, not restated, so no
-- transcription can flatter them.
--
-- STATUS 2026-09-07: part 2 (Hecke) is CLOSED and is kept below as a
-- regression witness; part 1 (Habiro) still stands. See the note at part 2.
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

-- 2. `QOU.Mathlib.HeckeAlgebra.IwahoriHeckeAlgebra` -- the sharper case, and
--    the one that has since been FIXED. Its three DEFINING relations (Hecke,
--    braid, far-commutativity) WERE free `Prop` fields, each merely asserted,
--    so an "algebra" in which every braid generator is ZERO -- satisfying none
--    of the three -- inhabited it:
--
--      instance degenerate : IwahoriHeckeAlgebra ℤ 3 (1 : ℤ) where
--        carrier := ℤ
--        carrier_addCommGroup := inferInstance
--        one := 1
--        mul := (· * ·)
--        sigma := fun _ => 0          -- every generator is 0
--        hecke_relation := True
--        hecke_holds := trivial
--        braid_relation := True
--        braid_holds := trivial
--        far_commute := True
--        far_commute_holds := trivial
--
--    That TYPE-CHECKED when this probe was written (2026-08-23), which was the
--    finding. It does not any more.
--
-- CLOSED 2026-09-07. `hecke`, `braid` and `far_commute` are now equations in
-- the class's own `mul`, `smul`, `one` and `sigma`, so the assignment above is
-- rejected: at `q = 1` over `ℤ` the `hecke` field demands
-- `0 * 0 = (1 - Ring.inverse 1) • 0 + 1`, i.e. `0 = 1`. The obstruction is
-- pure arithmetic and is stated as such, so the witness does not depend on how
-- the class is spelled next time.

theorem zero_generators_rejected :
    ¬ ((0 : ℤ) * 0 = ((1 : ℤ) - Ring.inverse (1 : ℤ)) • (0 : ℤ) + 1) := by
  simp

-- The `[IwahoriHeckeAlgebra …]` hypothesis is therefore no longer free at the
-- shape this probe exhibited. It is still *satisfiable* -- `triv_hecke` over
-- `PUnit`, and non-degenerately `H3.heckeAlgebra` over `H3Carrier` -- but a
-- model must now satisfy the presentation rather than choose what it means.
--
-- Part 1 above (`QOU.Habiro.HabiroFlowSolution`) is UNAFFECTED and its three
-- free `Prop` fields are still live. Do not read this closure as clearing the
-- probe: it closed one of the two carriers it examined.

end RealProbe
