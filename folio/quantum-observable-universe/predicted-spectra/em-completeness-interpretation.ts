import { remark } from "../../schema/builders";

export default remark({
  label: "rem:em-completeness-interpretation",
  title:
    "Spectral completeness interpretation: nothing is missing from $\\alpha_{\\mathrm{EM}}$",
  interprets: "thm:em-spectral-completeness",
  uses: [
    "cor:gauge-coupling-uniqueness",
    "prop:confinement-categorical",
  ],
  tags: [
    "interpretation",
    "completeness",
    "scalar-channel",
    "specialisation",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/alpha_em_form_ladder_probe.py",
    witness: "computations/alpha-em-form-ladder.witness.json",
    status: "verified",
  },
});
