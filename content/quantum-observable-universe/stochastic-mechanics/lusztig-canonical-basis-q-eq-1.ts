import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lusztig-canonical-basis-q-eq-1",
  title:
    "Lusztig canonical basis at $q = 1$ — decategorification of Kashiwara crystal via Kazhdan–Lusztig polynomials",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.LusztigCanonicalBasisQEqOne",
    validation: "not_checked",
  },
  uses: [
    "prop:reverse-limit-q-to-infinity",
    "prop:kazhdan-lusztig-classical-limit",
  ],
  cites: [
    "kazhdan-lusztig1979",
    "lusztig1990",
    "kashiwara1991",
  ],
  tags: [
    "lusztig-canonical-basis",
    "duality-d24",
    "kazhdan-lusztig",
    "classical-limit",
    "decategorification",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "non-scholarly-voice-exception",
  ],
});
