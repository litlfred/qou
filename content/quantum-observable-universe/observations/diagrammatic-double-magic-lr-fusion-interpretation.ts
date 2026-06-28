import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:diagrammatic-double-magic-lr-fusion",
  label: "rem:diagrammatic-double-magic-lr-fusion-interpretation",
  title:
    "Double-magic rigidity: empirical signature, examples, and the higher-magic ladder",
  uses: [
    "prop:diagrammatic-double-magic-lr-fusion",
    "ex:single-magic-O18-diagram",
    "ex:double-magic-Ca40-diagram",
    "ex:non-magic-Li6-diagram",
  ],
  cites: ["ariki1996"],
  tags: [
    "magic-numbers",
    "double-magic",
    "LR-fusion",
    "shell-closure",
    "interpretation",
  ],
});
