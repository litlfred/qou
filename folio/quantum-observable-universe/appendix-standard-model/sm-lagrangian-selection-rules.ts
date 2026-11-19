import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:gauge-action-groupoid",
  label: "rem:sm-lagrangian-selection-rules",
  title: "The action functional as selection rule",
  tags: ["appendix", "standard-model", "selection-rules", "conservation-laws", "2-group"],
  uses: [
    "def:gauge-action-groupoid",
    "def:coulomb-charge",
    "rem:self-dual-2group",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Formalized in the Lean sibling of `def:gauge-action-groupoid` (reversal, equivalence relation, residual-symmetry monoid) and `QOU/StandardModel/WritheMarkovInvariance.lean` (`writhe_conj` and `writhe_stabilize`).",
    },
  ],
});
