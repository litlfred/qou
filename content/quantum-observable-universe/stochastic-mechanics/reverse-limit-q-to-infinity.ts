import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reverse-limit-q-to-infinity",
  title:
    "Reverse limit $q \\to \\infty$ — symmetric counterpart of Kashiwara crystal $q \\to 0$ via bar involution",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.ReverseLimitQToInfinity",
    validation: "not_checked",
  },
  uses: [
    "def:bar-involution",
    "prop:crystal-isospin-degeneracy",
  ],
  cites: [
    "kashiwara1991",
    "lusztig1990",
  ],
  tags: [
    "reverse-limit",
    "q-to-infinity",
    "duality-d13",
    "kashiwara-paired",
    "bar-paired",
    "axiom-class",
    "open-problem",
    "non-scholarly-voice-exception",
  ],
});
