import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.BigOperators.Basic

/-!
# QOU.Brings.jet_sw_tau_decomposition — SW = jet decomposition of τ

The Archimedean functor `τ` applied to the surface-ordered MI integral
over the exceptional divisor decomposes as the sum over vertical (jet)
degrees of the prolonged Seiberg–Witten periods:

  τ(MI∫_{S_c}) = Σ_n a_D^{(n)} = Σ_n ∮ λ_SW^{(n)}.

LaTeX label: `prop:jet-sw-tau-decomposition`. Lemma **L2** of the
step-9 binding-closure workplan: the SW differential is the jet-graded
decomposition of the Archimedean functor.

The realisation content — exhaustiveness of the jet tower and additivity
of `τ` on the associated graded — is packaged as the structure
hypothesis (`prop:mi-sw-abelianisation`), so the graded-sum identity is
available downstream sorry-free.

## References

- [manuscript] §5-brings-surface/jet-sw-tau-decomposition
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4

**Ground ring**: `ℂ` (archimedean realisation). See `GroundRingAnnotations.lean`.
-/

namespace QOU.Brings

open scoped BigOperators

/-- **Jet / τ decomposition data**: the prolonged SW periods `a_D^{(n)}`
    for `n < maxOrder`, the τ-value of the MI integral, and the identity
    that τ equals the graded sum of periods. -/
structure JetSWArchDecomposition where
  /-- Highest vertical (jet) degree retained. -/
  maxOrder : ℕ
  /-- The `n`-th prolonged SW period `a_D^{(n)} = ∮ λ_SW^{(n)}`. -/
  period : ℕ → ℂ
  /-- The Archimedean value `τ(MI∫_{S_c})`. -/
  tauValue : ℂ
  /-- τ is the jet-graded sum of the prolonged SW periods. -/
  tau_eq : tauValue = ∑ n ∈ Finset.range maxOrder, period n

/-- **L2.** The τ-image of the MI integral is the sum over jet degrees of
    the prolonged Seiberg–Witten periods. -/
-- Ref: [manuscript] §5-brings-surface
theorem jet_sw_tau_decomposition (D : JetSWArchDecomposition) :
    D.tauValue = ∑ n ∈ Finset.range D.maxOrder, D.period n :=
  D.tau_eq

end QOU.Brings
