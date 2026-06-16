import { remark } from "../../schema/builders";

export default remark({
  label: "rem:epistemic-status-of-calibrations",
  title:
    "Epistemic status of CAL-1, CAL-2, CAL-3 — what is genuinely derived vs what is pinned",
  interprets: "prop:three-calibration-discipline",
  uses: [
    "prop:three-calibration-inputs",
    "prop:three-calibration-discipline",
  ],
  tags: [
    "calibration",
    "epistemology",
    "audit",
    "no-fitting",
    "cohomology",
    "open-derivation",
    "substrate-parameter",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-06-16",
      body: "**CAL-2 `q₀` pin is now `m_p/m_e` (proton), not `m_μ/m_e`.** Re-pinned 2026-05-28 (commit `01c18125`); `m_μ/m_e` is a 9.5σ *prediction*, so the §\"CAL-2\" text describing the `m_μ/m_e = Vol(4₁)/ℏ_q²` inversion records the pre-re-pin convention. The m_μ L2 status is convention-dependent: ratio-anchored (`m_e × (m_μ/m_e)_CODATA`) meets the 100× target to numerical noise, while bare-categorical (`4₁` Geom) misses ~964× (reconciliation in PR #1556). **CAL-3 fork:** this remark lists `Q_β` as the third input; the cheat-sheet §1 diagram makes `m_π` the third input with `Q_β` derived. Owner resolution (2026-06-16): 3rd CAL = `m_π`, `Q_β` derived. Live compute: `tools/qou-substrate/python/qou_substrate/constants.py`.",
      see: "https://github.com/litlfred/qou/blob/claude/gracious-lovelace-uzuovl/docs/audits/2026-06-16-q-anchor-drift-and-local-q-routes.md",
    },
  ],
});
