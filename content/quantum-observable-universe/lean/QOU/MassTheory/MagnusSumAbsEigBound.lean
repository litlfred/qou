import Mathlib.Analysis.MeanInequalities
import Mathlib.Analysis.SpecialFunctions.Pow.NNRpow
import Mathlib.Algebra.Order.Chebyshev
import Mathlib.Tactic

/-!
# The bound on `Σ|eig(M_λ)|` — the Cauchy–Schwarz step, formalized (qou-o6ov)

**Context.** #6556 established that the `b(λ)`-decay of `|tr_λ(ρΩ₂^P)|` is carried by the
magnitude factor `Σ_i |eig_i(M_λ)|`, with `M_λ = ρ_λ(ρ)·ρ_λ(Ω₂^P)`, and that
`‖M_λ‖_F² = tr_λ(X* X)` for `X = ρ·Ω₂^P` — a *positive* trace of a Hecke algebra element, whose
hook-column closed form in the reduced Burau is derived there. What was missing was a bound on
`Σ|eig|` itself. The derivation is three steps:

```
(i)   Σ_i |eig_i(M)|  ≤ √(dim · Σ_i |eig_i(M)|²)      Cauchy–Schwarz on the moduli vector
(ii)  Σ_i |eig_i(M)|² ≤ ‖M‖_F²                        Schur's inequality
(iii) ‖M_λ‖_F²        = tr_λ(X* X)                    anti-involution identity (#6556)
      ⟹  Σ_i |eig_i(M_λ)| ≤ √(dim_λ · tr_λ(X* X))                                    (B)
```

**What is formalized here is step (i), and step (i) only** — the one step that is pure inequality
over an arbitrary finite index set, with no matrix theory in it. `sum_le_sqrt_card_mul_sum_sq` is
Cauchy–Schwarz in the form the derivation uses; `sum_le_sqrt_card_mul_of_sq_le` composes it with a
hypothesis `Σ aᵢ² ≤ F`, which is exactly the shape step (ii) supplies, and yields `(B)`'s
right-hand side.

**What is NOT formalized, and is carried as a hypothesis rather than asserted:** Schur's inequality
(ii) is a classical theorem about the eigenvalues of a complex matrix (via Schur triangularization)
and is not proved here; `sum_le_sqrt_card_mul_of_sq_le` takes it as the hypothesis `hF`. The
identity (iii) is the measured anti-involution fact of #6556. The Hecke-specific content — the
seminormal construction, the atom word, the reduced-Burau closed form for `tr_λ(X*X)` — is outside
Mathlib, as in the sibling files.

**Honest note on strength.** Step (i) costs a factor up to `√dim` and is tight only when all
`|eig_i|` are equal. Measured on this corpus the resulting bound gives away a factor 2–6
(tightness `Σ|eig| / √(dim·tr(X*X))` runs 0.16–0.48). It is a *usable* bound — it holds and it
decays with `b` at controlled dimension — not a sharp one.

This is the archimedean side (`Real.sqrt`, an order), kept in its own file per §7c so the algebraic
siblings stay over a bare `CommRing`.
-/

namespace QOU.MassTheory

open Finset BigOperators

variable {ι : Type*} [Fintype ι]

/-- **Cauchy–Schwarz, in the form the `Σ|eig|` derivation uses.** For non-negative `a`,
`Σ aᵢ ≤ √(card ι · Σ aᵢ²)`. This is step (i) of the chain: it is what converts control of the
*squared* moduli (which Schur's inequality supplies, and which the Frobenius norm computes) into
control of `Σ|eig|` itself. -/
theorem sum_le_sqrt_card_mul_sum_sq (a : ι → ℝ) (ha : ∀ i, 0 ≤ a i) :
    ∑ i, a i ≤ Real.sqrt (Fintype.card ι * ∑ i, (a i) ^ 2) := by
  have hcs : (∑ i, a i) ^ 2 ≤ Fintype.card ι * ∑ i, (a i) ^ 2 := by
    simpa [Finset.card_univ] using
      (Finset.sq_sum_le_card_mul_sum_sq (s := (univ : Finset ι)) (f := a))
  have hnn : 0 ≤ ∑ i, a i := Finset.sum_nonneg fun i _ => ha i
  calc ∑ i, a i = Real.sqrt ((∑ i, a i) ^ 2) := (Real.sqrt_sq hnn).symm
    _ ≤ Real.sqrt (Fintype.card ι * ∑ i, (a i) ^ 2) := Real.sqrt_le_sqrt hcs

/-- **The composed bound `(B)`.** Given non-negative `a` (the eigenvalue moduli of `M_λ`) and any
`F` dominating `Σ aᵢ²` — the role played by Schur's inequality together with
`‖M_λ‖_F² = tr_λ(X* X)` — we get `Σ aᵢ ≤ √(card ι · F)`. With `F = tr_λ(X* X)` this is exactly

`Σ_i |eig_i(M_λ)| ≤ √(dim_λ · tr_λ(X* X))`,

whose right-hand side is a positive trace of an algebra element, explicit in the reduced Burau on
the hook column (#6556). Hypothesis-carrying by design: Schur's inequality is the classical input
and is **not** proved here (`_of_` naming per `local/formalizer`). -/
theorem sum_le_sqrt_card_mul_of_sq_le (a : ι → ℝ) (ha : ∀ i, 0 ≤ a i) (F : ℝ)
    (hF : ∑ i, (a i) ^ 2 ≤ F) :
    ∑ i, a i ≤ Real.sqrt (Fintype.card ι * F) := by
  refine (sum_le_sqrt_card_mul_sum_sq a ha).trans (Real.sqrt_le_sqrt ?_)
  exact mul_le_mul_of_nonneg_left hF (by positivity)

end QOU.MassTheory
