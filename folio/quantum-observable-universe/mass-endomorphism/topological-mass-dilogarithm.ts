import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:topological-mass-dilogarithm",
  renamedFrom: ["lem:topological-mass-dilogarithm"],
  lean: { ref: "qou:QOU.LiftingDescent.tm_dilogarithm_evaluation",
    validation: "not_checked",
  },
  title: "Quantum dilogarithm evaluation of exceptional-divisor contributions",
  tags: ["quantum-dilogarithm", "exceptional-divisor", "briggs-klein", "spectral-coordinates"],
  uses: [
    "lem:topological-mass-holonomy",
    "lem:topological-mass-transient-localisation",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "Demoted from lemma to conjecture (owner card \"Demote confinement-phase-stratification and topological-mass-dilogarithm to conjectures?\", option \"Demote both\", thread \"N2 Lean foundations\"). Proving was tried first: the first equality needs a definition of the non-abelian multiplicative integral and its evaluation in the Briggs–Klein chart, neither of which exists in Lean or Mathlib, and the Lean only projected a class field carrying it. Only the second equality, the integral form of the dilogarithm, holds, and it holds by definition.",
    },
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
