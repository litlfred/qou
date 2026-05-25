import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:nsi-q-deformed-kernel",
  lean: { ref: "qou:QOU.BraidsKnots.nsi_q_deformed_kernel",
    validation: "not_checked",
  },
  title: "$q$-deformed commutator replaces $1/r^2$ with a hard kernel at $r = \\hbar_q$",
  tags: ["q-deformation", "r-matrix", "q-hodge-star", "quantum-exclusion"],
  uses: ["def:q-hodge-star"],
  proofs: ["prf:nsi-q-deformed-kernel"],
});
