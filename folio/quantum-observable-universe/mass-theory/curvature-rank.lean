import Mathlib.Order.Basic
import Mathlib.Tactic

/-!
# Curvature-rank `r(T_w)`

For an element `T_w` of the Hecke algebra, the **curvature-rank**
`r(T_w)` is the smallest `r` with the `r`-fold iterated Hecke
curvature `F^r(T_w)` landing in `J^r \ J^{r+1}` of the
Gröbner–Shirshov confinement filtration `J^•`. Equivalently it is
the minimal number of Hecke / Yang–Baxter reductions needed to bring
`T_w` to normal form.

We model the filtration by a `gbValuation : A → ℕ∞`-style grade and
define the curvature-rank as that grade of the iterated-curvature
image. This sibling axiomatises the rank as the least index at which
the filtered piece is non-trivial.

-- Ref: [leitner2026] def:curvature-rank
-- Ref: [bokutchen2014] Bokut, Chen, "Gröbner–Shirshov bases and their calculation," Bull. Math. Sci. 4 (2014)
-/

namespace QOU.WedderburnMass

variable {A : Type*}

/-- The **curvature-rank** of `x`, given a GB-filtration grade
`grade : A → ℕ` on the iterated-curvature images: it is the least
`r` such that `gradeOfIter x r = r`, i.e. the iterated curvature
`F^r x` first occupies filtration step `r`. We package the
"first non-trivial step" content as the least element of the set of
witnessing indices. -/
noncomputable def curvatureRank
    (gradeOfIter : A → ℕ → ℕ) (x : A) : ℕ :=
  sInf { r : ℕ | gradeOfIter x r = r }

/-- If `r₀` witnesses the curvature-rank condition, the curvature-rank
is `≤ r₀` (the infimum is bounded by any witness). -/
theorem curvatureRank_le
    (gradeOfIter : A → ℕ → ℕ) (x : A) {r₀ : ℕ}
    (h : gradeOfIter x r₀ = r₀) :
    curvatureRank gradeOfIter x ≤ r₀ :=
  Nat.sInf_le h

end QOU.WedderburnMass
