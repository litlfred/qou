import { definition } from "../../schema/builders";

export default definition({
  label: "def:demand-profile",
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation (moved from the definition prose 2026-11-19): What follows invokes real- or complex-analytic constructs. Categorical identities remain valid over an abstract coefficient ring; their archimedean realisation is specialised here." },
  ],
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
