import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:strangelet-double-beta",
  label: "rem:strangelet-double-beta-interpretation",
  title:
    "Skein/EM-strong ratio, intermediate $4_1$ state, and observable double-beta signature",
  uses: [
    "prop:strangelet-double-beta",
    "prop:crossing-energy-decomposition",
    "rem:building-block-knots",
  ],
  tags: [
    "strangelet",
    "double-beta-decay",
    "skein-amplitude",
    "electromagnetic-signature",
    "falsifiability",
    "interpretation",
  ],
});
