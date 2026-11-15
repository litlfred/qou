import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# QOU.Eightfold.G2FrameDimensions — the `G₂` frame, as dimension arithmetic

Three results in the corpus point at `G₂` and have never been stated together.
This file supplies the arithmetic that joins them. **Everything here is integer
combinatorics** — no `ℝ`, no ordering, no analysis (§7c-clean). It proves nothing
about Lie groups, octonions, or manifolds; what it proves is that the *numbers*
those three fragments quote are forced, and that they are forced at exactly one
place each.

## The three fragments

1. **Eightfold open-problem item 3** — the continuous `G₂` completion,
   `S⁶ = G₂/SU(3)_c`, recorded as a Mathlib-infrastructure gap.
2. **Bean `qou-8p1f`** (`computations/form_stabilizer_genericity_su3_routes.py`) —
   the generic-form route runs through **3-forms in dimension 7**, not 4-forms in
   dimension 8, because `dim GL(8) = 64 < dim Λ⁴(ℝ⁸) = 70` leaves no room for an
   open orbit.
3. **Bean `qou-ko4g`** — `g2_dim_split : 8 + 6 = 14`, noting that `G₂/SU(3) = S⁶`
   and the quaternionic Wolf space `G₂/SO(4)` are complementary, and that the
   corpus had never put the tetraplectic `SU(2)` and colour `SU(3)` in one frame.

## What is proved here

Write `dim 𝔰𝔲(n) = n² − 1` and `dim 𝔰𝔬(n) = C(n,2)` (both standard), and
`dim 𝔤₂ = 14` (proved for `Der(𝕆)` over `ℚ` in
`QOU.MathlibExt.OctonionDerivations.octonion_derivation_dim`, and used here only
as the numeral it is).

* **The open-orbit necessary condition, as a table.** A `GL(n,ℝ)` orbit on
  `Λᵏ(ℝⁿ)` can be open only if `dim GL(n) = n² ≥ dim Λᵏ(ℝⁿ) = C(n,k)`.
  `choose_three_le_sq_iff` : for `k = 3` this holds **exactly for `n ≤ 8`**.
  `choose_four_le_sq_iff` : for `k = 4` it holds **exactly for `n ≤ 7`** — so
  `n = 8` is precisely where the 4-form route dies. That is `qou-8p1f`'s negative,
  generalised from one dimension to the whole series.
* **Dimension 7 is singled out, and uniquely.** `sq_sub_choose_three_eq_g2_iff` :
  `n² − C(n,3) = 14` holds **iff `n = 7`**. The left side is the dimension a
  stabiliser must have if the orbit is open; the right side is `dim 𝔤₂`. So the
  one dimension at which a generic 3-form has a 14-dimensional stabiliser is 7.
  (The identity is arithmetic. That the stabiliser there *is* `G₂` is classical
  input, not proved here.)
* **The two `G₂` quotients are supplied by disjoint classical series.**
  `g2_quotient_su_dim_six_iff` : `SU(3)` is the **only** unitary subgroup whose
  `G₂` quotient is 6-dimensional. `g2_quotient_so_dim_eight_iff` : `SO(4)` is the
  only orthogonal one giving 8. And the crossings fail:
  `no_orthogonal_quotient_of_dim_six` — **no** `SO(n)` gives a 6-dimensional
  quotient, so `S⁶` cannot be reached from the orthogonal series at all; and
  `no_unitary_quotient_of_dim_eight` — no `SU(n)` gives the 8-dimensional Wolf
  space. This is the sharp form of `qou-ko4g`'s observation: the tetraplectic
  `SU(2)`, which enters `G₂` through `SO(4) = (SU(2)×SU(2))/ℤ₂`
  (`so_dim_eq_two_su2_iff`), sits on the *other* series from colour `SU(3)`, and
  the two legs cannot be exchanged by any change of `n`.
* **Why 6 is the right shape for a degree-3 volume form.** `6 = 2·3`: the
  isotropy of `G₂/SU(3)` is the complex 3-dimensional `𝟑` of `SU(3)`, i.e. real
  dimension 6. `choose_three_eq_one_iff` records that a rank-3 object has exactly
  two exterior powers that are lines, `Λ⁰` and `Λ³` — so `Λ³W ≅ 𝟙` is the only
  non-trivial volume form such an object can carry, which is the degree-3 half of
  the dichotomy proved in
  `QOU.QuantumObservableUniverse.VolumeFormDegree`.

## What is deliberately NOT claimed

* No Lie group appears here. `dimSU`, `dimSO`, `dimG2` are `ℕ`-valued functions
  named after dimension formulas; nothing in this file connects them to a group.
  Mathlib has neither an `Octonion` type nor a `G₂` Lie group, and this file does
  not supply either.
* Nothing here says a generic 3-form on `ℝ⁷` **has** an open orbit, only that the
  dimension count does not forbid it (and forbids it for `Λ⁴(ℝ⁸)`). Openness is
  the classical Hitchin/Bryant fact, cited, not formalised.
* Nothing here says the isotropy representation of `G₂/SU(3)` is complex type.
  That is the Günaydin–Gürsey `Im 𝕆 = 𝟏 ⊕ 𝟑 ⊕ 𝟑̄` input already cited by
  `prop:color-su3-from-g2`; what is proved is only that its **dimension** is
  `2 · 3` and that no orthogonal quotient shares it.

-- Ref: [leitner2026] docs/audits/2026-09-04-the-g2-frame.md
-- Ref: [baez2002] https://doi.org/10.1090/S0273-0979-01-00934-X
-/

namespace QOU.Eightfold.G2Frame

/-- `dim 𝔰𝔲(n) = n² − 1`. A naming function on `ℕ`, not a group. -/
def dimSU (n : ℕ) : ℕ := n ^ 2 - 1

/-- `dim 𝔰𝔬(n) = C(n,2)`. -/
def dimSO (n : ℕ) : ℕ := n.choose 2

/-- `dim 𝔤₂ = 14`. Proved for `Der(𝕆)` over `ℚ` in
`QOU.MathlibExt.OctonionDerivations.octonion_derivation_dim`; used here as a
numeral. -/
def dimG2 : ℕ := 14

/-! ## 1. Growth lemmas for the binomial coefficients -/

/-- `2n + 1 ≤ C(n,2)` for `n ≥ 6`. The step needed to beat the increment of a
square. -/
theorem two_mul_add_one_le_choose_two : ∀ n : ℕ, 6 ≤ n → 2 * n + 1 ≤ n.choose 2 := by
  intro n hn
  induction n, hn using Nat.le_induction with
  | base => decide
  | succ m hm ih =>
    have hp : (m + 1).choose 2 = m.choose 1 + m.choose 2 := Nat.choose_succ_succ m 1
    have h1 : m.choose 1 = m := Nat.choose_one_right m
    omega

/-- `2n + 1 ≤ C(n,3)` for `n ≥ 6`. -/
theorem two_mul_add_one_le_choose_three : ∀ n : ℕ, 6 ≤ n → 2 * n + 1 ≤ n.choose 3 := by
  intro n hn
  induction n, hn using Nat.le_induction with
  | base => decide
  | succ m hm ih =>
    have hp : (m + 1).choose 3 = m.choose 2 + m.choose 3 := Nat.choose_succ_succ m 2
    have h2 : 15 ≤ m.choose 2 := le_trans (by decide) (Nat.choose_mono 2 hm)
    omega

/-- **The induction that makes `C(n,k+1)` outrun `n²`.** If the inequality holds at
`n₀` and each step of `C(·,k)` exceeds the increment `2m + 1` of a square, it holds
from `n₀` on. -/
theorem sq_lt_choose_succ {k n₀ : ℕ}
    (hbase : n₀ ^ 2 < n₀.choose (k + 1))
    (hstep : ∀ m : ℕ, n₀ ≤ m → 2 * m + 1 ≤ m.choose k) :
    ∀ n : ℕ, n₀ ≤ n → n ^ 2 < n.choose (k + 1) := by
  intro n hn
  induction n, hn using Nat.le_induction with
  | base => exact hbase
  | succ m hm ih =>
    calc (m + 1) ^ 2 = m ^ 2 + (2 * m + 1) := by ring
      _ < m.choose (k + 1) + m.choose k :=
          Nat.add_lt_add_of_lt_of_le ih (hstep m hm)
      _ = (m + 1).choose (k + 1) := by rw [Nat.choose_succ_succ]; exact Nat.add_comm _ _

/-- `n² < C(n,3)` for every `n ≥ 9`. -/
theorem sq_lt_choose_three_of_nine_le (n : ℕ) (hn : 9 ≤ n) : n ^ 2 < n.choose 3 :=
  sq_lt_choose_succ (k := 2) (by decide)
    (fun m hm => two_mul_add_one_le_choose_two m (by omega)) n hn

/-- `n² < C(n,4)` for every `n ≥ 8`. -/
theorem sq_lt_choose_four_of_eight_le (n : ℕ) (hn : 8 ≤ n) : n ^ 2 < n.choose 4 :=
  sq_lt_choose_succ (k := 3) (by decide)
    (fun m hm => two_mul_add_one_le_choose_three m (by omega)) n hn

/-! ## 2. The open-orbit necessary condition, as a table

`GL(n,ℝ)` has dimension `n²` and acts on `Λᵏ(ℝⁿ)`, of dimension `C(n,k)`. An orbit
is a quotient of the group, so an **open** orbit requires `C(n,k) ≤ n²`. -/

/-- **3-forms: the count permits an open orbit exactly for `n ≤ 8`.**
`C(7,3) = 35 ≤ 49` and `C(8,3) = 56 ≤ 64`, but `C(9,3) = 84 > 81`. -/
theorem choose_three_le_sq_iff (n : ℕ) : n.choose 3 ≤ n ^ 2 ↔ n ≤ 8 := by
  constructor
  · intro h
    by_contra hlt
    push_neg at hlt
    exact absurd h (not_le.mpr (sq_lt_choose_three_of_nine_le n hlt))
  · intro h
    interval_cases n <;> decide

/-- **4-forms: the count permits an open orbit exactly for `n ≤ 7`.** So the first
failure is `n = 8`: `C(8,4) = 70 > 64 = dim GL(8)`. This is bean `qou-8p1f`'s
negative — "no 4-form on `ℝ⁸` has an open orbit, so *generic 4-form* singles out
nothing" — with the surrounding series supplied, which is what shows `8` is a
boundary rather than an isolated bad case. -/
theorem choose_four_le_sq_iff (n : ℕ) : n.choose 4 ≤ n ^ 2 ↔ n ≤ 7 := by
  constructor
  · intro h
    by_contra hlt
    push_neg at hlt
    exact absurd h (not_le.mpr (sq_lt_choose_four_of_eight_le n hlt))
  · intro h
    interval_cases n <;> decide

/-- **Dimension 7 is the unique one whose generic-3-form stabiliser has dimension
`dim 𝔤₂`.** If the `GL(n)` orbit of a 3-form is open then the stabiliser has
dimension `n² − C(n,3)`, and that equals `14` for `n = 7` and for no other `n`.
The classical fact that the stabiliser there is `G₂` is input, not proved here;
what is proved is that the arithmetic leaves exactly one candidate dimension. -/
theorem sq_sub_choose_three_eq_g2_iff (n : ℕ) : n ^ 2 - n.choose 3 = dimG2 ↔ n = 7 := by
  unfold dimG2
  constructor
  · intro h
    rcases le_or_gt n 8 with h8 | h9
    · interval_cases n <;> revert h <;> decide
    · exact absurd h (by
        rw [Nat.sub_eq_zero_of_le (le_of_lt (sq_lt_choose_three_of_nine_le n h9))]
        decide)
  · rintro rfl; decide

/-! ## 3. The two `G₂` quotients, and why the series do not cross -/

/-- **`SU(3)` is the only unitary subgroup with a 6-dimensional `G₂` quotient.**
`14 − dim 𝔰𝔲(n) = 6` iff `n = 3`. The quotient is `S⁶`. -/
theorem g2_quotient_su_dim_six_iff (n : ℕ) : dimG2 - dimSU n = 6 ↔ n = 3 := by
  unfold dimG2 dimSU
  constructor
  · intro h
    rcases le_or_gt n 3 with h3 | h4
    · interval_cases n <;> revert h <;> decide
    · exfalso
      have h16 : 16 ≤ n ^ 2 := by
        have := Nat.pow_le_pow_left h4 2
        norm_num at this
        exact this
      generalize n ^ 2 = A at h h16
      omega
  · rintro rfl; decide

/-- **`SO(4)` is the only orthogonal subgroup with an 8-dimensional `G₂`
quotient.** `14 − dim 𝔰𝔬(n) = 8` iff `n = 4`. The quotient is the quaternionic
Wolf space `G₂/SO(4)`. -/
theorem g2_quotient_so_dim_eight_iff (n : ℕ) : dimG2 - dimSO n = 8 ↔ n = 4 := by
  unfold dimG2 dimSO
  constructor
  · intro h
    rcases le_or_gt n 4 with h4 | h5
    · interval_cases n <;> revert h <;> decide
    · exfalso
      have h10 : 10 ≤ n.choose 2 := le_trans (by decide) (Nat.choose_mono 2 h5)
      omega
  · rintro rfl; decide

/-- **No orthogonal subgroup gives a 6-dimensional `G₂` quotient — at all.**
`C(n,2)` jumps `6 → 10` from `n = 4` to `n = 5`, so `14 − C(n,2)` never equals `6`.
Consequence for the framework: `S⁶` is *not* reachable from the orthogonal series,
so the tetraplectic `SU(2)` leg — which enters `G₂` through `SO(4)` — cannot be
deformed into the colour leg by any change of `n`. The two fragments meet in `G₂`
and nowhere below it. -/
theorem no_orthogonal_quotient_of_dim_six (n : ℕ) : dimG2 - dimSO n ≠ 6 := by
  unfold dimG2 dimSO
  intro h
  rcases le_or_gt n 5 with h5 | h6
  · revert h; interval_cases n <;> decide
  · have h15 : 15 ≤ n.choose 2 := le_trans (by decide) (Nat.choose_mono 2 h6)
    omega

/-- **No unitary subgroup gives an 8-dimensional `G₂` quotient.**
`14 − (n² − 1) = 8` would need `n² = 7`. The mirror of
`no_orthogonal_quotient_of_dim_six`: the Wolf space is not `G₂/SU(n)` for any `n`. -/
theorem no_unitary_quotient_of_dim_eight (n : ℕ) : dimG2 - dimSU n ≠ 8 := by
  unfold dimG2 dimSU
  intro h
  rcases le_or_gt n 3 with h3 | h4
  · revert h; interval_cases n <;> decide
  · have h16 : 16 ≤ n ^ 2 := by
      have := Nat.pow_le_pow_left h4 2
      norm_num at this
      exact this
    generalize n ^ 2 = A at h h16
    omega

/-- **`𝔰𝔬(4) ≅ 𝔰𝔲(2) ⊕ 𝔰𝔲(2)` at the level of dimensions, and only at `n = 4`.**
`C(n,2) = 3 + 3` iff `n = 4`. This is where the tetraplectic `SU(2)` of
`lem:bring-cone-reeb-quaternionic-twist` enters `G₂`. -/
theorem so_dim_eq_two_su2_iff (n : ℕ) : dimSO n = dimSU 2 + dimSU 2 ↔ n = 4 := by
  have h6 : dimSU 2 + dimSU 2 = 6 := by decide
  rw [h6]
  unfold dimSO
  constructor
  · intro h
    rcases le_or_gt n 4 with h4 | h5
    · interval_cases n <;> revert h <;> decide
    · exfalso
      have h10 : 10 ≤ n.choose 2 := le_trans (by decide) (Nat.choose_mono 2 h5)
      omega
  · rintro rfl; decide

/-! ## 4. The degree tie: a rank-3 object has exactly one non-trivial volume form -/

/-- **`Λᵏ` of a 3-dimensional object is a line iff `k = 0` or `k = 3`.**
`C(3,k) = 1 ↔ k ∈ {0,3}`. So `Λ³W ≅ 𝟙` is the *only* non-trivial volume form a
rank-3 object admits — the degree-3 half of the dichotomy in
`QOU.QuantumObservableUniverse.VolumeFormDegree`, at the dimension the
`G₂/SU(3)` isotropy supplies (`6 = 2 · 3` real, i.e. complex 3). -/
theorem choose_three_eq_one_iff (k : ℕ) : Nat.choose 3 k = 1 ↔ k = 0 ∨ k = 3 := by
  constructor
  · intro h
    rcases le_or_gt k 3 with h3 | h4
    · interval_cases k <;> revert h <;> decide
    · rw [Nat.choose_eq_zero_of_lt h4] at h
      exact absurd h (by decide)
  · rintro (rfl | rfl) <;> decide

end QOU.Eightfold.G2Frame
