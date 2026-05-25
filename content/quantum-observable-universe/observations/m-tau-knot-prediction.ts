import { remark } from "../../schema/builders";

export default remark({
  label: "rem:m-tau-knot-prediction",
  title:
    "Simple $\\mathrm{Vol}(K_\\tau)/\\hbar_q^{k_\\tau}$ pattern for $m_\\tau/m_e$ — falsified at 1\\% (negative result)",
  interprets: "rem:calibration-inputs",
  uses: [
    "rem:calibration-inputs",
    "rem:epistemic-status-of-calibrations",
    "prop:three-calibration-discipline",
  ],
  cites: ["codata2022"],
  tags: [
    "calibration",
    "lepton-generation",
    "knot-volume",
    "negative-result",
    "falsifiable",
    "cohomology",
    "audit",
  ],
  computation: {
    witness: "folio-assistant/computations/m-tau-knot-prediction.witness.json",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-05-25",
      body: "**Honest negative result.** Per the CAL-2 audit's §5 option 4 (PR #1246), this remark surfaces a falsifiable test of the cohomological lepton-generation hierarchy. The naive extension ($m_\\tau/m_e = \\mathrm{Vol}(K_\\tau)/\\hbar_q^{k_\\tau}$ for some hyperbolic knot and integer $k$) is **falsified** at 1\\% precision across 108 candidate (knot, $k$) pairs from the SnapPy knot census up to 10 crossings + standard hyperbolic links. The best single-knot candidate ($\\mathrm{Vol}(8_1)/\\hbar_q^3 \\approx 3523.6$ vs CODATA $3477.23$) misses by 1.33\\%. No product-pair $\\mathrm{Vol}(K_1)\\mathrm{Vol}(K_2)/\\hbar_q^k$ matches within 0.1\\% either. This rules out the simplest pattern; extensions (volume + Chern-Simons, Whitehead doubling, $\\mathrm{Li}_n(q^{-2})/\\hbar_q^k$ for $n > 2$, multi-stratum sums) remain untested.",
      see: "https://github.com/litlfred/qou/pull/1246",
    },
  ],
});
