import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-positivity-filter",
  title:
    "Frobenius positivity filter for even-$A$ decays",
  tags: [
    "frobenius",
    "positivity",
    "filter",
    "even-A",
    "config-exclusion",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.frobenius_positivity_filter",
    validation: "not_checked",
  },
  uses: ["thm:parity-regime-selection"],
});
