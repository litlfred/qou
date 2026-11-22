import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Algebra.Group.Commute.Units
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Tactic.LinearCombination

/-!
# What the colour-singlet reduction does to braid words (working assumption, issue #9106)

On the colour-singlet sector the tensor braiding is `X = c·b` with `c = −q⁻¹` a central scalar and
`b` the flavour Hecke generator (`HopfColourTensorBraid.singlet_hecke`,
`JimboGl3Singlet.R12_eps`). This file proves, with no numerical input:

* `word_eval_smul`: a braid word evaluated on the generators `c·bᵢ` equals `c^{e}` times the same
  word on the `bᵢ`, where `e` is the word's exponent sum (positive minus negative crossings).
  So every Markov-trace value of a word with `e = 0` is unchanged by colour, and a word with
  `e ≠ 0` gains the factor `(−q⁻¹)^{e}` (`trace_word_smul`).
* `coideal_mul_tensor`: the gl₆-coideal singlet generator `s = −b⁻¹` (the `#`-twist, see
  `ColourSingletSignTwist`) and the tensor-route singlet generator `X = −q⁻¹·b` satisfy
  `s·X = q⁻¹`. The two colour routes agree on the singlet sector up to inversion and the scalar
  `q⁻¹`: that is the precise sense of "convention D up to the mirror".
-/

namespace QOU.Braiding.ColourSingletDownstream

/-- A braid word: a list of (generator index, sign), `true` = positive crossing. -/
abbrev Word (n : ℕ) := List (Fin n × Bool)

/-- Exponent sum of a word. -/
def expSum {n : ℕ} : Word n → ℤ
  | [] => 0
  | (_, true) :: w => 1 + expSum w
  | (_, false) :: w => -1 + expSum w

variable {M : Type*} [Monoid M]

/-- Evaluate a word on generators `g i` in the unit group. -/
def eval {n : ℕ} (g : Fin n → Mˣ) : Word n → Mˣ
  | [] => 1
  | (i, true) :: w => g i * eval g w
  | (i, false) :: w => (g i)⁻¹ * eval g w

/-- **Exponent-sum scaling.** If `c` is central, replacing every generator `g i` by `c·g i`
multiplies the value of a word by `c^{e}`, `e` its exponent sum. -/
theorem word_eval_smul {n : ℕ} (g : Fin n → Mˣ) (c : Mˣ) (hc : ∀ x : Mˣ, Commute c x)
    (w : Word n) : eval (fun i => c * g i) w = c ^ expSum w * eval g w := by
  induction w with
  | nil => simp [eval, expSum]
  | cons p w ih =>
    obtain ⟨i, s⟩ := p
    cases s with
    | true =>
      simp only [eval, expSum, ih]
      rw [zpow_add, zpow_one]
      have h2 : Commute (c ^ expSum w) (g i) := (hc (g i)).zpow_left _
      calc c * g i * (c ^ expSum w * eval g w)
          = c * (g i * c ^ expSum w) * eval g w := by simp only [mul_assoc]
        _ = c * (c ^ expSum w * g i) * eval g w := by rw [h2.eq]
        _ = c * c ^ expSum w * (g i * eval g w) := by simp only [mul_assoc]
    | false =>
      simp only [eval, expSum, ih]
      rw [zpow_add, zpow_neg, zpow_one, mul_inv_rev]
      have h2 : Commute (c ^ expSum w) (g i)⁻¹ := ((hc (g i)).inv_right).zpow_left _
      have h3 : Commute c⁻¹ (g i)⁻¹ := ((hc (g i)).inv_right).inv_left
      calc (g i)⁻¹ * c⁻¹ * (c ^ expSum w * eval g w)
          = c⁻¹ * (g i)⁻¹ * (c ^ expSum w * eval g w) := by rw [h3.eq]
        _ = c⁻¹ * ((g i)⁻¹ * c ^ expSum w) * eval g w := by simp only [mul_assoc]
        _ = c⁻¹ * (c ^ expSum w * (g i)⁻¹) * eval g w := by rw [h2.eq]
        _ = c⁻¹ * c ^ expSum w * ((g i)⁻¹ * eval g w) := by simp only [mul_assoc]

/-- **Traces pick up the exponent-sum factor.** For a `K`-algebra `A`, a `K`-linear trace
`τ : A →ₗ[K] K`, a scalar unit `c` of `K` and generators `g i` in `Aˣ`: the trace of a word on the
generators `c·g i` is `c^{e}` times the trace of the same word on the `g i`. -/
theorem trace_word_smul {K A : Type*} [Field K] [Ring A] [Algebra K A] {n : ℕ}
    (τ : A →ₗ[K] K) (g : Fin n → Aˣ) (c : Kˣ) (w : Word n) :
    τ (eval (fun i => Units.map (algebraMap K A).toMonoidHom c * g i) w : Aˣ)
      = (c : K) ^ expSum w * τ (eval g w : Aˣ) := by
  have hc : ∀ x : Aˣ, Commute (Units.map (algebraMap K A).toMonoidHom c) x := by
    intro x
    apply Units.ext
    simp [Algebra.commutes]
  rw [word_eval_smul g _ hc w]
  have : ((Units.map (algebraMap K A).toMonoidHom c ^ expSum w : Aˣ) : A)
      = algebraMap K A ((c : K) ^ expSum w) := by
    rw [← map_zpow (Units.map (algebraMap K A).toMonoidHom) c (expSum w), Units.coe_map,
      Units.val_zpow_eq_zpow_val]
    rfl
  rw [Units.val_mul, this, ← Algebra.smul_def, map_smul, smul_eq_mul]

/-- **Coideal versus tensor on the singlet.** With `b` Hecke at `q` (`q·qi = 1`), its inverse is
`b − (q − qi)`. The coideal singlet generator `s = −b⁻¹` and the tensor singlet generator
`X = −qi·b` satisfy `s·X = qi`. -/
theorem coideal_mul_tensor {K : Type*} [CommRing K] (q qi b : K) (hqi : q * qi = 1)
    (hb : (b - q) * (b + qi) = 0) : (-(b - (q - qi))) * (-qi * b) = qi := by
  linear_combination qi * hb + qi * hqi

/-- The Hecke inverse: `b·(b − (q − qi)) = 1`. -/
theorem hecke_inv {K : Type*} [CommRing K] (q qi b : K) (hqi : q * qi = 1)
    (hb : (b - q) * (b + qi) = 0) : b * (b - (q - qi)) = 1 := by
  linear_combination hb + hqi

end QOU.Braiding.ColourSingletDownstream
