import { example } from "../../schema/builders";

export default example({
  label: "ex:single-magic-O18-diagram",
  title:
    "Single-magic illustration: $^{18}\\mathrm{O}$ at $Z = 8$, $N = 10$",
  interprets: "prop:diagrammatic-double-magic-lr-fusion",
  uses: [
    "prop:diagrammatic-double-magic-lr-fusion",
    "prop:categorical-neutrality-saturated-shells",
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
