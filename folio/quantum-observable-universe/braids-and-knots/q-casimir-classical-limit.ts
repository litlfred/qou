import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-casimir-classical-limit",
  title:
    "Classical limit $q \\to 1$ of the $q$-Casimir eigenvalue",
  tags: [
    "casimir",
    "quantum-group",
    "su-q-2",
    "classical-limit",
    "archimedean",
  ],
  lean: {
    ref: "qou:QOU.QCasimirEigenvalue_classical_limit",
    validation: "not_checked",
  },
  uses: ["def:q-casimir"],
  cites: ["kassel1995", "lusztig1993"],
});
