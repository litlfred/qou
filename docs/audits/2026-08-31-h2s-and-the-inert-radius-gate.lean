/-
  Bean `qou-z9ws` — two content-block sibling classes adjudicated, and one gate
  that can neither pass nor reject anything.

  WHY THIS FILE HAS NO IMPORTS.  Both classes live in content-block siblings,
  not modules, so nothing can `import` them.  Compile with the concatenating
  runner (invocation at the bottom of this header).

  ─────────────────────────────────────────────────────────────────────────
  1.  `H2SAngleS3HolonomyConjecture` — NOT vacuous

  It takes `d : H2SChiralData`, a pair of reals, and asserts they are equal.
  The parameter is supplied by the CALLER and the claim constrains it, so the
  class is satisfiable at `⟨0, 0⟩` and **refutable** at `⟨1, 0⟩` — both below.
  A class refutable at one parameter assumes something at every parameter, so
  `opening_eq_holonomy_of_conj` is a genuine conditional, not an empty one.

  Its content is thin in a different way, worth separating from vacuity: the
  class quantifies over an ARBITRARY `d`, while the physics claim is about one
  specific measured pair (the H₂S H–S–H opening above the pure-`p` 90° base,
  against the chiral `S³` braid-holonomy phase).  Nothing in the file pins `d`
  to either quantity, so the theorem is "if two reals are equal then they are
  equal" until a `d` is constructed from the actual angle and the actual
  holonomy.  That is a modelling gap, not a §3b-cond item-5 defect.

  ─────────────────────────────────────────────────────────────────────────
  2.  `RadiusOfConvergenceGateClass` — INERT: neither direction can be invoked

  This one has no witness below because none can exist, and that is the
  finding.  The gate is built on

      axiom qBetaCandidatePoleLocation : ℝ

  — an opaque global constant with no defining property.  Measured: the
  identifier occurs in exactly four places corpus-wide, all in that one file —
  the `axiom` line, the class field, and the two gate theorems.  Nothing gives
  it a value, and nothing states any property of it.  Therefore:

  - **The forward gate cannot fire.**  `RadiusOfConvergenceGateClass` has one
    field, `qBetaCandidatePoleLocation = u_substrate`.  Discharging it needs a
    proof of an equation about a constant with no defining property; no such
    proof exists or can be written.  So no instance can ever be supplied, and
    `qbeta_g_simple_pole_at_u_substrate` is unreachable.
  - **The reject gate cannot fire either.**  `radius_of_convergence_gate_reject`
    takes `h_candidate_pole : qBetaCandidatePoleLocation = u_0` as a hypothesis
    — the same unprovable shape.  So the refutation direction is unreachable
    for exactly the same reason as the acceptance direction.
  - **And it could not discriminate even if it could fire.**
    `qBetaCandidatePoleLocation` is a single *global*, not a function of a
    candidate.  The docstring says *"A candidate failing to predict this
    location is REFUTED"*, but there is no argument by which one candidate's
    predicted pole differs from another's.  Every candidate in the corpus
    shares one opaque constant.

  This is the same shape as the direction-sanity finding in
  [`2026-08-30-gate-classes-admit-zero.lean`](2026-08-30-gate-classes-admit-zero.lean)
  — a gate weaker than its prose — but by a different mechanism, and further
  along: those gates fire and admit too much; this one cannot fire at all.

  It is also a third distinct reason a declaration can be unreachable, after
  the false class field (`SkeinMassRelationHolds`) and the false side condition
  (`HadronicMass.pair_skein_denom_hypothesis_false`).  Here the hypothesis is
  not false — it is undecidable, because its subject is opaque.

  **What this does NOT say.**  It does not say the radius-of-convergence
  prediction is wrong.  `u_substrate = 0.008517234550156142` is a recorded
  measurement and the structural claim about the ratio test may well hold; the
  finding is that the Lean encoding cannot express it, because it names the
  candidate's pole with an `axiom` instead of a function of the candidate.  The
  repair is to make it one — `poleLocation : Candidate → ℝ` — which is an
  authorial change and is not attempted here.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build`):

      scripts/lean-sibling-witness-check.sh \
        docs/audits/2026-08-31-h2s-and-the-inert-radius-gate.lean \
        content/quantum-observable-universe/molecular-construction/h2s-angle-s3-braid-holonomy.lean

  Measured 2026-08-31: exit 0, 0 errors.
-/

namespace H2SProbe
open QOU.Molecular

/-- Satisfiable: the two quantities agree at the degenerate datum. -/
instance : H2SAngleS3HolonomyConjecture ⟨0, 0⟩ where
  angle_eq_holonomy := rfl

/-- **Refutable** at a datum where they disagree — so the class is not vacuous
at any parameter. -/
theorem h2s_refutable : ¬ H2SAngleS3HolonomyConjecture ⟨1, 0⟩ := by
  rintro ⟨h⟩
  norm_num at h

end H2SProbe
