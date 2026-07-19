import QOU.MathlibExt.MatrixSemisimple
import Mathlib.LinearAlgebra.Matrix.ToLin

/-!
# QOU.MathlibExt.EndSemisimple — endomorphism rings of finite-dimensional
# vector spaces are semisimple

Fills the field + `Module.Finite` case of Mathlib's `proof_wanted
IsSemisimpleRing.module_end` (`RingTheory/SimpleModule/Basic.lean`),
companion to `QOU.MathlibExt.MatrixSemisimple` (bean `qou-ciun` /
epic `qou-otbb` infrastructure).

Route: a finite module over a field is free with a finite chosen basis;
`algEquivMatrix` identifies `Module.End K V` with the matrix algebra
over that basis, and the matrix instance of `MatrixSemisimple`
transfers back along the ring equivalence.

Scope note (honest): Mathlib's `proof_wanted` is stated for a finite
semisimple module over an arbitrary ring; that generality needs the
isotypic decomposition and is **not** covered here — this file covers
the vector-space case, which is what the QOU Wedderburn ladder
consumes.  Stated Mathlib-conventionally for upstreaming.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/

namespace QOU.MathlibExt.EndSemisimple

/-- **Endomorphism rings of finite-dimensional vector spaces are
    semisimple (sorry-free):** the field + finite case of Mathlib's
    `proof_wanted IsSemisimpleRing.module_end`. -/
instance isSemisimpleRing_end (K V : Type*) [Field K] [AddCommGroup V]
    [Module K V] [Module.Finite K V] :
    IsSemisimpleRing (Module.End K V) := by
  classical
  exact ((algEquivMatrix (Module.Free.chooseBasis K V)).toRingEquiv).symm.isSemisimpleRing

end QOU.MathlibExt.EndSemisimple
