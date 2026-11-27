/-
  The remaining photon assertions of `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md`,
  formalised (owner 2026-11-25: "lean formalize all assertions on the photon").

  Photon `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`; with the `H₃(q)` relations `σ₁⁻¹ = σ₁ − h`, so
  the vertex is `QOU.Mass.BorromeanPhotonFactorisation.vertex h a b = a(b − h)`.

  1. **One-photon Markov trace** (`markov_trace_photon`):
     `t(γ) = 1 + z(φ₀ + φ₁) + z(z − h)φ₀₁` for any linear `t` with `t 1 = 1`, `t a = t b = z`
     and the Markov rule `t(a·b) = z·t(a)`.
  2. **The flip-reverse symmetry preserves the photon family** (`flipReverse_photon`). For an
     anti-homomorphism `f` (an algebra map to `Aᵐᵒᵖ`) with `f a = b`, `f b = a`, the image of
     `γ(φ₀, φ₁, φ₀₁)` is `γ(φ₁ + hφ₀₁, φ₀ − hφ₀₁, φ₀₁)`. Every cyclic trace is invariant
     under this map (`QOU.Mass.PhotonTraceLemmas.trace_flip_reverse`), so it acts on the photon
     space without changing any observable.
  3. **The reflection block** (`refl*`). Explicit `2 × 2` matrices satisfying the `H₃(q)`
     relations; in them the trace-free parts satisfy
     `tr((A₀ + A₁)²) = 2`, `tr((A₀ + A₁)·A_V) = 0`, `A₀² = ((q² + 1)²/(4q²))·1`
     (so `A₀` is not nilpotent), and the vertex satisfies `V² + (1 + h²)V + 1 = 0`.
  4. **`1, V, V²` are independent** in any algebra carrying the trivial character plus the
     reflection block (`independent_of_rep`), provided `h² + 3 ≠ 0`. Combined with
     `QOU.PhotonTangent.borromean_weights_forced`, this removes the measured hypothesis for
     every such algebra (`borromean_weights_forced_of_rep`).

  Field `K` with `q ≠ 0` and `(2 : K) ≠ 0` where division is needed; otherwise generic (§7c).

  -- Ref: [leitner2026] predicted-spectra, def:photon
  -- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9
-/
import QOU.StandardModel.PhotonTangent
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FinCases

namespace QOU.PhotonAssertions

open QOU.Mass.BorromeanPhotonFactorisation

section Trace

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **One-photon Markov trace.** -/
theorem markov_trace_photon {h z : R} {a b : A} (t : A →ₗ[R] R)
    (h1 : t 1 = 1) (ha : t a = z) (hb : t b = z) (hmk : t (a * b) = z * t a)
    (φ₀ φ₁ φ₀₁ : R) :
    t (1 + φ₀ • a + φ₁ • b + φ₀₁ • vertex h a b)
      = 1 + z * (φ₀ + φ₁) + z * (z - h) * φ₀₁ := by
  rw [vertex_eq]
  simp only [map_add, map_smul, map_sub, h1, ha, hb, hmk, smul_eq_mul]
  ring

end Trace

section FlipReverse

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **The flip-reverse anti-automorphism maps photons to photons.** `f` is an algebra map
`A → Aᵐᵒᵖ`, i.e. an anti-homomorphism, swapping `a` and `b`. -/
theorem flipReverse_photon {h : R} {a b : A} (f : A →ₐ[R] Aᵐᵒᵖ)
    (fa : (f a).unop = b) (fb : (f b).unop = a) (φ₀ φ₁ φ₀₁ : R) :
    (f (1 + φ₀ • a + φ₁ • b + φ₀₁ • vertex h a b)).unop
      = 1 + (φ₁ + h * φ₀₁) • a + (φ₀ - h * φ₀₁) • b + φ₀₁ • vertex h a b := by
  have hv : (f (vertex h a b)).unop = vertex h a b + h • a - h • b := by
    rw [vertex, map_mul, MulOpposite.unop_mul, map_sub, map_smul, map_one,
      MulOpposite.unop_sub, MulOpposite.unop_smul, MulOpposite.unop_one, fa, fb]
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one]
    abel
  simp only [map_add, map_smul, map_one, MulOpposite.unop_add, MulOpposite.unop_smul,
    MulOpposite.unop_one, fa, fb, hv]
  simp only [smul_add, smul_sub, smul_smul, add_smul, sub_smul]
  rw [mul_comm φ₀₁ h]
  abel

end FlipReverse

section Reflection

variable {K : Type*} [Field K]

/-- `σ₀` in the reflection block. -/
def reflA (q : K) : Matrix (Fin 2) (Fin 2) K := !![q, 1; 0, -q⁻¹]
/-- `σ₁` in the reflection block. -/
def reflB (q : K) : Matrix (Fin 2) (Fin 2) K := !![-q⁻¹, 0; 1, q]
/-- The vertex `σ₀σ₁⁻¹` in the reflection block. -/
def reflV (q : K) : Matrix (Fin 2) (Fin 2) K :=
  reflA q * (reflB q - (q - q⁻¹) • (1 : Matrix (Fin 2) (Fin 2) K))

/-- Trace-free part. -/
def tl (M : Matrix (Fin 2) (Fin 2) K) : Matrix (Fin 2) (Fin 2) K :=
  M - (M.trace / 2) • (1 : Matrix (Fin 2) (Fin 2) K)

theorem reflA_quad {q : K} (hq : q ≠ 0) :
    reflA q * reflA q = (q - q⁻¹) • reflA q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [reflA, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem reflB_quad {q : K} (hq : q ≠ 0) :
    reflB q * reflB q = (q - q⁻¹) • reflB q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [reflB, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem refl_braid {q : K} (hq : q ≠ 0) :
    reflA q * reflB q * reflA q = reflB q * reflA q * reflB q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [reflA, reflB, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem reflV_eq {q : K} (hq : q ≠ 0) :
    reflV q = !![1 - q ^ 2, q⁻¹; -q⁻¹, -(q⁻¹ ^ 2)] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [reflV, reflA, reflB, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- The vertex satisfies `V² + (1 + h²)V + 1 = 0` in the reflection block. -/
theorem reflV_quad {q : K} (hq : q ≠ 0) :
    reflV q * reflV q = -(1 + (q - q⁻¹) ^ 2) • reflV q - 1 := by
  rw [reflV_eq hq]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- `tr((A₀ + A₁)²) = 2` for the trace-free parts. -/
theorem tl_sum_norm {q : K} (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    ((tl (reflA q) + tl (reflB q)) * (tl (reflA q) + tl (reflB q))).trace = 2 := by
  simp [tl, reflA, reflB, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two]
  field_simp
  ring

/-- `σ₀ + σ₁` is orthogonal to the vertex in the trace form on trace-free parts. -/
theorem tl_sum_orth_vertex {q : K} (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    ((tl (reflA q) + tl (reflB q)) * tl (reflV q)).trace = 0 := by
  rw [reflV_eq hq]
  simp [tl, reflA, reflB, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two]
  field_simp
  ring

/-- The trace-free part of `σ₀` squares to a nonzero scalar: it is not nilpotent. -/
theorem tl_A_sq {q : K} (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    tl (reflA q) * tl (reflA q) = ((q ^ 2 + 1) ^ 2 / (4 * q ^ 2)) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  have h4 : (4 : K) ≠ 0 := by
    rw [show (4 : K) = 2 * 2 by norm_num]; exact mul_ne_zero h2 h2
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [tl, reflA, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring


/-- The trace-form Gram matrix of the trace-free parts of `σ₀, σ₁, V`. -/
def reflGram (q : K) : Matrix (Fin 3) (Fin 3) K :=
  Matrix.of fun i j =>
    ((![tl (reflA q), tl (reflB q), tl (reflV q)] i) * (![tl (reflA q), tl (reflB q), tl (reflV q)] j)).trace

/-- **The three trace-free parts span `sl₂`**: their Gram determinant is
`−(q² − q + 1)²(q² + q + 1)²/(2q⁴)`, nonzero when `q⁴ + q² + 1 ≠ 0`. -/
theorem reflGram_det {q : K} (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    (reflGram q).det = -((q ^ 2 - q + 1) ^ 2 * (q ^ 2 + q + 1) ^ 2) / (2 * q ^ 4) := by
  rw [Matrix.det_fin_three]
  simp [reflGram, reflV_eq hq, tl, reflA, reflB, Matrix.trace_fin_two, Matrix.mul_apply,
    Fin.sum_univ_two]
  field_simp
  ring

end Reflection

section Independence

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]

/-- **`1, V, V²` are independent** in any `K`-algebra with a representation on
`K × M₂(K)` sending the vertex to `(1, reflV q)`, when `h² + 3 ≠ 0`. -/
theorem independent_of_rep {q : K} (hq : q ≠ 0) (h3 : (q - q⁻¹) ^ 2 + 3 ≠ 0) {V : A}
    (ρ : A →ₐ[K] K × Matrix (Fin 2) (Fin 2) K) (hV : ρ V = (1, reflV q)) :
    LinearIndependent K ![(1 : A), V, V * V] := by
  apply LinearIndependent.of_comp ρ.toLinearMap
  rw [Fintype.linearIndependent_iff]
  intro c hc
  simp only [Fin.sum_univ_three, Function.comp_apply, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, AlgHom.toLinearMap_apply, map_one,
    map_mul, hV] at hc
  have h1 := congrArg Prod.fst hc
  have h2 := congrArg Prod.snd hc
  simp only [Prod.fst_add, Prod.smul_fst, Prod.fst_one, Prod.fst_mul, smul_eq_mul, mul_one,
    Prod.fst_zero] at h1
  simp only [Prod.snd_add, Prod.smul_snd, Prod.snd_one, Prod.snd_mul, Prod.snd_zero] at h2
  rw [reflV_eq hq] at h2
  have e01 := congrFun (congrFun h2 0) 1
  have e00 := congrFun (congrFun h2 0) 0
  simp [Matrix.mul_apply, Fin.sum_univ_two] at e01 e00
  have k1 : c 1 * q ^ 2 = c 2 * (q ^ 4 - q ^ 2 + 1) := by
    field_simp at e01
    linear_combination e01
  have k0' : q ^ 2 * (c 0 - c 2) = 0 := by
    field_simp at e00
    linear_combination e00 - (1 - q ^ 2) * k1
  have k0 : c 0 = c 2 := by
    rcases mul_eq_zero.mp k0' with h | h
    · exact absurd h (pow_ne_zero 2 hq)
    · exact sub_eq_zero.mp h
  have h3' : q ^ 4 + q ^ 2 + 1 ≠ 0 := by
    intro h; apply h3; field_simp; linear_combination h
  have k2 : c 2 = 0 := by
    have : c 2 * (q ^ 4 + q ^ 2 + 1) = 0 := by linear_combination q ^ 2 * h1 - k1 - q ^ 2 * k0
    exact (mul_eq_zero.mp this).resolve_right h3'
  have k1' : c 1 = 0 := by
    rw [k2, zero_mul] at k1
    exact (mul_eq_zero.mp k1).resolve_right (pow_ne_zero 2 hq)
  intro i; fin_cases i
  · simpa [k2] using k0
  · simpa using k1'
  · simpa using k2

open QOU.PhotonTangent in
/-- **The Borromean photon weights are forced** in every algebra satisfying the `H₃(q)`
relations that carries the trivial character plus the reflection block. -/
theorem borromean_weights_forced_of_rep {q q' : K} (hq : q ≠ 0) (hqq : q * q' = 1)
    (h3 : (q - q⁻¹) ^ 2 + 3 ≠ 0) {a b : A} (H : HeckeH3Rel (q - q') a b)
    (ρ : A →ₐ[K] K × Matrix (Fin 2) (Fin 2) K)
    (hV : ρ (vertex (q - q') a b) = (1, reflV q)) {x y : K}
    (hxy : (1 + x • vertex (q - q') a b) * (1 + y • vertex (q - q') a b)
      = vertex (q - q') a b * vertex (q - q') a b * vertex (q - q') a b) :
    (x = q * (q - q') ∧ y = -(q' * (q - q'))) ∨ (x = -(q' * (q - q')) ∧ y = q * (q - q')) :=
  borromean_weights_forced H rfl hqq (independent_of_rep hq h3 ρ hV) hxy

end Independence

end QOU.PhotonAssertions
