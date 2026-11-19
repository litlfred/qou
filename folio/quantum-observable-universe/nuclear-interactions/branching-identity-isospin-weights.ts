import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:branching-identity-isospin-weights",
  title:
    "$\\mu_+ = y_{(3)} + y_{(2,1)}$, $\\mu_- = y_{(2,1)} + y_{(1^3)}$ --- hence under convention D the singlet draws nothing from the radical",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.mu_singlet_eq_y21_of_radical",
    validation: "not_checked",
  },
  uses: [
    "prop:isospin-singlet-binds-more",
    "prop:markov-branching-three-term",
  ],
  tags: [
    "branching",
    "isospin",
    "radical",
    "temperley-lieb",
    "bratteli",
    "trace-convention",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/y_lambda_cyclotomic_factor.py",
    witness: "computations/y-lambda-cyclotomic-factor.witness.json",
    status: "verified",
  },
});
