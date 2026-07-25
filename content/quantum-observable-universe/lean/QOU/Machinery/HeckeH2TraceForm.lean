import QOU.Machinery.HeckeH2Wedderburn
import Mathlib.RingTheory.Trace.Basic

/-!
# QOU.Machinery.HeckeH2TraceForm — the regular trace of H₂(q)

The **trace capstone** for the rank-two Hecke algebra `H2A R h`
(`HeckeH2AlgebraInstance`). Two statements, both sorry-free over a
generic `[CommRing R]` (§7c — nothing archimedean is used):

* `regTraceForm_apply` — the regular trace (trace of left
  multiplication, i.e. Mathlib's `Algebra.trace`) is the explicit
  linear form
  $$\mathrm{tr}_{\mathrm{reg}}(a\,\gamma + b\,\sigma) = 2a + h\,b.$$
  The `2` is $\dim_R H_2 = 2$ (the trace of the identity); the `h`
  is the trace of the generator $\sigma$ (its regular matrix
  $\bigl(\begin{smallmatrix}0&1\\1&h\end{smallmatrix}\bigr)$).

* `regTrace_eq_sum_characters` — the Wedderburn reading: for the two
  **distinct** roots $l_+ , l_-$ of the Hecke quadratic
  $l^2 = h\,l + 1$, the regular trace is the **sum of the two
  irreducible characters** `character l± ·` of `HeckeH2Wedderburn`,
  $$\mathrm{tr}_{\mathrm{reg}} = \chi_{l_+} + \chi_{l_-},$$
  because the regular representation $H_2 \cong R \times R$
  decomposes as the direct sum of the two one-dimensional blocks.
  The only ring fact used is Vieta's $l_+ + l_- = h$, forced by the
  two root equations and $l_+ \neq l_-$.

This is the trace-level companion to `HeckeH2Wedderburn.wedderburn`:
that file split the algebra; this one reads its regular trace off the
same two characters. Higher ranks stay open (bean `qou-vndn`).

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/

namespace QOU.Machinery.H3
namespace H2A

open scoped Matrix

variable {R : Type*} [CommRing R] {h : R}

/-- The coordinate linear equivalence `H₂(q) ≃ₗ (Fin 2 → R)`,
    `a·γ + b·σ ↦ ![a, b]`. -/
def coordEquiv : H2A R h ≃ₗ[R] (Fin 2 → R) where
  toFun x := ![x.a, x.b]
  invFun v := ⟨v 0, v 1⟩
  map_add' x y := by funext i; fin_cases i <;> simp
  map_smul' c x := by funext i; fin_cases i <;> simp
  left_inv x := by cases x; rfl
  right_inv v := by funext i; fin_cases i <;> rfl

@[simp] lemma coordEquiv_apply (x : H2A R h) (i : Fin 2) :
    coordEquiv x i = ![x.a, x.b] i := rfl

/-- The standard basis `{γ, σ}` of `H₂(q)` as an R-module. -/
noncomputable def basisH2 : Module.Basis (Fin 2) R (H2A R h) :=
  Module.Basis.ofEquivFun coordEquiv

@[simp] lemma basisH2_repr_apply (y : H2A R h) (i : Fin 2) :
    (basisH2.repr y) i = coordEquiv y i :=
  Module.Basis.ofEquivFun_repr_apply _ _ _

@[simp] lemma basisH2_zero : (basisH2 : Module.Basis (Fin 2) R (H2A R h)) 0 = ⟨1, 0⟩ := by
  rw [basisH2, Module.Basis.coe_ofEquivFun]
  apply (coordEquiv (R := R) (h := h)).injective
  funext i; fin_cases i <;> simp [coordEquiv]

@[simp] lemma basisH2_one : (basisH2 : Module.Basis (Fin 2) R (H2A R h)) 1 = ⟨0, 1⟩ := by
  rw [basisH2, Module.Basis.coe_ofEquivFun]
  apply (coordEquiv (R := R) (h := h)).injective
  funext i; fin_cases i <;> simp [coordEquiv]

/-- **The regular trace of H₂(q).** The trace of left multiplication
    by `a·γ + b·σ` is `2a + h·b` — the `2` is `dim_R H₂ = 2`, the `h`
    is the trace of the generator `σ`. -/
theorem regTraceForm_apply (x : H2A R h) :
    Algebra.trace R (H2A R h) x = 2 * x.a + h * x.b := by
  rw [Algebra.trace_eq_matrix_trace basisH2, Matrix.trace_fin_two]
  simp only [Algebra.leftMulMatrix_eq_repr_mul, basisH2_zero, basisH2_one,
    basisH2_repr_apply, coordEquiv_apply, Matrix.cons_val_zero, Matrix.cons_val_one,
    mul_a, mul_b]
  ring

/-- Vieta for the Hecke quadratic: two **distinct** roots of
    `l² = h·l + 1` sum to `h`. Needs `NoZeroDivisors` — over a ring
    with zero divisors two distinct roots need not obey Vieta. -/
lemma root_sum_eq [NoZeroDivisors R] (lp lm : R) (hlp : lp * lp = h * lp + 1)
    (hlm : lm * lm = h * lm + 1) (hne : lp ≠ lm) : lp + lm = h := by
  have hd : lp - lm ≠ 0 := sub_ne_zero.mpr hne
  have key : (lp + lm) * (lp - lm) = h * (lp - lm) := by linear_combination hlp - hlm
  exact mul_right_cancel₀ hd key

/-- **Wedderburn reading of the regular trace.** The regular trace of
    `H₂(q)` is the sum of the two irreducible characters `χ_{l±}` for
    the distinct roots `l±` of the Hecke quadratic — the trace-level
    shadow of the split `H₂ ≅ R × R` (`HeckeH2Wedderburn.wedderburn`). -/
theorem regTrace_eq_sum_characters [NoZeroDivisors R] (lp lm : R)
    (hlp : lp * lp = h * lp + 1) (hlm : lm * lm = h * lm + 1) (hne : lp ≠ lm)
    (x : H2A R h) :
    Algebra.trace R (H2A R h) x = character lp hlp x + character lm hlm x := by
  rw [regTraceForm_apply, character_apply, character_apply]
  have hsum := root_sum_eq lp lm hlp hlm hne
  linear_combination (-x.b) * hsum

end H2A
end QOU.Machinery.H3
