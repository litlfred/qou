/-!
# QOU.AlgebraicSubstrate.AdelicSubstrate — adelic substrate interface

Formalizes `def:adelic-substrate`.

The QOU framework's macroscopic substrate is the rational adele
ring `𝔸_ℚ = ℝ × ∏'_p ℚ_p`: an archimedean place `ℝ` (the
laboratory continuum) together with one non-archimedean local
ring per rational prime `p`, restricted-product compatible.

The interface below is abstract: a carrier type with an
archimedean projection and per-prime non-archimedean projections.
The QOU instance (not constructed here) identifies each `Loc p`
with the localized quantum-geometric state at the `p`-th
cyclotomic / Kummer level of the Habiro completion, and the
archimedean projection with the classical-limit functor.

## References

- [tate1967] Tate, *Fourier Analysis in Number Fields and Hecke's
  Zeta-Functions*. In *Algebraic Number Theory* (Cassels-Fröhlich,
  eds.), Academic Press, 1967.
-/

import Mathlib.Data.Real.Basic

namespace QOU.AlgebraicSubstrate

/-- The **adelic substrate** of the QOU framework.

    Abstract interface: a ring `Carrier` carrying an archimedean
    place (projection to `ℝ`) and one non-archimedean place per
    rational prime `p` (projection to a local quantum-state ring
    `Loc p`).

    Encodes the rational adele ring `𝔸_ℚ = ℝ × ∏'_p ℚ_p` as
    used by Tate's adelic Fourier analysis. -/
structure AdelicSubstrate where
  /-- The carrier ring of the substrate. -/
  Carrier : Type*
  /-- Local non-archimedean rings, indexed by rational primes. -/
  Loc : Nat → Type*
  /-- Archimedean projection π_∞ : A → ℝ (the laboratory continuum). -/
  archimedean : Carrier → ℝ
  /-- Non-archimedean projection π_p : A → Loc p at each prime p. -/
  nonArchimedean : (p : Nat) → Carrier → Loc p

end QOU.AlgebraicSubstrate
