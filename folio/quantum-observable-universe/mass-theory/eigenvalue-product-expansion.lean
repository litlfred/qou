/-
  Eigenvalue product expansion of the nuclear braid Markov trace.

  For Z protons and N neutrons, the symmetric channel eigenvalue product is:
    Λ_sym = q^{(Z-N)(A-1)/2} · ([2]/2)^{ZN}

  Its logarithm decomposes into four terms:
    ln|Λ_sym| = ℓ₂·A²/4 + ℓ·T·A - ℓ·T - ℓ₂·T²

  These are the algebraic origins of the BW mass formula terms.

  Ref: [leitner2026] §5.15, prop:eigenvalue-product-expansion
-/

import Mathlib.Algebra.Group.NatPowAssoc
import Mathlib.Algebra.Order.Field.GeomSum
import Mathlib.Algebra.Order.Ring.GeomSum
import Mathlib.Algebra.Ring.Regular
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.BraidKnot

open Finset

/-- The symmetric channel eigenvalue for each crossing type. -/
noncomputable def symEigenvalue (q : ℝ) (crossing_type : String) : ℝ :=
  match crossing_type with
  | "pp" => q                      -- proton-proton: cq+d = q
  | "nn" => 1/q                    -- neutron-neutron: q⁻¹
  | "pn" => (q + 1/q) / 2         -- proton-neutron: [2]/2
  | _ => 1

/-- The crossing-count exponent numerator identity
    `Z(Z-1) - N(N-1) = (Z-N)(Z+N-1)` (the `×2`, division-free form of
    `n_pp - n_nn = (Z-N)(A-1)/2`; both numerators are even, so the halved
    identity follows, but the polynomial identity is the genuine algebraic
    content and is proved here by `ring`). -/
theorem crossing_exponent (Z N : ℤ) :
    Z * (Z - 1) - N * (N - 1) = (Z - N) * (Z + N - 1) := by
  ring

/-- **q-integer as geometric sum.**  The `q`-integer `[c+1]_q` is the
    geometric sum of eigenvalue powers over `c` crossings.  After clearing
    the negative powers (multiply the displayed identity
    `Σ_{j=0}^c q^{c-2j} = (q^{c+1}-q^{-(c+1)})/(q-q⁻¹)` through by `q^c`),
    the content is the real geometric-series identity in `x = q²`:

      `(∑_{k=0}^{c} (q²)^k) · (q² - 1) = (q²)^{c+1} - 1`,

    i.e. `Σ_{k=0}^{c} q^{2k} = (q^{2(c+1)} - 1)/(q² - 1)`.  This is the
    `[c+1]_q` quantum-integer identity, here **derived** from
    `geom_sum_mul` rather than asserted. -/
theorem geometric_sum_is_qint (q : ℝ) (c : ℕ) :
    (∑ k ∈ range (c + 1), (q ^ 2) ^ k) * (q ^ 2 - 1) = (q ^ 2) ^ (c + 1) - 1 :=
  geom_sum_mul (q ^ 2) (c + 1)

/-- The four-term expansion of `ln|Λ_sym|` is exact:

      `ln|Λ_sym| = ℓ₂·A²/4 + ℓ·T·A - ℓ·T - ℓ₂·T²`

    where `A = Z+N`, `T = (Z-N)/2`, `ℓ = ln q`, `ℓ₂ = ln([2]/2)`.  This
    follows from the substitution `Z = A/2+T`, `N = A/2-T` into
    `n_pp - n_nn = T(A-1)` and `n_pn = A²/4 - T²`.

    Stated here as the `ℝ`-coefficient quadratic identity that the
    substitution produces (with the real exponents `t, a` standing for
    `T, A`); the `ℓ`, `ℓ₂` are carried as the log coefficients and the
    identity is the algebraic core proved by `ring`. -/
theorem four_term_expansion (ell ell2 a t : ℝ) :
    ell2 * (a ^ 2 / 4 - t ^ 2) + ell * (t * (a - 1)) =
    ell2 * a ^ 2 / 4 + ell * t * a - ell * t - ell2 * t ^ 2 := by
  ring

end QOU.BraidKnot
