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

- [manuscript] §3-lifting-of-quantum-torsion/knot-particle-generation

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
-- Ref: CODATA 2022, [manuscript] §1
noncomputable def q_substrate : ℝ := 1.10997  -- :leanval[q_0]{precision=6}

/-- Quantum Planck constant ℏ_q = 1 - 1/q. -/
-- Ref: [manuscript] §1/quantum-planck-constant
noncomputable def hbar_q : ℝ := 1 - 1 / q_substrate

-- ═══════════════════════════════════════════════════════════════════
-- Torus knot generators
-- ═══════════════════════════════════════════════════════════════════

/-- A torus knot type T_{m,n} with coprime winding numbers. -/
-- Ref: [manuscript] §3/knot-particle-generation
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
-- Ref: [manuscript] §3/torus-knot-generators
def seifertGenus (T : TorusKnot) : ℕ := (T.m - 1) * (T.n - 1) / 2

/-- Torus knots have zero hyperbolic volume. -/
-- Ref: [manuscript] §3/knot-particle-generation
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
-- Dressed quark masses and pair Skein masses
-- ═══════════════════════════════════════════════════════════════════

/-- Dressed up-quark Skein mass (MeV), from CODATA nucleon masses. -/
-- Ref: CODATA 2022, [manuscript] §11/terminal-resolution-proof
noncomputable def mu_up : ℝ := 311.10

/-- Dressed down-quark Skein mass (MeV), from CODATA nucleon masses. -/
-- Ref: CODATA 2022, [manuscript] §11/terminal-resolution-proof
noncomputable def mu_down : ℝ := 312.39

/-- Pair Skein mass: S_ab(q) = (q·μ_a + q⁻¹·μ_b) / (q^½ + q^{-½}).
    This is the mass contribution from a single crossing pair in the
    Borromean braid of a nucleon. -/
-- Ref: [manuscript] §11/terminal-resolution-proof
noncomputable def pairSkeinMass (mu_a mu_b : ℝ) : ℝ :=
  (q_substrate * mu_a + (1 / q_substrate) * mu_b) /
  (Real.sqrt q_substrate + 1 / Real.sqrt q_substrate)

/-- S_uu ≈ 312.370 MeV. -/
noncomputable def skein_uu : ℝ := pairSkeinMass mu_up mu_up

/-- S_ud ≈ 312.950 MeV. -/
noncomputable def skein_ud : ℝ := pairSkeinMass mu_up mu_down

/-- S_dd ≈ 313.665 MeV. -/
noncomputable def skein_dd : ℝ := pairSkeinMass mu_down mu_down

-- ═══════════════════════════════════════════════════════════════════
-- Nucleon masses from pair Skein formula
-- ═══════════════════════════════════════════════════════════════════

/-- Proton mass = S_uu + 2·S_ud (MeV). -/
-- Ref: [manuscript] §11/terminal-resolution-proof
noncomputable def mass_proton_qou : ℝ := skein_uu + 2 * skein_ud

/-- Neutron mass = 2·S_ud + S_dd (MeV). -/
-- Ref: [manuscript] §11/terminal-resolution-proof
noncomputable def mass_neutron_qou : ℝ := 2 * skein_ud + skein_dd

-- ═══════════════════════════════════════════════════════════════════
-- Atomic mass computation from knot generation
-- ═══════════════════════════════════════════════════════════════════

/-- Mass of an atom with Z protons, N neutrons, and Z electrons,
    minus nuclear binding energy B. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def atomicMass (Z N : ℕ) (binding : ℝ) (m_e : ℝ) : ℝ :=
  Z * mass_proton_qou + N * mass_neutron_qou - binding + Z * m_e

/-- Electron mass (MeV), CODATA 2022. -/
-- Ref: [codata2022] CODATA 2022
noncomputable def m_electron : ℝ := 0.51099895069

end QOU.Torsion
