import BraidKnotOctonion.ColourStructureConstantCommutator

/-!
# `su(3)` structure constants: antisymmetry of `f`, symmetry of `d`, the Jacobi identity

Bean `qou-t3zb` (QFT-7, math-only core; epic `qou-3fjn`).

With `T^a = λ^a / 2` the Gell-Mann generators (`QOU.Braiding.ColourStructureConstantCommutator.gellMann`,
where `i` plays `√−1` and `r` plays `1/√3`), define

  `f^{abc} = −2i · tr([T^a, T^b] T^c)`,   `d^{abc} = 2 · tr({T^a, T^b} T^c)`.

## Main statements

* `trace_gellMann_mul` — orthonormality `tr(T^a T^b) = δ^{ab}/2`.
* `f_antisymm`, `f_cyclic` — `f` is totally antisymmetric (from trace cyclicity alone; this part
  holds for any three square matrices, `trace_comm_mul_cyclic`).
* `d_symm`, `d_cyclic` — `d` is totally symmetric.
* `expand_traceless` — **completeness**: every traceless `3 × 3` matrix is
  `X = 2 Σ_e tr(X T^e) T^e`. Derived from the Fierz identity `fierz`, already on main.
* `comm_gellMann_expand` — hence `[T^a, T^b] = i Σ_e f^{abe} T^e`.
* `jacobi_f` — the **Jacobi identity**
  `Σ_e (f^{abe} f^{ecd} + f^{bce} f^{ead} + f^{cae} f^{ebd}) = 0`, from the matrix Jacobi identity
  and completeness.

Base ring (§7c): a generic field of characteristic zero containing `i` (`i² = −1`) and `r`
(`r² = 1/3`), as in the Fierz file. No `ℂ` is fixed.

## Scope

Lie-algebra facts only. The Bern–Kosower gluon vertex and the Slavnov–Taylor identity, which this
bean named before its 2026-11-21 re-scope, are not formalised (they are statements about virtual
gluons). This file imports the colour-commutator file read-only and changes nothing in it.
-/

namespace QOU.QFTMath.Su3

open Matrix QOU.Braiding.ColourStructureConstantCommutator

section Generic

variable {n K : Type*} [Fintype n] [CommRing K]

/-- `tr([A,B] C)` is invariant under cyclic permutation of `A, B, C`. -/
theorem trace_comm_mul_cyclic (A B C : Matrix n n K) :
    trace ((A * B - B * A) * C) = trace ((B * C - C * B) * A) := by
  simp only [sub_mul, trace_sub]
  rw [trace_mul_cycle B C A, trace_mul_cycle B A C, trace_mul_cycle C B A]

/-- `tr({A,B} C)` is invariant under cyclic permutation of `A, B, C`. -/
theorem trace_anticomm_mul_cyclic (A B C : Matrix n n K) :
    trace ((A * B + B * A) * C) = trace ((B * C + C * B) * A) := by
  simp only [add_mul, trace_add]
  rw [trace_mul_cycle B C A, trace_mul_cycle B A C, trace_mul_cycle C B A]

/-- The matrix Jacobi identity. -/
theorem matrix_jacobi (A B C : Matrix n n K) :
    (A * B - B * A) * C - C * (A * B - B * A) + ((B * C - C * B) * A - A * (B * C - C * B))
      + ((C * A - A * C) * B - B * (C * A - A * C)) = 0 := by
  noncomm_ring

end Generic

variable {K : Type*} [Field K] (i r : K)

/-- The structure constants `f^{abc} = −2i tr([T^a,T^b] T^c)`. -/
def f (a b c : Fin 8) : K :=
  -2 * i * trace ((gellMann i r a * gellMann i r b - gellMann i r b * gellMann i r a) * gellMann i r c)

/-- The symmetric constants `d^{abc} = 2 tr({T^a,T^b} T^c)`. -/
def d (a b c : Fin 8) : K :=
  2 * trace ((gellMann i r a * gellMann i r b + gellMann i r b * gellMann i r a) * gellMann i r c)

theorem f_antisymm (a b c : Fin 8) : f i r a b c = - f i r b a c := by
  unfold f
  rw [show gellMann i r b * gellMann i r a - gellMann i r a * gellMann i r b
      = -(gellMann i r a * gellMann i r b - gellMann i r b * gellMann i r a) by abel,
    Matrix.neg_mul, trace_neg]; ring

theorem f_cyclic (a b c : Fin 8) : f i r a b c = f i r b c a := by
  unfold f; rw [trace_comm_mul_cyclic]

theorem d_symm (a b c : Fin 8) : d i r a b c = d i r b a c := by
  unfold d; rw [add_comm (gellMann i r a * gellMann i r b)]

theorem d_cyclic (a b c : Fin 8) : d i r a b c = d i r b c a := by
  unfold d; rw [trace_anticomm_mul_cyclic]

variable [CharZero K] (hi : i ^ 2 = -1) (hr : r ^ 2 = (3 : K)⁻¹)
include hi hr

set_option maxHeartbeats 2000000 in
/-- **Orthonormality** `tr(T^a T^b) = δ^{ab}/2`. -/
theorem trace_gellMann_mul (a b : Fin 8) :
    trace (gellMann i r a * gellMann i r b) = if a = b then (2 : K)⁻¹ else 0 := by
  fin_cases a <;> fin_cases b <;>
    simp [gellMann, trace, Fin.sum_univ_three] <;> ring_nf <;>
    simp only [hi, hr] <;> ring_nf

/-- **Completeness**: a traceless `3 × 3` matrix is `X = 2 Σ_e tr(X T^e) T^e`. -/
theorem expand_traceless (X : Matrix (Fin 3) (Fin 3) K) (htr : trace X = 0) :
    X = (2 : K) • ∑ e, trace (X * gellMann i r e) • gellMann i r e := by
  ext c d'
  have key : ∀ e, trace (X * gellMann i r e) * gellMann i r e c d'
      = ∑ a, ∑ b, X a b * (gellMann i r e b a * gellMann i r e c d') := by
    intro e
    simp only [trace, diag, Matrix.mul_apply, Finset.sum_mul]
    refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => by ring
  simp only [Matrix.smul_apply, Matrix.sum_apply, smul_eq_mul, key]
  rw [Finset.sum_comm]
  simp_rw [fun a => Finset.sum_comm (s := Finset.univ) (t := Finset.univ)
    (f := fun (e : Fin 8) (b : Fin 3) => X a b * (gellMann i r e b a * gellMann i r e c d'))]
  simp_rw [← Finset.mul_sum, fierz i r hi hr]
  have htr' : X 0 0 + X 1 1 + X 2 2 = 0 := by simpa [trace, Fin.sum_univ_three] using htr
  fin_cases c <;> fin_cases d' <;> simp [Fin.sum_univ_three] <;>
    first | ring1 | linear_combination (3 : K)⁻¹ * htr'

/-- **Commutator expansion** `[T^a, T^b] = i Σ_e f^{abe} T^e`. -/
theorem comm_gellMann_expand (a b : Fin 8) :
    gellMann i r a * gellMann i r b - gellMann i r b * gellMann i r a
      = ∑ e, (i * f i r a b e) • gellMann i r e := by
  have htr : trace (gellMann i r a * gellMann i r b - gellMann i r b * gellMann i r a) = 0 := by
    rw [trace_sub, trace_mul_comm, sub_self]
  conv_lhs => rw [expand_traceless i r hi hr _ htr]
  rw [Finset.smul_sum]
  refine Finset.sum_congr rfl fun e _ => ?_
  rw [smul_smul]; congr 1
  unfold f
  have : i * (-2 * i) = 2 := by linear_combination (-2 : K) * hi
  linear_combination (-(trace ((gellMann i r a * gellMann i r b - gellMann i r b * gellMann i r a)
    * gellMann i r e))) * this

/-- **Jacobi identity** for the structure constants:
`Σ_e (f^{abe} f^{ecd} + f^{bce} f^{ead} + f^{cae} f^{ebd}) = 0`. -/
theorem jacobi_f (a b c d' : Fin 8) :
    ∑ e, (f i r a b e * f i r e c d' + f i r b c e * f i r e a d' + f i r c a e * f i r e b d') = 0 := by
  set T := gellMann i r
  -- `−2i tr([[T^x,T^y],T^z] T^w) = i Σ_e f^{xye} f^{ezw}`
  have step : ∀ x y z, -2 * i * trace (((T x * T y - T y * T x) * T z - T z * (T x * T y - T y * T x))
      * T d') = i * ∑ e, f i r x y e * f i r e z d' := by
    intro x y z
    rw [comm_gellMann_expand i r hi hr x y, Finset.sum_mul, Finset.mul_sum, ← Finset.sum_sub_distrib,
      Finset.sum_mul, trace_sum, Finset.mul_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun e _ => ?_
    rw [smul_mul_assoc, mul_smul_comm, ← smul_sub, smul_mul_assoc, trace_smul, smul_eq_mul]
    unfold f; ring
  have hjac := congrArg (fun M => -2 * i * trace (M * T d')) (matrix_jacobi (T a) (T b) (T c))
  simp only [add_mul, trace_add, mul_add, zero_mul, trace_zero, mul_zero] at hjac
  rw [step a b c, step b c a, step c a b, ← mul_add, ← mul_add, ← Finset.sum_add_distrib,
    ← Finset.sum_add_distrib] at hjac
  have hi0 : i ≠ 0 := by
    rintro rfl; norm_num at hi
  exact (mul_eq_zero.mp hjac).resolve_left hi0

end QOU.QFTMath.Su3
