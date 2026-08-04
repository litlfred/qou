import { remark } from "../../schema/builders";

/**
 * Derived properties of the stable-atom ILP condition: pointwise
 * (fixed-$q$) independence of neighborhood, the strict-strengthening
 * relation to the LP relaxation, and the confinement-filtration scope.
 */
export default remark({
  label: "rem:stable-atom-properties",
  title: "Properties of ILP stability",
  interprets: "def:stable-atom",
  uses: [
    "def:stable-atom",
    "def:confinement-level",
    "prop:mass-endomorphism-tower",
  ],
  tags: [
    "stability",
    "ilp",
    "lp-dual",
    "frobenius-positivity",
    "confinement",
  ],
});
