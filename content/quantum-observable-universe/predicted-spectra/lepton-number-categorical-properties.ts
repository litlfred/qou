import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lepton-number-categorical-properties",
  interprets: "def:lepton-number-categorical",
  title:
    "Conservation, $\\mathbb{Z}$-grading, and the $\\chi = -6$ constraint on lepton number",
  tags: [
    "lepton-number",
    "skein-relation",
    "smoothing",
    "conservation-law",
    "categorical",
    "weak-force",
  ],
  uses: [
    "def:lepton-number-categorical",
    "def:beta-decay-skein",
    "prop:torus-knot-generators",
  ],
});
