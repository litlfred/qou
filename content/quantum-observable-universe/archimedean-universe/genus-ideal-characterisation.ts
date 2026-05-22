import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:genus-ideal-characterisation",
  lean: { ref: "qou:QOU.Descartes.genus_ideal_characterisation",
    validation: "not_checked",
  },
  title: "Genus-filtration ideal in Hecke coordinates",
  tags: ["seifert-surface", "ideal", "hecke-coordinates", "truncation"],
  uses: ["lem:genus-from-hecke-completeness", "lem:chebyshev-degree-genus"],
  proofs: ["prf:genus-ideal-characterisation"],
});
