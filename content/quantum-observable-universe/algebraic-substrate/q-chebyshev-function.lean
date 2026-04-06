/-!
# QOU.AlgebraicSubstrate.QChebyshevFunction

The q-Chebyshev function — partial sum of the q-von Mangoldt function
over maximal ideals with bounded norm.
LaTeX: `\label{def:q-chebyshev-function}`
-/

import Mathlib.Data.Real.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

/-- The q-Chebyshev function ψ_q(X).

    Sums the q-von Mangoldt weights Λ_q(𝔪) over all maximal ideals
    𝔪 ∈ MaxSpec(𝒪_q(ℬ)) with N(𝔪) ≤ X. -/
noncomputable def QChebyshevFunction
    (hbar_q : ℝ) (hbar_pos : 0 < hbar_q)
    (ideals : List MaxIdeal) (X : ℝ) : ℝ :=
  (ideals.filter (fun m => decide (m.norm ≤ X))).foldl
    (fun acc m => acc + QVonMangoldtFunction hbar_q hbar_pos m) 0

end QOU.AlgebraicSubstrate
