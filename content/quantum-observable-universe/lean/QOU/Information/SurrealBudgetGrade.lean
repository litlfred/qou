import QOU.Information.PhysicalIntractability

/-!
# QOU.Information.SurrealBudgetGrade — the ω-grade cost/budget squeeze

The surreal / Hardy-field **ω-grading** is a rigorous *ordered* home for the
P-vs-NP cost/budget comparison: a growth function's ω-grade orders it against
the polynomials. In these terms `SuperPolynomial` (from
`PhysicalIntractability`) is exactly

    ord_ω(cost) > ord_ω(every polynomial budget),

and a *polynomial budget* is a function whose ω-grade is `≤` that of some
`c·n^k`. This file formalizes the **grade algebra** — the content of "surreal
grading is bound *management*, not bookkeeping": the poly-budget grade is
closed under the operations one performs while bounding (monotone domination),
the super-poly grade is *stable* under adding or multiplying sub-dominant
terms, and the super-poly grade **strictly dominates** the poly-budget grade
(`not_polyBounded_of_superPoly`, the squeeze). Applied to the derived physical
cost this gives, sorry-free, `¬ PolyBounded steps` — the surreal squeeze
`ord_ω(steps) > ord_ω(budget)` underlying the `P ⊊ (bandwidth-limited)`
separation.

All sorry-free; the nontrivial facts route through `SuperPolynomial.of_le`
(the grade is monotone), so there are no `n = 0` boundary artifacts.
-/

namespace QOU.Information

/-- **Polynomially bounded** — the *budget grade*: `f` is dominated by some
    polynomial `c·nᵏ`. In ω-grade terms `ord_ω(f) ≤ ord_ω(nᵏ)`. This is the
    exact De Morgan dual of `SuperPolynomial`. -/
def PolyBounded (f : ℕ → ℕ) : Prop := ∃ c k, ∀ n, f n ≤ c * n ^ k

/-- **The surreal squeeze (sorry-free).**  A super-polynomial cost is not
    polynomially budgeted: `ord_ω(cost) > ord_ω(budget)`. Immediate from the
    De Morgan duality of the two grades. -/
theorem not_polyBounded_of_superPoly {f : ℕ → ℕ} (h : SuperPolynomial f) :
    ¬ PolyBounded f := by
  rintro ⟨c, k, hb⟩
  obtain ⟨n, _, hn⟩ := h c k
  exact absurd (hb n) (not_le.mpr hn)

/-- **Dually (sorry-free): a polynomial budget is never super-polynomial.** -/
theorem not_superPoly_of_polyBounded {f : ℕ → ℕ} (h : PolyBounded f) :
    ¬ SuperPolynomial f := fun hs => not_polyBounded_of_superPoly hs h

/-- **Budget grade is monotone / downward-closed (sorry-free).**  Anything
    dominated by a poly-budgeted function is poly-budgeted — bounding a
    smaller quantity by the same budget. -/
theorem mono {f g : ℕ → ℕ} (hf : PolyBounded f)
    (hle : ∀ n, g n ≤ f n) : PolyBounded g := by
  obtain ⟨c, k, hb⟩ := hf
  exact ⟨c, k, fun n => le_trans (hle n) (hb n)⟩

/-- **Super-poly grade is stable under adding a sub-dominant term
    (sorry-free).**  Adding *any* overhead `g` to a super-polynomial cost `f`
    keeps it super-polynomial — the higher ω-grade absorbs the lower.  This is
    the bound-management fact: overheads never lower the grade. -/
theorem superPoly_add_left {f g : ℕ → ℕ} (hf : SuperPolynomial f) :
    SuperPolynomial (fun n => f n + g n) :=
  hf.of_le (fun n => Nat.le_add_right (f n) (g n))

/-- **Super-poly grade is stable under multiplying by a `≥ 1` factor
    (sorry-free).**  Multiplying a super-polynomial cost by any factor that is
    at least `1` keeps it super-polynomial — polynomial (or larger) dressing
    factors never lower the ω-grade. -/
theorem superPoly_mul_of_one_le {f g : ℕ → ℕ} (hf : SuperPolynomial f)
    (hg : ∀ n, 1 ≤ g n) : SuperPolynomial (fun n => f n * g n) :=
  hf.of_le (fun n => Nat.le_mul_of_pos_right (f n) (Nat.lt_of_lt_of_le Nat.zero_lt_one (hg n)))

/-! ## The physical cost sits at a strictly higher grade than any budget -/

/-- **The derived physical cost is not polynomially budgeted (sorry-free).**
    Applying the squeeze to the derived boundary cost: a bandwidth-`B` device
    that must read the full `3^{3n}` surviving resolution tree has a step count
    of strictly greater ω-grade than every polynomial budget.  This is the
    surreal `ord_ω(steps) > ord_ω(budget)` statement of
    `qou_physical_intractability_unconditional`. -/
theorem physical_cost_not_polyBounded (B : ℕ) (hB : 0 < B) (steps : ℕ → ℕ)
    (correct : ∀ n, resolutionTreeSize (3 * n) ≤ steps n * B) :
    ¬ PolyBounded steps :=
  not_polyBounded_of_superPoly
    (qou_physical_intractability_unconditional B hB steps correct)

end QOU.Information
