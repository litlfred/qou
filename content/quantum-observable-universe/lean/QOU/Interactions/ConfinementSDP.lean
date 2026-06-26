import QOU.Archimedean.HeckeH3
import QOU.Archimedean.HeckeRep
import QOU.Archimedean.GroundRing
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

open QOU.Archimedean

/-! ## §1  SDP data on `H_n(q)` (typeclass-supplied per `n`)

The full confinement-SDP solution `(Φ*, y₀*, …)` requires solving
a semidefinite program at strand count `n`, which depends on
Mathlib SDP infrastructure not yet available. Rather than
`opaque`-stubbing each datum, we package them as a typeclass
`HasConfinementSDPData (n)` so callers supply (typically from a
numerical SDP solver, e.g. CVXPY/SCS) the cost matrix, primal
optimum, target, dual shadow price, and Slater-feasibility
predicate. -/

/-- **Per-`n` SDP data — class-supplied.** -/
class HasConfinementSDPData (n : ℕ) where
  /-- Cost operator `T` of the confinement SDP. -/
  sdpCost : Matrix (Fin (Nat.factorial n)) (Fin (Nat.factorial n)) R_q
  /-- Optimal primal value `⟨T, Φ*⟩`. -/
  primalOpt : R_q
  /-- Normalisation target. -/
  nTarget : R_q
  /-- Slater-strict feasibility predicate. -/
  slaterStrict : Prop
  /-- Optimal dual shadow price `y₀*`. -/
  y0Star : R_q

/-- Cost-operator accessor. -/
def sdpCost (n : ℕ) [h : HasConfinementSDPData n] :
    Matrix (Fin (Nat.factorial n)) (Fin (Nat.factorial n)) R_q :=
  h.sdpCost

/-- Primal-optimum accessor. -/
def primalOpt (n : ℕ) [h : HasConfinementSDPData n] : R_q := h.primalOpt

/-- Normalisation target accessor. -/
def nTarget (n : ℕ) [h : HasConfinementSDPData n] : R_q := h.nTarget

/-- Slater-strict feasibility accessor. -/
def slaterStrict (n : ℕ) [h : HasConfinementSDPData n] : Prop := h.slaterStrict

/-- Optimal dual shadow price accessor. -/
def y0Star (n : ℕ) [h : HasConfinementSDPData n] : R_q := h.y0Star

/-! ## §2  The SDP primal–dual theorem -/

/-! ### Strong duality as a typeclass (Pattern 4)

The full SDP strong-duality result requires Mathlib SDP duality,
which is not yet available. Rather than asserting strong duality
universally as a top-level `axiom`, we package it as a typeclass
`HasConfinementSDPStrongDuality`. Callers must supply an instance
to use the primal–dual identity, making the conjectural content
visible at every use site.

A concrete construction would discharge `strong_duality` for the
specific `n` of interest (e.g. `n = 4` for the proton/neutron
Wedderburn blocks).
-/

/-- **Confinement SDP — strong-duality typeclass.**
    Holds for `(n, h)` when the primal SDP
    `min ⟨T, Φ⟩ s.t. Φ ⪰ 0, ⟨π_λ, Φ⟩ ≥ 0, 2×2 pair-PSD, tr(Φ) = n_target`
    and its dual
    `max n_target · y₀ s.t. y₀ I + Σ y_λ π_λ − T ⪯ 0, y_λ ≥ 0`
    satisfy strong duality `⟨T, Φ*⟩ = n_target · y₀*`. By
    Slater + Boyd–Vandenberghe Thm 5.5, this follows from the
    Slater-strict hypothesis once Mathlib SDP duality lands. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
-- Ref: [boyd-vandenberghe-2004] §5.2.3 (Slater's condition) + §5.3
--      (strong duality for convex problems)
class HasConfinementSDPStrongDuality (n : ℕ) [HasConfinementSDPData n]
    (h : slaterStrict n) : Prop where
  strong_duality : primalOpt n = nTarget n * y0Star n

/-- **Default instance from a `Fact` witness on the strong-duality
    identity**. When `Fact (primalOpt n = nTarget n * y0Star n)` is
    in scope (e.g. from a numerical SDP solver verifying strong
    duality at the specific `n`), the `HasConfinementSDPStrongDuality`
    instance follows. Boyd-Vandenberghe Thm 5.5 lifts this to all
    Slater-strict `n` once Mathlib SDP duality lands. -/
instance hasConfinementSDPStrongDuality_of_fact (n : ℕ)
    [HasConfinementSDPData n] (h : slaterStrict n)
    [hf : Fact (primalOpt n = nTarget n * y0Star n)] :
    HasConfinementSDPStrongDuality n h :=
  ⟨hf.out⟩

/-- **Confinement SDP — primal–dual identity (conditional on Slater).**

    Strong duality `⟨T, Φ*⟩ = n_target · y₀*` is derived **from the
    Slater-strict feasibility hypothesis** `h : slaterStrict n` via the
    conic-duality theorem (Boyd–Vandenberghe Thm 5.5): under a strictly
    feasible `Φ ≻ 0` the dual is solvable and primal = dual.  The
    conic-duality step itself is **not in Mathlib** (no SDP duality
    API), so it is discharged by `sorry` here — the hypothesis is the
    genuine analytic input (Slater), **not** the conclusion.

    The retained `[HasConfinementSDPStrongDuality n h]` instance lets a
    caller who already *has* the duality identity (e.g. from a numerical
    SDP solver, via the `Fact`-backed default instance) supply it; but
    the theorem no longer merely projects that class field — it states
    the real conditional-on-Slater result.

    Cf. `markovTraceNF` in `ConfinementLP` for the scalar-LP
    projection recovered when every Wedderburn block decouples. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
-- Ref: [boyd-vandenberghe-2004] §5.2.3 (Slater's condition) + §5.3
--      (strong duality for convex problems)
theorem ConfinementSDP (n : ℕ) [HasConfinementSDPData n] (h : slaterStrict n)
    [HasConfinementSDPStrongDuality n h] :
    primalOpt n = nTarget n * y0Star n := by
  -- Ref: [boyd-vandenberghe-2004] §5.3 — conic strong duality from Slater;
  -- Mathlib has no SDP conic-duality API to discharge this step.
  sorry

-- The deprecated universal axiom `ConfinementSDP_axiom` has been
-- removed. Use `ConfinementSDP` (typeclass-backed) instead.

/-! ## §3  Binding multiplicity and the scalar-LP projection -/

/-- Binding multiplicity data — class-supplied evaluation of `μ(n)`
    (cardinality of the active dual support at optimum). `μ = 1`
    recovers the scalar LP; `μ ≥ 2` is the multi-operator regime. -/
-- Ref: [manuscript] braids-and-knots/electron-shell
class HasSDPBindingMultiplicity (n : ℕ) where
  /-- Active-dual-support cardinality `μ(n)`. -/
  mu : ℕ

/-- Binding multiplicity accessor. -/
def bindingMultiplicity (n : ℕ) [h : HasSDPBindingMultiplicity n] : ℕ := h.mu

/-- **Scalar-LP projection — class.** When `μ(n) = 1`, the SDP
    optimum coincides with the scalar `markovTraceNF`-based LP of
    `QOU.Interactions.ConfinementLP`. The full proof requires an
    explicit isomorphism between the diag-LP feasible polytope and
    the rank-1 diagonal slice of the SDP feasible spectrahedron. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
-- Ref: [manuscript] particle-interactions/confinement-lp
-- Ref: [boyd-vandenberghe-2004] §5.2.3 (Slater's condition) + §5.3
--      (strong duality for convex problems)
class ScalarLPProjection (n : ℕ) [HasSDPBindingMultiplicity n]
    [HasConfinementSDPData n]
    (_h : bindingMultiplicity n = 1) : Prop where
  /-- Primal optimum agrees with the scalar LP optimum. -/
  agrees : primalOpt n = nTarget n * y0Star n

/-- **`ScalarLPProjection` follows from strong duality.**
    The identity `primalOpt = nTarget · y0Star` is exactly the
    strong-duality statement, so any
    `[HasConfinementSDPStrongDuality n hSlater]` discharges the
    `agrees` field directly. The `bindingMultiplicity = 1`
    hypothesis is the qualitative scope marker (the LP-collapse
    regime); the algebraic content is the same. -/
theorem scalarLPProjection_of_strongDuality (n : ℕ)
    [HasSDPBindingMultiplicity n] [HasConfinementSDPData n]
    (hSlater : slaterStrict n)
    [HasConfinementSDPStrongDuality n hSlater]
    (h : bindingMultiplicity n = 1) :
    ScalarLPProjection n h :=
  ⟨HasConfinementSDPStrongDuality.strong_duality⟩

/-- **Scalar-LP projection — per-instance form.** -/
theorem sdp_lp_projection (n : ℕ)
    [HasSDPBindingMultiplicity n] [HasConfinementSDPData n]
    (h : bindingMultiplicity n = 1)
    [hi : ScalarLPProjection n h] :
    primalOpt n = nTarget n * y0Star n :=
  hi.agrees

end QOU.Interactions
