import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-exponential-unique",
  title: "Uniqueness of the $q$-exponential grouplike (conditional)",
  lean: { ref: "qou:QOU.QExponential.unique_of_flow_rigid",
    validation: "not_checked",
  },
  uses: ["prop:q-exponential-exists"],
  proofs: ["prf:q-exponential-unique"],
  tags: ["uniqueness", "q-exponential", "grouplike", "hopf-algebra"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-06",
      body:
        "**Conditional, and previously false.** This block was backed by " +
        "`QExponential.unique_axiom`, an unconditional claim that grouplikes " +
        "agreeing on `coprod`, `counit` and `D_q` are equal. The axiom is " +
        "false: `coprod := fun x => (x, x)`, a constant counit and " +
        "`D_q := id` satisfy all three structure fields for every `e_q`. " +
        "Refuted by `QOU.QAnalysisCounterexamples.not_qExponential_unique`. " +
        "A verbatim duplicate stood in `q-exponential.lean`; both are " +
        "deleted. The live statement carries the accompanying proof's own " +
        "rigidity step, and the additivity it silently used, as explicit " +
        "hypotheses.",
      see: "docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md",
    },
  ],
});
