import Mathlib.Tactic

/-!
# QOU.FluidDynamics.pair_viscous_core_race

**The viscous core-growth race** — the PDE-anchored leg of the
model-to-PDE uniformity question (bean `qou-ohaz`), for the
anti-parallel pair-collision channel.

The two-regime model (`pair_phase1_riccati.lean`,
`rem:townsend-biot-savart-strain`, `rem:hyperbolic-overlap-saturation`)
engages its regularizing overlap cutoff when the core scale reaches the
separation.  Its core-growth law (`V₁' = αV₁`, strain-driven) is the
model's *least* PDE-grounded ingredient.  This file proves that the
cutoff engagement does **not** depend on it:

viscous diffusion alone grows a vortex core as `a²(t) = a₀² + 4νt` —
the **Lamb–Oseen** law, an *exact* solution of the Navier–Stokes
equations for a single diffusing vortex — while the phase-1 approach
shrinks the separation as `d²(t) = d₀² − (Γ/π)t`.  Both are linear in
`t`, so the race is elementary: for every `ν > 0` the lines cross at

  `t_ov = (d₀² − a₀²)/(Γ/π + 4ν)`,

which is strictly positive and strictly before the inviscid collision
time `t* = πd₀²/Γ`, with strictly positive separation at crossing.
**Overlap engages before collision even with zero strain-driven core
growth.**  Combined with the `Γ(t)`-robustness of the strain-driven
race (`overlap_at_small_separation`), the pair channel now has two
independent in-model regularization channels, one of them anchored to
an exact NS solution.

**Scope (honest).**  The Lamb–Oseen law is exact for a *single*
axisymmetric vortex; applying it per-core during the approach is a
localization hypothesis (the same one Biot–Savart approach itself
uses).  What this file does NOT address: 3D effects absent from the
two-regime model entirely (Crow instability, axial core flow) — those
remain the open content of bean `qou-ohaz`.  Statements are over a
generic linearly ordered field (§7c): the race is pure order/field
algebra; no `Real.exp` is needed because only the core-variance law,
not the full Lamb–Oseen profile, enters.
-/

namespace QOU.FluidDynamics.PairViscousRace

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Viscous (Lamb–Oseen) core variance: `a²(t) = a₀² + 4νt`. -/
def coreSq (a0sq ν t : K) : K := a0sq + 4 * ν * t

/-- Phase-1 separation-squared (as in `pair_phase1_riccati`):
    `d²(t) = d₀² − r·t` with `r = Γ/π`. -/
def sepSq (d0sq r t : K) : K := d0sq - r * t

/-- The crossing time of the linear race:
    `t_ov = (d₀² − a₀²)/(r + 4ν)`. -/
def tOverlap (d0sq a0sq r ν : K) : K := (d0sq - a0sq) / (r + 4 * ν)

section Race

variable (d0sq a0sq r ν : K)

/-- The crossing time is strictly positive. -/
theorem tOverlap_pos (hr : 0 < r) (hν : 0 < ν) (hlt : a0sq < d0sq) :
    0 < tOverlap d0sq a0sq r ν := by
  unfold tOverlap
  have hden : 0 < r + 4 * ν := by nlinarith
  exact div_pos (by linarith) hden

/-- **The race is won strictly before the inviscid collision time**
    `t* = d₀²/r`: viscosity's head start (`a₀² ≥ 0`) and its own
    contribution to the closing speed both shorten the crossing. -/
theorem tOverlap_lt_collision (hr : 0 < r) (hν : 0 < ν) (ha : 0 ≤ a0sq)
    (hlt : a0sq < d0sq) : tOverlap d0sq a0sq r ν < d0sq / r := by
  unfold tOverlap
  have hden : 0 < r + 4 * ν := by nlinarith
  have hd0 : 0 < d0sq := lt_of_le_of_lt ha hlt
  rw [div_lt_div_iff₀ hden hr]
  nlinarith

/-- At the crossing time the core exactly meets the separation:
    `a²(t_ov) = d²(t_ov)` (the overlap condition engages). -/
theorem core_meets_sep_at_tOverlap (hr : 0 < r) (hν : 0 < ν) :
    coreSq a0sq ν (tOverlap d0sq a0sq r ν)
      = sepSq d0sq r (tOverlap d0sq a0sq r ν) := by
  unfold coreSq sepSq tOverlap
  have hden : r + 4 * ν ≠ 0 := by nlinarith
  field_simp
  ring

/-- **Positive separation at overlap**: the cutoff engages while the
    pair is still separated — `d²(t_ov) > 0`.  (Explicitly,
    `d²(t_ov) = (4ν·d₀² + r·a₀²)/(r + 4ν)`.) -/
theorem sep_pos_at_tOverlap (hr : 0 < r) (hν : 0 < ν) (ha : 0 ≤ a0sq)
    (hlt : a0sq < d0sq) : 0 < sepSq d0sq r (tOverlap d0sq a0sq r ν) := by
  unfold sepSq tOverlap
  have hden : 0 < r + 4 * ν := by nlinarith
  have hd0 : 0 < d0sq := lt_of_le_of_lt ha hlt
  rw [sub_pos, ← mul_div_assoc, div_lt_iff₀ hden]
  -- goal: r·(d₀² − a₀²) < d₀²·(r + 4ν), i.e. 0 < 4ν·d₀² + r·a₀²
  nlinarith

/-- **The viscous race summary**: for every positive viscosity the
    overlap condition engages at a strictly positive time, strictly
    before the inviscid collision time, at strictly positive
    separation — with *no* strain-driven core growth assumed.  The
    two-regime model's regularizing cutoff is therefore robust to
    removing its least-PDE-grounded ingredient: the diffusive
    (Lamb–Oseen, exact-NS) channel alone forces engagement. -/
theorem viscous_race_won (hr : 0 < r) (hν : 0 < ν) (ha : 0 ≤ a0sq)
    (hlt : a0sq < d0sq) :
    0 < tOverlap d0sq a0sq r ν ∧
    tOverlap d0sq a0sq r ν < d0sq / r ∧
    coreSq a0sq ν (tOverlap d0sq a0sq r ν)
      = sepSq d0sq r (tOverlap d0sq a0sq r ν) ∧
    0 < sepSq d0sq r (tOverlap d0sq a0sq r ν) :=
  ⟨tOverlap_pos d0sq a0sq r ν hr hν hlt,
   tOverlap_lt_collision d0sq a0sq r ν hr hν ha hlt,
   core_meets_sep_at_tOverlap d0sq a0sq r ν hr hν,
   sep_pos_at_tOverlap d0sq a0sq r ν hr hν ha hlt⟩

end Race

end QOU.FluidDynamics.PairViscousRace
