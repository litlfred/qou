import { proposition } from "../../schema/builders";

/**
 * LP stability criterion for atoms.
 */
export default proposition({
  label: "prop:atomic-lp-stability",
  lean: { ref: "qou:QOU.ParticleInteractions.atomic_lp_stability", validation: "not_checked" },
  title: "LP stability of the atomic braid",
  uses: ["def:atomic-braid"],
});
