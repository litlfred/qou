import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:surreal-squeeze",
  title:
    "Surreal squeeze: standard-scale cost dominates infinitesimal dissipation",
  lean: {
    decl: "QOU.AlgebraicSubstrate.surreal_squeeze",
    validation: "not_checked",
  },
  uses: [
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "prop:surreal-rate-calculus",
    "rem:big-o-surreal",
    "def:surreal-blowup-calculus",
  ],
  tags: [
    "surreal",
    "squeeze",
    "error-bounds",
    "millennium-problem",
    "classical-limit",
  ],
});
