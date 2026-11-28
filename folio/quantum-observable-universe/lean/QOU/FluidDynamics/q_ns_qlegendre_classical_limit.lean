import QOU.FluidDynamics.q_ns_qlegendre_norm

/-!
# QOU.FluidDynamics.q_ns_qlegendre_classical_limit — the triad coupling at `q = 1`

Part A of `conj:regularity-breakdown` (beans `qou-pa7n`, `qou-q3dc`). The norm factor
`nf P z` of `q_ns_qlegendre_norm` is `0/0` at `P = 1`. Each difference `P^n − 1` equals
`(P − 1)[n]_P`, so the four factors of `P − 1` cancel and the factor equals a rational function
`nfc P k` whose denominator is a product of q-integers. That denominator does not vanish at `P = 1`.
The value at `q = 1` is therefore an evaluation, not a limit. No ε–δ argument is used.

## Results

* `nf_eq_nfc`: `nf P (P^k) = P^{2k+2}[k+1]⁴ / ([2k+1][2k+2]²[2k+3])` when `P` is not a
  root of unity.
* `coupling_raise_sq_eq_nfc`: the squared raising coupling of `q_ns_triad_raising_coupling`,
  divided by the two Haar norms, equals `Rc q s := (κ_s q⁻¹)² · nfc(q², s+1)`. That rational
  function is defined at every `q`, including `q = 1`.
* `Rc_one`: `Rc 1 s = (s+1)²(s+2)⁴ / ((2s+3)(2s+4)²(2s+5))`, the classical value.
* `Rc_one_ge`: over an ordered field, `Rc 1 s ≥ (s+1)²/16`. At `q = 1` the normalised squared
  coupling is unbounded in `s` (the amplitude grows linearly). At fixed `q > 1` it decays
  like `q^{−4s}` (closed form in `q_ns_qlegendre_norm`). So the triad transfer from mode `s+1`
  to `s+2` is not uniform in `q` as `q → 1⁺`.

All algebraic. No empirical value enters. Sorry-free.

## Not established

* A uniform-in-`q` statement on a neighbourhood of `q = 1` (continuity of `Rc` is evident from
  the formula, but not stated as a limit here).
* The factor `1/‖βδ‖²` of `C̃(r)²`, other velocity modes, and Part A itself.
-/

namespace QOU.FluidDynamics.QLegendreClassical

open Finset
open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2
open QOU.FluidDynamics.TriadRaising QOU.FluidDynamics.QLegendreNorm

variable {K : Type*} [Field K]

/-- The cancelled norm factor: `P^{2k+2}[k+1]⁴ / ([2k+1][2k+2]²[2k+3])`. -/
noncomputable def nfc (P : K) (k : ℕ) : K :=
  P ^ (2 * k + 2) * jk P (k + 1) ^ 4 /
    (jk P (2 * k + 1) * jk P (2 * k + 2) ^ 2 * jk P (2 * k + 3))

theorem pow_sub_one_eq (P : K) (n : ℕ) : P ^ n - 1 = jk P n * (P - 1) :=
  (geom_sum_mul P n).symm

theorem nf_eq_nfc {P : K} (hP : ∀ m : ℕ, P ^ (m + 1) ≠ 1) (k : ℕ) :
    nf P (P ^ k) = nfc P k := by
  have h1 : P - 1 ≠ 0 := sub_ne_zero.mpr (by simpa using hP 0)
  have hj : ∀ n : ℕ, jk P (n + 1) ≠ 0 := fun n h0 => by
    apply hP n
    have := pow_sub_one_eq P (n + 1); rw [h0, zero_mul] at this
    exact sub_eq_zero.mp this
  have e1 : P * P ^ k - 1 = jk P (k + 1) * (P - 1) := by
    rw [← pow_sub_one_eq, pow_succ, mul_comm]
  have e2 : P * (P ^ k) ^ 2 - 1 = jk P (2 * k + 1) * (P - 1) := by
    rw [← pow_sub_one_eq]; ring
  have e3 : P ^ 2 * (P ^ k) ^ 2 - 1 = jk P (2 * k + 2) * (P - 1) := by
    rw [← pow_sub_one_eq]; ring
  have e4 : P ^ 3 * (P ^ k) ^ 2 - 1 = jk P (2 * k + 3) * (P - 1) := by
    rw [← pow_sub_one_eq]; ring
  have j1 := hj (2 * k); have j2 := hj (2 * k + 1); have j3 := hj (2 * k + 2)
  unfold nf nfc
  rw [e1, e2, e3, e4]
  have : P ^ (2 * k + 2) = P ^ 2 * (P ^ k) ^ 2 := by ring
  rw [this]
  field_simp

variable (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))
local notation "PP" => ((q : K) * q)

/-- The normalised squared raising coupling, as a rational function of `q` defined at `q = 1`. -/
noncomputable def Rc (s : ℕ) : K := (kap q s * qi) ^ 2 * nfc PP (s + 1)

open QOU.FluidDynamics.HaarFieldInvariance in
/-- **The normalised squared raising coupling equals `Rc`.**
`C_s² = Rc q s · ‖p_{s+2}‖² ‖p_{s+1}‖²`. -/
theorem coupling_raise_sq_eq_nfc (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) (s : ℕ) :
    haarState q (ev q (jacobiPoly q (s + 2)) *
        ((β q * δ q) * fieldPlus q (ev q (jacobiPoly q (s + 1))))) ^ 2 =
      Rc q s *
        haarState q (ev q (jacobiPoly q (s + 2)) * ev q (jacobiPoly q (s + 2))) *
        haarState q (ev q (jacobiPoly q (s + 1)) * ev q (jacobiPoly q (s + 1))) := by
  rw [coupling_raise_sq q hp, nf_eq_nfc hp, Rc]

theorem jk_one_eq (n : ℕ) : jk (1 : K) n = n := by simp [jk]

/-- **The classical value.** `Rc 1 s = (s+1)²(s+2)⁴ / ((2s+3)(2s+4)²(2s+5))`. -/
theorem Rc_one (s : ℕ) :
    Rc (1 : Kˣ) s = ((s : K) + 1) ^ 2 * ((s : K) + 2) ^ 4 /
      ((2 * (s : K) + 3) * (2 * (s : K) + 4) ^ 2 * (2 * (s : K) + 5)) := by
  simp only [Rc, nfc, kap, Units.val_one, inv_one, one_mul, one_pow, mul_one, jk_one_eq]
  push_cast
  ring

section Ordered

variable [LinearOrder K] [IsStrictOrderedRing K]

/-- **At `q = 1` the normalised squared coupling is unbounded:** `Rc 1 s ≥ (s+1)²/16`. -/
theorem Rc_one_ge (s : ℕ) : ((s : K) + 1) ^ 2 / 16 ≤ Rc (1 : Kˣ) s := by
  rw [Rc_one]
  have hs : (0 : K) ≤ s := Nat.cast_nonneg s
  have d1 : 0 < 2 * (s : K) + 3 := by linarith
  have d2 : 0 < 2 * (s : K) + 4 := by linarith
  have d3 : 0 < 2 * (s : K) + 5 := by linarith
  rw [div_le_div_iff₀ (by norm_num) (by positivity)]
  have key : (2 * (s : K) + 3) * (2 * (s : K) + 5) ≤ 4 * ((s : K) + 2) ^ 2 := by nlinarith
  have hA : 0 ≤ ((s : K) + 1) ^ 2 * (2 * (s : K) + 4) ^ 2 := by positivity
  have : (2 * (s : K) + 4) ^ 2 = 4 * ((s : K) + 2) ^ 2 := by ring
  nlinarith [mul_le_mul_of_nonneg_left key hA]

end Ordered

end QOU.FluidDynamics.QLegendreClassical
