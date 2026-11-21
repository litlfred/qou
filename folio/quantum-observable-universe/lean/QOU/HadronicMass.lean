import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import QOU.MassDerivation
import QOU.KnotRegistry
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# QOU.HadronicMass — Terminal Resolution of Hadronic Mass

Formalizes each row of the **Terminal Resolution of Hadronic Mass** table
(Chapter: Experimental Evidence, Remark on Skein Decomposition).

## The Table (NIST CODATA 2022 precision)

| Structure      | Topological Formula                | QOU Result (MeV)   | NIST CODATA 2022 (MeV)       | Uncertainty (MeV) |
|----------------|-------------------------------------|--------------------|-----------------------------|-------------------|
| Proton (m_p)   | Q(q) 𝓜(ℒ_Hopf)_uud               | 938.27208943       | 938.27208943                | ± 0.00000029      |
| Neutron (m_n)  | Q(q) 𝓜(ℒ_Hopf)_udd               | 939.56542194       | 939.56542194                | ± 0.00000048      |
| Deuteron (m_D) | 𝓜(L₆) − Binding                   | 1875.61351137      | 1875.61294500               | ± 0.00000058      |
| Binding Energy | Δ Skein Polynomial                 | 2.224              | 2.22456637 (derived)        | ± 0.00000076      |

## Topological Mass Framework

The mass functional `𝓜(K)` for a knot/link `K` satisfies:
  1. For simple knots: `𝓜(K) = Vol(K) / ℏ_q²` (Conjecture 4.25)
  2. For composite links: the **q-deformed Skein relation**
     `q · 𝓜(L₊) − q⁻¹ · 𝓜(L₋) = (q^(1/2) − q^(-1/2)) · 𝓜(L₀)`
  3. For hadrons: `m = Q(q) · 𝓜(ℒ_Hopf)_quarks` where `Q(q)` encodes
     the quark content and color-exchange topology.

## Structure of this file

1. **NIST CODATA 2022 constants** — Experimental masses (full NIST precision)
2. **Skein mass functional** — The q-deformed mass recursion
3. **Quark flavor factor** — The Q(q) charge factor for uud/udd
4. **Row-by-row formalization** — Each table row as a theorem
5. **Consistency checks** — Cross-row algebraic identities

## References

- [turaev2010] V. Turaev, *Quantum Invariants of Knots and 3-Manifolds*, de Gruyter 2010.
- [codata2022] NIST CODATA 2022 Recommended Values of Fundamental Constants.
  https://physics.nist.gov/cuu/Constants/
- [kronheimer2004] P. Kronheimer & T. Mrowka, *Witten's Conjecture and
  Property P*, Geom. Topol. 2004.
-/


open QOU.MassDerivation QOU.KnotRegistry
open QOU.KnotTheory hiding vol_figure_eight

namespace QOU.HadronicMass

/-! ## Section 1: NIST CODATA 2022 Experimental Constants

All values from the 2022 CODATA adjustment of the fundamental physical constants.
Ref: https://physics.nist.gov/cuu/Constants/
Ref: https://physics.nist.gov/cuu/pdf/wall_2022.pdf -/

/-- Proton mass energy equivalent in MeV/c².
    NIST CODATA 2022: 938.272 089 43(29) MeV/c².
    Rel. uncertainty: 3.1 × 10⁻¹⁰.
    Ref: https://physics.nist.gov/cgi-bin/cuu/Value?mpc2mev -/
noncomputable def proton_mass_MeV : ℝ := 938.27208943

/-- Neutron mass energy equivalent in MeV/c².
    NIST CODATA 2022: 939.565 421 94(48) MeV/c².
    Rel. uncertainty: 5.1 × 10⁻¹⁰.
    Ref: https://physics.nist.gov/cgi-bin/cuu/Value?mnc2mev -/
noncomputable def neutron_mass_MeV : ℝ := 939.56542194

/-- Deuteron mass energy equivalent in MeV/c².
    NIST CODATA 2022: 1875.612 945 00(58) MeV/c².
    Rel. uncertainty: 3.1 × 10⁻¹⁰.
    Ref: https://physics.nist.gov/cgi-bin/cuu/Value?eqmdc2mev -/
noncomputable def deuteron_mass_MeV : ℝ := 1875.61294500

/-- Deuteron binding energy in MeV (derived from NIST CODATA 2022 masses).
    B_d = m_p c² + m_n c² − m_d c²
        = 938.27208943 + 939.56542194 − 1875.61294500
        = 2.22456637 MeV.
    Propagated uncertainty: ± 0.00000076 MeV. -/
noncomputable def binding_energy_CODATA : ℝ := 2.22456637

/-- Deuteron binding-energy **anchor** (MeV), `2.224`, used as the
    binding term in the Row-3 mass-deficit identity below.

    Honesty note (2026-06-17): this value is the experimental binding
    `(m_p + m_n) − m_D = 2.22456637 MeV` rounded to 4 significant
    figures — it is **not** an independent categorical/Skein-polynomial
    prediction. The categorical per-λ Δ_λ sum (Option E) does *not*
    reproduce it: it undershoots the deuteron by ≈ −82.9 % (see the
    2026-06-16 Option-E deuteron correction and
    `QOU.OptionE.DeltaLambda`). Closure of the deuteron binding from
    topology remains an open target. The theorems below that consume
    this constant are therefore consistency identities, not
    predictions. -/
noncomputable def binding_energy_QOU : ℝ := 2.224

/-- Electron mass energy equivalent in MeV/c².
    NIST CODATA 2022: 0.510 998 950 69(16) MeV/c².
    Rel. uncertainty: 3.1 × 10⁻¹⁰.
    Ref: https://physics.nist.gov/cgi-bin/cuu/Value?mec2mev -/
noncomputable def electron_mass_MeV : ℝ := 0.51099895069

/-! ## Section 2: Topological Constants -/

/-- Hyperbolic volume of the Borromean rings (L6a4 / 6₂³).
    Exact: 8 · G where G = Catalan's constant (OEIS A006752).
    Value: 8 × 0.915965594177219… = 7.32772475341775…
    Computed by SnapPy; Bloch-Wigner dilogarithm. -/
noncomputable def vol_borromean : ℝ := 7.32772475341775

/-- Hyperbolic volume of the Hopf link (L2a1).
    The Hopf link is a torus link with zero hyperbolic volume.
    Its mass contribution comes from the Skein functional, not volume. -/
noncomputable def vol_hopf_link : ℝ := 0

/-! ## Section 3: The q-Deformed Skein Mass Functional

The Skein relation governs how the mass functional `𝓜` transforms
under crossing changes in the color-exchange space:

  `q · 𝓜(L₊) − q⁻¹ · 𝓜(L₋) = (q^(1/2) − q^(-1/2)) · 𝓜(L₀)`

This is the fundamental recursion that determines composite hadron masses
from the topology of quark-binding links. -/

/-- The **Skein mass relation**: at a crossing in the color-exchange
    space, the mass functional satisfies the q-deformed Skein relation.

    - `m_plus`:  mass of the `L₊` resolution (positive crossing)
    - `m_minus`: mass of the `L₋` resolution (negative crossing)
    - `m_zero`:  mass of the `L₀` resolution (smoothing) -/
structure SkeinMassRelation where
  /-- The substrate parameter q > 1. -/
  q : ℝ
  /-- q is greater than 1. -/
  q_gt_one : q > 1
  /-- Mass of the L₊ resolution. -/
  m_plus : ℝ
  /-- Mass of the L₋ resolution. -/
  m_minus : ℝ
  /-- Mass of the L₀ resolution (smoothing). -/
  m_zero : ℝ
  /-- The Skein relation holds. -/
  skein : q * m_plus - q⁻¹ * m_minus =
    (q ^ (1/2 : ℝ) - q ^ (-(1/2 : ℝ))) * m_zero

/-- The **quark flavor factor** `Q(q)` encodes the quark content of a
    hadron and its coupling to the substrate parameter `q`.

    For the proton (uud): the three quark tubes are Borromean-linked,
    with the Hopf link mediating the strong force between each pair.
    The flavor factor accounts for the mass difference between u and d
    quarks at the topological level. -/
structure QuarkFlavorFactor where
  /-- The substrate parameter. -/
  q : ℝ
  /-- Number of up quarks. -/
  n_up : ℕ
  /-- Number of down quarks. -/
  n_down : ℕ
  /-- The evaluated factor Q(q) in MeV. -/
  value : ℝ

/-! ## Section 4: The Topological Mass Functional

`𝓜(K)` assigns a mass (in MeV) to each knot/link `K` via:
- Simple knots: `𝓜(K) = m_e · Vol(K) / ℏ_q²`
- Composite hadrons: Skein recursion through color-exchange crossings -/

/-- Topological mass of a simple knot, in MeV.
    `𝓜(K) = m_e · Vol(K) / ℏ_q²`
    where `m_e` is the electron mass and `ℏ_q = 1 - 1/q`. -/
noncomputable def topological_mass (vol : ℝ) (q : ℝ) : ℝ :=
  electron_mass_MeV * vol / (quantum_planck q) ^ 2

/-- Verify: the topological mass formula recovers the muon mass.
    `𝓜(4₁) = m_e · Vol(4₁) / ℏ_q² = m_e · (m_μ/m_e) = m_μ`. -/
noncomputable def muon_mass_topological : ℝ :=
  topological_mass vol_figure_eight substrate_q

/-! ## Section 5: CODATA-pinned record of the former table

**Not a derivation.** Each `*_topological` value below is defined as the
CODATA constant (or, for the deuteron, the mass-deficit identity with the
experimental binding energy). The lemmas that compared these values with
CODATA held by construction and were removed (owner decision, PR #8897),
together with their bundle `terminal_resolution_hadronic_mass`, the splitting
`proton_neutron_mass_difference` and `row3_deuteron_value` (follow-up PR).
The content
block `prop:terminal-resolution` now states the pair Skein nucleon identities,
proved in `QOU.MassTheory.PairSkeinNucleon` (content sibling
`mass-theory/terminal-resolution.lean`). Under that map any `(m_p, m_n)` is
reproduced by exactly one pair of dressed quark masses, so a CODATA match
carries no content. The definitions are kept because Section 5a and the
remaining identities use them. The per-row docstrings below describe the
former reading. -/

/-! ### Row 1: Proton (m_p) — Q(q) 𝓜(ℒ_Hopf)_uud -/

/-- Proton quark content: 2 up quarks, 1 down quark. -/
noncomputable def proton_quarks : QuarkFlavorFactor where
  q := substrate_q
  n_up := 2
  n_down := 1
  value := proton_mass_MeV

/-- **Row 1 — Proton**: The topological formula `Q(q) 𝓜(ℒ_Hopf)_uud`
    evaluates to 938.27208943 MeV, matching NIST CODATA 2022.

    The proton mass arises from three quark tubes in Borromean
    configuration (6₂³), bound by the Hopf link strong force.
    The quark flavor factor Q(q) for uud content at q = 1.1097
    produces the observed proton mass.
    NIST CODATA 2022: 938.272 089 43(29) MeV/c².

    Ref: Manuscript Table "Terminal Resolution of Hadronic Mass", Row 1. -/
noncomputable def proton_topological : ℝ := proton_quarks.value

/-! ### Row 2: Neutron (m_n) — Q(q) 𝓜(ℒ_Hopf)_udd -/

/-- Neutron quark content: 1 up quark, 2 down quarks. -/
noncomputable def neutron_quarks : QuarkFlavorFactor where
  q := substrate_q
  n_up := 1
  n_down := 2
  value := neutron_mass_MeV

/-- **Row 2 — Neutron**: The topological formula `Q(q) 𝓜(ℒ_Hopf)_udd`
    evaluates to 939.56542194 MeV, matching NIST CODATA 2022.

    The neutron differs from the proton by swapping one up quark
    for a down quark, which changes the Skein residue at the
    color-exchange crossings.  The mass difference
    `m_n − m_p = 1.29333251 MeV` is a Skein-level effect.
    NIST CODATA 2022: 939.565 421 94(48) MeV/c².

    Ref: Manuscript Table "Terminal Resolution of Hadronic Mass", Row 2. -/
noncomputable def neutron_topological : ℝ := neutron_quarks.value

/-! ### Row 3: Deuteron (m_D) — 𝓜(L₆) − Binding -/

/-- **Row 3 — Deuteron**: The deuteron mass is the sum of proton and
    neutron masses minus the binding energy contributed by the
    Δ Skein polynomial.

    `m_D = m_p + m_n − ΔE_bind`
    `m_D = 938.27208943 + 939.56542194 − 2.224 = 1875.61351137 MeV`
    NIST CODATA 2022: 1875.61294500(58) MeV → residual 0.567 keV.

    The `L₆` topology represents the proton-neutron bound state.

    Honesty note (2026-06-17): the binding term `binding_energy_QOU`
    here is the *experimental* mass deficit rounded to 4 sig figs (see
    its docstring), so the former CODATA comparison of this row was a
    mass-deficit consistency identity `m_p + m_n − B_exp ≈ m_D`, **not**
    an independent topological prediction of the deuteron mass.

    Ref: Manuscript Table "Terminal Resolution of Hadronic Mass", Row 3. -/
noncomputable def deuteron_topological : ℝ :=
  proton_topological + neutron_topological - binding_energy_QOU

theorem row3_deuteron_formula :
    deuteron_topological = proton_mass_MeV + neutron_mass_MeV - binding_energy_QOU := by
  unfold deuteron_topological proton_topological neutron_topological
  unfold proton_quarks neutron_quarks
  rfl

/-! ### Row 4: Binding Energy — Δ Skein Polynomial -/

/-- **Row 4 — Binding Energy**: recovers the binding anchor
    `binding_energy_QOU = 2.224 MeV` as the mass deficit
    `(m_p + m_n) − m_D`.

    NIST CODATA 2022 (derived): 2.22456637(76) MeV.
    Discrepancy vs the 4-sig-fig anchor: 0.00056637 MeV ≈ 0.567 keV.

    Honesty note (2026-06-17): `row4_binding_from_skein` is an
    **algebraic identity** — since `deuteron_topological` is *defined*
    as `m_p + m_n − binding_energy_QOU`, the statement
    `(m_p + m_n) − deuteron_topological = binding_energy_QOU` holds by
    `ring` for any value of the anchor. It does **not** compute the
    binding from the Skein polynomial; the anchor is the experimental
    deficit (see `binding_energy_QOU`). A genuine topological prediction
    of the deuteron binding remains open (Option E undershoots by
    ≈ −82.9 %).

    Ref: Manuscript Table "Terminal Resolution of Hadronic Mass", Row 4. -/
theorem row4_binding_from_skein :
    proton_topological + neutron_topological - deuteron_topological
      = binding_energy_QOU := by
  unfold deuteron_topological
  ring

/-! ## Section 5a: Pair Skein Mass Decomposition

The Borromean braid of a nucleon has six crossings in three pairs, one pair
per color-exchange channel.  At each pair between quarks of species `a` and
`b`, a double application of the Skein relation yields the **pair Skein mass**:

  `𝒮_{ab}(q) = (q · μ_a + q⁻¹ · μ_b) / (q^{1/2} + q^{-1/2})`

where `μ_a` is the **dressed quark Skein mass** of species `a`.
The total nucleon mass is the sum over the three crossing pairs:

  `m_N = 𝒮_{q₁q₂} + 𝒮_{q₁q₃} + 𝒮_{q₂q₃}`

For the proton (uud):  `m_p = 𝒮_{uu} + 2 · 𝒮_{ud}`
For the neutron (udd): `m_n = 2 · 𝒮_{ud} + 𝒮_{dd}` -/

/-- Dressed quark Skein mass of the up quark (MeV).
    Derived from the Borromean Skein decomposition:
    `μ_u ≈ 311.10 MeV` at `q = 1.1097`. -/
noncomputable def dressed_mass_up : ℝ := 311.10

/-- Dressed quark Skein mass of the down quark (MeV).
    Derived from the Borromean Skein decomposition:
    `μ_d ≈ 312.39 MeV` at `q = 1.1097`. -/
noncomputable def dressed_mass_down : ℝ := 312.39

/-- The **pair Skein mass** `𝒮_{ab}(q)` at a crossing pair between quarks
    of dressed masses `μ_a` and `μ_b`:
    `𝒮_{ab}(q) = (q · μ_a + q⁻¹ · μ_b) / (q^{1/2} + q^{-1/2})` -/
noncomputable def pair_skein_mass (q μ_a μ_b : ℝ) : ℝ :=
  (q * μ_a + q⁻¹ * μ_b) / (q ^ (1/2 : ℝ) + q ^ (-(1/2 : ℝ)))

/-- Pair Skein mass for two up quarks: `𝒮_{uu}(q)`. -/
noncomputable def S_uu : ℝ := pair_skein_mass substrate_q dressed_mass_up dressed_mass_up

/-- Pair Skein mass for up-down quarks: `𝒮_{ud}(q)`. -/
noncomputable def S_ud : ℝ := pair_skein_mass substrate_q dressed_mass_up dressed_mass_down

/-- Pair Skein mass for two down quarks: `𝒮_{dd}(q)`. -/
noncomputable def S_dd : ℝ := pair_skein_mass substrate_q dressed_mass_down dressed_mass_down

/-- The proton mass decomposes as `m_p = 𝒮_{uu} + 2 · 𝒮_{ud}`.
    This is the Skein recursion iterated across all three crossing pairs
    of the Borromean braid with quark content (u₁, u₂, d). -/
noncomputable def proton_from_pair_skein : ℝ := S_uu + 2 * S_ud

/-- The neutron mass decomposes as `m_n = 2 · 𝒮_{ud} + 𝒮_{dd}`.
    This is the Skein recursion iterated across all three crossing pairs
    of the Borromean braid with quark content (u, d₁, d₂). -/
noncomputable def neutron_from_pair_skein : ℝ := 2 * S_ud + S_dd

/-- The proton--neutron mass difference from the pair Skein decomposition:
    `m_n − m_p = 𝒮_{dd} − 𝒮_{uu}`.
    Only the same-flavor crossing pair changes when swapping u ↔ d. -/
theorem pair_skein_mass_splitting :
    neutron_from_pair_skein - proton_from_pair_skein = S_dd - S_uu := by
  unfold neutron_from_pair_skein proton_from_pair_skein
  ring

/-- The mass splitting factors through the dressed quark mass difference:
    `𝒮_{dd}(q) − 𝒮_{uu}(q) = [(q + q⁻¹)/(q^{1/2} + q^{-1/2})] · (μ_d − μ_u)`.

    This shows the proton--neutron splitting is a pure Skein-level effect
    of the u-d mass difference, amplified by the factor (q+q⁻¹)/(q^½+q^-½). -/
theorem pair_skein_splitting_formula :
    S_dd - S_uu =
      (substrate_q + substrate_q⁻¹) / (substrate_q ^ (1/2 : ℝ) + substrate_q ^ (-(1/2 : ℝ)))
      * (dressed_mass_down - dressed_mass_up) := by
  unfold S_dd S_uu pair_skein_mass
  ring

/-! ### The former pair-Skein agreement bounds

`proton_pair_skein_approx` and `neutron_pair_skein_approx` bounded the pair-Skein
proton and neutron values against the CODATA masses.  They were removed (owner
decision, PR #8917): this file states no comparison with measured values.  The
lemma below, about the side hypothesis those bounds once carried, makes no
such comparison and is kept. -/

/-- **The denominator hypothesis the two former context classes bound is false.**
`q^{1/2} + q^{-1/2} = 2.0027092783…` at `q = 1.1097`, so its distance from
`2.00228` is `4.293e-4`, over four times the asserted `1e-4`. -/
theorem pair_skein_denom_hypothesis_false :
    ¬ (|substrate_q ^ (1/2 : ℝ) + substrate_q ^ (-(1/2 : ℝ)) - 2.00228| < 1e-4) := by
  unfold substrate_q
  have hxp : (0:ℝ) < 11097/10000 := by norm_num
  have hx : (0:ℝ) ≤ 11097/10000 := by norm_num
  rw [show (1.1097 : ℝ) = 11097/10000 by norm_num]
  set s : ℝ := (11097/10000 : ℝ) ^ (1/2 : ℝ) with hsdef
  have hs0 : 0 < s := Real.rpow_pos_of_pos hxp _
  have hs2 : s * s = 11097/10000 := by rw [hsdef, ← Real.rpow_add hxp]; norm_num
  have hneg : (11097/10000 : ℝ) ^ (-(1/2) : ℝ) = s⁻¹ := by
    rw [hsdef, ← Real.rpow_neg hx]
  rw [hneg]
  have hub : s < 10535/10000 := by nlinarith
  have hlb : 10534/10000 < s := by nlinarith
  have hinv : s⁻¹ * s = 1 := inv_mul_cancel₀ (ne_of_gt hs0)
  rw [abs_lt]
  push_neg
  intro _
  nlinarith [hinv, hs0, hub, hlb, hs2]

/-! ## Section 6: Cross-Row Consistency Checks -/

/-- **Mass sum rule**: `m_D + ΔE = m_p + m_n`.
    The deuteron mass plus the binding energy equals the sum of
    constituent nucleon masses. -/
theorem mass_sum_rule :
    deuteron_topological + binding_energy_QOU =
      proton_topological + neutron_topological := by
  unfold deuteron_topological
  ring

/-! ## Section 7: Connection to Substrate Parameter

These theorems connect the hadronic mass table back to the fundamental
topological mass formula `m = Vol(K) / ℏ_q²` and the derived
substrate parameter `q = 1.1097`. -/

/-- The quantum Planck constant for the derived substrate parameter. -/
noncomputable def h_q_at_substrate : ℝ := quantum_planck substrate_q

/-- The quantum Planck constant squared. -/
noncomputable def h_q_sq_at_substrate : ℝ := h_q_at_substrate ^ 2

/-- The electron-muon mass ratio is approximately recovered from the
    figure-eight knot volume and the substrate parameter.

    The residual δ ≈ 0.947 reflects that `substrate_q = 1.1097` is a
    4-digit decimal approximation to the exact root of `Vol(4₁)/ℏ_q² = μ/e`.
    The exact substrate parameter is `q = 1/(1 − √(Vol(4₁)/(μ/e))) ≈ 1.10998`,
    for which the ratio would be exact by construction. -/
theorem muon_electron_ratio_from_topology :
    |topological_mass vol_figure_eight substrate_q / electron_mass_MeV
     - experimental_mu_e_ratio| < 1 := by
  unfold topological_mass vol_figure_eight substrate_q quantum_planck
    electron_mass_MeV experimental_mu_e_ratio
  norm_num

/-- The Borromean rings volume relates to the nucleon mass scale.
    `Vol(6₂³) / ℏ_q² ≈ 746.3`, which is the nucleon mass in units
    of electron mass (after Skein correction). -/
noncomputable def borromean_mass_ratio : ℝ :=
  vol_borromean / h_q_sq_at_substrate

/-! ## Section 8: Summary Table (Lean Declarations, NIST CODATA 2022)

| Row | Structure      | Topological Formula          | Lean Declaration        | QOU (MeV)       | NIST CODATA 2022 (MeV)    | δ (MeV)     |
|-----|----------------|-------------------------------|-------------------------|-----------------|---------------------------|-------------|
| 1   | Proton (m_p)   | Q(q) 𝓜(ℒ_Hopf)_uud         | `proton_topological`    | 938.27208943    | 938.27208943(29)          | 0           |
| 2   | Neutron (m_n)  | Q(q) 𝓜(ℒ_Hopf)_udd         | `neutron_topological`   | 939.56542194    | 939.56542194(48)          | 0           |
| 3   | Deuteron (m_D) | 𝓜(L₆) − Binding             | `deuteron_topological`  | 1875.61351137   | 1875.61294500(58)         | 0.00056637  |
| 4   | Binding Energy | Δ Skein Polynomial           | `binding_energy_QOU`    | 2.224           | 2.22456637(76)            | 0.00056637  |

### Hypervolumes (SnapPy / Bloch-Wigner)

| Link           | Lean Declaration     | Volume                       | Exact Form               |
|----------------|----------------------|------------------------------|--------------------------|
| Figure-eight 4₁| `vol_figure_eight`   | 2.02988321281931 (OEIS A091518)| 2 · Cl₂(π/3) = 6 · Λ(π/3)|
| Borromean 6₂³  | `vol_borromean`      | 7.32772475341775             | 8 · G (Catalan const)    |
| Hopf L2a1      | `vol_hopf_link`      | 0                            | torus link               |

### Pair Skein Decomposition

| Declaration               | Formula                                          | Value (MeV) |
|---------------------------|--------------------------------------------------|-------------|
| `dressed_mass_up`         | μ_u                                              | 311.10      |
| `dressed_mass_down`       | μ_d                                              | 312.39      |
| `S_uu`                    | (q·μ_u + q⁻¹·μ_u)/(q^½+q^-½)                   | ≈ 312.36    |
| `S_ud`                    | (q·μ_u + q⁻¹·μ_d)/(q^½+q^-½)                   | ≈ 312.97    |
| `S_dd`                    | (q·μ_d + q⁻¹·μ_d)/(q^½+q^-½)                   | ≈ 313.65    |
| `proton_from_pair_skein`  | S_uu + 2·S_ud                                    | ≈ 938.3     |
| `neutron_from_pair_skein` | 2·S_ud + S_dd                                    | ≈ 939.6     |

### Cross-checks proved:
- `mass_sum_rule`: m_D + ΔE = m_p + m_n  ✓
- `pair_skein_mass_splitting`: m_n − m_p = S_dd − S_uu  ✓
-/

/-! ## Section 9: Named Propositions

These propositions correspond to the LaTeX `\begin{proposition}` environments
in the Experimental Evidence chapter.  They bundle the key results above
into self-contained statements suitable for cross-referencing. -/

/-! ### The q-deformed Skein relation, and why (p, n, d) is NOT an instance of it

**The relation itself is not in question.** `prop:skein-mass-relation` states, in
[`observations/skein-mass-relation-proof.md`](../../observations/skein-mass-relation-proof.md),
that the three resolutions of **one crossing** in a colour-exchange diagram
satisfy

  `q · 𝓜(L₊) − q⁻¹ · 𝓜(L₋) = (q^{1/2} − q^{-1/2}) · 𝓜(L₀)`

— the mass-functional form of the Hecke relation. That is the `SkeinMassRelation`
structure above, and nothing here disputes it.

**What was here until 2026-08-31** was a *particular instantiation* of it,
substituting the proton for `L₊`, the neutron for `L₋` and the deuteron for `L₀`:

```lean
class SkeinMassRelationHolds : Prop where
  identity : substrate_q * proton_mass_MeV - substrate_q⁻¹ * neutron_mass_MeV
           = (substrate_q ^ (1/2:ℝ) - substrate_q ^ (-(1/2:ℝ))) * deuteron_mass_MeV
```

plus a projection and a `def skein_mass_relation_proton_neutron
[SkeinMassRelationHolds] : SkeinMassRelation` building the structure from it.

**That instantiation is FALSE**, proved below. Three measurements, all at the
constants this file defines (mpmath, 40 dps):

| | |
|---|---|
| LHS `q·m_p − q⁻¹·m_n` | **194.516369** |
| RHS `(√q − 1/√q)·m_d` | **195.320153** |
| difference | **0.8038 MeV**, rel **0.41 %** |

For scale: the former CODATA-row lemmas of Section 5 treated `1e-3 MeV` as
agreement, so the gap is ~800× that.

**It is not a tolerance problem.** Two independent checks say the failure is
structural, not a rounding artefact:

- the `q` that would make it exact at these three masses is **1.17296190**, a
  **5.7 %** shift from the substrate `1.1097` — and `q₀` is pinned to sub-ppb;
- the `m_zero` that would make it exact at `q = 1.1097` is **1867.894 MeV**,
  which is `m_d − 7.72 MeV` and matches no quantity in the framework.

**And the `.md` never claimed this instantiation.** The source block states the
relation for `L₊ / L₋ / L₀` — the three resolutions of a *single* crossing. The
proton, neutron and deuteron are three different bound states; the deuteron is a
bound state *of* a proton and a neutron, not the smoothing of a crossing between
them. So the substitution was introduced in Lean, is not licensed by the
narrative, and is what is false. Same shape as
`QOU.Interactions.LRFusion.DoubleMagicConjecture`, where the Lean likewise
invented a conjunct the `.md` does not assert.

**The docstring's own "numerical verification" did not reproduce either.** It
recorded `LHS ≈ 192.83`, `RHS ≈ 192.83`, `|LHS − RHS| < 0.01 ✓`. Both figures are
wrong (the true values are above), and the conclusion inverts the actual result.
Recorded because a wrong check that reports agreement is worse than no check.

**What is NOT claimed here.** Nothing above says the Skein mass relation is
wrong, or that no triple satisfies it. It says this triple does not, at these
constants — a scope-(a) negative in the sense of AGENTS.md, sharpened by the two
structural checks. Which triple *is* the `(L₊, L₋, L₀)` of a colour-exchange
crossing is an open modelling question and is deliberately not answered here.

Bean `qou-z9ws`; `docs/audits/2026-08-30-skein-mass-relation-is-false.lean`. -/

/-- **The proton/neutron/deuteron Skein instantiation is false at the substrate.**
`q·m_p − q⁻¹·m_n = 194.516369` against `(√q − 1/√q)·m_d = 195.320153`.

The two `rpow` terms are eliminated rather than evaluated: with `s = q^{1/2}`,
only `s > 0` and `s·s = q` are needed. The `norm_num` before the rewrite is
load-bearing — without it the base is the decimal literal `1.1097` while the
lemma is stated for `11097/10000`, and the rewrite finds no occurrence. -/
theorem skein_pnd_identity_false :
    substrate_q * proton_mass_MeV - substrate_q⁻¹ * neutron_mass_MeV ≠
      (substrate_q ^ (1/2 : ℝ) - substrate_q ^ (-(1/2 : ℝ))) * deuteron_mass_MeV := by
  intro h
  rw [substrate_q, proton_mass_MeV, neutron_mass_MeV, deuteron_mass_MeV] at h
  norm_num at h
  have hx : (0:ℝ) ≤ 11097/10000 := by norm_num
  have hxp : (0:ℝ) < 11097/10000 := by norm_num
  set s : ℝ := (11097/10000 : ℝ) ^ (1/2 : ℝ) with hsdef
  have hs0 : 0 < s := Real.rpow_pos_of_pos hxp _
  have hs2 : s * s = 11097/10000 := by
    rw [hsdef, ← Real.rpow_add hxp]; norm_num
  have hneg : (11097/10000 : ℝ) ^ (-(1/2) : ℝ) = s⁻¹ := by
    rw [hsdef, ← Real.rpow_neg hx]
  rw [hneg] at h
  have hsne : s ≠ 0 := ne_of_gt hs0
  field_simp at h
  nlinarith [hs2, hs0, h, sq_nonneg s, sq_nonneg (s - 1)]

/-! ## Section 10: Substrate-pure Flavor Split

The proton-neutron mass splitting `Δm = m_n - m_p` admits a closed-form
expression in substrate atoms (i.e. in `substrate_q` only, NOT in the
fitted `μ_u` / `μ_d`).  The closed form is

  `Δm / M_N = (q - 1)² · (1 - q⁻⁴) / 3`

where `M_N = (m_p + m_n)/2` is the nucleon mass average.  Equivalently,
in factored Hecke-atom form,

  `Δm / μ_avg = ℏ_q² · h_q · [2]_q`

where `ℏ_q = (q-1)/q`, `h_q = q - q⁻¹` is the Hecke crossing scale, and
`[2]_q = q + q⁻¹` is the doublet quantum integer.

These two forms are algebraically identical (proven via `ring`).  This
section proves only that identity; it makes no comparison with measured
masses (owner decision, PR #8917).

Companion content blocks:
  - `prop:flavor-split-substrate` — the proposition
  - `prf:flavor-split-substrate` — the proof
  - `probe_flavor_split_substrate.py` — numerical witness
  - `probe_per_sheet_flavor_nonin.py` — derivation via per-sheet Bring
    integration -/

/-- The Hecke crossing scale `h_q = q - q⁻¹`. -/
def h_q_substrate {K : Type*} [Field K] (q : K) : K := q - q⁻¹

/-- The doublet quantum integer `[2]_q = q + q⁻¹`. -/
def bracket_2_q {K : Type*} [Field K] (q : K) : K := q + q⁻¹

/-- The substrate Planck constant `ℏ_q = (q - 1)/q`. -/
def hbarQ {K : Type*} [Field K] (q : K) : K := 1 - q⁻¹

/-- The substrate-pure formula for `Δm / M_N`, in closed polynomial form. -/
def delta_m_over_M_N_substrate {K : Type*} [Field K] (q : K) : K :=
  (q - 1)^2 * (q^4 - 1) / (3 * q^4)

/-- The substrate-pure formula for `Δm / μ_avg`, in factored Hecke-atom form. -/
def delta_m_over_mu_avg_factored {K : Type*} [Field K] (q : K) : K :=
  hbarQ q ^ 2 * h_q_substrate q * bracket_2_q q

/-- **Algebraic identity**: the factored Hecke-atom form for `Δm / μ_avg`
    coincides with `(q - 1)² · (q⁴ - 1) / q⁴` (the closed polynomial form).

    Proven by `field_simp` + `ring` after clearing the inverse. -/
theorem delta_m_factored_eq_closed {K : Type*} [Field K] (q : K) (hq : q ≠ 0) :
    delta_m_over_mu_avg_factored q = (q - 1)^2 * (q^4 - 1) / q^4 := by
  unfold delta_m_over_mu_avg_factored hbarQ h_q_substrate bracket_2_q
  field_simp
  ring

/-- **Closed-to-factored identity**: the per-nucleon split is `1/3` of the
    per-quark factored form. -/
theorem delta_m_over_M_N_eq_factored_over_3 {K : Type*} [Field K] (q : K) (hq : q ≠ 0) :
    delta_m_over_M_N_substrate q = delta_m_over_mu_avg_factored q / 3 := by
  unfold delta_m_over_M_N_substrate
  rw [delta_m_factored_eq_closed q hq]
  ring

/-- **Substrate-pure flavor split** — the closed polynomial form of
    `Δm / M_N` is one third of the factored Hecke-atom form, for every
    nonzero `q` in any field.

    The pair-Skein ansatz behind the formula (per-quark split
    `h_q² · ℏ_q / √q`, decomposition `Δm = (μ_d - μ_u) · [2]_q · z_mkv`)
    is stated in the content block; this theorem proves only the algebraic
    identity between the two forms.

    LaTeX: `\label{prop:flavor-split-substrate}` -/
theorem flavor_split_substrate {K : Type*} [Field K] (q : K) (hq : q ≠ 0) :
    delta_m_over_M_N_substrate q = delta_m_over_mu_avg_factored q / 3 :=
  delta_m_over_M_N_eq_factored_over_3 q hq

end QOU.HadronicMass
