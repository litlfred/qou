/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Tactic

/-!
# Where does the `−12 m_e` in the proton identity come from?

Production identity (convention D, `computations/m_p_substrate_identity_50dps.py`):

    m_p / m_e = 2 · (Vol(4₁)/ℏ_q²) · F_Bor(q) − 12,
    F_Bor(q)  = tr_M(β_Bor) · [3]_q! / q³,        m_μ = m_e · Vol(4₁)/ℏ_q²,  ℏ_q = 1 − q⁻¹,

with `β_Bor = (σ₀σ₁⁻¹)³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)` for the ruled photon
`γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`. The `12` was selected against `m_p`
(owner label 2026-11-18). This file records what the framework does and does not
fix about it. Everything here is algebra over a field of characteristic zero; no
empirical number enters.

## Results

* `fBor_one`: `F_Bor(1) = 6`, so `12 = 2·F_Bor(1)`.
* `fE_one`: the electron word `σ₀σ₁σ₀` (ruling 2026-11-21) has `F_e(1) = 3`, so
  also `12 = 4·F_e(1)`. `trMe_closed` gives its convention-D trace
  `q³(q⁴+1)/(q²+1)²`.
* `twelve_readings`: `12 = 2·F_Bor(1) = 4·F_e(1) = 2·|S₃|`. Several structural
  integers give the same value, so the value alone does not select one.
* `identity_in_tower_scale`: in the tower's own scale the identity is
  `m_p = 2 m_μ (F_Bor(q) − ℏ_q²·F_Bor(1)/Vol)`. The subtracted piece is an
  `O(ℏ_q²)` term that carries `1/Vol`. `F_Bor` is a rational function of `q`
  with no `Vol` in it, so the `−12` is not a correction to the Borromean
  observable; it is a separate term at the electron scale `m_e`.
* `tower_has_double_pole`: `ℏ_1 = 0` while `ℏ_q²·T(q)/m_e = 2 Vol F_Bor(q)`
  equals `12·Vol ≠ 0` at `q = 1`. So the tower has a pole of order 2 at the
  classical point and no finite classical limit. Reading the `12` as
  "subtract the classical limit of the same observable" fails: that limit is
  infinite. The `12` is the *coefficient* of the pole with `Vol` removed, and
  the removal of `Vol` (equivalently the change of scale `m_μ → m_e`) is the
  step nothing in the framework supplies.
* `reebSlot_one`: in the two-term Lagrangian trace with scale `m_e/ℏ_q²`, the
  only `ℏ`-free term is the Reeb square `ℏ_q²·τ(R∘R)`. Under the corpus
  hypothesis `τ(R_p∘R_p) = q·tr(V³_A)` (`CategoricalLagrangianTwoTermBridge`,
  `hReebP`) its value at `q = 1` is `−3`, not `−12`.

Scope (AGENTS.md (a)/(b)): `tower_has_double_pole` is a (b) exclusion of the
"classical limit of the tower" reading, by the pole-order invariant. The other
negatives are (a): they concern the named candidates only.
-/

namespace QOU.MassTheory.ProtonTwelveOrigin

variable {K : Type*} [Field K] [CharZero K]

/-- `h = q − q⁻¹`. -/
def hq (q : K) : K := q - q⁻¹

/-- `ℏ_q = 1 − q⁻¹`. -/
def hbar (q : K) : K := 1 - q⁻¹

/-- The Lean-proved Borromean Markov trace, convention D
(`BorromeanMarkovTrace.lean`, `PoincareCenteringOfQ3.trMBorromean`). -/
def trMBor (q : K) : K :=
  (4 + hq q ^ 2 - 3 * hq q ^ 4 - hq q ^ 6) / (hq q ^ 2 + 4)

/-- Balanced `[3]_q! = (q² + 1 + q⁻²)(q + q⁻¹)`. -/
def qFact3 (q : K) : K := (q ^ 2 + 1 + q⁻¹ ^ 2) * (q + q⁻¹)

/-- `F_Bor(q) = tr_M(β_Bor)·[3]_q!/q³`. -/
def fBor (q : K) : K := trMBor q * qFact3 q / q ^ 3

/-- Convention-D Ocneanu parameter `z_D = q³/(q²+1)`. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- Ocneanu trace of the electron word: `tr(σ₀σ₁σ₀) = tr(σ₀²σ₁) = z(hz + 1)`. -/
def trMe (q : K) : K := zD q * (hq q * zD q + 1)

/-- `F_e(q) = tr_M(σ₀σ₁σ₀)·[3]_q!/q³`, the electron analogue of `F_Bor`. -/
def fE (q : K) : K := trMe q * qFact3 q / q ^ 3

/-- Closed form of `tr(V³_A)` on the proton weight space
(`NucleonWeightSpaceTraces.trace_borromeanV3A`). -/
def trV3A (q : K) : K :=
  (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6

/-- The Reeb-square slot of the two-term Lagrangian trace under `hReebP`. -/
def reebSlot (q : K) : K := q * trV3A q

omit [CharZero K] in
theorem hq_one : hq (1 : K) = 0 := by simp [hq]

omit [CharZero K] in
theorem hbar_one : hbar (1 : K) = 0 := by simp [hbar]

/-- **`F_Bor(1) = 6`.** -/
theorem fBor_one : fBor (1 : K) = 6 := by
  simp only [fBor, trMBor, qFact3, hq_one]
  norm_num

omit [CharZero K] in
/-- **The electron trace in convention D** is `q³(q⁴+1)/(q²+1)²`. -/
theorem trMe_closed (q : K) (hq0 : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) :
    trMe q = q ^ 3 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  simp only [trMe, zD, hq]
  field_simp
  ring

/-- **`F_e(1) = 3`.** -/
theorem fE_one : fE (1 : K) = 3 := by
  simp only [fE, trMe, zD, qFact3, hq_one]
  norm_num

/-- **Three readings of the same integer.** -/
theorem twelve_readings :
    2 * fBor (1 : K) = 12 ∧ 4 * fE (1 : K) = 12 ∧
      2 * Fintype.card (Equiv.Perm (Fin 3)) = 12 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [fBor_one]; norm_num
  · rw [fE_one]; norm_num
  · rw [Fintype.card_perm, Fintype.card_fin]; decide

/-- **The identity in the tower's own scale.** With `m_μ = m_e·Vol/ℏ_q²`,
`2 m_μ F_Bor(q) − 12 m_e = 2 m_μ (F_Bor(q) − ℏ_q²·F_Bor(1)/Vol)`. -/
theorem identity_in_tower_scale (q me vol : K) (hv : vol ≠ 0) (hh : hbar q ≠ 0) :
    2 * (me * vol / hbar q ^ 2) * fBor q - 12 * me =
      2 * (me * vol / hbar q ^ 2) * (fBor q - hbar q ^ 2 * fBor 1 / vol) := by
  rw [fBor_one]
  field_simp
  ring

/-- **The tower has a double pole at the classical point.** `ℏ_q` vanishes at
`q = 1` while `ℏ_q²·(tower/m_e) = 2·Vol·F_Bor(q)` equals `12·Vol`, which is
nonzero for `Vol ≠ 0`. -/
theorem tower_has_double_pole (vol : K) (hv : vol ≠ 0) :
    hbar (1 : K) = 0 ∧ 2 * vol * fBor (1 : K) = 12 * vol ∧ 12 * vol ≠ 0 := by
  refine ⟨hbar_one, ?_, ?_⟩
  · rw [fBor_one]; ring
  · exact mul_ne_zero (by norm_num) hv

/-- **The Reeb-square slot is `−3` at `q = 1`, not `−12`.** -/
theorem reebSlot_one : reebSlot (1 : K) = -3 := by
  simp only [reebSlot, trV3A]
  norm_num

theorem reebSlot_one_ne_neg_twelve : reebSlot (1 : K) ≠ -12 := by
  rw [reebSlot_one]; norm_num

/-! ## The Reeb-square slot as the `−12`

For the Reeb square to *be* the `−12 m_e` term, `τ(R_p∘R_p)` must be `−12` for
every `q`. Two statements follow. (1) The corpus hypothesis `hReebP` cannot play
that role at any normalisation, because `q·tr(V³_A)` is not constant. (2) If the
Reeb generator acts as a circle action of integer weight `k` (`R∘R = −k²·𝟙`), the
trace is `−k²·dim`; on the 3-dimensional proton weight space that `hReebP` traces
over, `−12` forces `k = ±2`, while with a normalised trace (`τ(𝟙) = 1`) no integer
weight gives `−12`. So the `−12` reduces to "the proton's Reeb weight is 2", which
nothing in the corpus fixes. That is a reduction, not a derivation. -/

/-- `q·tr(V³_A)` takes different values at `q = 1` and `q = 2`. -/
theorem reebSlot_one_ne_two : reebSlot (1 : K) ≠ reebSlot 2 := by
  simp only [reebSlot, trV3A]
  norm_num

/-- **`hReebP` cannot be a constant term**: no constant equals `q·tr(V³_A)` for
all `q`. Scope (b) for the `hReebP` reading of the `−12`: a nonconstant function
of `q` is not a constant. -/
theorem reebSlot_not_constant : ¬ ∃ c : K, ∀ q : K, reebSlot q = c := by
  rintro ⟨c, hc⟩
  exact reebSlot_one_ne_two (by rw [hc 1, hc 2])

omit [CharZero K] in
/-- A scalar Reeb square has trace `c·n` on an `n`-dimensional space. -/
theorem trace_scalar_square {n : ℕ} (R : Matrix (Fin n) (Fin n) K) (c : K)
    (hR : R * R = c • (1 : Matrix (Fin n) (Fin n) K)) :
    Matrix.trace (R * R) = c * n := by
  rw [hR, Matrix.trace_smul, Matrix.trace_one, Fintype.card_fin, smul_eq_mul]

/-- **On the 3-dimensional proton weight space, `−12` forces Reeb weight `±2`.** -/
theorem weight_space_weight_eq_two (k : ℤ) :
    -((k : ℚ) ^ 2) * 3 = -12 ↔ k = 2 ∨ k = -2 := by
  constructor
  · intro h
    have h4 : (k : ℚ) ^ 2 = 4 := by linarith
    have : k ^ 2 = 4 := by exact_mod_cast h4
    have : (k - 2) * (k + 2) = 0 := by ring_nf; linarith
    rcases mul_eq_zero.mp this with h | h
    · left; linarith
    · right; linarith
  · rintro (rfl | rfl) <;> norm_num

/-- **With a normalised trace (`τ(𝟙) = 1`) no integer Reeb weight gives `−12`.** -/
theorem normalised_no_integer_weight (k : ℤ) : -(k ^ 2) ≠ (-12 : ℤ) := by
  intro h
  have h12 : k ^ 2 = 12 := by linarith
  have hk : k.natAbs ^ 2 = 12 := by
    have := congrArg Int.natAbs h12
    simpa [Int.natAbs_pow] using this
  have hle : k.natAbs ≤ 3 := by nlinarith
  interval_cases (k.natAbs) <;> omega

end QOU.MassTheory.ProtonTwelveOrigin
