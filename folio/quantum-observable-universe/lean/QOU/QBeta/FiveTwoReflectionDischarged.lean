/-
# The 5₂ reflection reduction with `Li := cLiTwoExt` — `hrefl` discharged

`QOU.QBeta.FiveTwo.sum_reflection_of_branch` takes the reflection identity
`Li z + Li (1 − z) = π²/6 − log z · log(1 − z)` as a hypothesis for **every**
`z : ℂ`. That global form cannot be supplied for the genuine dilogarithm: the
principal-branch identity holds only off both real cuts, i.e. on
`QOU.Archimedean.reflDomain = ℂ ∖ ((−∞,0] ∪ [1,∞))`
(`QOU.Archimedean.cLiTwoExt_reflection`). The reduction itself only ever uses
the identity **at the three roots**, so this file

1. restates the reduction with the reflection hypothesis required only at the
   `yⱼ` (`sum_reflection_of_branch_at`, proof identical in shape to the
   original);
2. instantiates it at `Li := cLiTwoExt` for any roots lying in `reflDomain`
   (`sum_reflection_cLiTwoExt`), so the hypothesis becomes a domain condition;
3. checks that domain condition for the 5₂ saddle roots `(a, ā, t)` of
   `X³ − 2X² + 3X − 1` (`SaddleRoots.mem_reflDomain_*`), and supplies the branch
   data `ε = (+1, −1, 0)` from `SaddleRoots.branch_upper/lower/real`;
4. states the resulting unconditional identity for the actual roots
   (`fiveTwo_sum_reflection`).

Nothing is assumed: no `sorry`, no axiom, no hypothesis left on `Li`.

-- Ref: [leitner2026] beans qou-ph1k, qou-gkco, qou-0yqu
-/
import QOU.Archimedean.ComplexDilogReflectionExt
import QOU.QBeta.FiveTwoComplexPentagon

namespace QOU.QBeta.FiveTwo

open Complex QOU.MathlibExt QOU.Archimedean

/-- **The reflection reduction, with the reflection identity needed only at the
roots.** Same conclusion as `sum_reflection_of_branch`, weaker hypothesis. -/
theorem sum_reflection_of_branch_at
    (Li : ℂ → ℂ) (y ε : Fin 3 → ℂ)
    (hrefl : ∀ j, Li (y j) + Li (1 - y j)
      = (Real.pi : ℂ) ^ 2 / 6 - Complex.log (y j) * Complex.log (1 - y j))
    (hbranch : ∀ j, 2 * Complex.log (y j) - 3 * Complex.log (1 - y j)
      = 2 * (Real.pi : ℂ) * I * ε j) :
    (∑ j, Li (y j)) + (∑ j, Li (1 - y j))
      = (Real.pi : ℂ) ^ 2 / 2 - (2 / 3) * ∑ j, Complex.log (y j) ^ 2
        + (2 * (Real.pi : ℂ) * I / 3) * ∑ j, ε j * Complex.log (y j) := by
  have per : ∀ j, Li (y j) + Li (1 - y j)
      = (Real.pi : ℂ) ^ 2 / 6 - (2 / 3) * Complex.log (y j) ^ 2
        + (2 * (Real.pi : ℂ) * I / 3) * (ε j * Complex.log (y j)) := by
    intro j
    have hk : Complex.log (1 - y j)
        = (2 * Complex.log (y j) - 2 * (Real.pi : ℂ) * I * ε j) / 3 := by
      linear_combination (-1 / 3 : ℂ) * hbranch j
    rw [hrefl j, hk]; ring
  simp only [Fin.sum_univ_three]
  linear_combination per 0 + per 1 + per 2

/-- The original (global-hypothesis) reduction is a special case of the local one. -/
theorem sum_reflection_of_branch_eq_at
    (Li : ℂ → ℂ) (y ε : Fin 3 → ℂ)
    (hrefl : ∀ z : ℂ, Li z + Li (1 - z)
      = (Real.pi : ℂ) ^ 2 / 6 - Complex.log z * Complex.log (1 - z))
    (hbranch : ∀ j, 2 * Complex.log (y j) - 3 * Complex.log (1 - y j)
      = 2 * (Real.pi : ℂ) * I * ε j) :
    (∑ j, Li (y j)) + (∑ j, Li (1 - y j))
      = (Real.pi : ℂ) ^ 2 / 2 - (2 / 3) * ∑ j, Complex.log (y j) ^ 2
        + (2 * (Real.pi : ℂ) * I / 3) * ∑ j, ε j * Complex.log (y j) :=
  sum_reflection_of_branch_at Li y ε (fun j => hrefl (y j)) hbranch

/-- **The reduction at `Li := cLiTwoExt`, `hrefl` discharged.** The reflection
hypothesis is replaced by the domain condition `yⱼ ∈ reflDomain`, which
`cLiTwoExt_reflection` turns into the identity. -/
theorem sum_reflection_cLiTwoExt (y ε : Fin 3 → ℂ)
    (hy : ∀ j, y j ∈ reflDomain)
    (hbranch : ∀ j, 2 * Complex.log (y j) - 3 * Complex.log (1 - y j)
      = 2 * (Real.pi : ℂ) * I * ε j) :
    (∑ j, cLiTwoExt (y j)) + (∑ j, cLiTwoExt (1 - y j))
      = (Real.pi : ℂ) ^ 2 / 2 - (2 / 3) * ∑ j, Complex.log (y j) ^ 2
        + (2 * (Real.pi : ℂ) * I / 3) * ∑ j, ε j * Complex.log (y j) :=
  sum_reflection_of_branch_at cLiTwoExt y ε (fun j => cLiTwoExt_reflection (hy j)) hbranch

end QOU.QBeta.FiveTwo

/-! ### The 5₂ saddle roots lie in `reflDomain` -/

namespace QOU.QBeta.FiveTwoComplexPentagon

open Complex QOU.MathlibExt QOU.Archimedean QOU.QBeta.FiveTwo

namespace SaddleRoots

variable (S : SaddleRoots)

/-- The upper root `a` (`Im a > 0`) is off both real cuts. -/
theorem mem_reflDomain_a : S.a ∈ reflDomain := Or.inl (ne_of_gt S.him)

/-- The lower root `ā` (`Im ā < 0`) is off both real cuts. -/
theorem mem_reflDomain_conj_a : (starRingEnd ℂ) S.a ∈ reflDomain :=
  Or.inl (by simpa using ne_of_gt S.him)

/-- The real root `t ∈ (0,1)` is off both real cuts. -/
theorem mem_reflDomain_t : ((S.t : ℝ) : ℂ) ∈ reflDomain :=
  Or.inr ⟨by simpa using S.ht0, by simpa using S.ht1⟩

/-- The three roots as a vector `(y₁, y₂, y₃) = (a, ā, t)`. -/
noncomputable def roots : Fin 3 → ℂ := ![S.a, (starRingEnd ℂ) S.a, (S.t : ℂ)]

/-- The branch integers `ε = (+1, −1, 0)`, proved in `FiveTwoComplexPentagon`. -/
def eps : Fin 3 → ℂ := ![1, -1, 0]

theorem roots_mem_reflDomain : ∀ j, S.roots j ∈ reflDomain := by
  intro j
  fin_cases j
  · exact S.mem_reflDomain_a
  · exact S.mem_reflDomain_conj_a
  · exact S.mem_reflDomain_t

theorem roots_branch : ∀ j, 2 * Complex.log (S.roots j) - 3 * Complex.log (1 - S.roots j)
    = 2 * (Real.pi : ℂ) * I * eps j := by
  intro j
  fin_cases j
  · simp only [roots, eps]
    simp only [Fin.zero_eta, Matrix.cons_val_zero]
    linear_combination S.branch_upper
  · simp only [roots, eps]
    simp only [Fin.mk_one, Matrix.cons_val_one, Matrix.cons_val_zero]
    linear_combination S.branch_lower
  · simp only [roots, eps]
    simp only [Fin.reduceFinMk, Matrix.cons_val]
    linear_combination S.branch_real

/-- **The reflection reduction at the 5₂ saddle roots, unconditional.**

    Σⱼ Li₂(yⱼ) + Σⱼ Li₂(1−yⱼ)
      = π²/2 − (2/3)·Σⱼ log²yⱼ + (2πi/3)·(log a − log ā)

with `Li₂ = cLiTwoExt`, `(y₁,y₂,y₃) = (a, ā, t)`. Both former hypotheses of
`sum_reflection_of_branch` are now theorems: the reflection identity at each
root (`cLiTwoExt_reflection` + `roots_mem_reflDomain`) and the branch data
(`roots_branch`). -/
theorem sum_reflection :
    (cLiTwoExt S.a + cLiTwoExt ((starRingEnd ℂ) S.a) + cLiTwoExt (S.t : ℂ))
      + (cLiTwoExt (1 - S.a) + cLiTwoExt (1 - (starRingEnd ℂ) S.a)
          + cLiTwoExt (1 - (S.t : ℂ)))
      = (Real.pi : ℂ) ^ 2 / 2
        - (2 / 3) * (Complex.log S.a ^ 2 + Complex.log ((starRingEnd ℂ) S.a) ^ 2
            + Complex.log (S.t : ℂ) ^ 2)
        + (2 * (Real.pi : ℂ) * I / 3)
            * (Complex.log S.a - Complex.log ((starRingEnd ℂ) S.a)) := by
  have h := sum_reflection_cLiTwoExt S.roots eps S.roots_mem_reflDomain S.roots_branch
  simp only [Fin.sum_univ_three, roots, eps, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons] at h
  linear_combination h

end SaddleRoots

/-- **For the actual roots of `X³ − 2X² + 3X − 1`.** `SaddleRoots` is inhabited by
the real root from the intermediate value theorem and its conjugate pair, so the
reduction is a statement about the cubic itself. -/
theorem fiveTwo_sum_reflection :
    ∃ (t : ℝ) (a : ℂ), 0 < t ∧ t < 1 ∧ 0 < a.im
      ∧ (t : ℂ) ^ 3 - 2 * (t : ℂ) ^ 2 + 3 * (t : ℂ) - 1 = 0
      ∧ a ^ 3 - 2 * a ^ 2 + 3 * a - 1 = 0
      ∧ ((starRingEnd ℂ) a) ^ 3 - 2 * ((starRingEnd ℂ) a) ^ 2
          + 3 * ((starRingEnd ℂ) a) - 1 = 0
      ∧ (cLiTwoExt a + cLiTwoExt ((starRingEnd ℂ) a) + cLiTwoExt (t : ℂ))
        + (cLiTwoExt (1 - a) + cLiTwoExt (1 - (starRingEnd ℂ) a)
            + cLiTwoExt (1 - (t : ℂ)))
        = (Real.pi : ℂ) ^ 2 / 2
          - (2 / 3) * (Complex.log a ^ 2 + Complex.log ((starRingEnd ℂ) a) ^ 2
              + Complex.log (t : ℂ) ^ 2)
          + (2 * (Real.pi : ℂ) * I / 3)
              * (Complex.log a - Complex.log ((starRingEnd ℂ) a)) := by
  obtain ⟨t, h0, h1, hc⟩ := SaddleRoots.exists_real_root
  set S := SaddleRoots.ofRealRoot h0 h1 hc with hS
  have hst : S.t = t := rfl
  refine ⟨t, S.a, h0, h1, S.him, ?_, S.cubic_a, S.cubic_conj_a, ?_⟩
  · exact S.cubic_t
  · have h := S.sum_reflection
    rw [hst] at h
    exact h

end QOU.QBeta.FiveTwoComplexPentagon
