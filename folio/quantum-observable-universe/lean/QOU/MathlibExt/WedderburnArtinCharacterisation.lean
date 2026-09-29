import QOU.MathlibExt.MatrixSemisimple
import Mathlib.RingTheory.SimpleModule.WedderburnArtin

namespace QOU.MathlibExt.WedderburnArtinCharacterisation

universe u

/-- **The converse half of Artin–Wedderburn**: a finite product of matrix rings
over division rings is semisimple.

Mathlib proves the forward half
(`IsSemisimpleRing.exists_ringEquiv_pi_matrix_divisionRing`) but states the
`iff` only as `proof_wanted`; this is the direction it is missing. -/
theorem isSemisimpleRing_of_ringEquiv_pi_matrix_divisionRing
    {R : Type u} [Ring R] {n : ℕ} {S : Fin n → Type u} {d : Fin n → ℕ}
    [∀ i, DivisionRing (S i)]
    (e : R ≃+* Π i, Matrix (Fin (d i)) (Fin (d i)) (S i)) :
    IsSemisimpleRing R :=
  e.symm.isSemisimpleRing

/-- **Artin–Wedderburn, as a characterisation** — Mathlib's
`proof_wanted isSemisimpleRing_iff_pi_matrix_divisionRing`.

Forward is Mathlib's own `exists_ringEquiv_pi_matrix_divisionRing` (dropping its
`NeZero` conjunct); backward is the converse above, which rests on
`MatrixSemisimple.instIsSemisimpleRing_matrix` (matrix rings over a division
ring are semisimple), the finite-product instance, and transport. -/
theorem isSemisimpleRing_iff_pi_matrix_divisionRing {R : Type u} [Ring R] :
    IsSemisimpleRing R ↔
    ∃ (n : ℕ) (S : Fin n → Type u) (d : Fin n → ℕ) (_ : ∀ i, DivisionRing (S i)),
      Nonempty (R ≃+* Π i, Matrix (Fin (d i)) (Fin (d i)) (S i)) := by
  constructor
  · intro _
    obtain ⟨n, D, d, hD, _, ⟨e⟩⟩ :=
      IsSemisimpleRing.exists_ringEquiv_pi_matrix_divisionRing R
    exact ⟨n, D, d, hD, ⟨e⟩⟩
  · rintro ⟨n, S, d, hS, ⟨e⟩⟩
    letI := hS
    exact isSemisimpleRing_of_ringEquiv_pi_matrix_divisionRing e

end QOU.MathlibExt.WedderburnArtinCharacterisation
