import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-codifferential-formula",
  title: "Closed formula for the $q$-codifferential $\\delta_q$",
  tags: ["codifferential", "reeb", "adjoint", "webster"],
  lean: { ref: "qou:QOU.QuantumGeometry.q_codifferential_formula",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-q-ext-deriv",
    "ex:reeb-decomposition",
  ],
});
