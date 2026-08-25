import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-coefficient-is-hbar-q",
  title:
    "The Reeb coefficient of $D_\\nabla$ is the quantum Planck constant: $1 - q^{-1} = (q-1)/q$",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.reeb_coefficient_eq_hbar_q",
    validation: "not_checked",
  },
  // def:quantum-planck-constant is deliberately NOT listed: def:planck-time
  // already uses[] it, so naming both is transitively redundant on the
  // editorial relation (reading order is transitive).
  uses: ["def:planck-time"],
  tags: [
    "reeb-flow",
    "dirac-operator",
    "hbar-q",
    "information-theory",
  ],
});
