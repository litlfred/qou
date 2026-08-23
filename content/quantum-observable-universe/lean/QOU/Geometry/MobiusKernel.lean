import Mathlib.Tactic

/-!
# QOU.Geometry.MobiusKernel — the classical Möbius-energy integrand

The classical Möbius energy of a curve `γ` (Freedman–He–Wang) is

    E(γ) = ∫∫ ( 1/‖γ s - γ t‖² − 1/d(s,t)² ) ds dt

where `d(s,t)` is the arc-length distance. For an **arc-length
parametrised** curve `d(s,t) = |s − t|`, and arc-length parametrisation is
exactly `LipschitzWith 1 γ`.

The point of this file is that the integrand's non-negativity is **derived**
here, not assumed. It follows from the elementary chord-≤-arc inequality,
which for a 1-Lipschitz curve is immediate.

This matters because `climax-volume-mass/mobius-energy.lean` currently
carries

    energy_classical_nonneg : 0 ≤ energy_classical

as a *structure field* on `CategoricalMobiusEnergy`, with a `theorem`
projecting it straight back out. That theorem is a self-assuming projection
(AGENTS.md §3b-cond item 5) and it is unprovable there, because
`energy_classical` is an opaque real with no definition — there is nothing to
derive it *from*. This file supplies the missing subject.

Deliberately independent of the `q`-side. Nothing here mentions `q`, the
Frobenius–Hopf kernel, or the categorical connection; see beans `vta3` /
`ne0m` for why the `q → 1` identification is blocked (the framework's
transport runs along the `q`-deformation path, not along the filament, so it
carries no two-point Euclidean data).

Base ring: `ℝ` is forced (§7c) — `‖·‖`, the ordering, and division are all
archimedean. `E` stays a generic `NormedAddCommGroup`.
-/

namespace QOU.Geometry

variable {E : Type*} [NormedAddCommGroup E]

/-- The **Möbius-energy integrand** for an arc-length parametrised curve:
    the chord term minus the arc term. -/
noncomputable def mobiusKernel (γ : ℝ → E) (s t : ℝ) : ℝ :=
  1 / ‖γ s - γ t‖ ^ 2 - 1 / (s - t) ^ 2

/-- **Chord ≤ arc.** For an arc-length parametrised (`1`-Lipschitz) curve the
    straight-line distance between two points never exceeds the parameter
    distance. -/
-- Ref: [freedman1994] https://doi.org/10.2307/2118583
theorem chord_le_arc {γ : ℝ → E} (hγ : LipschitzWith 1 γ) (s t : ℝ) :
    ‖γ s - γ t‖ ≤ |s - t| := by
  have h := hγ.dist_le_mul s t
  simpa [dist_eq_norm, Real.dist_eq] using h

/-- **The Möbius integrand is pointwise non-negative** — derived from
    chord ≤ arc, at any two parameters carrying distinct points.

    This is the statement `mobius_energy_nonneg` should rest on: the energy
    is non-negative because its integrand is, not by assumption. -/
-- Ref: [freedman1994] https://doi.org/10.2307/2118583
theorem mobiusKernel_nonneg {γ : ℝ → E} (hγ : LipschitzWith 1 γ) {s t : ℝ}
    (hne : γ s ≠ γ t) : 0 ≤ mobiusKernel γ s t := by
  have h0 : 0 < ‖γ s - γ t‖ := by
    rw [norm_pos_iff, sub_ne_zero]
    exact hne
  have hle : ‖γ s - γ t‖ ≤ |s - t| := chord_le_arc hγ s t
  have habs : ‖γ s - γ t‖ ^ 2 ≤ |s - t| ^ 2 := by
    nlinarith [norm_nonneg (γ s - γ t), abs_nonneg (s - t)]
  have hsq : ‖γ s - γ t‖ ^ 2 ≤ (s - t) ^ 2 := by rwa [sq_abs] at habs
  have h0sq : (0 : ℝ) < ‖γ s - γ t‖ ^ 2 := by positivity
  rw [mobiusKernel, sub_nonneg]
  gcongr <;> assumption

/-- **Distinct parameters give distinct points, for an embedded curve.**
    Packaged so the non-negativity can be applied from an injectivity
    hypothesis rather than a pointwise one. -/
theorem mobiusKernel_nonneg_of_injective {γ : ℝ → E} (hγ : LipschitzWith 1 γ)
    (hinj : Function.Injective γ) {s t : ℝ} (hst : s ≠ t) :
    0 ≤ mobiusKernel γ s t :=
  mobiusKernel_nonneg hγ fun h => hst (hinj h)

end QOU.Geometry
