import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:genus-from-hecke-completeness",
  lean: { ref: "qou:QOU.Descartes.genus_from_hecke_completeness",
    validation: "not_checked",
  },
  title: "Genus from Hecke completeness for torus knots",
  tags: ["torus-knot", "hecke-algebra", "completeness", "genus"],
  uses: ["prop:cohomological-embedding"],
  proofs: ["prf:genus-from-hecke-completeness"],
});
