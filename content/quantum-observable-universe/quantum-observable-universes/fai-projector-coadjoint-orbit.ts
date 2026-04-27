import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:fai-projector-coadjoint-orbit",
  lean: { ref: "qou:QOU.QuantumObservableUniverse.fai_projector_coadjoint_orbit",
    validation: "not_checked",
  },
  title: "Rank-1 projectors embed $\\mathbb{P}(V)$ as a coadjoint orbit in $\\mathrm{Ad}(A)$",
  tags: ["rank-one-projector", "coadjoint-orbit", "involution", "categorical-trace"],
  uses: ["def:involutive-structure"],
  proofs: ["prf:fai-projector-coadjoint-orbit"],
});
