import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:delta-max-uniform-bound",
  title:
    "Uniform bound on the per-level jet residual $|\\Delta^{(n)}|$",
  tags: [
    "jet-tower",
    "convergence",
    "operator-norm",
    "markov-trace",
    "binding-energy",
    "legacy-phi-q-tower",
  ],
  lean: {
    ref: "qou:QOU.MassEndomorphism.delta_max_uniform_bound",
    validation: "not_checked",
  },
  uses: [
    // def:recursive-brane-tower is NOT listed although the proof invokes it
    // by name for A_{n+1} = A_n (x) Omega^1(A_n): it is already reachable
    // through this cone.
    "prop:jet-tower-convergence",
    // The End(A_{n+1}) splitting that puts every transient endomorphism in
    // ker tau-hat_n.
    "prop:descent-eigenspaces",
  ],
  cites: ["kassel1995", "leitner2026"],
  computation: {
    engine: "mpmath",
    script: "computations/gram-matrix-dual.py",
    witness: [
      "computations/gram-matrix-dual.witness.json",
      "computations/jet-tower-delta-max.witness.json",
      "computations/gram-h3-symbolic-regression.witness.json",
    ],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-09-04",
      body:
        "The deleted content-block sibling carried this note verbatim: *\"The " +
        "proof strategy based on representation dimension bound by braid length " +
        "is known to be incomplete/mathematically flawed.\"* It names Step 4 of " +
        "the narrative proof, which bounds the Jones-Wenzl module dimension " +
        "`d_q` by `L(beta) * ||rho(beta)||_op` citing Kassel-Turaev Prop. 4.4.3. " +
        "That source is not held in `library/`, so the citation has not been " +
        "checked here and the note is recorded as received, not re-derived. " +
        "What IS verified: the Lean formalisation " +
        "(`QOU.MassEndomorphism.DeltaMaxUniformBound`) does not assert Step 4 -- " +
        "`OperatorNormBound.per_level_bound` carries the combined Steps 1-4 " +
        "conclusion as a **hypothesis field** and `delta_max_uniform_bound` " +
        "derives `|Delta^(n)| <= Delta_max` from it, sorry-free " +
        "(`[propext, Classical.choice, Quot.sound]`). So the Lean is a rigorous " +
        "conditional and the open item is the per-level bound itself. " +
        "Migrated here when the `theorem delta_max_uniform_bound : sorry := sorry` " +
        "sibling was deleted: it shadowed the real library theorem of the same " +
        "name and the same namespace (AGENTS.md ss0a, no shadowing stubs).",
    },
  ],
});
