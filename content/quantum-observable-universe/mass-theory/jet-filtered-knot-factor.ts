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
    "tier:S",
    "knot-factor",
    "jet-filtration",
    "character-convergence",
    "nuclear-quotient-braid",
    "open-problem",
  ],
  computation: {
    engine: "python",
    script: "computations/nf_transition_lifting.py",
    witness: "computations/nf-transition-lifting.witness.json",
    status: "experimental",
  },
});
