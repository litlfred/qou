/-
The bare Borromean braid gives no vertex split on the weight spaces (prereg Addendum 19, D1;
audit §31).

On the weight-zero space of `V^{⊗4}` (basis `uudd, udud, uddu, duud, dudu, dduu`, indices
0–5, generators from `H4VertexEnergy`), the nucleon braid `β_Bor = (σ₁σ₂⁻¹)³` acts on the
three quark strands and the lepton strand is a spectator. The initial states (one `u` quark,
lepton `u`) are indices 2, 4, 5; the final states (two `u` quarks, lepton `d`) are 0, 1, 3.

`bbor_diag_split_eq` proves that the diagonal of `β_Bor ⊗ 1` sums to the same value on the
two sets, for every `q` with `q² = h q + 1`. So candidate D1 of Addendum 19 gives the ratio 1
and vertex energy 0 identically, not only at `q = 1`.

No empirical number enters any statement.
-/
import MathlibExt.H4VertexEnergy

namespace QOU.QBeta.BBorWeightTrace

open Matrix QOU.QBeta.H4VertexEnergy

variable {R : Type*} [Field R]

def s2i (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![-h, 1, 0, 0, 0, 0;
     1, 0, 0, 0, 0, 0;
     0, 0, -h + q, 0, 0, 0;
     0, 0, 0, -h + q, 0, 0;
     0, 0, 0, 0, -h, 1;
     0, 0, 0, 0, 1, 0]
def ma (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![-h*q, q, 0, 0, 0, 0;
     0, 0, 0, -h + q, 0, 0;
     0, 0, 0, 0, -h, 1;
     1, 0, 0, -h^2 + h*q, 0, 0;
     0, 0, -h + q, 0, -h^2, h;
     0, 0, 0, 0, q, 0]
def ma2 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![h^2*q^2, -h*q^2, 0, -h*q + q^2, 0, 0;
     -h + q, 0, 0, h^3 - 2*h^2*q + h*q^2, 0, 0;
     0, 0, h^2 - h*q, 0, h^3 + q, -h^2;
     -h^2, q, 0, h^4 - 2*h^3*q + h^2*q^2, 0, 0;
     0, 0, h^3 - h^2*q, 0, h^4 + h^2, -h^3 - h + q;
     0, 0, -h*q + q^2, 0, -h^2*q, h*q]

variable (q h : R)

/-- `σ₂ · s2i = 1` given the Hecke relation, so `s2i` is `σ₂⁻¹`. -/
theorem s2_mul_s2i (hH : q ^ 2 = h * q + 1) : s2 q h * s2i q h = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s2, s2i, Matrix.mul_apply, Fin.sum_univ_succ] <;>
    first | ring1 | linear_combination hH

theorem s1_mul_s2i : s1 q h * s2i q h = ma q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s1, s2i, ma, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring1

theorem ma_sq : ma q h * ma q h = ma2 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [ma, ma2, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring1

/-- `β_Bor = (σ₁σ₂⁻¹)³` on the quark strands. -/
def bBor : Matrix (Fin 6) (Fin 6) R := ma2 q h * ma q h

theorem bBor_eq : (s1 q h * s2i q h) * (s1 q h * s2i q h) * (s1 q h * s2i q h) = bBor q h := by
  rw [s1_mul_s2i, ma_sq]; rfl

/-- The diagonal of `β_Bor ⊗ 1` sums to the same value on the initial and final sets. -/
theorem bbor_diag_split_eq (hH : q ^ 2 = h * q + 1) :
    bBor q h 2 2 + bBor q h 4 4 + bBor q h 5 5 = bBor q h 0 0 + bBor q h 1 1 + bBor q h 3 3 := by
  simp [bBor, ma, ma2, Matrix.mul_apply, Fin.sum_univ_succ]
  linear_combination (3 * h ^ 4) * hH

end QOU.QBeta.BBorWeightTrace
