import QOU.MassTheory.NahmBlochBridge

/-!
# Nahm data of the lepton bundles: the state sum beyond `4₁`

`NahmBlochBridge` proves that a symmetric Nahm datum `N` defines a Bloch class: every
solution of `1 − z_i = ∏_j z_j ^ N_ij` gives `∑_i [z_i] ∈ B(F)`. It reads the datum
off a state sum only for `4₁`. `TwistKnotNahm` does it for `5₂` from Masbaum's
sum. This file does it for the mapping tori of the lepton words (bean `qou-35a8`,
PR #9835): under `B₃ → SL(2, ℤ)`, `σ₀ ↦ R`, `σ₁⁻¹ ↦ L`, so

* `e  = Δ` is periodic (trace `0`): no hyperbolic bundle, no datum;
* `4₁ = RL`  (trace 3, two tetrahedra) is the neutral control;
* `μ  = σ₀²σ₁⁻¹ ↦ R²L` (trace 4, three tetrahedra);
* `τ  = σ₀⁴σ₁⁻¹ ↦ R⁴L` (trace 6, five tetrahedra).

## Where the datum comes from

The Floyd–Hatcher layered triangulation of the once-punctured-torus bundle of a word
in `R, L` (one tetrahedron per letter) gives Neumann–Zagier rows
`∏_j z_j ^ a_j (1 − z_j) ^ b_j = ±1`; these rows are produced from the word by
`computations/probes/nz_gluing_from_braid_monodromy_probe.py`, with no SnapPy input.
Keep all edge rows but one, add one cusp row, and call the square blocks `A` and `B`.
The `Φ_b` state integral of that triangulation (the `sinh`-lattice sum) has
quadratic form `−B⁻¹A` in its exponent, and its saddle-point equations are the Nahm
equations of `N = −B⁻¹A`. That `N` is symmetric is the Neumann–Zagier symplectic
property (`A Bᵀ` symmetric). So the datum is computed from the word and is not
chosen to match anything.

For each word this file records:

* the rows `A`, `B` and the identity `A + B N = 0` (`*_rect_identity`), which says
  that `N` is `−B⁻¹A`: on a Nahm solution every chosen gluing row holds;
* `N` is symmetric (`*_isSymm`);
* an exact solution in a number field, with all signs `+1` (`*Solution`);
* its Nahm class lies in `B(F)` (`*Class_mem_blochGroup`).

## The exact shapes

* `4₁ = RL`: `N = [[0, −1], [−1, 0]]`, shapes `(ω, ω)` with `ω² − ω + 1 = 0`. Its class
  is `fig8Class ω`: the same class as the datum `−I`, in a different polarization.
* `μ = R²L`: `N = [[−1, −1, −1], [−1, 0, −1], [−1, −1, 0]]`, shapes
  `(y + 1/2, y, y)` with `2y² − 3y + 2 = 0`, i.e. `y = (3 + √−7)/4`. The field is
  `ℚ(√−7)`. These are the shapes `(5 + √−7)/4, (3 + √−7)/4, (3 + √−7)/4` that the
  probe found for the complete structure.
* `τ = R⁴L`: a symmetric `5 × 5` datum, shapes in the cubic field `ℚ(s)`,
  `s³ − 6s² + 8s − 4 = 0` (polynomial discriminant `−176 = −2⁴·11`):
  `(1/2 + s − s²/4, 2s − s², 1/2 + s − s²/4, s, s)`.

Each equation is checked by exact polynomial division by the minimal polynomial; no
number is measured or fitted.

## Scope

Pre-Archimedean only: no `ℝ`, `ℂ`, limit or regulator. That these exact roots are the
geometric (complete-structure) shapes, and the volumes of the bundles, are the probe's
numerical identification and live outside this file; the regulator belongs under
`QOU/Transcendental/`. The datum depends on the polarization (which edge row is
dropped and which cusp curve is added); the class `∑ [z_i]` does not. That the
`Φ_b` state integral has the saddle equations `1 − z = z^{−B⁻¹A}` is cited, not proved.

-- Ref: [dimofte-garoufalidis2013] Dimofte, Garoufalidis, The quantum content of the gluing equations, Geom. Topol. 17 (2013) 1253-1315.
-- Ref: [andersen-kashaev2014] Andersen, Kashaev, A TQFT from quantum Teichmüller theory, Comm. Math. Phys. 330 (2014) 887-934.
-- Ref: [gueritaud2006] Guéritaud, On canonical triangulations of once-punctured torus bundles and two-bridge link complements, Geom. Topol. 10 (2006) 1239-1284.
-- Ref: [nahm2007] Nahm, Conformal field theory and torsion elements of the Bloch group, in Frontiers in Number Theory, Physics and Geometry II (2007) 67-132.
-/

namespace QOU.Archimedean.LeptonBundleNahm

open QOU.Archimedean.PreArchimedeanBloch QOU.Archimedean.NahmBlochBridge

set_option linter.unusedSectionVars false
set_option linter.unusedSimpArgs false

noncomputable section

variable {F : Type*} [Field F] [DecidableEq F]

/-- A unit given with an explicit inverse. -/
def mkU (z zi : F) (h : z * zi = 1) : Fˣ := ⟨z, zi, h, by rw [mul_comm]; exact h⟩

/-! ## `4₁ = RL`: the neutral control -/

/-- The Nahm datum of the `RL` bundle (the figure-eight complement). -/
def rlNahm : Matrix (Fin 2) (Fin 2) ℤ := !![0, -1; -1, 0]

/-- Gluing rows of the `RL` layering: one edge row and one cusp row. -/
def rlRectA : Matrix (Fin 2) (Fin 2) ℤ := !![-1, -1; 1, 0]
def rlRectB : Matrix (Fin 2) (Fin 2) ℤ := !![-1, -1; 0, 1]

theorem rl_rect_identity : rlRectA + rlRectB * rlNahm = 0 := by decide

theorem rlNahm_isSymm : rlNahm.IsSymm := by decide

/-- The `RL` solution `(ω, ω)`, `ω² − ω + 1 = 0`. -/
def rlSolution {ω : F} (h : ω ^ 2 - ω + 1 = 0) : NahmSolution F (Fin 2) rlNahm where
  w _ := mkU ω (1 - ω) (by linear_combination -h)
  nahm i := by
    fin_cases i <;> simp [Fin.prod_univ_two, rlNahm, mkU]

/-- **The `RL` class is the figure-eight class.** -/
theorem rlClass_eq_fig8Class {ω : F} (h : ω ^ 2 - ω + 1 = 0) :
    nahmClass (rlSolution h) = fig8Class ω := by
  simp only [fig8Class, nahmClass, nahmSum, rlSolution, mkU, Finset.sum_const,
    Finset.card_univ, Fintype.card_fin, QuotientAddGroup.mk_nsmul]

/-! ## `μ = σ₀²σ₁⁻¹ ↦ R²L` -/

/-- The Nahm datum of the `R²L` bundle. -/
def muNahm : Matrix (Fin 3) (Fin 3) ℤ := !![-1, -1, -1; -1, 0, -1; -1, -1, 0]

/-- Gluing rows of the `R²L` layering: two edge rows and one cusp row. -/
def muRectA : Matrix (Fin 3) (Fin 3) ℤ := !![-2, 0, 0; 0, -1, -1; 1, -1, 0]
def muRectB : Matrix (Fin 3) (Fin 3) ℤ := !![2, -2, -2; -2, 1, 1; -2, 2, 1]

/-- `N = −B⁻¹A`: on a Nahm solution the chosen gluing rows hold. -/
theorem mu_rect_identity : muRectA + muRectB * muNahm = 0 := by decide

theorem muNahm_isSymm : muNahm.IsSymm := by decide

variable [CharZero F]

/-- The `R²L` solution `(y + 1/2, y, y)`, `2y² − 3y + 2 = 0`. -/
def muSolution {y : F} (hy : 2 * y ^ 2 - 3 * y + 2 = 0) : NahmSolution F (Fin 3) muNahm where
  w := ![mkU (1 / 2 + y) (1 - 1 / 2 * y) (by linear_combination (-1 / 4 : F) * hy),
         mkU y (3 / 2 - y) (by linear_combination (-1 / 2 : F) * hy),
         mkU y (3 / 2 - y) (by linear_combination (-1 / 2 : F) * hy)]
  nahm i := by
    fin_cases i
    · simp [Fin.prod_univ_three, muNahm, mkU]
      linear_combination (-7 / 8 + 1 / 4 * y : F) * hy
    · simp [Fin.prod_univ_three, muNahm, mkU]
      linear_combination (-1 / 4 : F) * hy
    · simp [Fin.prod_univ_three, muNahm, mkU]
      linear_combination (-1 / 4 : F) * hy

/-- **The `μ` class is a Bloch class.** -/
theorem muClass_mem_blochGroup {y : F} (hy : 2 * y ^ 2 - 3 * y + 2 = 0) :
    nahmClass (muSolution hy) ∈ BlochGroup F :=
  nahmClass_mem_blochGroup muNahm_isSymm _

/-- The generator is `(3 + r)/4` with `r² = −7`. -/
theorem mu_generator_of_sqrt {r : F} (hr : r ^ 2 = -7) :
    2 * ((3 + r) / 4) ^ 2 - 3 * ((3 + r) / 4) + 2 = 0 := by
  linear_combination (1 / 8 : F) * hr

/-! ## `τ = σ₀⁴σ₁⁻¹ ↦ R⁴L` -/

/-- The Nahm datum of the `R⁴L` bundle. -/
def tauNahm : Matrix (Fin 5) (Fin 5) ℤ :=
  !![-1, -2, -2, -2, 0;
     -2, -2, -2, -1, -1;
     -2, -2, -1, 0, -2;
     -2, -1, 0, 2, -3;
     0, -1, -2, -3, 2]

/-- Gluing rows of the `R⁴L` layering: four edge rows and one cusp row. -/
def tauRectA : Matrix (Fin 5) (Fin 5) ℤ :=
  !![-1, 0, -1, 0, 0;
     0, -1, 0, 0, -1;
     -1, 0, -1, 0, 0;
     0, -1, 0, -1, 0;
     -2, 0, 0, 2, -2]
def tauRectB : Matrix (Fin 5) (Fin 5) ℤ :=
  !![1, 0, 1, -2, -2;
     -2, 1, 0, 0, 1;
     1, -2, 1, 0, 0;
     0, 1, -2, 1, 0;
     2, 0, 0, -2, -2]

theorem tau_rect_identity : tauRectA + tauRectB * tauNahm = 0 := by decide

theorem tauNahm_isSymm : tauNahm.IsSymm := by decide

/-- The two shapes of `R⁴L` that are not `s` itself. -/
def tauA (s : F) : F := 1 / 2 + s - 1 / 4 * s ^ 2
def tauB (s : F) : F := 2 * s - s ^ 2

/-- `(z ^ n)⁻¹ = zi ^ n` once `z⁻¹ = zi`. -/
theorem pow_inv_of {z zi : F} (h : z⁻¹ = zi) (n : ℕ) : (z ^ n)⁻¹ = zi ^ n := by
  rw [← inv_pow, h]

theorem tauA_inv {s : F} (hs : s ^ 3 - 6 * s ^ 2 + 8 * s - 4 = 0) :
    (tauA s)⁻¹ = 2 - 2 * s + s ^ 2 :=
  inv_eq_of_mul_eq_one_right (by unfold tauA; linear_combination (-1 / 4 * s : F) * hs)

theorem tauB_inv {s : F} (hs : s ^ 3 - 6 * s ^ 2 + 8 * s - 4 = 0) :
    (tauB s)⁻¹ = 1 - 1 / 4 * s :=
  inv_eq_of_mul_eq_one_right (by unfold tauB; linear_combination (1 / 4 : F) * hs)

theorem tauS_inv {s : F} (hs : s ^ 3 - 6 * s ^ 2 + 8 * s - 4 = 0) :
    s⁻¹ = 2 - 3 / 2 * s + 1 / 4 * s ^ 2 :=
  inv_eq_of_mul_eq_one_right (by linear_combination (1 / 4 : F) * hs)

/-- The `R⁴L` solution in the cubic field `s³ − 6s² + 8s − 4 = 0`. -/
def tauSolution {s : F} (hs : s ^ 3 - 6 * s ^ 2 + 8 * s - 4 = 0) :
    NahmSolution F (Fin 5) tauNahm where
  w := ![mkU (tauA s) (2 - 2 * s + s ^ 2) (by unfold tauA; linear_combination (-1 / 4 * s : F) * hs),
         mkU (tauB s) (1 - 1 / 4 * s) (by unfold tauB; linear_combination (1 / 4 : F) * hs),
         mkU (tauA s) (2 - 2 * s + s ^ 2) (by unfold tauA; linear_combination (-1 / 4 * s : F) * hs),
         mkU s (2 - 3 / 2 * s + 1 / 4 * s ^ 2) (by linear_combination (1 / 4 : F) * hs),
         mkU s (2 - 3 / 2 * s + 1 / 4 * s ^ 2) (by linear_combination (1 / 4 : F) * hs)]
  nahm i := by
    fin_cases i
    · simp [Fin.prod_univ_five, tauNahm, mkU]
      simp only [zpow_ofNat, pow_inv_of (tauA_inv hs), pow_inv_of (tauB_inv hs), pow_inv_of (tauS_inv hs)]
      try unfold tauA
      try unfold tauB
      linear_combination (63 / 8 - 24 * s + 297 / 8 * s ^ 2 - 1161 / 32 * s ^ 3 + 769 / 32 * s ^ 4
        - 703 / 64 * s ^ 5 + 109 / 32 * s ^ 6 - 87 / 128 * s ^ 7 + 5 / 64 * s ^ 8
        - 1 / 256 * s ^ 9 : F) * hs
    · simp [Fin.prod_univ_five, tauNahm, mkU]
      simp only [zpow_ofNat, pow_inv_of (tauA_inv hs), pow_inv_of (tauB_inv hs), pow_inv_of (tauS_inv hs)]
      try unfold tauA
      try unfold tauB
      linear_combination (63 / 4 - 64 * s + 1041 / 8 * s ^ 2 - 2733 / 16 * s ^ 3 + 631 / 4 * s ^ 4
        - 1701 / 16 * s ^ 5 + 845 / 16 * s ^ 6 - 613 / 32 * s ^ 7 + 315 / 64 * s ^ 8
        - 27 / 32 * s ^ 9 + 11 / 128 * s ^ 10 - 1 / 256 * s ^ 11 : F) * hs
    · simp [Fin.prod_univ_five, tauNahm, mkU]
      simp only [zpow_ofNat, pow_inv_of (tauA_inv hs), pow_inv_of (tauB_inv hs), pow_inv_of (tauS_inv hs)]
      try unfold tauA
      try unfold tauB
      linear_combination (63 / 8 - 24 * s + 297 / 8 * s ^ 2 - 1161 / 32 * s ^ 3 + 769 / 32 * s ^ 4
        - 703 / 64 * s ^ 5 + 109 / 32 * s ^ 6 - 87 / 128 * s ^ 7 + 5 / 64 * s ^ 8
        - 1 / 256 * s ^ 9 : F) * hs
    · simp [Fin.prod_univ_five, tauNahm, mkU]
      simp only [zpow_ofNat, pow_inv_of (tauA_inv hs), pow_inv_of (tauB_inv hs), pow_inv_of (tauS_inv hs)]
      try unfold tauA
      try unfold tauB
      linear_combination (-1 / 4 - 1 / 4 * s + 63 / 8 * s ^ 2 - 319 / 16 * s ^ 3 + 101 / 4 * s ^ 4
        - 157 / 8 * s ^ 5 + 635 / 64 * s ^ 6 - 209 / 64 * s ^ 7 + 43 / 64 * s ^ 8
        - 5 / 64 * s ^ 9 + 1 / 256 * s ^ 10 : F) * hs
    · simp [Fin.prod_univ_five, tauNahm, mkU]
      simp only [zpow_ofNat, pow_inv_of (tauA_inv hs), pow_inv_of (tauB_inv hs), pow_inv_of (tauS_inv hs)]
      try unfold tauA
      try unfold tauB
      linear_combination (-1 / 4 - 1 / 4 * s + 63 / 8 * s ^ 2 - 319 / 16 * s ^ 3 + 101 / 4 * s ^ 4
        - 157 / 8 * s ^ 5 + 635 / 64 * s ^ 6 - 209 / 64 * s ^ 7 + 43 / 64 * s ^ 8
        - 5 / 64 * s ^ 9 + 1 / 256 * s ^ 10 : F) * hs

/-- **The `τ` class is a Bloch class.** -/
theorem tauClass_mem_blochGroup {s : F} (hs : s ^ 3 - 6 * s ^ 2 + 8 * s - 4 = 0) :
    nahmClass (tauSolution hs) ∈ BlochGroup F :=
  nahmClass_mem_blochGroup tauNahm_isSymm _

/-- The `τ` cubic has polynomial discriminant `−176 = −2⁴ · 11`
(`b²c² − 4c³ − 4b³d − 27d² + 18bcd` at `(b, c, d) = (−6, 8, −4)`). -/
theorem tau_cubic_discriminant :
    (-6 : ℤ) ^ 2 * 8 ^ 2 - 4 * 8 ^ 3 - 4 * (-6) ^ 3 * (-4) - 27 * (-4) ^ 2
      + 18 * (-6) * 8 * (-4) = -176 := by norm_num

end

end QOU.Archimedean.LeptonBundleNahm
