import QOU.MathlibExt.MarkovTraceInterleavedCrossTerm

/-!
# The two `n = 4` words are two *different links*: the cross term is a difference of closures

Route A, step 1, of the 2026-09-05 binding-gap survey (bean `qou-amw3`) asks whether the `n = 4`
interleaving cross term `Δ = tr(g₀g₁g₀g₂g₁) − tr(g₀²g₁²g₂) = z(z² − hz − 1)` is an Euler
characteristic — i.e. whether the categorified trace (HOMFLY-PT homology, whose graded Euler
characteristic is the two-variable Ocneanu trace) sees it as one object.

The first thing to settle is what the two words *are*, and the Markov axioms answer it exactly.
From (T1) cyclicity, (T3) stabilisation and the Hecke quadratic alone:

    tr(g₀ g₁ g₀ g₂ g₁) = z² · tr(g₀³)          (`interleaved_eq_stab_sq_cube`)
    tr(g₀² g₁² g₂)     = z  · tr(g₀²)²         (`sequential_eq_stab_sq_sq`)

The interleaved word is `σ³ ∈ B₂` after two Markov stabilisations — its closure is the (positive)
**trefoil**, one component; the sequential word is a stabilised product of two `σ²` — its closure is
the three-component **chain of two Hopf links**. So the "cross term" is the difference of two
link invariants of two different links:

    Δ = z² · tr(σ³) − z · tr(σ²)²             (`crossTerm_eq_closures`)

At the level of the polynomial both terms are Euler characteristics of Khovanov–Rozansky
homology (the trefoil's and the chain's), so *a* categorification of `Δ` always exists as a shifted
direct sum; what does **not** follow is a natural chain map between the two whose cone carries
`Δ`, because the two words are not related by any braid move (their closures have different
component counts). That negative is recorded in the probe and the survey §7d, not here.

Everything in this file is over the generic `MarkovTrace R A` structure of
`QOU.MathlibExt.OcneanuTrace` (base ring §7c: `CommRing R`), sorry-free, with the same hypotheses
as `interleaved_sub_sequential`.

-- Ref: [leitner2026] computations/probes/interleaving_cross_term_closures_probe.py
-- Ref: [jones1987] https://doi.org/10.2307/1971403 — Markov moves and the Ocneanu trace.
-/

namespace QOU.MathlibExt.InterleavedWordClosures

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.InterleavedCrossTerm

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-- `tr(g₀³) = h·(hz+1) + z`: one Hecke reduction on `g₀ · g₀²`. -/
theorem tr_g0_cube (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1) :
    T.tr (T.g 0 * T.g 0 * T.g 0) = h * (h * T.z + 1) + T.z := by
  have hw : T.g 0 * T.g 0 * T.g 0 = h • (T.g 0 * T.g 0) + T.g 0 := by
    calc T.g 0 * T.g 0 * T.g 0 = T.g 0 * (T.g 0 * T.g 0) := by rw [mul_assoc]
      _ = T.g 0 * (h • T.g 0 + 1) := by rw [hq0]
      _ = h • (T.g 0 * T.g 0) + T.g 0 := by rw [mul_add, mul_one, mul_smul_comm]
  rw [hw, map_add, map_smul, smul_eq_mul, tr_g0_sq T h hq0, tr_g0]

/-- **The interleaved word is a doubly-stabilised `σ³`.**
`tr(g₀ g₁ g₀ g₂ g₁) = z² · tr(g₀³)` — its closure is the trefoil. -/
theorem interleaved_eq_stab_sq_cube (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1)
    (hbraid : T.g 0 * T.g 1 * T.g 0 = T.g 1 * T.g 0 * T.g 1) :
    T.tr (T.g 0 * T.g 1 * T.g 0 * T.g 2 * T.g 1) = T.z ^ 2 * T.tr (T.g 0 * T.g 0 * T.g 0) := by
  rw [tr_interleaved T h hq0 hbraid, tr_g0_cube T h hq0]
  ring

/-- **The sequential word is a stabilised product of two `σ²`.**
`tr(g₀² g₁² g₂) = z · tr(g₀²)²` — its closure is the three-component chain of two Hopf links. -/
theorem sequential_eq_stab_sq_sq (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1)
    (hq1 : T.g 1 * T.g 1 = h • T.g 1 + 1) :
    T.tr (T.g 0 * T.g 0 * (T.g 1 * T.g 1) * T.g 2) = T.z * T.tr (T.g 0 * T.g 0) ^ 2 := by
  rw [tr_sequential T h hq0 hq1, tr_g0_sq T h hq0]

/-- **The cross term is a difference of two link invariants of two different links**:
`Δ = z²·tr(σ³) − z·tr(σ²)²`, trefoil minus Hopf-chain. -/
theorem crossTerm_eq_closures (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1)
    (hq1 : T.g 1 * T.g 1 = h • T.g 1 + 1)
    (hbraid : T.g 0 * T.g 1 * T.g 0 = T.g 1 * T.g 0 * T.g 1) :
    T.z * (T.z ^ 2 - h * T.z - 1)
      = T.z ^ 2 * T.tr (T.g 0 * T.g 0 * T.g 0) - T.z * T.tr (T.g 0 * T.g 0) ^ 2 := by
  rw [← interleaved_sub_sequential T h hq0 hq1 hbraid, interleaved_eq_stab_sq_cube T h hq0 hbraid,
    sequential_eq_stab_sq_sq T h hq0 hq1]

end QOU.MathlibExt.InterleavedWordClosures
