import QOU.Observations.LeptonWordsCatMap
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# Where `i` enters the mass pipeline: at `q = i` the pre-trace action is the cat-map group

Thread "Derive the muon mass relation" (2026-11-28). Owner: "If we have the mass in the ring, and
there is a group action before we take the trace, can we use that at all? … Track where the
imaginary part comes up." This file follows `i = √−1` through the N = 2 pipeline
(`def:mass-identity`: Hecke image on `V^{⊗3}`, then the quantum trace).

**Step 1. Before the trace.** The 2-dimensional (standard) Hecke block sends `σ₀ ↦ T₀`, `σ₁ ↦ T₁`, with
`T₀ = [[q, 1], [0, −q⁻¹]]` and `T₁ = [[−q⁻¹, 0], [1, q]]`. Both have eigenvalues `q` and `−q⁻¹`.
At `q = i` the two eigenvalues coincide (`−i⁻¹ = i`). After the framing normalisation `q⁻¹`
per crossing, the generators become the unipotent `A₀ = [[1, −i], [0, 1]]` and
`A₁ = [[1, 0], [−i, 1]]` (`stdBlock_at_i`).

* `conj_gen`, `conj_word`: conjugation by `P = diag(1, i)` turns `A` into the integer generators
  `genZ` of `B₃ → SL(2, ℤ)`, word by word. **So the `SL(2, ℤ)` (cat-map) action is the
  pre-trace Hecke block at `q = i`.**
* `conj_gen_neg`: the other root `−i`, with `P̄ = diag(1, −i)`, gives the same integer
  matrices. The integer image is blind to the choice of `√−1`. The choice sits in the
  conjugator, the same one bit as the `G_m` orientation (`Aut(G_m) = {±1}`, #9944).

**Step 2. The trace.** Every N = 2 ring mass carries the factor `q² + 1 = q·[2]_q`, the quantum
dimension, which vanishes at `q = i`. So all masses vanish there. Writing `m = (q² + 1)·J`, the
reduced masses `J` at `q = i` are
`J_e = −2`, `J_μ = 4`, `J_τ = −8` (`reduced_at_i`). Their absolute values are
`|2 − tr img(β)|`: the traces are 0, 6 and 10 (`LeptonWordsCatMap.traces`), and these values are
the link determinants of Hopf, T(2,4) and Whitehead (`reduced_eq_two_sub_trace`). Hence
`m_μ/m_e → −2` and `m_τ/m_μ → −2` at `q = i` (`ratio_at_i`): the ladder doubles.

What this does not do: it gives the ratios at `q = i`, not at `q₀`. It does not derive CAL-2.
The general statement that `J(i) = ±(2 − tr)` holds for every 3-braid is checked here only on
the three lepton words.
-/

namespace QOU.Observations.LeptonMassAtI

open QOU.Observations.LeptonChargeClassTrace QOU.Observations.LeptonWordsCatMap Matrix

section Conj

variable {A : Type*} [CommRing A] (i : A)

/-- The framing-normalised standard block at `q = i`. -/
def gA : Fin 2 → Bool → Matrix (Fin 2) (Fin 2) A
  | 0, true => !![1, -i; 0, 1]
  | 0, false => !![1, i; 0, 1]
  | 1, true => !![1, 0; -i, 1]
  | 1, false => !![1, 0; i, 1]

def imgA : List (Fin 2 × Bool) → Matrix (Fin 2) (Fin 2) A
  | [] => 1
  | (g, s) :: w => gA i g s * imgA w

/-- `P = diag(1, c)`. -/
def P (c : A) : Matrix (Fin 2) (Fin 2) A := !![1, 0; 0, c]

variable {i}

theorem P_mul_P (hi : i * i = -1) : P i * P (-i) = 1 := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [P, hi]

theorem P_mul_P' (hi : i * i = -1) : P (-i) * P i = 1 := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [P, hi]

/-- **Generator by generator:** `P⁻¹ Aₛ P = genZ`, with `P⁻¹ = diag(1, −i)`. -/
theorem conj_gen (hi : i * i = -1) (g : Fin 2) (s : Bool) :
    P (-i) * gA i g s * P i = (genZ g s).map (Int.castRingHom A) := by
  fin_cases g <;> cases s <;> ext a b <;> fin_cases a <;> fin_cases b <;>
    simp [P, gA, genZ, Matrix.mul_apply, Fin.sum_univ_two, hi]

/-- **Word by word:** the pre-trace block at `q = i` is conjugate to the `SL(2, ℤ)` image. -/
theorem conj_word (hi : i * i = -1) (w : List (Fin 2 × Bool)) :
    P (-i) * imgA i w * P i = (imgZ w).map (Int.castRingHom A) := by
  induction w with
  | nil => simp [imgA, imgZ, P_mul_P' hi, Matrix.map_one]
  | cons x w ih =>
    obtain ⟨g, s⟩ := x
    simp only [imgA, imgZ, Matrix.map_mul]
    rw [← conj_gen hi g s, ← ih]
    have h1 := P_mul_P hi
    calc P (-i) * (gA i g s * imgA i w) * P i
        = P (-i) * gA i g s * (P i * P (-i)) * imgA i w * P i := by
          rw [h1]; simp [Matrix.mul_assoc]
      _ = P (-i) * gA i g s * P i * (P (-i) * imgA i w * P i) := by
          simp [Matrix.mul_assoc]

/-- **The other square root gives the same integers.** With `j = −i` (so `j·j = −1`),
conjugation by `diag(1, j)` also lands on `genZ`. -/
theorem conj_gen_neg (hi : i * i = -1) (g : Fin 2) (s : Bool) :
    P i * gA (-i) g s * P (-i) = (genZ g s).map (Int.castRingHom A) := by
  have hj : (-i) * (-i) = -1 := by rw [neg_mul_neg]; exact hi
  simpa using conj_gen hj g s

end Conj

section Field

variable {F : Type*} [Field F]

/-- The standard Hecke block generators (eigenvalues `q`, `−q⁻¹`). -/
def T0 (q : F) : Matrix (Fin 2) (Fin 2) F := !![q, 1; 0, -q⁻¹]
def T1 (q : F) : Matrix (Fin 2) (Fin 2) F := !![-q⁻¹, 0; 1, q]

/-- The Hecke quadratic relation `(T − q)(T + q⁻¹) = 0`. -/
theorem T0_quadratic (q : F) :
    (T0 q - q • 1) * (T0 q + q⁻¹ • 1) = 0 := by
  ext a b; fin_cases a <;> fin_cases b <;>
    simp [T0, Matrix.mul_apply, Fin.sum_univ_two]

/-- The braid relation `T₀T₁T₀ = T₁T₀T₁`. -/
theorem T_braid {q : F} (hq : q ≠ 0) : T0 q * T1 q * T0 q = T1 q * T0 q * T1 q := by
  ext a b; fin_cases a <;> fin_cases b <;>
    simp [T0, T1, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- **At `q = i`** the normalised block `q⁻¹ T` is the unipotent `A`. -/
theorem stdBlock_at_i {i : F} (hi : i * i = -1) :
    i⁻¹ • T0 i = gA i 0 true ∧ i⁻¹ • T1 i = gA i 1 true := by
  have hi0 : i ≠ 0 := by
    intro h; rw [h, zero_mul] at hi; exact one_ne_zero (neg_eq_zero.mp hi.symm)
  have hinv : i⁻¹ = -i := by
    apply inv_eq_of_mul_eq_one_right; linear_combination -hi
  constructor <;> ext a b <;> fin_cases a <;> fin_cases b <;>
    simp [T0, T1, gA, hinv, hi]

/-- Reduced masses `J = m/(q² + 1)` (writhe-framed N = 2 trace, `def:mass-identity`). -/
def Je (q : F) : F := (q ^ 4 + 1) / q ^ 6
def Jmu (q : F) : F := (q ^ 8 + q ^ 4 - q ^ 2 + 1) / q ^ 12
def Jtau (q : F) : F := (q ^ 10 - q ^ 8 + 2 * q ^ 6 - q ^ 4 + 2 * q ^ 2 - 1) / q ^ 8

theorem reduced_at_i {i : F} (hi : i * i = -1) :
    Je i = -2 ∧ Jmu i = 4 ∧ Jtau i = -8 := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  have h4 : i ^ 4 = 1 := by rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, h2]; norm_num
  have h6 : i ^ 6 = -1 := by rw [show (6 : ℕ) = 4 + 2 from rfl, pow_add, h4, h2]; ring
  have h8 : i ^ 8 = 1 := by rw [show (8 : ℕ) = 4 * 2 from rfl, pow_mul, h4]; norm_num
  have h10 : i ^ 10 = -1 := by rw [show (10 : ℕ) = 8 + 2 from rfl, pow_add, h8, h2]; ring
  have h12 : i ^ 12 = 1 := by rw [show (12 : ℕ) = 4 * 3 from rfl, pow_mul, h4]; norm_num
  refine ⟨?_, ?_, ?_⟩ <;> simp only [Je, Jmu, Jtau, h2, h4, h6, h8, h10, h12] <;> norm_num

/-- `|J(i)| = |2 − tr img(β)|` on the three lepton words (traces 0, 6, 10). -/
theorem reduced_eq_two_sub_trace {i : F} (hi : i * i = -1) :
    Je i = -(2 - ((Matrix.trace (imgZ wE) : ℤ) : F)) ∧
    Jmu i = -(2 - ((Matrix.trace (imgZ wMu) : ℤ) : F)) ∧
    Jtau i = (2 - ((Matrix.trace (imgZ wTau) : ℤ) : F)) := by
  obtain ⟨h1, h2, h3⟩ := reduced_at_i hi
  obtain ⟨t1, t2, t3, -⟩ := traces
  rw [h1, h2, h3, t1, t2, t3]; norm_num

/-- **The ladder doubles at `q = i`:** `J_μ/J_e = −2` and `J_τ/J_μ = −2`
(`char F ≠ 2`). -/
theorem ratio_at_i [CharZero F] {i : F} (hi : i * i = -1) :
    Jmu i / Je i = -2 ∧ Jtau i / Jmu i = -2 := by
  obtain ⟨h1, h2, h3⟩ := reduced_at_i hi
  rw [h1, h2, h3]; constructor <;> norm_num

end Field

end QOU.Observations.LeptonMassAtI
