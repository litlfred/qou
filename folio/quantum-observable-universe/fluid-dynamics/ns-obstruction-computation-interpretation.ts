import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:ns-obstruction-computation",
  label: "rem:ns-obstruction-computation-interpretation",
  title: "Topological and analytic terms occupy complementary tower subgroups",
  uses: ["prop:ns-obstruction-computation"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped by owner decision (Q-VO9T-2 = 1, beans qou-nzyr, qou-507c, qou-hjl0). " +
        "The remark previously asserted that the topological and analytic terms occupy complementary " +
        "subgroups of the obstruction tower on $\\Sigma$. Old text, verbatim: " +
        "\"**Mathematical novelty.** Computing local Euler classes via excision ($H^2_{\\{p\\}}$) and " +
        "the Biot-Savart jet divergence are standard differential topology and fluid mechanics. The " +
        "novelty is bridging them to show that the analytic and topological terms occupy complementary " +
        "subgroups of the obstruction tower. This proves that adjustments in the topological background " +
        "manifold cannot cancel the classical divergence bounds: the obstruction persists across all " +
        "jet levels.\" Withdrawn because $H^2(\\Sigma, \\cdot) = 0$ on a 1D collision curve, " +
        "$H^2(\\Sigma_4, \\mathcal{O}_{\\Sigma_4}) = 0$ forces $\\delta_n = 0$, and the restated " +
        "`def:ns-regular-qou` places $\\mathrm{NS}(A) = e(\\xi)$ in the global surface group " +
        "$H^2(\\mathcal{S}, \\mathbb{Z})$.",
      see: "prop:ns-obstruction-computation",
    },
  ],
});
