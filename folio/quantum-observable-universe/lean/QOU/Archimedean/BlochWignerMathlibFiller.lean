import Mathlib.Tactic
import QOU.Archimedean.BlochWignerUnitCircle


/-!
# Bloch-Wigner dilogarithm `D` — repo-internal Mathlib filler

The Bloch-Wigner dilogarithm `D : ℂ \ {0,1} → ℝ` is the
single-valued version of `Im Li_2(z)`:

  D(z) := Im(Li_2(z)) + log|z| · arg(1 - z).

On the unit circle `z = e^{iθ}` (where `|z| = 1`, `log|z| = 0`),
`D` simplifies to the Clausen function:

  D(e^{iθ}) = Cl_2(θ).

This is the case relevant to the QOU framework's hyperbolic-knot
contributions:

* Figure-8 shape parameter `e^{iπ/3}` → `D(e^{iπ/3}) = Cl_2(π/3)`,
  yielding `Vol(4_1) = 2 · Cl_2(π/3)`.
* Borromean per-octahedron shape parameter `i = e^{iπ/2}` →
  `D(i) = Cl_2(π/2) = G` (Catalan), yielding
  `Vol(B_3) = 8G = 8 · Cl_2(π/2)` after the 4-tetrahedra-per-
  octahedron decomposition.

This file provides:

* `BlochWigner_unit_circle : ℝ → ℝ` — the BW dilogarithm
  restricted to unit-circle shape parameters, defined as `Cl_2`.
* `BlochWigner_unit_circle_zero` — `D(e^{i·0}) = D(1) = 0`
  (boundary; `Li_2(1) = π²/6` real, imaginary part zero).
* The figure-8 and Borromean BW values exposed as named carriers.

Mathlib gaps still open after this filler:

* General `D : ℂ \ {0,1} → ℝ` for non-unit-circle shape
  parameters — needs `Complex.log` and `Complex.arg` infrastructure
  with branch-cut handling.
* The 5-term pentagon identity for `D` — proved via Bloch's
  functional equation; full proof needs the general `D`.
* `BlochSuslinUniqueness D` instance — depends on the pentagon
  identity plus the K-theoretic injectivity of the Suslin map.

-- Ref: [leitner2026] prop:archimedean-functor-uniqueness
-- Ref: [leitner2026] rem:figure-8-archimedean-illustration
-- Ref: [leitner2026] binding-scale-catalan
-- Ref: [bloch2000]
-- Ref: [zagier1986] DOI 10.1007/BFb0084581
-/

namespace QOU.Archimedean

/-- The **Bloch-Wigner dilogarithm restricted to the unit circle**:
    for `z = e^{iθ}` with `|z| = 1`, the boundary correction
    `log|z| · arg(1-z)` vanishes, leaving
    `D(e^{iθ}) = Im(Li_2(e^{iθ})) = Cl_2(θ)`.
    Imported from `QOU.Archimedean.BlochWignerUnitCircle` (bean `qou-tc8y`). -/
-- Ref: [zagier1986], [bloch2000]
@[simp] theorem BlochWigner_unit_circle_eq_Cl_2 (θ : ℝ) :
    BlochWigner_unit_circle θ = Cl_2 θ := by
  unfold BlochWigner_unit_circle
  ring

/-- **Boundary lemma:** `D(e^{i · 0}) = D(1) = 0`. -/
@[simp] theorem BlochWigner_unit_circle_zero :
    BlochWigner_unit_circle 0 = 0 := by
  unfold BlochWigner_unit_circle
  exact Cl_2_zero

/-- **Figure-8 BW value carrier:** `D(e^{iπ/3}) = Cl_2(π/3)`. The
    shape parameter `e^{iπ/3}` is the regular ideal tetrahedron
    realising the 2-tetrahedra triangulation of the figure-8 knot
    complement (Thurston 1978). -/
-- Ref: [thurston1978], [zagier1986]
noncomputable def BlochWigner_figure_8_per_tetrahedron : ℝ :=
  BlochWigner_unit_circle (Real.pi / 3)

/-- **Borromean per-octahedron BW value:** the regular ideal
    octahedron decomposes into 4 ideal tetrahedra of shape
    parameter `i = e^{iπ/2}`, each contributing
    `D(i) = Cl_2(π/2) = G` (Catalan constant). The
    per-octahedron BW value is therefore `4 · Cl_2(π/2) = 4G`. -/
-- Ref: [leitner2026] binding-scale-catalan
noncomputable def BlochWigner_Borromean_per_octahedron : ℝ :=
  4 * BlochWigner_unit_circle (Real.pi / 2)

/-- **Identity: `Vol(4_1) = 2 · BW_figure_8_per_tetrahedron`.**

    Direct combination of the Thurston 2-tetrahedra triangulation
    with the BW dilogarithm formula. Sorry-free by definition. -/
-- Ref: [thurston1978]
theorem Vol_figure_8_eq_two_BW_tetrahedron :
    Vol_figure_8 = 2 * BlochWigner_figure_8_per_tetrahedron := by
  unfold Vol_figure_8 BlochWigner_figure_8_per_tetrahedron
        BlochWigner_unit_circle
  rfl

/-- **Identity: `Vol(B_3) = 2 · BW_Borromean_per_octahedron`.**

    Via the 2-octahedra decomposition of the Borromean rings
    complement, each octahedron contributing `4G = 4 Cl_2(π/2)`.
    Sorry-free by definition. -/
-- Ref: [leitner2026] binding-scale-catalan
theorem Vol_Borromean_eq_two_BW_octahedron :
    Vol_Borromean = 2 * BlochWigner_Borromean_per_octahedron := by
  unfold Vol_Borromean BlochWigner_Borromean_per_octahedron
        BlochWigner_unit_circle
  ring

end QOU.Archimedean
