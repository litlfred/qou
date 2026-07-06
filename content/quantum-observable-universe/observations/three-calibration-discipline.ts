import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-calibration-discipline",
  title:
    "Three-calibration discipline ($m_e$, $m_\\mu$, $m_\\pi$) aligned to (co)homological data",
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
    "prop:substrate-consistency-window",
    "prop:calibration-cohomology-alignment",
  ],
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
      body: "**The cohomological mapping is structural; the calibration *choice* is independent.** The proposition maps $m_e \\leftrightarrow$ the $W$-plane scale, $q_0 \\leftrightarrow$ the $W$-plane modulus (anchored by the lepton ratio $m_\\mu/m_e$), and $m_\\pi \\leftrightarrow$ the orthogonal $\\mathrm{Vol}(\\mathrm{Hopf})=0$ meson class — the three real degrees of freedom of $H^1 = 2W$ (see [`prop:calibration-cohomology-alignment`](../mass-theory/calibration-cohomology-alignment.md)). These are categorically forced. That they are pinned by CODATA/PDG values *rather than derived structurally* is an independent stance. Open derivation work in flight: PR #1127 (CAL-3 net-ansatz finding), PR #1246 (CAL-2 self-referential critique), and the substrate-$q_0$ workplan (re-opened 2026-05-25). See [`rem:epistemic-status-of-calibrations`](epistemic-status-of-calibrations.md) for the unified accounting per-CAL.",
      see: "https://github.com/litlfred/qou/pull/1246",
    },
    {
      kind: "refined-framing",
      date: "2026-06-16",
      body: "**Two-layer calibration convention (owner-clarified 2026-06-16).** The **canonical mathematical** calibration triple is `(m_e, m_μ/m_e → q₀, m_π)` with `𝔔_β` **derived** (the bar-odd `sinh` partner of the bar-even `cosh` meson scale `m_π`; see `substrate-cohomology-calibration-story`). In the **Physical-Observations** layer one may substitute a *derived* quantity of smaller experimental error for a calibration — concretely `q₀` is numerically anchored on the proton ratio `m_p/m_e` (0.06 ppb vs the muon ratio's 22 ppb; live solver `tools/qou-substrate/python/qou_substrate/constants.py::q_at`, re-pin 2026-05-28), making `m_μ/m_e` a `9.5σ` cross-check prediction (the μ–p substrate tension). This is a precision substitution, **not** a change to the canonical CAL-2. CAL-3 = `m_π` is forced because `m_π` is provably independent of `(m_e, q₀)` (`Vol(Hopf)=0`) whereas `𝔔_β = m_e·|q₀²−2q₀−1|(q₀+1)/(2q₀³)` is a function of CAL-1+CAL-2. **Remaining ripple:** `prop:three-calibration-inputs` still carries the older neutron-width (`𝔇_β`, h²) framing for CAL-2 — reconciled in the same PR to the canonical lepton-ratio framing.",
      see: "https://github.com/litlfred/qou/blob/claude/gracious-lovelace-uzuovl/docs/audits/2026-06-16-q-anchor-drift-and-local-q-routes.md",
    },
    {
      kind: "refined-framing",
      date: "2026-06-26",
      body: "**Supersedes the 2026-06-16 note above (owner ruling 2026-06-26, PR #2866).** The ideal *mathematical* canonical calibration triple is the weak-sector decay-width observables `(m_e, 𝔇_β, 𝔇_π)`, NOT three masses. CAL-2 = `𝔇_β` (neutron β-decay width, h²); CAL-3 = `𝔇_π` (pion decay width, h³). The masses `(m_e, m_μ/m_e, m_π)` and `𝔔_β = ℏ/𝔇_β` are the numerical *proxies*; `𝔔_β` is the **CAL-2 proxy**, not 'derived, not a calibration'. The modulus is overdetermined and pinned most precisely by `m_μ/m_e`, so `𝔔_β` reproduced from q₀ is a 0.17% cross-check. The 2026-06-16 'reconciliation to the lepton-ratio framing' is reversed: the `𝔇_β` framing is canonical.",
      see: "https://github.com/litlfred/qou/pull/2866",
    },
  ],
});
