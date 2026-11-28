import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.GCD.Basic


/-!
# QOU.Torsion.KnotParticleGeneration — Torus knot generators and linking operations

The particle spectrum is generated from a finite set of torus knot
generators T_{m,n} (with gcd(m,n) = 1) embedded in the standard
torus T² ⊂ S³, together with Hopf linking, color-tube threading,
and Skein crossing changes.

LaTeX label: `def:knot-particle-generation`

## References

- [leitner2026] §3-lifting-of-quantum-torsion/knot-particle-generation

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Torsion

-- ═══════════════════════════════════════════════════════════════════
-- Substrate parameter and derived constants
-- ═══════════════════════════════════════════════════════════════════

/-- The substrate parameter q, derived from the muon-electron mass ratio.
    CODATA 2022: m_μ/m_e = 206.7682830 → q ≈ 1.10997. -/
-- Ref: CODATA 2022, [leitner2026] §1
noncomputable def q_substrate : ℝ := 1.10997  -- :leanval[q_0]{precision=6}

/-- Quantum Planck constant ℏ_q = 1 - 1/q. -/
-- Ref: [leitner2026] §1/quantum-planck-constant
noncomputable def hbarQ : ℝ := 1 - q_substrate⁻¹

-- ═══════════════════════════════════════════════════════════════════
-- Torus knot generators
-- ═══════════════════════════════════════════════════════════════════

/-- A torus knot type T_{m,n} with coprime winding numbers. -/
-- Ref: [leitner2026] §3/knot-particle-generation
structure TorusKnot where
  /-- Meridional winding number. -/
  m : ℕ
  /-- Longitudinal winding number. -/
  n : ℕ
  /-- Winding numbers are coprime. -/
  coprime : Nat.Coprime m n
  /-- Convention m < n (for m ≥ 2). -/
  m_lt_n : m = 1 ∨ m < n

/-- Seifert genus of T_{m,n} = (m-1)(n-1)/2. -/
-- Ref: [leitner2026] §3/torus-knot-generators
def seifertGenus (T : TorusKnot) : ℕ := (T.m - 1) * (T.n - 1) / 2

/-- Torus knots have zero hyperbolic volume. -/
-- Ref: [leitner2026] §3/knot-particle-generation
noncomputable def hyperbolicVolume (_T : TorusKnot) : ℝ := 0

-- ═══════════════════════════════════════════════════════════════════
-- Hyperbolic volumes of Skein descendants (mathematical constants)
-- ═══════════════════════════════════════════════════════════════════

/-- Vol(4₁) = 2·Cl₂(π/3) ≈ 2.0298832128 (figure-eight knot, muon). -/
-- Ref: [culler2024] SnapPy; [thurston1978] Thurston
noncomputable def vol_figure_eight : ℝ := 2.0298832128  -- :leanval[Vol_4_1]{precision=11}

/-- Vol(5₂) ≈ 2.8281220883 (three-twist knot, strange/down quark). -/
-- Ref: [culler2024] SnapPy
noncomputable def vol_three_twist : ℝ := 2.8281220883

-- ═══════════════════════════════════════════════════════════════════
-- Pair Skein masses (convention D)
-- ═══════════════════════════════════════════════════════════════════

-- The dressed quark masses μ_u, μ_d are parameters. The constants
-- 311.10 / 312.39 MeV that stood here were chosen under the retired
-- convention-C pair formula to reproduce the nucleon masses (selection
-- against the target) and are removed (owner rules 2026-11-27: "derive
-- what you can", no fitting). Their derivation from the aether is open;
-- under convention D the nucleon map (μ_u, μ_d) ↦ (m_p, m_n) is a
-- bijection (`QOU.MassTheory.PairSkeinNucleon`), so measured nucleon
-- masses fix them only by a change of variables.

/-- Pair Skein mass, convention D (owner ruling 2026-11-27):
    `S_ab(q) = (q³·μ_a + q⁻¹·μ_b) / (q² + 1)`, the Markov trace at
    `z_D = q³/(q²+1)` of `μ_a·σ + μ_b·σ⁻¹`
    (`QOU.MassTheory.PairSkeinD.pairMassD_closed`). The convention-C
    denominator `q^½ + q^{-½}` is retired. -/
-- Ref: [leitner2026] §11/pair-skein-mass-formula
noncomputable def pairSkeinMass (mu_a mu_b : ℝ) : ℝ :=
  (q_substrate ^ 3 * mu_a + q_substrate⁻¹ * mu_b) / (q_substrate ^ 2 + 1)

/-- Pair Skein mass of two up strands. -/
noncomputable def skein_uu (mu_up : ℝ) : ℝ := pairSkeinMass mu_up mu_up

/-- Pair Skein mass of an up and a down strand. -/
noncomputable def skein_ud (mu_up mu_down : ℝ) : ℝ := pairSkeinMass mu_up mu_down

/-- Pair Skein mass of two down strands. -/
noncomputable def skein_dd (mu_down : ℝ) : ℝ := pairSkeinMass mu_down mu_down

-- ═══════════════════════════════════════════════════════════════════
-- Nucleon masses from pair Skein formula
-- ═══════════════════════════════════════════════════════════════════

/-- Proton mass = S_uu + 2·S_ud, as a function of the dressed masses. -/
-- Ref: [leitner2026] §11/terminal-resolution-proof
noncomputable def mass_proton_qou (mu_up mu_down : ℝ) : ℝ :=
  skein_uu mu_up + 2 * skein_ud mu_up mu_down

/-- Neutron mass = 2·S_ud + S_dd, as a function of the dressed masses. -/
-- Ref: [leitner2026] §11/terminal-resolution-proof
noncomputable def mass_neutron_qou (mu_up mu_down : ℝ) : ℝ :=
  2 * skein_ud mu_up mu_down + skein_dd mu_down

-- ═══════════════════════════════════════════════════════════════════
-- Atomic mass computation from knot generation
-- ═══════════════════════════════════════════════════════════════════

/-- Mass of an atom with Z protons, N neutrons, and Z electrons,
    minus nuclear binding energy B. -/
-- Ref: [leitner2026] §11/mass-from-generators
noncomputable def atomicMass (mu_up mu_down : ℝ) (Z N : ℕ) (binding : ℝ)
    (m_e : ℝ) : ℝ :=
  Z * mass_proton_qou mu_up mu_down + N * mass_neutron_qou mu_up mu_down
    - binding + Z * m_e

/-- Electron mass (MeV), CODATA 2022. -/
-- Ref: [codata2022] CODATA 2022
noncomputable def m_electron : ℝ := 0.51099895069

end QOU.Torsion
