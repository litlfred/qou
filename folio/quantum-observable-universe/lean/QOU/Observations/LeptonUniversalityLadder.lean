/-
# The lepton-universality ladder `Δ, Δ³, Δ⁵` and its ring masses

Thread "Derive the tau lepton's word" (2026-11-27). Writeup:
`docs/audits/2026-11-27-tau-lepton-word.md`.

The electron is the half twist `Δ = σ₀σ₁σ₀ ∈ B₃` (owner ruling 2026-11-21, Hopf closure). No
rule in the corpus said what the muon and tau words are on three strands. This file records the
rule the owner chose on 2026-11-27 (card "Universality ladder Δ, Δ3, Δ5"; a working conjecture,
`docs/coordination/owner-rulings.md`) and what it gives.

**The rule (lepton universality).** Every generation couples to the photon generators exactly as
the electron does. Read as a statement about conjugation, a word `β` couples like `Δ` when
`β σ₀ = σ₁ β` and `β σ₁ = σ₀ β`, as `Δ` does. Then `Δ⁻¹β` commutes with `σ₀` and `σ₁`, so it lies in
the centre of `B₃`, which is `⟨Δ²⟩` (Chow 1948; cited, not formalised here). So the charged leptons
are `Δ^{2k+1}`: `e = Δ`, `μ = Δ³`, `τ = Δ⁵`.

What is proved here, over any monoid with the braid relation and any field:

* `delta_swap_left`, `delta_swap_right`: `Δ σ₀ = σ₁ Δ` and `Δ σ₁ = σ₀ Δ`.
* `deltaSq_comm_left`, `deltaSq_comm_right`: `Δ²` commutes with both generators.
* `ladder_swap_left`, `ladder_swap_right`: every `Δ^{2k+1}` couples exactly like `Δ`
  (the forward direction of the rule).
* `ladder_components`: every rung closes to a two-component link (same charge class as `e`).
* `rho21_delta`: in the two-dimensional Hecke representation used by the ring mass,
  `ρ(Δ) = [[0, −1], [−1, 0]]`, independent of `q`. So `ρ(Δ)² = 1` and `tr ρ(Δ^{2k+1}) = 0`.
* `ladderMass_eq`: the ring mass (`def:mass-identity`, convention D, three strands, writhe
  `3(2k+1)`) of `Δ^{2k+1}` is `[4]/q³ · q^{−6k}`. The electron row `k = 0` is `[4]/q³`.
* `ladderMass_succ`: each rung is the previous one times `q⁻⁶`.
* `ladderMass_strictAnti`: for `q > 1` the ladder gets strictly lighter.

**Reading.** This is a scope-(b) statement with its invariant named: centrality of `Δ²` makes the
mass ratio a pure power `q^{−6k}`, so on the ring chart no word of this ladder is heavier than the
electron. If the rule is right, the lepton hierarchy has to come from the mass map, not from the
word. No measured value enters.
-/
import QOU.Observations.RingMassLinkingNumber
import QOU.BraidsAndKnots.ElectronWordCandidates

namespace QOU.Observations.LeptonUniversalityLadder

open QOU.Observations.ElectronRingMassReading

/-! ### 1. The half twist and the centre (any monoid with the braid relation) -/

section Monoid

variable {M : Type*} [Monoid M] (a b : M)

/-- The half twist `Δ = σ₀σ₁σ₀`. -/
def delta : M := a * b * a

variable {a b}

theorem delta_swap_left (hbr : a * b * a = b * a * b) : delta a b * a = b * delta a b := by
  unfold delta
  calc a * b * a * a = (a * b * a) * a := rfl
    _ = (b * a * b) * a := by rw [hbr]
    _ = b * (a * b * a) := by simp only [mul_assoc]

theorem delta_swap_right (hbr : a * b * a = b * a * b) : delta a b * b = a * delta a b := by
  unfold delta
  calc a * b * a * b = a * (b * a * b) := by simp only [mul_assoc]
    _ = a * (a * b * a) := by rw [hbr]

/-- `Δ²` commutes with `σ₀`. -/
theorem deltaSq_comm_left (hbr : a * b * a = b * a * b) :
    delta a b ^ 2 * a = a * delta a b ^ 2 := by
  rw [sq, mul_assoc, delta_swap_left hbr, ← mul_assoc, delta_swap_right hbr, mul_assoc]

/-- `Δ²` commutes with `σ₁`. -/
theorem deltaSq_comm_right (hbr : a * b * a = b * a * b) :
    delta a b ^ 2 * b = b * delta a b ^ 2 := by
  rw [sq, mul_assoc, delta_swap_right hbr, ← mul_assoc, delta_swap_left hbr, mul_assoc]

theorem deltaSq_pow_comm_left (hbr : a * b * a = b * a * b) (k : ℕ) :
    (delta a b ^ 2) ^ k * a = a * (delta a b ^ 2) ^ k := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, mul_assoc, deltaSq_comm_left hbr, ← mul_assoc, ih, mul_assoc]

theorem deltaSq_pow_comm_right (hbr : a * b * a = b * a * b) (k : ℕ) :
    (delta a b ^ 2) ^ k * b = b * (delta a b ^ 2) ^ k := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, mul_assoc, deltaSq_comm_right hbr, ← mul_assoc, ih, mul_assoc]

/-- The ladder word `Δ^{2k+1} = Δ · (Δ²)^k`. -/
def ladder (a b : M) (k : ℕ) : M := delta a b * (delta a b ^ 2) ^ k

/-- **Every rung couples to `σ₀` exactly like the electron.** -/
theorem ladder_swap_left (hbr : a * b * a = b * a * b) (k : ℕ) :
    ladder a b k * a = b * ladder a b k := by
  unfold ladder
  rw [mul_assoc, deltaSq_pow_comm_left hbr, ← mul_assoc, delta_swap_left hbr, mul_assoc]

/-- **Every rung couples to `σ₁` exactly like the electron.** -/
theorem ladder_swap_right (hbr : a * b * a = b * a * b) (k : ℕ) :
    ladder a b k * b = a * ladder a b k := by
  unfold ladder
  rw [mul_assoc, deltaSq_pow_comm_right hbr, ← mul_assoc, delta_swap_right hbr, mul_assoc]

theorem ladder_eq_pow (k : ℕ) : ladder a b k = delta a b ^ (2 * k + 1) := by
  unfold ladder
  rw [← pow_mul, pow_succ, mul_comm (delta a b ^ (2 * k)) (delta a b), ← pow_succ']
  rw [pow_succ']

end Monoid

/-! ### 2. Closure components -/

open QOU.BraidKnot.ElectronWordCandidates in
/-- The letters of `Δ^{2k+1}`: `[0, 1, 0]` repeated `2k+1` times. -/
def ladderLetters (k : ℕ) : List (Fin 2) := (List.replicate (2 * k + 1) [0, 1, 0]).flatten

open QOU.BraidKnot.ElectronWordCandidates in
/-- **Every rung closes to a two-component link**, like the electron's Hopf link. -/
theorem ladder_components (k : ℕ) : numCycles (permOf (ladderLetters k)) = 2 := by
  apply numCycles_permOf_of_odd
  have hlen : (ladderLetters k).length = 3 * (2 * k + 1) := by
    unfold ladderLetters
    rw [List.length_flatten]
    simp [List.map_replicate, List.sum_replicate]
    ring
  rw [hlen]
  omega

/-! ### 3. The ring mass of the ladder -/

section Field

variable {R : Type*} [Field R]

/-- The image of `σ₀` in the two-dimensional Hecke representation (eigenvalues `q`, `−q⁻¹`),
as in `computations/probes/electron_weight/ring_mass_braid_words_probe.py`. -/
def rhoA (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, 1; 0, -q⁻¹]

/-- The image of `σ₁`. -/
def rhoB (q : R) : Matrix (Fin 2) (Fin 2) R := !![-q⁻¹, 0; 1, q]

/-- The constant matrix `[[0, −1], [−1, 0]]`. -/
def swapNeg : Matrix (Fin 2) (Fin 2) R := !![0, -1; -1, 0]

/-- **`ρ(Δ) = [[0, −1], [−1, 0]]` for every `q ≠ 0`.** -/
theorem rho21_delta (q : R) (hq : q ≠ 0) : rhoA q * rhoB q * rhoA q = swapNeg := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rhoA, rhoB, swapNeg, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- The braid relation holds in this representation. -/
theorem rho21_braid (q : R) (hq : q ≠ 0) :
    rhoA q * rhoB q * rhoA q = rhoB q * rhoA q * rhoB q := by
  rw [rho21_delta q hq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rhoA, rhoB, swapNeg, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem swapNeg_sq : (swapNeg : Matrix (Fin 2) (Fin 2) R) ^ 2 = 1 := by
  rw [sq]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [swapNeg, Matrix.mul_apply, Fin.sum_univ_two]

theorem swapNeg_pow_odd (k : ℕ) : (swapNeg : Matrix (Fin 2) (Fin 2) R) ^ (2 * k + 1) = swapNeg := by
  rw [pow_succ, pow_mul, swapNeg_sq, one_pow, one_mul]

theorem trace_swapNeg : Matrix.trace (swapNeg : Matrix (Fin 2) (Fin 2) R) = 0 := by
  simp [swapNeg, Matrix.trace, Fin.sum_univ_two]

/-- **`tr ρ(Δ^{2k+1}) = 0`.** -/
theorem trace_rho_ladder (q : R) (hq : q ≠ 0) (k : ℕ) :
    Matrix.trace ((rhoA q * rhoB q * rhoA q) ^ (2 * k + 1)) = 0 := by
  rw [rho21_delta q hq, swapNeg_pow_odd, trace_swapNeg]

/-- The ring mass of `Δ^{2k+1}` (`def:mass-identity`, convention D, `n = 3`, writhe
`w = 3(2k+1)`): `[2]³ q^{−2w} (y₍₃₎ q^w + y₍₂₁₎ tr ρ(β))`, with `y₍₃₎ = 1 − 2/[2]²` and
`y₍₂₁₎ = 1/[2]²`, exactly as in the probe. -/
def ladderMass (q : R) (k : ℕ) : R :=
  (q + q⁻¹) ^ 3 * q⁻¹ ^ (2 * (3 * (2 * k + 1))) *
    ((1 - 2 / (q + q⁻¹) ^ 2) * q ^ (3 * (2 * k + 1)) +
      1 / (q + q⁻¹) ^ 2 * Matrix.trace ((rhoA q * rhoB q * rhoA q) ^ (2 * k + 1)))

/-- **The ring mass of `Δ^{2k+1}` is `[4]/q³ · q^{−6k}`.** -/
theorem ladderMass_eq (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (k : ℕ) :
    ladderMass q k = qInt4 q / q ^ 3 * q⁻¹ ^ (6 * k) := by
  have hs : q + q⁻¹ ≠ 0 := by
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this]; exact div_ne_zero h2 hq
  unfold ladderMass
  rw [trace_rho_ladder q hq, mul_zero, add_zero]
  have e1 : q⁻¹ ^ (2 * (3 * (2 * k + 1))) = q⁻¹ ^ 6 * (q⁻¹ ^ (6 * k)) ^ 2 := by
    rw [← pow_mul, ← pow_add]; congr 1; ring
  have e2 : q ^ (3 * (2 * k + 1)) = q ^ 3 * q ^ (6 * k) := by
    rw [← pow_add]; congr 1; ring
  rw [e1, e2]
  have hk : q ^ (6 * k) * q⁻¹ ^ (6 * k) = 1 := by
    rw [← mul_pow, mul_inv_cancel₀ hq, one_pow]
  have hk' : q⁻¹ ^ (6 * k) ≠ 0 := pow_ne_zero _ (inv_ne_zero hq)
  unfold qInt4
  field_simp
  have : q ^ (6 * k) = (q⁻¹ ^ (6 * k))⁻¹ := by rw [inv_pow, inv_inv]
  rw [this]
  field_simp
  ring

/-- The electron row: `m(Δ) = [4]/q³`. -/
theorem ladderMass_zero (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ladderMass q 0 = qInt4 q / q ^ 3 := by
  rw [ladderMass_eq q hq h2]; simp

/-- **Each rung is the previous one times `q⁻⁶`.** -/
theorem ladderMass_succ (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (k : ℕ) :
    ladderMass q (k + 1) = ladderMass q k * q⁻¹ ^ 6 := by
  rw [ladderMass_eq q hq h2, ladderMass_eq q hq h2, mul_assoc, ← pow_add]
  congr 2

/-- At `q = 1` every rung has the electron's mass `4`. -/
theorem ladderMass_one [CharZero R] (k : ℕ) : ladderMass (1 : R) k = 4 := by
  rw [ladderMass_eq (1 : R) one_ne_zero (by norm_num)]
  unfold qInt4; norm_num

end Field

/-- **For `q > 1` the ladder gets strictly lighter: `m(Δ^{2k+3}) < m(Δ^{2k+1})`.** -/
theorem ladderMass_strictAnti {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq1 : 1 < q) (k : ℕ) :
    ladderMass q (k + 1) < ladderMass q k := by
  have hq : (0 : R) < q := lt_trans zero_lt_one hq1
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  rw [ladderMass_succ q hq.ne' h2]
  have hpos : 0 < ladderMass q k := by
    rw [ladderMass_eq q hq.ne' h2]
    unfold qInt4
    positivity
  have hlt : q⁻¹ ^ 6 < 1 := by
    apply pow_lt_one₀ (by positivity) (inv_lt_one_of_one_lt₀ hq1) (by norm_num)
  calc ladderMass q k * q⁻¹ ^ 6 < ladderMass q k * 1 := by
        exact mul_lt_mul_of_pos_left hlt hpos
    _ = ladderMass q k := mul_one _

end QOU.Observations.LeptonUniversalityLadder
