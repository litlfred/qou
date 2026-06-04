import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

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

/-! ## §3  The hyperbolic (sinh/cosh) structure of the p-n mass split

    The even/odd-δ parity (m_avg even, Δ_pn odd) is not a per-order
    accident — it is the cosh/sinh of a single hyperbolic rotation by a
    p-n rapidity θ. The q-deformation is *already* hyperbolic: writing
    `q = e^η` with `η = log q`,

        h     = q − q⁻¹ = 2 sinh η   (ODD),
        [2]_q = q + q⁻¹ = 2 cosh η   (EVEN),

    and the recurring Hecke/HOMFLY weight `[2]_q ≈ 2.0109` at q₀ is exactly
    `2·cosh(log q₀)`. The nucleon masses are the archimedean image of a
    hyperbolic rotation by the flavor angle θ:

        m_p = m₀·e^{−θ},   m_n = m₀·e^{+θ},

    so `m_avg = m₀·cosh θ` (even ⇒ all δ², δ⁴ … corrections) and
    `Δ_pn/2 = m₀·sinh θ` (odd ⇒ all δ¹, δ³ … corrections). The production
    `m_{p,n} = m_avg·(1 ∓ δ/2)` is the O(δ) truncation `e^{∓δ/2} ≈ 1 ∓ δ/2`
    (`θ = δ/2` at leading order). This makes the parity a THEOREM
    (`mass_avg_even` / `mass_split_odd`), not an order-by-order check, so a
    δ² (even) correction is parity-allowed on m_avg and parity-FORBIDDEN on
    Δ_pn. -/

/-- The doublet quantum integer `[2]_q = q + q⁻¹` (local copy of
    `HadronicMass.bracket_2_q`). -/
noncomputable def bracket_2_q (q : ℝ) : ℝ := q + q⁻¹

/-- **`h = 2·sinh(log q)`** — the Hecke crossing scale is the *odd*
    hyperbolic function of the rapidity `η = log q`. -/
theorem h_crossing_eq_two_sinh_log (q : ℝ) (hq : 0 < q) :
    h_crossing q = 2 * Real.sinh (Real.log q) := by
  unfold h_crossing
  rw [Real.sinh_eq, Real.exp_log hq, Real.exp_neg, Real.exp_log hq]
  ring

/-- **`[2]_q = 2·cosh(log q)`** — the doublet integer is the *even*
    hyperbolic function of the rapidity. At q₀ this is the recurring
    `≈ 2.0109` Hecke/HOMFLY weight. -/
theorem bracket_2_q_eq_two_cosh_log (q : ℝ) (hq : 0 < q) :
    bracket_2_q q = 2 * Real.cosh (Real.log q) := by
  unfold bracket_2_q
  rw [Real.cosh_eq, Real.exp_log hq, Real.exp_neg, Real.exp_log hq]
  ring

/-- Proton mass as a hyperbolic rotation `m₀·e^{−θ}` by the p-n rapidity θ. -/
noncomputable def mass_proton (m0 θ : ℝ) : ℝ := m0 * Real.exp (-θ)

/-- Neutron mass as the opposite rotation `m₀·e^{+θ}`. -/
noncomputable def mass_neutron (m0 θ : ℝ) : ℝ := m0 * Real.exp θ

/-- **Average mass is `m₀·cosh θ`** (EVEN in θ ⇒ carries every even-δ
    correction; the m_avg channel). -/
theorem mass_avg_eq_cosh (m0 θ : ℝ) :
    (mass_proton m0 θ + mass_neutron m0 θ) / 2 = m0 * Real.cosh θ := by
  unfold mass_proton mass_neutron
  rw [Real.cosh_eq]
  ring

/-- **Half the mass split is `m₀·sinh θ`** (ODD in θ ⇒ carries every odd-δ
    correction; the antisymmetric Δ_pn channel). -/
theorem mass_split_eq_sinh (m0 θ : ℝ) :
    (mass_neutron m0 θ - mass_proton m0 θ) / 2 = m0 * Real.sinh θ := by
  unfold mass_proton mass_neutron
  rw [Real.sinh_eq]
  ring

/-- **Parity (even): m_avg is invariant under p↔n (θ ↦ −θ).** Hence a δ²
    correction is parity-allowed on the average. -/
theorem mass_avg_even (m0 θ : ℝ) :
    m0 * Real.cosh (-θ) = m0 * Real.cosh θ := by
  rw [Real.cosh_neg]

/-- **Parity (odd): the split flips sign under p↔n (θ ↦ −θ).** Hence a δ²
    (even) correction is parity-FORBIDDEN on Δ_pn — only odd powers of θ
    (δ¹, δ³, …) may appear. This is the formal statement of the
    quadratic-δ consistency check. -/
theorem mass_split_odd (m0 θ : ℝ) :
    m0 * Real.sinh (-θ) = -(m0 * Real.sinh θ) := by
  rw [Real.sinh_neg]; ring

/-- The leading p-n rapidity `θ = δ/2`, so `e^{∓θ} ≈ 1 ∓ δ/2` recovers the
    production linear split at O(δ); the exact θ carries the higher odd-δ
    tower (sinh) with no even contamination. -/
noncomputable def pn_rapidity_leading (q : ℝ) : ℝ := delta_subleading q / 2

end QOU.Mass
