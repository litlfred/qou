import { remark } from "../../schema/builders";

export default remark({
  label: "rem:photon-nucleon-hecke-action",
  title: "A 4-term photon scatters off a bare nucleon as left multiplication in $H_3(q)$",
  interprets: "prop:four-term-pair-nucleon",
  uses: [
    "prop:four-term-pair-nucleon",
    "prop:confinement-universality",
    "def:breit-wheeler-pair-production",
  ],
  tags: [
    "photon", "nucleon", "scattering", "hecke-action",
    "compton", "left-multiplication", "bare-proton",
  ],
});
