import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:jet-filtered-knot-factor",
  title:
    "Jet-filtered knot factor: per-level character convergence and nuclear quotient braid",
  lean: { ref: "qou:QOU.BraidKnot.jet_filtered_knot_factor",
    validation: "not_checked",
  },
  uses: [
    "prop:confined-knot-binding",
    "prop:hook-weight-derivation",
  ],
  tags: [
    "knot-factor",
    "jet-filtration",
    "character-convergence",
    "nuclear-quotient-braid",
    "open-problem",
  ],
});
