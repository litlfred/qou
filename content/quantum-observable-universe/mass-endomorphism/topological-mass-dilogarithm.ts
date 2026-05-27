import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-dilogarithm",
  lean: { ref: "qou:QOU.LiftingDescent.tm_dilogarithm_evaluation",
    validation: "not_checked",
  },
  title: "Quantum dilogarithm evaluation of exceptional-divisor contributions",
  tags: ["quantum-dilogarithm", "exceptional-divisor", "briggs-klein", "spectral-coordinates"],
  uses: [
    "lem:topological-mass-holonomy",
    "lem:topological-mass-transient-localisation",
  ],
  proofs: ["prf:topological-mass-dilogarithm"],
});
