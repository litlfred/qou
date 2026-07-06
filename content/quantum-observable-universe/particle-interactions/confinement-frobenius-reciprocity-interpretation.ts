import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:confinement-frobenius-reciprocity",
  label: "rem:confinement-frobenius-reciprocity-interpretation",
  title: "Master formula: ingredients, corollaries, computational protocol",
  tags: [
    "frobenius-pairing",
    "lp-duality",
    "shadow-price",
    "bound-state",
    "axial-coupling",
    "computational-protocol",
  ],
  uses: [
    "prop:confinement-frobenius-reciprocity",
    "conj:knot-factor-frobenius-pairing",
    "prop:mass-coefficient-shadow-price",
    "rem:yekutieli-stokes",
    "prop:confinement-operator-selection",
  ],
});
