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
  uses: ["prop:jet-tower-convergence"],
  cites: ["kassel1995", "leitner2026"],
  computation: {
    engine: "mpmath",
    script: "computations/gram-matrix-dual.py",
    witness: "computations/gram-matrix-dual.witness.json",
    status: "verified",
  },
});
