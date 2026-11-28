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
* `Rc_ge`: for every `q ≥ 1`, `Rc q s · q^{4(5s+7)} ≥ (s+1)²/16`. So every mode with
  `q^{20s+28} ≤ 2` keeps a normalised squared coupling `≥ (s+1)²/32`. That window holds
  `s ≈ ln 2/(20 ln q)` modes, and it grows without bound as `q → 1⁺`.
* `Rc_le`: for `q² > 1`, `Rc q s · q^{4s} · (q² − 1)³(q⁴ − 1)²(q⁶ − 1) ≤ q⁸`, so `Rc` decays
  like `q^{−4s}` with a prefactor of order `(q² − 1)^{−6}`.

## Surreal reading: where the triad transfer lives

Put `q² = 1 + δ` with `δ` a positive infinitesimal (`q = 1 + ε`, `δ ≈ 2ε`). The two bounds pin
the band of modes that carry a non-negligible raising coupling:

* if `s·δ` is at most a small standard constant (`(1 + δ)^{10s+14} ≤ 2`), then
  `Rc ≥ (s+1)²/32`, which is infinite once `s` is infinite;
* if `s·δ ≥ 3.5·log(1/δ)` (roughly), then `(1 + δ)^{2s} ≥ δ^{−7}` and `Rc ≤ 12⁻¹δ·(1 + O(δ))`,
  which is infinitesimal.

So the edge `s*` of the coupled band has ω-grade exactly `1` (between `c/δ` and
`C·log(1/δ)/δ`). This is the triad-level counterpart of the grade-1 cap in
`qou_ns_surreal_bridge` (`enstrophy_grade_one_of_dissipation_closure`): above ω-grade `1` (up to the log) the raising
coupling is infinitesimal. Whether infinitely many infinitesimal steps can still move a finite
amount of energy is not decided here; that needs the other velocity modes and the dissipation.

All algebraic. No empirical value enters. Sorry-free.

## Not established

* The sharp location of the peak in `s` for fixed `q`, and a Lean statement of the surreal
  window reading below (it is read off `Rc_ge` and `Rc_le`, not proved as a surreal theorem).
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

/-! ## A lower bound uniform in `q ≥ 1`

For `P ≥ 1`, `n ≤ [n]_P` and `[n+1]_P ≤ (n+1)P^n`. Bounding each q-integer of `Rc` this way
gives `Rc q s · q^{4(5s+7)} ≥ Rc 1 s ≥ (s+1)²/16`. Read the other way: modes with
`q^{20s+28} ≤ 2` keep a normalised squared coupling of at least `(s+1)²/32`, and that window
grows without bound as `q → 1⁺`. -/

theorem jk_ge_of_one_le {P : K} (hP : 1 ≤ P) (n : ℕ) : (n : K) ≤ jk P n := by
  induction n with
  | zero => simp
  | succ n ih => rw [jk_succ]; push_cast; linarith [one_le_pow₀ (n := n) hP]

theorem jk_le_of_one_le {P : K} (hP : 1 ≤ P) (n : ℕ) :
    jk P (n + 1) ≤ ((n : K) + 1) * P ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [jk_succ]; push_cast
    have h1 : P ^ n ≤ P ^ (n + 1) := pow_le_pow_right₀ hP (Nat.le_succ n)
    have h0 : (0 : K) ≤ (n : K) + 1 := by positivity
    nlinarith [mul_le_mul_of_nonneg_left h1 h0]

theorem nfc_ge {P : K} (hP : 1 ≤ P) (k : ℕ) :
    ((k : K) + 1) ^ 4 / ((2 * (k : K) + 1) * (2 * (k : K) + 2) ^ 2 * (2 * (k : K) + 3)) ≤
      nfc P k * P ^ (8 * k + 4) := by
  have hP0 : 0 < P := lt_of_lt_of_le one_pos hP
  have hk : (0 : K) ≤ k := Nat.cast_nonneg k
  have c1 : jk P (2 * k + 1) ≤ (2 * (k : K) + 1) * P ^ (2 * k) := by
    have := jk_le_of_one_le hP (2 * k); push_cast at this; exact this
  have c2 : jk P (2 * k + 2) ≤ (2 * (k : K) + 2) * P ^ (2 * k + 1) := by
    have := jk_le_of_one_le hP (2 * k + 1); push_cast at this
    rw [show 2 * k + 1 + 1 = 2 * k + 2 by ring] at this; linarith
  have c3 : jk P (2 * k + 3) ≤ (2 * (k : K) + 3) * P ^ (2 * k + 2) := by
    have := jk_le_of_one_le hP (2 * k + 2); push_cast at this
    rw [show 2 * k + 2 + 1 = 2 * k + 3 by ring] at this; linarith
  have l1 : (2 * (k : K) + 1) ≤ jk P (2 * k + 1) := by
    have := jk_ge_of_one_le hP (2 * k + 1); push_cast at this; exact this
  have l2 : (2 * (k : K) + 2) ≤ jk P (2 * k + 2) := by
    have := jk_ge_of_one_le hP (2 * k + 2); push_cast at this; exact this
  have l3 : (2 * (k : K) + 3) ≤ jk P (2 * k + 3) := by
    have := jk_ge_of_one_le hP (2 * k + 3); push_cast at this; exact this
  have b : (k : K) + 1 ≤ jk P (k + 1) := by
    have := jk_ge_of_one_le hP (k + 1); push_cast at this; exact this
  have e : 1 ≤ P ^ (2 * k + 2) := one_le_pow₀ hP
  set C1 := jk P (2 * k + 1); set C2 := jk P (2 * k + 2); set C3 := jk P (2 * k + 3)
  set B := jk P (k + 1)
  have hC1 : 0 < C1 := by linarith
  have hC2 : 0 < C2 := by linarith
  have hC3 : 0 < C3 := by linarith
  have hd : 0 < (2 * (k : K) + 1) * (2 * (k : K) + 2) ^ 2 * (2 * (k : K) + 3) := by positivity
  unfold nfc
  rw [div_mul_eq_mul_div, div_le_div_iff₀ hd (by positivity)]
  have hC : C1 * C2 ^ 2 * C3 ≤
      (2 * (k : K) + 1) * (2 * (k : K) + 2) ^ 2 * (2 * (k : K) + 3) * P ^ (8 * k + 4) := by
    calc C1 * C2 ^ 2 * C3
        ≤ ((2 * (k : K) + 1) * P ^ (2 * k)) * ((2 * (k : K) + 2) * P ^ (2 * k + 1)) ^ 2 *
            ((2 * (k : K) + 3) * P ^ (2 * k + 2)) := by gcongr
      _ = _ := by ring
  calc ((k : K) + 1) ^ 4 * (C1 * C2 ^ 2 * C3)
      ≤ ((k : K) + 1) ^ 4 *
          ((2 * (k : K) + 1) * (2 * (k : K) + 2) ^ 2 * (2 * (k : K) + 3) * P ^ (8 * k + 4)) := by
        gcongr
    _ ≤ B ^ 4 *
          ((2 * (k : K) + 1) * (2 * (k : K) + 2) ^ 2 * (2 * (k : K) + 3) * P ^ (8 * k + 4)) := by
        gcongr
    _ ≤ P ^ (2 * k + 2) * B ^ 4 * P ^ (8 * k + 4) *
          ((2 * (k : K) + 1) * (2 * (k : K) + 2) ^ 2 * (2 * (k : K) + 3)) := by
        have h0 : 0 ≤ B ^ 4 *
            ((2 * (k : K) + 1) * (2 * (k : K) + 2) ^ 2 * (2 * (k : K) + 3) * P ^ (8 * k + 4)) := by
          positivity
        nlinarith [mul_le_mul_of_nonneg_right e h0]

/-- **Uniform lower bound for `q ≥ 1`:** `Rc q s · q^{4(5s+7)} ≥ (s+1)²/16`. -/
theorem Rc_ge (hq : 1 ≤ (q : K)) (s : ℕ) :
    ((s : K) + 1) ^ 2 / 16 ≤ Rc q s * ((q : K) * q) ^ (10 * s + 14) := by
  have hP : 1 ≤ (q : K) * q := one_le_mul_of_one_le_of_one_le hq hq
  have hqq : qi * (q : K) = 1 := by simp
  have hA : (kap q s * qi) ^ 2 * ((q : K) * q) ^ (2 * s + 2) = jk ((q : K) * q) (s + 1) ^ 2 := by
    unfold kap
    rw [show (qi * jk ((q : K) * q) (s + 1) * (qi * qi) ^ s * qi) ^ 2 * ((q : K) * q) ^ (2 * s + 2)
        = jk ((q : K) * q) (s + 1) ^ 2 * (qi * q) ^ (4 * s + 4) by ring, hqq, one_pow, mul_one]
  have hsplit : Rc q s * ((q : K) * q) ^ (10 * s + 14) =
      jk ((q : K) * q) (s + 1) ^ 2 * (nfc PP (s + 1) * PP ^ (8 * (s + 1) + 4)) := by
    rw [← hA, Rc, show 10 * s + 14 = (2 * s + 2) + (8 * (s + 1) + 4) by ring, pow_add]; ring
  rw [hsplit]
  have hb := jk_ge_of_one_le hP (s + 1); push_cast at hb
  have hn := nfc_ge hP (s + 1); push_cast at hn
  have hs : (0 : K) ≤ s := Nat.cast_nonneg s
  have h1 := Rc_one_ge (K := K) s
  rw [Rc_one] at h1
  have hcls : 0 ≤ ((s : K) + 1 + 1) ^ 4 /
      ((2 * ((s : K) + 1) + 1) * (2 * ((s : K) + 1) + 2) ^ 2 * (2 * ((s : K) + 1) + 3)) := by
    apply div_nonneg (pow_nonneg (by linarith) 4)
    apply mul_nonneg (mul_nonneg (by linarith) (sq_nonneg _)) (by linarith)
  have heq : ((s : K) + 1) ^ 2 * (((s : K) + 1 + 1) ^ 4 /
      ((2 * ((s : K) + 1) + 1) * (2 * ((s : K) + 1) + 2) ^ 2 * (2 * ((s : K) + 1) + 3))) =
      ((s : K) + 1) ^ 2 * ((s : K) + 2) ^ 4 /
        ((2 * (s : K) + 3) * (2 * (s : K) + 4) ^ 2 * (2 * (s : K) + 5)) := by
    rw [mul_div_assoc']; congr 1 <;> ring
  calc ((s : K) + 1) ^ 2 / 16 ≤ ((s : K) + 1) ^ 2 * (((s : K) + 1 + 1) ^ 4 /
        ((2 * ((s : K) + 1) + 1) * (2 * ((s : K) + 1) + 2) ^ 2 * (2 * ((s : K) + 1) + 3))) := by
        rw [heq]; exact h1
    _ ≤ jk ((q : K) * q) (s + 1) ^ 2 * (nfc PP (s + 1) * PP ^ (8 * (s + 1) + 4)) := by
        gcongr

/-! ## A matching upper bound for `q² > 1`

For `z ≥ 1`, `a z² − 1 ≥ (a − 1) z²`. Applied to the four denominator factors of
`nf` this gives `nf P z · (P − 1)(P² − 1)²(P³ − 1) · z² ≤ P⁶`, and with `[s+1]_P (P − 1) ≤ P^{s+1}`
it gives `Rc q s · P^{2s} · (P − 1)³(P² − 1)²(P³ − 1) ≤ P⁴`. So `Rc` decays like `q^{−4s}`, with a
prefactor that grows like `(P − 1)^{−6}` as `q → 1⁺`. -/

theorem sq_sub_one_ge (a : K) {z : K} (hz : 1 ≤ z) : (a - 1) * z ^ 2 ≤ a * z ^ 2 - 1 := by
  have : 1 ≤ z ^ 2 := one_le_pow₀ hz
  nlinarith

theorem nf_le {P z : K} (hP : 1 < P) (hz : 1 ≤ z) :
    nf P z * ((P - 1) * (P ^ 2 - 1) ^ 2 * (P ^ 3 - 1)) * z ^ 2 ≤ P ^ 6 := by
  have hP0 : 0 < P := lt_trans one_pos hP
  have hz0 : 0 < z := lt_of_lt_of_le one_pos hz
  have hP2 : 1 < P ^ 2 := one_lt_pow₀ hP (by norm_num)
  have hP3 : 1 < P ^ 3 := one_lt_pow₀ hP (by norm_num)
  have g1 := sq_sub_one_ge P hz
  have g2 := sq_sub_one_ge (P ^ 2) hz
  have g3 := sq_sub_one_ge (P ^ 3) hz
  have p1 : 0 < (P - 1) * z ^ 2 := by have := sub_pos.mpr hP; positivity
  have p2 : 0 < (P ^ 2 - 1) * z ^ 2 := by have := sub_pos.mpr hP2; positivity
  have p3 : 0 < (P ^ 3 - 1) * z ^ 2 := by have := sub_pos.mpr hP3; positivity
  have a1 : 0 ≤ P * z - 1 := by nlinarith
  have hnum : P ^ 2 * z ^ 2 * (P * z - 1) ^ 4 ≤ P ^ 6 * z ^ 6 := by
    have : (P * z - 1) ^ 4 ≤ (P * z) ^ 4 := pow_le_pow_left₀ a1 (by linarith) 4
    have h0 : 0 ≤ P ^ 2 * z ^ 2 := by positivity
    nlinarith [mul_le_mul_of_nonneg_left this h0]
  have hden : ((P - 1) * z ^ 2) * ((P ^ 2 - 1) * z ^ 2) ^ 2 * ((P ^ 3 - 1) * z ^ 2) ≤
      (P * z ^ 2 - 1) * (P ^ 2 * z ^ 2 - 1) ^ 2 * (P ^ 3 * z ^ 2 - 1) := by
    have n1 : 0 ≤ P * z ^ 2 - 1 := by linarith
    have n2 : 0 ≤ P ^ 2 * z ^ 2 - 1 := by linarith
    have n3 : 0 ≤ P ^ 3 * z ^ 2 - 1 := by linarith
    gcongr
  have hD : 0 < (P * z ^ 2 - 1) * (P ^ 2 * z ^ 2 - 1) ^ 2 * (P ^ 3 * z ^ 2 - 1) :=
    lt_of_lt_of_le (by positivity) hden
  have hc : 0 < (P - 1) * (P ^ 2 - 1) ^ 2 * (P ^ 3 - 1) := by
    have := sub_pos.mpr hP; have := sub_pos.mpr hP2; have := sub_pos.mpr hP3; positivity
  unfold nf
  rw [div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ hD]
  calc P ^ 2 * z ^ 2 * (P * z - 1) ^ 4 * ((P - 1) * (P ^ 2 - 1) ^ 2 * (P ^ 3 - 1)) * z ^ 2
      ≤ P ^ 6 * z ^ 6 * ((P - 1) * (P ^ 2 - 1) ^ 2 * (P ^ 3 - 1)) * z ^ 2 := by gcongr
    _ = P ^ 6 * (((P - 1) * z ^ 2) * ((P ^ 2 - 1) * z ^ 2) ^ 2 * ((P ^ 3 - 1) * z ^ 2)) := by
        ring
    _ ≤ P ^ 6 * ((P * z ^ 2 - 1) * (P ^ 2 * z ^ 2 - 1) ^ 2 * (P ^ 3 * z ^ 2 - 1)) := by
        gcongr

/-- **Upper bound for `q² > 1`:**
`Rc q s · q^{4s} · (q² − 1)³(q⁴ − 1)²(q⁶ − 1) ≤ q⁸`. -/
theorem Rc_le (hq : 1 < (q : K) * q) (s : ℕ) :
    Rc q s * ((q : K) * q) ^ (2 * s) *
        ((PP - 1) ^ 3 * (PP ^ 2 - 1) ^ 2 * (PP ^ 3 - 1)) ≤ PP ^ 4 := by
  have hP0 : 0 < PP := lt_trans one_pos hq
  have hp : ∀ m : ℕ, PP ^ (m + 1) ≠ 1 := fun m => (one_lt_pow₀ hq (Nat.succ_ne_zero m)).ne'
  have hqq : qi * (q : K) = 1 := by simp
  have hA : (kap q s * qi) ^ 2 * PP ^ (2 * s + 2) = jk PP (s + 1) ^ 2 := by
    unfold kap
    rw [show (qi * jk PP (s + 1) * (qi * qi) ^ s * qi) ^ 2 * PP ^ (2 * s + 2)
        = jk PP (s + 1) ^ 2 * (qi * q) ^ (4 * s + 4) by ring, hqq, one_pow, mul_one]
  set z := PP ^ (s + 1) with hzdef
  have hz : 1 ≤ z := one_le_pow₀ hq.le
  have hj : jk PP (s + 1) * (PP - 1) ≤ z := by
    rw [← pow_sub_one_eq]; linarith
  have hj0 : 0 ≤ jk PP (s + 1) := le_trans (Nat.cast_nonneg _) (jk_ge_of_one_le hq.le (s + 1))
  have hn := nf_le hq hz
  have hnf0 : 0 ≤ nf PP z := by
    have h := nf_pos_of_one_lt hq hz; exact h.le
  have hc0 : 0 ≤ (PP - 1) * (PP ^ 2 - 1) ^ 2 * (PP ^ 3 - 1) := by
    have := sub_pos.mpr hq
    have := sub_pos.mpr (one_lt_pow₀ hq (n := 2) (by norm_num))
    have := sub_pos.mpr (one_lt_pow₀ hq (n := 3) (by norm_num)); positivity
  have key : Rc q s * PP ^ (2 * s) * ((PP - 1) ^ 3 * (PP ^ 2 - 1) ^ 2 * (PP ^ 3 - 1)) * PP ^ 2 =
      (jk PP (s + 1) * (PP - 1)) ^ 2 *
        (nf PP z * ((PP - 1) * (PP ^ 2 - 1) ^ 2 * (PP ^ 3 - 1))) := by
    rw [Rc, ← nf_eq_nfc hp, ← hzdef,
      show (jk PP (s + 1) * (PP - 1)) ^ 2 = jk PP (s + 1) ^ 2 * (PP - 1) ^ 2 by ring, ← hA]
    ring
  have hsq : (jk PP (s + 1) * (PP - 1)) ^ 2 ≤ z ^ 2 :=
    pow_le_pow_left₀ (mul_nonneg hj0 (sub_pos.mpr hq).le) hj 2
  have hzP : z ^ 2 = PP ^ (2 * s) * PP ^ 2 := by rw [hzdef]; ring
  have hfin : Rc q s * PP ^ (2 * s) * ((PP - 1) ^ 3 * (PP ^ 2 - 1) ^ 2 * (PP ^ 3 - 1)) * PP ^ 2
      ≤ PP ^ 4 * PP ^ 2 := by
    rw [key]
    calc (jk PP (s + 1) * (PP - 1)) ^ 2 * (nf PP z * ((PP - 1) * (PP ^ 2 - 1) ^ 2 * (PP ^ 3 - 1)))
        ≤ z ^ 2 * (nf PP z * ((PP - 1) * (PP ^ 2 - 1) ^ 2 * (PP ^ 3 - 1))) := by
          gcongr
      _ = nf PP z * ((PP - 1) * (PP ^ 2 - 1) ^ 2 * (PP ^ 3 - 1)) * z ^ 2 := by ring
      _ ≤ PP ^ 6 := hn
      _ = PP ^ 4 * PP ^ 2 := by ring
  exact le_of_mul_le_mul_right hfin (by positivity)

end Ordered

end QOU.FluidDynamics.QLegendreClassical
