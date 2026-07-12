import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Data.Nat.Cast.Field

/-!
# QOU.AppendixSurreals.EcalleBorelResummation

Sibling formalisation for content block
[`def:ecalle-borel-resummation`](ecalle-borel-resummation.md):
the coefficient-level formal Borel transform `a n ↦ a n / n !`.

Per AGENTS.md §7c the transform is stated over a generic
`{R : Type*} [Field R] [CharZero R]` — no archimedean structure is
needed at the coefficient level. The ℝ-specialised **analytic**
scaffold (Laplace–Borel integral, `BorelSummable`, Nevanlinna–Sokal
placeholders) lives in the library file
`QOU/Mathlib/BorelResummation.lean`; it is deliberately **not**
imported here (heavy-import avoidance + §7c wall discipline).

-- Ref: [ecalle1981] Écalle, *Les fonctions résurgentes*, Tome I,
--      Publ. Math. d'Orsay 81-05 (1981).
-/

namespace QOU.AppendixSurreals.EcalleBorelResummation

variable {R : Type*} [Field R] [CharZero R]

/--
The **coefficient-level formal Borel transform**: the sequence of
coefficients `a : ℕ → R` of a formal series `Σ aₙ z^{-n-1}` is sent to
the coefficient sequence `aₙ / n!` of its Borel transform
`𝓑f̃(ξ) = Σ aₙ ξⁿ / n!`. This is the exact division that converts
Gevrey-1 (factorial) growth `aₙ = O(n! · A^{-n})` into geometric
growth `O(A^{-n})`, i.e. into a germ analytic on `|ξ| < A`.
-/
noncomputable def borelCoeff (a : ℕ → R) (n : ℕ) : R :=
  a n / (Nat.factorial n : R)

/--
Normalisation check: the Borel transform flattens the archetypal
Gevrey-1 sequence `aₙ = n!` to the constant sequence `1` — the Borel
transform of Euler's factorially divergent series is the geometric
germ `1 / (1 - ξ)`, coefficient by coefficient.
-/
theorem borelCoeff_factorial (n : ℕ) :
    borelCoeff (fun k => (Nat.factorial k : R)) n = 1 :=
  div_self (Nat.cast_ne_zero.mpr n.factorial_ne_zero)

end QOU.AppendixSurreals.EcalleBorelResummation
