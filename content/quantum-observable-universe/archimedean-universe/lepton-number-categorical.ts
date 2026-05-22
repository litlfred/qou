import { definition } from "../../schema/builders";

export default definition({
  label: "def:lepton-number-categorical",
  title:
    "Categorical Lepton Number",
  tags: [
    "lepton-number",
    "skein-relation",
    "smoothing",
    "conservation-law",
    "categorical",
    "weak-force",
  ],
  lean: { ref: "qou:QOU.Descartes.LeptonNumber",
    validation: "not_checked",
  },
  uses: ["def:beta-decay-skein"],
});
