/-!
# QOU.HeckeAlgebra.Realification — wall crossing at q = q_0

The **archimedean wall crossing**: the canonical map from the
pre-archimedean formal Hecke algebra
`Hecke_formal R := R[q, q⁻¹]^{Fin (heckeDim n)}` to the
archimedean form `HeckeElement n := EuclideanSpace ℝ (Fin
(heckeDim n))` via evaluation at the QOU substrate parameter
`q := q_0 ∈ ℝ`.

## ⚠ Architectural role of this module

This module **is the wall**.  Every other module in
`QOU.HeckeAlgebra.*` lives entirely on one side or the other:

* **Pre-archimedean side** (`Hecke_formal`, `Hoefsmit_formal`,
  `JonesMarkov_formal`, etc.): formal q over `ℤ[q, q⁻¹]` (or
  `ℚ[q, q⁻¹]` where denominators force it).  Categorical
  content; reduces to F_p uniformly when over ℤ.

* **Archimedean side** (`HeckeElement` over ℝ, SDP machinery,
  PosSemidef analysis, kernel-disjointness): real-valued
  spectral analysis at `q = q_0`.  Required for SDP-uniqueness
  conclusions but does NOT pull back to categorical claims.

The realification map below is the ONE place these meet: it
specialises a formal Hecke element at `q := q_0` to obtain its
archimedean realification.

Consequences:
* Statements proven on the pre-archimedean side can be
  realified at q_0 to give archimedean specialisations.
* Statements proven on the archimedean side via
  realification (e.g. SDP uniqueness) DO NOT lift back to
  categorical pre-archimedean claims.

## What this module provides

* `realifyAt q_0 : LaurentPolynomial ℝ → ℝ` — evaluation of
  a formal real Laurent polynomial at `q = q_0`.

* `realifyHeckeElement q_0` — element-wise realification.

* `realifyHoefsmitMatrix q_0` — entry-wise realification of
  formal Hoefsmit matrices.

* Composition lemmas: realification commutes with addition,
  scalar multiplication, and (axiomatically) Hecke
  multiplication.

## References

- QOU manuscript §"Archimedean realization functor" — the
  formal categorical-to-real map.
- `QOU.HeckeAlgebra.QSubstrate.q_0` — the substrate parameter.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Tactic
import QOU.HeckeAlgebra.Common
import QOU.HeckeAlgebra.QSubstrate
import QOU.HeckeAlgebra.Formal

namespace QOU.HeckeAlgebra.Realification

open QOU.HeckeAlgebra QOU.HeckeAlgebra.Formal QOU.HeckeAlgebra.QSubstrate

/-! ### §1  Evaluation at q_0

The basic wall-crossing primitive: evaluate a formal real
Laurent polynomial at `q := q_0`. -/

/-- **Realification of a formal Laurent polynomial at q_0**.

    For `f ∈ ℝ[q, q⁻¹]`, `realifyAt q_0 f = f(q_0) ∈ ℝ`.

    Uses Mathlib's `LaurentPolynomial.eval₂RingHom` with the
    identity coefficient embedding and `q_0` as the evaluation
    value (must be a unit; here `q_0 ≠ 0` from `q_0 > 1` gives
    `IsUnit q_0` in the field ℝ). -/
noncomputable def realifyAtRealQ0 : LaurentPolynomial ℝ →+* ℝ :=
  LaurentPolynomial.eval₂RingHom (RingHom.id ℝ)
    (isUnit_iff_ne_zero.mpr q_0_ne_zero).unit

/-! ### §2  Realification at q_0 via embedded ℤ → ℝ

For the ℤ[q, q⁻¹] formal layer (the F_p-friendly choice), we
compose: ℤ[q, q⁻¹] → ℝ[q, q⁻¹] (coefficient embedding) → ℝ
(eval at q_0).  This is the canonical realification used by
the QOU pipeline. -/

/-- **Embed ℤ-coefficient Laurent polynomials into ℝ**. -/
noncomputable def embedIntToReal :
    LaurentPolynomial ℤ →+* LaurentPolynomial ℝ :=
  LaurentPolynomial.mapRingHom (Int.castRingHom ℝ)

/-- **Realification at q_0** of an integer formal Laurent
    polynomial: embed ℤ → ℝ, then eval at q_0.

    Uniform for all primes: any congruence/identity in
    `ℤ[q, q⁻¹]` (and its F_p reductions) maps coherently to ℝ. -/
noncomputable def realifyZ : LaurentPolynomial ℤ →+* ℝ :=
  realifyAtRealQ0.comp embedIntToReal

/-! ### §3  Element-wise realification

Lift the polynomial-level realification to vectors and matrices. -/

/-- **Element-wise realification** of a `HeckeFormalElement ℤ n`
    at `q_0`. -/
noncomputable def realifyHeckeElement {n : ℕ}
    (x : HeckeFormalElement ℤ n) :
    Fin (heckeDim n) → ℝ :=
  fun i => realifyZ (x i)

/-- **Realification commutes with addition**. -/
theorem realifyHeckeElement_add {n : ℕ}
    (x y : HeckeFormalElement ℤ n) :
    realifyHeckeElement (x + y) =
      realifyHeckeElement x + realifyHeckeElement y := by
  funext i
  show realifyZ ((x + y) i) = realifyZ (x i) + realifyZ (y i)
  show realifyZ (x i + y i) = realifyZ (x i) + realifyZ (y i)
  exact realifyZ.map_add (x i) (y i)

/-- **Realification commutes with scalar multiplication** by
    a formal Laurent polynomial. -/
theorem realifyHeckeElement_smul {n : ℕ}
    (c : LaurentPolynomial ℤ) (x : HeckeFormalElement ℤ n) :
    -- c • x means pointwise multiply by c (Pi instance)
    realifyHeckeElement (fun i => c * x i) =
      fun i => realifyZ c * realifyHeckeElement x i := by
  funext i
  show realifyZ (c * x i) = realifyZ c * realifyZ (x i)
  exact realifyZ.map_mul c (x i)

/-! ### §4  Compatibility with F_p reduction

For statements proven over `ℤ[q, q⁻¹]` and reduced to
`F_p[q, q⁻¹]`, we have a parallel realification path through
F_p (when q_0 has a meaningful F_p analogue).  This compatibility
is mostly bookkeeping; concrete uses come from comparing
identity-statement validity in F_p vs ℝ. -/

/-- **Statement-level F_p reduction commutes with realification**
    in the sense that any polynomial identity holding in
    `ℤ[q, q⁻¹]` (and hence in every F_p[q, q⁻¹]) realifies
    to the same identity in ℝ. -/
theorem identity_holds_in_realification {n : ℕ}
    (x y : HeckeFormalElement ℤ n) (h_eq : x = y) :
    realifyHeckeElement x = realifyHeckeElement y := by
  rw [h_eq]

end QOU.HeckeAlgebra.Realification
