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
    "completeness",
  ],
  lean: { ref: "qou:QOU.Descartes.genus_filtration_ideal",
    validation: "not_checked",
  },
  uses: [
    "prop:cohomological-embedding",
    "prop:categorical-dq-squared",
  ],
  cites: ["yekutieli2010"],
  proofs: ["prf:genus-filtration-ideal"],
});
