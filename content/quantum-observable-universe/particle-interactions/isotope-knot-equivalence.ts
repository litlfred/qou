import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:isotope-knot-equivalence",
  proofs: ["prf:isotope-knot-equivalence"],
  title: "Isotope relation is an equivalence",
  lean: { ref: "qou:QOU.BraidKnot.IsotopeKnot.equivalence",
    validation: "not_checked",
  },
  uses: ["def:isotope-knot"],
  tags: ["equivalence-relation", "isotope", "atom-knot"],
});
