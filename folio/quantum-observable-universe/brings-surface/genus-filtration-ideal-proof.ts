import { proof } from "../../schema/builders";

export default proof({
  label: "prf:genus-filtration-ideal",
  title: "Proof of genus-filtration ideal characterisation",
  of: "prop:genus-filtration-ideal",
  tags: ["chebyshev", "yekutieli", "hecke-algebra", "ideal"],
  uses: [
    "prop:genus-filtration-ideal",
    "lem:yekutieli-leading-coefficient",
  ],
});
