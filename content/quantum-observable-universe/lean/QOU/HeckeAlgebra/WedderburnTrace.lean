/-
# The Markov trace against the regular trace

`QOU/HeckeAlgebra/MarkovTrace.lean`'s module doc used to advertise `wenzlBridge`
as

    markovTrace n (wedderburnEmbed x) = Σ_λ y_λ(q_0) · trace (x λ)

That is not what `wenzlBridge` says. Its statement is
`markovTraceOnWedderburn x = Σ_λ y_λ(q_0) · trace (x λ)`, whose left-hand side
*is* that sum by definition — it is proved by `rfl`, and it never mentions an
embedding. Relating a trace on the assembled matrix algebra to the per-block sum
is real content, and until `blockDiagonal` was constructed (bean `qou-usol`)
there was no embedding in the corpus to state it over. The doc was corrected in
`qou-kp2z`; this module supplies what it was reaching for.

## What is proved here

`blockDiagonal_trace` (in `WedderburnConstruction`) gives the regular-representation
side: `trace (blockDiagonal x) = Σ_λ f^λ · trace (x λ)`. Set beside
`markovTraceOnWedderburn x = Σ_λ y_λ(q_0) · trace (x λ)`, the two are **the same
functional form with `y_λ(q_0)` in place of `f^λ`**, and that is stated exactly:

* `markovTrace_sub_regular_trace` — the difference is
  `Σ_λ (y_λ(q_0) − f^λ) · trace (x λ)`, so the deformation is entirely in the
  coefficients and nowhere in the algebra.
* `markovTrace_eq_regular_trace_of_coeff_eq` — they agree when the coefficients
  agree.
* `coeff_eq_of_markovTrace_eq_regular_trace` — and only then. Agreement for
  *every* decomposition forces `y_λ(q_0) = f^λ` for every `λ`, read off the
  single-block indicator. This is the sharp form: the Markov trace is a genuine
  deformation of the regular trace unless the Jones–Markov coefficients are the
  seminormal dimensions.

## What is *not* proved here

Nothing about `markovTrace` on `HeckeElement` — that is `opaque` in
`QOU/HeckeAlgebra/Common.lean` and connecting it to this sum is a separate
obligation. The identity the old doc line stated, with `markovTrace` on the left,
therefore remains unproved; what is proved is the block-sum comparison it should
have said.
-/
import QOU.HeckeAlgebra.WedderburnConstruction
import QOU.HeckeAlgebra.MarkovTrace

namespace QOU.HeckeAlgebra.WedderburnTrace

open QOU.HeckeAlgebra QOU.HeckeAlgebra.Wedderburn QOU.HeckeAlgebra.MarkovTrace
open QOU.HeckeAlgebra.Hoefsmit

variable {n : ℕ}

/-- **The Markov trace is the regular trace with deformed coefficients.** The
difference collapses to a single sum over partitions in which the algebra plays
no part — only `y_λ(q_0) − f^λ` does. -/
theorem markovTrace_sub_regular_trace (x : WedderburnDecomposition n) :
    markovTraceOnWedderburn x - (blockDiagonal x).trace
      = ∑ lam : Nat.Partition n,
          (JonesMarkovCoefficient lam QSubstrate.q_0 - (seminormalDim lam : ℝ))
            * (x lam).trace := by
  classical
  have h1 : markovTraceOnWedderburn x
      = ∑ lam : Nat.Partition n,
          JonesMarkovCoefficient lam QSubstrate.q_0 * (x lam).trace := by
    rw [wenzlBridge]; rfl
  rw [h1, blockDiagonal_trace, ← Finset.sum_sub_distrib]
  exact Finset.sum_congr rfl fun lam _ => by ring

/-- If the Jones–Markov coefficients are the seminormal dimensions, the Markov
trace *is* the regular trace. -/
theorem markovTrace_eq_regular_trace_of_coeff_eq
    (h : ∀ lam : Nat.Partition n,
        JonesMarkovCoefficient lam QSubstrate.q_0 = (seminormalDim lam : ℝ))
    (x : WedderburnDecomposition n) :
    markovTraceOnWedderburn x = (blockDiagonal x).trace := by
  classical
  have := markovTrace_sub_regular_trace x
  rw [show (∑ lam : Nat.Partition n,
        (JonesMarkovCoefficient lam QSubstrate.q_0 - (seminormalDim lam : ℝ))
          * (x lam).trace) = 0 from
      Finset.sum_eq_zero fun lam _ => by rw [h lam]; ring] at this
  linarith

/-- **The single-block indicator.** `blockOne lam` is the decomposition carrying
the identity matrix on block `lam` and zero elsewhere; its block trace is `f^λ`
at `lam` and `0` away from it. This is what turns "the two traces agree on every
`x`" into a statement about the coefficients themselves. -/
noncomputable def blockOne (lam : Nat.Partition n) : WedderburnDecomposition n := by
  classical
  exact fun mu => if h : mu = lam then h ▸ (1 : Matrix (Fin (seminormalDim lam))
    (Fin (seminormalDim lam)) ℝ) else 0

@[simp] theorem blockOne_self (lam : Nat.Partition n) :
    blockOne lam lam = (1 : Matrix (Fin (seminormalDim lam))
      (Fin (seminormalDim lam)) ℝ) := by
  classical
  simp [blockOne]

@[simp] theorem blockOne_of_ne {lam mu : Nat.Partition n} (h : mu ≠ lam) :
    blockOne lam mu = 0 := by
  classical
  simp [blockOne, h]

/-- **Sharpness.** If the Markov trace agrees with the regular trace on *every*
decomposition, the coefficients were the dimensions all along. So any genuine
`q`-deformation of `y_λ` is visible on some element — the bridge is not a
restatement of the regular trace. -/
theorem coeff_eq_of_markovTrace_eq_regular_trace
    (h : ∀ x : WedderburnDecomposition n,
        markovTraceOnWedderburn x = (blockDiagonal x).trace)
    (lam : Nat.Partition n) :
    JonesMarkovCoefficient lam QSubstrate.q_0 = (seminormalDim lam : ℝ) := by
  classical
  have hsub := markovTrace_sub_regular_trace (blockOne lam)
  rw [h (blockOne lam), sub_self] at hsub
  have hterm : ∀ mu ∈ (Finset.univ : Finset (Nat.Partition n)), mu ≠ lam →
      (JonesMarkovCoefficient mu QSubstrate.q_0 - (seminormalDim mu : ℝ))
        * ((blockOne lam) mu).trace = 0 := by
    intro mu _ hne; rw [blockOne_of_ne hne]; simp
  rw [Finset.sum_eq_single lam hterm (by simp)] at hsub
  rw [blockOne_self, Matrix.trace_one, Fintype.card_fin] at hsub
  have hpos : (0 : ℝ) < (seminormalDim lam : ℝ) := by
    exact_mod_cast seminormalDim_pos' lam
  rcases mul_eq_zero.mp hsub.symm with hh | hh
  · exact sub_eq_zero.mp hh
  · linarith

end QOU.HeckeAlgebra.WedderburnTrace
