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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): `QOU/StandardModel/WritheMarkovInvariance.lean` proves `writhe_conj` (conjugation preserves the writhe) alongside `writhe_stabilize` (the vertical stabilisation move shifts the writhe by ±1)." },
  ],
});
