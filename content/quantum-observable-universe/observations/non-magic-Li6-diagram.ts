import { example } from "../../schema/builders";

export default example({
  label: "ex:non-magic-Li6-diagram",
  title:
    "Non-magic illustration: $^{6}\\mathrm{Li}$ at $Z = N = 3$ (frayed both sides)",
  interprets: "conj:diagrammatic-double-magic-lr-fusion",
  uses: [
    "conj:diagrammatic-double-magic-lr-fusion",
    "conj:categorical-neutrality-saturated-shells",
    "prop:magic-numbers-from-q",
  ],
  tags: [
    "magic-numbers",
    "non-magic",
    "lithium-6",
    "frayed-blocks",
    "full-twist-flux",
    "diagram",
  ],
});
