import QOU.SchurWeyl.SeminormalRangeTop

/-!
# QOU.SchurWeyl.SeminormalInequivalence — separating the blocks by a central character

The second half of SW-5 (`qou-jfr8`): `ρ_λ ≇ ρ_μ` for `λ ≠ μ`.

The natural first attempt is the central element the corpus already has — `barSymJMSum`, acting by
`cellContentCoshSum λ q`.  **That element cannot work, and the reason is structural rather than a
matter of special `q`.**  The contents of the transpose `λ'` are the negatives of the contents of
`λ`, and `q^{2c} + q^{−2c}` is even in `c`, so the bar-symmetrised sum is *transpose-invariant*: it
takes the same value on `λ` and `λ'` at **every** `q`.  Measured in exact rational arithmetic, at
`n = 7` its 15 partitions collapse to 8 values, and every collision is exactly a transpose pair.
(Recorded as its own item; nothing here depends on it beyond the choice of element.)

What does separate is the **unsymmetrised** Murphy power sum `Σ_k L_k`, which is central under the
same hypothesis (`qJM_sum_comm_sigma'`, sorry-free) and acts by `Σ_{c∈λ} q^{2c}` — no longer even
in `c`, so no longer blind to transposition.

This file proves the two halves that are unconditional:

* `seminormalRep_jmSum` — the block scalar, by the same cell-sweep as `seminormalRep_barSymJMSum`.
* `contentSum_eq_of_intertwiner` — **any** intertwining algebra isomorphism forces the two scalars
  to agree.  Contrapositive: shapes with different content-sums have inequivalent seminormal
  representations.

**What is deliberately not claimed.**  That distinct partitions of `n` have distinct
`Σ_c q^{2c}` *at a given real `q`* is a genuinely separate arithmetic question and is **not**
proved here.  The sums are distinct Laurent polynomials in `q²` (the content multiset determines
the partition), but a nonzero integer Laurent polynomial can vanish at a real `q` that is not a
root of unity, so `q ≠ 0 ∧ q² ≠ 1` does not suffice on its own.  Separation was observed at every
sampled `q` up to `n = 9` in exact arithmetic; that is evidence, not a proof, and it is stated as
such.

LaTeX label: `lem:seminormal-central-character`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep

variable {μ : YoungDiagram}

/-- **The unsymmetrised Murphy power sum acts by the content sum.**  Each `L_k` contributes
`q^{2c}` at the cell holding `k+1`; summing over `k` sweeps every cell of `μ` once
(`sum_cellOf_range`), so the diagonal is constant. -/
theorem seminormalRep_jmSum (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) :
    seminormalRep q hq0 hq2 n hN (∑ k ∈ Finset.range (n + 1), qJM ℝ q q⁻¹ n k)
      = (∑ c ∈ μ.cells, q ^ (2 * cellContent c))
          • (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) := by
  classical
  rw [map_sum]
  have hterm : ∀ k ∈ Finset.range (n + 1),
      seminormalRep q hq0 hq2 n hN (qJM ℝ q q⁻¹ n k)
        = Matrix.diagonal (fun T : StandardYoungTableau μ =>
            q ^ (2 * cellContent (cellOf T (k + 1)))) := by
    intro k hk
    rw [Finset.mem_range] at hk
    rw [seminormalRep_qJM q hq0 hq2 n hN k (by omega), jmDiagVal]
  rw [Finset.sum_congr rfl hterm]
  ext T U
  simp only [Matrix.sum_apply, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
  by_cases h : T = U
  · subst h
    simp only [Matrix.diagonal_apply_eq, if_pos, mul_one]
    exact sum_cellOf_range T hN (fun c => q ^ (2 * cellContent c))
  · simp only [Matrix.diagonal_apply_ne _ h, if_neg h, mul_zero, Finset.sum_const_zero]

/-- **An intertwiner forces the central characters to agree.**  If some algebra isomorphism carries
`ρ_μ` to `ρ_ν`, then `μ` and `ν` have the same content sum `Σ_c q^{2c}` — because the Murphy power
sum is central, so both sides are scalars, and an algebra isomorphism fixes scalars.

Contrapositive: **shapes whose content sums differ have inequivalent seminormal representations.**
This is the separating half of SW-5; the element is the unsymmetrised sum precisely because the
bar-symmetrised one is transpose-blind. -/
theorem contentSum_eq_of_intertwiner {ν : YoungDiagram} (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (n : ℕ) (hMu : μ.cells.card = n + 1) (hNu : ν.cells.card = n + 1)
    (e : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ ≃ₐ[ℝ]
         Matrix (StandardYoungTableau ν) (StandardYoungTableau ν) ℝ)
    (hint : ∀ x, e (seminormalRep q hq0 hq2 n hMu x) = seminormalRep q hq0 hq2 n hNu x) :
    (∑ c ∈ μ.cells, q ^ (2 * cellContent c)) = ∑ c ∈ ν.cells, q ^ (2 * cellContent c) := by
  classical
  have h := hint (∑ k ∈ Finset.range (n + 1), qJM ℝ q q⁻¹ n k)
  rw [seminormalRep_jmSum q hq0 hq2 n hMu, seminormalRep_jmSum q hq0 hq2 n hNu,
    map_smul, map_one] at h
  -- read the equality of scalar matrices off a diagonal entry
  obtain ⟨T⟩ : Nonempty (StandardYoungTableau ν) := inferInstance
  have hT := congrFun (congrFun h T) T
  simpa [Matrix.smul_apply, Matrix.one_apply] using hT

/-! ## Why the bar-symmetrised sum cannot be the separating element

The claim above that `barSymJMSum` is transpose-blind is not an observation — it is a theorem, and
it is what forces the choice of the unsymmetrised sum. -/

/-- **The bar-symmetrised content sum is transpose-invariant.**  Transposing a Young diagram negates
every content, and `q^{2c} + q^{−2c}` is even in `c`, so the sum is unchanged — at **every** `q`.

Consequence: `barSymJMSum` acts by the *same* scalar on `ρ_λ` and `ρ_{λ'}`, so it cannot separate a
partition from its transpose, and cannot be the central character witnessing SW-5's inequivalence
half.  Measured in exact rational arithmetic, the collapse is total: at `n = 7` the 15 partitions
give only 8 distinct values, and every collision is exactly a transpose pair.

This sharpens what `cellContentCoshSum_eq_bracket` already records (that the two bar-even brackets
are not independent spectral degrees of freedom): the invariant is not merely dependent, it is
strictly coarser than the partition. -/
theorem coshSum_transpose (q : ℝ) (μ : YoungDiagram) :
    ∑ c ∈ μ.transpose.cells, (q ^ (2 * cellContent c) + q ^ (-(2 * cellContent c)))
      = ∑ c ∈ μ.cells, (q ^ (2 * cellContent c) + q ^ (-(2 * cellContent c))) := by
  classical
  refine Finset.sum_nbij' Prod.swap Prod.swap (fun c hc => ?_) (fun c hc => ?_)
    (fun c _ => Prod.swap_swap c) (fun c _ => Prod.swap_swap c) (fun c _ => ?_)
  · rw [YoungDiagram.mem_cells] at hc ⊢
    exact YoungDiagram.mem_transpose.mp hc
  · rw [YoungDiagram.mem_cells] at hc ⊢
    exact YoungDiagram.mem_transpose.mpr (by rwa [Prod.swap_swap])
  · -- the summand is even in the content, and transposition negates it
    have hneg : cellContent (Prod.swap c) = -cellContent c := by
      unfold cellContent
      simp only [Prod.fst_swap, Prod.snd_swap]
      ring
    rw [hneg, show -(2 * -cellContent c) = 2 * cellContent c by ring,
      show (2 : ℤ) * -cellContent c = -(2 * cellContent c) by ring]
    exact add_comm _ _

end QOU.SchurWeyl
