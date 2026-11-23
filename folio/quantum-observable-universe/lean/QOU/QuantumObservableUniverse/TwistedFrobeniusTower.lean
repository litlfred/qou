/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.QuantumObservableUniverse.NakayamaTwist

/-!
# A tower of finite Frobenius levels: boundary-to-bulk compatibility

This file sets up the limited bulk/boundary structure of option B. We use a tower of
finite levels, not the full symmetric tower `Sym(Ω¹)`. Owner ruling 104 records that the
full tower drops the Frobenius structure at `n ≥ 1`, and a Nakayama twist does not
change that, because a Frobenius form forces finite rank.

Data over a commutative ring `R`:

* algebras `A n`, with forms `τ n : A n →ₗ[R] R`;
* inclusions `ι n : A n →ₐ[R] A (n+1)`;
* conditional expectations `E n : A (n+1) →ₗ[R] A n` with
  `E n (ι n a) = a`, `E n (y * ι n a) = E n y * a`, and `τ (n+1) = τ n ∘ E n`.

This is a Frobenius-extension tower in the sense of Kadison. The levels need not be
symmetric. Each may carry its own Nakayama twist (`Nakayama.frobMap_mul_nu`).

Proved here, with no `sorry`:

* `iota_injective`: each inclusion is injective;
* `frobMap_iota`: the level `n+1` Frobenius functional of `ι a`, restricted along `ι`,
  is the level `n` functional of `a` (boundary data is compatible upward);
* `frobMap_iota_eq_comp`: that functional factors through `E`, so it is the level-`n`
  functional pulled back along `E` (bulk data is determined by the lower level);
* `frobMap_iota_injective`: given nondegeneracy at level `n+1`, the composite
  `a ↦ φ_{n+1}(ι a)` is injective.

Not done here, and open: the packaging of the colimit (boundary) and the limit of
duals (bulk) as objects with a comparison map, compatibility of the twists
`ν (n+1) ∘ ι n = ι n ∘ ν n`, and any analogue at real `q₀` on `Sym(Ω¹)`.

## References
- Kadison, *New examples of Frobenius extensions*, AMS University Lecture Series 14 (1999). Not yet in the bibliography.
- [lorenz2011] Nakayama automorphism of a Frobenius algebra.
- [leitner2026] §1 Categorical foundations.
-/

namespace QOU.QuantumObservableUniverse.Tower

open QOU.QuantumObservableUniverse.Nakayama

variable {R : Type*} [CommRing R]
variable {A : ℕ → Type*} [∀ n, Ring (A n)] [∀ n, Algebra R (A n)]
variable (τ : ∀ n, A n →ₗ[R] R) (ι : ∀ n, A n →ₐ[R] A (n + 1))
variable (E : ∀ n, A (n + 1) →ₗ[R] A n)

include E in
/-- The inclusions are injective, because `E n` is a left inverse. -/
theorem iota_injective (hE : ∀ n a, E n (ι n a) = a) (n : ℕ) :
    Function.Injective (ι n) := by
  intro a b h
  rw [← hE n a, ← hE n b, h]

/-- **Boundary compatibility.** Restricting the level `n+1` functional of `ι a`
along `ι` gives the level `n` functional of `a`. -/
theorem frobMap_iota (hτ : ∀ n y, τ (n + 1) y = τ n (E n y))
    (hE : ∀ n a, E n (ι n a) = a) (n : ℕ) (a x : A n) :
    frobMap (τ (n + 1)) (ι n a) (ι n x) = frobMap (τ n) a x := by
  simp only [frobMap]
  rw [← map_mul, hτ, hE]

/-- **Bulk factorisation.** The level `n+1` functional of `ι a` is the level `n`
functional of `a` composed with the conditional expectation. -/
theorem frobMap_iota_eq_comp (hτ : ∀ n y, τ (n + 1) y = τ n (E n y))
    (hEmod : ∀ n y a, E n (y * ι n a) = E n y * a) (n : ℕ) (a : A n) (y : A (n + 1)) :
    frobMap (τ (n + 1)) (ι n a) y = frobMap (τ n) a (E n y) := by
  simp only [frobMap]
  rw [hτ, hEmod]

include E in
/-- Given nondegeneracy at level `n+1`, the map `a ↦ φ_{n+1}(ι a)` is injective. -/
theorem frobMap_iota_injective (hE : ∀ n a, E n (ι n a) = a) (n : ℕ)
    (hnd : ∀ y : A (n + 1), (∀ x, τ (n + 1) (x * y) = 0) → y = 0) :
    Function.Injective (fun a : A n => frobMap (τ (n + 1)) (ι n a)) :=
  (frobMap_injective (τ (n + 1)) hnd).comp (iota_injective ι E hE n)

end QOU.QuantumObservableUniverse.Tower
