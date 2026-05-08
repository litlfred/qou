import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:figure-eight-bw-coefficients",
  title:
    "Figure-eight BW coefficients from Wedderburn-Artin channel decomposition",
  lean: { ref: "qou:QOU.BraidKnot.figure_eight_bw_coefficients",
    validation: "not_checked",
  },
  uses: [
    "prop:nuclear-knot-classification",
    "conj:q-integer-mass-formula",
    "prop:bw-categorical-descent",
    "prop:wedderburn-trace-identity",
  ],
  tags: [
    "figure-eight",
    "bethe-weizsacker",
    "wedderburn-artin",
    "nuclear-binding",
    "character-ratio",
    "amphicheiral",
  ],
});
