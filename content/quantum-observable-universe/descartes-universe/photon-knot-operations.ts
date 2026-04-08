import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:breit-wheeler-pair-production",
  label: "rem:photon-knot-operations",
  title:
    "Photon--photon pair production with torus knot operators",
  tags: [
    "photon",
    "pair-production",
    "torus-knot",
    "normal-form",
    "hecke-algebra",
    "colored-photon",
    "4-term-photon",
  ],
  uses: [
    "def:breit-wheeler-pair-production",
    "rem:knot-basis-color-content",
    "rem:knot-particle-dictionary",
    "rem:particle-nf-table",
  ],
});
