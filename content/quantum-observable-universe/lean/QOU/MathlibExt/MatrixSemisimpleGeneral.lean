import QOU.MathlibExt.MatrixSemisimple
import Mathlib.Data.Matrix.Composition
import Mathlib.RingTheory.SimpleModule.WedderburnArtin

namespace QOU.MathlibExt.MatrixSemisimpleGeneral

variable {m : Type*} [Fintype m] [DecidableEq m]

/-- **Matrices over a product ring are the product of the matrix rings.**

`Matrix m m (Π i, S i) ≃+* Π i, Matrix m m (S i)`. A transposition of the two
outer indices; every field is `rfl` except multiplicativity. Mathlib has
`Matrix.compRingEquiv` for matrices *of* matrices but nothing for matrices over
a `Pi`.

The `Matrix.of` in `toFun` is load-bearing, not decoration. `Matrix m m α` is a
type synonym for `m → m → α`, so a bare `fun a b => …` elaborates with the **Pi**
multiplication (`instHMul` on `m → m → S i`) even under a
`: Matrix m m (S i)` ascription — and then `Matrix.mul_apply` does not fire,
while `Pi.mul_apply` fires and rewrites the product pointwise, which is the
wrong lemma. `Matrix.of` pins the matrix structure. -/
def matrixPiRingEquiv {ι : Type*} (S : ι → Type*) [∀ i, Ring (S i)] :
    Matrix m m (Π i, S i) ≃+* Π i, Matrix m m (S i) where
  toFun M := fun i => Matrix.of fun a b => M a b i
  invFun N := Matrix.of fun a b i => N i a b
  left_inv _ := rfl
  right_inv _ := rfl
  map_add' _ _ := rfl
  map_mul' M N := by
    funext i a b
    show ((M * N) a b) i
      = ((Matrix.of fun a b => M a b i) * (Matrix.of fun a b => N a b i)) a b
    rw [Matrix.mul_apply, Matrix.mul_apply, Finset.sum_apply]
    simp

/-- **`IsSemisimpleRing (Matrix m m R)` for a general semisimple base** —
Mathlib's `proof_wanted IsSemisimpleRing.matrix`, in full.

`MatrixSemisimple.instIsSemisimpleRing_matrix` covers the **division-ring**
base. This lifts it to any semisimple `R`, by composing pieces that all already
exist:

1. Artin–Wedderburn (`exists_ringEquiv_pi_matrix_divisionRing`) writes
   `R ≃+* Π i, Matrix (Fin (d i)) (Fin (d i)) (D i)` over division rings `D i`;
2. `RingEquiv.mapMatrix` carries that inside `Matrix m m`;
3. `matrixPiRingEquiv` pushes the product outwards;
4. `Matrix.compRingEquiv` flattens each `Matrix m m (Matrix _ _ (D i))` to
   `Matrix (m × Fin (d i)) (m × Fin (d i)) (D i)`, semisimple by the
   division-ring case;
5. a finite product of semisimple rings is semisimple, and
   `RingEquiv.isSemisimpleRing` transports back along the composite. -/
instance instIsSemisimpleRing_matrix_of_isSemisimpleRing
    {R : Type*} [Ring R] [IsSemisimpleRing R] :
    IsSemisimpleRing (Matrix m m R) := by
  classical
  obtain ⟨N, D, d, _, _, ⟨e⟩⟩ :=
    IsSemisimpleRing.exists_ringEquiv_pi_matrix_divisionRing R
  have hblock : ∀ i, IsSemisimpleRing (Matrix m m (Matrix (Fin (d i)) (Fin (d i)) (D i))) :=
    fun i => (Matrix.compRingEquiv m (Fin (d i)) (D i)).symm.isSemisimpleRing
  exact ((e.mapMatrix (m := m)).trans (matrixPiRingEquiv _)).symm.isSemisimpleRing

end QOU.MathlibExt.MatrixSemisimpleGeneral
