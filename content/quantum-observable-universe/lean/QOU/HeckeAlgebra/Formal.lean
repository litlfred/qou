/-!
# QOU.HeckeAlgebra.Formal — pre-archimedean Hecke layer over ℤ[q, q⁻¹]

The **pre-archimedean** Hecke algebra layer, parameterised over
a commutative ring `R` so that:

* `R := ℤ` gives `ℤ[q, q⁻¹]` — the canonical integer-coefficient
  formal Hecke algebra.  This is the **preferred** ground ring
  because it admits clean reduction to F_p for every prime p
  (via `ZMod.castRingHom`), making categorical statements
  about character / trace / structure constants hold in finite
  characteristic.

* `R := ℚ` gives `ℚ[q, q⁻¹]` — needed when denominators force
  rationality (e.g. some Hoefsmit seminormal matrix entries).
  Loses clean F_p reduction at primes dividing the
  denominators.

* `R := ZMod p` gives `F_p[q, q⁻¹]` — direct F_p formal Hecke,
  obtained from `R := ℤ` by reduction mod p.

* `R := ℝ` recovers the archimedean form via realification at
  the QOU substrate value `q_0` (see
  `QOU.HeckeAlgebra.Realification`).

## Design philosophy: F_p compatibility

Per user direction "we want as many stmts to hold in F_p":
state every statement we can over `ℤ[q, q⁻¹]`, falling back
to `ℚ[q, q⁻¹]` only when denominators are unavoidable.
Statements over `ℤ[q, q⁻¹]` reduce automatically to F_p for
every prime; statements with rational denominators only reduce
at primes coprime to those denominators.

## What this module provides

* `HeckeFormalElement R n` — a formal Hecke element as a
  function-space vector over `LaurentPolynomial R`.

* `HeckeFormalAlgebra R n` — abstract formal algebra (axiomatised
  multiplication; concrete construction deferred to a future
  Mathlib port of the Iwahori-Hecke generators).

* Reduction maps to F_p via `LaurentPolynomial.map`.

## ⚠ Archimedean wall

This module lives ENTIRELY on the **pre-archimedean side**.
No real-valued analysis, no PSD machinery, no inner products.
The realification `Hecke_formal R → Hecke_archimedean ℝ` lives
in `QOU.HeckeAlgebra.Realification` and is what crosses the wall.

## References

- [kazhdan-lusztig-1979] *Representations of Coxeter groups and
  Hecke algebras*, Invent. Math. 53 — KL basis with integer
  structure constants over ℤ[q, q⁻¹].
- [hoefsmit1974] Hoefsmit's seminormal form — denominators
  introduce ℚ.
- [wenzl1988] Wenzl's y_λ Jones-Markov coefficients —
  rational-in-q.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic
import QOU.HeckeAlgebra.Common

namespace QOU.HeckeAlgebra.Formal

/-- **Formal Hecke element** over a commutative ring `R`,
    represented as a vector of Laurent polynomials in `R[q, q⁻¹]`.

    For `R := ℤ`, this is the canonical integer-coefficient
    Hecke element — admits clean reduction to F_p for every p.

    Dimension uses the same `heckeDim n = n!` count as the
    archimedean form. -/
abbrev HeckeFormalElement (R : Type*) [CommRing R] (n : ℕ) : Type :=
  Fin (QOU.HeckeAlgebra.heckeDim n) → LaurentPolynomial R

/-- The formal Hecke variable `q` as a `LaurentPolynomial`. -/
abbrev formalQ (R : Type*) [CommRing R] : LaurentPolynomial R :=
  LaurentPolynomial.T 1

/-- The formal Hecke variable `q⁻¹` as a `LaurentPolynomial`. -/
abbrev formalQInv (R : Type*) [CommRing R] : LaurentPolynomial R :=
  LaurentPolynomial.T (-1)

/-- `q · q⁻¹ = 1` in `R[q, q⁻¹]`. -/
theorem formalQ_mul_formalQInv (R : Type*) [CommRing R] :
    formalQ R * formalQInv R = 1 := by
  unfold formalQ formalQInv
  rw [← LaurentPolynomial.T_add]
  norm_num

/-! ### F_p reduction maps

For the `R := ℤ` case, the canonical reduction mod p gives
maps `ℤ[q, q⁻¹] → F_p[q, q⁻¹]`, lifting any statement over ℤ
to one in characteristic p. -/

/-- **Reduction mod p** on Laurent polynomials: applies
    `ZMod.castRingHom` coefficient-wise via
    `LaurentPolynomial.map`. -/
noncomputable def reduceModP (p : ℕ) [Fact p.Prime] :
    LaurentPolynomial ℤ →+* LaurentPolynomial (ZMod p) :=
  LaurentPolynomial.mapRingHom (Int.castRingHom (ZMod p))

/-- Reduction mod p preserves zero. -/
theorem reduceModP_zero (p : ℕ) [Fact p.Prime] :
    reduceModP p 0 = 0 := (reduceModP p).map_zero

/-- Reduction mod p preserves one. -/
theorem reduceModP_one (p : ℕ) [Fact p.Prime] :
    reduceModP p 1 = 1 := (reduceModP p).map_one

/-- Reduction mod p of the formal variable `q`. -/
theorem reduceModP_formalQ (p : ℕ) [Fact p.Prime] :
    reduceModP p (formalQ ℤ) = formalQ (ZMod p) := by
  unfold reduceModP formalQ
  rw [LaurentPolynomial.mapRingHom_T]
  rfl

/-- **Element-wise F_p reduction** of a Hecke formal element
    over ℤ. -/
noncomputable def reduceModP_HeckeFormalElement
    (p : ℕ) [Fact p.Prime] {n : ℕ}
    (x : HeckeFormalElement ℤ n) :
    HeckeFormalElement (ZMod p) n :=
  fun i => reduceModP p (x i)

/-! ### Formal Hecke-algebra interface (axiomatised)

The full categorical structure (Iwahori-Hecke generators
σ_i, T-form vs σ-form relations, KL basis transitions) requires
Mathlib infrastructure not yet in scope.  We axiomatise the
type-level interface here; concrete construction is open work. -/

/-- **Formal Iwahori-Hecke algebra multiplication** over `R`.
    Axiomatised pending Mathlib port of the Hecke generators.

    Concrete structure: T-form generators `T_i ∈ Hecke_formal R n`
    with `T_i² = (q - 1) T_i + q` (relation in `R[q, q⁻¹]`,
    integer-coefficient when `R = ℤ`). -/
axiom heckeFormalMul :
    ∀ {R : Type*} [CommRing R] {n : ℕ},
      HeckeFormalElement R n → HeckeFormalElement R n → HeckeFormalElement R n

/-- **Formal Hecke-algebra unit** — the multiplicative identity. -/
axiom heckeFormalOne :
    ∀ {R : Type*} [CommRing R] (n : ℕ), HeckeFormalElement R n

/-- **T-form Hecke generator** `T_i ∈ Hecke_formal R n`.
    Axiomatised at the type level; concrete construction
    pending Mathlib Iwahori-Hecke port. -/
axiom heckeFormalGenerator :
    ∀ {R : Type*} [CommRing R] {n : ℕ} (_i : Fin (n - 1)),
      HeckeFormalElement R n

/-- **Scalar action** of `R[q, q⁻¹]` on `HeckeFormalElement R n`:
    formal scalar multiplication by a Laurent polynomial. -/
axiom heckeFormalSMul :
    ∀ {R : Type*} [CommRing R] {n : ℕ},
      LaurentPolynomial R → HeckeFormalElement R n → HeckeFormalElement R n

/-- **T-form Hecke relation** (the F_p-friendly form):
    `T_i² = (q − 1) · T_i + q · 1`.

    Integer-coefficient when `R = ℤ`: `q − 1, q ∈ ℤ[q, q⁻¹]`.
    Reducing mod p (when `R = ℤ` then `R = ZMod p`) preserves
    the relation since coefficients are integers — making the
    Hecke relation hold uniformly across all primes.

    Axiomatised pending the concrete algebra structure (the
    Iwahori-Hecke port has not yet landed in Mathlib).
    Pointwise add `+` on `Fin _ → LaurentPolynomial R` uses the
    natural `Pi` ring instance. -/
axiom heckeFormalGenerator_T_relation :
    ∀ {R : Type*} [CommRing R] {n : ℕ} (i : Fin (n - 1)),
      heckeFormalMul (heckeFormalGenerator (R := R) (n := n) i)
                     (heckeFormalGenerator (R := R) (n := n) i) =
      (heckeFormalSMul (formalQ R - 1) (heckeFormalGenerator i)) +
        (heckeFormalSMul (formalQ R) (heckeFormalOne n))

end QOU.HeckeAlgebra.Formal
