import { remark } from "../../schema/builders";

export default remark({
  label: "rem:em-completeness-interpretation",
  title:
    "Spectral completeness interpretation: nothing is missing from $\\alpha_{\\mathrm{EM}}$",
  interprets: "thm:em-spectral-completeness",
  uses: [
    "cor:gauge-coupling-uniqueness",
    "prop:em-coupling-projection",
    "prop:confinement-categorical",
  ],
  tags: [
    "interpretation",
    "completeness",
    "scalar-channel",
    "specialisation",
  ],
});
