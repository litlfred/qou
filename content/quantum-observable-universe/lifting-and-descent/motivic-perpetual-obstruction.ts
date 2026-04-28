import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:motivic-perpetual-obstruction",
  title:
    "Motivic perpetual obstruction: $\\chi^{\\mathrm{mot}}_A$ is non-trivial at almost every finite place when $\\chi(A) \\neq 0$",
  tags: [
    "motivic-galois",
    "perpetuity",
    "yekutieli",
    "kummer-tower",
    "frobenius",
  ],
  uses: [
    "def:motivic-galois-character",
    "rem:kummer-tower",
    "thm:qu-to-qou",
  ],
  cites: ["yekutieli2010"],
  lean: {
    ref: "qou:QOU.LiftingDescent.motivic_perpetual_obstruction",
    validation: "not_checked",
  },
});
