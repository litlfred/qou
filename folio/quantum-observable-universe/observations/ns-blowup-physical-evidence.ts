import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-blowup-physical-evidence",
  title:
    "Physical signatures of the Navier--Stokes blow-up: intermittency, GRBs, CMB anomalies",
  interprets: "prop:blowup-yekutieli",
  uses: [
    "rem:conway-normal-form",
    "sec:cmb-torsion-data",
    "rem:bec-vortex-data",
    "def:leray-profile",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): Finite intermittency exponents inconsistent with any surreal-order scaling disconfirm the NS-blowup reading of [NS surreal bound](#rem:ns-surreal-bound)." },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): Quantitative prediction: Along the Leray self-similar profile ([Leray profile](#def:leray-profile)), the distribution of velocity increments $\\delta u_r$ at separation $r$ satisfies $\\ordw(\\delta u_r) = -\\tfrac{r + 1}{3} \\ordw(d)$ in surreal-order notation ([Big-O via $\\ordw$](#rem:conway-normal-form)). Classical intermittency exponents are the standard parts of these surreal orders." },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): where the enstrophy transfinite $\\mathcal{Z}_q \\asymp \\varepsilon^{-4/3}$ outruns the mass-gap infinitesimal $\\Delta_q \\asymp \\varepsilon^3$ ([NS surreal bound](#rem:ns-surreal-bound), [blowup as lifting obstruction](#prop:blowup-yekutieli))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([calculus up to $\\varepsilon$](#rem:calculus-up-to-epsilon))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([NS surreal bound](#rem:ns-surreal-bound))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([millennium unification](#rem:millennium-unification))" },
  ],
  tags: [
    "navier-stokes",
    "blowup",
    "physical-evidence",
    "intermittency",
    "gamma-ray-burst",
    "cmb",
    "falsifiability",
    "millennium-problem",
  ],
});
