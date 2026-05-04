import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:tower-pair-equality-fixed-level",
  title:
    "Pair-contribution equality at a fixed jet level: $z^2 \\sum_{(i,j) \\in \\mathcal{P}_n} \\Phi_q(|\\hat V_i^{(n)} \\hat V_j^{(n)}|)$ is an exact identity",
  lean: {
    ref: "qou:QOU.BraidKnot.TowerPairEqualityFixedLevel",
    validation: "not_checked",
  },
  uses: [
    "prop:markov-pair-z2",
    "lem:vhat-pair-commutation-trace",
    "thm:markov-trace-factorization",
    "def:algebraic-quantum-volume",
  ],
  cites: [
    "kassel1995",
    "geckpfeiffer2000",
  ],
  tags: [
    "pair-contribution",
    "markov-trace",
    "jet-tower",
    "sharpness",
    "equality",
    "narrative-replacement",
  ],
});
