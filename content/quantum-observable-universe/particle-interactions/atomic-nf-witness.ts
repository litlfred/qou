import { proposition } from "../../schema/builders";

/**
 * Each atom's construction produces a verified NF element.
 */
export default proposition({
  label: "prop:atomic-nf-witness",
  lean: { ref: "qou:QOU.ParticleInteractions.atomic_nf_witness", validation: "not_started" },
  title: "Atomic braid normal form witness",
  uses: ["def:atomic-braid"],
});
