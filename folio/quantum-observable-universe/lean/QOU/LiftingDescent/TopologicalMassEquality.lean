import Mathlib.Analysis.Convex.StrictConvexSpace
import Mathlib.Analysis.InnerProductSpace.Convex
import Mathlib.Analysis.InnerProductSpace.Basic

/-!
# QOU.Torsion.TopologicalMassEquality — when the topological mass decomposition is an equality

Content block `conj:topological-mass` asserts

  `‖t‖ = ‖d‖ + Σ_{i ∈ s} ‖τ_i‖`,   where `t = d + Σ_{i ∈ s} τ_i`

(`t` the trace value of the cycle, `d` its descended part, `τ_i` the transient
part localised at the `i`-th blow-up centre). The split `t = d + Σ τ_i` and the
inequality `‖t‖ ≤ ‖d‖ + Σ ‖τ_i‖` are proved
(`prop:topological-mass-upper-bound`, `QOU.Torsion.mass_upper_bound_localised`).
So the conjecture is exactly the statement that the triangle inequality is an
equality for this particular family.

This file proves, sorry-free, what that equality is equivalent to.

* `norm_sum_eq_sum_norm_iff` — in a strictly convex real normed space,
  `‖Σ_{i ∈ s} f i‖ = Σ_{i ∈ s} ‖f i‖` holds **iff** every two summands lie on a
  common ray (`SameRay ℝ (f i) (f j)` for all `i, j ∈ s`).
* `mass_decomposition_eq_iff` — the conjecture's equality, for one cycle, holds
  **iff** the descended part is on a common ray with every transient part, and
  the transient parts are pairwise on a common ray.
* `mass_decomposition_eq_of_nonneg` / `mass_decomposition_lt_of_anti_aligned` —
  the real-valued case: equality when all pieces are `≥ 0`, and **strict
  inequality** as soon as one piece is `> 0` and another `< 0`.
* `transient_norm_equality_mult_iff` — the multiplicative-integral form used by
  `lem:topological-mass-transient-localisation`: for values in
  `Multiplicative ℝ`, `‖∏ div i‖ = Σ ‖div i‖` iff the logarithms
  `toAdd (div i)` share a sign.

## What this does and does not settle

It settles nothing about the sign or phase of the corpus's actual pieces. It
reduces the conjecture to a single, checkable condition (a common ray), and it
proves that condition is also necessary.

The condition is *not* a consequence of the idempotent splitting. Nor does
orthogonality supply it, in either of two readings:

* Orthogonality of the **algebra pieces** (`τ̂(α) ⟂ α − τ̂(α)` for the Killing or
  Frobenius form) is a statement about elements of the endomorphism algebra.
  The conjecture is about the **scalar trace values** of those pieces, and
  orthogonality of two elements constrains nothing about whether their traces
  share a phase.
* Read instead as a statement about the norms of the pieces themselves, it
  points the wrong way: `norm_add_lt_of_inner_eq_zero` proves that two non-zero
  orthogonal vectors in a real inner product space satisfy the triangle
  inequality **strictly**. Orthogonality gives additivity of squared norms,
  never of norms, except when one piece vanishes.

**Base ring (§7c).** The ray characterisation is stated over an arbitrary real
normed space `E` (strictly convex for the converse direction). `ℝ` appears only
as the scalar field of `SameRay`, which is what the norm's homogeneity needs,
and as the value space in the explicitly real corollaries.

-- Ref: [leitner2026] §3 Lifting and Descent, topological decomposition of mass
-/

open Finset

namespace QOU.Torsion

section Seminormed

variable {E : Type*} [SeminormedAddCommGroup E] [NormedSpace ℝ E]

/-- If `x` is on a common ray with each `f i`, it is on a common ray with their
sum. -/
theorem sameRay_sum_right {ι : Type*} (s : Finset ι) (x : E) (f : ι → E)
    (h : ∀ i ∈ s, SameRay ℝ x (f i)) : SameRay ℝ x (∑ i ∈ s, f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih =>
    rw [sum_insert ha]
    exact (h a (mem_insert_self a s)).add_right
      (ih fun i hi => h i (mem_insert_of_mem hi))

/-- **Sufficiency (any real normed space).** If the summands are pairwise on a
common ray, the norm of the sum is the sum of the norms. -/
theorem norm_sum_eq_sum_norm_of_pairwise_sameRay {ι : Type*} (s : Finset ι)
    (f : ι → E) (h : ∀ i ∈ s, ∀ j ∈ s, SameRay ℝ (f i) (f j)) :
    ‖∑ i ∈ s, f i‖ = ∑ i ∈ s, ‖f i‖ := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih =>
    rw [sum_insert ha, sum_insert ha]
    have hray : SameRay ℝ (f a) (∑ i ∈ s, f i) :=
      sameRay_sum_right s (f a) f fun i hi =>
        h a (mem_insert_self a s) i (mem_insert_of_mem hi)
    rw [hray.norm_add,
      ih fun i hi j hj => h i (mem_insert_of_mem hi) j (mem_insert_of_mem hj)]

end Seminormed

section StrictlyConvex

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [StrictConvexSpace ℝ E]

/-- **Necessity (strictly convex space).** If the norm of a finite sum equals
the sum of the norms, any two distinct summands are on a common ray. -/
theorem sameRay_of_norm_sum_eq_sum_norm {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (f : ι → E) (heq : ‖∑ k ∈ s, f k‖ = ∑ k ∈ s, ‖f k‖)
    {i j : ι} (hi : i ∈ s) (hj : j ∈ s) (hij : i ≠ j) :
    SameRay ℝ (f i) (f j) := by
  have hj' : j ∈ s.erase i := mem_erase.2 ⟨hij.symm, hj⟩
  have hsum : ∑ k ∈ s, f k = (f i + f j) + ∑ k ∈ (s.erase i).erase j, f k := by
    rw [add_assoc, add_sum_erase _ _ hj', add_sum_erase _ _ hi]
  have hnorm : ∑ k ∈ s, ‖f k‖ =
      (‖f i‖ + ‖f j‖) + ∑ k ∈ (s.erase i).erase j, ‖f k‖ := by
    rw [add_assoc, add_sum_erase _ (fun k => ‖f k‖) hj',
      add_sum_erase _ (fun k => ‖f k‖) hi]
  have hle : ‖∑ k ∈ s, f k‖ ≤
      ‖f i + f j‖ + ∑ k ∈ (s.erase i).erase j, ‖f k‖ := by
    rw [hsum]
    exact (norm_add_le _ _).trans (by gcongr; exact norm_sum_le _ _)
  rw [sameRay_iff_norm_add]
  have := norm_add_le (f i) (f j)
  linarith

/-- **Equality in the finite triangle inequality.** In a strictly convex real
normed space, `‖Σ f‖ = Σ ‖f‖` iff all summands lie pairwise on a common ray. -/
theorem norm_sum_eq_sum_norm_iff {ι : Type*} (s : Finset ι) (f : ι → E) :
    ‖∑ i ∈ s, f i‖ = ∑ i ∈ s, ‖f i‖ ↔
      ∀ i ∈ s, ∀ j ∈ s, SameRay ℝ (f i) (f j) := by
  classical
  refine ⟨fun heq i hi j hj => ?_, norm_sum_eq_sum_norm_of_pairwise_sameRay s f⟩
  by_cases hij : i = j
  · subst hij; exact SameRay.rfl
  · exact sameRay_of_norm_sum_eq_sum_norm s f heq hi hj hij

/-- **Strict inequality off a common ray.** If two summands are not on a common
ray, the triangle inequality is strict. -/
theorem norm_sum_lt_sum_norm_of_not_sameRay {ι : Type*} (s : Finset ι) (f : ι → E)
    {i j : ι} (hi : i ∈ s) (hj : j ∈ s) (hnot : ¬ SameRay ℝ (f i) (f j)) :
    ‖∑ k ∈ s, f k‖ < ∑ k ∈ s, ‖f k‖ := by
  refine lt_of_le_of_ne (norm_sum_le _ _) fun heq => hnot ?_
  exact (norm_sum_eq_sum_norm_iff s f).1 heq i hi j hj

/-- **The topological mass equality, reduced.** Let a trace value split as a
descended part plus transient parts over a finite set of blow-up centres. Then
the conjectured equality `‖t‖ = ‖d‖ + Σ ‖τ_i‖` holds iff the descended part is
on a common ray with every transient part and the transient parts are pairwise
on a common ray. -/
theorem mass_decomposition_eq_iff {ι : Type*} (s : Finset ι)
    (total descended : E) (transient : ι → E)
    (hsplit : total = descended + ∑ i ∈ s, transient i) :
    ‖total‖ = ‖descended‖ + ∑ i ∈ s, ‖transient i‖ ↔
      (∀ i ∈ s, SameRay ℝ descended (transient i)) ∧
        ∀ i ∈ s, ∀ j ∈ s, SameRay ℝ (transient i) (transient j) := by
  let g : Option ι → E := fun o => o.elim descended transient
  have hsum : ∑ o ∈ s.insertNone, g o = descended + ∑ i ∈ s, transient i :=
    sum_insertNone g s
  have hnsum : ∑ o ∈ s.insertNone, ‖g o‖ = ‖descended‖ + ∑ i ∈ s, ‖transient i‖ :=
    sum_insertNone (fun o => ‖g o‖) s
  have hnone : (none : Option ι) ∈ s.insertNone := mem_insertNone.2 (by simp)
  have hsome : ∀ {i}, i ∈ s → (some i : Option ι) ∈ s.insertNone :=
    fun hi => mem_insertNone.2 (by simpa using hi)
  rw [hsplit, ← hsum, ← hnsum, norm_sum_eq_sum_norm_iff]
  constructor
  · intro h
    exact ⟨fun i hi => h none hnone (some i) (hsome hi),
      fun i hi j hj => h (some i) (hsome hi) (some j) (hsome hj)⟩
  · rintro ⟨hd, ht⟩ o ho o' ho'
    have mem : ∀ {o : Option ι} {i}, o ∈ s.insertNone → o = some i → i ∈ s := by
      intro o i ho e; subst e; simpa using mem_insertNone.1 ho
    rcases o with _ | i <;> rcases o' with _ | j
    · exact SameRay.rfl
    · exact hd j (mem ho' rfl)
    · exact (hd i (mem ho rfl)).symm
    · exact ht i (mem ho rfl) j (mem ho' rfl)

end StrictlyConvex

/-! ## Real-valued pieces: the sign condition -/

/-- Two non-negative reals are on a common ray. -/
theorem sameRay_of_nonneg {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) : SameRay ℝ a b := by
  rcases ha.eq_or_lt with rfl | ha'
  · exact SameRay.zero_left b
  rcases hb.eq_or_lt with rfl | hb'
  · exact SameRay.zero_right a
  exact Or.inr (Or.inr ⟨b, a, hb', ha', by simp [smul_eq_mul, mul_comm]⟩)

/-- A strictly positive and a strictly negative real are not on a common ray. -/
theorem not_sameRay_of_pos_of_neg {a b : ℝ} (ha : 0 < a) (hb : b < 0) :
    ¬ SameRay ℝ a b := by
  rintro (h | h | ⟨r₁, r₂, hr₁, hr₂, h⟩)
  · exact ha.ne' h
  · exact hb.ne h
  · simp only [smul_eq_mul] at h
    nlinarith [mul_pos hr₁ ha, mul_neg_of_pos_of_neg hr₂ hb]

/-- **Equality when all pieces are non-negative reals.** -/
theorem mass_decomposition_eq_of_nonneg {ι : Type*} (s : Finset ι)
    (total descended : ℝ) (transient : ι → ℝ)
    (hsplit : total = descended + ∑ i ∈ s, transient i)
    (hd : 0 ≤ descended) (ht : ∀ i ∈ s, 0 ≤ transient i) :
    ‖total‖ = ‖descended‖ + ∑ i ∈ s, ‖transient i‖ :=
  (mass_decomposition_eq_iff s total descended transient hsplit).2
    ⟨fun i hi => sameRay_of_nonneg hd (ht i hi),
      fun i hi j hj => sameRay_of_nonneg (ht i hi) (ht j hj)⟩

/-- **Strict inequality as soon as two transient pieces are anti-aligned.**
If one transient piece is `> 0` and another `< 0`, the conjectured equality
fails for that cycle. -/
theorem mass_decomposition_lt_of_anti_aligned {ι : Type*} (s : Finset ι)
    (total descended : ℝ) (transient : ι → ℝ)
    (hsplit : total = descended + ∑ i ∈ s, transient i)
    {i j : ι} (hi : i ∈ s) (hj : j ∈ s)
    (hpos : 0 < transient i) (hneg : transient j < 0) :
    ‖total‖ < ‖descended‖ + ∑ i ∈ s, ‖transient i‖ := by
  refine lt_of_le_of_ne ?_ fun heq => ?_
  · rw [hsplit]
    exact (norm_add_le _ _).trans (by gcongr; exact norm_sum_le _ _)
  · exact not_sameRay_of_pos_of_neg hpos hneg
      ((mass_decomposition_eq_iff s total descended transient hsplit).1 heq |>.2
        i hi j hj)

/-- **Strict inequality when the descended piece is anti-aligned with a
transient piece.** -/
theorem mass_decomposition_lt_of_desc_anti_aligned {ι : Type*} (s : Finset ι)
    (total descended : ℝ) (transient : ι → ℝ)
    (hsplit : total = descended + ∑ i ∈ s, transient i)
    {i : ι} (hi : i ∈ s) (hpos : 0 < descended) (hneg : transient i < 0) :
    ‖total‖ < ‖descended‖ + ∑ i ∈ s, ‖transient i‖ := by
  refine lt_of_le_of_ne ?_ fun heq => ?_
  · rw [hsplit]
    exact (norm_add_le _ _).trans (by gcongr; exact norm_sum_le _ _)
  · exact not_sameRay_of_pos_of_neg hpos hneg
      ((mass_decomposition_eq_iff s total descended transient hsplit).1 heq |>.1 i hi)

/-! ## The multiplicative-integral form -/

/-- **Transient localisation equality, reduced.** For values in the seminormed
group `Multiplicative ℝ` (the setting of
`QOU.LiftingDescent.TransientLocalisationNormEquality`), the norm of the ordered
product over `range N` equals the sum of the norms iff the logarithms
`toAdd (div i)` lie pairwise on a common ray, i.e. share a sign. -/
theorem transient_norm_equality_mult_iff (div : ℕ → Multiplicative ℝ) (N : ℕ) :
    ‖((List.range N).map div).prod‖ = ∑ i ∈ range N, ‖div i‖ ↔
      ∀ i ∈ range N, ∀ j ∈ range N,
        SameRay ℝ (Multiplicative.toAdd (div i)) (Multiplicative.toAdd (div j)) := by
  have hprod : ((List.range N).map div).prod = ∏ i ∈ range N, div i := rfl
  have hadd : Multiplicative.toAdd (∏ i ∈ range N, div i) =
      ∑ i ∈ range N, Multiplicative.toAdd (div i) := rfl
  rw [hprod, ← norm_toAdd, hadd]
  simp only [← norm_toAdd]
  exact norm_sum_eq_sum_norm_iff (range N) fun i => Multiplicative.toAdd (div i)

/-! ## Orthogonality forces strict inequality -/

/-- **Orthogonal pieces never give norm additivity.** In a real inner product
space, two non-zero orthogonal vectors satisfy `‖x + y‖ < ‖x‖ + ‖y‖`. So the
`.md` remark "when the splitting remains orthogonal the mass decomposes
additively" cannot be read as a statement about the norms of the pieces. -/
theorem norm_add_lt_of_inner_eq_zero {F : Type*} [NormedAddCommGroup F]
    [InnerProductSpace ℝ F] {x y : F} (h : inner ℝ x y = 0) (hx : x ≠ 0) (hy : y ≠ 0) :
    ‖x + y‖ < ‖x‖ + ‖y‖ := by
  have hpy : 0 < ‖x‖ := norm_pos_iff.2 hx
  have hpz : 0 < ‖y‖ := norm_pos_iff.2 hy
  have hsq : ‖x + y‖ * ‖x + y‖ = ‖x‖ * ‖x‖ + ‖y‖ * ‖y‖ :=
    norm_add_sq_eq_norm_sq_add_norm_sq_real h
  nlinarith [norm_nonneg (x + y)]

end QOU.Torsion
