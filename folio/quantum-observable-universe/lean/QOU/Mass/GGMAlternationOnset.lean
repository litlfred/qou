import Mathlib.Tactic

/-!
# QOU.Mass.GGMAlternationOnset — where the `(−1)^m` alternation of the GGM carrier can start

The Stokes carrier `𝒢` of `conj:c1-ggm-bar-parity-faces` is the three-term recurrence

  `y (m+2) = (2 − q^(m+1)) · y (m+1) − y m`.

Its sign pattern is the Door-v residual: the growing solution alternates as `(−1)^m`
*asymptotically*. The block's scope note says that while `2 − q^(m+1) > 0` "no sign change
occurs". That is not what the recurrence does — with a coefficient in `(0, 2)` it is
oscillatory, and every solution measured changes sign inside that window
(`computations/probes/door_v_residual_scope_probe.py`, six initial data, proton `q₀`).
What IS true, initial-data-independent, and what the block's argument actually needs:

* while the coefficient is **positive**, a sign flip is always followed by a same-sign
  pair (`no_double_flip_of_pos`) — strict `(−1)^m` alternation at two consecutive pairs is
  impossible for every solution;
* once the coefficient is **negative**, a same-sign pair is always followed by a flip
  (`flip_after_same_of_neg`), and a flip persists as soon as `|y m| < |c| · |y (m+1)|`
  (`flip_persists_of_lt`).

Consequence for the shift calculus: the full-alternation hypothesis of
`QOU.Mathlib.RamifiedShiftCalculusSum.twoOp_residual_kills_residue` (#6498) is
**unsatisfiable** by the GGM carrier at any `q < 2` (`ggm_full_alternation_impossible_of_lt_two`)
— it fails already at `m = 0`. The residual the corpus measures is the from-level-`n₀` form,
handled by `twoOp_residual_from_level_kills_residue_beyond`, and the coefficient threshold
`q^(m+1) < 2` (at the proton `q₀`: `m ≤ 5`) is a lower bound on `n₀`.

Ground ring: the sign statements need an ordered field, so per §7c this module sits on the
archimedean side of the wall — `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`.

## References

- [leitner2026] mass-theory/c1-ggm-bar-parity-faces (the block being re-scoped)
- [leitner2026] docs/audits/2026-09-03-door-v-residual-scope.md

LaTeX label: (library module — no content block)
-/

namespace QOU.Mass.GGMAlternationOnset

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- One step of the three-term recurrence `y (m+2) = c · y (m+1) − y m`. -/
def step (c a b : K) : K := c * b - a

/-- **Positive coefficient: a flip is followed by a same-sign pair.** -/
theorem no_double_flip_of_pos (c a b : K) (hc : 0 < c) (hab : a * b < 0) :
    0 < step c a b * b := by
  unfold step
  have h1 : 0 ≤ c * (b * b) := mul_nonneg hc.le (mul_self_nonneg b)
  nlinarith

/-- **Negative coefficient: a same-sign pair is followed by a flip.** -/
theorem flip_after_same_of_neg (c a b : K) (hc : c < 0) (hab : 0 < a * b) :
    step c a b * b < 0 := by
  unfold step
  have hb : b ≠ 0 := by rintro rfl; simp at hab
  have h1 : c * (b * b) < 0 := mul_neg_of_neg_of_pos hc (mul_self_pos.mpr hb)
  nlinarith

/-- **A flip persists once `|a| < −c · |b|`** (which itself forces `c < 0` and `b ≠ 0`). This
is why the strict alternation, once the growing solution dominates, never stops. -/
theorem flip_persists_of_lt (c a b : K) (hab : a * b < 0)
    (hlt : |a| < -c * |b|) : step c a b * b < 0 := by
  unfold step
  have hb2 : |b| * |b| = b * b := by rw [← abs_mul, abs_mul_self]
  have h1 : -(a * b) ≤ |a| * |b| := by rw [← abs_mul]; exact neg_le_abs _
  have hbpos : 0 < |b| := by
    rcases eq_or_ne b 0 with rfl | h
    · simp at hab
    · exact abs_pos.mpr h
  have h2 : |a| * |b| < -c * |b| * |b| := mul_lt_mul_of_pos_right hlt hbpos
  rw [mul_assoc, hb2] at h2
  nlinarith

/-! ## The GGM carrier -/

/-- The GGM coefficient `2 − q^(m+1)` at index `m`. -/
def ggmCoeff (q : K) (m : ℕ) : K := 2 - q ^ (m + 1)

theorem ggm_no_double_flip (q : K) (m : ℕ) (hq : q ^ (m + 1) < 2) (a b : K)
    (hab : a * b < 0) : 0 < step (ggmCoeff q m) a b * b :=
  no_double_flip_of_pos _ a b (by unfold ggmCoeff; linarith) hab

theorem ggm_flip_after_same (q : K) (m : ℕ) (hq : 2 < q ^ (m + 1)) (a b : K)
    (hab : 0 < a * b) : step (ggmCoeff q m) a b * b < 0 :=
  flip_after_same_of_neg _ a b (by unfold ggmCoeff; linarith) hab

/-- A solution of the GGM recurrence cannot flip at two consecutive pairs while the
coefficient is positive. -/
theorem ggm_solution_no_double_flip (q : K) (y : ℕ → K)
    (hy : ∀ m, y (m + 2) = step (ggmCoeff q m) (y m) (y (m + 1))) (m : ℕ)
    (hq : q ^ (m + 1) < 2) :
    ¬ (y m * y (m + 1) < 0 ∧ y (m + 2) * y (m + 1) < 0) := by
  rintro ⟨h1, h2⟩
  have := ggm_no_double_flip q m hq (y m) (y (m + 1)) h1
  rw [← hy m] at this
  exact absurd h2 (not_lt.mpr this.le)

/-- **Full `(−1)^m` alternation forces `2 ≤ q^(m+1)` at every `m`.** -/
theorem ggm_full_alternation_forces (q : K) (y : ℕ → K)
    (hy : ∀ m, y (m + 2) = step (ggmCoeff q m) (y m) (y (m + 1)))
    (halt : ∀ n, y n * y (n + 1) < 0) (m : ℕ) : 2 ≤ q ^ (m + 1) := by
  by_contra h
  push_neg at h
  exact ggm_solution_no_double_flip q y hy m h
    ⟨halt m, by rw [mul_comm]; exact halt (m + 1)⟩

/-- **At any `q < 2` — every physical substrate value — no solution of the GGM recurrence
alternates at every level.** The hypothesis of `twoOp_residual_kills_residue` cannot be
supplied by the corpus's Door-v carrier; only the from-level-`n₀` form can. -/
theorem ggm_full_alternation_impossible_of_lt_two (q : K) (hq : q < 2) (y : ℕ → K)
    (hy : ∀ m, y (m + 2) = step (ggmCoeff q m) (y m) (y (m + 1))) :
    ¬ ∀ n, y n * y (n + 1) < 0 := by
  intro halt
  have := ggm_full_alternation_forces q y hy halt 0
  rw [zero_add, pow_one] at this
  exact absurd hq (not_lt.mpr this)


/-- **Level-zero specialization of `ggm_no_double_flip` (`qou-0exp`).**
For `q ^ (0 + 1) < 2` and `a * b < 0`, `0 < step (ggmCoeff q 0) a b * b`. -/
theorem ggm_no_double_flip_zero (q : K) (hq : q ^ (0 + 1) < 2) (a b : K)
    (hab : a * b < 0) : 0 < step (ggmCoeff q 0) a b * b :=
  ggm_no_double_flip q 0 hq a b hab

end QOU.Mass.GGMAlternationOnset
