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
  lean: {
    decl: "QOU.ParticleInteractions.frobenius_positivity_filter",
    file: "QOU/ParticleInteractions.lean",
    validation: "not_checked",
  },
  uses: [
    "prop:confinement-lp",
    "thm:parity-regime-selection",
  ],
});
