import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.Mass.SaddleQShiftOffset

/-!
# QOU.Mass.MassVolDensity — Mass = Vol × Density (algebraic core)

The algebraic heart of the **Mass = Vol × Density** decomposition that
replaces the `VolDensity` black box with proper definitions:

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

/-! `hbarQ` (ℏ_q = 1 - q⁻¹) is NOT re-declared here. It comes from
`QOU.Mass.SaddleQShiftOffset`, where it is stated generically over
`{K : Type*} [Field K]`; this file uses it at `K = ℝ`. Consolidated
2026-08-30 (bean `qou-6bla`) — the two were the same function under
one namespace, so once both were named `hbarQ` they could no longer
be imported together. -/


/-! ## §1  The density (Hecke linking weight) and its two algebraic forms -/

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
    `Δm/M_N` at leading order (`conj:flavor-split-substrate-mass`). Equal to the
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

/-- **δ subleading** = `δ_leading · (1 + ℏ_q³)` — the full flavor split
    with the 3-loop substrate-Planck correction (`flavor_split_subleading`
    in `_li_2_q_util.py`; matches `_avg_color_delta()` to 2.6e-19). The
    factor `(1 + ℏ_q³)` is the algebraic image of the 3-loop term in the
    surface-ordered (non-abelian Stokes) holonomy expansion — see the P3/P4
    follow-up. Still purely algebraic in `q`. -/
noncomputable def delta_subleading (q : ℝ) : ℝ :=
  delta_leading q * (1 + hbarQ q ^ 3)

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

/-! ## §4  Generalisation to binding energy — the mirror-difference channel

    The §3 parity theorems are stated for a general `(m0, θ)` pair, so they
    apply verbatim to ANY mirror observable — in particular the binding
    energy of a mirror nuclear pair (³H, ³He). Writing the pair as a
    hyperbolic rotation `B_± = B₀·e^{∓θ_B}`:

      binding_avg = B₀·cosh θ_B   (EVEN — the absolute scale; M_λ-gated)
      ΔB          = 2·B₀·sinh θ_B (ODD  — the mirror DIFFERENCE)

    The ODD/sinh channel (the difference) is computable **prior to** the
    even/cosh absolute normalisation: it is the non-circular channel that
    **sidesteps the per-block M_λ gate** (which lives entirely in the
    even/absolute channel). This is the formal counterpart of the empirical
    fact that the eigenphase *difference* closes the ³H−³He mirror pair to
    ~2% with zero free parameters while the absolute binding stays gated.
    (Compute: `mass_vol_density.mirror_binding_difference`.) -/

/-- ³H-side binding as `B₀·e^{−θ_B}`. -/
noncomputable def binding_mirror_low (B0 θB : ℝ) : ℝ := B0 * Real.exp (-θB)

/-- ³He-side binding as `B₀·e^{+θ_B}`. -/
noncomputable def binding_mirror_high (B0 θB : ℝ) : ℝ := B0 * Real.exp θB

/-- **Mirror binding difference is `2·B₀·sinh θ_B`** — the ODD channel: the
    M_λ-gate sidestep. The antisymmetric (difference) content is `sinh`, so
    it is computable from the difference alone, before the absolute average. -/
theorem binding_mirror_difference_eq_sinh (B0 θB : ℝ) :
    binding_mirror_high B0 θB - binding_mirror_low B0 θB
      = 2 * (B0 * Real.sinh θB) := by
  unfold binding_mirror_high binding_mirror_low
  rw [Real.sinh_eq]
  ring

/-- **Mirror binding average is `B₀·cosh θ_B`** — the EVEN channel (the
    absolute scale, which the per-block M_λ gate blocks). -/
theorem binding_mirror_average_eq_cosh (B0 θB : ℝ) :
    (binding_mirror_high B0 θB + binding_mirror_low B0 θB) / 2
      = B0 * Real.cosh θB := by
  unfold binding_mirror_high binding_mirror_low
  rw [Real.cosh_eq]
  ring

/-- **Binding parity (odd):** the mirror difference flips sign under the
    mirror flip `θ_B ↦ −θ_B`. Hence — exactly as for the p-n mass split — a
    δ² (even) correction is parity-FORBIDDEN on ΔB and allowed only on the
    (M_λ-gated) average. The quadratic-δ consistency check, for binding. -/
theorem binding_difference_odd (B0 θB : ℝ) :
    B0 * Real.sinh (-θB) = -(B0 * Real.sinh θB) := by
  rw [Real.sinh_neg]; ring

/-! ## §5  The SU(2)_q generating function — cosh/sinh is the abelian shadow

    The §3/§4 cosh/sinh split is the U(1) (Cartan/abelian) projection: a
    SINGLE rapidity, the j=½ doublet. The framework is fundamentally
    SU(2)_q (Rep(SU_q(2)) / the Hecke algebra), whose Weyl character is the
    generating function over the irrep tower j = 0, ½, 1, …

        χ_j(η) = [2j+1]_q = sinh((2j+1)·η) / sinh η      (q = e^η).

    The U(1) cosh/sinh are its low-rank shadows: `[2]_q = 2 cosh η`
    (fundamental/doublet), with the Chebyshev/SU(2) recursion
    `[n+1]_q = [2]_q·[n]_q − [n−1]_q`. The DENSITY ρ(q) = Σ_λ y_λ χ^λ is a
    weighted sum of these SU(2) characters (the Markov trace over Wedderburn
    blocks) — so SU(2) already lives in the Vol×Density *magnitude*, while
    the U(1) rapidity is the orthogonal FLAVOR doublet split. Generalising
    the p-n doublet to full isospin multiplets (A>2 nuclei, resonances) is
    exactly replacing the j=½ cosh/sinh by the higher χ_j here. Algebraic
    throughout: `[n]_q` is the colored-Jones building block as a q-identity,
    NOT via Kashaev. -/

/-- SU(2)_q fundamental Weyl character `χ_{1/2}(η) = sinh(2η)/sinh η`
    (the j=½ doublet; `[2]_q` at `q = e^η`). -/
noncomputable def su2_fundamental_character (η : ℝ) : ℝ :=
  Real.sinh (2 * η) / Real.sinh η

/-- **The fundamental SU(2)_q character is the U(1) doublet `2 cosh η`.**
    This is the bridge: the abelian cosh is the j=½ SU(2) character, so the
    recurring `[2]_q ≈ 2.0109` weight is simultaneously the doublet
    SU(2) character and `2 cosh(log q₀)`. -/
theorem su2_fundamental_eq_two_cosh (η : ℝ) (hη : Real.sinh η ≠ 0) :
    su2_fundamental_character η = 2 * Real.cosh η := by
  unfold su2_fundamental_character
  rw [Real.sinh_two_mul]
  field_simp

/-! ## §6  SO(3)_q = SU(2)_q / ℤ₂ — the adjoint (j=1) one level up

    SO(3) is the ℤ₂-quotient of SU(2): only the INTEGER-spin irreps
    descend, the lowest non-trivial being the adjoint/vector `j = 1`.
    Its Weyl character is `χ_1(η) = [3]_q = sinh(3η)/sinh η`. The
    audit's "SO(3) sits one level up (SU(2)/ℤ₂)"
    (`docs/audits/2026-06-04-u1-su2-so3-symmetry-loss-audit.md`) is here
    the Chebyshev/Clebsch–Gordan recursion

        [3]_q = [2]_q² − 1                       (`so3_adjoint_eq_chebyshev`)

    i.e. the j=1 character is the symmetric square minus trivial of the
    j=½ doublet — exactly the rep that survives the ℤ₂ quotient. In the
    U(1) hyperbolic shadow it is `1 + 2 cosh(2η)`
    (`so3_adjoint_eq_one_plus_two_cosh_two`). These are pure q-identities
    (`[n]_q` as a colored-Jones building block), NOT the conjectural
    S₅↔SO(3) FIBRE action that fixes `chirality_sign` — that remains
    gated on `conj:s5-so3-fiber-action`. This section formalises only the
    representation-theoretic level structure — unconditional as
    representation theory (no conjecture), with the one analytic side
    condition `sinh η ≠ 0` (i.e. `q ≠ 1`, the substrate regime away from
    the classical point) because the characters are written as ratios
    `[n]_q = sinh(nη)/sinh η`. NOTE: Lean division is total, so the ratio
    `so3_adjoint_character 0 = sinh 0 / sinh 0 = 0` (a junk value, NOT the
    mathematical limit `[3]_q → 3`); the closed forms `4 cosh²η − 1` and
    `1 + 2 cosh(2η)` are the continuous representatives and agree with the
    ratio exactly on `q ≠ 1`, which is the only regime the theorems below
    assert (each carries `sinh η ≠ 0`). -/

/-- SO(3)_q adjoint (vector, j=1) Weyl character `χ_1(η) = sinh(3η)/sinh η`
    (the `[3]_q` quantum integer at `q = e^η`). The lowest integer-spin
    irrep, i.e. the lowest one descending through SO(3) = SU(2)/ℤ₂. -/
noncomputable def so3_adjoint_character (η : ℝ) : ℝ :=
  Real.sinh (3 * η) / Real.sinh η

/-- Closed form `[3]_q = 4 cosh²η − 1` (for `sinh η ≠ 0`), via
    `sinh(3η) = sinh η · (4 sinh²η + 3)` and `sinh²η = cosh²η − 1`. -/
theorem so3_adjoint_eq_four_cosh_sq_sub_one (η : ℝ) (hη : Real.sinh η ≠ 0) :
    so3_adjoint_character η = 4 * Real.cosh η ^ 2 - 1 := by
  unfold so3_adjoint_character
  have hnum : Real.sinh (3 * η) = Real.sinh η * (4 * Real.sinh η ^ 2 + 3) := by
    rw [Real.sinh_three_mul]; ring
  rw [hnum, mul_comm, mul_div_assoc, div_self hη, mul_one, Real.sinh_sq]
  ring

/-- **The SO(3)_q adjoint is the Chebyshev square of the SU(2)_q doublet:
    `[3]_q = [2]_q² − 1`.** This is the ℤ₂-quotient level structure —
    the j=1 (integer-spin) character is the symmetric-square-minus-trivial
    of the j=½ doublet, the lowest irrep surviving SO(3) = SU(2)/ℤ₂. -/
theorem so3_adjoint_eq_chebyshev (η : ℝ) (hη : Real.sinh η ≠ 0) :
    so3_adjoint_character η = su2_fundamental_character η ^ 2 - 1 := by
  rw [so3_adjoint_eq_four_cosh_sq_sub_one η hη, su2_fundamental_eq_two_cosh η hη]
  ring

/-- The SO(3)_q adjoint in the U(1) hyperbolic shadow: `[3]_q = 1 + 2 cosh(2η)`. -/
theorem so3_adjoint_eq_one_plus_two_cosh_two (η : ℝ) (hη : Real.sinh η ≠ 0) :
    so3_adjoint_character η = 1 + 2 * Real.cosh (2 * η) := by
  rw [so3_adjoint_eq_four_cosh_sq_sub_one η hη, Real.cosh_two_mul, Real.sinh_sq]
  ring

end QOU.Mass
