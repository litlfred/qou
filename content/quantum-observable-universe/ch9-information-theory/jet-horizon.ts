import { definition } from "../../schema/builders";

export default definition({
  label: "def:jet-horizon",
  title: "Jet horizon (degree-$0$ vanishing locus)",
  tags: [
    "jet-horizon", "event-horizon", "degree-zero",
    "vanishing-ideal", "information-barrier",
  ],
  lean: {
    decl: "QOU.JetHorizon",
    validation: "not_checked",
  },
  uses: [
    "prop:jet-prolongation",
    "def:bundle-initial-conditions",
    "def:exceptional-divisor",
    "rem:jet-planck-steps",
  ],
});
