import { example } from "../../schema/builders";

export default example({
  label: "ex:single-magic-O18-diagram",
  title:
    "Single-magic illustration: $^{18}\\mathrm{O}$ at $Z = 8$, $N = 10$",
  interprets: "conj:diagrammatic-double-magic-lr-fusion",
  uses: [
    "conj:diagrammatic-double-magic-lr-fusion",
    "conj:categorical-neutrality-saturated-shells",
    "prop:magic-numbers-from-q",
  ],
  tags: [
    "magic-numbers",
    "single-magic",
    "oxygen-18",
    "self-conjugate-partitions",
    "kappa-leakage",
    "diagram",
  ],
});
