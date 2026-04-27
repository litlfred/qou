import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-transient-localisation",
  lean: { ref: "qou:QOU.LiftingDescent.tm_transient_localisation",
    validation: "not_checked",
  },
  title: "Transient terms localise to exceptional divisors",
  tags: ["transient", "exceptional-divisor", "blow-up", "central-extension"],
  uses: [
    "def:brane-boundary",
    "lem:topological-mass-eigenspace-decomp",
  ],
  proofs: ["prf:topological-mass-transient-localisation"],
});
