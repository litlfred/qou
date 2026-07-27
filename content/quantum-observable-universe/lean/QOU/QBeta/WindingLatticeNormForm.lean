import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Data.ZMod.Basic

/-!
# The winding lattice of a braid-word geodesic: two quadratic orders, one parity

**Why only one of the two orders can carry a sign flip.**

A braid word's particle/vortex path closes to a geodesic on the cusp torus, a
class `(m, ℓ)` in the cusp lattice `ℤ⟨1, ω⟩`. With the meridian log-holonomy
`ln q₀` (`meridian-holonomy-boost`, proved) and the `4₁` cusp shape
`ω = e^{iπ/3}` (`cusp-shape-bar-parity`, proved), the imaginary part of the
complex volume collapses onto an integer binary quadratic form. This file
formalises the two facts that decide which order can produce a sign flip:

* **disc 12** — the cusp-torus order `ℤ[√3]`. Its fundamental unit `2 + √3` has
  norm `+1`, so *every* power has norm `+1` (`pell3_norm`). A parity-driven sign
  flip is structurally **unavailable** here.
* **disc 5** — Bring's golden order `ℤ[φ]`, `φ = (1+√5)/2`. Its fundamental unit
  `φ` has norm `−1`, so the norm of `φⁿ` alternates: `(−1)ⁿ`
  (`goldenPow_norm`). A parity-driven sign flip **exists** here.

The one-line reason is `normPhi_step` versus `norm3_step`: the golden recursion
`(a,b) ↦ (b, a+b)` *negates* the norm at each step, while the silver recursion
`(a,b) ↦ (2a+3b, a+2b)` *preserves* it.

Everything here is `ring`-level algebra over a generic `CommRing` (§7c) or over
`ℤ`; no archimedean structure, no ordering, no `ℝ`. The elements `s` and the
basis vector `φ` appear only through their defining relations (`s * s = 3`;
`φ² = φ + 1`), so nothing depends on a choice of real square root.

Companion probes: `computations/qbeta/qbeta_cusp_lattice_geodesic_probe.py`
(the disc-12 identity, 5 assertions) and
`computations/qbeta/qbeta_disc5_parity_probe.py` (the parity contrast,
4 assertions).

**Scope.** These are theorems about the two quadratic orders. They do **not**
establish that the physical S-channel sign is given by the winding parity: that
link is derived only on the cusp torus and is transported to Bring's surface by
analogy in the companion probe, where it is labelled conjectural.
-/

namespace QOU.QBeta.WindingLatticeNormForm

section CuspTorusForm

variable {R : Type*} [CommRing R]

/-- **The winding Lorentz form (disc 12).** For the geodesic `u = c·(m + ℓω)`
with cusp shape `ω = (1 + s)/2` where `s * s = 3` (i.e. `s` stands for `√3`,
`ω = e^{iπ/3}`), the doubled real and imaginary parts are `c(2m+ℓ)` and `c·ℓ·s`,
and the indefinite pairing `Re² − Im²` collapses onto the integer form
`(2m+ℓ)² − 3ℓ²` — the norm form of `ℤ[√3]`.

Stated over a generic `CommRing` with `s` given only by `s * s = 3`, so it holds
for any base ring carrying a square root of `3`; no ordering is used. -/
theorem winding_lorentz_form (c s m l : R) (hs : s * s = 3) :
    (c * (2 * m + l)) ^ 2 - (c * l * s) ^ 2
      = c ^ 2 * ((2 * m + l) ^ 2 - 3 * l ^ 2) := by
  linear_combination (-(c ^ 2 * l ^ 2)) * hs

end CuspTorusForm

/-! ### The silver order `ℤ[√3]` (disc 12): the norm is preserved -/

/-- Powers of the fundamental unit `2 + √3`, in the basis `(1, √3)`:
`(a, b)` represents `a + b√3`, and multiplying by `2 + √3` sends
`(a, b) ↦ (2a + 3b, a + 2b)`. -/
def pell3 : ℕ → ℤ × ℤ
  | 0 => (1, 0)
  | n + 1 => (2 * (pell3 n).1 + 3 * (pell3 n).2, (pell3 n).1 + 2 * (pell3 n).2)

/-- The norm form of `ℤ[√3]`: `N(a + b√3) = a² − 3b²`. -/
def norm3 (p : ℤ × ℤ) : ℤ := p.1 ^ 2 - 3 * p.2 ^ 2

/-- **The silver step PRESERVES the norm.** Multiplying by the fundamental unit
`2 + √3` (which has norm `+1`) leaves `a² − 3b²` unchanged. -/
theorem norm3_step (a b : ℤ) : norm3 (2 * a + 3 * b, a + 2 * b) = norm3 (a, b) := by
  simp only [norm3]
  ring

/-- **No parity flip on the cusp torus.** Every power of `2 + √3` has norm `+1`,
so the disc-12 order cannot produce a sign that alternates with the winding
number. -/
theorem pell3_norm (n : ℕ) : norm3 (pell3 n) = 1 := by
  induction n with
  | zero => simp [pell3, norm3]
  | succ k ih =>
      show norm3 (2 * (pell3 k).1 + 3 * (pell3 k).2, (pell3 k).1 + 2 * (pell3 k).2) = 1
      rw [norm3_step]
      exact ih

/-! ### Bring's golden order `ℤ[φ]` (disc 5): the norm alternates -/

/-- Powers of the fundamental unit `φ`, in the basis `(1, φ)`: `(a, b)`
represents `a + bφ`, and `φ² = φ + 1` gives `(a + bφ)·φ = b + (a + b)φ`, i.e.
`(a, b) ↦ (b, a + b)` — the Fibonacci recursion. -/
def goldenPow : ℕ → ℤ × ℤ
  | 0 => (1, 0)
  | n + 1 => ((goldenPow n).2, (goldenPow n).1 + (goldenPow n).2)

/-- The norm form of `ℤ[φ]` in the basis `(1, φ)`:
`N(a + bφ) = (a + bφ)(a + bφ̄) = a² + ab − b²`, of discriminant `5`. -/
def normPhi (p : ℤ × ℤ) : ℤ := p.1 ^ 2 + p.1 * p.2 - p.2 ^ 2

/-- **The golden step NEGATES the norm.** This single `ring` identity is the
whole parity mechanism: multiplying by `φ` (whose norm is `−1`) flips the sign
of `a² + ab − b²`. -/
theorem normPhi_step (a b : ℤ) : normPhi (b, a + b) = -normPhi (a, b) := by
  simp only [normPhi]
  ring

/-- **The parity flip on Bring's golden order.** `N(φⁿ) = (−1)ⁿ`: the norm of the
`n`-th power alternates with the parity of `n`. Contrast `pell3_norm`, where the
norm is constantly `+1`. -/
theorem goldenPow_norm (n : ℕ) : normPhi (goldenPow n) = (-1) ^ n := by
  induction n with
  | zero => simp [goldenPow, normPhi]
  | succ k ih =>
      show normPhi ((goldenPow k).2, (goldenPow k).1 + (goldenPow k).2) = (-1) ^ (k + 1)
      rw [normPhi_step, ih]
      ring

/-- **The structural contrast, in one statement.** On the cusp-torus order the
norm of every unit power is `+1`; on Bring's golden order it is `(−1)ⁿ`. Hence a
sign that alternates with the winding number is available on the disc-5 order and
structurally unavailable on the disc-12 one — which is exactly why the sign flip
must live on Bring's surface rather than on the cusp torus. -/
theorem parity_flip_iff_golden (n : ℕ) :
    norm3 (pell3 n) = 1 ∧ normPhi (goldenPow n) = (-1) ^ n :=
  ⟨pell3_norm n, goldenPow_norm n⟩

/-- The parity flip is genuine: the golden norm takes both signs. -/
theorem goldenPow_norm_alternates :
    normPhi (goldenPow 2) = 1 ∧ normPhi (goldenPow 3) = -1 := by
  constructor <;> decide

/-- **Structural exclusion (mod-3 obstruction).** The value `−1` is not
represented by the disc-12 norm form at all — by any lattice point, not merely
by unit powers: reducing `a² − 3b² = −1` mod `3` demands `a² ≡ 2 (mod 3)`, and
`2` is not a square mod `3`. This is the negative-Pell insolvability for
`D = 3`, the cited invariant behind `pell3_norm`'s "no parity flip": the norm
(Kummer/Galois norm of `ℚ(√3)/ℚ`) simply never takes the value `−1` on the
cusp-torus order, while on the golden order it does (`goldenPow_norm_alternates`,
`normPhi (goldenPow 3) = −1`). -/
theorem norm3_ne_neg_one (a b : ℤ) : norm3 (a, b) ≠ -1 := by
  simp only [norm3]
  intro h
  have hc := congrArg (fun z : ℤ => (z : ZMod 3)) h
  push_cast at hc
  revert hc
  generalize (a : ZMod 3) = x
  generalize (b : ZMod 3) = y
  revert x y
  decide

end QOU.QBeta.WindingLatticeNormForm
