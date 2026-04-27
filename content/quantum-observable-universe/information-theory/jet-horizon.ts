import { definition } from "../../schema/builders";

export default definition({
  label: "def:jet-horizon",
  title: "Jet horizon (degree-$0$ vanishing locus)",
  tags: [
    "jet-horizon", "event-horizon", "degree-zero",
    "vanishing-ideal", "information-barrier",
  ],
  lean: { ref: "qou:QOU.JetHorizon",
    validation: "not_checked",
  },
  uses: ["rem:jet-planck-steps"],
});
