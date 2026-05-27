import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:vhat-pair-commutation-trace",
  title:
    "Pair commutation at the traced-volume level: $\\hat V_i \\hat V_j = \\hat V_j \\hat V_i$ in $\\mathbb{Z}[q^{\\pm 1/2}, z]$",
  lean: {
    ref: "qou:QOU.BraidKnot.VhatPairCommutationTrace",
    validation: "not_checked",
  },
  cites: [
    "kassel1995",
    "geckpfeiffer2000",
  ],
  tags: [
    "v-hat",
    "pentagon",
    "commutation",
    "markov-trace",
    "jet-tower",
    "narrative-replacement",
  ],
});
