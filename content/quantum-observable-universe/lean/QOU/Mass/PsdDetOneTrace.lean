/-
# A PSD matrix of determinant one has trace at least two — and exactly two only
# when it is the identity

Bean `qou-99qc`. Companion to
`computations/qbeta/qbeta_gamma_gamma_sdp_feasibility_probe.py`.

## Why this exists

`QOU.Mass.GammaGammaWordSelection.SDPSelected` requires a candidate word to be
**PSD-feasible**: every Wedderburn projection `π_λ(w)` is `Matrix.PosSemidef`.
On `H₃` the γγ vertex `σ₀σ₁⁻¹` projects to the two one-dimensional blocks as
`1` (both of them), and to the `(2,1)` block as a real `2×2` matrix `V` with

    det V = 1        and        tr V = −1 − h²,      h = q − q⁻¹

(measured exactly in the companion probe, in the orthogonal Hoefsmit basis).
So `|tr V| < 2` for every `q` with `h² < 1`, i.e. `V` is **elliptic**: its
eigenvalues lie on the unit circle and every power `Vᵏ` again has determinant
`1`.

The lemma below is what turns that into an exclusion, and it is the only part
of the argument that is not a computation. It says a real symmetric PSD `2×2`
matrix of determinant one cannot have trace below `2`, and has trace exactly
`2` only when it is the identity. Since `tr(Vᵏ) = 2cos(kθ) ≤ 2` for an elliptic
`V`, a PSD `Vᵏ` is forced to have trace exactly `2`, hence to **be** the
identity.

Consequence, spelled out because it is the point: **a γγ word on three strands
is PSD-feasible only if its `(2,1)` projection is the identity matrix.** The
companion probe measures that this does not happen for any `k` in the range it
tests, and that `V³ = 1` forces `q = 1` — so the Borromean baryon `(σ₀σ₁⁻¹)³`
is SDP-feasible only in the classical limit.

## Scope

This file proves the `2×2` obstruction and nothing else. It does **not** claim
the γγ route is excluded — that would need the ellipticity and the eigenvalue
argument formalised too, and the `q`-independence of the trace formula, none of
which is here. What it removes is the possibility that the probe's exclusion
rests on an arithmetic accident: the obstruction is a theorem.

## Base ring (§7c)

`ℝ` throughout, deliberately: `Matrix.PosSemidef` needs a `StarOrderedRing`
and the trace bound needs an order. This is an archimedean statement and lives
on the archimedean side of the wall.
-/
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Data.Real.StarOrdered
import Mathlib.Tactic

namespace QOU.Mass.PsdDetOneTrace

open Matrix

variable {M : Matrix (Fin 2) (Fin 2) ℝ}

/-- The diagonal entries of a real PSD matrix are non-negative. -/
theorem diag_nonneg (h : M.PosSemidef) (i : Fin 2) : 0 ≤ M i i := by
  simpa using h.2 (Pi.single i 1)

/-- A real PSD `2×2` matrix is symmetric in the off-diagonal entries. -/
theorem offdiag_symm (h : M.PosSemidef) : M 0 1 = M 1 0 := by
  have h1 := h.1
  have := congrArg (fun A => A 1 0) h1
  simpa [Matrix.conjTranspose_apply] using this

/-- **The obstruction.** A real symmetric PSD `2×2` matrix of determinant `1`
has trace at least `2`. -/
theorem trace_ge_two (h : M.PosSemidef) (hdet : M.det = 1) : 2 ≤ M.trace := by
  have ha : 0 ≤ M 0 0 := diag_nonneg h 0
  have hd : 0 ≤ M 1 1 := diag_nonneg h 1
  have hsym : M 0 1 = M 1 0 := offdiag_symm h
  have hdet' : M 0 0 * M 1 1 - M 0 1 * M 1 0 = 1 := by
    simpa [Matrix.det_fin_two] using hdet
  have htr : M.trace = M 0 0 + M 1 1 := by
    simp [Matrix.trace_fin_two]
  have hdet2 : M 0 0 * M 1 1 - M 0 1 ^ 2 = 1 := by
    rw [← hsym] at hdet'; nlinarith [hdet']
  have hprod : 1 ≤ M 0 0 * M 1 1 := by nlinarith [sq_nonneg (M 0 1), hdet2]
  rw [htr]
  have hab : 0 ≤ M 0 0 + M 1 1 := by linarith
  nlinarith [sq_nonneg (M 0 0 - M 1 1), hprod, hab]

/-- **The equality case.** Trace exactly `2` forces the identity. -/
theorem eq_one_of_trace_eq_two (h : M.PosSemidef) (hdet : M.det = 1)
    (htr : M.trace = 2) : M = 1 := by
  have ha : 0 ≤ M 0 0 := diag_nonneg h 0
  have hd : 0 ≤ M 1 1 := diag_nonneg h 1
  have hsym : M 0 1 = M 1 0 := offdiag_symm h
  have hdet' : M 0 0 * M 1 1 - M 0 1 * M 1 0 = 1 := by
    simpa [Matrix.det_fin_two] using hdet
  have hsum : M 0 0 + M 1 1 = 2 := by
    simpa [Matrix.trace_fin_two] using htr
  have hdet2 : M 0 0 * M 1 1 - M 0 1 ^ 2 = 1 := by
    rw [← hsym] at hdet'; nlinarith [hdet']
  have hb2 : M 0 1 ^ 2 = 0 := by
    nlinarith [sq_nonneg (M 0 0 - M 1 1), sq_nonneg (M 0 1), hdet2, hsum]
  have hb : M 0 1 = 0 := by
    have := sq_eq_zero_iff.mp hb2; exact this
  have hb' : M 1 0 = 0 := by rw [← hsym, hb]
  have h00 : M 0 0 = 1 := by nlinarith [sq_nonneg (M 0 0 - 1), hb2, hdet2, hsum]
  have h11 : M 1 1 = 1 := by linarith
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [h00, h11, hb, hb']

/-- **What the two together say**, in the form the probe uses: for a
determinant-one real `2×2` matrix whose trace is *strictly below* `2`, being
PSD is impossible. An elliptic `SL₂(ℝ)` element's powers all have determinant
one and trace at most `2`, so this is the exclusion. -/
theorem not_posSemidef_of_trace_lt_two (hdet : M.det = 1) (htr : M.trace < 2) :
    ¬ M.PosSemidef := fun h => absurd (trace_ge_two h hdet) (not_le.mpr htr)

end QOU.Mass.PsdDetOneTrace
