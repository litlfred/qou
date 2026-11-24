import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:branching-identity-isospin-weights",
  title:
    "$\\mu_+ = y_{(3)} + y_{(2,1)}$, $\\mu_- = y_{(2,1)} + y_{(1^3)}$ --- hence at $z = q^3/(q^2+1)$ the singlet draws nothing from the radical",
  lean: {
    ref: "qou:QOU.Nuclear.GramSignature.mu_singlet_eq_y21_of_radical",
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
});
