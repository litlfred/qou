import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Tactic


/-!
# Clausen function `Cl_2` — repo-internal Mathlib filler

Mathlib does not currently expose the Clausen function

  Cl_2(θ) := Σ_{k=1}^∞ sin(kθ) / k²
        = Im(Li_2(e^{iθ}))
        = -∫_0^θ ln(2 sin(t/2)) dt    (for 0 < θ < 2π)

which is the imaginary part of the dilogarithm on the unit circle and
the standard ingredient in hyperbolic-volume formulas:

  Vol(figure-8 knot 4_1)  = 2 · Cl_2(π/3)         ≈ 2.029883
  Vol(Borromean rings B_3) = 8 · Cl_2(π/2) = 8G    ≈ 7.327724

Both volumes are needed in:

* prop:em-coupling-bring-zero-mode (additive Bring zero-mode for 1/α_EM)
* rem:figure-8-archimedean-illustration (algebraic / archimedean dichotomy)
* binding-scale-catalan (Borromean = 8G nuclear binding scale)
* conj:bring-hyperbolic-knot-bloch-decomposition (K-theoretic ID search)

This file provides:

* `Cl_2 : ℝ → ℝ` as the explicit `tsum` definition — no longer
  opaque, no longer requiring `Complex.dilog`.
* Unconditional boundary lemmas (`Cl_2_zero`, `Cl_2_two_pi`).
* Periodicity / antisymmetry: proved termwise, with no Fourier theory,
  as `Cl_2_add_two_pi` and `Cl_2_neg` in
  `QOU.Archimedean.BlochWignerLobachevsky` (each term inherits `2π`-periodicity
  and oddness from `Real.sin`). Mathlib's Fourier-series API
  (`Mathlib.Analysis.Fourier.AddCircle`) exists but is not needed for them.
* The carrier `Catalan_constant := Cl_2 (π/2)` recording the
  Catalan constant identity G = Cl_2(π/2).

Mathlib gaps remaining after this file:

* `Real.dilog` (already addressed via `LiTwo` in
  dilogarithm-archimedean-limit.lean).
* `BlochGroup` — algebraic structure, quotient of free abelian group
  on `ℂ \ {0,1}` by 5-term pentagon relations; substantial.
* Suslin map `K_3^ind(ℂ) → ℝ` — depends on full BlochGroup setup.

CLOSED 2026-07-26 (no longer a gap): the functional equation
`Cl_2(2θ) = 2 Cl_2(θ) - 2 Cl_2(π - θ)` is machine-proved sorry-free on
`(0, π)` as `QOU.Knot.Cl_2_duplication` (`QOU/Knot/Clausen.lean`, Borromean
brick B1) — no Fourier identities needed, just the sine duplication under
the integral representation plus the series↔integral bridge.

CLOSED 2026-07-19 (no longer gaps): the derivative
`Cl_2'(θ) = -log(2 sin(θ/2))` and the series↔integral bridge
`Cl_2(θ) = -∫₀^θ log(2 sin(t/2)) dt` (Zagier) are machine-proved
sorry-free in `QOU/Knot/Clausen.lean` (`hasDerivAt_cl_2`,
`clausen_eq_series`, via an Abel-regularised assembly), along with
`Cl_2` continuity (`continuous_Cl_2`) and the boundary lemmas
`Cl_2_pi` / `Cl_2_two_pi` below.

-- Ref: [leitner2026] rem:figure-8-archimedean-illustration
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [leitner2026] binding-scale-catalan
-- Ref: [thurston1978] The geometry and topology of three-manifolds
-- Ref: [zagier1986] DOI 10.1007/BFb0084581
-/

namespace QOU.Archimedean

/-- The **Clausen function** `Cl_2 : ℝ → ℝ` defined by the Fourier
    series

      Cl_2(θ) := Σ_{k≥1} sin(k θ) / k²

    via Mathlib's `tsum`. The series converges absolutely and
    uniformly on all of `ℝ` (since `|sin(k θ) / k²| ≤ 1 / k²`),
    The `tsum` is well-defined and continuous. Outside the
    standard fundamental domain `[0, 2π]` the function extends
    by periodicity (`Cl_2(θ + 2π) = Cl_2(θ)`). -/
-- Ref: [zagier1986] Cl_2 in hyperbolic volume formulas
noncomputable def Cl_2 (θ : ℝ) : ℝ :=
  ∑' k : ℕ, Real.sin ((k + 1) * θ) / ((k : ℝ) + 1) ^ 2

/-- **Boundary lemma:** `Cl_2(0) = 0`. Each term is `sin(0) = 0`. -/
@[simp] theorem Cl_2_zero : Cl_2 0 = 0 := by
  unfold Cl_2
  simp

/-- **Boundary lemma:** `Cl_2(π) = 0`. Each term is
    `sin((k+1)π) = 0` (`sin` at an integer multiple of `π`). Filled in
    per the docstring's "unconditional boundary lemmas"; needs no
    Fourier infrastructure. -/
@[simp] theorem Cl_2_pi : Cl_2 Real.pi = 0 := by
  have h : ∀ k : ℕ,
      Real.sin (((k : ℝ) + 1) * Real.pi) / ((k : ℝ) + 1) ^ 2 = 0 := by
    intro k
    have hc : ((k : ℝ) + 1) = ((k + 1 : ℕ) : ℝ) := by push_cast; ring
    rw [hc, Real.sin_nat_mul_pi, zero_div]
  unfold Cl_2
  simp only [h, tsum_zero]

/-- **Boundary lemma:** `Cl_2(2π) = 0` (the right endpoint of the
    fundamental domain). Each term is `sin(2(k+1)π) = 0`. This is the
    `Cl_2_two_pi` promised in the file docstring. -/
@[simp] theorem Cl_2_two_pi : Cl_2 (2 * Real.pi) = 0 := by
  have h : ∀ k : ℕ,
      Real.sin (((k : ℝ) + 1) * (2 * Real.pi)) / ((k : ℝ) + 1) ^ 2 = 0 := by
    intro k
    have hc : ((k : ℝ) + 1) * (2 * Real.pi)
        = ((2 * (k + 1) : ℕ) : ℝ) * Real.pi := by push_cast; ring
    rw [hc, Real.sin_nat_mul_pi, zero_div]
  unfold Cl_2
  simp only [h, tsum_zero]

/-- **Catalan constant carrier:** `G = Cl_2(π/2)`. The numerical
    value `G ≈ 0.91596...` is the imaginary part of the
    dilogarithm at `i = e^{iπ/2}` and gives the per-octahedron
    contribution to the Borromean rings hyperbolic volume
    `Vol(B_3) = 8G`
    ([`binding-scale-catalan`](../braids-and-knots/binding-scale-catalan.md)). -/
-- Ref: [leitner2026] binding-scale-catalan
noncomputable def Catalan_constant : ℝ := Cl_2 (Real.pi / 2)

/-- **Figure-8 hyperbolic volume carrier.** By the Thurston
    2-tetrahedra triangulation [`thurston1978`], the figure-8 knot
    complement decomposes into 2 ideal regular tetrahedra of shape
    parameter `e^{iπ/3}`, each contributing `Cl_2(π/3)`.
    Therefore `Vol(4_1) = 2 · Cl_2(π/3)`. -/
-- Ref: [thurston1978]
-- Ref: [leitner2026] rem:figure-8-archimedean-illustration
noncomputable def Vol_figure_8 : ℝ := 2 * Cl_2 (Real.pi / 3)

/-- **Borromean rings hyperbolic volume carrier.** By the
    2-octahedron decomposition, each ideal regular octahedron
    decomposes into 4 ideal tetrahedra of shape parameter
    `i = e^{iπ/2}`, each contributing `Cl_2(π/2) = G` (Catalan).
    Per octahedron = `4G = 4·Cl_2(π/2)`; total Borromean
    volume = `8G = 8·Cl_2(π/2)`. -/
-- Ref: [leitner2026] binding-scale-catalan
noncomputable def Vol_Borromean : ℝ :=
  8 * Cl_2 (Real.pi / 2)

/-- **Borromean = 8 · Catalan_constant equality.** The standard
    identification: `G = Cl_2(π/2)` (NOT `Cl_2(π/2)`), so
    `Catalan_constant = Cl_2(π/2) = G ≈ 0.91596`. The Borromean
    rings hyperbolic volume `8G = 8·Cl_2(π/2)` decomposes via
    2 ideal regular octahedra, each of which is 4 ideal tetrahedra
    of shape parameter `i = e^{iπ/2}` contributing
    `Cl_2(π/2) = G` per tetrahedron. -/
-- Ref: [leitner2026] binding-scale-catalan §"Catalan constant"
theorem catalan_constant_eq_cl_2_pi_over_2 :
    Catalan_constant = Cl_2 (Real.pi / 2) := rfl

/-- **Borromean volume in terms of Catalan constant.** -/
theorem Vol_Borromean_eq_eight_Catalan :
    Vol_Borromean = 8 * Catalan_constant := by
  unfold Vol_Borromean Catalan_constant
  rfl

end QOU.Archimedean
