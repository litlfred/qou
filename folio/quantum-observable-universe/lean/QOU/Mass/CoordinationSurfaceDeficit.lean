import QOU.Mass.CoordinationSaturation
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics

/-!
# QOU.Mass.CoordinationSurfaceDeficit — the boundary deficit of a bounded-degree bond count

`QOU.Mass.CoordinationSaturation` proves the structural dichotomy: complete-graph coordination
gives unbounded `B/A` (refuted by saturation), bounded-degree coordination gives **constant**
`B/A = ε·k/2`. That constant is a *pure volume term*: `perNucleonBounded` counts `k·A/2` bonds,
i.e. it gives **every** nucleon `k` neighbours.

A finite cluster cannot do that. Nucleons on the boundary have fewer neighbours than interior
ones, so the true bond count is smaller than `k·A/2` by a **boundary deficit**. This file is the
exact bookkeeping of that deficit and what it does to `B/A`.

## The result

Split `A = A_int + A_surf` with interior degree `k` and surface degree `k' ≤ k`. Handshake gives

    M(A) = (k·A_int + k'·A_surf)/2 = k·A/2 − (k − k')·A_surf/2         (`bondCount_split`)

so, with a single uniform per-bond energy `ε` (the only arrangement-invariant regime, by
`QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff`),

    B(A)/A = ε·k/2 − (ε(k − k')/2)·(A_surf/A)                          (`perNucleon_split`)

**The first term is the SEMF volume term and the second is a deficit with the SEMF sign.** Its
`A`-dependence is carried entirely by the surface fraction `A_surf/A`, so the shape of the
correction is a question about the *geometry of the cluster*, not about the algebra.

Feeding in the compact-packing surface law `A_surf = c·A^{2/3}` — stated as a **hypothesis**,
see the scope note — gives exactly

    B(A)/A = ε·k/2 − (ε·c·(k − k')/2)·A^(−1/3)                         (`perNucleon_surfaceLaw`)

which is the volume-minus-surface form of the semi-empirical mass formula, with **no constant
beyond the packing data `(k, k', c)`**. Two corollaries worth having:

* `perNucleon_lt_plateau` — the deficit is strictly negative when `k' < k` and `A_surf > 0`, so
  the plateau is approached **from below**: `B/A < ε·k/2` at every finite `A`.
* `perNucleon_tendsto_plateau` — `B/A → ε·k/2` as `A → ∞` under the surface law, so
  `CoordinationSaturation.bounded_degree_saturates` is recovered as the limit. This file
  **refines** that lemma, it does not contradict it.

And the ratio the data can be checked against is scale-free:

    a_S / a_V = c·(k − k')/k                                            (`surfaceToVolume_ratio`)

`ε` cancels, so this is a pure-geometry prediction testable against the measured residual shape.

## Scope — what is proved and what is assumed

* **Proved:** the handshake decomposition, the per-nucleon split, the SEMF shape under the
  surface law, approach from below, the `A → ∞` limit, and the scale-free ratio. All exact,
  no fit, `ε, k, k', c` free.
* **Assumed (hypothesis, not proved here):** that the coordination graph is a compact 3-D
  packing whose surface count obeys `A_surf = c·A^{2/3}`. That is standard packing geometry
  and is *stated as a hypothesis* everywhere it is used; proving an isoperimetric bound for
  sphere packings is not attempted.
* **NOT derived, and this is the honest gap:** that the substrate *emits* such a coordination
  graph. #6611's decision frame §5.2 asks for an edge set derived **from the braid geometry**;
  this file assumes a packing instead, which is a weaker input. The linking-vs-self-energy
  amplitude assignment (`qou-brng`) remains the open input, exactly as
  `CoordinationSaturation` records.
* **Not a fit.** No coefficient here is chosen against data. The probe
  `computations/probes/coordination_surface_deficit_probe.py` measures what ratio the AME data
  want and compares; it does not search on it.

Ground ring `ℝ` (§7c: archimedean — real powers `A^(2/3)` and an order claim).

-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/CoordinationSaturation.lean
-- Ref: [leitner2026] docs/audits/2026-09-04-normalised-law-residual-shape.md
-/

namespace QOU.Mass.CoordinationSurfaceDeficit

open QOU.Mass.CoordinationSaturation

/-- Total bond count of a cluster with `A_int` interior nucleons of degree `k` and `A_surf`
boundary nucleons of degree `k'`, by the handshake lemma. Real-valued so the surface law can
be fed in continuously. -/
noncomputable def bondCount (k k' : ℝ) (Aint Asurf : ℝ) : ℝ := (k * Aint + k' * Asurf) / 2

/-- **The boundary deficit, exactly.** With `A = A_int + A_surf`, the bond count is the
uniform-degree count `k·A/2` minus `(k − k')·A_surf/2`. -/
theorem bondCount_split (k k' Aint Asurf A : ℝ) (hA : A = Aint + Asurf) :
    bondCount k k' Aint Asurf = k * A / 2 - (k - k') * Asurf / 2 := by
  unfold bondCount
  rw [hA]; ring

/-- **Per-nucleon binding splits into a volume term and a boundary deficit.** With one uniform
per-bond energy `ε`, `B/A = ε·k/2 − (ε(k−k')/2)·(A_surf/A)`. The `A`-dependence of the
correction lives entirely in the surface fraction. -/
theorem perNucleon_split (ε k k' Aint Asurf A : ℝ) (hA : A = Aint + Asurf) (hA0 : A ≠ 0) :
    ε * bondCount k k' Aint Asurf / A
      = ε * k / 2 - (ε * (k - k') / 2) * (Asurf / A) := by
  rw [bondCount_split k k' Aint Asurf A hA]
  field_simp

/-- **The plateau is approached from below.** If the surface degree is strictly smaller
(`k' < k`) and the cluster has a boundary (`A_surf > 0`), the per-nucleon binding is strictly
less than the uniform-degree plateau `ε·k/2`. -/
theorem perNucleon_lt_plateau (ε k k' Aint Asurf A : ℝ) (hε : 0 < ε) (hkk : k' < k)
    (hsurf : 0 < Asurf) (hA : A = Aint + Asurf) (hApos : 0 < A) :
    ε * bondCount k k' Aint Asurf / A < ε * k / 2 := by
  rw [perNucleon_split ε k k' Aint Asurf A hA (ne_of_gt hApos)]
  have hfrac : 0 < Asurf / A := div_pos hsurf hApos
  have hcoef : 0 < ε * (k - k') / 2 := by
    have : 0 < k - k' := sub_pos.mpr hkk
    positivity
  nlinarith [mul_pos hcoef hfrac]

/-! ## The compact-packing surface law -/

/-- The surface count of a compact 3-D packing, **as a hypothesis**: `A_surf = c·A^(2/3)`. -/
noncomputable def surfaceCount (c A : ℝ) : ℝ := c * A ^ ((2 : ℝ) / 3)

/-- **The SEMF volume-minus-surface shape, exactly.** Under the packing surface law the
per-nucleon binding is `ε·k/2 − (ε·c·(k−k')/2)·A^(−1/3)` — the volume term and the surface
term of the semi-empirical mass formula, with no constant beyond `(ε, k, k', c)`. -/
theorem perNucleon_surfaceLaw (ε k k' c A : ℝ) (hApos : 0 < A)
    (Aint : ℝ) (hA : A = Aint + surfaceCount c A) :
    ε * bondCount k k' Aint (surfaceCount c A) / A
      = ε * k / 2 - (ε * c * (k - k') / 2) * A ^ (-(1 : ℝ) / 3) := by
  rw [perNucleon_split ε k k' Aint (surfaceCount c A) A hA (ne_of_gt hApos)]
  unfold surfaceCount
  have hpow : A ^ ((2 : ℝ) / 3) / A = A ^ (-(1 : ℝ) / 3) := by
    calc A ^ ((2 : ℝ) / 3) / A
        = A ^ ((2 : ℝ) / 3) / A ^ ((1 : ℝ)) := by rw [Real.rpow_one]
      _ = A ^ ((2 : ℝ) / 3 - (1 : ℝ)) := (Real.rpow_sub hApos _ _).symm
      _ = A ^ (-(1 : ℝ) / 3) := by norm_num
  rw [show c * A ^ ((2 : ℝ) / 3) / A = c * (A ^ ((2 : ℝ) / 3) / A) by ring, hpow]
  ring

/-- **The surface-to-volume coefficient ratio is scale-free.** `ε` cancels, so
`a_S/a_V = c·(k−k')/k` is a pure-geometry number, testable against the measured residual
shape with no scale input. -/
theorem surfaceToVolume_ratio (ε k k' c : ℝ) (hε : ε ≠ 0) (hk : k ≠ 0) :
    (ε * c * (k - k') / 2) / (ε * k / 2) = c * (k - k') / k := by
  field_simp

/-- **The limit recovers saturation.** Under the surface law, `B/A → ε·k/2` as `A → ∞`: this
file refines `CoordinationSaturation.bounded_degree_saturates` (which is the plateau itself)
by giving the `A^(−1/3)` approach to it, and does not contradict it. -/
theorem perNucleon_tendsto_plateau (ε k k' c : ℝ) :
    Filter.Tendsto
      (fun A : ℝ => ε * k / 2 - (ε * c * (k - k') / 2) * A ^ (-(1 : ℝ) / 3))
      Filter.atTop (nhds (ε * k / 2)) := by
  have hrpow : Filter.Tendsto (fun A : ℝ => A ^ (-(1 : ℝ) / 3)) Filter.atTop (nhds 0) := by
    have h := tendsto_rpow_neg_atTop (y := (1 : ℝ) / 3) (by norm_num)
    simpa [neg_div] using h
  have := ((hrpow.const_mul (ε * c * (k - k') / 2)).const_sub (ε * k / 2))
  simpa using this

end QOU.Mass.CoordinationSurfaceDeficit
