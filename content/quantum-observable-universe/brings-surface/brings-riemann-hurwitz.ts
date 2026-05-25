import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:brings-riemann-hurwitz",
  lean: { ref: "qou:QOU.ArchimedeanUniverse.brings_riemann_hurwitz",
    validation: "not_checked",
  },
  title: "Riemann--Hurwitz count for the canonical map $\\Sigma_4 \\to \\mathbb{P}(V)$",
  tags: ["riemann-hurwitz", "ramification", "brings-surface", "s5-symmetry"],
  uses: [],
  proofs: ["prf:brings-riemann-hurwitz"],
});
