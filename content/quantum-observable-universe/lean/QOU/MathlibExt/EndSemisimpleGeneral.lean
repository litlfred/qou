import QOU.MathlibExt.MatrixSemisimple
import Mathlib.RingTheory.SimpleModule.WedderburnArtin

namespace QOU.MathlibExt.EndSemisimpleGeneral

/-- **`IsSemisimpleRing (Module.End R M)` for any finite semisimple module** —
Mathlib's `proof_wanted IsSemisimpleRing.module_end`, in full.

`MathlibExt.EndSemisimple.isSemisimpleRing_end` covers `M` a
finite-dimensional vector space over a **field**. This is the general
statement, with the same hypotheses the `proof_wanted` carries.

Three steps, each already available:

1. `IsSemisimpleModule.exists_end_ringEquiv` decomposes
   `End R M ≃+* Π i, Matrix (Fin dᵢ) (Fin dᵢ) (End R Sᵢ)` with each `Sᵢ` a
   **simple** submodule — this is the isotypic decomposition, and it is where
   `Module.Finite` is used;
2. Schur's lemma (`Module.End.instDivisionRing`) makes each `End R Sᵢ` a
   division ring, so each block is semisimple by
   `MatrixSemisimple.instIsSemisimpleRing_matrix`;
3. a finite product of semisimple rings is semisimple, and
   `RingEquiv.isSemisimpleRing` transports back.

Note this does **not** need the general-base matrix result: the blocks land on
division rings by Schur, which is precisely the case already proved. -/
noncomputable instance instIsSemisimpleRing_end_of_isSemisimpleModule
    {R M : Type*} [Ring R] [AddCommGroup M] [Module R M]
    [IsSemisimpleModule R M] [Module.Finite R M] :
    IsSemisimpleRing (Module.End R M) := by
  classical
  obtain ⟨N, S, d, hS, _, ⟨e⟩⟩ := IsSemisimpleModule.exists_end_ringEquiv R M
  have hblock : ∀ i, IsSemisimpleRing
      (Matrix (Fin (d i)) (Fin (d i)) (Module.End R (S i))) := by
    intro i
    haveI := hS i
    exact MatrixSemisimple.instIsSemisimpleRing_matrix
  exact e.symm.isSemisimpleRing

end QOU.MathlibExt.EndSemisimpleGeneral
