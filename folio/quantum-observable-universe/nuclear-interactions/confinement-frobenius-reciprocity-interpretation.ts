import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:confinement-frobenius-reciprocity",
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
    "conj:confinement-frobenius-reciprocity",
    "conj:knot-factor-frobenius-pairing",
    "prop:mass-coefficient-shadow-price",
    "rem:yekutieli-stokes",
    "prop:confinement-operator-selection",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): — [`MarkovGramDegenerate.lean`](../lean/QOU/QBeta/MarkovGramDegenerate.lean)" },
  ],
});
