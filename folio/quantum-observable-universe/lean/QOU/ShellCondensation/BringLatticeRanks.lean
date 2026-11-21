import Mathlib.RingTheory.SimpleModule.Isotypic
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.FiniteDimensional.Defs
import Mathlib.LinearAlgebra.Dimension.Finite
import Mathlib.LinearAlgebra.Dimension.Free
import Mathlib.Algebra.BigOperators.Fin
import QOU.Common.MagicNumbers

/-!
# QOU.ShellCondensation.BringLatticeRanks

Tests the Bring-surface reading of `conj:homological-shell-condensation` /
`conj:magic-numbers-bring`: "a magic number `n` is the rank of an `S₅`-stable
(`τ̂`-stable) sub-lattice of `H₁(𝓑, ℤ)^{k(n)}`".

1. **Isotypic divisibility** (`finrank_dvd_of_isotypic`). If `M` is a
   finite-dimensional semisimple module over a `k`-algebra `R`, isotypic of type
   `S`, then every `R`-submodule `N` has `dim_k S ∣ dim_k N`. Proved from
   Mathlib's `IsIsotypicOfType.linearEquiv_finsupp`.

2. **Character arithmetic for `H₁(Bring, ℚ)`** (`bring_H1_character`). On the
   seven conjugacy classes of `S₅`, the Lefschetz character `2 − #Fix(g)` of
   `H₁` of Bring's curve (signature `(2,4,5)`) has inner product `2` with
   `std ⊗ sgn`, `0` with `std`, and norm `4`; hence `H₁(Bring, ℚ) ≅ 2·(std ⊗ sgn)`,
   isotypic of a 4-dimensional type. The character values are inputs, computed
   exactly in `computations/probes/bring_s5_sublattice_rank_probe.py`; Lean checks
   the arithmetic only.

3. **Consequence for the magic set** (`magic_not_four_dvd`, `four_dvd_ne_saturated`).
   With (1) applied to `R = ℚ[S₅]`, `M = H₁(Bring, ℚ)^k`, `dim S = 4`, the rank of
   an `S₅`-stable sub-lattice (= `dim_ℚ` of its `ℚ`-span) is a multiple of 4.
   The magic numbers `2, 50, 82, 126` are not; and `4` is a multiple of 4 that is
   not magic. So this reading cannot produce the magic set.

-- Ref: [leitner2026] conj:magic-numbers-bring, conj:homological-shell-condensation
-/

namespace QOU.ShellCondensation.BringLatticeRanks

universe u
open Module

/-- **Isotypic divisibility.** In a finite-dimensional semisimple module that is
    isotypic of type `S`, every submodule has `k`-dimension divisible by
    `dim_k S`. -/
theorem finrank_dvd_of_isotypic
    {k R : Type*} {M S : Type u} [Field k] [Ring R] [Algebra k R]
    [AddCommGroup M] [Module R M] [Module k M] [IsScalarTower k R M]
    [AddCommGroup S] [Module R S] [Module k S] [IsScalarTower k R S]
    [IsSemisimpleModule R M] [FiniteDimensional k M]
    (hM : IsIsotypicOfType R M S) (N : Submodule R M) :
    finrank k S ∣ finrank k N := by
  haveI : IsSemisimpleModule R N := IsSemisimpleModule.submodule R M
  have hN : IsIsotypicOfType R N S :=
    isIsotypicOfType_submodule_iff.mpr (fun m _ _ => hM m)
  obtain ⟨ι, ⟨e⟩⟩ := hN.linearEquiv_finsupp
  let e' : N ≃ₗ[k] (ι →₀ S) := e.restrictScalars k
  haveI : FiniteDimensional k N :=
    Module.Finite.of_injective ((N.restrictScalars k).subtype) Subtype.val_injective
  haveI : FiniteDimensional k (ι →₀ S) := Module.Finite.equiv e'
  rw [e'.finrank_eq]
  by_cases hS : Nontrivial S
  · obtain ⟨s, hs⟩ := exists_ne (0 : S)
    have hli : LinearIndependent k
        (fun ix : (Σ _ : ι, Unit) => Finsupp.single ix.1 s) :=
      Finsupp.linearIndependent_single (fun _ (_ : Unit) => s)
        (fun _ => linearIndependent_unique _ hs)
    haveI : Finite (Σ _ : ι, Unit) := hli.finite
    haveI : Finite ι := Finite.of_surjective (fun ix : (Σ _ : ι, Unit) => ix.1)
      (fun i => ⟨⟨i, ()⟩, rfl⟩)
    haveI : Fintype ι := Fintype.ofFinite ι
    rcases isEmpty_or_nonempty ι with hι | hι
    · have : finrank k (ι →₀ S) = 0 := finrank_zero_of_subsingleton
      rw [this]; exact dvd_zero _
    · haveI : FiniteDimensional k S :=
        Module.Finite.of_injective
          (Finsupp.lsingle (R := k) (M := S) (Classical.arbitrary ι))
          (Finsupp.single_injective _)
      rw [Module.finrank_finsupp]
      exact Dvd.intro_left _ rfl
  · rw [not_nontrivial_iff_subsingleton] at hS
    have : finrank k (ι →₀ S) = 0 := finrank_zero_of_subsingleton
    rw [this]; exact dvd_zero _

/-- Specialisation to a type of dimension 4 (the `S₅`-type `std ⊗ sgn`). -/
theorem four_dvd_finrank_of_isotypic
    {k R : Type*} {M S : Type u} [Field k] [Ring R] [Algebra k R]
    [AddCommGroup M] [Module R M] [Module k M] [IsScalarTower k R M]
    [AddCommGroup S] [Module R S] [Module k S] [IsScalarTower k R S]
    [IsSemisimpleModule R M] [FiniteDimensional k M]
    (hM : IsIsotypicOfType R M S) (hS : finrank k S = 4) (N : Submodule R M) :
    4 ∣ finrank k N :=
  hS ▸ finrank_dvd_of_isotypic hM N

/-! ### Character data on the classes of `S₅`

Class order: `1, (12), (12)(34), (123), (123)(45), (1234), (12345)`. -/

/-- Conjugacy-class sizes of `S₅`. -/
def classSize : Fin 7 → ℤ := ![1, 10, 15, 20, 20, 30, 24]

/-- `tr(g | H₁(Bring))`: `8` at the identity, `2 − #Fix(g)` otherwise, with
    `#Fix = 6, 2, 0, 0, 2, 4` on the non-trivial classes. -/
def chiH1 : Fin 7 → ℤ := ![8, -4, 0, 2, 2, 0, -2]

/-- Character of the standard representation (permutation character minus 1). -/
def chiStd : Fin 7 → ℤ := ![4, 2, 0, 1, -1, 0, -1]

/-- Character of `std ⊗ sgn`. -/
def chiStdSgn : Fin 7 → ℤ := ![4, -2, 0, 1, 1, 0, -1]

/-- Unnormalised inner product `|G|·⟨χ, ψ⟩` (all characters here are real). -/
def ip (χ ψ : Fin 7 → ℤ) : ℤ := ∑ i, classSize i * χ i * ψ i

/-- **`H₁(Bring, ℚ) = 2·(std ⊗ sgn)`** at the level of characters:
    multiplicity 2 of `std ⊗ sgn`, multiplicity 0 of `std`, norm 4 (so no other
    constituent), and `std ⊗ sgn` has norm 1 (irreducible). -/
theorem bring_H1_character :
    ip chiH1 chiStdSgn = 2 * 120 ∧ ip chiH1 chiStd = 0 ∧
    ip chiH1 chiH1 = 4 * 120 ∧ ip chiStdSgn chiStdSgn = 120 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp [ip, Fin.sum_univ_succ, classSize, chiH1, chiStd, chiStdSgn]

/-- So the character of `H₁` equals twice that of `std ⊗ sgn`, pointwise. -/
theorem chiH1_eq_two_stdSgn : chiH1 = 2 • chiStdSgn := by
  funext i; fin_cases i <;> rfl

/-! ### Consequence for the magic set -/

open QOU.Common

/-- The magic numbers that are multiples of 4 are exactly `8, 20, 28`. -/
theorem magic_four_dvd_iff (n : ℕ) (hn : Saturated n) :
    4 ∣ n ↔ n = 8 ∨ n = 20 ∨ n = 28 := by
  simp only [Saturated, magicSet, Finset.mem_insert, Finset.mem_singleton] at hn
  rcases hn with rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> omega

/-- Four magic numbers are not ranks of `S₅`-stable sub-lattices. -/
theorem magic_not_four_dvd : ¬ 4 ∣ 2 ∧ ¬ 4 ∣ 50 ∧ ¬ 4 ∣ 82 ∧ ¬ 4 ∣ 126 := by
  omega

/-- The realisable-rank predicate `4 ∣ n` disagrees with saturation in both
    directions on `0..126`: `2` is magic and not realisable, `4` is realisable
    and not magic. -/
theorem four_dvd_ne_saturated :
    (Saturated 2 ∧ ¬ 4 ∣ 2) ∧ (4 ∣ 4 ∧ ¬ Saturated 4) := by
  refine ⟨⟨by simp [Saturated, magicSet], by omega⟩, ⟨by omega, ?_⟩⟩
  simp [Saturated, magicSet]

end QOU.ShellCondensation.BringLatticeRanks
