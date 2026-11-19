import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:interface-band-between-isospin-weights",
  title:
    "The admissible interface band $[z-h,\\,z]$ lies strictly between $\\mu_-$ and $\\mu_+$",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.band_strictly_between",
    validation: "not_checked",
  },
  uses: ["prop:isospin-singlet-binds-more"],
  tags: [
    "isospin",
    "interface",
    "impossibility",
    "convention-d",
    "deuteron",
    "trace-convention",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/hbond_vdw_sdp.py",
    witness: [
      "computations/hbond-vdw-sdp.witness.json",
      "computations/qbeta/qbeta-c3-ladder-trace-convention-sensitivity.witness.json",
      "computations/h2-molecular-binding.witness.json",
      "computations/probes/binding-closed-form-c-vs-d.witness.json",
      "computations/phase-transition-sdp-derivation.witness.json",
    ],
    status: "verified",
  },
});
