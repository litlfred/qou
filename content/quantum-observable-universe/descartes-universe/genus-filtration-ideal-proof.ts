import { proof } from "../../schema/builders";

export default proof({
  label: "prf:genus-filtration-ideal",
  title: "Proof of genus-filtration ideal characterisation",
  of: "prop:genus-filtration-ideal",
  tags: ["chebyshev", "yekutieli", "hecke-algebra", "ideal"],
  uses: [
    "prop:categorical-dq-squared",
    "def:quantum-characteristic-classes",
    "lem:genus-from-hecke-completeness",
    "lem:chebyshev-degree-genus",
    "lem:genus-ideal-characterisation",
    "lem:yekutieli-leading-coefficient",
  ],
});
