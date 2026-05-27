import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-calibration-discipline",
  title:
    "Three-calibration discipline ($m_\\mu/m_e$, $m_e$, $Q_\\beta$) aligned to (co)homological degrees",
  tags: [
    "calibration",
    "dimensional-analysis",
    "substrate-parameter",
    "mass",
    "binding-energy",
    "beta-decay",
    "cohomology",
    "audit",
  ],
  uses: ["prop:substrate-consistency-window"],
  cites: [
    "jones1985",
    "kock2004",
    "wenzl1988",
  ],
  lean: { ref: "qou:QOU.Observations.threeCalibrationDiscipline" },
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-05-25",
      body: "**$H^0$/$H^1$/$H^2$ mapping is structural; the calibration *choice* is independent.** The proposition correctly maps $m_e \\leftrightarrow H^0$, $m_\\mu/m_e \\leftrightarrow H^1$, $Q_\\beta \\leftrightarrow H^2$ — these cohomological degrees are categorically forced. That these degrees are pinned by CODATA values *rather than derived structurally* is an independent stance. Open derivation work in flight: PR #1127 (CAL-3 net-ansatz finding), PR #1246 (CAL-2 self-referential critique), and the substrate-$q_0$ workplan (re-opened 2026-05-25). See [`rem:epistemic-status-of-calibrations`](epistemic-status-of-calibrations.md) for the unified accounting per-CAL.",
      see: "https://github.com/litlfred/qou/pull/1246",
    },
  ],
});
