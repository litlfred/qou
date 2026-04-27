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
    "prop:yekutieli-lifting",
  ],
  lean: { ref: "qou:QOU.Descartes.CSEvaluationFaithful",
    validation: "not_checked",
  },
});
