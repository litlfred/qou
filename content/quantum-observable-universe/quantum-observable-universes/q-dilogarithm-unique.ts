import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-dilogarithm-unique",
  title: "Uniqueness of the $q$-dilogarithm evaluation (conditional)",
  lean: { ref: "qou:QOU.QDilogarithm.eval_unique_of_pentagon_rigid",
    validation: "not_checked",
  },
  uses: ["prop:q-dilogarithm-exists"],
  proofs: ["prf:q-dilogarithm-unique"],
  tags: ["uniqueness", "q-dilogarithm"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-06",
      body:
        "**Conditional, and previously false.** This block was backed by " +
        "`QDilogarithm.unique_axiom`, which concluded `L1.Li2.1 = L2.Li2.1` " +
        "from agreement of `log_q`, `mul`, `compl` and `div`. The axiom is " +
        "false: `Li2` is not mentioned by the structure's `pentagon` field " +
        "-- the pentagon constrains `Li2_eval`, a different field -- so " +
        "`Li2` is free data. Refuted by " +
        "`QOU.QAnalysisCounterexamples.not_qDilogarithm_unique`. A verbatim " +
        "duplicate of the axiom stood in `q-dilogarithm.lean`; both are " +
        "deleted. The live statement concludes about `Li2_eval` and carries " +
        "the accompanying proof's one-dimensionality step as an explicit " +
        "`pentagon_rigid` hypothesis.",
      see: "docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md",
    },
  ],
});
