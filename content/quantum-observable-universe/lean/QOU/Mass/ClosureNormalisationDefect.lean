import QOU.MathlibExt.MarkovTraceMultiplicative
import QOU.Mass.ArchimedeanTraceBridge
import Mathlib.Tactic

/-!
# Juxtaposition carries one loop factor, so the free energy is not additive

`QOU.MathlibExt.MarkovTraceMultiplicative.markovTrace_juxtapose` proves the matrix identity
`tr(A ⊗ₖ B) = tr A · tr B`, and `QOU.Mass.ArchimedeanTraceBridge.freeEnergy_juxtapose` reads it as
free-energy additivity. Both are correct **about matrices**.

The reading as *knots* is off by exactly one loop factor, and this file makes the defect
machine-checked rather than leaving it as a caveat.

## The measurement that forces this

[`computations/_li_2_q_util.py:777-783`](computations/_li_2_q_util.py) records that the Markov
closure of an `n`-strand braid is normalised by **the loop value raised to `n − 1`**. Juxtaposing an
`m`-strand braid with an `n`-strand braid produces an `m + n`-strand braid, so the normaliser goes

    δ^{m−1} · δ^{n−1} = δ^{m+n−2}    ⟼    δ^{m+n−1}

— **one factor of `δ` that the unnormalised matrix identity does not see.** At the proton-pinned
`q₀ = 1.1099785827513808` the canonical (Wenzl) loop value is `δ = [2]_q = q + q⁻¹ =
2.01089686671`, so `log δ = 0.6985808249` per juxtaposition, and `⁴He` (four components, three
juxtapositions) is short by `≈ 2.096` in free energy.

**Do not read `q + 2 + q⁻¹ = 4.0109` as `δ`.** That figure, which appears in the source line above,
is `δ_C²` — a loop value already raised to `n − 1 = 2` for a three-strand closure. Mistaking it for
`δ` doubles `log δ` to `1.389`.

## What is proved here

`closureNorm δ k t = t / δ^k` is the closure-normalised trace of a `(k+1)`-strand braid whose
unnormalised trace is `t` (indexing by `k = n − 1` keeps the exponent a natural number).

* `closureNorm_juxtapose` — the normalised traces multiply **only after paying `δ`**:
  `closureNorm δ a A * closureNorm δ b B = δ * closureNorm δ (a+b+1) (A*B)`.
* `freeEnergy_closureNorm_juxtapose` — hence the free energy is additive **up to `log δ`**, not
  additive.
* `freeEnergy_closureNorm_additive_iff` — and it is genuinely additive **iff `δ = 1`**, which the
  substrate does not satisfy: `[2]_q = 1` forces `q = 1`, excluded at `q₀ > 1`.
* `loopValue_ne_one` — `[2]_q ≠ 1` for `q > 1`, so the exception never applies here.

## What this does NOT say

The matrix-level results it corrects are **true and stay true**; nothing in
`MarkovTraceMultiplicative` is refuted. What is corrected is the identification of that identity
with the knot-theoretic statement, and specifically the claim that a disjoint trivial component
costs no free energy. It costs `log δ`.

This also does not settle **which** normalisation the framework's mass observable uses. If the
amplitude is already closure-normalised, the defect below applies; if it is the raw matrix trace,
`markovTrace_juxtapose` applies unchanged and the *connected-sum* reading is the one to drop. One of
the two must give — the commit that introduced them claimed both. Bean `qou-bsfg`.
-/

namespace QOU.Mass.ClosureNormalisationDefect

open QOU.Mass.ArchimedeanTraceBridge

variable {R : Type*} [Field R]

/-- The closure-normalised trace of a braid on `k + 1` strands whose unnormalised trace is `t`:
divide by the loop value to the number of strands minus one. Indexed by `k = n − 1` so the exponent
is a natural number. -/
def closureNorm (δ : R) (k : ℕ) (t : R) : R := t / δ ^ k

/-- **Juxtaposition costs one loop factor.** Normalised traces do not simply multiply: combining a
`(a+1)`-strand and a `(b+1)`-strand closure into an `(a+b+2)`-strand one loses one power of `δ`
relative to the product. This is the precise sense in which the unnormalised identity
`tr(A ⊗ₖ B) = tr A · tr B` over-counts. -/
theorem closureNorm_juxtapose {δ : R} (hδ : δ ≠ 0) (a b : ℕ) (A B : R) :
    closureNorm δ a A * closureNorm δ b B = δ * closureNorm δ (a + b + 1) (A * B) := by
  unfold closureNorm
  field_simp
  ring

/-- **So the free energy is additive only up to `log δ`.** Over the reals with positive amplitudes
and a positive loop value, the composite closure-normalised free energy is the sum of the parts
**minus** `log δ` — not the sum. -/
theorem freeEnergy_closureNorm_juxtapose {δ : ℝ} (hδ : 0 < δ) (a b : ℕ) {A B : ℝ}
    (hA : 0 < A) (hB : 0 < B) :
    freeEnergy (closureNorm δ (a + b + 1) (A * B))
      = freeEnergy (closureNorm δ a A) + freeEnergy (closureNorm δ b B) - Real.log δ := by
  have hAn : (0:ℝ) < closureNorm δ a A := by
    unfold closureNorm; exact div_pos hA (pow_pos hδ a)
  have hBn : (0:ℝ) < closureNorm δ b B := by
    unfold closureNorm; exact div_pos hB (pow_pos hδ b)
  have key := closureNorm_juxtapose (ne_of_gt hδ) a b A B
  have hC : closureNorm δ (a + b + 1) (A * B)
      = closureNorm δ a A * closureNorm δ b B / δ := by
    rw [key]; field_simp
  rw [hC]
  unfold freeEnergy
  rw [Real.log_div (ne_of_gt (mul_pos hAn hBn)) (ne_of_gt hδ),
      Real.log_mul (ne_of_gt hAn) (ne_of_gt hBn)]

/-- **Additivity holds exactly when the loop value is trivial.** So `freeEnergy_juxtapose`'s reading
is correct precisely in the case the substrate excludes. -/
theorem freeEnergy_closureNorm_additive_iff {δ : ℝ} (hδ : 0 < δ) (a b : ℕ) {A B : ℝ}
    (hA : 0 < A) (hB : 0 < B) :
    freeEnergy (closureNorm δ (a + b + 1) (A * B))
        = freeEnergy (closureNorm δ a A) + freeEnergy (closureNorm δ b B)
      ↔ δ = 1 := by
  rw [freeEnergy_closureNorm_juxtapose hδ a b hA hB]
  constructor
  · intro h
    have hlog : Real.log δ = 0 := by linarith
    rcases Real.log_eq_zero.mp hlog with h1 | h1 | h1
    · exact absurd h1 (ne_of_gt hδ)
    · exact h1
    · linarith
  · intro h; subst h; simp

/-- The canonical (Wenzl) loop value `δ = [2]_q = q + q⁻¹`. -/
noncomputable def loopValue (q : ℝ) : ℝ := q + q⁻¹

/-- **The substrate never sits at the exceptional point.** For `q > 1` the loop value exceeds one —
`q + q⁻¹ > 1` — so `freeEnergy_closureNorm_additive_iff`'s escape hatch is closed and the `log δ`
term is always present. At `q₀` it is `log 2.01089686671 = 0.6985808249` per juxtaposition. -/
theorem loopValue_ne_one {q : ℝ} (hq : 1 < q) : loopValue q ≠ 1 := by
  have hq0 : (0:ℝ) < q := lt_trans one_pos hq
  have hinv : 0 < q⁻¹ := inv_pos.mpr hq0
  unfold loopValue
  intro h
  linarith

/-! ### `A` components, not two

The section this corrects (`MarkovTraceMultiplicative`, *"Extensivity: `n` disjoint components
multiply"*) states the two-fold case and cites an induction that is not there. With the loop factor
in hand the `A`-fold statement is worth having, because the deficit **grows with `A`** rather than
being a one-off constant.

Joining `A` components with strand counts `n_i = k_i + 1` gives `∑ n_i` strands, so the normaliser
goes from `∏ δ^{n_i − 1} = δ^{∑ k_i}` to `δ^{∑ k_i + (A − 1)}` — the composite is short by
`δ^{A−1}`, and the free energy by `(A − 1)·log δ`. Writing `A = m + 1` keeps the exponent a natural
number. At `q₀`, `⁴He` (`m = 3`) is short by `3 · 0.6985808249 = 2.0957424747`. -/

variable {ι : Type*}

/-- The closure-normalised traces of a family multiply into the normalisation at the **summed**
exponent — the bookkeeping step, with no deficit yet. -/
theorem closureNorm_prod {δ : R} (s : Finset ι) (k : ι → ℕ) (t : ι → R) :
    ∏ i ∈ s, closureNorm δ (k i) (t i)
      = closureNorm δ (∑ i ∈ s, k i) (∏ i ∈ s, t i) := by
  unfold closureNorm
  rw [Finset.prod_div_distrib, Finset.prod_pow_eq_pow_sum]

/-- **The `A`-component deficit is `δ^{A−1}`.** Assembling `m + 1` components multiplies the
normaliser by `δ^m` relative to the product of the parts, so the composite normalised trace is
short by exactly that factor. The two-fold `closureNorm_juxtapose` is `m = 1`. -/
theorem closureNorm_assemble {δ : R} (hδ : δ ≠ 0) (s : Finset ι) (k : ι → ℕ) (t : ι → R) (m : ℕ) :
    δ ^ m * closureNorm δ ((∑ i ∈ s, k i) + m) (∏ i ∈ s, t i)
      = ∏ i ∈ s, closureNorm δ (k i) (t i) := by
  rw [closureNorm_prod s k t]
  unfold closureNorm
  rw [pow_add]
  field_simp

/-- **So the free energy of an `m + 1`-component assembly is short by `m · log δ`** — the deficit is
extensive in the number of components, not a fixed offset. For `⁴He` (`m = 3`) that is
`3 · log [2]_q = 2.0957424747` at the proton-pinned `q₀`. -/
theorem freeEnergy_closureNorm_assemble {δ : ℝ} (hδ : 0 < δ) (s : Finset ι) (k : ι → ℕ)
    {t : ι → ℝ} (ht : ∀ i ∈ s, 0 < t i) (m : ℕ) :
    freeEnergy (closureNorm δ ((∑ i ∈ s, k i) + m) (∏ i ∈ s, t i))
      = (∑ i ∈ s, freeEnergy (closureNorm δ (k i) (t i))) - m * Real.log δ := by
  have hpos : ∀ i ∈ s, (0:ℝ) < closureNorm δ (k i) (t i) := fun i hi => by
    unfold closureNorm; exact div_pos (ht i hi) (pow_pos hδ _)
  have hprod : (0:ℝ) < ∏ i ∈ s, closureNorm δ (k i) (t i) := Finset.prod_pos hpos
  have key := closureNorm_assemble (ne_of_gt hδ) s k t m
  have hC : closureNorm δ ((∑ i ∈ s, k i) + m) (∏ i ∈ s, t i)
      = (∏ i ∈ s, closureNorm δ (k i) (t i)) / δ ^ m := by
    field_simp
    rw [mul_comm]
    exact key
  rw [hC]
  unfold freeEnergy
  rw [Real.log_div (ne_of_gt hprod) (ne_of_gt (pow_pos hδ m)), Real.log_pow,
      Real.log_prod s _ (fun i hi => ne_of_gt (hpos i hi))]

end QOU.Mass.ClosureNormalisationDefect
