import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:brings-euler-characteristic",
  lean: { ref: "qou:QOU.DescartesUniverse.brings_euler_characteristic",
    validation: "not_checked",
  },
  title: "Categorical Euler characteristic of $\\mathcal{O}_q(\\mathrm{SU}(2))$ on Bring's surface",
  tags: ["euler-characteristic", "brings-surface", "categorical-trace", "descartes-substrate"],
  uses: ["prop:euler-char-stability"],
  proofs: ["prf:brings-euler-characteristic"],
});
