import Mathlib.RingTheory.Idempotents
import Mathlib.RingTheory.SimpleModule.WedderburnArtin
import Mathlib.Tactic

namespace QOU.MathlibExt.WedderburnIdempotents

variable {R₀ A : Type*} [CommSemiring R₀] [Ring A] [Algebra R₀ A]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {M : ι → Type*} [∀ i, Ring (M i)] [∀ i, Algebra R₀ (M i)]

omit [Fintype ι] in
/-- **In a finite product of rings, `Pi.single i 1` is central.**

Mathlib's `CompleteOrthogonalIdempotents.single` gives idempotence, pairwise
orthogonality and completeness of this family; centrality is the part it does
not carry, and the part `QOU.Hecke.WedderburnDecomp.central` asks for. -/
theorem single_one_central (i : ι) (m : Π i, M i) :
    Pi.single (M := M) i 1 * m = m * Pi.single (M := M) i 1 := by
  funext j
  by_cases h : j = i
  · subst h; simp
  · simp [h]

omit [Fintype ι] in
/-- **Centrality transports along a ring equivalence.** -/
theorem central_of_equiv (e : A ≃ₐ[R₀] Π i, M i) (i : ι) (a : A) :
    e.symm (Pi.single i 1) * a = a * e.symm (Pi.single i 1) := by
  calc e.symm (Pi.single i 1) * a
      = e.symm (Pi.single i 1 * e a) := by rw [map_mul, e.symm_apply_apply]
    _ = e.symm (e a * Pi.single i 1) := by rw [single_one_central (M := M) i (e a)]
    _ = a * e.symm (Pi.single i 1) := by rw [map_mul, e.symm_apply_apply]

/-- **From an Artin–Wedderburn equivalence to the central idempotent system.**

An algebra equivalence `A ≃ₐ M₁ × ⋯ × M_N` — which
`IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing_finite` supplies for
any finite-dimensional semisimple algebra — transports the standard idempotents
of the product back to `A`. The result is exactly the data
`QOU.Hecke.WedderburnDecomp` asks for: **idempotent, pairwise orthogonal,
central, summing to `1`**.

The first three of those four come straight from Mathlib
(`CompleteOrthogonalIdempotents.single`, transported by `.map`); centrality is
supplied here.

**What this does not give**, and it is the whole remaining gap:
`WedderburnDecomp` indexes its idempotents by `Partition n`, while
Artin–Wedderburn produces an index of unconstrained size. Matching the two —
that the blocks of `H_n(q)` are indexed by the partitions of `n`, and there are
no others — is Mathas (1999) §3.43, which is not in Mathlib and not in this
tree. So this closes the *construction* of the idempotents and leaves the
*indexing* open. -/
theorem exists_central_completeOrthogonalIdempotents (e : A ≃ₐ[R₀] Π i, M i) :
    ∃ pi : ι → A, CompleteOrthogonalIdempotents pi
      ∧ ∀ (i : ι) (a : A), pi i * a = a * pi i :=
  ⟨fun i => e.symm (Pi.single i 1),
   (CompleteOrthogonalIdempotents.single M).map e.symm.toAlgHom.toRingHom,
   central_of_equiv e⟩

end QOU.MathlibExt.WedderburnIdempotents
