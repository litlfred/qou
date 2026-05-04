import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chirality-writhe-ribbon-derivation",
  title:
    "Chirality factor $1 + w \\cdot h$ from ribbon-twist framing (writhe $w$)",
  lean: {
    ref: "qou:QOU.BraidKnot.ChiralityWritheRibbon.chirality_writhe_ribbon",
    validation: "not_checked",
  },
  uses: ["prop:e-infinity-page-identifications"],
  tags: [
    "chirality",
    "writhe",
    "ribbon",
    "kauffman-framing",
    "derivation",
    "term-5",
  ],
});
