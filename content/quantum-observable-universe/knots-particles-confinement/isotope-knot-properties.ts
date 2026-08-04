import { remark } from "../../schema/builders";

/**
 * Derived properties of the isotope-knot relation: distinct Jones
 * polynomials (knot-distinctness) and per-isotope independence of
 * ILP stability.
 */
export default remark({
  label: "rem:isotope-knot-properties",
  title: "Isotopes are knot-distinct with independent stability",
  interprets: "def:isotope-knot",
  uses: ["def:isotope-knot", "def:unstable-atom"],
  tags: [
    "isotope",
    "knot",
    "jones-polynomial",
    "stability",
    "categorical",
  ],
});
