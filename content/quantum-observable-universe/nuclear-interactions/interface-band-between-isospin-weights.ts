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
});
