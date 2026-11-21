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
    "prop:leray-profile",
  ],
  authorNotes: [
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
