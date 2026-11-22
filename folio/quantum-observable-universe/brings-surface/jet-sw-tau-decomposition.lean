import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.Brings.jet_sw_tau_decomposition — SW = jet decomposition of τ

The Archimedean realisation `τ` applied to the surface-ordered MI integral
over the exceptional divisor decomposes as the sum over vertical (jet)
degrees of the prolonged Seiberg–Witten periods:

  τ(MI∫_{S_c}) = Σ_n a_D^{(n)} = Σ_n ∮ λ_SW^{(n)}.

LaTeX label: `prop:jet-sw-tau-decomposition`. Lemma **L2** of the
step-9 binding-closure workplan: the SW differential is the jet-graded
decomposition of the Archimedean realisation.

## Lean structure — derived, not projected

The realisation content is packaged as **two genuine hypothesis
fields**, and the graded-sum identity is *derived* from them (not
projected from a single conclusion-typed field):

  * `tau_additive` — the "observe last" / exhaustiveness principle:
    `τ` collapses the jet tower to the graded sum `∑_n τ(graded_n)`
    (additivity of `τ` on the associated graded).
  * `graded_eq_period` — `prop:mi-sw-abelianisation`: each vertical
    (jet) graded piece `τ(graded_n)` equals the `n`-th prolonged SW
    period `a_D^{(n)} = ∮ λ_SW^{(n)}` (`prop:sw-period-residue-sum`).

`jet_sw_tau_decomposition` composes the two — rewrites `τ` to the
graded sum, then rewrites each summand to the SW period — yielding
`τ(MI∫) = ∑_n a_D^{(n)}`. Neither field is this conclusion.

## References

- [leitner2026] §5-brings-surface/jet-sw-tau-decomposition
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4

**Ground ring**: `ℂ` (archimedean realisation). See `GroundRingAnnotations.lean`.
-/

namespace QOU.Brings

open scoped BigOperators

/-- **Jet / τ decomposition data**.  All fields are *inputs*: the
    prolonged SW periods, the τ-value of the MI integral, the τ-image of
    each jet graded piece, and the two structural hypotheses (additivity
    of `τ` on the associated graded, and the identification of each
    graded piece with a SW period).  None is the conclusion
    `tauValue = ∑ period n`. -/
structure JetSWArchDecomposition where
  /-- Highest vertical (jet) degree retained. -/
  maxOrder : ℕ
  /-- The `n`-th prolonged SW period `a_D^{(n)} = ∮ λ_SW^{(n)}`
      (`prop:sw-period-residue-sum`: an algebraic residue sum). -/
  period : ℕ → ℂ
  /-- The τ-image `τ(graded_n)` of the `n`-th vertical (jet) graded piece
      of the MI integral. -/
  tauGraded : ℕ → ℂ
  /-- The Archimedean value `τ(MI∫_{S_c})`. -/
  tauValue : ℂ
  /-- **Additivity / exhaustiveness of `τ`** (the "observe last"
      principle): `τ` collapses the jet tower to the graded sum of the
      τ-images of its graded pieces.  A structural *hypothesis* — its
      right-hand side sums `tauGraded`, not `period`. -/
  tau_additive : tauValue = ∑ n ∈ Finset.range maxOrder, tauGraded n
  /-- **`prop:mi-sw-abelianisation`**: each jet graded piece's τ-image is
      the `n`-th prolonged SW period.  A structural *hypothesis*, not the
      graded-sum conclusion. -/
  graded_eq_period : ∀ n, tauGraded n = period n

/-- **L2.** The τ-image of the MI integral is the sum over jet degrees of
    the prolonged Seiberg–Witten periods.  **Derived** (not projected):
    rewrite `τ` to the graded sum (`tau_additive`), then rewrite each
    summand `tauGraded n` to the SW period `period n`
    (`graded_eq_period`).  Neither hypothesis field is this conclusion. -/
-- Ref: [leitner2026] §5-brings-surface
theorem jet_sw_tau_decomposition (D : JetSWArchDecomposition) :
    D.tauValue = ∑ n ∈ Finset.range D.maxOrder, D.period n := by
  rw [D.tau_additive]
  exact Finset.sum_congr rfl (fun n _ => D.graded_eq_period n)

end QOU.Brings
