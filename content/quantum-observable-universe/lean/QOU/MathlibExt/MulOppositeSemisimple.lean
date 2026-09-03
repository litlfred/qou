import QOU.MathlibExt.MatrixSemisimple
import Mathlib.RingTheory.SimpleModule.WedderburnArtin
import Mathlib.Algebra.Field.Opposite
import Mathlib.Algebra.Ring.Equiv

namespace QOU.MathlibExt.MulOppositeSemisimple

universe u

/-- **`IsSemisimpleRing Rᵐᵒᵖ`** — Mathlib's `proof_wanted
IsSemisimpleRing.mulOpposite`.

`IsSemisimpleRing R` is `IsSemisimpleModule R R`, i.e. semisimplicity as a
**left** module; `Rᵐᵒᵖ` semisimple is the right-handed statement. That the two
agree is a theorem, not a definitional shuffle, and Artin–Wedderburn is what
supplies it: the decomposition is a product of matrix rings over division
rings, and each of those three constructions commutes with `ᵐᵒᵖ`.

    Rᵐᵒᵖ  ≃+*  (Π i, Matrix dᵢ dᵢ Dᵢ)ᵐᵒᵖ        `RingEquiv.op` of AW
          ≃+*  Π i, (Matrix dᵢ dᵢ Dᵢ)ᵐᵒᵖ         `RingEquiv.piMulOpposite`
          ≃+*  Π i, Matrix dᵢ dᵢ Dᵢᵐᵒᵖ           `RingEquiv.mopMatrix.symm`

and `Dᵢᵐᵒᵖ` is again a division ring (`MulOpposite.instDivisionRing`), so each
block is semisimple by `MatrixSemisimple.instIsSemisimpleRing_matrix`. -/
instance instIsSemisimpleRing_mulOpposite {R : Type u} [Ring R] [IsSemisimpleRing R] :
    IsSemisimpleRing Rᵐᵒᵖ := by
  classical
  obtain ⟨n, D, d, _, _, ⟨e⟩⟩ :=
    IsSemisimpleRing.exists_ringEquiv_pi_matrix_divisionRing R
  have chain : Rᵐᵒᵖ ≃+* Π i, Matrix (Fin (d i)) (Fin (d i)) (D i)ᵐᵒᵖ :=
    (RingEquiv.op e).trans <|
      (RingEquiv.piMulOpposite _).trans <|
        RingEquiv.piCongrRight fun i => (RingEquiv.mopMatrix).symm
  exact chain.symm.isSemisimpleRing

end QOU.MathlibExt.MulOppositeSemisimple
