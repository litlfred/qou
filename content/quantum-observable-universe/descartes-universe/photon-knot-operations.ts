import { remark } from "../../schema/builders";

export default remark({
  label: "rem:photon-knot-operations",
  title: "Photon knot operations and NF decompositions",
  interprets: "def:breit-wheeler-pair-production",
  tags: [
    "pair-production",
    "torus-knot",
    "hecke-normal-form",
    "photon",
    "trefoil",
  ],
  uses: [
    "def:breit-wheeler-pair-production",
    "rem:knot-particle-dictionary",
    "rem:knot-basis-color-content",
    "def:quark-antiquark-production",
  ],
});
