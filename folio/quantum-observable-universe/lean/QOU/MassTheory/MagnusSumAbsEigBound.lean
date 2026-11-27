import Mathlib.Algebra.Order.BigOperators.Ring.Finset
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

**Ring symbol for the square root (bean `qou-dk7p`).** The statements are over an arbitrary ordered
field `K`. The square root on the right-hand side is a symbol `s` with `0 ≤ s` and `s² = x`, not a
completed real: it is an element of the algebraic extension `K(√x)`, and a numerical value enters
only when `s` is compared to `ℚ` through a cut. The `ℝ` statements with `Real.sqrt`, under the
original names, are in `QOU/Transcendental/MassTheory/MagnusSumAbsEigBoundReal.lean`.
-/

namespace QOU.MassTheory

open Finset BigOperators

variable {ι : Type*} [Fintype ι]
variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Cauchy–Schwarz, in the form the `Σ|eig|` derivation uses.** For non-negative `a`,
`Σ aᵢ ≤ s` whenever `s ≥ 0` and `s² = card ι · Σ aᵢ²`. This is step (i) of the chain: it is what
converts control of the *squared* moduli (which Schur's inequality supplies, and which the Frobenius
norm computes) into control of `Σ|eig|` itself. -/
theorem sum_le_of_sq_eq_card_mul_sum_sq (a : ι → K) (ha : ∀ i, 0 ≤ a i) (s : K) (hs : 0 ≤ s)
    (hs2 : s ^ 2 = Fintype.card ι * ∑ i, (a i) ^ 2) :
    ∑ i, a i ≤ s := by
  have hcs : (∑ i, a i) ^ 2 ≤ Fintype.card ι * ∑ i, (a i) ^ 2 := by
    have h := sum_mul_sq_le_sq_mul_sq (univ : Finset ι) (fun _ => (1 : K)) a
    simpa [Finset.card_univ, mul_comm] using h
  have hnn : 0 ≤ ∑ i, a i := Finset.sum_nonneg fun i _ => ha i
  rw [← hs2] at hcs
  nlinarith

/-- **The composed bound `(B)`.** Given non-negative `a` (the eigenvalue moduli of `M_λ`) and any
`F` dominating `Σ aᵢ²` — the role played by Schur's inequality together with
`‖M_λ‖_F² = tr_λ(X* X)` — we get `Σ aᵢ ≤ s` for the square-root symbol `s² = card ι · F`. With
`F = tr_λ(X* X)` this is exactly

`Σ_i |eig_i(M_λ)| ≤ √(dim_λ · tr_λ(X* X))`,

whose right-hand side is a positive trace of an algebra element, explicit in the reduced Burau on
the hook column (#6556). Hypothesis-carrying by design: Schur's inequality is the classical input
and is **not** proved here (`_of_` naming per `local/formalizer`). -/
theorem sum_le_of_sq_eq_card_mul_of_sq_le (a : ι → K) (ha : ∀ i, 0 ≤ a i) (F : K)
    (hF : ∑ i, (a i) ^ 2 ≤ F) (s : K) (hs : 0 ≤ s) (hs2 : s ^ 2 = Fintype.card ι * F) :
    ∑ i, a i ≤ s := by
  have hcs : (∑ i, a i) ^ 2 ≤ Fintype.card ι * ∑ i, (a i) ^ 2 := by
    have h := sum_mul_sq_le_sq_mul_sq (univ : Finset ι) (fun _ => (1 : K)) a
    simpa [Finset.card_univ, mul_comm] using h
  have hle : (Fintype.card ι : K) * ∑ i, (a i) ^ 2 ≤ Fintype.card ι * F :=
    mul_le_mul_of_nonneg_left hF (by positivity)
  have hnn : 0 ≤ ∑ i, a i := Finset.sum_nonneg fun i _ => ha i
  have h2 : (∑ i, a i) ^ 2 ≤ s ^ 2 := by rw [hs2]; exact hcs.trans hle
  nlinarith

/-- Tightness at uniform modulus: when every entry equals a constant `c ≥ 0`, the sum equals the
square-root symbol `s` with `s ≥ 0`, `s² = card ι · Σ c²`. -/
theorem sum_const_eq_of_sq_eq_card_mul_sum_sq (c : K) (hc : 0 ≤ c) (s : K) (hs : 0 ≤ s)
    (hs2 : s ^ 2 = Fintype.card ι * ∑ _i : ι, c ^ 2) :
    (∑ _i : ι, c) = s := by
  have hsum : (∑ _i : ι, c) = (Fintype.card ι : K) * c := by
    simp [Finset.sum_const, nsmul_eq_mul]
  have hsum_sq : (∑ _i : ι, c ^ 2) = (Fintype.card ι : K) * c ^ 2 := by
    simp [Finset.sum_const, nsmul_eq_mul]
  have hnn : 0 ≤ (Fintype.card ι : K) * c := by positivity
  rw [hsum_sq] at hs2
  rw [hsum]
  have hsq : s ^ 2 = ((Fintype.card ι : K) * c) ^ 2 := by rw [hs2]; ring
  nlinarith [sq_nonneg (s - (Fintype.card ι : K) * c), sq_nonneg (s + (Fintype.card ι : K) * c)]

end QOU.MassTheory
