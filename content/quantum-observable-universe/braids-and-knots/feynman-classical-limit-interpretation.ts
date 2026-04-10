import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:feynman-classical-limit",
  label: "rem:feynman-classical-limit-interpretation",
  lean: {
    decl: "QOU.FeynmanPathIntegrals.jones_polynomial_at_one",
    validation: "not_checked",
  },
  title: "Classical limit and the symmetric degeneration",
  tags: ["path-integral", "classical-limit", "symmetric-group", "specht-module"],
  uses: [
    "prop:feynman-classical-limit",
    "prop:topological-mass-formula",
  ],
});
