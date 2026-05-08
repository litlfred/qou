import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:yekutieli-leading-coefficient",
  lean: { ref: "qou:QOU.Descartes.yekutieli_leading_coefficient",
    validation: "not_checked",
  },
  title: "Yekutieli obstruction equals the leading Chebyshev coefficient",
  tags: ["yekutieli", "obstruction", "chebyshev", "categorical-dq-squared"],
  uses: [
    "prop:categorical-dq-squared",
    "lem:genus-ideal-characterisation",
  ],
  proofs: ["prf:yekutieli-leading-coefficient"],
});
