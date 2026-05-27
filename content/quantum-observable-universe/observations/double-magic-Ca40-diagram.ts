import { example } from "../../schema/builders";

export default example({
  label: "ex:double-magic-Ca40-diagram",
  title:
    "Double-magic illustration: $^{40}\\mathrm{Ca}$ at $Z = N = 20$ (LR fusion rigid)",
  interprets: "prop:diagrammatic-double-magic-lr-fusion",
  uses: [
    "prop:diagrammatic-double-magic-lr-fusion",
    "prop:categorical-neutrality-saturated-shells",
    "prop:magic-numbers-from-q",
  ],
  tags: [
    "magic-numbers",
    "double-magic",
    "calcium-40",
    "self-conjugate-partitions",
    "lr-fusion-rigidity",
    "diagram",
  ],
  cites: [
    "geckpfeiffer2000",
  ],
});
