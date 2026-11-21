import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:jet-prolongation",
  label: "rem:jet-planck-particle-spectrum",
  title: "Particle spectrum per Planck step",
  tags: [
    "jet-bundle",
    "planck-time",
    "particle-spectrum",
    "crossing-number",
    "big-bang",
    "chiral-cubic",
    "information-theory",
  ],
  uses: [
    "rem:jet-planck-steps",
    "ex:photon-wavefront",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-20", body: "Owner ruling 2026-11-20 (option B of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`): a quark is an unknot strand of the pure Borromean braid $\\mathcal{B}_3$ (`def:up-quark`); $T_{2,3}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of $\\mathfrak{u}$ and $\\mathfrak{d}$, not their knot types. The identification in this block was reworded on that date; its mathematics was not changed. Assumed: the up and down quarks appear at Planck step 3 because they were taken to be the trefoil pair (crossing number 3). Needs re-scoping: the jet step at which the quarks themselves appear, now that each is an unknot strand carrying one crossing letter. Still valid: the electron and positron at step 3, and the Borromean baryon at step 4 as stated for the three-component link." },
  ],
});
