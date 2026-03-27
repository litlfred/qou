import { definition } from "../../schema/builders";

export default definition({
  label: "def:lepton-number-categorical",
  title:
    "Lepton number as the Skein smoothing count",
  tags: [
    "lepton-number",
    "skein-relation",
    "smoothing",
    "conservation-law",
    "categorical",
    "weak-force",
  ],
  lean: {
    decl: "QOU.Descartes.LeptonNumber",
    validation: "not_checked",
  },
  uses: [
    "def:beta-decay-skein",
    "def:electron-knot",
    "def:positron-knot",
    "def:neutrino-knot",
  ],
});
