import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:genus-filtration-ideal",
  title:
    "Genus-filtration ideal and the Chebyshev obstruction for $T_{2,p}$",
  tags: [
    "torus-knot",
    "ideal",
    "chebyshev",
    "yekutieli",
    "obstruction",
    "genus",
    "hecke-algebra",
    "continued-fraction",
  ],
  lean: {
    decl: "QOU.Descartes.genus_filtration_ideal",
    validation: "not_checked",
  },
  uses: [
    "thm:embeddability-closure",
    "def:yekutieli-lifting-condition",
    "prop:cohomological-embedding",
  ],
  cites: ["yekutieli2010"],
  proofs: ["prf:genus-filtration-ideal"],
});
