import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:positron-correction",
  title:
    "Parity-dependent Q-value offset",
  tags: [
    "positron",
    "correction",
    "pair-production",
    "action-difference",
    "parity",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.positron_correction",
    validation: "not_checked",
  },
  uses: ["thm:parity-regime-selection"],
  probe: "audit/positron-correction-probe",
  consumers: [],
});
