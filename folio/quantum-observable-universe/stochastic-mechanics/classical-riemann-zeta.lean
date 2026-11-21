import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.NumberTheory.ArithmeticFunction
import Mathlib.Topology.Algebra.InfiniteSum.Basic

/-!
# QOU.AlgebraicSubstrate.ClassicalRiemannZeta

The classical Riemann zeta function ζ(s) defined as the adelic
global limit of local q-zeta functions, via the Euler product.

LaTeX label: `def:classical-riemann-zeta`
-/

set_option autoImplicit false


open Complex Filter

namespace QOU.AlgebraicSubstrate

/-- **Classical Riemann zeta function** as the adelic limit of local
    q-zeta functions.

    The Dirichlet series ζ(s) = Σ_{n≥1} n^{-s} for Re(s) > 1,
    together with the Euler product representation and its relation
    to the local q-zeta functions at each prime.

    LaTeX: `\label{def:classical-riemann-zeta}`
    Ref: [weil1948] https://doi.org/10.1090/S0002-9904-1949-09219-4

    **`adelic_assembly : Prop` removed 2026-09-07 — universe-`Prop` typed, neither
    read nor constructed. Stating it needs the adelic data, not just `zeta`.** -/
structure ClassicalRiemannZeta where
  /-- The zeta function ζ : ℂ → ℂ (defined on Re(s) > 1,
      meromorphically continued). -/
  zeta : ℂ → ℂ
  /-- Dirichlet series representation: ζ(s) = Σ_{n≥1} n^{-s}
      for Re(s) > 1. -/
  -- Ref: [leitner2026] Chapter 8, Section 5
  dirichlet_series :
    ∀ (s : ℂ), 1 < s.re →
      HasSum (fun n : ℕ+ => (↑(n : ℕ) : ℂ) ^ (-s)) (zeta s)
  /-- Euler product: ζ(s) = ∏_p (1 - p^{-s})^{-1} for Re(s) > 1. -/
  euler_product :
    ∀ (s : ℂ), 1 < s.re →
      zeta s = ∏' (p : Nat.Primes), (1 - (↑(p : ℕ) : ℂ) ^ (-s))⁻¹

end QOU.AlgebraicSubstrate
