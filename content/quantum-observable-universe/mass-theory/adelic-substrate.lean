-- Ref: [tate1967] Tate, Fourier Analysis in Number Fields and Hecke's Zeta-Functions
--   in Algebraic Number Theory (Cassels-Fröhlich, eds.), Academic Press, 1967.
-- Adelic substrate of the QOU framework: A_Q = R × ∏'_p Q_p.
--
-- Canonical declaration lives in: lean/QOU/AlgebraicSubstrate.lean
-- This sibling is a documentation-mirror of the QOU library declaration.

namespace QOU.AlgebraicSubstrate

/-- The **adelic substrate** of the QOU framework.

    Abstract interface: a ring `A` carrying an archimedean place
    (projection to `ℝ`) and a non-archimedean place per rational
    prime `p` (projection to a local quantum-state ring `Loc p`),
    together with the restricted-product compatibility of the
    rational adele ring `𝔸_ℚ = ℝ × ∏'_p ℚ_p`.

    The QOU instance identifies each `Loc p` with the localized
    quantum-geometric state at the `p`-th cyclotomic / Kummer
    level of the Habiro completion, and the archimedean projection
    with the classical-limit functor on the substrate. -/
structure AdelicSubstrate where
  /-- The carrier ring of the substrate. -/
  Carrier : Type*
  /-- Local non-archimedean rings, indexed by rational primes. -/
  Loc : Nat → Type*
  /-- Archimedean projection π_∞ : A → ℝ (the laboratory continuum). -/
  archimedean : Carrier → Real
  /-- Non-archimedean projection π_p : A → Loc p at each prime p. -/
  nonArchimedean : (p : Nat) → Carrier → Loc p

end QOU.AlgebraicSubstrate
