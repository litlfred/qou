import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.Mass.MassVolDensity — Mass = Vol × Density (algebraic core)

The algebraic heart of the **Mass = Vol × Density** decomposition that
replaces the `Geom_full` black box with proper definitions:

    m(K) = m_e · Vol(K) · ρ(q) / ℏ_q²

- **Vol(K)** — hyperbolic volume of the complement, an *input* constant
  (Vol(𝓑₃) = 8·G, Adams 1985, asserted as the axiom `vol_B3_eq_8_catalan`
  in `QOU/Archimedean/BorromeanVolumeCatalan.lean`). We do **NOT** derive
  Vol from the Hecke trace — that is the Kashaev volume conjecture, kept
  strictly out of scope. Vol enters only as a measured/literature constant.
- **ρ(q)** — the **density**: the Hecke-energy linking weight, a purely
  *algebraic* rational function in `q`. This file proves its two forms agree.
- **ℏ_q = (q−1)/q** — the substrate Planck quantum.

## Scope discipline (owner directive 2026-06-04: keep algebraic)

Everything here is an algebraic `q`-identity provable by `field_simp; ring`.
No hyperbolic-volume analysis, no quantum dilogarithm, no Kashaev. The
volume side stays in `QOU/Archimedean/*` (Lobachevsky / Catalan), where the
q-hyperbolic machinery is already cleanly separated and Vol is an axiom.
The Kashaev `Vol = lim tr_M` link is touched only as a special-case sanity
check (q = 1 / unknot), never as a dependency.

This file is the P2′ + δ-structural layer of the roadmap
`docs/workplans/2026-06-04-mass-vol-density-stokes-delta-formalization.md`.
P1 assembly (combining the proved `geom_leading_eq_8G_over_hbar_q_sq` with
`density_borromean`) and the P3/P4 Stokes-interface holonomy follow as
separate files once these algebraic identities are CI-verified.

> **Verification status.** The Lean toolchain / Mathlib cache is
> network-unreachable in the authoring session, so these proofs are written
> against the proved `field_simp; ring` patterns of
> `BorromeanVolumeCatalan.geom_leading_eq_8G_over_hbar_q_sq` and
> `HadronicMass.delta_m_factored_eq_closed` but are **pending `lean_ci.yml`
> build confirmation**. The identities are hand-verified (see each `/-- … -/`).
-/

namespace QOU.Mass

/-! ## §1  The density (Hecke linking weight) and its two algebraic forms -/

/-- The substrate Planck quantum `ℏ_q = (q − 1)/q`. Local copy of
    `QOU.hbar_q` to keep this algebraic-core file import-light. -/
noncomputable def hbar_q (q : ℝ) : ℝ := (q - 1) / q

/-- The Hecke crossing scale `h = q − q⁻¹`. -/
noncomputable def h_crossing (q : ℝ) : ℝ := q - q⁻¹

/-- **Density ρ(q)** for the Borromean nucleon 𝓑₃ — the Family-A Hecke
    linking weight, in the manifestly symmetric `q`-power form

      `ρ(q) = (3 q² + 4 + 3 q⁻²) / 4`.

    This is the energy density that multiplies `Vol(𝓑₃)/ℏ_q²` in the mass
    formula; it is the partition-weighted Markov trace `Σ_λ y_λ χ^λ(𝓑₃)`
    (the Wedderburn form `(1/4) Σ_{λ⊢4} dim_q V_λ` is proved in
    `QOU/BraidsAndKnots/BorromeanMarkovTrace.lean`). -/
noncomputable def density_borromean (q : ℝ) : ℝ :=
  (3 * q ^ 2 + 4 + 3 * q ^ (-2 : ℤ)) / 4

/-- **P2′ — density agrees with the `5/2 + 3h²/4` linking-weight form.**

    `(3 q² + 4 + 3 q⁻²) / 4 = 5/2 + 3·(q − q⁻¹)² / 4`.

    Hand-check: `(q − q⁻¹)² = q² − 2 + q⁻²`, so `3(q−q⁻¹)²/4 =
    (3q² − 6 + 3q⁻²)/4`, and `5/2 + that = (10 + 3q² − 6 + 3q⁻²)/4 =
    (3q² + 4 + 3q⁻²)/4`. Pure algebra; `field_simp; ring` after `q ≠ 0`.
    This is the bridge between the `q`-power density and the `lwA` form
    (`QOU/BraidKnot/TwoRoutesProtonMass.lean`). -/
theorem density_borromean_eq_linking_weight (q : ℝ) (hq : q ≠ 0) :
    density_borromean q = 5 / 2 + 3 * h_crossing q ^ 2 / 4 := by
  unfold density_borromean h_crossing
  field_simp
  ring

/-! ## §2  The flavor split δ as an algebraic q-rational

    δ enters the p-n interface crossing `σ − h·(½ − δ/4)·𝟙` (the
    `bring_color_weighted` convention). Here δ is purely algebraic — a
    rational function of `q` — exactly what keeps the interface holonomy
    in the Hecke/algebraic world rather than the hyperbolic one. -/

/-- **δ leading** = `(q − 1)²·(1 − q⁻⁴)/3` — the substrate flavor split
    `Δm/M_N` at leading order (`prop:flavor-split-substrate`). Equal to the
    existing `HadronicMass.delta_m_over_M_N_substrate q = (q−1)²(q⁴−1)/(3q⁴)`
    via `1 − q⁻⁴ = (q⁴ − 1)/q⁴`. -/
noncomputable def delta_leading (q : ℝ) : ℝ :=
  (q - 1) ^ 2 * (1 - q ^ (-4 : ℤ)) / 3

/-- **δ leading agrees with the existing closed polynomial form.**

    `(q − 1)²·(1 − q⁻⁴)/3 = (q − 1)²·(q⁴ − 1)/(3 q⁴)`.

    Pins `delta_leading` to `HadronicMass.delta_m_over_M_N_substrate`
    without importing it. Pure algebra (`field_simp; ring`, `q ≠ 0`). -/
theorem delta_leading_eq_closed (q : ℝ) (hq : q ≠ 0) :
    delta_leading q = (q - 1) ^ 2 * (q ^ 4 - 1) / (3 * q ^ 4) := by
  unfold delta_leading
  field_simp
  ring

/-- **δ subleading** = `δ_leading · (1 + ℏ_q³)` — the full flavor split
    with the 3-loop substrate-Planck correction (`flavor_split_subleading`
    in `_li_2_q_util.py`; matches `_avg_color_delta()` to 2.6e-19). The
    factor `(1 + ℏ_q³)` is the algebraic image of the 3-loop term in the
    surface-ordered (non-abelian Stokes) holonomy expansion — see the P3/P4
    follow-up. Still purely algebraic in `q`. -/
noncomputable def delta_subleading (q : ℝ) : ℝ :=
  delta_leading q * (1 + hbar_q q ^ 3)

/-- The p-n interface crossing coefficient `d(q) = −h·(½ − δ/4)` of the
    color-weighted averaged crossing `σ + d·𝟙` (here δ = `delta_subleading`).
    This is the algebraic object whose holonomy P3 will identify with the
    non-abelian-Stokes interface curvature; recording it as a `def` fixes
    the target of that derivation. -/
noncomputable def pn_crossing_coeff (q : ℝ) : ℝ :=
  - h_crossing q * (1 / 2 - delta_subleading q / 4)

/-- Sanity: at the color-blind limit `δ = 0` the interface crossing
    coefficient is the symmetric average `−h/2` (the `strict_averaged`
    convention). Stated as the `δ ↦ 0` specialisation; the genuine
    `delta_subleading q = 0` only at `q = 1` (unknot/trivial limit), which
    is the one place the algebraic and hyperbolic pictures must agree. -/
theorem pn_crossing_coeff_color_blind (q : ℝ) (hδ : delta_subleading q = 0) :
    pn_crossing_coeff q = - h_crossing q / 2 := by
  unfold pn_crossing_coeff
  rw [hδ]
  ring

end QOU.Mass
