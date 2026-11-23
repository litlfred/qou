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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): a rule fixing the word, not just its crossing content.\n`the_nuclear_jet_level_is_the_retired_all_pairs_object_probe.py`." },
  ],
});
