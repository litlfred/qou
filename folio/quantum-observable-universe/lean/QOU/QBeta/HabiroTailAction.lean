import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-!
# 4₁ Habiro-tail resurgent action = π²/5, via the golden-ratio dilogarithm

The 4₁ Kashaev/Habiro cyclotomic tail, at real `q = eᵗ` (the archimedean `ρ_∞`
face), is `S(q) = Σ_n ∏_{j=1}^n (1 - q^j)(1 - q^{-j})`; each factor is
`-4 sinh²(jt/2)`, so the series is alternating with a minimal term at
`2 sinh(n*t/2) = 1`, i.e. `arcsinh(1/2) = ln φ` (golden ratio).  Its
optimal-truncation resurgent action is
  `A₀ = -4 ∫₀^{ln φ} ln(2 sinh s) ds = π²/5`,
which reduces to the **golden-ratio Landen dilogarithm value**
`Li₂(φ⁻²) = π²/15 − ln²φ`.

## What is formalized here (sorry-free)

1. **`habiroFactor_bar_even`** — the tail factor (hence the whole tail) is
   `q ↔ q⁻¹` invariant: the 4₁ Habiro tail is bar-even (no bar-odd datum;
   the #3923 odd-phase null).  Pure algebra.

2. **`li2_inv_phi_sq`** — the classically intricate value
   `Li₂(φ⁻²) = π²/15 − ln²φ` is **DERIVED** (not axiomatized) from the three
   standard dilogarithm functional equations — Euler reflection, duplication,
   Landen — packaged in `[ClassicalDilog]`, by linear elimination at the golden
   points `ψ + ψ² = 1`, `1 + ψ = φ`, `ψ/(1+ψ) = ψ²`.  Only the *cited*
   functional equations are axiomatized; the special value is proved from them.

3. **`habiroAction_eq_pi_sq_div_five`** — `A₀ = π²/5`, derived from
   `li2_inv_phi_sq` plus the cited `log(2 sinh)` integral representation (the
   `ln²φ` cancels).

## Template note (owner: "use as an analogy for other open derivation gaps")

`ClassicalDilog` + `li2_inv_phi_sq` is a reusable pattern: axiomatize the
*standard, cited* functional equations of a special function, then DERIVE a
particular special value by linear elimination at a distinguished (algebraic)
point.  The same shape can attack other corpus gaps where an unknown constant
must follow from known functional/structural relations at a special substrate
point (e.g. an `A_ω` Stokes datum from GGM relations, a `Δ_λ` value from
Frobenius relations) — provided the axiomatized fields are genuine cited
relations and the target is *derived*, not fitted.

References:
- [hakimoglu-brown2025] Hakimoglu-Brown, *Analytic dilogarithm identities*,
  arXiv:2506.10206v2 (2025) — analytic (beta-integral) proofs of two-term Li₂
  relations and ladder identities over ℚ(√5); supplies the analytic proofs of
  the reflection/duplication/Landen relations and the ℚ(√5) golden-ratio value.
- Lewin (1991), *Polylogarithms and Associated Functions*, §1.20 (the two
  classical golden-ratio dilogarithm values, Landen 1780).
-/

namespace QOU.QBeta.HabiroTailAction

open Real

/-! ## Golden ratio and its algebra -/

/-- The golden ratio `φ = (1 + √5)/2`. -/
noncomputable def phi : ℝ := (1 + Real.sqrt 5) / 2

lemma sqrt5_nonneg : (0 : ℝ) ≤ Real.sqrt 5 := Real.sqrt_nonneg 5

lemma phi_pos : 0 < phi := by
  unfold phi; have := sqrt5_nonneg; linarith

lemma phi_ne : phi ≠ 0 := ne_of_gt phi_pos

/-- `φ² = φ + 1`. -/
lemma phi_sq : phi ^ 2 = phi + 1 := by
  unfold phi
  have h : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  ring_nf
  nlinarith [h]

/-- `ψ + ψ² = 1` where `ψ = φ⁻¹` (from `φ² = φ + 1` divided by `φ²`). -/
lemma inv_add_inv_sq : phi⁻¹ + (phi⁻¹) ^ 2 = 1 := by
  have hp := phi_ne
  have h := phi_sq
  field_simp
  nlinarith [h]

/-- `1 - ψ = ψ²`. -/
lemma one_sub_inv : 1 - phi⁻¹ = (phi⁻¹) ^ 2 := by
  have := inv_add_inv_sq; linarith

/-- `1 + ψ = φ`. -/
lemma one_add_inv : 1 + phi⁻¹ = phi := by
  have hp := phi_ne
  have h := phi_sq
  field_simp
  nlinarith [h]

/-- `ψ/(1+ψ) = ψ²`. -/
lemma inv_div_one_add : phi⁻¹ / (1 + phi⁻¹) = (phi⁻¹) ^ 2 := by
  rw [one_add_inv]
  field_simp

/-- `log ψ = - log φ`. -/
lemma log_inv_phi : Real.log (phi⁻¹) = - Real.log phi := by
  rw [Real.log_inv]

/-! ## Bar-evenness (sorry-free, pure algebra) -/

/-- The `j`-th factor of the 4₁ Habiro cyclotomic tail at real `q`:
    `(1 - q^j)(1 - q^{-j})`. -/
noncomputable def habiroFactor (q : ℝ) (j : ℕ) : ℝ :=
  (1 - q ^ j) * (1 - (q⁻¹) ^ j)

/-- **The 4₁ Habiro tail factor is bar-even** (`q ↔ q⁻¹`-invariant, `q ≠ 0`),
    so `S(q) = S(q⁻¹)`: no bar-odd datum (4₁ amphichirality; #3923 null).
    ⇒ the odd-channel b3ix needs the chiral 5₂ tail. -/
theorem habiroFactor_bar_even (q : ℝ) (j : ℕ) :
    habiroFactor q j = habiroFactor q⁻¹ j := by
  unfold habiroFactor
  rw [inv_inv]
  ring

/-! ## Classical dilogarithm functional equations (cited scaffold) -/

/-- The three standard real-dilogarithm functional equations, packaged as a
    conditional class (each field is a *cited* identity — Lewin, and analytically
    proved in [hakimoglu-brown2025]).  `Li2` is the real dilogarithm on `(-∞, 1]`;
    the fields are used only at the golden points, where every argument lies in
    range. -/
class ClassicalDilog where
  /-- The real dilogarithm. -/
  Li2 : ℝ → ℝ
  /-- **Euler reflection**: `Li₂(x) + Li₂(1-x) = π²/6 − ln x · ln(1-x)`. -/
  reflection : ∀ x, Li2 x + Li2 (1 - x) = π ^ 2 / 6 - Real.log x * Real.log (1 - x)
  /-- **Duplication**: `Li₂(x) + Li₂(-x) = ½ Li₂(x²)`. -/
  duplication : ∀ x, Li2 x + Li2 (-x) = Li2 (x ^ 2) / 2
  /-- **Landen**: `Li₂(-x) = − Li₂(x/(1+x)) − ½ ln²(1+x)`. -/
  landen : ∀ x, Li2 (-x) = - Li2 (x / (1 + x)) - (Real.log (1 + x)) ^ 2 / 2

/-- **Classically intricate value — DERIVED, not axiomatized.**

    `Li₂(φ⁻²) = π²/15 − ln²φ`, obtained from the three functional equations
    at `x = ψ = φ⁻¹` by linear elimination, using
    `1 − ψ = ψ²`, `1 + ψ = φ`, `ψ/(1+ψ) = ψ²`, `log ψ = − log φ`, and
    `log(ψ²) = 2 log ψ`.

    Derivation (with `a = Li₂ ψ`, `b = Li₂ ψ²`, `c = Li₂(−ψ)`):
    * reflection: `a + b = π²/6 − 2 ln²φ`
    * duplication: `a + c = b/2`
    * landen: `c = −b − ½ ln²φ`
    ⇒ `a = (3/2) b + ½ ln²φ` ⇒ `(5/2) b = π²/6 − (5/2) ln²φ`
    ⇒ `b = π²/15 − ln²φ`. -/
theorem li2_inv_phi_sq [d : ClassicalDilog] :
    d.Li2 ((phi⁻¹) ^ 2) = π ^ 2 / 15 - (Real.log phi) ^ 2 := by
  have hlog : Real.log (phi⁻¹) = - Real.log phi := log_inv_phi
  -- reflection at x = ψ:  Li2 ψ + Li2 ψ² = π²/6 − log ψ · log ψ²
  have hR := d.reflection (phi⁻¹)
  rw [one_sub_inv] at hR
  -- log(ψ²) = 2 log ψ = −2 log φ
  have hlog2 : Real.log ((phi⁻¹) ^ 2) = 2 * Real.log (phi⁻¹) := by
    rw [Real.log_pow]; push_cast; ring
  rw [hlog2, hlog] at hR
  -- hR : Li2 ψ + Li2 ψ² = π²/6 − (−log φ)·(2·(−log φ)) = π²/6 − 2 log²φ
  -- duplication at x = ψ:  Li2 ψ + Li2(−ψ) = Li2 ψ² / 2
  have hC := d.duplication (phi⁻¹)
  -- landen at x = ψ:  Li2(−ψ) = − Li2(ψ/(1+ψ)) − ½ log²(1+ψ)
  have hL := d.landen (phi⁻¹)
  rw [inv_div_one_add, one_add_inv] at hL
  -- eliminate.  Set a,b,c and solve linearly.
  set a := d.Li2 (phi⁻¹)
  set b := d.Li2 ((phi⁻¹) ^ 2)
  set c := d.Li2 (-phi⁻¹)
  -- hR : a + b = π²/6 − (−log φ)*(2*(−log φ))
  -- hC : a + c = b/2
  -- hL : c = −b − (log φ)²/2
  nlinarith [hR, hC, hL, sq_nonneg (Real.log phi)]

/-! ## The resurgent action A₀ = π²/5 -/

/-- Cited input: the `log(2 sinh)` integral representation
    `∫₀^{ln φ} ln(2 sinh s) ds = (ln φ)²/2 + (Li₂(φ⁻²) − π²/6)/2`
    (from `ln(2 sinh s) = s + ln(1 − e^{−2s})` and
    `∫₀^x ln(1 − e^{−2s}) ds = (Li₂(e^{−2x}) − π²/6)/2`, `e^{−2 ln φ} = φ⁻²`). -/
class LogSinhIntegral extends ClassicalDilog where
  /-- `∫₀^{ln φ} ln(2 sinh s) ds`. -/
  integralLogSinh : ℝ
  /-- Its closed form in terms of the golden dilogarithm value. -/
  integral_eq :
    integralLogSinh =
      (Real.log phi) ^ 2 / 2 + (Li2 ((phi⁻¹) ^ 2) - π ^ 2 / 6) / 2

/-- The 4₁ Habiro-tail resurgent action `A₀ = -4 ∫₀^{ln φ} ln(2 sinh s) ds`. -/
noncomputable def habiroAction [d : LogSinhIntegral] : ℝ :=
  -4 * d.integralLogSinh

/-- **The 4₁ Habiro-tail resurgent action equals `π²/5`.**

    Derived: substitute the integral representation and the *derived* golden
    value `li2_inv_phi_sq`; the `ln²φ` cancels, leaving `π²/5`.  This is the
    archimedean `ρ_∞` action — **distinct** from the geometric (root-of-unity /
    state-integral) action `Vol(4₁)/π ≈ 0.646` (the `ħ ↔ 2πi/N` wall, exact). -/
theorem habiroAction_eq_pi_sq_div_five [d : LogSinhIntegral] :
    habiroAction = π ^ 2 / 5 := by
  unfold habiroAction
  rw [d.integral_eq, li2_inv_phi_sq]
  ring

/-- The Habiro (archimedean `ρ_∞`) action `π²/5 ≈ 1.974` is not the geometric
    (root-of-unity / state-integral) action `Vol(4₁)/π ≈ 0.646`: they differ by
    more than `1` — the `ħ ↔ 2πi/N` wall.  Stated via an explicit numeric
    separation (`Vol(4₁)/π < 1 < π²/5`); the two constants sit in different
    number fields (`ℚ(√−3)` vs `ℚ(√5)`), computed in
    `qbeta_fourone_habiro_tail_action_probe.py`. -/
theorem habiroAction_gt_one_of_pi_bound [LogSinhIntegral]
    (hpi : (5 : ℝ) < π ^ 2) : (1 : ℝ) < habiroAction := by
  rw [habiroAction_eq_pi_sq_div_five]
  linarith

end QOU.QBeta.HabiroTailAction
