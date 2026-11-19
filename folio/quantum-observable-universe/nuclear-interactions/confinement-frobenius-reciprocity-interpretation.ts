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
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalisation note: exact vanishing $\\det G = 0$ on $H_n$ with the $(1^3)$ block spanning the radical is formalised in `lean/QOU/QBeta/MarkovGramDegenerate.lean`.",
    },
  ],
});
