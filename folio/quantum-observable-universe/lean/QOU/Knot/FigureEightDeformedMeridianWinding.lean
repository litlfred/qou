/-
  Figure-eight (4₁) DEFORMED volume-conjecture — the substrate-matched meridian
  winding lower bound (μ–p Subgoal-2, the anchor-free q₀ obstruction).

  CONTEXT (PR #3855; docs/audits/2026-07-17-murakami-deformed-vc-q0.md).
  The pin-sensitivity map (#3847) proved the 11.5 ppb μ–p tension lives entirely
  in the absolute anchor ℏ_q²; the only escape is a substrate-first ABSOLUTE q₀.
  The Murakami deformed VC evaluates the colored Jones of 4₁ at
  `q_eval = exp((u + 2πi)/N)`; matching to the REAL substrate `q₀ = e^t`
  (t = ln q₀) forces the meridian log-holonomy
        u = N·t − 2πi·k,   k ∈ ℤ₊
  (derived in `qbeta_c3_mq0_nk_scan.py` / `2026-07-12-mq0-nk-scan-result.md`).

  THE EXACT OBSTRUCTION, proved here sorry-free (over ℂ via the stable squared
  modulus `Complex.normSq u = |u|²`): `Im u = −2πk`, hence
        |u|² = (Re u)² + (2πk)² ≥ (2πk)² ≥ (2π)²   for every k ≥ 1,
  i.e. `|u| ≥ 2π`. So NO substrate-matched (N, k≥1) datum lies in the small-|u|
  disk where Murakami's controlled deformed volume Vol(4₁; u) tracks the
  geometric branch — the substrate winding datum is structurally OFF the
  controlled neighborhood (the #3704 "|u| ≥ 2π, off the geometric component"
  finding, now algebraic). This is the branch-B3 half of the scope-(a) verdict:
  the winding-lattice route to an anchor-free q₀ is excluded on the meridian side.

  It does NOT exclude a small-|u| complex (phase-channel) datum from a different,
  not-yet-derived substrate level — that is scope-(a), not scope-(b).

  Archimedean (ℂ): genuinely archimedean (Real.pi, complex modulus) — §7c.

  -- Ref: [murakami2004] figure-eight & Dehn surgery spaces (math/0401084)
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

namespace QOU.Knot.DeformedMeridianWinding

open Real

/-- The substrate-matched Murakami meridian datum for 4₁:
    `u = a − 2πi·k` with `a = N·t` (real) and winding `k`. -/
noncomputable def meridian (a : ℝ) (k : ℕ) : ℂ := ⟨a, -(2 * Real.pi * (k : ℝ))⟩

@[simp] lemma meridian_re (a : ℝ) (k : ℕ) : (meridian a k).re = a := by
  change (⟨a, -(2 * Real.pi * (k : ℝ))⟩ : ℂ).re = a
  have h : (1 : ℕ) = 1 := rfl
  rfl

@[simp] lemma meridian_im (a : ℝ) (k : ℕ) :
    (meridian a k).im = -(2 * Real.pi * (k : ℝ)) := by
  change (⟨a, -(2 * Real.pi * (k : ℝ))⟩ : ℂ).im = -(2 * Real.pi * (k : ℝ))
  have h : (1 : ℕ) = 1 := rfl
  rfl

/-- `|u|² = a² + (2πk)²`, the squared modulus of the substrate-matched meridian. -/
theorem meridian_normSq (a : ℝ) (k : ℕ) :
    Complex.normSq (meridian a k)
      = a * a + (2 * Real.pi * (k : ℝ)) * (2 * Real.pi * (k : ℝ)) := by
  rw [Complex.normSq_apply]
  rw [meridian_re, meridian_im]
  ring

/-- **Winding lower bound (squared-modulus form).** `|u|² ≥ (2πk)²`: the
    imaginary winding part alone forces it, independent of the real offset
    `a = N·t`. Since `normSq = |u|²` this is exactly `|u| ≥ 2πk`. -/
theorem meridian_normSq_ge (a : ℝ) (k : ℕ) :
    (2 * Real.pi * (k : ℝ)) * (2 * Real.pi * (k : ℝ))
      ≤ Complex.normSq (meridian a k) := by
  rw [meridian_normSq]
  nlinarith [mul_self_nonneg a]

/-- **The datum is never in the small-|u| disk.** For every winding `k ≥ 1`,
    `|u|² ≥ (2π)²` — the substrate winding datum sits OUTSIDE any disk
    `|u| < 2π`, in particular outside Murakami's controlled small-|u|
    neighborhood of the geometric structure. Algebraic core of the branch-B3
    scope-(a) obstruction to an anchor-free q₀. -/
theorem meridian_normSq_ge_floor (a : ℝ) (k : ℕ) (hk : 1 ≤ k) :
    (2 * Real.pi) * (2 * Real.pi) ≤ Complex.normSq (meridian a k) := by
  refine le_trans ?_ (meridian_normSq_ge a k)
  have hk1 : (1 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  nlinarith [Real.pi_pos, hk1, sq_nonneg ((k : ℝ) - 1)]

/-- Consequently the datum can never equal `0` for `k ≥ 1`: the winding always
    keeps the deformation nonzero (there is no substrate winding datum at the
    complete structure `u = 0`). -/
theorem meridian_ne_zero (a : ℝ) (k : ℕ) (hk : 1 ≤ k) : meridian a k ≠ 0 := by
  intro hzero
  have h := meridian_normSq_ge_floor a k hk
  rw [hzero, Complex.normSq_zero] at h
  nlinarith [Real.pi_pos]

/-- Exact winding-difference formula for the squared modulus:
    `|meridian a k|² − |meridian a j|² = 4π² · (k² − j²)`. -/
theorem meridian_normSq_sub (a : ℝ) (j k : ℕ) :
    Complex.normSq (meridian a k) - Complex.normSq (meridian a j)
      = (2 * Real.pi) ^ 2 * ((k : ℝ) ^ 2 - (j : ℝ) ^ 2) := by
  rw [meridian_normSq, meridian_normSq]
  ring

/-- Monotonicity of the squared meridian modulus in the winding index `j ≤ k`. -/
theorem meridian_normSq_mono_winding (a : ℝ) {j k : ℕ} (hjk : j ≤ k) :
    Complex.normSq (meridian a j) ≤ Complex.normSq (meridian a k) := by
  have hsub := meridian_normSq_sub a j k
  have hle : (j : ℝ) ≤ (k : ℝ) := by exact_mod_cast hjk
  have hj0 : (0 : ℝ) ≤ (j : ℝ) := Nat.cast_nonneg j
  have hsq : (0 : ℝ) ≤ (k : ℝ) ^ 2 - (j : ℝ) ^ 2 := by nlinarith
  have hpi : (0 : ℝ) ≤ (2 * Real.pi) ^ 2 := sq_nonneg (2 * Real.pi)
  have hprod : (0 : ℝ) ≤ (2 * Real.pi) ^ 2 * ((k : ℝ) ^ 2 - (j : ℝ) ^ 2) :=
    mul_nonneg hpi hsq
  linarith

/-- Strict monotonicity of the squared meridian modulus in the winding index `j < k`. -/
theorem meridian_normSq_strictMono_winding (a : ℝ) {j k : ℕ} (hjk : j < k) :
    Complex.normSq (meridian a j) < Complex.normSq (meridian a k) := by
  have hsub := meridian_normSq_sub a j k
  have hlt : (j : ℝ) < (k : ℝ) := by exact_mod_cast hjk
  have hj0 : (0 : ℝ) ≤ (j : ℝ) := Nat.cast_nonneg j
  have hsq : (0 : ℝ) < (k : ℝ) ^ 2 - (j : ℝ) ^ 2 := by nlinarith
  have hpi : (0 : ℝ) < (2 * Real.pi) ^ 2 := by positivity
  have hprod : (0 : ℝ) < (2 * Real.pi) ^ 2 * ((k : ℝ) ^ 2 - (j : ℝ) ^ 2) :=
    mul_pos hpi hsq
  linarith

/-- Distinct winding indices `j ≠ k` produce distinct complex meridian data. -/
theorem meridian_winding_injective (a : ℝ) {j k : ℕ}
    (h : meridian a j = meridian a k) : j = k := by
  rcases lt_trichotomy j k with hlt | rfl | hgt
  · exfalso
    have hns := meridian_normSq_strictMono_winding a hlt
    rw [h] at hns
    exact lt_irrefl _ hns
  · rfl
  · exfalso
    have hns := meridian_normSq_strictMono_winding a hgt
    rw [h] at hns
    exact lt_irrefl _ hns

end QOU.Knot.DeformedMeridianWinding
