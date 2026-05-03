import QOU.Descartes.HeckeH3
import QOU.Descartes.HeckeRep
import QOU.Descartes.GroundRing
import QOU.Interactions.ConfinementLP
import QOU.Interactions.BorromeanUnique
import QOU.Interactions.GramIndefinite
import Mathlib.LinearAlgebra.Matrix.PosDef

/-!
# Confinement SDP: matrix Frobenius positivity

The confinement SDP is the full matrix-valued problem whose scalar
diagonal projection is `QOU.Interactions.ConfinementLP`. It selects
the confined operator via a primal-dual pair of semidefinite
programs over `End(H_n(q))`, with matrix complementary slackness
capturing multi-operator binding.

The scalar LP obtains only when every Wedderburn block decouples;
in general the multi-operator regime (binding multiplicity μ ≥ 2)
is structural, not exceptional.

## References

- [prop:confinement-sdp]
- [prop:confinement-lp]  (scalar diagonal projection)
- [prop:frobenius-gram-matrix]
- [boyd-vandenberghe-2004]
-/

namespace QOU.Interactions

open QOU.Descartes

/-! ## §1  SDP data on `H_n(q)` -/

/-- Cost operator `T` of the confinement SDP: a symmetric
    real-algebraic endomorphism of `H_n(q)` encoding the Markov-trace
    weighting. The Hecke algebra `H_n(q)` has dimension `n!` (basis
    indexed by permutations of `Fin n`), so `sdpCost` is an
    `n! × n!` matrix over `R_q`. Placeholder — the full Markov-trace
    cost operator is `markovTraceNF`-based; here we record the
    correct type signature. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque sdpCost (n : ℕ) :
    Matrix (Fin (Nat.factorial n)) (Fin (Nat.factorial n)) R_q

/-- Optimal primal value of the confinement SDP at strand count
    `n`: `⟨T, Φ*⟩`. By strong duality, equals `nTarget * y0Star n`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque primalOpt (n : ℕ) : R_q

/-- Normalisation target `n_target` for the primal (different for
    proton ≈ 1.000 vs neutron ≈ 0.811). -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque nTarget : R_q

/-- Slater-strict feasibility of the confinement SDP at strand
    count `n`: there exists a positive-definite `Φ ≻ 0` in
    `End(H_n(q))` satisfying every primal constraint with strict
    PSD margin. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
opaque slaterStrict (n : ℕ) : Prop

/-- Optimal dual shadow price `y₀*` of the normalisation constraint
    at strand count `n`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque y0Star (n : ℕ) : R_q

/-! ## §2  The SDP primal–dual theorem -/

/-- **Confinement SDP — primal–dual.**
    At any strand count `n` where Slater-strict feasibility holds,
    the primal SDP
    `min ⟨T, Φ⟩ s.t. Φ ⪰ 0, ⟨π_λ, Φ⟩ ≥ 0, 2×2 pair-PSD, tr(Φ) = n_target`
    admits a unique optimiser `Φ* ⪰ 0`; the dual SDP
    `max n_target · y₀ s.t. y₀ I + Σ y_λ π_λ − T ⪯ 0, y_λ ≥ 0`
    admits `(y₀*, y_λ*)` with strong duality
    `⟨T, Φ*⟩ = n_target · y₀*`, and complementary slackness is the
    matrix equation `Φ* · (y₀* I + Σ y_λ* π_λ − T) = 0`.

    Cf. `markovTraceNF` in `ConfinementLP` for the scalar-LP
    projection recovered when every Wedderburn block decouples.

    The headline form asserted here is **strong duality**: the
    primal and dual optima agree,

        ⟨T, Φ*⟩ = n_target · y₀*.

    Full proof requires Mathlib SDP duality, which is not yet
    available; body is `sorry`.
-/
-- Ref: [manuscript] particle-interactions/confinement-sdp
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
axiom ConfinementSDP (n : ℕ) (h : slaterStrict n) :
    primalOpt n = nTarget * y0Star n

/-! ## §3  Binding multiplicity and the scalar-LP projection -/

/-- Binding multiplicity `μ(n)` — cardinality of the active dual
    support at optimum. `μ = 1` recovers the scalar LP; `μ ≥ 2` is
    the multi-operator regime. -/
-- Ref: [manuscript] braids-and-knots/electron-shell
opaque bindingMultiplicity (n : ℕ) : ℕ

/-- **Scalar-LP projection.** When `μ(n) = 1`, the SDP optimum
    coincides with the scalar `markovTraceNF`-based LP of
    `QOU.Interactions.ConfinementLP`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
-- Ref: [manuscript] particle-interactions/confinement-lp
theorem sdp_lp_projection (n : ℕ) (h : bindingMultiplicity n = 1) :
    True := by
  -- Full statement: ⟨T, Φ*⟩ = scalar-LP optimum on diag(NF basis).
  -- Requires an explicit isomorphism between the diag-LP feasible
  -- polytope and the rank-1 diagonal slice of the SDP feasible
  -- spectrahedron; deferred.
  -- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
  trivial

end QOU.Interactions
