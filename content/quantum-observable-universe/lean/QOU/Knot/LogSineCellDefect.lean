/-
# L4-1a — the exact cell-defect representation (bean qou-me9q, epic qou-u1b5)

First sub-brick of L4-1 (the second-order log-sine expansion, feasibility
pass `docs/audits/2026-08-11-l41-euler-maclaurin-feasibility.md`): the
Riemann-sum defect of the corpus log-sine sums against the Clausen
primitive is EXACTLY the sum of per-cell integrals of `f(x_j) − f(u)` —
no estimate, pure rearrangement:

    (π/N)·S(n) − F(nπ/N) = Σ_{j=1}^{n} ∫_{(j−1)π/N}^{jπ/N}
                              ( log(2 sin(jπ/N)) − log(2 sin u) ) du,

with `S(n) = Σ_{j≤n} log(2 sin(jπ/N))` and `F(x) = −clausen(2x)/2 =
∫₀^x log(2 sin u) du`.  The E5c masterErr bricks bound each cell crudely
(`O(1)` total); vdV's Lemma-2 refinement (L4-1b Stirling + L4-1c uniform
remainder) will evaluate this same right-hand side to
`−½·log(n·sin(rπ)/(rπ)) + O(1/N)`.  Recording the representation exactly,
with no range restriction on `n` (the identity is formal — every
ingredient holds for arbitrary grid points), is what lets the later
bricks work term-by-term.
-/

/-
**REDUNDANT (2026-08-19) — L4-1's target was already proved on `main`, stronger,
before this file was written.**

`QOU.Knot.FigureEightVolume.kashaev_log_sum_asymptotic`
(`QOU/Knot/KashaevAsymptotic.lean`, on main since 2026-08-10, sorry-free) gives

    | ∑_{j=1}^{k} log(2 sin(jπ/N))
        − ( −(N/π)·Lob(kπ/N) + ½·log(2N·sin(kπ/N)) + (π/(12N))·cot(kπ/N) ) |
      ≤ 1/(144k²) + (7/12)(π/N)² + (π/N)²/(12·sin²(kπ/N))

— strictly stronger than the L4-1 target this file serves: it identifies the
`O(1/N)` term and its error is effective.  The decomposition L4-1 was organised
around is `KashaevEndpointSplit.sum_log_two_sin_split`, exact algebra with no
cell integrals and no telescope.

Kept, not deleted: the proofs here are correct and sorry-free.  **New
downstream work should cite `kashaev_log_sum_asymptotic`, not this file.**
Audit: `docs/audits/2026-08-19-l41-was-already-proved-on-main.md`.
-/

import QOU.Knot.Clausen

namespace QOU.Knot.FigureEightVolume

open Real MeasureTheory

/-- **L4-1a — the exact cell-defect representation (sorry-free).**  The
    scaled log-sine sum minus the Clausen primitive equals the sum of the
    per-cell integrals of `f(x_j) − f(u)`, exactly. -/
theorem cell_defect_repr {N : ℕ} (n : ℕ) (hN : 1 ≤ N) :
    (π / N) * (∑ j ∈ Finset.Icc 1 n,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      - (-clausen (2 * ((n : ℝ) * (π / N))) / 2)
      = ∑ j ∈ Finset.Icc 1 n,
          ∫ u in (((j : ℝ) - 1) * (π / N))..((j : ℝ) * (π / N)),
            (Real.log (2 * Real.sin ((j : ℝ) * (π / N)))
              - Real.log (2 * Real.sin u)) := by
  have hpi := Real.pi_pos
  -- the grid, and the total integral as the Clausen primitive
  have hadd := intervalIntegral.sum_integral_adjacent_intervals
    (a := fun k : ℕ => (k : ℝ) * (π / N)) (n := n)
    (f := fun u => Real.log (2 * Real.sin u)) (μ := volume)
    (fun k _ => intervalIntegrable_log_two_sin _ _)
  simp only [Nat.cast_zero, zero_mul] at hadd
  rw [integral_log_two_sin] at hadd
  -- per-cell: ∫ (c_j − f) = (π/N)·c_j − ∫ f
  have hcell : ∀ j : ℕ, 1 ≤ j →
      (∫ u in (((j : ℝ) - 1) * (π / N))..((j : ℝ) * (π / N)),
        (Real.log (2 * Real.sin ((j : ℝ) * (π / N)))
          - Real.log (2 * Real.sin u)))
      = (π / N) * Real.log (2 * Real.sin ((j : ℝ) * (π / N)))
        - ∫ u in (((j : ℝ) - 1) * (π / N))..((j : ℝ) * (π / N)),
            Real.log (2 * Real.sin u) := by
    intro j _
    rw [intervalIntegral.integral_sub intervalIntegrable_const
      (intervalIntegrable_log_two_sin _ _)]
    rw [intervalIntegral.integral_const, smul_eq_mul]
    ring_nf
  -- reindex the goal's Icc 1 n sums to range n (j = k+1)
  have hIcc : ∀ g : ℕ → ℝ,
      (∑ j ∈ Finset.Icc 1 n, g j) = ∑ k ∈ Finset.range n, g (1 + k) := by
    intro g
    rw [← Nat.Ico_succ_right, Finset.sum_Ico_eq_sum_range]
    simp
  rw [hIcc, hIcc, Finset.mul_sum]
  -- rewrite each summand with the cell identity, then telescope with hadd
  have hstep : ∀ k ∈ Finset.range n,
      (∫ u in (((1 + k : ℕ) : ℝ) - 1) * (π / N)..(((1 + k : ℕ) : ℝ))
            * (π / N),
          (Real.log (2 * Real.sin (((1 + k : ℕ) : ℝ) * (π / N)))
            - Real.log (2 * Real.sin u)))
      = (π / N) * Real.log (2 * Real.sin (((1 + k : ℕ) : ℝ) * (π / N)))
        - ∫ u in ((k : ℝ) * (π / N))..(((1 + k : ℕ) : ℝ) * (π / N)),
            Real.log (2 * Real.sin u) := by
    intro k _
    have h := hcell (1 + k) (by omega)
    have hlow : (((1 + k : ℕ) : ℝ) - 1) * (π / N) = (k : ℝ) * (π / N) := by
      push_cast
      ring
    rw [hlow] at h
    rw [hlow]
    exact h
  rw [Finset.sum_congr rfl hstep, Finset.sum_sub_distrib]
  -- the second sum telescopes to the primitive via hadd
  have hsum2 : (∑ k ∈ Finset.range n,
      ∫ u in ((k : ℝ) * (π / N))..(((1 + k : ℕ) : ℝ) * (π / N)),
        Real.log (2 * Real.sin u))
      = -clausen (2 * ((n : ℝ) * (π / N))) / 2 := by
    have hcongr : ∀ k ∈ Finset.range n,
        (∫ u in ((k : ℝ) * (π / N))..(((1 + k : ℕ) : ℝ) * (π / N)),
          Real.log (2 * Real.sin u))
        = ∫ u in ((k : ℝ) * (π / N))..(((k + 1 : ℕ) : ℝ) * (π / N)),
            Real.log (2 * Real.sin u) := by
      intro k _
      have : ((1 + k : ℕ) : ℝ) = ((k + 1 : ℕ) : ℝ) := by push_cast; ring
      rw [this]
    rw [Finset.sum_congr rfl hcongr, hadd]
  rw [hsum2]

end QOU.Knot.FigureEightVolume
