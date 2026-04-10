import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cs-evaluation-faithfulness",
  title:
    "Faithfulness of the Chern--Simons evaluation on the brane tower",
  tags: [
    "chern-simons",
    "yekutieli",
    "faithfulness",
    "obstruction",
    "brane-tower",
  ],
  uses: [
    "prop:volume-tower-decomposition",
    "def:quantum-characteristic-classes",
    "prop:yekutieli-lifting",
  ],
  lean: {
    decl: "QOU.Descartes.CSEvaluationFaithful",
    file: "QOU/Descartes/HyperbolicVolumeTranscendence.lean",
    validation: "not_checked",
  },
});
