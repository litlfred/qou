import { remark } from "../../schema/builders";

export default remark({
  label: "rem:m-tau-knot-prediction",
  title:
    "The $m_\\tau$ knot prediction and its falsification",
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The quantified targets are pinned in the witness `m-tau-volume-target.witness.json`." },
    {
      kind: "status",
      date: "2026-06-03",
      body: "**Primary content moved to [`docs/audits/2026-06-03-m-tau-knot-prediction-falsification.md`](../../../docs/audits/2026-06-03-m-tau-knot-prediction-falsification.md).** Per AGENTS.md canonical-no-negative-result-in-paper discipline (PR #1758): the simple-knot-prediction empirical search is a falsified ansatz, not a substrate derivation; the audit doc carries the full search table + 5 queued extensions. This block remains in the paper as an interpretive forward-reference.",
      see: "https://github.com/litlfred/qou/pull/1758",
    },
  ],
});
