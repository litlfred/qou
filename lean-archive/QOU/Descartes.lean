/-!
# Descartes Universe — Module Index

Re-exports all Descartes universe formalization modules.

**Note to reader**: all Lean proofs in this module work exclusively
over `ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).  Numerical
evaluations at the substrate parameter `q₀ ≈ 1.1098` appear only
in Chapter 7 (Physical Observations) and are NOT part of the
formal proof chain.
-/

import QOU.Descartes.GroundRing
import QOU.Descartes.TorusKnot
import QOU.Descartes.TransferMatrix
import QOU.Descartes.BetaDecay
