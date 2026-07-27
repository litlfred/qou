/-
# Conjugation-symmetric `Δ_λ` gives zero bar-even binding — a structural exclusion

Building on `ConjugationParitySplit.lean`: the deuteron binding is a `Δ`-dressed Wedderburn sum
`B = m_e Σ_{λ⊢6} T_λ Δ_λ`, `T_λ = w_λ χ^λ`, and under the physical bar `q ↦ q⁻¹` the per-block term
transforms as `T_λ(q⁻¹) = sgn · T_{λ'}(q)` with `sgn = (−1)^{n-1}` (`= −1` for `n = 6`) and `λ'` the
Young-diagram conjugate.

The **bar-even total** (the channel that carries the bar-even coefficient `g₂`) is, up to
normalisation, `S + sgn·(bar image of S)` where `S = Σ_λ T_λ Δ_λ`. This file proves, over a finite
index set with an involution `c` (`= λ ↦ λ'`):

1. a reindexing identity `Σ T_{cλ} Δ_λ = Σ T_λ Δ_{cλ}` (from `c` being a bijection), and
2. **the exclusion:** for `sgn = −1`, if the dressing is conjugation-symmetric (`Δ ∘ c = Δ`) then the
   **bar-even total vanishes**. Since the deuteron's `g₂ ≈ 1 ≠ 0`, **no conjugation-symmetric `Δ_λ`
   can produce the bar-even binding** — a scope-(b) structural exclusion (the proved invariant is
   conjugation symmetry ⇒ zero bar-even).

Numerically (companion probe) the Markov weight `w_λ`, classical `dim(λ)²`, and the hook-form
q-dimension are all conjugation-symmetric ⇒ all excluded; the conjugation-covariant Wenzl principal
specialisation `s_λ(1,q,…,q^{n-1})` survives. This file supplies the *magnitudes*-free structural half;
it does not compute any `Δ_λ` (the Track-A gate).
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

open Finset

namespace QOU.MassTheory.ConjugationParity

variable {I : Type*} {R : Type*} [Fintype I] [CommRing R]

/-- **Reindexing over the conjugation involution.** For a permutation `c` with `c (c p) = p`,
`∑ T (c p) · Δ p = ∑ T p · Δ (c p)` — the bar image can be moved from `T` onto `Δ`. -/
theorem sum_reindex_conj (c : Equiv.Perm I) (hcc : ∀ p, c (c p) = p) (T Δ : I → R) :
    ∑ p, T (c p) * Δ p = ∑ p, T p * Δ (c p) := by
  have h := Equiv.sum_comp c (fun p => T p * Δ (c p))
  -- h : ∑ p, T (c p) * Δ (c (c p)) = ∑ p, T p * Δ (c p)
  simp only [hcc] at h
  exact h

/-- The (unnormalised) **bar-even total** of the `Δ`-dressed Wedderburn sum `S = ∑ T_λ Δ_λ`:
`S + sgn · (bar image of S)`, with `sgn = (−1)^{n-1}` the weight bar-sign. -/
def barEvenTotal (sgn : R) (c : Equiv.Perm I) (T Δ : I → R) : R :=
  (∑ p, T p * Δ p) + sgn * (∑ p, T (c p) * Δ p)

/-- **Per-block form** of the bar-even total: `∑ T_λ · (Δ_λ + sgn·Δ_{λ'})`. -/
theorem barEvenTotal_eq (sgn : R) (c : Equiv.Perm I) (hcc : ∀ p, c (c p) = p) (T Δ : I → R) :
    barEvenTotal sgn c T Δ = ∑ p, T p * (Δ p + sgn * Δ (c p)) := by
  unfold barEvenTotal
  rw [sum_reindex_conj c hcc T Δ, Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun p _ => ?_)
  ring

/-- **The exclusion (deuteron, `sgn = −1`): a conjugation-symmetric dressing kills the bar-even
total.** If `Δ (c p) = Δ p` for all `p`, then `barEvenTotal (−1) c T Δ = 0`. Hence no
conjugation-symmetric `Δ_λ` can supply the deuteron's nonzero bar-even coefficient `g₂`. -/
theorem barEvenTotal_symmetric_zero_deuteron (c : Equiv.Perm I) (hcc : ∀ p, c (c p) = p)
    (T Δ : I → R) (hsym : ∀ p, Δ (c p) = Δ p) :
    barEvenTotal (-1 : R) c T Δ = 0 := by
  rw [barEvenTotal_eq (-1 : R) c hcc T Δ]
  apply Finset.sum_eq_zero
  intro p _
  rw [hsym p]; ring

/-- Contrapositive form: if the bar-even total is nonzero (as for the deuteron `g₂ ≠ 0`), the dressing
is **not** conjugation-symmetric — it must differ on some conjugate pair `Δ_λ ≠ Δ_{λ'}`. -/
theorem barEven_nonzero_implies_asymmetric (c : Equiv.Perm I) (hcc : ∀ p, c (c p) = p)
    (T Δ : I → R) (hne : barEvenTotal (-1 : R) c T Δ ≠ 0) :
    ∃ p, Δ (c p) ≠ Δ p := by
  by_contra h
  push_neg at h
  exact hne (barEvenTotal_symmetric_zero_deuteron c hcc T Δ h)

end QOU.MassTheory.ConjugationParity
