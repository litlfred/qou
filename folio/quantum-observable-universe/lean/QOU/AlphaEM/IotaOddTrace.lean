import Mathlib.Tactic

/-!
# The `(1, 0, −1)` weights are forced by the involution `σ ↦ −σ⁻¹`

`ι : σᵢ ↦ −σᵢ⁻¹` is an involution of the Hecke algebra `H₃(q)` (it respects
`(σ − q)(σ + q⁻¹) = 0` and the braid relation). It swaps the trivial block
`σ ↦ q` with the sign block `σ ↦ −q⁻¹`, and maps the 2-dimensional hook
representation to an equivalent one.

Words in `σᵢ^{±1}` are lists of letters `(i, b)` (`b = true` for `σᵢ`,
`false` for `σᵢ⁻¹`); `ι` sends `(i, b)` to `(i, !b)` with a factor `−1`.
For weights `w = (w₃, w₂₁, w₁₁₁)` on the three blocks,

`iota_odd_iff`: `τ_w(ι x) = −τ_w(x)` for every word `x` **iff**
`w₂₁ = 0` and `w₁₁₁ = −w₃`.

So the weights the α_em linchpin needs (`t35_weights_unique`) are exactly
the `ι`-odd block functionals. The overall scale `w₃` is not fixed by this.
-/

namespace QOU.AlphaEM.IotaOdd

open Matrix

variable {K : Type*} [Field K]

/-- A letter: generator index and sign (`true` = `σᵢ`, `false` = `σᵢ⁻¹`). -/
abbrev Letter := Fin 2 × Bool

/-- Hook representation on the generators (as in `T35TenLinchpinFromH3`). -/
def hookGen (q : K) : Fin 2 → Matrix (Fin 2) (Fin 2) K
  | 0 => !![q, 1; 0, -q⁻¹]
  | 1 => !![-q⁻¹, 0; 1, q]

/-- Hook inverse, `σ⁻¹ = σ − (q − q⁻¹)` by the Hecke relation. -/
def hookGenInv (q : K) : Fin 2 → Matrix (Fin 2) (Fin 2) K
  | 0 => !![q⁻¹, 1; 0, -q]
  | 1 => !![-q, 0; 1, q⁻¹]

theorem hookGen_mul_inv (q : K) (hq : q ≠ 0) (i : Fin 2) :
    hookGen q i * hookGenInv q i = 1 := by
  fin_cases i <;>
  · ext a b; fin_cases a <;> fin_cases b <;>
      simp [hookGen, hookGenInv, Matrix.mul_apply, Fin.sum_univ_two] <;>
      field_simp

def hookLetter (q : K) : Letter → Matrix (Fin 2) (Fin 2) K
  | (i, true) => hookGen q i
  | (i, false) => hookGenInv q i

/-- `ι` on a letter: flip the sign, times `−1`. -/
def iotaHook (q : K) : Letter → Matrix (Fin 2) (Fin 2) K
  | (i, true) => -hookGenInv q i
  | (i, false) => -hookGen q i

def symLetter (q : K) : Letter → K
  | (_, true) => q
  | (_, false) => q⁻¹

def altLetter (q : K) : Letter → K
  | (_, true) => -q⁻¹
  | (_, false) => -q

def hookWord (q : K) (w : List Letter) : Matrix (Fin 2) (Fin 2) K :=
  (w.map (hookLetter q)).prod
def iotaHookWord (q : K) (w : List Letter) : Matrix (Fin 2) (Fin 2) K :=
  (w.map (iotaHook q)).prod
def symWord (q : K) (w : List Letter) : K := (w.map (symLetter q)).prod
def altWord (q : K) (w : List Letter) : K := (w.map (altLetter q)).prod

/-- The intertwiner between the hook representation and its `ι`-twist. -/
def P (q : K) : Matrix (Fin 2) (Fin 2) K :=
  !![-1, -((q ^ 2 + 1) / q); (q ^ 2 + 1) / q, 1]

theorem P_letter (q : K) (hq : q ≠ 0) (l : Letter) :
    P q * hookLetter q l = iotaHook q l * P q := by
  obtain ⟨i, b⟩ := l
  fin_cases i <;> cases b <;>
  · ext a c; fin_cases a <;> fin_cases c <;>
      simp [P, hookLetter, iotaHook, hookGen, hookGenInv, Matrix.mul_apply,
        Fin.sum_univ_two] <;>
      field_simp <;> ring

theorem P_word (q : K) (hq : q ≠ 0) (w : List Letter) :
    P q * hookWord q w = iotaHookWord q w * P q := by
  induction w with
  | nil => simp [hookWord, iotaHookWord]
  | cons l w ih =>
    simp only [hookWord, iotaHookWord, List.map_cons, List.prod_cons] at *
    rw [← Matrix.mul_assoc, P_letter q hq l, Matrix.mul_assoc, ih, Matrix.mul_assoc]

theorem det_P (q : K) (hq : q ≠ 0) :
    (P q).det = (q ^ 2 + 1 + (q ^ 2)⁻¹) := by
  simp [P, Matrix.det_fin_two_of]; field_simp; ring

/-- The `ι`-twisted hook has the same character on every word. -/
theorem trace_iota_hook (q : K) (hq : q ≠ 0) (h3 : q ^ 2 + 1 + (q ^ 2)⁻¹ ≠ 0)
    (w : List Letter) : (iotaHookWord q w).trace = (hookWord q w).trace := by
  have hu : IsUnit (P q).det := by rw [det_P q hq]; exact isUnit_iff_ne_zero.2 h3
  have e : iotaHookWord q w = P q * hookWord q w * (P q)⁻¹ := by
    rw [P_word q hq, Matrix.mul_assoc, Matrix.mul_nonsing_inv _ hu, Matrix.mul_one]
  rw [e, Matrix.trace_mul_cycle, Matrix.nonsing_inv_mul _ hu, Matrix.one_mul]

/-- Block functional with weights `(w₃, w₂₁, w₁₁₁)`. -/
def tau (q w3 w21 w111 : K) (w : List Letter) : K :=
  w3 * symWord q w + w21 * (hookWord q w).trace + w111 * altWord q w

/-- `τ` on the `ι`-image of a word: the 1-dim blocks swap, the hook is kept
    up to the intertwiner `P`. -/
def tauIota (q w3 w21 w111 : K) (w : List Letter) : K :=
  w3 * altWord q w + w21 * (iotaHookWord q w).trace + w111 * symWord q w

/-- **The `(1,0,−1)` weights are exactly the `ι`-odd block functionals.** -/
theorem iota_odd_iff [CharZero K] (q w3 w21 w111 : K) (hq : q ≠ 0)
    (h3 : q ^ 2 + 1 + (q ^ 2)⁻¹ ≠ 0) :
    (∀ w, tauIota q w3 w21 w111 w = -tau q w3 w21 w111 w) ↔
      (w21 = 0 ∧ w111 = -w3) := by
  constructor
  · intro h
    have e0 := h []
    have e2 := h [(0, true), (1, true)]
    simp [tau, tauIota, symWord, altWord, hookWord, iotaHookWord, hookLetter,
      iotaHook, symLetter, altLetter, hookGen, hookGenInv, Matrix.trace_fin_two,
      mul_inv_cancel₀ hq, inv_mul_cancel₀ hq] at e0 e2
    have h2 : (2 : K) ≠ 0 := two_ne_zero
    have hA : w3 + w111 + 2 * w21 = 0 := by
      apply mul_left_cancel₀ h2; linear_combination e0
    have hw : w21 * (q ^ 2 + 1 + (q ^ 2)⁻¹) = 0 := by
      apply mul_left_cancel₀ h2
      linear_combination -e2 + (q ^ 2 + (q ^ 2)⁻¹) * hA
    have h21 : w21 = 0 := (mul_eq_zero.1 hw).resolve_right h3
    exact ⟨h21, by linear_combination hA - 2 * h21⟩
  · rintro ⟨h21, h111⟩ w
    simp only [tau, tauIota, h21, h111, trace_iota_hook q hq h3]
    ring

end QOU.AlphaEM.IotaOdd
