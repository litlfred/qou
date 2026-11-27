/-
  The Hopf-link complement has zero complex volume: the two algebraic steps.

  Bean `qou-c9fh` ("GATE: is CS(Hopf link complement) nonzero?").  The gate was set in
  `docs/audits/2026-08-07-two-row-projection-is-the-pairwise-cap.md` §4: *"verify `CS`
  of the Hopf-link complement is nonzero and well-defined … If `CS(Hopf) = 0`, this
  resolution dies immediately."*  This file and
  `docs/audits/2026-11-22-hopf-link-complement-complex-volume.md` answer it: the value is
  `0`, by two invariants rather than by a computation.

  ═══ THE ARGUMENT ═══

  `S³ ∖ Hopf ≅ T² × (0,1)`, so `π₁ = ℤ²` and every representation into `SL₂(ℂ)` has
  abelian image.

  (A) **Boundary-parabolic representations land in `±P`.**  If a generator goes to a
      nontrivial unipotent `U_b = [[1,b],[0,1]]`, `b ≠ 0`, then everything commuting
      with it is `±[[1,c],[0,1]]` (`commute_unipotent_iff`,
      `eq_pm_unipotent_of_commute`, below).  So the whole image lies in `±P`, `P` the
      unipotent subgroup.  The complex volume of a boundary-parabolic `ρ` is
      `⟨ρ_*[M, ∂M], ĉ⟩` with `ρ_*[M, ∂M] ∈ H₃(SL₂ℂ, P)` (up to the `±`); when `ρ` itself
      factors through `P` the class comes from `H₃(P, P) = 0`, so the complex volume
      `Vol + i·CS` is `0`.  The functoriality step is cited, not formalized here.
      -- Ref: [garoufalidis-thurston-zickert2011] §4.1 (the fundamental class of a
      --   decorated representation), §6.1 (`[ρ] ∈ H₃(SL(n,ℂ), N)` and the map to the
      --   extended Bloch group), §7 (independence of the decoration); held at
      --   library/arxiv-1111.2828v2/.

  (B) **The Chern–Simons form of a connection pulled back from `T²` vanishes
      pointwise.**  Every flat connection on `T² × I` is gauge-equivalent to the
      pullback `π^*a` of a flat connection on `T²` (holonomy determines it, and
      `π₁(T² × I) = π₁(T²)`), and `CS(π^*a) = π^*(cs(a))` with `cs(a)` a 3-form on a
      2-manifold.  At each point that is an alternating 3-form on a 2-dimensional
      tangent space composed with the differential of `π`, which is zero
      (`alternating_three_eq_zero_of_finrank_two`, `pullback_alternating_three_eq_zero`,
      below).  So with the product trivialisation of the boundary, `CS = 0` for every
      representation, parabolic or not.

  `Vol = 0` for every representation as well: the complement is Seifert-fibred, its
  simplicial volume is `0`, and `|Vol(ρ)| ≤ v₃ · ‖M‖` (Gromov–Thurston).
  -- Ref: [thurston1978] ch. 6; [gromov1982].

  ═══ WHAT IS PROVED HERE, AND WHAT IS NOT ═══

  Proved, sorry-free: the two algebraic facts that (A) and (B) turn on.
  Not proved: the topology around them — the homeomorphism `S³ ∖ Hopf ≅ T² × (0,1)`,
  the functoriality of the fundamental class, the gauge statement, Gromov's inequality.  Those are cited.
  No physical quantity enters this file.

  Scope of the conclusion: **(b), structural**, with the invariants named above.  A
  nonzero "CS(Hopf)" can only come from choosing a boundary trivialisation other than
  the product one, that is, from a convention picked by hand.
-/

import Mathlib.LinearAlgebra.Alternating.Basic
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.LinearIndependent.Lemmas
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Tactic.LinearCombination

namespace QOU.Archimedean.HopfLinkComplexVolume

/-! ### (B) A 3-form on a 2-dimensional space is zero -/

section Forms

variable {K V W : Type*} [Field K] [AddCommGroup V] [Module K V]
  [AddCommGroup W] [Module K W] [FiniteDimensional K W]

/-- **An alternating 3-form on a 2-dimensional space is zero.**  Three vectors in a
    space of dimension `2` are linearly dependent, and an alternating map vanishes on a
    linearly dependent family. -/
theorem alternating_three_eq_zero_of_finrank_two (hW : Module.finrank K W = 2)
    (ω : W [⋀^Fin 3]→ₗ[K] K) : ω = 0 := by
  ext v
  have hdep : ¬ LinearIndependent K v := by
    intro hli
    have := hli.fintype_card_le_finrank
    simp [hW] at this
  exact ω.map_linearDependent v hdep

/-- **A 3-form pulled back from a 2-dimensional space vanishes.**  This is the pointwise
    content of `CS(π^*a) = π^*(cs(a)) = 0` for `π : T² × I → T²`: the differential of
    `π` lands in the 2-dimensional tangent space of `T²`. -/
theorem pullback_alternating_three_eq_zero (hW : Module.finrank K W = 2)
    (f : V →ₗ[K] W) (ω : W [⋀^Fin 3]→ₗ[K] K) :
    ω.compLinearMap f = 0 := by
  rw [alternating_three_eq_zero_of_finrank_two hW ω]
  ext v
  rfl

/-- Non-vacuity check for the hypothesis: the dimension the lemma needs is the one the
    torus tangent space has (`K²`). -/
example : Module.finrank K (Fin 2 → K) = 2 := by simp

end Forms

/-! ### (A) The centraliser of a nontrivial unipotent in `SL₂` -/

section Centraliser

variable {K : Type*} [Field K]

open Matrix

/-- The unipotent `U_b = [[1, b], [0, 1]]`. -/
def unipotent (b : K) : Matrix (Fin 2) (Fin 2) K := !![1, b; 0, 1]

/-- **What commutes with a nontrivial unipotent.**  For `b ≠ 0`, `B` commutes with `U_b`
    exactly when `B` is upper triangular with equal diagonal entries. -/
theorem commute_unipotent_iff {b : K} (hb : b ≠ 0) (B : Matrix (Fin 2) (Fin 2) K) :
    B * unipotent b = unipotent b * B ↔ B 1 0 = 0 ∧ B 0 0 = B 1 1 := by
  constructor
  · intro h
    have h00 := congrFun (congrFun h 0) 0
    have h01 := congrFun (congrFun h 0) 1
    simp [unipotent, Matrix.mul_apply, Fin.sum_univ_two] at h00 h01
    -- after `simp`: h00 : b = 0 ∨ B 1 0 = 0 ;  h01 : B 0 0 * b + B 0 1 = B 0 1 + b * B 1 1
    have h10 : B 1 0 = 0 := h00.resolve_left hb
    refine ⟨h10, ?_⟩
    have : b * (B 0 0 - B 1 1) = 0 := by linear_combination h01
    rcases mul_eq_zero.1 this with h | h
    · exact absurd h hb
    · exact sub_eq_zero.1 h
  · rintro ⟨h10, hd⟩
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [unipotent, Matrix.mul_apply, Fin.sum_univ_two, h10, hd, mul_comm]
    all_goals ring

/-- **A determinant-one matrix commuting with a nontrivial unipotent is `±` a unipotent.**
    So a representation of `ℤ²` into `SL₂` that sends one element to a nontrivial
    parabolic sends everything into `±P`. -/
theorem eq_pm_unipotent_of_commute {b : K} (hb : b ≠ 0) (B : Matrix (Fin 2) (Fin 2) K)
    (hdet : B.det = 1) (hc : B * unipotent b = unipotent b * B) :
    (B 0 0 = 1 ∨ B 0 0 = -1) ∧ B = B 0 0 • unipotent (B 0 0 * B 0 1) := by
  obtain ⟨h10, hd⟩ := (commute_unipotent_iff hb B).1 hc
  have hsq : B 0 0 * B 0 0 = 1 := by
    rw [Matrix.det_fin_two, h10, ← hd] at hdet
    simpa using hdet
  have hpm : B 0 0 = 1 ∨ B 0 0 = -1 := by
    have : (B 0 0 - 1) * (B 0 0 + 1) = 0 := by linear_combination hsq
    rcases mul_eq_zero.1 this with h | h
    · exact Or.inl (sub_eq_zero.1 h)
    · exact Or.inr (eq_neg_of_add_eq_zero_left h)
  refine ⟨hpm, ?_⟩
  ext i j
  fin_cases i <;> fin_cases j <;> simp [unipotent, h10, ← hd]
  all_goals first
    | exact hsq.symm
    | (rw [← mul_assoc, hsq, one_mul])

/-- Non-vacuity check: `U_1` has determinant one and commutes with itself, so the
    hypotheses of `eq_pm_unipotent_of_commute` are met by a genuine parabolic. -/
example : (unipotent (1 : K)).det = 1 ∧
    unipotent (1 : K) * unipotent 1 = unipotent 1 * unipotent 1 := by
  refine ⟨?_, rfl⟩
  simp [unipotent, Matrix.det_fin_two]

end Centraliser

end QOU.Archimedean.HopfLinkComplexVolume
