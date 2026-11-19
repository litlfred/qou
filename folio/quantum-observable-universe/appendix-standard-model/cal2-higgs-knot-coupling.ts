import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:epistemic-status-of-calibrations",
  label: "rem:cal2-higgs-knot-coupling",
  title: "The CAL-2 proxy as a Higgs-knot volume coupling",
  tags: ["appendix", "standard-model", "higgs", "calibration", "mass"],
  uses: ["rem:epistemic-status-of-calibrations"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-01",
      body:
        "Bean qou-u9lt (tau-knot discussion review, " +
        "docs/audits/2026-08-01-tau-knot-discussion-review.md). Purely " +
        "interpretive: links the canonical table identity (4_1 = Higgs) " +
        "to the CAL-2 anchor formula. No new mathematical claim.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/m_tau_volume_target_probe.py",
    witness: "computations/m-tau-volume-target.witness.json",
    status: "verified",
  },
});
