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
    {
      kind: "status",
      date: "2026-06-16",
      body: "**Live anchor is `m_p/m_e` (proton), not `m_μ/m_e`.** `q₀` was re-pinned 2026-05-28 (commit `01c18125`) from the muon ratio to the proton ratio (`m_p/m_e = 1836.152673426`, CODATA 2022, 0.06 ppb — the most precise anchor; `σ(q₀) ≈ 2853 ppQ`). `m_μ/m_e` and `Q_β` are now **predictions**. This proposition's title/body still state the pre-re-pin muon basis (live compute: `tools/qou-substrate/python/qou_substrate/constants.py`). **3rd-calibration fork:** this block makes `Q_β` the third input; the canonical-derivation cheat-sheet §1 diagram makes `m_π` the third input with `Q_β` derived. Owner resolution (2026-06-16): 3rd CAL = `m_π`, `Q_β` derived, `q₀` proton-anchored. Prose migration of the basis is a tracked follow-up (it ripples into `prop:three-calibration-inputs`, the Wedderburn-count proposition, and the SDP `m_π`-independence validation).",
      see: "https://github.com/litlfred/qou/blob/claude/gracious-lovelace-uzuovl/docs/audits/2026-06-16-q-anchor-drift-and-local-q-routes.md",
    },
  ],
});
