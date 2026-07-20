import Mathlib.Data.Real.Basic

/-!
# QOU.Mass.QDifferenceKernelIsProlongationSymbol — the keystone (E)

Conjecture (`conj:qdifference-kernel-prolongation-symbol`): the
q-difference kernel `R` of the binding generating function
(`prop:binding-genfun-qdifference`) is the **symbol of the jet-prolongation
operator** of the Seiberg–Witten connection (`prop:mi-sw-abelianisation`).

Per AGENTS.md §3b the conjecture is axiomatised as a `class`: an instance
asserts the kernel coincides with the prolongation symbol. This is the
single open input (E) of the step-9b binding closure — (C), (D) and the
recurrence (L3) are proved; only this identification remains, and it is to
be *derived* from the prolonged connection's local monodromy, not fitted.

LaTeX label: `conj:qdifference-kernel-prolongation-symbol`.

## References

- [manuscript] §mass-theory/qdifference-kernel-prolongation-symbol
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4

**Ground ring**: generic `[CommRing R]` (the kernel/symbol coefficients).
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

/-- **Conjecture class (keystone E).** The q-difference kernel coefficients
    `kernel j` coincide with the jet-prolongation operator symbol
    coefficients `prolongationSymbol j`. An instance is the conjecture. -/
class QDifferenceKernelIsProlongationSymbol (R : Type*) [CommRing R] where
  /-- The q-difference kernel coefficients `a_j` (from `R(q,x)`). -/
  kernel : ℕ → R
  /-- The jet-prolongation operator symbol coefficients. -/
  prolongationSymbol : ℕ → R
  /-- The conjecture: the kernel IS the prolongation symbol. -/
  kernel_eq_symbol : ∀ j, kernel j = prolongationSymbol j

/-- Under the keystone, the recurrence kernel is the prolongation symbol —
    so it is structurally fixed, not fitted. -/
theorem kernel_is_prolongation_symbol {R : Type*} [CommRing R]
    [K : QDifferenceKernelIsProlongationSymbol R] (j : ℕ) :
    K.kernel j = K.prolongationSymbol j :=
  K.kernel_eq_symbol j

end QOU.Mass
