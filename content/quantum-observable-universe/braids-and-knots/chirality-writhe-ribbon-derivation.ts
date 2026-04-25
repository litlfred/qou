import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chirality-writhe-ribbon-derivation",
  title:
    "Chirality factor $1 + w \\cdot h$ from ribbon-twist framing (writhe $w$)",
  lean: {
    ref: "qou:QOU.BraidKnot.chirality_writhe_ribbon",
    validation: "not_checked",
  },
  uses: [
    "prop:chirality-from-frobenius-self-pairing",
    "prop:figure-eight-bw-coefficients",
    "thm:jones-markov-trace",
    "thm:frobenius-codim-universal",
    "prop:e-infinity-page-identifications",
  ],
  tags: [
    "chirality",
    "writhe",
    "ribbon",
    "kauffman-framing",
    "derivation",
    "term-5",
  ],
});
