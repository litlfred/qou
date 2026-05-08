import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:demand-stability",
  lean: { ref: "qou:QOU.ParticleInteractions.demand_stability", validation: "not_started" },
  title: "Demand profile determines nuclear and atomic stability",
  tags: [
    "stability",
    "demand",
    "normal-form",
    "beta-decay",
    "shell-closure",
    "magic-numbers",
  ],
  uses: ["def:derived-atom"],
});
