import QOU.BraidKnot.HabiroNewtonLadder

/-!
# QOU.BraidKnot.AJFigureEightTelescope

**Division-free split-product bookkeeping for the 4₁ certificate telescope
(bean `udmw`, foundational tranche).**

The one remaining `sorry` in `QOU.BraidKnot.AJFigureEight` (general-`N`
annihilation) is discharged, corpus-side, by the qZeilberger certificate
(`computations/aj_figure_eight_certificate.py`; content Lean-proved in
`QOU.BraidKnot.AJFigureEightCertificate`).  Assembling it in Lean requires
telescoping values whose *rational* form has denominators
`(q^k − q^N)(q^k − q^{N+1})` — these vanish both at the tower boundary
`k ∈ {N, N+1}` and at roots of unity, while the class field quantifies over
ALL `q ≠ 0`.  The assembly must therefore be **division-free**: this file
provides the split-product layer it stands on.

## Contents (all sorry-free)

* `risingA q x k = ∏_{j<k} (x − q^{j+1})`, `risingB q x k = ∏_{j<k} (x·q^{j+1} − 1)`
  — the two halves of the Newton-ladder element after clearing.
* `ladder_factor_split` — the per-factor identity
  `(x + x⁻¹ − λ_{j+1}) · (x q^{j+1}) = (x − q^{j+1})(x q^{j+1} − 1)`.
* `newtonLadder_split` — the cleared ladder:
  `g_k(x + x⁻¹) · ∏_{j<k} (x q^{j+1}) = risingA · risingB`, generic `x ≠ 0`.
* `newtonLadder_lam_split` — the specialization `x = q^N` used by the
  colored Jones tower.
* `risingA_shift` / `risingB_shift` — the color-shift (`N → N+1`, i.e.
  `x → q·x`) relations that produce the certificate ratios `r₁, r₂`
  division-free.

## Base ring (§7c)

The split products and their shift relations are polynomial identities —
generic `{R : Type*} [CommRing R]`.  Only the split of the ladder *at*
`x + x⁻¹` (which touches the nodes `λ_j = q^j + q^{−j}`) needs
`{K : Type*} [Field K]`.  Everything is algebraic — no `ℝ`, no ordering,
no archimedean constructs.
-/

namespace QOU.BraidKnot.AJFigureEight

open Finset
open QOU.BraidKnot.HabiroNewtonLadder

section SplitProducts
variable {R : Type*} [CommRing R]

/-- First split half: `A(k) = ∏_{j<k} (x − q^{j+1})` — carries the
    termination zeros (`x = q^N` kills it at `k ≥ N`). -/
def risingA (q x : R) (k : ℕ) : R :=
  ∏ j ∈ Finset.range k, (x - q ^ (j + 1))

/-- Second split half: `B(k) = ∏_{j<k} (x·q^{j+1} − 1)` — pole-free on the
    tower (at `x = q^N` it vanishes only at roots of unity). -/
def risingB (q x : R) (k : ℕ) : R :=
  ∏ j ∈ Finset.range k, (x * q ^ (j + 1) - 1)

@[simp] theorem risingA_zero (q x : R) : risingA q x 0 = 1 := by
  simp [risingA]

@[simp] theorem risingB_zero (q x : R) : risingB q x 0 = 1 := by
  simp [risingB]

theorem risingA_succ (q x : R) (k : ℕ) :
    risingA q x (k + 1) = risingA q x k * (x - q ^ (k + 1)) := by
  unfold risingA; rw [Finset.prod_range_succ]

theorem risingB_succ (q x : R) (k : ℕ) :
    risingB q x (k + 1) = risingB q x k * (x * q ^ (k + 1) - 1) := by
  unfold risingB; rw [Finset.prod_range_succ]

/-- **Color shift for `A` (division-free)**: shifting `x → q·x` (one color
    up, `N → N+1`) and one rung up factors as
    `A_{qx}(k+1) = q^{k+1} · (x − 1) · A_x(k)` — the `(x − 1)` is the
    `(1 − 1/x)`-numerator of the certificate ratio `r₁`, cleared. -/
theorem risingA_shift (q x : R) (k : ℕ) :
    risingA q (q * x) (k + 1) = q ^ (k + 1) * (x - 1) * risingA q x k := by
  induction k with
  | zero => simp [risingA]; ring
  | succ k ih =>
      rw [risingA_succ, ih, risingA_succ]
      have hstep : q * x - q ^ (k + 1 + 1) = q * (x - q ^ (k + 1)) := by
        rw [pow_succ]; ring
      rw [hstep, pow_succ]
      ring

/-- **Color shift for `B` (division-free)**: shifting `x → q·x` re-indexes
    the nodes one step up, so prepending the lowest factor recovers the
    unshifted product one rung higher:
    `(x·q − 1) · B_{qx}(k) = B_x(k+1)`. -/
theorem risingB_shift (q x : R) (k : ℕ) :
    (x * q - 1) * risingB q (q * x) k = risingB q x (k + 1) := by
  unfold risingB
  rw [Finset.prod_range_succ']
  have h : ∀ j ∈ Finset.range k,
      q * x * q ^ (j + 1) - 1 = x * q ^ (j + 1 + 1) - 1 := by
    intro j _
    rw [pow_succ]; ring
  rw [Finset.prod_congr rfl h]
  ring

end SplitProducts

/-! ## Splitting the ladder at `x + x⁻¹` — the tower face (needs a field) -/

section LadderSplit
variable {K : Type*} [Field K]

/-- **Per-factor split**: clearing the single denominator `x·q^{j+1}` of a
    ladder factor at `x + x⁻¹` splits it into the two linear halves. -/
theorem ladder_factor_split {q x : K} (hq : q ≠ 0) (hx : x ≠ 0) (j : ℕ) :
    (x + x⁻¹ - lam q (j + 1)) * (x * q ^ (j + 1))
      = (x - q ^ (j + 1)) * (x * q ^ (j + 1) - 1) := by
  have hqj : q ^ (j + 1) ≠ 0 := pow_ne_zero _ hq
  unfold lam
  field_simp
  ring

/-- **The cleared Newton ladder (division-free)**: multiplying the ladder
    element at `x + x⁻¹` by the product of the per-factor denominators
    yields the split product `A(k)·B(k)`.  Generic in `x ≠ 0` — the tower
    case is `x = q^N` (`newtonLadder_lam_split`). -/
theorem newtonLadder_split {q x : K} (hq : q ≠ 0) (hx : x ≠ 0) (k : ℕ) :
    newtonLadder (lam q) (x + x⁻¹) k * ∏ j ∈ Finset.range k, (x * q ^ (j + 1))
      = risingA q x k * risingB q x k := by
  induction k with
  | zero => simp
  | succ k ih =>
      rw [newtonLadder_succ, Finset.prod_range_succ, risingA_succ, risingB_succ]
      calc (x + x⁻¹ - lam q (k + 1)) * newtonLadder (lam q) (x + x⁻¹) k
            * ((∏ j ∈ Finset.range k, (x * q ^ (j + 1))) * (x * q ^ (k + 1)))
          = (newtonLadder (lam q) (x + x⁻¹) k
              * ∏ j ∈ Finset.range k, (x * q ^ (j + 1)))
            * ((x + x⁻¹ - lam q (k + 1)) * (x * q ^ (k + 1))) := by ring
        _ = risingA q x k * risingB q x k
            * ((x - q ^ (k + 1)) * (x * q ^ (k + 1) - 1)) := by
              rw [ih, ladder_factor_split hq hx]
        _ = risingA q x k * (x - q ^ (k + 1))
            * (risingB q x k * (x * q ^ (k + 1) - 1)) := by ring

/-- The tower specialization `x = q^N`: the colored-Jones ladder element,
    cleared, is the split product. -/
theorem newtonLadder_lam_split {q : K} (hq : q ≠ 0) (N k : ℕ) :
    newtonLadder (lam q) (lam q N) k
        * ∏ j ∈ Finset.range k, (q ^ N * q ^ (j + 1))
      = risingA q (q ^ N) k * risingB q (q ^ N) k := by
  have hx : (q : K) ^ N ≠ 0 := pow_ne_zero _ hq
  have hlam : lam q N = q ^ N + (q ^ N)⁻¹ := rfl
  rw [hlam]
  exact newtonLadder_split hq hx k

end LadderSplit

end QOU.BraidKnot.AJFigureEight
