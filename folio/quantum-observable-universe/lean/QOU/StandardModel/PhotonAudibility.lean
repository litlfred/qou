/-
  What the photon responses can hear (audit `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md` §14).

  1. **Responses determine a state modulo the radical of the trace form**
     (`responses_determine_mod_radical`). If products of photons span the algebra and two
     states `x, x'` give the same response `t(y·x) = t(y·x')` for every product `y` of photons,
     then `x − x'` lies in the radical `{u : ∀ y, t(y·u) = 0}`. This corrects the earlier claim
     (audit §3, `conj:bring-isospectrality-question` item 3) that responses factor through the
     cocenter `H/[H,H]`. That is true of the zero-photon response `t(x)` only.
  2. **Under convention D the sign direction is inaudible** (`sign_inaudible_D`). In the
     concrete model of `H₃(q)`, the element `e = Σ_w (−q⁻¹)^{ℓ(w)} T_w` satisfies
     `t(T_w · e) = 0` for every basis element `T_w` when `z = q³/(q²+1)`. Measured exactly
     (`audibility_and_depth_exact_probe.py`): the determinant of the trace form is
     `−(z−q)⁵(qz+1)⁵(z(q²+1) − q³)(q³z+qz+1)/q⁸`, so at `z_D` the radical is exactly this line.
     A state is heard by the photons except for its component along `e`.

  -- Ref: [geckpfeiffer2000] Geck–Pfeiffer, Characters of finite Coxeter groups and Iwahori–Hecke algebras
-/
import QOU.StandardModel.HeckeH3Model
import Mathlib.Tactic.FieldSimp

namespace QOU.PhotonAudibility

open QOU.Mass.BorromeanPhotonFactorisation QOU.HeckeH3Model

section Abstract

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **Responses determine a state modulo the radical.** `P` is the set of photon products; if
its span is everything and the responses agree on `P`, the difference is in the radical. -/
theorem responses_determine_mod_radical (t : A →ₗ[R] R) (P : Set A)
    (hspan : Submodule.span R P = ⊤) {x x' : A} (hresp : ∀ y ∈ P, t (y * x) = t (y * x')) :
    ∀ y : A, t (y * (x - x')) = 0 := by
  intro y
  have hy : y ∈ Submodule.span R P := hspan ▸ Submodule.mem_top
  induction hy using Submodule.span_induction with
  | mem y hyP => rw [mul_sub, map_sub, hresp y hyP, sub_self]
  | zero => simp
  | add a b _ _ ha hb => rw [add_mul, map_add, ha, hb, add_zero]
  | smul c a _ ha => rw [smul_mul_assoc, map_smul, ha, smul_zero]

end Abstract

section Model

variable {K : Type*} [Field K]

/-- The Markov trace on the model, read from coordinates:
`t(T_w) = 1, z, z, z², z², (hz + 1)z` on `T_e, T_0, T_1, T_01, T_10, T_010`. -/
def trM (h z : K) (X : M6 K) : K :=
  coord X 0 + z * (coord X 1 + coord X 2) + z ^ 2 * (coord X 3 + coord X 4)
    + (h * z + 1) * z * coord X 5

/-- The sign direction `Σ_w (−q⁻¹)^{ℓ(w)} T_w`, as a coordinate vector. -/
def signVec (q : K) : Fin 6 → K := ![1, -q⁻¹, -q⁻¹, q⁻¹ ^ 2, q⁻¹ ^ 2, -(q⁻¹ ^ 3)]

/-- The six basis elements applied to a vector. -/
theorem basis_apply (h : K) (v : Fin 6 → K) :
    (heckeL0 h * heckeL1 h) v = heckeL0 h (heckeL1 h v) ∧
    (heckeL1 h * heckeL0 h) v = heckeL1 h (heckeL0 h v) ∧
    (heckeL0 h * heckeL1 h * heckeL0 h) v = heckeL0 h (heckeL1 h (heckeL0 h v)) :=
  ⟨rfl, rfl, rfl⟩

/-- **The sign direction is inaudible under convention D.** For `z = q³/(q²+1)` and every basis
element `b ∈ {1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}`, the response `t(b · e)` vanishes. -/
theorem sign_inaudible_D {q : K} (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    let h := q - q⁻¹
    let z := q ^ 3 / (q ^ 2 + 1)
    let tv := fun v : Fin 6 → K =>
      v 0 + z * (v 1 + v 2) + z ^ 2 * (v 3 + v 4) + (h * z + 1) * z * v 5
    tv (signVec q) = 0 ∧
    tv (heckeL0 h (signVec q)) = 0 ∧
    tv (heckeL1 h (signVec q)) = 0 ∧
    tv (heckeL0 h (heckeL1 h (signVec q))) = 0 ∧
    tv (heckeL1 h (heckeL0 h (signVec q))) = 0 ∧
    tv (heckeL0 h (heckeL1 h (heckeL0 h (signVec q)))) = 0 := by
  intro h z tv
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
  · simp only [tv, z, h, signVec, heckeL0_apply, heckeL1_apply, Matrix.cons_val_zero,
      Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val, Matrix.head_cons,
      Matrix.tail_cons, Fin.isValue]
    field_simp
    ring

end Model

end QOU.PhotonAudibility
