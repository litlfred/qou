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
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/LiftingDescent/tm_dilogarithm_evaluation.lean` uses an " +
        "integral `∫`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
