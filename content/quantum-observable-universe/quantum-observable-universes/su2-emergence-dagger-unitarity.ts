import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:su2-emergence-dagger-unitarity",
  lean: { ref: "qou:QOU.su2_emergence_dagger_unitarity",
    validation: "not_checked",
  },
  title: "Frobenius dagger forces $G \\subseteq \\mathrm{U}(2)$",
  tags: ["frobenius", "dagger", "unitarity", "u2"],
  uses: ["thm:su2-emergence", "prop:fiber-adjoint-involution", "prop:positive-definite-dagger"],
  proofs: ["prf:su2-emergence-dagger-unitarity"],
});
