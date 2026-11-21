import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

/-!
# The figure-eight gluing data from its braid monodromy — the algebraic spine

Companion to `computations/probes/nz_gluing_from_braid_monodromy_probe.py` (bean `qou-n2cl`).
The probe derives the Neumann–Zagier data of `S³ ∖ 4₁` from the canonical 3-braid
`(σ₁σ₂⁻¹)²` with no SnapPy input: Stallings monodromy → LR word → Floyd–Hatcher layering →
edge and cusp rows. The combinatorial layering is checked by the probe against five independent
facts; this file records the three algebraic identities in that chain that are theorems rather
than computations:

* `stallings_monodromy_eq` — the product of the two Dehn-twist matrices on `H₁` of the fibre,
  one per crossing column of `(σ₁σ₂⁻¹)²`, is `[[2,1],[1,1]] = R·L`; `stallings_trace_three` and
  `stallings_charpoly` give trace `3` and `det(t − φ) = t² − 3t + 1`, the Alexander polynomial of
  `4₁` (the trefoil control `σ₁σ₂σ₁σ₂ ↦ T₁T₂`, trace `1`, is `trefoil_control_trace_one`).
* `figure_eight_gluing_at_sixth_root` — the derived edge equation `z₀ z₁ (1 − z₀)(1 − z₁) = 1`
  (Thurston's) is satisfied at `z₀ = z₁ = ω` for ANY `ω` with `ω² − ω + 1 = 0`, i.e. at a
  primitive sixth root of unity; the geometric solution `e^{iπ/3}` is one of these. Stated over a
  generic commutative ring, §7c.
* `rrl_gluing_at_sqrt_minus_seven` — the R²L bundle's first derived edge equation holds at the
  exact shapes `(5 + r)/4, (3 + r)/4, (3 + r)/4` for ANY `r` with `r² = −7` in a field of
  characteristic zero; the probe identified the numeric root there and re-verified all three rows
  in `sympy`; this is the same verification as a theorem for the row that carries the content
  (the other two are its rect-form partners).

Nothing here asserts the triangulation is geometric — that is the probe's `Im z > 0` check and
its volume; these are the exact identities the geometry rests on.

-- Ref: [leitner2026] computations/probes/nz_gluing_from_braid_monodromy_probe.py
-- Ref: library/arxiv-0808.2716v4 (Futer–Kalfagianni–Purcell) §2.2 for the R, L matrices.
-- Ref: [martelli2016] §14.1 (Prop 14.1.8 + Fig 14.7: the two-tetrahedron, valence-6 triangulation
--   with all shapes e^{iπ/3} is the figure-eight complement — the literature form of the
--   sixth-root check), §15.2 (Prop 15.2.9 / 15.2.11: the incidence rows generate a Lagrangian
--   subspace — the NZ symplectic check; Cor 15.2.8: rk A = 2n − c). Not in that book: the
--   Guéritaud two-bridge layering and the Floyd–Hatcher bundle layering (keep FKP for those).
-/

namespace QOU.Mass.FigureEightGluingFromMonodromy

open Matrix

/-- Dehn twist `T_{γ₁}` on `H₁(F; ℤ)` in the basis `(γ₁, γ₂)` with `γ₁ · γ₂ = 1`. -/
def R : Matrix (Fin 2) (Fin 2) ℤ := !![1, 1; 0, 1]

/-- `T_{γ₂}⁻¹` in the same basis. -/
def L : Matrix (Fin 2) (Fin 2) ℤ := !![1, 0; 1, 1]

/-- **Stallings monodromy of `(σ₁σ₂⁻¹)²`.** Column 1 (two positive crossings) contributes
`T_{γ₁} = R`, column 2 (two negative crossings) contributes `T_{γ₂}⁻¹ = L`; the fibre is their
Murasugi sum and the monodromy their product. -/
theorem stallings_monodromy_eq : R * L = !![2, 1; 1, 1] := by
  simp [R, L]

theorem stallings_trace_three : (R * L).trace = 3 := by
  rw [stallings_monodromy_eq]; simp [Matrix.trace_fin_two]

theorem stallings_det_one : (R * L).det = 1 := by
  rw [stallings_monodromy_eq]; simp [Matrix.det_fin_two]

/-- `det(t·1 − φ) = t² − 3t + 1`: the Alexander polynomial of `4₁`. -/
theorem stallings_charpoly (t : ℤ) :
    (!![t, 0; 0, t] - R * L).det = t ^ 2 - 3 * t + 1 := by
  rw [stallings_monodromy_eq]
  simp [Matrix.det_fin_two]
  ring

/-- Control: the positive braid `σ₁σ₂σ₁σ₂` (closure the trefoil) has monodromy `T₁ T₂ = R · L⁻¹`
with trace `1`, i.e. `Δ = t² − t + 1`. -/
theorem trefoil_control_trace_one : (R * !![1, 0; -1, 1]).trace = 1 := by
  simp [R, Matrix.trace_fin_two]

section SixthRoot

variable {K : Type*} [CommRing K]

/-- **The derived figure-eight edge equation at a primitive sixth root of unity.** If
`ω² − ω + 1 = 0` then `ω (1 − ω) = 1`, hence `z₀ z₁ (1 − z₀)(1 − z₁) = 1` at `z₀ = z₁ = ω`. -/
theorem figure_eight_gluing_at_sixth_root {ω : K} (h : ω ^ 2 - ω + 1 = 0) :
    ω * ω * (1 - ω) * (1 - ω) = 1 := by
  have h1 : ω * (1 - ω) = 1 := by linear_combination -h
  calc ω * ω * (1 - ω) * (1 - ω) = (ω * (1 - ω)) * (ω * (1 - ω)) := by ring
    _ = 1 := by rw [h1, one_mul]

end SixthRoot

section RRL

variable {K : Type*} [Field K] [CharZero K]

/-- The three derived edge rows of the R²L bundle, in rect form
`Π z^a (1−z)^b`: `a = (2,1,1), b = (0,1,1)`; `a = (−2,0,0), b = (2,−2,−2)`;
`a = (0,−1,−1), b = (−2,1,1)`. At the exact shapes `z₀ = (5+r)/4`, `z₁ = z₂ = (3+r)/4` with
`r² = −7` the first row equals `1`; the other two are its inverse-type partners and follow from
the same identity. Only the first is stated; the probe verifies all three symbolically. -/
theorem rrl_gluing_at_sqrt_minus_seven {r : K} (hr : r ^ 2 = -7) :
    ((5 + r) / 4) ^ 2 * ((3 + r) / 4) * ((3 + r) / 4) * (1 - (3 + r) / 4) * (1 - (3 + r) / 4)
      = 1 := by
  -- the whole identity is `(5+r)(3+r)(1−r) = 8(1+r)(1−r) = 8(1 − r²) = 64`, squared over 4⁶
  have key : (5 + r) * (3 + r) * (1 - r) = 64 := by linear_combination (-(r + 7)) * hr
  calc ((5 + r) / 4) ^ 2 * ((3 + r) / 4) * ((3 + r) / 4) * (1 - (3 + r) / 4) * (1 - (3 + r) / 4)
      = ((5 + r) * (3 + r) * (1 - r)) ^ 2 / 4096 := by ring
    _ = 64 ^ 2 / 4096 := by rw [key]
    _ = 1 := by norm_num

end RRL

end QOU.Mass.FigureEightGluingFromMonodromy
