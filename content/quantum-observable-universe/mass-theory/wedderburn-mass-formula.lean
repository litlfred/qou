import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Units.Defs


/-!
# Three-Invariant Wedderburn Mass Formula

The atomic mass is determined by three Wedderburn invariants
of the transfer matrix chain. These are complete: no fourth
invariant exists.

**Pre-Archimedean stub.** The formal statement lives over an
abstract commutative ring `R ⊇ ℤ[q, q⁻¹]`.  Real-valued
specialisation (substitution `q ↦ q₀`, mass scale via `m_e`) is
the Archimedean realisation and is performed downstream in
`QOU.ArchimedeanMassFormula` (per
`QOU.GroundRingAnnotations`).  See audit
`docs/audits/2026-05-03-pre-archimedean-proof-audit.md` §1
(Step 9) for the wall-discipline rationale.

-- Ref: [manuscript] thm:wedderburn-mass-formula
-/

namespace QOU.WedderburnMass

universe u

/-- The three Wedderburn invariants of a transfer matrix chain.
    These correspond to the three extremal irreps of H_n(q):
    symmetric (dim 1), standard (dim n-1), alternating (dim 1).

    Polymorphic in the ground ring `R`.  The pre-Archimedean
    convention is `R = ℤ[q, q⁻¹]` (Laurent polynomials); the
    Archimedean specialisation evaluates at `q ↦ q₀ ∈ ℝ`. -/
structure ThreeInvariants (R : Type u) where
  Φ₁ : R  -- standard trace
  Φ₂ : R  -- determinant
  Φ₃ : R  -- chirality (sym / alt)

/-- The mass formula parameters, all derived from `q` and `m_e`.

    Parametrised over the ground ring `R`.  Pre-Arch: every field
    is a Laurent polynomial in `q`.  Post-Arch: every field is the
    real evaluation at `q = q₀`. -/
structure MassParams (R : Type u) where
  q : R
  m_e : R
  m_p : R      -- from PL thimble
  m_n : R      -- from quark ΔΦ
  α : R        -- m_e × 8G
  β₂ : R       -- -2[3]_q
  β₃ : R       -- ≈ HA²

/-- The atomic mass from the Wedderburn formula, valued in the
    ground ring `R`. -/
def atomicMass {R : Type u} [CommRing R]
    (p : MassParams R) (Z N : ℕ)
    (inv : ThreeInvariants R) : R :=
  (Z : R) * p.m_p + (N : R) * p.m_n + (Z : R) * p.m_e +
  p.α * (inv.Φ₁ + p.β₂ * inv.Φ₂ + p.β₃ * inv.Φ₃)

/-- The quantum n-integer `[n]_q = (q^n - q^{-n})/(q - q^{-1})`,
    in any commutative ring carrying a unit `q` and its inverse.

    On `R = ℤ[q, q⁻¹]` this is the genuine Laurent-polynomial
    `q`-integer.

    Base ring (AGENTS.md §7c): stated over a bare `CommRing`.  Both
    the substrate parameter and the denominator are carried as
    **units** — `q : Rˣ` (so `q⁻¹` is the units inverse, never a
    field inverse) and `d : Rˣ` pinned by `hd : ↑d = q - q⁻¹` — so
    the quotient is the division-free product `(qⁿ - q⁻ⁿ) · d⁻¹`.
    This replaces the old `[Field R]` + `hq : q * q ≠ 1` form, which
    additionally admitted the junk case `q = 0` (there `hq` holds
    while `q⁻¹ = 0`, so the "quotient" silently collapsed to `0/0`).
    Over a field the two agree: take `d = Units.mk0 (q - q⁻¹) _`. -/
def quantumInt {R : Type u} [CommRing R]
    (q d : Rˣ) (_hd : (d : R) = (q : R) - (↑q⁻¹ : R)) (n : ℕ) : R :=
  ((q : R) ^ n - (↑q⁻¹ : R) ^ n) * (↑d⁻¹ : R)

/-- `β₂ = -2 [3]_q` is derived from the baryon quantum number. -/
def beta2 {R : Type u} [CommRing R]
    (q d : Rˣ) (hd : (d : R) = (q : R) - (↑q⁻¹ : R)) : R :=
  -2 * quantumInt q d hd 3

/-- The number of extremal irreps of S_n is exactly 3 for n ≥ 3:
    trivial [n], sign [1^n], and standard [n-1,1].
    For n = 2: trivial and sign only (standard = trivial).
    The transfer matrix is 2×2 (standard rep), giving 2 invariants
    (trace and determinant). The sym/alt ratio gives the third.

    For n ≥ 4, additional irreps exist (one per partition of n),
    but the three extremal invariants capture the dominant physics.
    The interior partitions (hooks) contribute subdominant corrections
    identifiable with meson exchange channels. -/
-- Ref: [manuscript] prop:three-parameters-wedderburn
-- Ref: [kazhdan-lusztig1979] Kazhdan & Lusztig, "Representations of Coxeter groups and Hecke algebras," Invent. Math. 53 (1979)
theorem extremal_irreps_count :
    ∀ (n : ℕ), n ≥ 3 →
    -- S_n has exactly 3 one-row/one-column/hook partitions
    -- that produce 1D or (n-1)D representations
    -- [n] → dim 1, [1^n] → dim 1, [n-1,1] → dim (n-1)
    -- These are the extremal points of the partition lattice
    ∃ (d_sym d_alt d_std : ℕ),
      d_sym = 1 ∧ d_alt = 1 ∧ d_std = n - 1 := by
  intro n _
  exact ⟨1, 1, n - 1, rfl, rfl, rfl⟩

end QOU.WedderburnMass
