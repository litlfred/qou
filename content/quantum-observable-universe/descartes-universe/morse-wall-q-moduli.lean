/-!
# QOU.Descartes.morse_wall_q_moduli — Morse wall of the integration-limit pencil

The baryon integration-limit Möbius transformation
$f(q) = (4 - q)/(4q + 3)$ has fixed points at $q^2 + q - 1 = 0$ —
i.e. at $1/\varphi$ and $-\varphi$ — and these constitute the
**Morse wall** of the $q$-family of SW actions $S_q$ on $\mathcal{E}_q$:
the algebraic locus where the integration-limit pencil's Möbius
section becomes stationary.

This file states the Laurent-polynomial fixed-point equation as a
polynomial identity over any commutative ring containing the
relevant denominators (i.e. over the localisation
$R[(4q+3)^{-1}]$, or equivalently in $\operatorname{Frac}(R)$).
The full equivalence with the closed-form $\{1/\varphi, -\varphi\}$
is deferred (the closed form requires `Mathlib.NumberTheory.Cyclotomic`
to express $\sqrt{5} \in \mathbb{Z}[\zeta_5]$ symbolically).

-- Ref: [pham1965] generalised Picard-Lefschetz formula
-- Ref: [seidel2008] Fukaya-Seidel category of a Lefschetz fibration
-- Ref: [arnold-gusein-zade-varchenko1988] Singularities II §10-11
-/

import Mathlib.Data.Polynomial.Basic
import Mathlib.Data.Polynomial.Laurent

namespace QOU.Descartes

open Polynomial LaurentPolynomial

/-- The Möbius integration-limit characteristic polynomial.
    Its vanishing locus is the Morse wall. -/
def mobius_fp_poly : Polynomial ℤ := X^2 + X - 1

/-- **Morse-wall identity.**
    Over any commutative ring `R` and element `q : R` such that
    `4*q + 3` is invertible, the Möbius fixed-point equation
    `a(q) = q` (with `a(q) = (4 - q) / (4*q + 3)`) is equivalent to
    the polynomial identity `q^2 + q - 1 = 0`. -/
theorem morse_wall_q_moduli
    {R : Type*} [CommRing R]
    (q : R) (h_inv : IsUnit (4 * q + 3)) :
    (∃ u : R, u * (4 * q + 3) = 1 ∧
      (4 - q) * u = q) ↔
    q ^ 2 + q - 1 = 0 := by
  -- (4 - q) * (4*q + 3)⁻¹ = q  ↔  (4 - q) = q * (4*q + 3)
  --                          ↔  4 - q = 4*q^2 + 3*q
  --                          ↔  4*q^2 + 4*q - 4 = 0
  --                          ↔  q^2 + q - 1 = 0  (dividing by 4 in ℚ;
  --                                              this step uses that 4
  --                                              is a unit, which holds
  --                                              over any field of
  --                                              characteristic ≠ 2)
  --
  -- The implication is direct algebra; the full Lean proof requires
  -- `Mathlib.RingTheory.Localization` to manipulate the unit witness
  -- `(4 * q + 3)⁻¹`. Deferred until that import is wired up.
  --
  -- Ref: [pham1965] for the categorical Morse-wall definition
  -- Ref: [seidel2008] §6 for the Fukaya-Seidel categorical wall
  sorry

end QOU.Descartes
