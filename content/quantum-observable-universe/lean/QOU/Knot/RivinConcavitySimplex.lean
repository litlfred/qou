import QOU.Knot.RivinConcavity
import QOU.MathlibExt.StrictConcaveOnSegments
import QOU.MathlibExt.ConcaveOnSum

/-!
# QOU.Knot.RivinConcavitySimplex — Rivin concavity on the angle simplex, not just on a line

Bean `qou-mlgp` **Gap 3**, completed.

`QOU.Knot.RivinConcavity.strictConcaveOn_tetVolLine` proves that
`Λ(α) + Λ(β) + Λ(γ)` is strictly concave **along a line** in the angle simplex, and its
docstring then says

> Since strict concavity on a convex set is exactly strict concavity along every
> segment, this is Rivin's theorem for a single tetrahedron.

That sentence is true and was **not proved**. It is the difference between a
one-variable statement and Rivin's theorem, and the corpus had no way to cross it:
Mathlib's concavity-from-second-derivative results are all one-dimensional
(see `QOU.MathlibExt.StrictConcaveOnSegments` for the measured gap).

With `strictConcaveOn_of_segments` in hand the crossing is direct, and this file makes
it. `strictConcaveOn_tetVol` below is Rivin's theorem for one ideal tetrahedron, as a
statement about a set in `ℝ³` rather than about a parametrised line.

## What makes the promotion work

The tangency condition is free. `RivinConcavity` needs `u + v + w = 0` — otherwise
`cot_quadratic_pos` does not apply and the angles do not stay summing to `π` along the
line. Here `(u, v, w)` is not chosen: it is `y − x` for two points of the simplex, and
both sum to `π`, so it sums to `0` automatically.

The non-degeneracy is nearly free too: `¬(u = 0 ∧ v = 0)` would fail only if the first
two coordinates agreed, and then `w = −u − v = 0` forces `y = x`, which the strict
hypothesis already excludes.

So the geometry that the line version had to be *given* is exactly what "two distinct
points of the simplex" already supplies.

Archimedean (ℝ).

-- Ref: [rivin1994] Euclidean structures on simplicial surfaces and hyperbolic volume
-/

namespace QOU.Knot.Rivin

open Real Set QOU.MathlibExt

/-- The angle simplex of one ideal tetrahedron: three positive dihedral angles
summing to `π`. Points are `(α, β, γ)`. -/
def tetAngleSimplex : Set (ℝ × ℝ × ℝ) :=
  {p | 0 < p.1 ∧ 0 < p.2.1 ∧ 0 < p.2.2 ∧ p.1 + p.2.1 + p.2.2 = π}

/-- The volume functional on the angle simplex, `Λ(α) + Λ(β) + Λ(γ)`. This is the
`tetVolLine` of `RivinConcavity` with the line parametrisation stripped off. -/
noncomputable def tetVol (p : ℝ × ℝ × ℝ) : ℝ :=
  QOU.Archimedean.Lob p.1 + QOU.Archimedean.Lob p.2.1 + QOU.Archimedean.Lob p.2.2

theorem convex_tetAngleSimplex : Convex ℝ tetAngleSimplex := by
  rintro x ⟨hx1, hx2, hx3, hxs⟩ y ⟨hy1, hy2, hy3, hys⟩ a b ha hb hab
  -- A convex combination of two positives is positive: `a + b = 1` stops both
  -- weights vanishing at once.
  have key : ∀ p q : ℝ, 0 < p → 0 < q → 0 < a * p + b * q := by
    intro p q hp hq
    rcases ha.lt_or_eq with h | h
    · exact add_pos_of_pos_of_nonneg (mul_pos h hp) (mul_nonneg hb hq.le)
    · have hb1 : b = 1 := by linarith
      rw [← h, hb1, zero_mul, one_mul, zero_add]; exact hq
  refine ⟨key _ _ hx1 hy1, key _ _ hx2 hy2, key _ _ hx3 hy3, ?_⟩
  show a * x.1 + b * y.1 + (a * x.2.1 + b * y.2.1) + (a * x.2.2 + b * y.2.2) = π
  -- `a·(Σx) + b·(Σy) = a·π + b·π = π`.
  linear_combination a * hxs + b * hys + π * hab

/-- **RIVIN CONCAVITY FOR ONE IDEAL TETRAHEDRON, on the simplex.**

`Λ(α) + Λ(β) + Λ(γ)` is strictly concave on `{α, β, γ > 0, α + β + γ = π}`.

This is the statement `strictConcaveOn_tetVolLine`'s docstring claims to be equivalent
to; here it is derived from it, by `strictConcaveOn_of_segments`. -/
theorem strictConcaveOn_tetVol : StrictConcaveOn ℝ tetAngleSimplex tetVol := by
  refine strictConcaveOn_of_segments convex_tetAngleSimplex ?_
  rintro x ⟨hx1, hx2, hx3, hxs⟩ y ⟨hy1, hy2, hy3, hys⟩ hxy
  set u := y.1 - x.1 with hu
  set v := y.2.1 - x.2.1 with hv
  set w := y.2.2 - x.2.2 with hw
  -- The direction is tangent to the constraint for free: both endpoints sum to `π`.
  have htan : u + v + w = 0 := by rw [hu, hv, hw]; linarith
  -- Non-degeneracy: `u = v = 0` forces `w = 0` by `htan`, hence `y = x`.
  have hne : ¬(u = 0 ∧ v = 0) := by
    rintro ⟨hu0, hv0⟩
    have hw0 : w = 0 := by linarith
    refine hxy (Prod.ext ?_ (Prod.ext ?_ ?_)) <;> simp only [hu, hv, hw] at hu0 hv0 hw0 <;>
      linarith
  -- The restriction to the segment IS `tetVolLine`.
  have hfun : (fun t : ℝ => tetVol (x + t • (y - x)))
      = tetVolLine x.1 x.2.1 x.2.2 u v w := by
    funext t
    simp only [tetVol, tetVolLine, Prod.fst_add, Prod.snd_add, Prod.smul_fst, Prod.smul_snd,
      Prod.fst_sub, Prod.snd_sub, smul_eq_mul, hu, hv, hw]
  rw [hfun]
  -- `[0,1]` sits inside the line's admissible domain: each angle stays a convex
  -- combination of two positive angles.
  refine (strictConcaveOn_tetVolLine hxs htan hne).subset ?_ (convex_Icc 0 1)
  rintro t ⟨ht0, ht1⟩
  have pos : ∀ p q : ℝ, 0 < p → 0 < q → 0 < p + t * (q - p) := by
    intro p q hp hq
    have : p + t * (q - p) = (1 - t) * p + t * q := by ring
    rw [this]
    rcases eq_or_lt_of_le ht1 with h | h
    · rw [h]; simpa using hq
    · exact add_pos_of_pos_of_nonneg (mul_pos (by linarith) hp) (mul_nonneg ht0 hq.le)
  exact ⟨pos _ _ hx1 hy1, pos _ _ hx2 hy2, pos _ _ hx3 hy3⟩

/-! ## From one tetrahedron to a triangulation -/

/-- The total volume of an ideal triangulation with `n` tetrahedra, as a function of the
tuple of angle triples. -/
noncomputable def totalVol {n : ℕ} (θ : Fin n → ℝ × ℝ × ℝ) : ℝ :=
  ∑ i, tetVol (θ i)

/-- **RIVIN CONCAVITY FOR AN IDEAL TRIANGULATION.**

The total volume is strictly concave on **any** convex set of angle assignments whose
points are tetrahedron-wise admissible.

The gluing equations never appear. That is the point: they are linear, so whatever
polytope they cut out is convex, and `P` may be taken to be it. Concavity does not care
*which* convex set — only that it is one, and that each of its points gives every
tetrahedron a genuine angle triple. So this covers Rivin's angle-structure polytope, any
face of it, and any further linear restriction, without proving anything about the
gluing equations themselves.

**Where strictness comes from.** Each summand `tetVol ∘ (eval i)` is constant in every
*other* tetrahedron's angles, so as a function on `P` it is concave and not strictly so.
But two distinct angle assignments must differ at some tetrahedron `j`, and there the
summand is strictly concave by `strictConcaveOn_tetVol`. `StrictConcaveOn.sum_of_mem` is
shaped for exactly this: one strict summand carries the sum.

This is the variational statement the hyperbolic structure is characterised by — the
complete structure is the unique critical point — and hence what the volume-conjecture
work rests on downstream. -/
theorem strictConcaveOn_totalVol {n : ℕ} {P : Set (Fin n → ℝ × ℝ × ℝ)}
    (hP : Convex ℝ P) (hsub : ∀ θ ∈ P, ∀ i, θ i ∈ tetAngleSimplex) :
    StrictConcaveOn ℝ P totalVol := by
  classical
  refine strictConcaveOn_of_segments hP fun x hx y hy hxy => ?_
  -- Two distinct assignments differ at some tetrahedron.
  obtain ⟨j, hj⟩ : ∃ j, x j ≠ y j := by
    by_contra hcon
    push_neg at hcon
    exact hxy (funext hcon)
  -- The restriction to the segment is the sum of the per-tetrahedron restrictions.
  have hfun : (fun t : ℝ => totalVol (x + t • (y - x)))
      = fun t : ℝ => ∑ i, tetVol (x i + t • (y i - x i)) := by
    funext t
    simp only [totalVol, Pi.add_apply, Pi.smul_apply, Pi.sub_apply]
  rw [hfun]
  -- Every summand is concave: constant where the tetrahedron does not move, strictly
  -- concave where it does.
  have hcon : ∀ i : Fin n, i ≠ j →
      ConcaveOn ℝ (Icc (0 : ℝ) 1) (fun t : ℝ => tetVol (x i + t • (y i - x i))) := by
    intro i _
    by_cases h : x i = y i
    · have hconst : (fun t : ℝ => tetVol (x i + t • (y i - x i)))
          = fun _ : ℝ => tetVol (x i) := by
        funext t; rw [← h]; simp
      rw [hconst]
      exact concaveOn_const _ (convex_Icc 0 1)
    · exact (StrictConcaveOn.restrict_segment strictConcaveOn_tetVol
        (hsub x hx i) (hsub y hy i) h).concaveOn
  -- and the `j`-th is strictly concave.
  exact StrictConcaveOn.sum_of_mem (Finset.mem_univ j) (convex_Icc 0 1)
    (StrictConcaveOn.restrict_segment strictConcaveOn_tetVol (hsub x hx j) (hsub y hy j) hj)
    (fun i _ hij => hcon i hij)

end QOU.Knot.Rivin
