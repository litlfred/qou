import { remark } from "../../schema/builders";

export default remark({
  label: "rem:m-tau-knot-prediction",
  title:
    "m_τ knot-prediction (forward-reference to falsification audit)",
  interprets: "rem:calibration-inputs",
  uses: [
    "rem:calibration-inputs",
    "rem:epistemic-status-of-calibrations",
  ],
  cites: ["codata2022"],
  tags: [
    "lepton-generation",
    "knot-volume",
    "cohomology",
    "falsifiable",
    "audit-forward-reference",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-06-03",
      body: "**Primary content moved to [`docs/audits/2026-06-03-m-tau-knot-prediction-falsification.md`](../../../docs/audits/2026-06-03-m-tau-knot-prediction-falsification.md).** Per AGENTS.md canonical-no-negative-result-in-paper discipline (PR #1758): the simple-knot-prediction empirical search is a falsified ansatz, not a substrate derivation; the audit doc carries the full search table + 5 queued extensions. This block remains in the paper as an interpretive forward-reference.",
      see: "https://github.com/litlfred/qou/pull/1758",
    },
  ],
});
