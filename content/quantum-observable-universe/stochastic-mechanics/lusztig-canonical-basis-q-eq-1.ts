import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:lusztig-canonical-basis-q-eq-1",
  title:
    "Lusztig canonical basis at $q = 1$ — decategorification of Kashiwara crystal via Kazhdan–Lusztig polynomials",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.LusztigCanonicalBasisQEq1",
    validation: "not_checked",
  },
  uses: [
    "conj:reverse-limit-q-to-infinity",
    "conj:kazhdan-lusztig-classical-limit",
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
