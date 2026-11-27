/-
Copyright (c) 2026 litlfred. All rights reserved.

# Projector insertions on 4₁ with the full Ocneanu trace: a free `z` does not force a w² dressing

Bean `qou-6gf9` (compute-accuracy C3, epic `qou-myts`). Follows PR #9445
(`MuPProjectorInsertionWOrder.lean`), which used the SU(2) weights (`y₁₁₁ = 0`).
Probe: `computations/probes/mu_p_full_hecke_weights_probe.py`
(witness `mu-p-full-hecke-weights.witness.json`).
Audit: `docs/audits/2026-11-27-mu-p-full-hecke-weights.md`.

## The question

PR #9445 showed that, with SU(2) Markov weights, photon-projector insertions
`e_i = (q − σ_i)/[2]_q` into `4₁ = (σ₁σ₂⁻¹)²` never have vanishing `O(w⁰)` and
`O(w¹)` terms, and that once both are cancelled by choice the `w²` coefficient
is free. It left open the full Hecke algebra `H₃` with `y₁₁₁ ≠ 0`. Here the
Markov (Ocneanu) trace over all of `H₃` is kept with its parameter `z` symbolic.
Convention D (owner ruling 2026-08-15) is `y₁₁₁ = 0`; this is a comparison
family only, and no value of `z` is chosen to fit anything.

Everything is a statement over a generic field `K`. No measured quantity enters
any statement.

## What is proved (sorry-free)

1. `ocneanu_one`, `ocneanu_sigma1`, `ocneanu_sigma1sigma2`: the weights
   `y₃, y₂₁, y₁₁₁ ∈ K(q, z)` below are the Ocneanu trace: `tr 1 = 1`,
   `tr σ₁ = z`, `tr σ₁σ₂ = z²`. (Three conjugacy classes, three irreducibles, so
   these three values fix the trace.)
2. `y111_factor`, `su2_weights`: `y₁₁₁ = q²(z − q)((q²+1)z − q³)/den`; at the
   SU(2) point `z = q³/(q²+1)` the weights are exactly those of PR #9445.
3. `trM41Z_eq`, `pairCorrZ_eq`: closed forms of `tr_M(4₁)` and of the
   bar-symmetric single insertion `⟨e₁⟩+⟨e₂⟩` as elements of `K(q, z)`.
   The correlator carries the factor `(z − q)`.
4. `pairCorrZ_su2`: at the SU(2) point it equals PR #9445's `pairCorr`.
5. `pairCorrZ_at_one`: at `q = 1` it equals `(z − 1)/z`. So `O(w⁰)` vanishes
   only if `z(1) = 1`.
6. `pairCorrZ_degenerate`, `sign_only_weights`: at `z = q` (trivial
   representation only) every insertion correlator is `0` at every order; at
   `z = −q⁻¹` only the sign representation survives.
7. `suN_vanishing_forces_degenerate`: in the SU(N) / HOMFLY family `a = q^N`
   (`N` symbolic), using the probe's exact `w`-Taylor data, `O(1) = O(w) = 0`
   for the single, double or connected observable forces `N = ±1`, the two
   degenerate traces of item 6.
8. `suN_w2_not_forced`: for every `N` off `{0, ±1}` and off the roots of
   `7N⁴ + 126N² − 621`, every `w²` value is reached by a combination of
   `1, S₁, D` with vanishing `O(1)` and `O(w)`.
9. `general_z_w2_free`: in the general bar-covariant family
   `z = sinh h · (1 + 2c/h + 2k₁h + 2k₃h³)` (`q = eʰ`), the single insertion with
   `O(1) = O(w) = 0` has `w²` coefficient `(90k₃ + 1)/45`, and every target is
   reached by one `k₃`. The `w²` coefficient is a free parameter of the trace,
   not a consequence of the knot.

Items 7–9 take the `w`-Taylor coefficients from the probe (exact sympy series);
only items 1–6 are derived here from the matrices.

Scope (a) for the route: the full-Hecke projector-insertion class does not
derive a `w²` dressing. It does not exclude a dressing from a different
construction.
-/
import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Trace
import QOU.BraidsAndKnots.MuPProjectorInsertionWOrder

namespace QOU.BraidsAndKnots.MuPFullHeckeWeights

open Matrix
open QOU.BraidsAndKnots.MuPProjectorInsertionWOrder

variable {K : Type*} [Field K]

/-! ## The Ocneanu trace on `H₃` with symbolic `z` -/

/-- Common denominator `(q²+1)(q⁴+q²+1)` of the three weights. -/
def den (q : K) : K := (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)

/-- Weight of the trivial representation `(3)`, where `σ_i ↦ q`. -/
def y3 (q z : K) : K := (q * z + 1) * (q ^ 3 * z + q * z + 1) / den q

/-- Weight of the 2-dimensional representation `(2,1)`. -/
def y21 (q z : K) : K := -(q * (z - q) * (q * z + 1) * (q ^ 2 + 1)) / den q

/-- Weight of the sign representation `(1,1,1)`, where `σ_i ↦ −q⁻¹`. -/
def y111 (q z : K) : K := q ^ 2 * (z - q) * (q ^ 2 * z + z - q ^ 3) / den q

/-- A class function from the three weights: `χ_(3)` and `χ_(111)` are given,
and `χ_(21) = tr₃ − χ_(3)` in the 3-dimensional representation `(3) ⊕ (2,1)`. -/
def mtrace (q z : K) (M : Matrix (Fin 3) (Fin 3) K) (triv sgn : K) : K :=
  y3 q z * triv + y21 q z * (trace M - triv) + y111 q z * sgn

theorem den_ne_zero (q : K) (h2 : q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) : den q ≠ 0 :=
  mul_ne_zero h2 h4

theorem trace_A1 (q : K) : trace (A1 q) = 2 * q - q⁻¹ := by
  simp [trace, A1, Fin.sum_univ_three]; ring

theorem trace_A1A2 (q : K) (hq : q ≠ 0) : trace (A1 q * A2 q) = q ^ 2 - 1 := by
  simp [trace, A1, A2, Fin.sum_univ_three]
  field_simp

theorem ocneanu_one (q z : K) (h2 : q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    mtrace q z (1 : Matrix (Fin 3) (Fin 3) K) 1 1 = 1 := by
  have hd := den_ne_zero q h2 h4
  simp only [mtrace, trace_one, Fintype.card_fin, y3, y21, y111]
  field_simp
  unfold den
  push_cast
  ring

theorem ocneanu_sigma1 (q z : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    mtrace q z (A1 q) q (-q⁻¹) = z := by
  have hd := den_ne_zero q h2 h4
  rw [mtrace, trace_A1]
  simp only [y3, y21, y111]
  field_simp
  unfold den
  ring

theorem ocneanu_sigma1sigma2 (q z : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    mtrace q z (A1 q * A2 q) (q ^ 2) (q⁻¹ ^ 2) = z ^ 2 := by
  have hd := den_ne_zero q h2 h4
  rw [mtrace, trace_A1A2 q hq]
  simp only [y3, y21, y111]
  field_simp
  unfold den
  ring

/-- The sign weight factors through `(z − q)((q²+1)z − q³)`: it vanishes exactly at
the trivial-only trace `z = q` and at the SU(2) point `z = q³/(q²+1)`. -/
theorem y111_factor (q z : K) :
    y111 q z = q ^ 2 * (z - q) * ((q ^ 2 + 1) * z - q ^ 3) / den q := by
  unfold y111; ring

/-- At the SU(2) point the weights are those of PR #9445 and `y₁₁₁ = 0`. -/
theorem su2_weights (q : K) (h2 : q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    y3 q (q ^ 3 / (q ^ 2 + 1)) = MuPProjectorInsertionWOrder.y3 q ∧
      y21 q (q ^ 3 / (q ^ 2 + 1)) = MuPProjectorInsertionWOrder.y21 q ∧
      y111 q (q ^ 3 / (q ^ 2 + 1)) = 0 := by
  have hd := den_ne_zero q h2 h4
  refine ⟨?_, ?_, ?_⟩
  · simp only [y3, MuPProjectorInsertionWOrder.y3]
    rw [div_eq_div_iff hd (pow_ne_zero 2 h2)]
    field_simp
    unfold den
    ring
  · simp only [y21, MuPProjectorInsertionWOrder.y21]
    rw [div_eq_div_iff hd (pow_ne_zero 2 h2)]
    field_simp
    unfold den
    ring
  · simp only [y111]
    rw [div_eq_zero_iff]
    left
    field_simp
    ring

/-- At `z = −q⁻¹` only the sign representation survives. -/
theorem sign_only_weights (q : K) (hq : q ≠ 0) :
    y3 q (-q⁻¹) = 0 ∧ y21 q (-q⁻¹) = 0 := by
  have h : q * -q⁻¹ + 1 = 0 := by field_simp; ring
  constructor
  · unfold y3; rw [h]; simp
  · unfold y21; rw [show q * (-q⁻¹ - q) * (q * -q⁻¹ + 1) * (q ^ 2 + 1) = 0 by rw [h]; ring]
    simp

/-! ## `tr_M(4₁)` and the single insertion -/

/-- `W(q,z)`, with `tr_M(4₁) = W/q³`. -/
def W (q z : K) : K :=
  q ^ 6 * z - q ^ 5 * z ^ 2 + q ^ 5 - 4 * q ^ 4 * z + 3 * q ^ 3 * z ^ 2 - 2 * q ^ 3 +
    4 * q ^ 2 * z - q * z ^ 2 + q - z

/-- `R(q,z)`, the second factor of the single-insertion numerator. -/
def R (q z : K) : K :=
  q ^ 7 * z + q ^ 6 - 2 * q ^ 5 * z - 2 * q ^ 3 * z - 2 * q ^ 2 + q * z + 1

/-- `tr_M(4₁)` for the full trace. `4₁` has exponent sum 0, so `χ_(3) = χ_(111) = 1`. -/
def trM41Z (q z : K) : K := mtrace q z (word41 q) 1 1

theorem trM41Z_eq (q z : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) : trM41Z q z = W q z / q ^ 3 := by
  have hd := den_ne_zero q h2 h4
  rw [trM41Z, mtrace, trace_word41 q hq]
  simp only [y3, y21, y111]
  field_simp
  unfold den W
  ring

/-- The bar-symmetric single insertion `⟨e₁⟩ + ⟨e₂⟩`, full trace, normalised by
`tr_M(4₁)`. `e_i` kills `(3)` and is `1` on `(111)`. -/
def pairCorrZ (q z : K) : K :=
  (y21 q z * (trace (E1 q * word41 q) + trace (E2 q * word41 q)) + 2 * y111 q z) / trM41Z q z

theorem pairCorrZ_num (q z : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    y21 q z * (trace (E1 q * word41 q) + trace (E2 q * word41 q)) + 2 * y111 q z =
      -((z - q) * R q z) / (q ^ 3 * (q ^ 2 + 1)) := by
  have hd := den_ne_zero q h2 h4
  rw [trace_E1_word41 q hq h2, trace_E2_word41 q hq h2]
  simp only [y21, y111]
  field_simp
  unfold den R
  ring

/-- Closed form in `K(q, z)`: `⟨e₁⟩+⟨e₂⟩ = −(z − q)·R / ((q²+1)·W)`. -/
theorem pairCorrZ_eq (q z : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (hW : W q z ≠ 0) :
    pairCorrZ q z = -((z - q) * R q z) / ((q ^ 2 + 1) * W q z) := by
  rw [pairCorrZ, pairCorrZ_num q z hq h2 h4, trM41Z_eq q z hq h2 h4]
  field_simp

/-- Trivial-only trace: every single insertion vanishes identically. -/
theorem pairCorrZ_degenerate (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) : pairCorrZ q q = 0 := by
  rw [pairCorrZ, pairCorrZ_num q q hq h2 h4]
  simp

/-- At `q = 1`: `W(1,z) = z²`, and the single insertion is `(z − 1)/z`. -/
theorem W_at_one (z : K) : W 1 z = z ^ 2 := by unfold W; ring

theorem pairCorrZ_at_one (z : K) (hz : z ≠ 0) (htwo : (2 : K) ≠ 0) (hthree : (3 : K) ≠ 0) :
    pairCorrZ (1 : K) z = (z - 1) / z := by
  have h2 : (1 : K) ^ 2 + 1 ≠ 0 := by norm_num; exact htwo
  have h4 : (1 : K) ^ 4 + 1 ^ 2 + 1 ≠ 0 := by norm_num; exact hthree
  have hW : W (1 : K) z ≠ 0 := by rw [W_at_one]; exact pow_ne_zero 2 hz
  rw [pairCorrZ_eq 1 z one_ne_zero h2 h4 hW, W_at_one]
  simp only [R]
  field_simp
  linear_combination (z ^ 2 - z) * inv_mul_cancel₀ htwo

/-- At the SU(2) point the full-trace correlator is PR #9445's `pairCorr`. -/
theorem pairCorrZ_su2 (q : K) (h2 : q ^ 2 + 1 ≠ 0)
    (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    pairCorrZ q (q ^ 3 / (q ^ 2 + 1)) = pairCorr q := by
  obtain ⟨h3, h21, h111⟩ := su2_weights q h2 h4
  have hT : trM41Z q (q ^ 3 / (q ^ 2 + 1)) = trM41 q := by
    rw [trM41Z, mtrace, h3, h21, h111, trM41]; ring
  rw [pairCorrZ, pairCorr, hT, h21, h111]
  ring

/-! ## The SU(N) family `a = q^N`, `N` symbolic (w-Taylor data from the probe) -/

section SUN

variable (N : ℚ)

/-- `(O(1), O(w), O(w²))` of `S₁ = 4·⟨e₁⟩+⟨e₂⟩` in the SU(N) family. At `N = 2`
this is `(−4, 80, −812)` (PR #9445). -/
def s1Taylor : ℚ × ℚ × ℚ :=
  (-4 * (N - 1), 40 * N * (N - 1) * (N + 1) / 3,
    -14 * N * (N - 1) * (N + 1) * (52 * N ^ 2 - 63) / 15)

/-- All doubles `D`. At `N = 2`: `(−11, 217, −8811/4)`. -/
def dTaylor : ℚ × ℚ × ℚ :=
  ((N - 1) * (3 * N - 17), -(N - 1) * (N + 1) * (33 * N ^ 2 - 200 * N + 51) / 3,
    (N - 1) * (N + 1) * (2408 * N ^ 4 - 14560 * N ^ 3 + 903 * N ^ 2 + 17640 * N - 4995) / 60)

/-- Connected doubles `C`. At `N = 2`: `(−21, 617, −41051/4)`. -/
def cTaylor : ℚ × ℚ × ℚ :=
  (-7 * (N - 1) * (N + 1), (N - 1) * (N + 1) * (167 * N ^ 2 - 51) / 3,
    -(N - 1) * (N + 1) * (56456 * N ^ 4 - 75629 * N ^ 2 + 14985) / 180)

theorem suN_at_two :
    s1Taylor 2 = (-4, 80, -812) ∧ dTaylor 2 = (-11, 217, -8811 / 4) ∧
      cTaylor 2 = (-21, 617, -41051 / 4) := by
  simp only [s1Taylor, dTaylor, cTaylor]; norm_num

/-- Vanishing `O(1)` and `O(w)` in any one of `S₁`, `D`, `C` forces `N = ±1`,
the two degenerate traces (trivial-only `z = q`, sign-only `z = −q⁻¹`). -/
theorem suN_vanishing_forces_degenerate :
    ((s1Taylor N).1 = 0 ∧ (s1Taylor N).2.1 = 0 → N = 1) ∧
      ((dTaylor N).1 = 0 ∧ (dTaylor N).2.1 = 0 → N = 1) ∧
      ((cTaylor N).1 = 0 ∧ (cTaylor N).2.1 = 0 → N = 1 ∨ N = -1) := by
  simp only [s1Taylor, dTaylor, cTaylor]
  refine ⟨fun ⟨h0, _⟩ => by linarith, fun ⟨h0, h1⟩ => ?_, fun ⟨h0, _⟩ => ?_⟩
  · rcases mul_eq_zero.mp h0 with h | h
    · linarith
    · exfalso
      have hN : N = 17 / 3 := by linarith
      subst hN; norm_num at h1
  · have : (N - 1) * (N + 1) = 0 := by linarith
    rcases mul_eq_zero.mp this with h | h
    · left; linarith
    · right; linarith

/-- The determinant of the `3×3` coefficient matrix on columns `1, S₁, D`. -/
def delta : ℚ := 8 * N * (N - 1) ^ 2 * (N + 1) ^ 2 * (7 * N ^ 4 + 126 * N ^ 2 - 621) / 45

theorem delta_eq :
    (dTaylor N).2.1 * (s1Taylor N).2.2 - (s1Taylor N).2.1 * (dTaylor N).2.2 = -delta N := by
  simp only [s1Taylor, dTaylor, delta]; ring

/-- **Non-forcing in the SU(N) family.** Off the degenerate set, for every target
`t` there is a combination of `1, S₁, D` with vanishing `O(1)` and `O(w)` and
`O(w²) = t`. -/
theorem suN_w2_not_forced (hΔ : delta N ≠ 0) (t : ℚ) :
    ∃ x0 x1 x2 : ℚ,
      x0 + x1 * (s1Taylor N).1 + x2 * (dTaylor N).1 = 0 ∧
      x1 * (s1Taylor N).2.1 + x2 * (dTaylor N).2.1 = 0 ∧
      x1 * (s1Taylor N).2.2 + x2 * (dTaylor N).2.2 = t := by
  set a1 := (s1Taylor N).2.1
  set b1 := (dTaylor N).2.1
  set a2 := (s1Taylor N).2.2
  set b2 := (dTaylor N).2.2
  have hd : b1 * a2 - a1 * b2 ≠ 0 := by
    rw [show b1 * a2 - a1 * b2 = -delta N from delta_eq N]; exact neg_ne_zero.mpr hΔ
  refine ⟨-(b1 * t / (b1 * a2 - a1 * b2)) * (s1Taylor N).1 +
      a1 * t / (b1 * a2 - a1 * b2) * (dTaylor N).1,
    b1 * t / (b1 * a2 - a1 * b2), -(a1 * t / (b1 * a2 - a1 * b2)), ?_, ?_, ?_⟩
  · ring
  · field_simp; ring
  · field_simp; ring

end SUN

/-! ## The general bar-covariant family (w-Taylor data from the probe) -/

/-- `(O(1), O(w), O(w²))` of `⟨e₁⟩+⟨e₂⟩` for `z = sinh h·(1 + 2c/h + 2k₁h + 2k₃h³)`,
`q = eʰ`. (The SU(N) family is `c = 1/(2N)`, `k₁ = N/6`, `k₃ = −N³/90`.) -/
def pairGeneral (c k1 k3 : ℚ) : ℚ × ℚ × ℚ :=
  ((2 * c - 1) / (2 * c), -(40 * c ^ 2 - 12 * c * k1 - 9) / (24 * c ^ 3),
    -(1176 * c ^ 4 - 260 * c ^ 3 * k1 - 80 * c ^ 3 * k3 + 80 * c ^ 2 * k1 ^ 2 - 515 * c ^ 2 +
      180 * c * k1 + 45) / (160 * c ^ 5))

/-- **The `w²` coefficient is a free parameter of the trace.** `O(1) = 0` forces
`c = 1/2`, then `O(w) = 0` forces `k₁ = 1/6`; the remaining `O(w²)` is
`(90k₃ + 1)/45`, and every target `t` is hit by exactly one `k₃`. -/
theorem general_z_w2_free (t : ℚ) :
    (pairGeneral (1 / 2) (1 / 6) ((45 * t - 1) / 90)).1 = 0 ∧
      (pairGeneral (1 / 2) (1 / 6) ((45 * t - 1) / 90)).2.1 = 0 ∧
      (pairGeneral (1 / 2) (1 / 6) ((45 * t - 1) / 90)).2.2 = t := by
  simp only [pairGeneral]; refine ⟨by norm_num, by norm_num, by ring⟩

theorem general_z_w2_eq (k3 : ℚ) :
    (pairGeneral (1 / 2) (1 / 6) k3).2.2 = (90 * k3 + 1) / 45 := by
  simp only [pairGeneral]; ring

/-- `O(1) = 0` and `O(w) = 0` pin `c` and `k₁` (for `c ≠ 0`). -/
theorem general_z_low_orders (c k1 k3 : ℚ) (hc : c ≠ 0)
    (h0 : (pairGeneral c k1 k3).1 = 0) (h1 : (pairGeneral c k1 k3).2.1 = 0) :
    c = 1 / 2 ∧ k1 = 1 / 6 := by
  simp only [pairGeneral] at h0 h1
  have hc' : c = 1 / 2 := by
    rcases div_eq_zero_iff.mp h0 with h | h
    · linarith
    · exact absurd (by linarith : c = 0) hc
  subst hc'
  refine ⟨rfl, ?_⟩
  norm_num at h1
  linarith

end QOU.BraidsAndKnots.MuPFullHeckeWeights
