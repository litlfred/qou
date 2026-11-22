import QOU.MathlibExt.TemperleyLiebSpanning
import QOU.MathlibExt.TraceRadicalNondegenerate

/-!
# Wedderburn decompositions of `TL₂(δ)` and `TL₃(δ)`

**Bean `qou-cds1`.** `QOU.MathlibExt.HeckeToTemperleyLieb` proved
`TL_n(δ) ≅ H_n(v²)/⟨relators⟩` and left exactly one thing open:

    ⟨ U_i U_j U_i − v²·U_i ⟩  =  traceRadical tr_M

whose hard half — that the trace sees everything outside the ideal — needs
`TL_n(δ)` semisimple. `QOU.MathlibExt.TraceRadicalNondegenerate` proved
everything *downstream* of a Wedderburn decomposition, as a theorem about
whatever satisfies the hypothesis; nothing was known to satisfy it.

This file supplies the decomposition itself at `n = 2` and `n = 3`:

    TL₂(δ) ≃ₐ[R] R × R                                 (δ a unit)
    TL₃(δ) ≃ₐ[R] Matrix (Fin 2) (Fin 2) R × R          (δ and δ² − 1 units)

so at those two levels the hypothesis is **discharged rather than assumed**,
and `tl3_traceRadical` reads the open item's conclusion off it: the weighted
trace on `TL₃(δ)` has zero radical.

## Where the maps come from — nothing new is constructed

Both are representations the corpus already had. `tl2Rep` is in
`TemperleyLiebAlgebra`; `tl3Rep5` is in `TemperleyLiebSpanning`, built there to
prove linear independence. What is new is that each is **bijective**, and the
proof of that is the same three steps twice:

1. the images of the basis are linearly independent — already the content of
   the independence lemma, refactored out;
2. they *span*, which is where the unit hypotheses enter and is the only new
   computation;
3. so they are a basis of the target, and a linear map sending a basis to a
   basis is an isomorphism (`Module.Basis.equiv` plus `Module.Basis.ext`).

## Why `δ² − 1` must be a unit and not merely a non-zero-divisor

`TemperleyLiebSpanning.tl3Basis` needs `δ² − 1` only to be a non-zero-divisor —
enough for injectivity. Surjectivity is strictly stronger over a ring: an
injective endomorphism of a free module of finite rank need not be onto
(`×2 : ℤ → ℤ`). The determinant of the five images against the standard basis
of `Matrix (Fin 2) (Fin 2) R × R` is

    det = (δ² − 1)²

so the map is onto exactly when `δ² − 1` is invertible. That is not an artefact
of the chosen basis: at `δ = ±1` the algebra genuinely degenerates.

The inverse is *polynomial* in `c = δ⁻¹` and `w = (δ² − 1)⁻¹`, both carried as
primitive data with polynomial hypotheses `c * δ = 1` and `w * (δ² − 1) = 1`. So
§7c is satisfied for free — nothing here is over `ℝ`, nothing needs an ordering,
and no square root or division appears.

At the substrate `δ = q + q⁻¹ ≈ 2.01` with `q ≈ 1.11`, so `δ² − 1 ≈ 3.05`; both
hypotheses hold with room.

## What this does NOT do

**`n = 2` and `n = 3` are not `n`.** The decompositions are exhibited by hand,
one map each, and give no general theorem — `TL_n(δ)` is still not proved
semisimple, and the ideal equality above is still open for `n ≥ 4`. General `n`
needs the planar diagram basis, which is what everything in this arc keeps
arriving at from a different side.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
--   (Annals 126(2) 335-388, "Hecke algebra representations of braid groups and link
--   polynomials" — the TL-quotient + Markov-trace construction this file is about.
--   The key read `jones1985` until 2026-09-27 while carrying jones1987's DOI; the DOI
--   was the correct half. `jones1985` is the Bull. AMS 12(1) 103-111 von Neumann paper,
--   DOI 10.1090/S0273-0979-1985-15304-2 — a different paper, and one that IS ingested
--   (`library/s0273-0979-1985-15304-2/`), whereas jones1987 carries no `library:` field.
-/

namespace QOU.MathlibExt.TemperleyLiebWedderburn

open QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.TemperleyLiebSpanning
open QOU.MathlibExt.TraceRadicalNondegenerate
open QOU.QBeta.TemperleyLiebTower (traceRadical)

variable {R : Type*} [CommRing R]

/-! ## A unit is a non-zero-divisor

Stated because `tl3Basis` is phrased with the weaker hypothesis and this file
supplies the stronger one; without this the two do not compose. -/

theorem nonZeroDivisor_of_unit (δ w : R) (hw : w * (δ ^ 2 - 1) = 1) :
    ∀ x : R, x * (δ ^ 2 - 1) = 0 → x = 0 := by
  intro x hx
  have h : x = x * (w * (δ ^ 2 - 1)) := by rw [hw, mul_one]
  rw [h, ← mul_assoc, mul_comm x w, mul_assoc, hx, mul_zero]

/-! ## `n = 2` -/

section TL2

/-- The two images of `tl2Rep` on the basis `{1, e₀}`. -/
noncomputable def tl2Img (δ : R) : Fin 2 → R × R := ![(1, 1), (δ, 0)]

/-- `{(1,1), (δ,0)}` spans `R × R` as soon as `δ` is a unit — the `n = 2`
surjectivity computation, in the concrete target where it is one line. -/
theorem tl2Img_span (δ c : R) (hc : c * δ = 1) :
    Submodule.span R (Set.range (tl2Img δ)) = ⊤ := by
  rw [eq_top_iff]
  rintro ⟨x, y⟩ -
  have h1 : ((1 : R), (1 : R)) ∈ Submodule.span R (Set.range (tl2Img δ)) :=
    Submodule.subset_span ⟨0, rfl⟩
  have h2 : ((δ : R), (0 : R)) ∈ Submodule.span R (Set.range (tl2Img δ)) :=
    Submodule.subset_span ⟨1, rfl⟩
  have hxy : (x, y) = (c * (x - y)) • ((δ : R), (0 : R)) + y • ((1 : R), (1 : R)) := by
    simp only [Prod.smul_mk, smul_eq_mul, Prod.mk_add_mk, mul_zero, zero_add,
      Prod.mk.injEq]
    exact ⟨by linear_combination (y - x) * hc, by ring⟩
  rw [hxy]
  exact Submodule.add_mem _ (Submodule.smul_mem _ _ h2) (Submodule.smul_mem _ _ h1)

/-- The images are independent: the second coordinate kills `g₀` on its own,
and `δ` being a unit then kills `g₁`. -/
theorem tl2Img_linearIndependent (δ c : R) (hc : c * δ = 1) :
    LinearIndependent R (tl2Img δ) := by
  rw [Fintype.linearIndependent_iff]
  intro g hg
  simp only [tl2Img, Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one,
    Prod.smul_mk, Prod.mk_add_mk, smul_eq_mul, Prod.mk_eq_zero, mul_one, mul_zero,
    add_zero] at hg
  obtain ⟨h1, h0⟩ := hg
  have hg0 : g 0 = 0 := by linear_combination h0
  rw [hg0] at h1
  have hg1 : g 1 = 0 := by linear_combination c * h1 - g 1 * hc
  intro i
  fin_cases i
  · exact hg0
  · exact hg1

noncomputable def tl2ImgBasis {δ c : R} (hc : c * δ = 1) : Module.Basis (Fin 2) R (R × R) :=
  Module.Basis.mk (tl2Img_linearIndependent δ c hc) (by rw [tl2Img_span δ c hc])

theorem tl2Rep_basis (δ : R) (i : Fin 2) :
    tl2Rep δ (![(1 : TL2 (R := R) δ), tl2e δ] i) = tl2Img δ i := by
  fin_cases i
  · simp [tl2Img]; rfl
  · simp [tl2Img, tl2Rep_e]

noncomputable def tl2LinEquiv {δ c : R} (hc : c * δ = 1)
    (hδ : ∀ x : R, x * δ = 0 → x = 0) : TL2 (R := R) δ ≃ₗ[R] R × R :=
  (tl2Basis δ hδ).equiv (tl2ImgBasis hc) (Equiv.refl (Fin 2))

theorem tl2Rep_eq_linEquiv {δ c : R} (hc : c * δ = 1)
    (hδ : ∀ x : R, x * δ = 0 → x = 0) :
    (tl2Rep (R := R) δ).toLinearMap = (tl2LinEquiv hc hδ : TL2 (R := R) δ →ₗ[R] _) := by
  refine (tl2Basis δ hδ).ext fun i => ?_
  have hb : (tl2Basis (R := R) δ hδ) i = ![(1 : TL2 (R := R) δ), tl2e δ] i := by
    simp [tl2Basis, Module.Basis.coe_mk]
  have hi : tl2ImgBasis (R := R) hc i = tl2Img δ i := by
    simp [tl2ImgBasis, Module.Basis.coe_mk]
  simp only [tl2LinEquiv, LinearEquiv.coe_coe, Module.Basis.equiv_apply, Equiv.refl_apply]
  simp only [AlgHom.toLinearMap_apply, hb, hi]
  exact tl2Rep_basis δ i

/-- **`TL₂(δ) ≃ₐ[R] R × R` when `δ` is a unit.**

`TemperleyLiebAlgebra` says of exactly this statement that it is *not* claimed
there, and gives the reason: it had no upper bound. `tl2Basis` supplied the
upper bound; the remaining content is that `{(1,1), (δ,0)}` spans, whose
obstruction is the determinant `−δ`. -/
noncomputable def tl2AlgEquiv {δ c : R} (hc : c * δ = 1)
    (hδ : ∀ x : R, x * δ = 0 → x = 0) : TL2 (R := R) δ ≃ₐ[R] R × R :=
  AlgEquiv.ofBijective (tl2Rep δ) (by
    have h : ∀ x : TL2 (R := R) δ, tl2Rep δ x = tl2LinEquiv hc hδ x := fun x =>
      congrFun (congrArg DFunLike.coe (tl2Rep_eq_linEquiv hc hδ)) x
    refine ⟨fun a b hab => (tl2LinEquiv hc hδ).injective (by rw [← h, ← h, hab]), fun y => ?_⟩
    obtain ⟨x, hx⟩ := (tl2LinEquiv hc hδ).surjective y
    exact ⟨x, by rw [h, hx]⟩)

end TL2

/-! ## `n = 3` -/

section TL3

/-- The five images of `tl3Rep5` on the basis `{1, e₀, e₁, e₀e₁, e₁e₀}`. The
last two are `tl3M₀_mul_tl3M₁` and `tl3M₁_mul_tl3M₀`, already computed. -/
noncomputable def tl3Img (δ c : R) : Fin 5 → Matrix (Fin 2) (Fin 2) R × R :=
  ![(1, 1), (tl3M₀ δ, 0), (tl3M₁ δ c, 0),
    ((!![1, 1; 0, 0] : Matrix (Fin 2) (Fin 2) R), 0),
    ((!![1, 0; δ ^ 2 - 1, 0] : Matrix (Fin 2) (Fin 2) R), 0)]

/-- **Every element of `Matrix (Fin 2) (Fin 2) R × R` is this combination of the
five images.** The coefficients are the entries of the inverse of the `5 × 5`
matrix of images, which is why they are polynomial in `c` and `w` and why the
statement is an identity rather than an existence claim — inverting a matrix
whose determinant is `(δ² − 1)²` needs `w`, and nothing else. -/
theorem tl3Img_decomp (δ c w : R) (hc : c * δ = 1) (hw : w * (δ ^ 2 - 1) = 1)
    (A : Matrix (Fin 2) (Fin 2) R) (r : R) :
    (A, r)
      = r • tl3Img δ c 0
        + (c * A 0 0 - c * A 0 1 - c * w * A 1 0 + c * w * A 1 1 - δ * w * r) • tl3Img δ c 1
        + (δ * w * A 1 1 - δ * w * r) • tl3Img δ c 2
        + (A 0 1 - w * A 1 1 + w * r) • tl3Img δ c 3
        + (w * A 1 0 - w * A 1 1 + w * r) • tl3Img δ c 4 := by
  simp only [tl3Img, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.cons_val_two, Matrix.tail_cons, Matrix.cons_val_three, Matrix.cons_val_four,
    Prod.smul_mk, Prod.mk_add_mk, smul_eq_mul, Prod.mk.injEq]
  refine ⟨?_, by linear_combination (r * δ - r * δ) * hc⟩
  ext i j
  fin_cases i <;> fin_cases j <;> simp [tl3M₀, tl3M₁]
  · linear_combination (-A 0 0 + A 0 1 + w * A 1 0 - 2 * w * A 1 1 + w * r) * hc + r * hw
  · linear_combination (w * (r - A 1 1)) * hc
  · linear_combination (-(w * (r - A 1 1))) * hc + (-A 1 0) * hw
  · linear_combination (-(w * (r - A 1 1))) * hc + (r - A 1 1) * hw

theorem tl3Img_span (δ c w : R) (hc : c * δ = 1) (hw : w * (δ ^ 2 - 1) = 1) :
    Submodule.span R (Set.range (tl3Img δ c)) = ⊤ := by
  rw [eq_top_iff]
  rintro ⟨A, r⟩ -
  rw [tl3Img_decomp δ c w hc hw A r]
  exact Submodule.add_mem _ (Submodule.add_mem _ (Submodule.add_mem _ (Submodule.add_mem _
    (Submodule.smul_mem _ _ (Submodule.subset_span ⟨0, rfl⟩))
    (Submodule.smul_mem _ _ (Submodule.subset_span ⟨1, rfl⟩)))
    (Submodule.smul_mem _ _ (Submodule.subset_span ⟨2, rfl⟩)))
    (Submodule.smul_mem _ _ (Submodule.subset_span ⟨3, rfl⟩)))
    (Submodule.smul_mem _ _ (Submodule.subset_span ⟨4, rfl⟩))

/-- The images are independent. This is the content already inside
`TemperleyLiebSpanning.tl3_linearIndependent`; stated here in the target, where
`Module.Basis.mk` can use it. -/
theorem tl3Img_linearIndependent (δ c : R) (hc : c * δ = 1)
    (hu : ∀ x : R, x * (δ ^ 2 - 1) = 0 → x = 0) :
    LinearIndependent R (tl3Img δ c) := by
  rw [Fintype.linearIndependent_iff]
  intro g hg
  simp only [tl3Img, Fin.sum_univ_five, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.head_cons, Matrix.cons_val_two, Matrix.tail_cons, Matrix.cons_val_three,
    Matrix.cons_val_four, Prod.smul_mk, Prod.mk_add_mk, smul_eq_mul,
    Prod.mk_eq_zero] at hg
  obtain ⟨hMat, hsc⟩ := hg
  have h0 : g 0 = 0 := by simpa using hsc
  rw [h0] at hMat
  simp only [zero_smul, zero_add] at hMat
  obtain ⟨h1, h2, h3, h4⟩ := tl3_matrix_indep hc hu (g 1) (g 2) (g 3) (g 4) hMat
  intro i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2
  · exact h3
  · exact h4

noncomputable def tl3ImgBasis {δ c w : R} (hc : c * δ = 1) (hw : w * (δ ^ 2 - 1) = 1) :
    Module.Basis (Fin 5) R (Matrix (Fin 2) (Fin 2) R × R) :=
  Module.Basis.mk (tl3Img_linearIndependent δ c hc (nonZeroDivisor_of_unit δ w hw))
    (by rw [tl3Img_span δ c w hc hw])

theorem tl3Rep5_basis {δ c : R} (hc : c * δ = 1) (i : Fin 5) :
    tl3Rep5 hc (![(1 : TL3 (R := R) δ), a3 δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ] i)
      = tl3Img δ c i := by
  fin_cases i <;>
    simp [tl3Img, tl3Rep5_e, tl3Fam5, a3, b3, tl3M₀_mul_tl3M₁ hc, tl3M₁_mul_tl3M₀ hc]
  rfl

noncomputable def tl3LinEquiv {δ c w : R} (hc : c * δ = 1) (hw : w * (δ ^ 2 - 1) = 1) :
    TL3 (R := R) δ ≃ₗ[R] Matrix (Fin 2) (Fin 2) R × R :=
  (tl3Basis hc (nonZeroDivisor_of_unit δ w hw)).equiv (tl3ImgBasis hc hw) (Equiv.refl (Fin 5))

theorem tl3Rep5_eq_linEquiv {δ c w : R} (hc : c * δ = 1) (hw : w * (δ ^ 2 - 1) = 1) :
    (tl3Rep5 hc).toLinearMap = (tl3LinEquiv hc hw : TL3 (R := R) δ →ₗ[R] _) := by
  refine (tl3Basis hc (nonZeroDivisor_of_unit δ w hw)).ext fun i => ?_
  have hb : (tl3Basis (R := R) hc (nonZeroDivisor_of_unit δ w hw)) i
      = ![(1 : TL3 (R := R) δ), a3 δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ] i := by
    simp [tl3Basis, Module.Basis.coe_mk]
  have hi : tl3ImgBasis (R := R) hc hw i = tl3Img δ c i := by
    simp [tl3ImgBasis, Module.Basis.coe_mk]
  simp only [tl3LinEquiv, LinearEquiv.coe_coe, Module.Basis.equiv_apply, Equiv.refl_apply]
  simp only [AlgHom.toLinearMap_apply, hb, hi, tl3Rep5_basis]

theorem tl3Rep5_bijective {δ c w : R} (hc : c * δ = 1) (hw : w * (δ ^ 2 - 1) = 1) :
    Function.Bijective (tl3Rep5 (R := R) (δ := δ) hc) := by
  have h : ∀ x : TL3 (R := R) δ, tl3Rep5 hc x = tl3LinEquiv hc hw x := fun x =>
    congrFun (congrArg DFunLike.coe (tl3Rep5_eq_linEquiv hc hw)) x
  refine ⟨fun a b hab => (tl3LinEquiv hc hw).injective (by rw [← h, ← h, hab]), fun y => ?_⟩
  obtain ⟨x, hx⟩ := (tl3LinEquiv hc hw).surjective y
  exact ⟨x, by rw [h, hx]⟩

/-- **`TL₃(δ) ≃ₐ[R] Matrix (Fin 2) (Fin 2) R × R` when `δ` and `δ² − 1` are
units** — the Wedderburn decomposition at `n = 3`.

The block shape `1 ⊕ 2` matches `TemperleyLiebTower.catalan_three`, which
records the same decomposition as the partition count `1² + 2² = 5`, arrived at
from the representation-theoretic side. The two now agree as theorems rather
than as a table and a table. -/
noncomputable def tl3AlgEquiv {δ c w : R} (hc : c * δ = 1) (hw : w * (δ ^ 2 - 1) = 1) :
    TL3 (R := R) δ ≃ₐ[R] Matrix (Fin 2) (Fin 2) R × R :=
  AlgEquiv.ofBijective (tl3Rep5 hc) (tl3Rep5_bijective hc hw)

end TL3

/-! ## The payoff: the open item's conclusion, at `n = 3` -/

section Payoff

/-- A weighted trace on the decomposed algebra: `y₁` on the scalar block, `y₂`
on the `2 × 2` block. This is the shape `TraceRadicalNondegenerate` treats in
general — a weighted sum of block traces, which is what a Markov trace is. -/
def prodTrace (y₁ y₂ : R) : Matrix (Fin 2) (Fin 2) R × R → R :=
  fun p => y₁ * p.2 + y₂ * Matrix.trace p.1

/-- The weighted trace has zero radical as soon as both weights are
non-zero-divisors. Unlike the general statement in
`TraceRadicalNondegenerate`, this needs no field: the two blocks are concrete,
so `Matrix.ext_iff_trace_mul_right` applies directly. -/
theorem prodTrace_traceRadical {y₁ y₂ : R}
    (h₁ : ∀ x : R, y₁ * x = 0 → x = 0) (h₂ : ∀ x : R, y₂ * x = 0 → x = 0) :
    traceRadical (prodTrace y₁ y₂) = {(0 : Matrix (Fin 2) (Fin 2) R × R)} := by
  ext p
  obtain ⟨A, r⟩ := p
  constructor
  · intro hp
    have hr : r = 0 := by
      have := hp (0, 1)
      simpa [prodTrace] using h₁ _ (by simpa [prodTrace] using this)
    have hA : A = 0 := by
      refine matrix_eq_zero_of_forall_trace_mul fun x => ?_
      have := hp (x, 0)
      simp only [prodTrace, Prod.mk_mul_mk, mul_zero, zero_add] at this
      exact h₂ _ this
    simp [hA, hr]
  · rintro hp
    have hA : A = 0 := (Prod.mk_eq_zero.mp hp).1
    have hr : r = 0 := (Prod.mk_eq_zero.mp hp).2
    subst hA; subst hr
    intro b
    simp [prodTrace]

/-- **The weighted trace on `TL₃(δ)` has zero radical.**

This is the `⊇` half of `HeckeToTemperleyLieb`'s open item, at `n = 3`, with no
hypothesis left standing in for semisimplicity: the decomposition is
`tl3AlgEquiv`, and the weights are only required to be non-zero-divisors — which
`TemperleyLiebTower.yw_pos` already gives for the Markov weights at `1 < q`.

It is `n = 3` only. Nothing here bears on general `n`. -/
theorem tl3_traceRadical {δ c w y₁ y₂ : R} (hc : c * δ = 1) (hw : w * (δ ^ 2 - 1) = 1)
    (h₁ : ∀ x : R, y₁ * x = 0 → x = 0) (h₂ : ∀ x : R, y₂ * x = 0 → x = 0) :
    traceRadical (prodTrace y₁ y₂ ∘ (tl3AlgEquiv hc hw : TL3 (R := R) δ → _))
      = {(0 : TL3 (R := R) δ)} := by
  rw [traceRadical_comp_algEquiv (tl3AlgEquiv (R := R) hc hw) (prodTrace y₁ y₂),
    prodTrace_traceRadical h₁ h₂]
  ext x
  simp [Set.mem_preimage, map_eq_zero_iff _ (tl3AlgEquiv hc hw).injective]

end Payoff

end QOU.MathlibExt.TemperleyLiebWedderburn
