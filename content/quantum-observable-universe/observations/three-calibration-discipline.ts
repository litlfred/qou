import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-calibration-discipline",
  title:
    "Three-calibration discipline ($m_e$, $m_p/m_e$, $m_\\pi$) aligned to (co)homological data",
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
      body: "**The cohomological mapping is structural; the calibration *choice* is independent.** The proposition maps $m_e \\leftrightarrow$ the $W$-plane scale, $q_0 \\leftrightarrow$ the $W$-plane modulus (anchored by the proton ratio $m_p/m_e$), and $m_\\pi \\leftrightarrow$ the orthogonal $\\mathrm{Vol}(\\mathrm{Hopf})=0$ meson class — the three real degrees of freedom of $H^1 = 2W$ (see [`prop:calibration-cohomology-alignment`](../mass-theory/calibration-cohomology-alignment.md)). These are categorically forced. That they are pinned by CODATA/PDG values *rather than derived structurally* is an independent stance. Open derivation work in flight: PR #1127 (CAL-3 net-ansatz finding), PR #1246 (CAL-2 self-referential critique), and the substrate-$q_0$ workplan (re-opened 2026-05-25). See [`rem:epistemic-status-of-calibrations`](epistemic-status-of-calibrations.md) for the unified accounting per-CAL.",
      see: "https://github.com/litlfred/qou/pull/1246",
    },
    {
      kind: "refined-framing",
      date: "2026-06-16",
      body: "**Basis migrated to the proton + `m_π` calibration (this revision).** `q₀` was re-pinned 2026-05-28 (commit `01c18125`) from the muon ratio to the proton ratio (`m_p/m_e = 1836.152673426`, CODATA 2022, 0.06 ppb — the most precise anchor; live compute: `tools/qou-substrate/python/qou_substrate/constants.py`). Per the owner resolution (2026-06-16): the third calibration is `m_π` (the orthogonal `Vol(Hopf)=0` meson scale), `Q_β` is **derived** from `m_e` + `q₀`, and `q₀` is proton-anchored. The title, table, mass formula (`m_e^a m_π^c · Q_X(q₀)`), discussion, and Lean class (`ThreeCalibrationDiscipline`, field `m_pi`) have all been migrated to match [`prop:calibration-cohomology-alignment`](../mass-theory/calibration-cohomology-alignment.md). **Remaining ripple (owner-gated):** `prop:three-calibration-inputs` is internally inconsistent across three q₀-anchor framings (top table: neutron decay width `𝔇_β` at `h²`; Wedderburn map + proof: muon ratio; live: proton ratio). Reconciling it needs a decision on whether CAL-2's canonical *physical input* is the proton ratio (`H¹` modulus) or the neutron decay width (`h²`) — a jet-order question the 'proton-anchored' call does not settle.",
      see: "https://github.com/litlfred/qou/blob/claude/gracious-lovelace-uzuovl/docs/audits/2026-06-16-q-anchor-drift-and-local-q-routes.md",
    },
  ],
});
