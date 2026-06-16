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
      body: "**Two-layer convention (owner-clarified 2026-06-16).** Canonical math triple = `(m_e, m_μ/m_e → q₀, m_π)`; **CAL-3 = `m_π`**, and **`𝔔_β` is derived** (the bar-odd `sinh` partner of the bar-even `cosh` meson scale `m_π`). The §\"CAL-3\" section below discusses the *derived* `𝔔_β`/`E₀` hadronic observable — its epistemic status is unchanged, but it is **not** a calibration; the third calibration is `m_π`. CAL-2 stays the canonical lepton ratio `m_μ/m_e` (it dimensionalises to `Vol(4₁)`); the **Physical-Observations** layer may numerically anchor `q₀` on the more-precise proton ratio `m_p/m_e` (re-pin 2026-05-28, `01c18125`), making `m_μ/m_e` a 9.5σ cross-check prediction — a precision substitution, not a change to CAL-2. (m_μ L2 status convention note: ratio-anchored meets 100× to noise; bare-categorical `4₁` Geom misses ~964×, PR #1556.) Live compute: `tools/qou-substrate/python/qou_substrate/constants.py`.",
      see: "https://github.com/litlfred/qou/blob/claude/gracious-lovelace-uzuovl/docs/audits/2026-06-16-q-anchor-drift-and-local-q-routes.md",
    },
  ],
});
