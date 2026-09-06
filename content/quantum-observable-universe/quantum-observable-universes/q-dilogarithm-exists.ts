import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-dilogarithm-exists",
  title: "Inhabitation of the $q$-dilogarithm structure",
  lean: { ref: "qou:QOU.QDilogarithm.exists_of_addZeroClass",
    validation: "not_checked",
  },
  uses: [
    "def:q-dilogarithm",
    "prop:q-logarithm-exists",
  ],
  proofs: ["prf:q-dilogarithm-exists"],
  tags: ["existence", "q-dilogarithm", "pentagon-identity"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-06",
      body:
        "**Previously false, now axiom-free but weaker than the prose.** " +
        "This block was backed by `QDilogarithm.exists_axiom`, which " +
        "asserted `Nonempty (QDilogarithm H)` for every carrier with an " +
        "`Add` -- including `Empty`, where the `log_q : H` field cannot be " +
        "supplied. Refuted by `QOU.QAnalysisCounterexamples." +
        "not_qDilogarithm_exists_over_every_add_carrier`. Over an " +
        "`AddZeroClass` the statement is true and is now proved with no " +
        "axiom. The witness is the all-zero record, so what is established " +
        "is inhabitation of the structure, not the shuffle-recursion " +
        "construction of Li2^q; the prose has been narrowed to match, and " +
        "its previous claim of uniqueness moved to the conditional " +
        "`prop:q-dilogarithm-unique`.",
      see: "docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md",
    },
  ],
});
