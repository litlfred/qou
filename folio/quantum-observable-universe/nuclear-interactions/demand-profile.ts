import { definition } from "../../schema/builders";

export default definition({
  label: "def:demand-profile",
  lean: { ref: "qou:QOU.ParticleInteractions.demandProfile", validation: "not_checked" },
  title: "Demand profile of a derived atom",
  tags: [
    "demand",
    "normal-form",
    "stability",
    "derived-atom",
  ],
  uses: ["def:derived-atom"],
});
