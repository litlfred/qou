import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:positron-correction",
  title:
    "Positron correction to the Q-value",
  tags: [
    "positron",
    "correction",
    "pair-production",
    "action-difference",
  ],
  lean: {
    decl: "QOU.ParticleInteractions.positron_correction",
    validation: "not_checked",
  },
  uses: [
    "thm:parity-regime-selection",
    "def:breit-wheeler-pair-production",
  ],
});
