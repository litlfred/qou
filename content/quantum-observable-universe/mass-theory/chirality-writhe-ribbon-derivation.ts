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
  computation: {
    engine: "mpmath",
    script: "computations/chirality_avg_content.py",
    witness: "computations/chirality-avg-content.witness.json",
    status: "experimental",
  },
  tags: [
    "chirality",
    "writhe",
    "ribbon",
    "kauffman-framing",
    "derivation",
    "term-5",
  ],
});
