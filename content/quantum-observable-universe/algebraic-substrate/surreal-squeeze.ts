import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:surreal-squeeze",
  title:
    "Surreal squeeze: standard-scale cost dominates infinitesimal dissipation",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.surreal_squeeze",
    validation: "not_checked",
  },
  uses: [
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "prop:surreal-rate-calculus",
    "rem:conway-normal-form",
    "def:surreal-blowup-calculus",
    "rem:rh-surreal-bound",
    "rem:ns-surreal-bound",
    "rem:collatz-surreal-bound",
    "rem:p-vs-np-surreal-bound",
    "rem:millennium-unification",
  ],
  tags: [
    "surreal",
    "squeeze",
    "error-bounds",
    "millennium-problem",
    "classical-limit",
  ],
});
