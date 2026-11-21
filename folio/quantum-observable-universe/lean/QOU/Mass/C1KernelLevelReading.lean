import Mathlib.Tactic
import QOU.Mathlib.RamifiedShiftCalculusSum
import QOU.Mass.QDifferenceConfluentObstruction

/-!
# QOU.Mass.C1KernelLevelReading — `L_K` is a recurrence on the residue tower, level by level

`conj:qdifference-kernel-prolongation-symbol` writes its carrier as
`[m+2]_q b_{m+2} = b_{m+1} + b_m` with `x = q^m`, and `m` there is the **body order**,
which `prop:sw-period-residue-sum` identifies with the **jet degree**
(`prop:binding-genfun-qdifference`: `G(x;q) = Σ_n B_n x^n` in body order `n`). So the
operator `L_K = (q²x − 1)σ² − (q−1)σ − (q−1)` is a *second-order recurrence in the
level* — the relation that the level-indexed sequence of residues of the jet tower,

  `r_n := (Dⁿ X)(−2)`   (the period of the `n`-th prolonged differential at the pole),

must satisfy. `D : Jⁿ → Jⁿ⁺¹` is first-order in the level, so `L_K` is never `D` itself.

`C1KernelAsShiftSum` (#6582) and `C1KernelDictionaryParity` (#6610) read `σ` instead as
a shift in the **`t`-exponent** of a single jet. That is the pure-shift-1 special case —
for a tower `X ↦ c·X(· + 1)` the level index and the `t`-exponent lock together,
`r_n = cⁿ a_{n−2}` (`shiftOne_const_residueSeq`) — not the conjecture's reading. Their
theorems stand as mathematics about those `t`-operators; this module re-derives what the
conjecture actually asks on the correct axis.

## What is proved

* `residueSeq_zero_of_powerSeries`: on a power-series seed the level-`0` residue is `0`,
  for **every** operator. So the residue tower can never equal a carrier with
  `b_0 ≠ 0` (the involution-number carrier has `b_0 = b_1 = 1`) — the body-order index
  and the jet level are offset, or the recurrence is demanded only from a level on.
* `c1RecFrom_ext`: a level-`n₀` C1 sequence is fixed by its two values at `n₀`, `n₀+1`
  (rank `2`), for `q` not a root of unity — the conjecture's own "needs two base cases".
* `c1Rec_zero_of_init_zero`: two zero initial values force the zero sequence.
* `twoOp_residueSeq_one`: for the admissible two-term operator the level-`1` residue is
  `c₂(−2) · a₀` — it reads the branch value with the shift-2 weight at the residue slot.
* `derivativeLike_twoOp_c1Rec_zero`: a **derivative-like** shift-2 term (`c₂(−2) = 0`)
  therefore has `r_0 = r_1 = 0`, and if its residues satisfy C1 from level `0` they are
  all zero. That is #6582's conclusion — the prolongation needs a non-derivative
  component — re-derived on the level axis, with the invariant named: the first two
  residues of a derivative-like tower vanish and C1 is homogeneous of order `2`.
* `twoOp_c1RecFrom_two_iff`: for the derivative-only two-term operator, C1 **from level
  `2`** on the residues is *equivalent* to the index-shifted C1 recurrence
  `[m+4]_q s_{m+2} = s_{m+1} + s_m` on the tower's `t¹`-coefficients
  `s_m := (Dᵐ X)(1)` (via #6498's `twoOp_iterate_residue`, `r_{m+2} = κ s_m`,
  `κ = c₁(−2) c₂(−1) ≠ 0`). So on the level axis the symbol identification is a
  concrete constraint on the tower, not on `D`'s shape: which `(c₁, c₂, X)` make the
  `t¹`-coefficient sequence C1.

Nothing here constructs `D_q` or decides the conjecture.

## References

- [leitner2026] mass-theory/qdifference-kernel-prolongation-symbol
- [leitner2026] mass-theory/binding-genfun-qdifference
- [leitner2026] docs/audits/2026-09-04-c1-kernel-level-reading.md

LaTeX label: (library module — no content block)
-/

namespace QOU.Mass.C1KernelLevelReading

open QOU.Mathlib.RamifiedShiftCalculus QOU.Mathlib.RamifiedShiftCalculusSum
  QOU.Mass.QDifferenceConfluentObstruction Finset

variable {K : Type*} [Field K]

/-- The residue tower of an operator `D` on a seed `X`: the `t⁻²` coefficient of the
level-`n` jet. -/
def residueSeq (D : (ℤ → K) → (ℤ → K)) (X : ℤ → K) (n : ℕ) : K := D^[n] X (-2)

/-- The C1 recurrence `[n+2]_q r_{n+2} = r_{n+1} + r_n` demanded from level `n₀` on,
in the geometric `q`-integer `qint`. -/
def C1RecFrom (q : K) (n₀ : ℕ) (r : ℕ → K) : Prop :=
  ∀ n, n₀ ≤ n → qint q (n + 2) * r (n + 2) = r (n + 1) + r n

/-! ## Generic facts about C1 sequences -/

/-- **Rank two.** Two C1-from-`n₀` sequences agreeing at `n₀` and `n₀ + 1` agree from
`n₀` on, for `q` not a root of unity. -/
theorem c1RecFrom_ext (q : K) (hq : ∀ n, qint q (n + 2) ≠ 0) (n₀ : ℕ) (r s : ℕ → K)
    (hr : C1RecFrom q n₀ r) (hs : C1RecFrom q n₀ s)
    (h0 : r n₀ = s n₀) (h1 : r (n₀ + 1) = s (n₀ + 1)) (k : ℕ) :
    r (n₀ + k) = s (n₀ + k) := by
  have key : ∀ k, r (n₀ + k) = s (n₀ + k) ∧ r (n₀ + k + 1) = s (n₀ + k + 1) := by
    intro k
    induction k with
    | zero => exact ⟨by simpa using h0, by simpa using h1⟩
    | succ k ih =>
      refine ⟨ih.2, ?_⟩
      have hr' := hr (n₀ + k) (Nat.le_add_right _ _)
      have hs' := hs (n₀ + k) (Nat.le_add_right _ _)
      rw [ih.1, ih.2] at hr'
      have : qint q (n₀ + k + 2) * r (n₀ + k + 2) = qint q (n₀ + k + 2) * s (n₀ + k + 2) := by
        rw [hr', hs']
      have h2 := mul_left_cancel₀ (hq (n₀ + k)) this
      simpa [Nat.add_assoc] using h2
  exact (key k).1

/-- Two zero initial values force the zero sequence. -/
theorem c1Rec_zero_of_init_zero (q : K) (hq : ∀ n, qint q (n + 2) ≠ 0) (r : ℕ → K)
    (hr : C1RecFrom q 0 r) (h0 : r 0 = 0) (h1 : r 1 = 0) (n : ℕ) : r n = 0 := by
  have := c1RecFrom_ext q hq 0 r (fun _ => 0) hr (fun _ _ => by simp) (by simpa using h0)
    (by simpa using h1) n
  simpa using this

/-! ## The residue tower on a power-series seed -/

/-- The level-`0` residue vanishes on a power-series seed, for every operator. -/
theorem residueSeq_zero_of_powerSeries (D : (ℤ → K) → (ℤ → K)) (X : ℤ → K)
    (hX : PowerSeriesSupported X) : residueSeq D X 0 = 0 := by
  simp only [residueSeq, Function.iterate_zero, id_eq]
  exact hX (-2) (by norm_num)

/-- For the two-term operator the level-`1` residue reads the branch value through the
shift-2 weight at the residue slot: `c₂(−2) · a₀`. -/
theorem twoOp_residueSeq_one (c₁ c₂ : ℤ → K) (X : ℤ → K) (hX : PowerSeriesSupported X) :
    residueSeq (twoOp c₁ c₂) X 1 = c₂ (-2) * X 0 := by
  simp only [residueSeq, Function.iterate_one, twoOp_apply]
  have h := hX (-1) (by norm_num)
  norm_num [h]

/-- **A derivative-like shift-2 term cannot carry C1 from level `0`.** With `c₂(−2) = 0`
the first two residues vanish, so a C1 residue tower is identically zero. -/
theorem derivativeLike_twoOp_c1Rec_zero (q : K) (hq : ∀ n, qint q (n + 2) ≠ 0)
    (c₁ c₂ : ℤ → K) (hc₂ : AnnihilatesConstants 2 c₂) (X : ℤ → K)
    (hX : PowerSeriesSupported X) (hr : C1RecFrom q 0 (residueSeq (twoOp c₁ c₂) X))
    (n : ℕ) : residueSeq (twoOp c₁ c₂) X n = 0 := by
  apply c1Rec_zero_of_init_zero q hq _ hr (residueSeq_zero_of_powerSeries _ _ hX)
  rw [twoOp_residueSeq_one c₁ c₂ X hX]
  have h2 : c₂ (-2) = 0 := hc₂
  rw [h2, zero_mul]

/-! ## C1 from level `2` on a derivative-only tower is C1 on its `t¹`-coefficients -/

/-- The `t¹`-coefficient sequence of the tower. -/
def coeffOneSeq (D : (ℤ → K) → (ℤ → K)) (X : ℤ → K) (n : ℕ) : K := D^[n] X 1

/-- #6498's residue formula in tower language: `r_{n+2} = κ · s_n`. -/
theorem twoOp_residueSeq_add_two (c₁ c₂ : ℤ → K) (hc₁ : AnnihilatesConstants 1 c₁)
    (hc₂ : AnnihilatesConstants 2 c₂) (X : ℤ → K) (n : ℕ) :
    residueSeq (twoOp c₁ c₂) X (n + 2) = c₁ (-2) * c₂ (-1) * coeffOneSeq (twoOp c₁ c₂) X n :=
  twoOp_iterate_residue c₁ c₂ hc₁ hc₂ X n

/-- **C1 on the residues from level `2` ⇔ index-shifted C1 on the `t¹`-coefficients**,
for a derivative-only two-term tower with `κ = c₁(−2) c₂(−1) ≠ 0`. -/
theorem twoOp_c1RecFrom_two_iff (q : K) (c₁ c₂ : ℤ → K) (hc₁ : AnnihilatesConstants 1 c₁)
    (hc₂ : AnnihilatesConstants 2 c₂) (hκ : c₁ (-2) * c₂ (-1) ≠ 0) (X : ℤ → K) :
    C1RecFrom q 2 (residueSeq (twoOp c₁ c₂) X)
      ↔ ∀ m, qint q (m + 4) * coeffOneSeq (twoOp c₁ c₂) X (m + 2)
          = coeffOneSeq (twoOp c₁ c₂) X (m + 1) + coeffOneSeq (twoOp c₁ c₂) X m := by
  constructor
  · intro h m
    have hm := h (m + 2) (by omega)
    rw [show m + 2 + 2 = (m + 2) + 2 by ring, show m + 2 + 1 = (m + 1) + 2 by ring,
      twoOp_residueSeq_add_two c₁ c₂ hc₁ hc₂, twoOp_residueSeq_add_two c₁ c₂ hc₁ hc₂,
      twoOp_residueSeq_add_two c₁ c₂ hc₁ hc₂] at hm
    apply mul_left_cancel₀ hκ
    rw [show m + 2 + 2 = m + 4 by ring] at hm
    linear_combination hm
  · intro h n hn
    obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hn
    rw [show 2 + m + 2 = (m + 2) + 2 by ring, show 2 + m + 1 = (m + 1) + 2 by ring,
      show 2 + m = m + 2 by ring, twoOp_residueSeq_add_two c₁ c₂ hc₁ hc₂,
      twoOp_residueSeq_add_two c₁ c₂ hc₁ hc₂, twoOp_residueSeq_add_two c₁ c₂ hc₁ hc₂]
    have hm := h m
    rw [show m + 2 + 2 = m + 4 by ring]
    linear_combination (c₁ (-2) * c₂ (-1)) * hm

/-! ## The locked case: a pure shift-1 tower ties level to `t`-exponent -/

/-- For a constant-weight pure shift-1 tower the level index and the `t`-exponent lock:
`r_n = cⁿ · a_{n−2}`. This is the sense in which the `t`-shift reading of #6582/#6610 is
a special case of the level reading. -/
theorem shiftOne_const_residueSeq (c : K) (X : ℤ → K) (n : ℕ) :
    residueSeq (shiftOp 1 (fun _ => c)) X n = c ^ n * X (-2 + n) := by
  simp only [residueSeq]
  rw [shiftOp_iterate]
  simp

end QOU.Mass.C1KernelLevelReading
