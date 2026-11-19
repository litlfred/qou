import { proposition } from "../../schema/builders";

/**
 * The provable core of the jet-filtration binding: it is EXTENSIVE — a finite
 * sum of non-negative body-order terms, hence monotone (and strictly increasing
 * when a body-order contributes positively) in the body-order cutoff A. This is
 * the property the intensive rotation-phase θ_λ route structurally lacked.
 * Lean sorry-free (QOU.Mass.jetBinding_mono / jetBinding_lt_succ).
 */
export default proposition({
  label: "prop:jet-filtration-binding-extensive",
  title: "The jet-filtration binding is extensive (monotone in body order)",
  lean: {
    ref: "qou:QOU.Mass.jetBinding_mono",
    validation: "not_checked",
  },
  uses: ["conj:binding-manybody-eq-jet-filtration"],
  tags: [
    "binding",
    "jet-filtration",
    "extensive",
    "na-stokes",
    "reeb",
    "body-order",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c): stated over R; combinatorial content is a finite non-negative sum. Rotation-phase non-closure recorded in computations/probe_full_theta_binding.py.",
    },
  ],
});
