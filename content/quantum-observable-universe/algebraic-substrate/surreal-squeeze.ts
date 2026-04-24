import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:surreal-squeeze",
  title:
    "Surreal squeeze: standard-scale cost dominates infinitesimal dissipation",
  lean: {
    decl: "QOU.AlgebraicSubstrate.surreal_squeeze",
    file: "lean/QOU/AlgebraicSubstrate/SurrealSqueeze.lean",
    validation: "not_checked",
  },
  uses: ["prop:surreal-rate-calculus"],
  tags: [
    "surreal",
    "squeeze",
    "error-bounds",
    "millennium-problem",
    "classical-limit",
  ],
});
