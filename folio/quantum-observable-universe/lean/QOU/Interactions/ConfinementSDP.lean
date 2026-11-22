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
  /-- **Strict positive-definiteness** on the block algebra.

      Carried as a field, not referenced: `R_q` is `LaurentPolynomial ℤ`,
      which has no order at all, so there is no `≻ 0` to appeal to. That
      absence is what made the old `slaterStrict : Prop` look unavoidable,
      and carrying the cone is what makes it avoidable. -/
  PosDef : Matrix (Fin (Nat.factorial n)) (Fin (Nat.factorial n)) R_q → Prop
  /-- **The primal feasible set** — `⟨π_λ, Φ⟩ ≥ 0`, the 2×2 pair-PSD
      conditions and `tr(Φ) = n_target`, as one predicate. Carried for the
      same reason: this class holds an optimum and no constraint set. -/
  Feasible : Matrix (Fin (Nat.factorial n)) (Fin (Nat.factorial n)) R_q → Prop
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

/-- **Slater's condition**: a strictly feasible point exists.

    Was `h.slaterStrict`, a field typed with the *universe* `Prop` — so the
    instance supplied a proposition and `True` was a legal choice. It is now
    the condition itself, `∃ Φ ≻ 0 feasible`, built from the cone and the
    constraint set the class carries.

    **This narrows the freedom; it does not remove it, and saying otherwise
    would be the over-claim.** An instance can still choose
    `PosDef := fun _ => True` and `Feasible := fun _ => True`, and
    `slaterStrict_is_freely_dischargeable` below still holds — with a
    different proof. What changed is *where* the choice lives: the SHAPE of
    Slater's condition is now fixed (an existential over matrices conjoining
    two predicates) and only the cone is chosen, where before the whole
    proposition was. A model that supplies a real PSD cone gets a real
    hypothesis; before, no model could. -/
def slaterStrict (n : ℕ) [h : HasConfinementSDPData n] : Prop :=
  ∃ Φ : Matrix (Fin (Nat.factorial n)) (Fin (Nat.factorial n)) R_q,
    h.PosDef Φ ∧ h.Feasible Φ

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
-- Ref: [leitner2026] particle-interactions/confinement-sdp
-- Ref: [boyd-vandenberghe-2004] §5.2.3 (Slater's condition) + §5.3
--      (strong duality for convex problems)
class HasConfinementSDPStrongDuality (n : ℕ) [HasConfinementSDPData n]
    (h : slaterStrict n) : Prop where
  /-- Strong duality.
      (Needs abstract LP/SDP duality infrastructure that does not exist in Mathlib; kept as an honest assumption for models without certificates) -/
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

/-- **Confinement SDP — primal–dual identity (conditional on a supplied
    duality identity; the Slater hypothesis is decorative).**

    Strong duality `⟨T, Φ*⟩ = n_target · y₀*` comes from the supplied
    `[hi : HasConfinementSDPStrongDuality n h]`, not from `h`.  The
    manuscript argument is the conic-duality theorem (Boyd–Vandenberghe
    §5.2.3 + §5.3): under a strictly feasible `Φ ≻ 0` the dual is solvable
    and primal = dual.  That step is **not in Mathlib**, and this is
    measured rather than repeated:
    `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §U7
    records `semidefinite program` **0**, `strict complementarity` **0**,
    `KKT` **0**, `duality gap` **0** and `LinearProgram` **0** at the
    pinned revision, with no optimisation layer under `Analysis/Convex/`.
    Tracked as bean `qou-apcl` (CONFIRMED).  So the step is supplied
    rather than derived.

    **`h : slaterStrict n` does no work, and can be discharged for free**
    (measured 2026-09-07, `lean`-direct exit 0; see
    `slaterStrict_is_freely_dischargeable` below).  `slaterStrict` is a
    field typed with the *universe* `Prop`, so the instance chooses the
    proposition, and `slaterStrict := True` makes `h := trivial`.  The
    signature therefore reads as Slater-conditional while constraining
    nothing.

    **That paragraph said this was "not encodable here". It was wrong, and
    it was mine (2026-09-07).** The reasoning — Slater is `∃ Φ ≻ 0
    feasible`, and this class carries no constraint set and no PSD order,
    `R_q` being `LaurentPolynomial ℤ` — is all correct. The conclusion does
    not follow: missing vocabulary is carried as fields, which is what
    `PosDef` and `Feasible` now are. `slaterStrict` is the condition itself.

    What survives of the caveat: an instance still chooses the cone, so the
    hypothesis is not thereby non-trivial in every model. See the note on
    `slaterStrict` for the exact scope of the improvement.

    **Two sentences here were false and were corrected on 2026-09-03**;
    the lead sentence above was not among them and asserted, until
    2026-09-07, that strong duality "is derived **from** the Slater-strict
    feasibility hypothesis".  It is not, and the paragraph below already
    said so — the correction reached the body and not the lead.

    **Two sentences here were false and are corrected (2026-09-03).** This
    docstring said the step "is discharged by `sorry` here" and that "the
    theorem no longer merely projects that class field". The body is
    `exact hi.strong_duality` and `#print axioms` reports no `sorryAx`: it
    *does* project, and there is no `sorry`.

    What it projects is legitimate, which is why only the prose changes.
    `[HasConfinementSDPStrongDuality n h]` is a conditional **input** a caller
    supplies when they already have the duality identity (e.g. from a numerical
    SDP solver, via the `Fact`-backed default instance) — not a data field
    positing the conclusion. The in-body comment records that the earlier
    version projected exactly such a data field, and that it was deleted. So the
    result is conditional on Slater *and* on the supplied duality, and this
    docstring now says so.

    Cf. `markovTraceNF` in `ConfinementLP` for the scalar-LP
    projection recovered when every Wedderburn block decouples. -/
-- Ref: [leitner2026] particle-interactions/confinement-sdp
-- Ref: [boyd-vandenberghe-2004] §5.2.3 (Slater's condition) + §5.3
--      (strong duality for convex problems)
theorem ConfinementSDP (n : ℕ) [HasConfinementSDPData n] (h : slaterStrict n)
    [hi : HasConfinementSDPStrongDuality n h] :
    primalOpt n = nTarget n * y0Star n := by
  -- The body previously read `exact HasConfinementSDPData.strong_duality`, projecting a
  -- `strong_duality` field the DATA class carried (doc-labelled "conclusion"), while this
  -- docstring said the conic-duality step "is discharged by `sorry` here" and that the
  -- theorem "no longer merely projects that class field". Both were false. The data-class
  -- field is deleted; `[HasConfinementSDPStrongDuality n h]` remains as the legitimate
  -- conditional input a caller with a solver-verified identity can supply.
  -- Ref: [boyd-vandenberghe-2004] §5.2.3 (Slater) + §5.3 (strong duality for convex
  --      programs) — the conic-duality step, which Mathlib has no SDP API for.
  -- Ref: [leitner2026] particle-interactions/confinement-sdp
  exact hi.strong_duality

/-- **The Slater hypothesis of `ConfinementSDP` is still freely
    dischargeable — by a different route since 2026-09-07.**

    It used to be free because `slaterStrict` was a `Prop`-universe FIELD:
    the instance supplied a proposition and `True` was legal. It is now the
    real condition `∃ Φ, PosDef Φ ∧ Feasible Φ`, and the instance below
    discharges it by choosing a trivial CONE instead — `PosDef` and
    `Feasible` both `fun _ => True`, witnessed at `Φ = 0`.

    Keeping this theorem is the point. The encoding narrowed the freedom
    without eliminating it, and a theorem that still proves the hypothesis
    free is the honest record of exactly how much was bought: the shape of
    Slater's condition, not its content.

    Note the statement is `∃ inst, slaterStrict` and **not** `∃ _inst,
    True`: the latter says only that the class is inhabited, which is the
    weak discriminator this corpus already has an audit about
    (`2026-08-09-inhabitation-is-a-weak-discriminator`).  What is claimed
    here is stronger and is the point — an instance whose Slater condition
    *holds*, by `trivial`.

    Kept in the file deliberately, in the idiom of
    `TransferMatrixEigenphase`: a demonstration that a field asserts
    nothing is the honest record while the field cannot yet be encoded. -/
theorem slaterStrict_is_freely_dischargeable (n : ℕ) :
    ∃ inst : HasConfinementSDPData n, @slaterStrict n inst :=
  ⟨{ sdpCost := 0, primalOpt := 0, nTarget := 0, y0Star := 0,
     PosDef := fun _ => True, Feasible := fun _ => True },
   ⟨0, trivial, trivial⟩⟩

-- The deprecated universal axiom `ConfinementSDP_axiom` has been
-- removed. Use `ConfinementSDP` (typeclass-backed) instead.

/-! ## §3  Binding multiplicity and the scalar-LP projection -/

/-- Binding multiplicity data — class-supplied evaluation of `μ(n)`
    (cardinality of the active dual support at optimum). `μ = 1`
    recovers the scalar LP; `μ ≥ 2` is the multi-operator regime. -/
-- Ref: [leitner2026] braids-and-knots/electron-shell
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
-- Ref: [leitner2026] particle-interactions/confinement-sdp
-- Ref: [leitner2026] particle-interactions/confinement-lp
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
  ⟨HasConfinementSDPStrongDuality.strong_duality hSlater⟩

/-- **Scalar-LP projection — per-instance form.** -/
theorem sdp_lp_projection (n : ℕ)
    [HasSDPBindingMultiplicity n] [HasConfinementSDPData n]
    (h : bindingMultiplicity n = 1)
    [hi : ScalarLPProjection n h] :
    primalOpt n = nTarget n * y0Star n :=
  hi.agrees

end QOU.Interactions
