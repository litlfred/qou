import { remark } from "../../schema/builders";

export default remark({
  label: "rem:em-completeness-interpretation",
  title:
    "Spectral completeness interpretation: nothing is missing from $\\alpha_{\\mathrm{EM}}$",
  interprets: "thm:em-spectral-completeness",
  uses: [
    "thm:em-spectral-completeness",
    "cor:gauge-coupling-uniqueness",
    "prop:em-coupling-projection",
    "prop:spectral-sequence-collapse",
    "prop:confinement-categorical",
  ],
  tags: [
    "interpretation",
    "completeness",
    "scalar-channel",
    "specialisation",
  ],
});
