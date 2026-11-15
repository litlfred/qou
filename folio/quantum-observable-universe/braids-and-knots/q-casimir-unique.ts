import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "The Lean link previously pointed at `QCasimir.unique_up_to_scalar`, a wrapper around an axiom that was false: " +
        "it claimed every central element of an arbitrary ring is C_q plus a scalar (counterexample: (1,0) in R_q × R_q). " +
        "Even in U_q(su(2)) the centre is R_q[C_q], so C_q² is central and not C_q + scalar; the prose needs the " +
        "eigenvalue normalisation as a hypothesis. Axiom and wrapper removed; the link points at the refutation. Bean qou-n2un.",
    },
  ],
  label: "prop:q-casimir-unique",
  title: "Uniqueness of the $q$-Casimir element up to scalar",
  lean: { ref: "qou:QOU.QCasimir.not_unique_up_to_scalar_unconstrained",
    validation: "not_checked",
  },
  uses: ["prop:q-casimir-exists"],
  proofs: ["prf:q-casimir-unique"],
  tags: ["uniqueness", "casimir", "central-element"],
});
