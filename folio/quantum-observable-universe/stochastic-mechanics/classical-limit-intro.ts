import { prose } from "../../schema/builders";

export default prose({ label: "sec:classical-limit-preamble",
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Skeleton of this section.** The remaining results share the [surreal rate calculus](#prop:surreal-rate-calculus) machinery. Treating the Reeb infinitesimal $\\varepsilon$ ([Reeb infinitesimal](#def:reeb-epsilon)) as a strictly positive infinitesimal in $\\mathbb{R}(\\varepsilon) \\subset \\mathbf{No}$, there are two categorical invariants:\n\n$$\n  \\Delta_q \\;\\asymp\\; \\varepsilon^3\n  \\qquad\\text{(mass-gap dissipation, infinitesimal),}\n$$\n$$\n  \\Omega_q \\;\\asymp\\; \\varepsilon^{-1}\n  \\qquad\\text{(Reeb period, transfinite).}\n$$\n\nThe [surreal squeeze](#lem:surreal-squeeze) $\\delta^2 \\cdot \\Omega_q > \\Delta_q$ holds strictly for every standard real $\\delta > 0$. Each millennium-problem remark applies this squeeze." },
  ] });
