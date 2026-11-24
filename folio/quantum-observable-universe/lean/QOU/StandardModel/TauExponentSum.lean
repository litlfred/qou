import Mathlib.Tactic

/-!
# The `(1, 0, −1)` functional depends only on the exponent sum

`τ = χ_(3) − χ_(1³)` on `H₃(q)` (the weights the α_em linchpin needs) reads only
the trivial and sign blocks, where `σᵢ^{±1}` acts by `q^{±1}` and `(−q⁻¹)^{±1}`.
So `τ(w) = q^e − (−q⁻¹)^e` with `e` the exponent sum of `w` (the writhe of the
closure), and under `q ↦ q⁻¹` it is even for odd `e`, odd for even `e`.

Electron `σ₀σ₁σ₀`: `e = 3`, `τ = q³ + q⁻³`. Linchpin `(σ₁σ₂)⁵`: `e = 10`,
`τ = q¹⁰ − q⁻¹⁰`. Pure algebra over a generic field; no evaluation at `q₀`.
-/

namespace QOU.AlphaEM.TauExp

variable {K : Type*} [Field K]

abbrev Letter := Fin 2 × Bool

def sign (l : Letter) : ℤ := if l.2 then 1 else -1
def expSum (w : List Letter) : ℤ := (w.map sign).sum

def symLetter (q : K) : Letter → K
  | (_, true) => q
  | (_, false) => q⁻¹
def altLetter (q : K) : Letter → K
  | (_, true) => -q⁻¹
  | (_, false) => -q
def symWord (q : K) (w : List Letter) : K := (w.map (symLetter q)).prod
def altWord (q : K) (w : List Letter) : K := (w.map (altLetter q)).prod

theorem symWord_eq (q : K) (hq : q ≠ 0) (w : List Letter) :
    symWord q w = q ^ expSum w := by
  induction w with
  | nil => simp [symWord, expSum]
  | cons l w ih =>
    simp only [symWord, expSum, List.map_cons, List.prod_cons, List.sum_cons] at *
    rw [ih, zpow_add₀ hq]
    obtain ⟨_, b⟩ := l; cases b <;> simp [symLetter, sign]

theorem altWord_eq (q : K) (hq : q ≠ 0) (w : List Letter) :
    altWord q w = (-q⁻¹) ^ expSum w := by
  have hq' : (-q⁻¹) ≠ 0 := neg_ne_zero.2 (inv_ne_zero hq)
  induction w with
  | nil => simp [altWord, expSum]
  | cons l w ih =>
    simp only [altWord, expSum, List.map_cons, List.prod_cons, List.sum_cons] at *
    rw [ih, zpow_add₀ hq']
    obtain ⟨_, b⟩ := l; cases b <;> simp [altLetter, sign, inv_neg]

/-- **The `(1,0,−1)` functional depends only on the exponent sum `e`:
    `τ(w) = q^e − (−q⁻¹)^e`.** -/
theorem tau_eq (q : K) (hq : q ≠ 0) (w : List Letter) :
    symWord q w - altWord q w = q ^ expSum w - (-q⁻¹) ^ expSum w := by
  rw [symWord_eq q hq, altWord_eq q hq]

/-- Bar parity: under `q ↦ q⁻¹`, `τ` is even for odd `e` and odd for even `e`. -/
theorem tau_bar (q : K) (e : ℤ) :
    (q⁻¹) ^ e - (-(q⁻¹)⁻¹) ^ e = -((-1 : K) ^ e) * (q ^ e - (-q⁻¹) ^ e) := by
  have h1 : ((-1 : K) ^ e) * (-1) ^ e = 1 := by
    rw [← mul_zpow]; norm_num
  rw [inv_inv, show (-q) = (-1) * q by ring, show (-q⁻¹) = (-1) * q⁻¹ by ring,
    mul_zpow, mul_zpow]
  linear_combination (-(q⁻¹ ^ e)) * h1

end QOU.AlphaEM.TauExp
