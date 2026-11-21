import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

/-!
# Bar-parity of the Ohtsuki κ-tower at the imaginary substrate

The finite-`b` complex volume of the figure-eight complement expands as an
Ohtsuki tower `𝔙_b = 𝔙_0 + Σ_{n≥1} κ_n (2πb²)ⁿ` with **real** coefficients
`κ_n ∈ ℚ(√3)·π^{⌈n/2⌉}` (`κ₁ = 11√3π/108`, `κ₂ = 2π²/27`, … ; #3628,
`qbeta_c3_phib_kappa_tower_scale_probe.py`, `qbeta_c3_borel_pade_resummation_probe.py`).

At the **substrate** the fluctuation variable is **imaginary**, `2πb² = i·t` with
`t = ln q₀ ∈ ℝ` (`b = √(ln q₀ / 2π)·e^{iπ/4}`, so `2πb² = i·ln q₀`). This file
proves the **bar-parity selection rule** that organizes the tower into the two
faces of `𝔙 = Vol + i·CS`:

* **Even rungs feed `Re 𝔙 = Vol` (bar-even / mass).** `(i·t)^{2m}·κ` is real:
  `Im = 0` (`even_rung_real`). Since `(i·t)² = −t²` is real, every even power is
  real, so the even sub-tower is the volume/mass channel.
* **Odd rungs feed `Im 𝔙 = CS` (bar-odd / decay = the c₃ `S`).** `(i·t)^{2m+1}·κ`
  is purely imaginary: `Re = 0` (`odd_rung_imaginary`). The single factor of `i`
  left after pairing makes every odd power imaginary, so the odd sub-tower is the
  Chern–Simons / bar-odd `S` channel.

This is the Lean root of the "even Ohtsuki rungs → `Vol`, odd rungs → the bar-odd
`S`" split used across the merged c₃-wall thread (#3600/#3636/#3654/#3675/#3682):
the sign-flip lives entirely in the **odd** (imaginary) sub-tower, and the
Borel–Padé resummation (`qbeta_c3_borel_pade_resummation_probe.py`) resums that
odd sub-tower to the exact smooth `Im 𝔙` with no Stokes ambiguity on the
imaginary ray.

Base ring is `ℂ` by necessity (§7c archimedean side): the `Re`/`Im` projections
against the imaginary substrate direction are the content. No `sorry`; no `c_k`
wired.

-- Ref: [leitner2026] conj:im-q-physical-role
-- Ref: [leitner2026] computations/qbeta/qbeta_c3_borel_pade_resummation_probe.py (Ohtsuki κ-tower)
-- Ref: [murakami-murakami2001] complex volume 𝔙 = Vol + i·CS
-/

namespace QOU.QBeta.OhtsukiTowerBarParity

/-- **The paired imaginary factor is real:** `(i·t)² = −t²`, cast of a real. The
    single squaring that turns the imaginary substrate direction into a real
    scalar — the seed of the even/odd parity split. -/
theorem imaginary_sub_sq (t : ℝ) :
    (Complex.I * (t : ℂ)) ^ 2 = ((-(t ^ 2) : ℝ) : ℂ) := by
  rw [mul_pow, Complex.I_sq]; push_cast; ring

/-- **Even rung ⇒ real ⇒ feeds `Re 𝔙 = Vol` (bar-even / mass channel).** For a
    real coefficient `κ`, the `2m`-th tower rung at the imaginary substrate
    `x = i·t` has vanishing imaginary part: `Im((i·t)^{2m}·κ) = 0`. Pairing the
    imaginary factors via `(i·t)² = −t²` (real) leaves `(−t²)^m·κ`, a real
    number. So every even Ohtsuki rung contributes to the volume/mass face of
    `𝔙`, never to the bar-odd `S`. -/
theorem even_rung_real (t κ : ℝ) (m : ℕ) :
    ((Complex.I * (t : ℂ)) ^ (2 * m) * (κ : ℂ)).im = 0 := by
  have h : (Complex.I * (t : ℂ)) ^ (2 * m) * (κ : ℂ) = (((-(t ^ 2)) ^ m * κ : ℝ) : ℂ) := by
    rw [pow_mul, imaginary_sub_sq]; push_cast; ring
  rw [h, Complex.ofReal_im]

/-- **Odd rung ⇒ imaginary ⇒ feeds `Im 𝔙 = CS` (bar-odd / decay = the c₃ `S`).**
    For a real coefficient `κ`, the `2m+1`-th tower rung at the imaginary
    substrate `x = i·t` has vanishing real part: `Re((i·t)^{2m+1}·κ) = 0`.
    Pairing the imaginary factors leaves one factor of `i`, so the rung is
    `((−t²)^m·t·κ)·i`, purely imaginary. So every odd Ohtsuki rung contributes to
    the Chern–Simons / bar-odd `S` face of `𝔙`, never to the volume/mass. This is
    where the c₃ bar-odd sign-flip lives; the Borel resummation of exactly this
    odd sub-tower gives the exact smooth `Im 𝔙`. -/
theorem odd_rung_imaginary (t κ : ℝ) (m : ℕ) :
    ((Complex.I * (t : ℂ)) ^ (2 * m + 1) * (κ : ℂ)).re = 0 := by
  have h : (Complex.I * (t : ℂ)) ^ (2 * m + 1) * (κ : ℂ)
      = (((-(t ^ 2)) ^ m * t * κ : ℝ) : ℂ) * Complex.I := by
    rw [pow_succ, pow_mul, imaginary_sub_sq]; push_cast; ring
  rw [h, Complex.mul_I_re, Complex.ofReal_im, neg_zero]

/-- **Leading odd rung `κ₁` is the bar-odd `S` carrier** (`n = 1`, `m = 0`): the
    `i·t·κ₁` term (`κ₁ = 11√3π/108`; the finite-`b` `Im 𝔙_b ≈ 0.058` scale, #3654)
    is purely imaginary, `Re = 0`. Concrete instance of `odd_rung_imaginary`. -/
theorem kappa1_rung_imaginary (t κ₁ : ℝ) :
    ((Complex.I * (t : ℂ)) ^ 1 * (κ₁ : ℂ)).re = 0 := by
  simpa using odd_rung_imaginary t κ₁ 0

/-- **First even rung `κ₂` is a volume/mass correction** (`n = 2`, `m = 1`): the
    `(i·t)²·κ₂ = −t²·κ₂` term (`κ₂ = 2π²/27`) is real, `Im = 0`. Concrete
    instance of `even_rung_real`. -/
theorem kappa2_rung_real (t κ₂ : ℝ) :
    ((Complex.I * (t : ℂ)) ^ 2 * (κ₂ : ℂ)).im = 0 := by
  simpa using even_rung_real t κ₂ 1

end QOU.QBeta.OhtsukiTowerBarParity
