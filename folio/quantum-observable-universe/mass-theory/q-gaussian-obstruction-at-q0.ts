import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-gaussian-obstruction-at-q0",
  title:
    "Bożejko–Speicher $q$-Gaussian obstruction at the aether $q_0 > 1$",
  tags: [
    "q-gaussian",
    "bozejko-speicher",
    "moment-problem",
    "touchard",
    "crossing-number",
    "substrate-q0",
    "obstruction",
  ],
  lean: {
    ref: "qou:QOU.MassTheory.qGaussianObstructionAtQ0",
    validation: "not_checked",
  },
  cites: ["bozejko-speicher1991"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/m_p_substrate_identity_50dps.py",
    witness: "computations/m-p-substrate-identity-50dps.witness.json",
    status: "verified",
  },
});
