/-!
# QOU.Descartes.morse_wall_q_moduli — Morse wall of the integration-limit pencil

The baryon integration-limit Möbius transformation
$f(q) = (4 - q)/(4q + 3)$ has fixed points at $q^2 + q - 1 = 0$ —
i.e. at $1/\varphi$ and $-\varphi$ — and these constitute the
**Morse wall** of the $q$-family of SW actions $S_q$ on $\mathcal{E}_q$:
the algebraic locus where the integration-limit pencil's Möbius
section becomes stationary.

This file states the Laurent-polynomial fixed-point equation over any
field `R` in which `4 ≠ 0` (i.e. characteristic ≠ 2), matching the
narrative setting $\operatorname{Frac}(\mathbb{Z}[q^{\pm 1}])$. The
final cancellation step `4·(q² + q − 1) = 0  ⟹  q² + q − 1 = 0`
genuinely requires both a no-zero-divisors structure and `4 ≠ 0`;
neither is available over an arbitrary `CommRing` (e.g. the equivalence
fails at `R = ℤ/4ℤ`, `q = 0`).  The full equivalence with the
closed-form $\{1/\varphi, -\varphi\}$ over the cyclotomic ring is
deferred (requires `Mathlib.NumberTheory.Cyclotomic` to express
$\sqrt{5} \in \mathbb{Z}[\zeta_5]$ symbolically).

-- Ref: [pham1965] generalised Picard-Lefschetz formula
-- Ref: [seidel2008] Fukaya-Seidel category of a Lefschetz fibration
-- Ref: [arnold-gusein-zade-varchenko1988] Singularities II §10-11
-/

import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp

namespace QOU.Descartes

open Polynomial LaurentPolynomial

/-- The Möbius integration-limit characteristic polynomial.
    Its vanishing locus is the Morse wall. -/
def mobius_fp_poly : Polynomial ℤ := X^2 + X - 1

/-- **Morse-wall identity.**
    Over any field `R` in which `4 ≠ 0`, and an element `q : R` such
    that `4*q + 3` is invertible, the Möbius fixed-point equation
    `a(q) = q` (with `a(q) = (4 - q) / (4*q + 3)`) is equivalent to the
    polynomial identity `q^2 + q - 1 = 0`.

    The `(4 : R) ≠ 0` hypothesis is essential: without it the final
    cancellation `4·(q²+q−1) = 0 ⟹ q²+q−1 = 0` fails (e.g. char 2). -/
-- Ref: [pham1965] generalised Picard-Lefschetz formula
-- Ref: [seidel2008] Fukaya-Seidel category of a Lefschetz fibration
theorem morse_wall_q_moduli
    {R : Type*} [Field R]
    (q : R) (h_inv : IsUnit (4 * q + 3)) (h4 : (4 : R) ≠ 0) :
    (∃ u : R, u * (4 * q + 3) = 1 ∧
      (4 - q) * u = q) ↔
    q ^ 2 + q - 1 = 0 := by
  have h_ne : (4 * q + 3 : R) ≠ 0 := h_inv.ne_zero
  refine ⟨?_, ?_⟩
  · -- (⇒)  Multiply the fixed-point equation by `(4q+3)`, then use
    --      `u*(4q+3) = 1` to clear `u`, then cancel the leading `4`.
    rintro ⟨u, hu, hfix⟩
    have h1 : (4 - q) = q * (4 * q + 3) := by
      have key : (4 - q) * (u * (4 * q + 3)) = q * (4 * q + 3) := by
        rw [← mul_assoc, hfix]
      rwa [hu, mul_one] at key
    have h2 : (4 : R) * (q ^ 2 + q - 1) = 0 := by linear_combination -h1
    exact (mul_eq_zero.mp h2).resolve_left h4
  · -- (⇐)  Take `u := (4q + 3)⁻¹`; the fixed-point equation then
    --      reduces, after clearing the denominator, to `4·(q²+q−1) = 0`,
    --      which holds by hypothesis.
    intro h_poly
    refine ⟨(4 * q + 3)⁻¹, inv_mul_cancel₀ h_ne, ?_⟩
    field_simp
    linear_combination -4 * h_poly

end QOU.Descartes
