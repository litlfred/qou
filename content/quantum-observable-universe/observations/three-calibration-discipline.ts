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
  uses: [
    "def:categorical-action",
    "def:frobenius-pairing",
    "def:mass-identity",
    "prop:mass-endomorphism-tower",
    "thm:jones-markov-trace",
    "prop:substrate-consistency-window",
  ],
  cites: [
    "jones1985",
    "kock2004",
    "wenzl1988",
  ],
  lean: { ref: "qou:QOU.Observations.threeCalibrationDiscipline" },
});
