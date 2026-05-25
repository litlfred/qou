-- Feynman transition amplitude as categorical trace
-- See QOU/FeynmanPathIntegrals.lean §2 for the full formalization
--
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [chari1994] Chari & Pressley, "A Guide to Quantum Groups," CUP 1994

import QOU.FeynmanPathIntegrals

/-!
The central proposition: the Feynman transition amplitude, evaluated on
the knot-type eigenbasis V^{⊗n} ≅ ⊕_λ V_λ ⊗ S_λ, equals the
Jones–Markov trace on the Hecke algebra H_n(q).

  ⟨ψ_f|ψ_i⟩_{eigenbasis} = Σ_λ dim_q(V_λ) · tr_{S_λ}(ρ(β)) = tr_M(ρ(β))

The absolute value gives the categorical mass at a single brane level:

  𝔪(ϱ)|_{single level} = |tr_M(ρ(β))| = |⟨ψ_f|ψ_i⟩_{eigenbasis}|

Lean declarations:
  - `QOU.FeynmanPathIntegrals.FeynmanCategoricalTrace`
  - `QOU.FeynmanPathIntegrals.amplitude_finite_sum`
  - `QOU.FeynmanPathIntegrals.mass_eq_abs_amplitude`
-/
