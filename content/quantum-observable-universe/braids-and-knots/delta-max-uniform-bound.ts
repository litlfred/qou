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
    decl: "QOU.MassEndomorphism.delta_max_uniform_bound",
    validation: "not_checked",
  },
  uses: [
    "prop:jet-tower-convergence",
    "rem:mass-endomorphism-jet-tower",
    "prop:mass-endomorphism-tower",
    "def:recursive-brane-tower",
    "thm:markov-trace-factorization",
    "prop:confinement-sdp",
  ],
  cites: ["kassel1995", "leitner2026"],
});
