import { remark } from "../../schema/builders";

export default remark({
  label: "rem:breit-wheeler-pair-production-derivation",
  interprets: "def:breit-wheeler-pair-production",
  title:
    "Color-dressed photon, polarization models, and the $4$-term Breit--Wheeler normal form",
  tags: [
    "breit-wheeler",
    "pair-production",
    "photon",
    "electron",
    "positron",
    "hecke-algebra",
    "colored-photon",
    "normal-form",
  ],
  uses: [
    "def:breit-wheeler-pair-production",
    "rem:knot-basis-color-content",
    "rem:physics-names-knot-operations",
    "prop:four-term-pair-nucleon",
  ],
});
