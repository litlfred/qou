import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Abel
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp

/-!
# Normal-form length invariants of `H₃(q)` are rewrite-order independent

Bean `qou-99qc`, P3 (owner, 2026-11-20): read an energy off the change of a
normal-form q-degree or Bruhat length between the initial and final states of
`n → p e⁻ ν̄`.

`predicted-spectra/beta-decay-skein-properties` reads its `Q`-value off a
*count of rewrite steps*. R3 (PR #8632) measured that count on `(σ₁σ₂)⁵`:
25 leftmost-first, 30 rightmost-first, same normal form. A step count is a
property of a rewrite *path*, not of the element.

This file proves the replacement: in `H₃(q)` (generic commutative ring,
`h = q − q⁻¹`) the coefficient vector in the basis `T_w`, `w ∈ S₃`, is
unchanged by every Gröbner–Shirshov rewrite (quadratic `σᵢσᵢ ↦ hσᵢ + 1`,
braid `σ₁σ₂σ₁ ↦ σ₂σ₁σ₂`) at every position (`eval_quad`, `eval_braid`). So any
function of that vector is a function of the element, independent of rewrite
order. This is the H₃ case of the statement bean `qou-n2un` records as open for
`thm:groebner-shirshov-energy` ("paths are reductions of the same element").

The invariants defined here:

* `leadLen` — leading Bruhat length `max {ℓ(w) : c_w ≠ 0}`;
* `lenWeighted q` — `Σ_w c_w q^{ℓ(w)}`. It is multiplicative along words
  (`lenWeighted_act`): it is the index character `χ_(3)`, so on a braid word
  it is `q^{writhe}` (`lenWeighted_eval_pos`, `lenWeighted_eval_inv`).

Basis order (`Fin 6`): `0 = e, 1 = s₁, 2 = s₂, 3 = s₁s₂, 4 = s₂s₁, 5 = s₁s₂s₁`.
Letters (`Fin 2`): `0 = σ₁`, `1 = σ₂`. A word acts on the right:
`eval w = T_{w₁} ⋯ T_{w_k}` expanded in the basis.
-/

namespace QOU.QBeta.NFLength

open Finset

variable {R : Type*} [CommRing R]

/-- Bruhat length of the six elements of `S₃` in the fixed basis order. -/
def len : Fin 6 → ℕ := ![0, 1, 1, 2, 2, 3]

/-- Right multiplication by `σ₁` on coefficient vectors:
`T_w T_{s₁} = T_{ws₁}` if `ℓ(ws₁) > ℓ(w)`, else `h T_w + T_{ws₁}`. -/
def act1 (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 1, v 0 + h * v 1, v 4, v 5, v 2 + h * v 4, v 3 + h * v 5]

/-- Right multiplication by `σ₂`. -/
def act2 (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 2, v 3, v 0 + h * v 2, v 1 + h * v 3, v 5, v 4 + h * v 5]

/-- Right multiplication by the letter `i`. -/
def act (h : R) : Fin 2 → (Fin 6 → R) → Fin 6 → R
  | 0 => act1 h
  | 1 => act2 h

/-- The unit `T_e`. -/
def one : Fin 6 → R := ![1, 0, 0, 0, 0, 0]

/-- Normal form of a positive braid word: apply its letters left to right. -/
def eval (h : R) (w : List (Fin 2)) : Fin 6 → R :=
  w.foldl (fun v i => act h i v) one

theorem act_add (h : R) (i : Fin 2) (v u : Fin 6 → R) :
    act h i (v + u) = act h i v + act h i u := by
  funext k; fin_cases i <;> fin_cases k <;> simp [act, act1, act2] <;> ring

theorem act_smul (h c : R) (i : Fin 2) (v : Fin 6 → R) :
    act h i (c • v) = c • act h i v := by
  funext k; fin_cases i <;> fin_cases k <;> simp [act, act1, act2] <;> ring

/-- **Quadratic relation** `σᵢ² = h σᵢ + 1`, as operators on coefficient vectors. -/
theorem act_quad (h : R) (i : Fin 2) (v : Fin 6 → R) :
    act h i (act h i v) = h • act h i v + v := by
  funext k; fin_cases i <;> fin_cases k <;> simp [act, act1, act2] <;> ring

/-- **Braid relation** `σ₁σ₂σ₁ = σ₂σ₁σ₂`, as operators on coefficient vectors. -/
theorem act_braid (h : R) (v : Fin 6 → R) :
    act h 0 (act h 1 (act h 0 v)) = act h 1 (act h 0 (act h 1 v)) := by
  funext k; fin_cases k <;> simp [act, act1, act2] <;> ring

theorem eval_append (h : R) (u w : List (Fin 2)) :
    eval h (u ++ w) = w.foldl (fun v i => act h i v) (eval h u) := by
  simp [eval, List.foldl_append]

/-- Folding a word is additive in the starting vector. -/
theorem foldl_act_add (h : R) (w : List (Fin 2)) (v u : Fin 6 → R) :
    w.foldl (fun x i => act h i x) (v + u)
      = w.foldl (fun x i => act h i x) v + w.foldl (fun x i => act h i x) u := by
  induction w generalizing v u with
  | nil => rfl
  | cons i w ih => simp only [List.foldl_cons, act_add]; exact ih _ _

theorem foldl_act_smul (h c : R) (w : List (Fin 2)) (v : Fin 6 → R) :
    w.foldl (fun x i => act h i x) (c • v) = c • w.foldl (fun x i => act h i x) v := by
  induction w generalizing v with
  | nil => rfl
  | cons i w ih => simp only [List.foldl_cons, act_smul]; exact ih _

/-- **A quadratic rewrite, anywhere in the word, preserves the normal form.**
`eval (u σᵢσᵢ w) = h · eval (u σᵢ w) + eval (u w)`. -/
theorem eval_quad (h : R) (u w : List (Fin 2)) (i : Fin 2) :
    eval h (u ++ [i, i] ++ w) = h • eval h (u ++ [i] ++ w) + eval h (u ++ w) := by
  simp only [eval_append, List.foldl_cons, List.foldl_nil]
  rw [act_quad, foldl_act_add, foldl_act_smul]

/-- **A braid rewrite, anywhere in the word, preserves the normal form.** -/
theorem eval_braid (h : R) (u w : List (Fin 2)) :
    eval h (u ++ [0, 1, 0] ++ w) = eval h (u ++ [1, 0, 1] ++ w) := by
  simp only [eval_append, List.foldl_cons, List.foldl_nil]
  rw [act_braid]

/-- The six reduced words evaluate to the six basis vectors: the coefficient
vector *is* the Gröbner–Shirshov normal form. -/
theorem eval_reduced (h : R) :
    eval h [] = ![1, 0, 0, 0, 0, 0] ∧ eval h [0] = ![0, 1, 0, 0, 0, 0] ∧
    eval h [1] = ![0, 0, 1, 0, 0, 0] ∧ eval h [0, 1] = ![0, 0, 0, 1, 0, 0] ∧
    eval h [1, 0] = ![0, 0, 0, 0, 1, 0] ∧ eval h [0, 1, 0] = ![0, 0, 0, 0, 0, 1] := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;> funext k <;> fin_cases k <;>
    simp [eval, act, act1, act2, one]

/-! ## Inverse letters -/

/-- `σᵢ⁻¹ = σᵢ − h` as an operator. -/
def actInv (h : R) (i : Fin 2) (v : Fin 6 → R) : Fin 6 → R := act h i v - h • v

/-- `σᵢ⁻¹` is a two-sided inverse of `σᵢ` (from the quadratic relation). -/
theorem actInv_act (h : R) (i : Fin 2) (v : Fin 6 → R) :
    actInv h i (act h i v) = v ∧ act h i (actInv h i v) = v := by
  constructor
  · unfold actInv; rw [act_quad]; abel
  · unfold actInv
    have : act h i (act h i v - h • v) = act h i (act h i v) - h • act h i v := by
      funext k; fin_cases i <;> fin_cases k <;> simp [act, act1, act2]
    rw [this, act_quad]; abel

/-! ## Invariants -/

/-- Length-weighted functional `Σ_w c_w q^{ℓ(w)}`. -/
def lenWeighted (q : R) (v : Fin 6 → R) : R := ∑ k, v k * q ^ len k

/-- **`lenWeighted` is the index character.** With `h = q − q⁻¹`, appending a
letter multiplies it by `q`. -/
theorem lenWeighted_act (q qi : R) (hq : q * qi = 1) (i : Fin 2) (v : Fin 6 → R) :
    lenWeighted q (act (q - qi) i v) = q * lenWeighted q v := by
  fin_cases i
  · simp only [lenWeighted, Fin.sum_univ_six, len, act, act1]
    simp
    linear_combination (-(v 1 + q * v 4 + q ^ 2 * v 5)) * hq
  · simp only [lenWeighted, Fin.sum_univ_six, len, act, act2]
    simp
    linear_combination (-(v 2 + q * v 3 + q ^ 2 * v 5)) * hq

theorem lenWeighted_actInv (q qi : R) (hq : q * qi = 1) (i : Fin 2) (v : Fin 6 → R) :
    lenWeighted q (actInv (q - qi) i v) = qi * lenWeighted q v := by
  have hlin : ∀ (a b : Fin 6 → R) (c : R),
      lenWeighted q (a - c • b) = lenWeighted q a - c * lenWeighted q b := by
    intro a b c
    simp only [lenWeighted, Fin.sum_univ_six, Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
    ring
  unfold actInv; rw [hlin, lenWeighted_act q qi hq]; ring

/-- On a positive word of length `k`, `lenWeighted = q^k`. -/
theorem lenWeighted_eval_pos (q qi : R) (hq : q * qi = 1) (w : List (Fin 2)) :
    lenWeighted q (eval (q - qi) w) = q ^ w.length := by
  have key : ∀ (w : List (Fin 2)) (v : Fin 6 → R),
      lenWeighted q (w.foldl (fun x i => act (q - qi) i x) v)
        = q ^ w.length * lenWeighted q v := by
    intro w
    induction w with
    | nil => intro v; simp
    | cons i w ih =>
      intro v
      simp only [List.foldl_cons, List.length_cons]
      rw [ih, lenWeighted_act q qi hq]; ring
  rw [eval, key]; simp [lenWeighted, Fin.sum_univ_six, len, one]

/-- Signed words: `true` = `σᵢ`, `false` = `σᵢ⁻¹`. -/
def evalSigned (h : R) (w : List (Fin 2 × Bool)) : Fin 6 → R :=
  w.foldl (fun v p => if p.2 then act h p.1 v else actInv h p.1 v) one

/-- **On a signed braid word, `lenWeighted = q^{#σ} · q⁻¹^{#σ⁻¹}`, i.e. `q^{writhe}`.** -/
theorem lenWeighted_eval_signed (q qi : R) (hq : q * qi = 1) (w : List (Fin 2 × Bool)) :
    lenWeighted q (evalSigned (q - qi) w)
      = q ^ (w.filter (·.2)).length * qi ^ (w.filter (fun p => !p.2)).length := by
  have key : ∀ (w : List (Fin 2 × Bool)) (v : Fin 6 → R),
      lenWeighted q (w.foldl (fun x p => if p.2 then act (q - qi) p.1 x
          else actInv (q - qi) p.1 x) v)
        = q ^ (w.filter (·.2)).length * qi ^ (w.filter (fun p => !p.2)).length
            * lenWeighted q v := by
    intro w
    induction w with
    | nil => intro v; simp
    | cons p w ih =>
      intro v
      obtain ⟨i, b⟩ := p
      cases b
      · simp only [List.foldl_cons, Bool.false_eq_true, if_false]
        rw [ih, lenWeighted_actInv q qi hq]
        simp; ring
      · simp only [List.foldl_cons, if_true]
        rw [ih, lenWeighted_act q qi hq]
        simp; ring
  rw [evalSigned, key]; simp [lenWeighted, Fin.sum_univ_six, len, one]

/-- **The Borromean / γγ core `V³ = (σ₁σ₂⁻¹)³` has `lenWeighted = 1`.** It has
writhe 0. Since the γγ-selected element is `V³` for the proton and the neutron
alike, `lenWeighted` gives them the same value. -/
theorem lenWeighted_V3 (q qi : R) (hq : q * qi = 1) :
    lenWeighted q (evalSigned (q - qi)
      [(0, true), (1, false), (0, true), (1, false), (0, true), (1, false)]) = 1 := by
  rw [lenWeighted_eval_signed q qi hq]
  simp
  linear_combination (q ^ 2 * qi ^ 2 + q * qi + 1) * hq

/-- Leading Bruhat length of a coefficient vector (`0` for the zero vector). -/
def leadLen [DecidableEq R] (v : Fin 6 → R) : ℕ :=
  (univ.filter (fun k => v k ≠ 0)).sup len

/-- Any function of the normal form is unchanged by a braid rewrite. -/
theorem invariant_braid {α : Type*} (f : (Fin 6 → R) → α) (h : R) (u w : List (Fin 2)) :
    f (eval h (u ++ [0, 1, 0] ++ w)) = f (eval h (u ++ [1, 0, 1] ++ w)) := by
  rw [eval_braid]

/-! ## The short typed-crossing nucleons

`p = σ₁σ₂ − (h/2)σ₁`, `n = σ₁σ₂ − hσ₁ − (h/2)σ₂ + h²/2`, so `n − p = Δ_S`
(`qbeta_delta_element_fork_pricing_probe`, R3 probe). -/

/-- Short-model proton normal form. -/
def nucP {K : Type*} [Field K] (h : K) : Fin 6 → K := ![0, -h / 2, 0, 1, 0, 0]

/-- Short-model neutron normal form. -/
def nucN {K : Type*} [Field K] (h : K) : Fin 6 → K := ![h ^ 2 / 2, -h, -h / 2, 1, 0, 0]

/-- **The length-weighted functional separates the short-model nucleons**:
`χ(n) − χ(p) = −h(q + q⁻¹)/2 = −h[2]/2`. -/
theorem lenWeighted_nucN_sub_nucP {K : Type*} [Field K] (q qi : K) (h2 : (2 : K) ≠ 0) :
    lenWeighted q (nucN (q - qi)) - lenWeighted q (nucP (q - qi))
      = -(q - qi) * (q + qi) / 2 := by
  simp only [lenWeighted, Fin.sum_univ_six, len, nucN, nucP]
  simp
  field_simp
  ring

/-- Corpus `thm:groebner-shirshov-energy`: `E(ξ) = Σ_w |c_w| ℓ(w)` on the normal form. -/
noncomputable def gsEnergy (v : Fin 6 → ℝ) : ℝ := ∑ k, |v k| * (len k : ℝ)

/-- **`thm:groebner-shirshov-energy` path-independence, H₃ case**: a quadratic rewrite
at any position leaves the energy of the element unchanged, because it leaves the
normal form unchanged (`eval_quad`). -/
theorem gsEnergy_quad (h : ℝ) (u w : List (Fin 2)) (i : Fin 2) :
    gsEnergy (eval h (u ++ [i, i] ++ w))
      = gsEnergy (h • eval h (u ++ [i] ++ w) + eval h (u ++ w)) := by
  rw [eval_quad]

end QOU.QBeta.NFLength
