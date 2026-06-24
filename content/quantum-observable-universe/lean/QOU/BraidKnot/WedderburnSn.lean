import Mathlib.RingTheory.SimpleModule.WedderburnArtin
import Mathlib.RingTheory.SimpleModule.IsAlgClosed
import QOU.BraidKnot.MaschkeSnSemisimple

/-!
# QOU.BraidKnot.WedderburnSn — Wedderburn–Artin matrix decomposition of `k[S_n]`

Building on [`MaschkeSnSemisimple`](MaschkeSnSemisimple.lean) (`k[S_n]` is a semisimple ring over a
characteristic-zero field), this file applies Mathlib's **Wedderburn–Artin theorem** to expose the
block structure of the symmetric-group algebra — the next increment toward discharging side-2's
`SnWedderburnSpectralData` hypothesis (`RegularRepBlockTrace`).

- `sn_wedderburnArtin` — `k[S_n] ≃+* ∏ᵢ Matrix (Fin 𝔫ᵢ) (Fin 𝔫ᵢ) 𝔇ᵢ` over division rings `𝔇ᵢ`
  (ring form; needs only `IsSemisimpleRing`).
- `sn_wedderburnArtin_algClosed` — over an algebraically-closed field `K` the division rings collapse
  to `K`: `K[S_n] ≃ₐ[K] ∏ᵢ Matrix (Fin 𝔫ᵢ) (Fin 𝔫ᵢ) K`, so block `i` has `K`-dimension `𝔫ᵢ²`.
- `sn_block_finrank_sq` — the per-block square dimension `finrank K (Matrix (Fin 𝔫ᵢ) _ K) = 𝔫ᵢ²`.
- `sn_sum_sq_eq_factorial` — **`Σᵢ 𝔫ᵢ² = n!`**, the **RSK sum-of-squares**, here **unconditional**:
  `dim_K K[S_n] = n!` equals `Σᵢ 𝔫ᵢ²` by transporting `finrank` across the Wedderburn equivalence.
  This is exactly the identity that `RegularRepBlockTrace.sumSq_dim_eq` obtained only *conditionally*
  on `SnWedderburnSpectralData`; via Wedderburn–Artin it now holds outright (the `𝔫ᵢ` are the
  irreducible dimensions — *which* irreducible each is, i.e. the partition labelling, remains the
  residual Okounkov–Vershik gap, but the sum identity needs no labelling).

## Relation to side 2

`SnWedderburnSpectralData` bundles existence + identification of the block spectral decomposition.
`MaschkeSnSemisimple` discharged *existence* (semisimplicity); this file adds the *structural* face —
the `∏ Matrix` blocks and their `𝔫ᵢ²` dimensions — leaving only the **S_n Okounkov–Vershik
identification** (`𝔫ᵢ` ↔ `dim(λ)=#SYT(λ)`, and the JM-eigenvalue = contents) as the conditional input.

## References
- [manuscript] content/.../BraidKnot/RegularRepBlockTrace.lean (`SnWedderburnSpectralData`, side 2)
- [manuscript] content/.../BraidKnot/MaschkeSnSemisimple.lean (`sn_isSemisimpleRing`)
-/

namespace QOU.BraidKnot.WedderburnSn

open QOU.BraidKnot.MaschkeSnSemisimple

-- `k` lives in `Type` (universe 0), matching `MaschkeSnSemisimple`: the Maschke instance is
-- single-universe and `G = Perm (Fin n) : Type 0` forces `u = 0`.
variable {k : Type} [Field k] [CharZero k]

/-- **Wedderburn–Artin for `k[S_n]`.** Over a characteristic-zero field, the symmetric-group algebra
`k[S_n]` is isomorphic to a finite product of matrix rings over division rings. The block count `N`,
the matrix sizes `𝔫 i`, and the division rings `𝔇 i` are produced by the Wedderburn–Artin theorem;
semisimplicity is `sn_isSemisimpleRing` (Maschke). -/
theorem sn_wedderburnArtin (n : ℕ) :
    ∃ (N : ℕ) (𝔇 : Fin N → Type) (𝔫 : Fin N → ℕ) (_ : ∀ i, DivisionRing (𝔇 i)),
      (∀ i, NeZero (𝔫 i)) ∧
      Nonempty (MonoidAlgebra k (Equiv.Perm (Fin n)) ≃+*
        (∀ i, Matrix (Fin (𝔫 i)) (Fin (𝔫 i)) (𝔇 i))) := by
  haveI : IsSemisimpleRing (MonoidAlgebra k (Equiv.Perm (Fin n))) :=
    sn_isSemisimpleRing n
  exact IsSemisimpleRing.exists_ringEquiv_pi_matrix_divisionRing
    (MonoidAlgebra k (Equiv.Perm (Fin n)))

/-- **Wedderburn–Artin for `K[S_n]` over an algebraically closed field.** When the base field `K` is
algebraically closed (and characteristic zero) the division rings collapse to `K`, so `K[S_n]` is
isomorphic — as a `K`-algebra — to a finite product of matrix algebras `Matrix (Fin 𝔫ᵢ) (Fin 𝔫ᵢ) K`.
Block `i` therefore has `K`-dimension `𝔫ᵢ²`. Finite-dimensionality of `K[S_n]` is automatic. -/
theorem sn_wedderburnArtin_algClosed
    (K : Type) [Field K] [IsAlgClosed K] [CharZero K] (n : ℕ) :
    ∃ (N : ℕ) (𝔫 : Fin N → ℕ), (∀ i, NeZero (𝔫 i)) ∧
      Nonempty (MonoidAlgebra K (Equiv.Perm (Fin n)) ≃ₐ[K]
        (∀ i, Matrix (Fin (𝔫 i)) (Fin (𝔫 i)) K)) := by
  haveI : IsSemisimpleRing (MonoidAlgebra K (Equiv.Perm (Fin n))) :=
    sn_isSemisimpleRing n
  exact IsSemisimpleRing.exists_algEquiv_pi_matrix_of_isAlgClosed K
    (MonoidAlgebra K (Equiv.Perm (Fin n)))

/-- **Block `K`-dimensions are perfect squares.** Each block `Matrix (Fin 𝔫ᵢ) (Fin 𝔫ᵢ) K` of the
algebraically-closed decomposition has `K`-dimension `𝔫ᵢ²`. -/
theorem sn_block_finrank_sq
    (K : Type) [Field K] [IsAlgClosed K] [CharZero K] (n : ℕ) :
    ∃ (N : ℕ) (𝔫 : Fin N → ℕ),
      (∀ i, Module.finrank K (Matrix (Fin (𝔫 i)) (Fin (𝔫 i)) K) = 𝔫 i ^ 2) := by
  obtain ⟨N, 𝔫, _, -⟩ := sn_wedderburnArtin_algClosed K n
  refine ⟨N, 𝔫, fun i => ?_⟩
  rw [Module.finrank_matrix, Module.finrank_self, mul_one, Fintype.card_fin, sq]

/-- **RSK sum-of-squares, unconditional.** The Wedderburn block sizes of `K[S_n]` (over an
algebraically-closed characteristic-zero field) satisfy `Σᵢ 𝔫ᵢ² = n!`. Proof: `dim_K K[S_n] = n!`
(free module on `S_n`), and transporting `finrank` across the Wedderburn algebra-equivalence
`K[S_n] ≃ₐ[K] ∏ᵢ Matrix(𝔫ᵢ)` gives `dim_K K[S_n] = Σᵢ dim_K Matrix(𝔫ᵢ) = Σᵢ 𝔫ᵢ²`. This is the
identity `RegularRepBlockTrace.sumSq_dim_eq` obtained only conditionally on `SnWedderburnSpectralData`;
here it is outright (no partition labelling of the `𝔫ᵢ` is needed for the sum). -/
theorem sn_sum_sq_eq_factorial
    (K : Type) [Field K] [IsAlgClosed K] [CharZero K] (n : ℕ) :
    ∃ (N : ℕ) (𝔫 : Fin N → ℕ), ∑ i, 𝔫 i ^ 2 = n.factorial := by
  obtain ⟨N, 𝔫, -, ⟨e⟩⟩ := sn_wedderburnArtin_algClosed K n
  refine ⟨N, 𝔫, ?_⟩
  have hfact : Module.finrank K (MonoidAlgebra K (Equiv.Perm (Fin n))) = n.factorial := by
    unfold MonoidAlgebra
    rw [Module.finrank_finsupp_self, Fintype.card_perm, Fintype.card_fin]
  have hblocks : Module.finrank K (∀ i, Matrix (Fin (𝔫 i)) (Fin (𝔫 i)) K) = ∑ i, 𝔫 i ^ 2 := by
    rw [Module.finrank_pi_fintype]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Module.finrank_matrix, Module.finrank_self, mul_one, Fintype.card_fin, sq]
  rw [← hblocks, ← e.toLinearEquiv.finrank_eq, hfact]

end QOU.BraidKnot.WedderburnSn
