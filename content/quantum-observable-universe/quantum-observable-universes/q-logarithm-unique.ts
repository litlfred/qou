import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-logarithm-unique",
  title: "Uniqueness of the $q$-logarithm primitive (conditional)",
  lean: { ref: "qou:QOU.QLogarithm.unique_of_prim_rigid",
    validation: "not_checked",
  },
  uses: ["prop:q-logarithm-exists"],
  proofs: ["prf:q-logarithm-unique"],
  tags: ["uniqueness", "q-logarithm", "primitive", "hopf-algebra"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-06",
      body:
        "**Conditional, and previously false.** This block was backed by " +
        "`QLogarithm.unique_axiom`, an unconditional claim that primitives " +
        "agreeing on `coprod`, `counit` and `one` are equal. The axiom is " +
        "false: `coprod := fun x => (x, x)` satisfies both primitivity " +
        "fields and a constant zero counit satisfies `counit_eq_zero`, for " +
        "every `log_q`. Refuted by " +
        "`QOU.QAnalysisCounterexamples.not_qLogarithm_unique`. The live " +
        "statement carries the accompanying proof's Milnor-Moore rigidity " +
        "step, and the additivity it silently used, as explicit hypotheses.",
      see: "docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md",
    },
  ],
});
