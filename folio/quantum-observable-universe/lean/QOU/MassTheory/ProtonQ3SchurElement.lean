/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import QOU.MassTheory.PoincareCenteringOfQ3
import Mathlib.Analysis.Calculus.Deriv.Mul

/-!
# The proton's `/q³`: it is the Schur element of the sign character of `H₃`

Thread "Justify the proton's /q³ normalisation" (2026-11-21). Follows
`QOU.MassTheory.PoincareCentering` (bean `qou-24w9`), which showed that the
factor in

    F_Bor(q) = |tr_M(β_Bor, q)| · [3]_q! / q³

is `P(q⁻¹)`, the Poincaré polynomial of `S₃` at the inverse variable, that the
writhe prefactor is `1` on `β_Bor`, and that `/q³` is the only bar-asymmetric step.

This file asks the coordinator's four questions in turn and answers them with
theorems. No measured value enters any statement; `q` is a variable throughout.

## 1. What `[3]_q!/q³` is: the Schur element of the sign character

Take `H₃(q)` with `(T − q)(T + q⁻¹) = 0` (the corpus's relation) and its
canonical symmetrising trace `τ(σ_w) = δ_{w,1}`, where `σ_w` is the positive
braid lift of `w ∈ S₃` (§7a: the Hecke generator is written `σ`). It splits over the three
irreducible characters, `τ = Σ_χ χ / c_χ`, and the `c_χ` are the **Schur
elements**. With the character values on `1, σ₁, σ₁σ₂`

| χ        | `1` | `σ₁`      | `σ₁σ₂` |
|----------|-----|------------|------------|
| trivial  | 1   | `q`        | `q²`       |
| sign     | 1   | `−q⁻¹`     | `q⁻²`      |
| reflection | 2 | `q − q⁻¹`  | `−1`       |

the three conditions `τ(1) = 1, τ(σ₁) = 0, τ(σ₁σ₂) = 0` have exactly one
solution (`schur_inverse_unique`, no hypothesis beyond `q ≠ 0`):

    c_triv = P(q) = q³·[3]_q!,   c_sign = P(q⁻¹) = [3]_q!/q³,   c_refl = [3]_q.

So **the factor in `F_Bor` is `c_sign`** (`fBor_normaliser_eq_schurSign`). It is
also the constant in `x₋² = c_sign · x₋` for the unnormalised antisymmetriser
`x₋ = Σ_w (−q)^{−ℓ(w)} σ_w`; the corpus's `H3.blockAlt3` is `x₋ / P(q⁻¹)`.

## 2. Which normalisations are admissible

Among the normalisers `q^k · [3]_q!` (every one equals `6 = |S₃|` at `q = 1`, so
the classical limit does not fix `k`):

* it is a Schur element of a linear character iff `k = 3` (trivial) or `k = −3`
  (sign) — `qpow_fact_eq_schurTriv_iff`, `qpow_fact_eq_schurSign_iff`;
* it is bar-symmetric iff `k = 0` — `qpow_fact_bar_symmetric_iff`.

So there are three principled choices, `k ∈ {3, 0, −3}`, and the code uses
`k = −3`. For `q > 1` they are strictly ordered,
`c_sign < [3]_q! < c_triv` (`schurSign_lt_balanced`, `balanced_lt_schurTriv`).
The reflection Schur element `[3]_q` is not of this form; it coincides with
`c_sign` only at `q⁴ = q² + 1` (`schurSign_eq_schurRefl_iff`).

The mirror ratio `F_Bor(q⁻¹) = q⁶·F_Bor(q)` of `qou-24w9` is
`c_triv / c_sign = q⁶` (`schurTriv_div_schurSign`), the generic degree of the
sign character.

## 3. The routes that do not give `q⁻³`

* **Convention-D Markov normalisation.** With `z_D = q³/(q²+1)`,
  `tr(σ⁻¹) = w_D = 1/(q³ + q)` (`wD_eq`), so `z_D·w_D = [2]_q⁻²` and
  `z_D/w_D = q⁴` (`zD_mul_wD`, `zD_div_wD`). The link normaliser of a 3-strand
  closure of writhe `e` is `(z_D w_D)^{−1}·(w_D/z_D)^{e/2}`; at `e = 0` it is
  `[2]_q²`, which is bar-symmetric and never equals `q⁻³` for `q > 1`
  (`markov_normaliser_ne_inv_cube`). The `q³` inside `z_D` does not survive.
* **Markov stabilisation.** `β_Bor` has 3 strands and braid index 3; there is no
  stabilisation to undo, and each one would contribute `[2]_q`, not a power of `q`.
* **Writhe and framing.** The ruled word `V³ = (σ₀σ₁⁻¹)³` has writhe 0
  (`v3_writhe_zero`) and is a pure braid (`v3_pure`), so each of its three
  closure components is one strand and has blackboard framing 0. The ribbon twist
  of the convention-D fundamental satisfies `θ² = q³` (`twist_sq_eq_q_cube`), so
  `q⁻³ = θ⁻²` would need total framing `−2`. Under the `ℤ/3` symmetry that
  permutes the three components, equal integer framings give a total `3f`, and
  `3f = ±2` has no solution (`no_symmetric_framing_total_two`).
* **Word length.** `q^{−ℓ/2}` with `ℓ(V³) = 6` does give `q⁻³`, but word length
  is not a braid invariant: `σ₀σ₀⁻¹ = 1` has length 2 (`length_not_invariant`).
  This is the Hecke→Reshetikhin–Turaev rescaling `σ ↦ q^{−1/2}σ` applied as if
  every crossing were positive; done correctly it gives `q^{−e/2} = 1`.
* **Quantum dimension.** The relevant quantum dimensions are `[2]_q` (strand),
  `[3]_q` (reflection Schur element), and the generic degrees
  `1, q⁶, q³[2]_q`. None is `q⁻³·[3]_q!` except through `c_sign` itself.

## The tension, and one candidate that resolves it (end of file)

Convention D gives the sign block weight `y_{(1³)} = 0`, yet the normaliser is
that block's Schur element. Frame-independently, the code's rule is "the Schur
element of the linear block the trace kills" (`trXMinus_zD`,
`trXPlus_zD_relabel`, `schurSign_relabel`). And `−∂_z tr_z(x₋)` at `z_D` is
exactly `q⁻³` (`hasDerivAt_trXMinus_zD`), the derivative-type modified trace of
the killed block. That is a candidate derivation of the `q⁻³` alone, conditional
on `z` being the right coordinate.

## Verdict

`/q³` is **identified, not derived**. It has a canonical name, the Schur element
of the sign character of `H₃`, and it is one of exactly three principled
`S₃`-normalisers. Choosing the sign character over the trivial one (or the
bar-symmetric middle) is a choice the axioms do not make. It sits in tension with
convention D itself, which gives the sign block weight `y_{(1³)} = 0`.

Scope (a): this does not refute `F_Bor`, and it does not touch the Lean-proved
`|tr_M(β_Bor)|`.
-/

namespace QOU.MassTheory.ProtonQ3Schur

open QOU.MassTheory.PoincareCentering

section Schur

variable {K : Type*} [Field K]

/-- Schur element of the trivial character, `P(q)`. -/
def schurTriv (q : K) : K := poincareS3 q

/-- Schur element of the sign character, `P(q⁻¹)`. -/
def schurSign (q : K) : K := poincareS3 q⁻¹

/-- Schur element of the 2-dimensional reflection character, the balanced `[3]_q`. -/
def schurRefl (q : K) : K := q ^ 2 + 1 + q⁻¹ ^ 2

/-- `τ = a·χ_triv + b·χ_sign + c·χ_refl` satisfies `τ(1) = 1`, `τ(σ₁) = 0` and
`τ(σ₁σ₂) = 0`. Here `a, b, c` are the inverse Schur elements. -/
structure IsSchurInverse (q a b c : K) : Prop where
  at_one : a + b + 2 * c = 1
  at_s : q * a - q⁻¹ * b + (q - q⁻¹) * c = 0
  at_s1s2 : q ^ 2 * a + q⁻¹ ^ 2 * b - c = 0

/-- **Uniqueness of the Schur elements.** Any solution of the three trace
conditions satisfies `a·P(q) = 1`, `b·P(q⁻¹) = 1` and `c·[3]_q = 1`. -/
theorem schur_inverse_unique {q a b c : K} (hq : q ≠ 0)
    (h : IsSchurInverse q a b c) :
    a * schurTriv q = 1 ∧ b * schurSign q = 1 ∧ c * schurRefl q = 1 := by
  have hq' : q * q⁻¹ - 1 = 0 := by rw [mul_inv_cancel₀ hq]; ring
  have E2 : q ^ 2 * a - b + (q ^ 2 - 1) * c = 0 := by
    linear_combination q * h.at_s + (b + c) * hq'
  have E3 : q ^ 4 * a + b - q ^ 2 * c = 0 := by
    linear_combination q ^ 2 * h.at_s1s2 - b * (q * q⁻¹ + 1) * hq'
  have E1 := h.at_one
  have ha : a * (1 + 2 * q ^ 2 + 2 * q ^ 4 + q ^ 6) = 1 := by
    linear_combination E1 + (q ^ 2 + 2) * E2 + (q ^ 2 + 1) * E3
  have hb : b * (q ^ 6 + 2 * q ^ 4 + 2 * q ^ 2 + 1) = q ^ 6 := by
    linear_combination q ^ 6 * E1 - q ^ 2 * (2 * q ^ 2 + 1) * E2 + (q ^ 2 + 1) * E3
  have hc : c * (q ^ 4 + q ^ 2 + 1) = q ^ 2 := by
    linear_combination q ^ 2 * E1 + (q ^ 2 - 1) * E2 - E3
  refine ⟨?_, ?_, ?_⟩
  · unfold schurTriv poincareS3; linear_combination ha
  · unfold schurSign poincareS3
    have hq6 : q ^ 6 ≠ 0 := pow_ne_zero 6 hq
    field_simp
    linear_combination hb
  · unfold schurRefl
    have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
    field_simp
    linear_combination hc

/-- **The factor in `F_Bor` is the sign Schur element.** -/
theorem fBor_normaliser_eq_schurSign (q : K) (hq : q ≠ 0) :
    qFactThreeBalanced q / q ^ 3 = schurSign q :=
  code_form_eq_poincare_bar q hq

/-- The trivial Schur element is `q³·[3]_q!`. -/
theorem schurTriv_eq (q : K) (hq : q ≠ 0) :
    schurTriv q = q ^ 3 * qFactThreeBalanced q := by
  rw [balanced_is_already_centered q hq]
  unfold schurTriv
  field_simp

/-- The balanced `[3]_q!` is the geometric mean of the two linear Schur elements. -/
theorem schurTriv_mul_schurSign (q : K) (hq : q ≠ 0) :
    schurTriv q * schurSign q = qFactThreeBalanced q ^ 2 := by
  rw [schurTriv_eq q hq, ← fBor_normaliser_eq_schurSign q hq]
  field_simp

/-- **The mirror ratio is the generic degree of the sign character:**
`c_triv / c_sign = q⁶`. -/
theorem schurTriv_div_schurSign (q : K) (hq : q ≠ 0)
    (hs : schurSign q ≠ 0) :
    schurTriv q / schurSign q = q ^ 6 := by
  rw [div_eq_iff hs, schurTriv_eq q hq, ← fBor_normaliser_eq_schurSign q hq]
  field_simp

/-- Classical limits: the linear Schur elements and `[3]_q!` all equal `6 = |S₃|`
at `q = 1`; the reflection one equals `3`. -/
theorem classical_limits :
    schurTriv (1 : K) = 6 ∧ schurSign (1 : K) = 6 ∧
      qFactThreeBalanced (1 : K) = 6 ∧ schurRefl (1 : K) = 3 := by
  unfold schurTriv schurSign qFactThreeBalanced schurRefl poincareS3
  norm_num

end Schur

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

theorem qFact_pos {q : K} (hq : 0 < q) : 0 < qFactThreeBalanced q := by
  unfold qFactThreeBalanced; positivity

/-- **Existence:** the three named Schur elements do solve the trace conditions. -/
theorem isSchurInverse_schur {q : K} (hq : 0 < q) :
    IsSchurInverse q (schurTriv q)⁻¹ (schurSign q)⁻¹ (schurRefl q)⁻¹ := by
  have h0 : q ≠ 0 := hq.ne'
  have hT : (1 + 2 * q ^ 2 + 2 * q ^ 4 + q ^ 6 : K) ≠ 0 := by positivity
  have hS : (1 + 2 * q⁻¹ ^ 2 + 2 * q⁻¹ ^ 4 + q⁻¹ ^ 6 : K) ≠ 0 := by positivity
  have hR : (q ^ 2 + 1 + q⁻¹ ^ 2 : K) ≠ 0 := by positivity
  refine ⟨?_, ?_, ?_⟩ <;>
  · unfold schurTriv schurSign schurRefl poincareS3
    field_simp
    ring

/-- For `q > 1`: `c_sign < [3]_q!`. -/
theorem schurSign_lt_balanced {q : K} (hq : 1 < q) :
    schurSign q < qFactThreeBalanced q := by
  have h0 : 0 < q := lt_trans zero_lt_one hq
  rw [← fBor_normaliser_eq_schurSign q h0.ne']
  have hf := qFact_pos h0
  have h3 : 1 < q ^ 3 := one_lt_pow₀ hq (by norm_num)
  rw [div_lt_iff₀ (by positivity)]
  nlinarith

/-- For `q > 1`: `[3]_q! < c_triv`. -/
theorem balanced_lt_schurTriv {q : K} (hq : 1 < q) :
    qFactThreeBalanced q < schurTriv q := by
  have h0 : 0 < q := lt_trans zero_lt_one hq
  rw [schurTriv_eq q h0.ne']
  have hf := qFact_pos h0
  have h3 : 1 < q ^ 3 := one_lt_pow₀ hq (by norm_num)
  nlinarith

/-- **Admissibility, Schur reading (sign).** For `q > 1`,
`q^k · [3]_q! = c_sign` iff `k = −3`. -/
theorem qpow_fact_eq_schurSign_iff {q : K} (hq : 1 < q) (k : ℤ) :
    q ^ k * qFactThreeBalanced q = schurSign q ↔ k = -3 := by
  have h0 : 0 < q := lt_trans zero_lt_one hq
  have hf := (qFact_pos h0).ne'
  rw [← fBor_normaliser_eq_schurSign q h0.ne', div_eq_mul_inv, mul_comm _ (q ^ 3)⁻¹,
    mul_left_inj' hf, ← zpow_natCast, ← zpow_neg]
  exact (zpow_right_injective₀ h0 hq.ne').eq_iff

/-- **Admissibility, Schur reading (trivial).** For `q > 1`,
`q^k · [3]_q! = c_triv` iff `k = 3`. -/
theorem qpow_fact_eq_schurTriv_iff {q : K} (hq : 1 < q) (k : ℤ) :
    q ^ k * qFactThreeBalanced q = schurTriv q ↔ k = 3 := by
  have h0 : 0 < q := lt_trans zero_lt_one hq
  have hf := (qFact_pos h0).ne'
  rw [schurTriv_eq q h0.ne', mul_left_inj' hf, ← zpow_natCast]
  exact (zpow_right_injective₀ h0 hq.ne').eq_iff

/-- **Admissibility, bar reading.** For `q > 1`, `q^k · [3]_q!` is invariant
under `q ↦ q⁻¹` iff `k = 0`. -/
theorem qpow_fact_bar_symmetric_iff {q : K} (hq : 1 < q) (k : ℤ) :
    q⁻¹ ^ k * qFactThreeBalanced q⁻¹ = q ^ k * qFactThreeBalanced q ↔ k = 0 := by
  have h0 : 0 < q := lt_trans zero_lt_one hq
  have hf := (qFact_pos h0).ne'
  rw [← balanced_is_bar_symmetric q h0.ne', mul_left_inj' hf, inv_zpow',
    (zpow_right_injective₀ h0 hq.ne').eq_iff]
  omega

/-- `c_sign` and the reflection Schur element `[3]_q` coincide only at
`q⁴ = q² + 1` (that is, `q² = φ`). -/
theorem schurSign_eq_schurRefl_iff {q : K} (hq : 0 < q) :
    schurSign q = schurRefl q ↔ q ^ 4 = q ^ 2 + 1 := by
  have h0 : q ≠ 0 := hq.ne'
  have hR : (q ^ 4 + q ^ 2 + 1 : K) ≠ 0 := by positivity
  unfold schurSign schurRefl poincareS3
  constructor
  · intro h
    field_simp at h
    have key : (q ^ 4 + q ^ 2 + 1) * (q ^ 4 - q ^ 2 - 1) = 0 := by
      linear_combination -h
    rcases mul_eq_zero.mp key with h1 | h1
    · exact absurd h1 hR
    · linear_combination h1
  · intro h
    field_simp
    linear_combination -(q ^ 4 + q ^ 2 + 1) * h

end Ordered

/-! ### Convention-D Markov normalisation and the ribbon twist -/

section Markov

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Convention-D Markov parameter `z_D = q³/(q² + 1) = tr(σ)`. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- `w_D = tr(σ⁻¹) = z_D − (q − q⁻¹)`, from `σ⁻¹ = σ − (q − q⁻¹)`. -/
def wD (q : K) : K := zD q - (q - q⁻¹)

theorem wD_eq {q : K} (hq : 0 < q) : wD q = 1 / (q ^ 3 + q) := by
  have h0 : q ≠ 0 := hq.ne'
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : q ^ 3 + q ≠ 0 := by positivity
  unfold wD zD
  field_simp
  ring

/-- `z_D · w_D = [2]_q⁻²`: the loop value of the Markov normalisation is the
quantum dimension `[2]_q = q + q⁻¹`. -/
theorem zD_mul_wD {q : K} (hq : 0 < q) : zD q * wD q = ((q + q⁻¹) ^ 2)⁻¹ := by
  have h0 : q ≠ 0 := hq.ne'
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : q + q⁻¹ ≠ 0 := by positivity
  rw [wD_eq hq]
  unfold zD
  field_simp

/-- `z_D / w_D = q⁴`: the per-crossing writhe factor is `λ = q⁻²`. -/
theorem zD_div_wD {q : K} (hq : 0 < q) : zD q / wD q = q ^ 4 := by
  have h0 : q ≠ 0 := hq.ne'
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  rw [wD_eq hq]
  unfold zD
  field_simp

/-- **The Markov route gives `[2]_q²`, not `q⁻³`.** For a writhe-0 closure of a
3-strand braid the normaliser is `(z_D w_D)⁻¹ = [2]_q²`, which exceeds `1`
while `q⁻³ < 1` for `q > 1`. -/
theorem markov_normaliser_ne_inv_cube {q : K} (hq : 1 < q) :
    (zD q * wD q)⁻¹ ≠ (q ^ 3)⁻¹ := by
  have h0 : 0 < q := lt_trans zero_lt_one hq
  rw [zD_mul_wD h0, inv_inv]
  have h3 : 1 < q ^ 3 := one_lt_pow₀ hq (by norm_num)
  have hl : (q ^ 3)⁻¹ < 1 := inv_lt_one_of_one_lt₀ h3
  have hr : 1 < (q + q⁻¹) ^ 2 := by
    have : 1 < q + q⁻¹ := by have := inv_pos.mpr h0; linarith
    nlinarith
  intro h
  linarith

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- The Markov normaliser `[2]_q²` is bar-symmetric. -/
theorem markov_normaliser_bar (q : K) :
    (q⁻¹ + q⁻¹⁻¹) ^ 2 = (q + q⁻¹) ^ 2 := by
  rw [inv_inv, add_comm]

/-- **Ribbon twist.** Reading `z_D = q^{1/2}·θ / [2]_q` (the partial quantum
trace of the Reshetikhin–Turaev braiding `q^{−1/2}σ` is `θ`), the twist of the
convention-D fundamental satisfies `θ² = (z_D [2]_q)² / q = q³`. So
`q⁻³ = θ⁻²`. -/
theorem twist_sq_eq_q_cube {q : K} (hq : 0 < q) :
    (zD q * (q + q⁻¹)) ^ 2 / q = q ^ 3 := by
  have h0 : q ≠ 0 := hq.ne'
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  unfold zD
  field_simp

/-- **No symmetric framing gives `θ^{±2}`.** Equal integer framings `f` on the
three components of a `ℤ/3`-symmetric link total `3f`, never `±2`. -/
theorem no_symmetric_framing_total_two (f : ℤ) : 3 * f ≠ 2 ∧ 3 * f ≠ -2 := by
  constructor <;> omega

end Markov

/-! ### The ruled Borromean word: writhe, purity, length -/

section Word

/-- A braid letter: generator index (0-based) and sign (`true` = positive). -/
abbrev Letter := ℕ × Bool

/-- The ruled word `V³ = (σ₀σ₁⁻¹)³` (photon ruling 2026-11-20; `AGENTS.md`). -/
def v3 : List Letter := [(0, true), (1, false), (0, true), (1, false), (0, true), (1, false)]

def writheOf (w : List Letter) : ℤ :=
  (w.map (fun g => if g.2 then (1 : ℤ) else -1)).sum

/-- Swap the entries at positions `i` and `i+1`. -/
def swapAt (l : List ℕ) (i : ℕ) : List ℕ :=
  (l.set i (l.getD (i + 1) 0)).set (i + 1) (l.getD i 0)

/-- The strand permutation of a 3-strand word, as the final order of labels. -/
def braidPerm (w : List Letter) : List ℕ :=
  w.foldl (fun l g => swapAt l g.1) [0, 1, 2]

theorem v3_writhe_zero : writheOf v3 = 0 := by decide

/-- **`V³` is a pure braid**: its closure has three components, one strand each,
so no component crosses itself and every blackboard framing is 0. -/
theorem v3_pure : braidPerm v3 = [0, 1, 2] := by decide

theorem v3_length : v3.length = 6 := rfl

/-- **Word length is not a braid invariant.** `σ₀σ₀⁻¹` is the identity braid,
yet has length 2 against 0 for the empty word, while both have writhe 0. So
`q^{−ℓ/2}` is not a function on braids, and the `q⁻³ = q^{−ℓ(V³)/2}` reading
does not define a normalisation. -/
theorem length_not_invariant :
    ([(0, true), (0, false)] : List Letter).length ≠ ([] : List Letter).length ∧
      writheOf [(0, true), (0, false)] = writheOf [] := by
  decide

end Word


/-! ### The tension: convention D kills the block whose Schur element is used

The Ocneanu trace `tr_z` on `H₃` is fixed by `tr(1) = 1`, `tr(σ₁) = z`,
`tr(σ₁σ₂) = z²` and `tr(σ₁σ₂σ₁) = z·tr(σ₁²) = z(1 + h z)`, `h = q − q⁻¹`.
On the unnormalised antisymmetriser `x₋ = Σ (−q)^{−ℓ(w)} σ_w` and symmetriser
`x₊ = Σ q^{ℓ(w)} σ_w` it gives quadratics in `z`:

    tr_z(x₋) = (z − q)(z(q² + 1) − q³) / q⁴,
    tr_z(x₊) = (qz + 1)(q³z + qz + 1).

* `trXMinus_zD`: `tr_{z_D}(x₋) = 0`, which is `y_{(1³)} = 0`.
* `trXPlus_zD_relabel`: at the relabelled point `z_D(−q⁻¹) = −1/(q³ + q)` the
  trivial block dies instead. Relabelling `q ↦ −q⁻¹` swaps `c_triv ↔ c_sign`
  (`P(−q) = P(q)`). So the code's rule is frame-independent: **the normaliser is
  the Schur element of the linear block the convention-D trace kills.**
* `hasDerivAt_trXMinus_zD`: **`∂_z tr_z(x₋)` at `z_D` is exactly `−q⁻³`.** Only
  the derivative is proved. When a family of traces vanishes on a block at one
  parameter value, the derivative in the parameter is a standard *candidate* for
  a modified trace on that block (Geer–Patureau-Mirand); that reading is not
  proved here. Caveat, stated: this
  uses `z` as the coordinate. `z` is the axioms' own Markov parameter and the
  shift `w = z − h` leaves `∂_z` unchanged, but another coordinate (Wenzl's `r`,
  or `a = q^{2r}`) multiplies the derivative by `dz/d(coord)`. -/

section Tension

variable {K : Type*} [Field K]

/-- `tr_z(x₋)` from the six basis traces. -/
def trXMinus (q z : K) : K :=
  1 + 2 * (-q)⁻¹ * z + 2 * ((-q)⁻¹) ^ 2 * z ^ 2 + ((-q)⁻¹) ^ 3 * (z * (1 + (q - q⁻¹) * z))

/-- `tr_z(x₊)` from the six basis traces. -/
def trXPlus (q z : K) : K :=
  1 + 2 * q * z + 2 * q ^ 2 * z ^ 2 + q ^ 3 * (z * (1 + (q - q⁻¹) * z))

theorem trXMinus_factor (q z : K) (hq : q ≠ 0) :
    trXMinus q z = (z - q) * (z * (q ^ 2 + 1) - q ^ 3) / q ^ 4 := by
  unfold trXMinus
  rw [inv_neg]
  field_simp
  ring

theorem trXPlus_factor (q z : K) (hq : q ≠ 0) :
    trXPlus q z = (q * z + 1) * (q ^ 3 * z + q * z + 1) := by
  unfold trXPlus
  field_simp
  ring

end Tension

section TensionOrdered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Convention D kills the sign block**: `tr_{z_D}(x₋) = 0`. -/
theorem trXMinus_zD {q : K} (hq : 0 < q) : trXMinus q (zD q) = 0 := by
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  rw [trXMinus_factor q _ hq.ne']
  unfold zD
  field_simp
  ring

/-- **The relabelled convention D kills the trivial block**:
`tr_{z'}(x₊) = 0` at `z' = z_D(−q⁻¹) = −1/(q³ + q)`. -/
theorem trXPlus_zD_relabel {q : K} (hq : 0 < q) :
    trXPlus q (-1 / (q ^ 3 + q)) = 0 := by
  have h1 : q ^ 3 + q ≠ 0 := by positivity
  rw [trXPlus_factor q _ hq.ne']
  field_simp
  ring

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- The relabelling `q ↦ −q⁻¹` swaps the two linear Schur elements. -/
theorem schurSign_relabel (q : K) :
    schurSign (-q⁻¹) = schurTriv q := by
  unfold schurSign schurTriv poincareS3
  rw [inv_neg, inv_inv]
  ring

/-- `z_D` relabels to `−1/(q³ + q)`. -/
theorem zD_relabel {q : K} (hq : 0 < q) : zD (-q⁻¹) = -1 / (q ^ 3 + q) := by
  have h0 : q ≠ 0 := hq.ne'
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : q ^ 3 + q ≠ 0 := by positivity
  unfold zD
  field_simp
  ring

end TensionOrdered

section Derivative

/-! The derivative statements are stated over any nontrivially normed field `𝕜`
(§7c: no archimedean structure is used; only the field operations and
`HasDerivAt`). The convention-D point is written out as `q³/(q² + 1)`. -/

variable {𝕜 : Type*} [NontriviallyNormedField 𝕜]

/-- **`∂_z tr_z(x₋)` at `z_D` is `−q⁻³`.** Only the derivative is proved here.
Reading `−∂_z tr_z(x₋)|_{z_D}` as a modified (Geer–Patureau-Mirand) dimension of
the killed block is an interpretation, not a theorem, and the value depends on
using `z` as the coordinate (`hasDerivAt_trXMinus_idempotent_coord`). -/
theorem hasDerivAt_trXMinus_zD {q : 𝕜} (h0 : q ≠ 0) (h1 : q ^ 2 + 1 ≠ 0) :
    HasDerivAt (fun z => (z - q) * (z * (q ^ 2 + 1) - q ^ 3) / q ^ 4)
      (-(q ^ 3)⁻¹) (q ^ 3 / (q ^ 2 + 1)) := by
  have hd := (((hasDerivAt_id (q ^ 3 / (q ^ 2 + 1))).sub_const q).mul
    (((hasDerivAt_id (q ^ 3 / (q ^ 2 + 1))).mul_const (q ^ 2 + 1)).sub_const (q ^ 3))).div_const
      (q ^ 4)
  convert hd using 1
  simp only [id, one_mul]
  field_simp
  ring

/-- The same function as the named trace, via `trXMinus_factor`. -/
theorem trXMinus_eq_fun {q : 𝕜} (h0 : q ≠ 0) :
    (fun z => trXMinus q z) = (fun z => (z - q) * (z * (q ^ 2 + 1) - q ^ 3) / q ^ 4) := by
  funext z
  exact trXMinus_factor q z h0

/-- **The coordinate is not forced.** In the idempotent coordinate
`t = τ(P₋) = (q − z)/[2]_q`, so `z = q − [2]_q t`, the same trace has derivative
`(q + q⁻¹)·q⁻³` at the convention-D point, so `−∂_t tr(x₋) = −[2]_q q⁻³`, not
`q⁻³`. (Symbolically, Wenzl's `a = q^{2r}` gives
`−1/(q⁴(q² − 1)(q² + 1)²)`, not a power of `q`; that case is a sympy
computation in `computations/probes/proton_q3_normaliser/` and is not formalised
here.) Only the standard-basis coordinates `z = tr(σ)` and `w = tr(σ⁻¹)` give
exactly `q⁻³`. -/
theorem hasDerivAt_trXMinus_idempotent_coord {q : 𝕜} (h0 : q ≠ 0) (h1 : q ^ 2 + 1 ≠ 0) :
    HasDerivAt (fun t => (q - (q + q⁻¹) * t - q) *
        ((q - (q + q⁻¹) * t) * (q ^ 2 + 1) - q ^ 3) / q ^ 4)
      ((q + q⁻¹) * (q ^ 3)⁻¹) ((q - q ^ 3 / (q ^ 2 + 1)) / (q + q⁻¹)) := by
  have hz : HasDerivAt (fun t : 𝕜 => q - (q + q⁻¹) * t) (-(q + q⁻¹))
      ((q - q ^ 3 / (q ^ 2 + 1)) / (q + q⁻¹)) := by
    simpa using
      ((hasDerivAt_id ((q - q ^ 3 / (q ^ 2 + 1)) / (q + q⁻¹))).const_mul (q + q⁻¹)).const_sub q
  have hd := ((hz.sub_const q).mul ((hz.mul_const (q ^ 2 + 1)).sub_const (q ^ 3))).div_const
    (q ^ 4)
  convert hd using 1
  field_simp
  ring

end Derivative

/-! ### A canonical-coordinate criterion: integral and bar-invariant

A coordinate on the family of Markov traces that is itself a trace,
`c = tr(b)` with `b = u·σ + v ∈ H₂`, is affine in `z`: `c = u z + v`, so
`−∂_c tr(x₋) = −u⁻¹ ∂_z tr(x₋) = u⁻¹ q⁻³` at `z_D`. Wenzl's `a` is not of this
form, and the idempotent `τ(P₋)` has `u = −[2]_q⁻¹`, which is not in the integral
form `ℤ[q, q⁻¹]`.

Ask that `b` generate `H₂` over `ℤ[q, q⁻¹]` together with `1` (so `u` is a unit,
`u = ε q^m`, `ε = ±1`; this is the standard description of the units of a Laurent
ring and is an input here, not proved) and that `b` be bar-invariant (the
Kazhdan–Lusztig condition; `bar σ = σ⁻¹ = σ − (q − q⁻¹)`, `bar q = q⁻¹`). The
`σ`-coefficient of `bar b` is `bar u = ε q^{−m}`, so bar-invariance forces
`q^{−m} = q^m`, hence `m = 0` (`kl_unit_exponent_zero`), and then
`|u⁻¹ q⁻³| = q⁻³` (`kl_coordinate_derivative`). Both
`C'_s = σ + q⁻¹` and `C_s = σ − q` qualify. So **under "integral and
bar-invariant", the coordinate is forced up to sign and the derivative is
`±q⁻³`.** The criterion itself is a choice, stated. -/

section KLCoordinate

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Bar-invariance of `ε q^m σ + v` forces `m = 0` (for `q > 1`). -/
theorem kl_unit_exponent_zero {q : K} (hq : 1 < q) (ε : K) (hε : ε ≠ 0) (m : ℤ)
    (hbar : ε * q ^ (-m) = ε * q ^ m) : m = 0 := by
  have h0 : 0 < q := lt_trans zero_lt_one hq
  have h := mul_left_cancel₀ hε hbar
  have := (zpow_right_injective₀ h0 hq.ne').eq_iff.mp h
  omega

/-- With `u = ε = ±1` the coordinate derivative is `ε·q⁻³`, so its absolute
value is `q⁻³`. -/
theorem kl_coordinate_derivative {q : K} (hq : 0 < q) (ε : K) (hε : ε = 1 ∨ ε = -1) :
    |ε⁻¹ * (q ^ 3)⁻¹| = (q ^ 3)⁻¹ := by
  have : 0 < (q ^ 3)⁻¹ := by positivity
  rcases hε with h | h <;> subst h <;> simp [abs_of_pos this]

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- Both Kazhdan–Lusztig elements `C'_s = σ + q⁻¹` and `C_s = σ − q` are
bar-invariant: with `bar σ = σ − (q − q⁻¹)` and `bar q = q⁻¹`, the constant terms
match. -/
theorem kl_elements_bar_invariant (q : K) :
    (-(q - q⁻¹) + q⁻¹⁻¹ = q⁻¹) ∧ (-(q - q⁻¹) - q⁻¹ = -q) := by
  refine ⟨?_, ?_⟩
  · rw [inv_inv]; ring
  · ring

end KLCoordinate

end QOU.MassTheory.ProtonQ3Schur
