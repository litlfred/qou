import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:knot-particle-generation",
  label: "rem:knot-particle-generation-interpretation",
  title: "Hopf linking, color-tube threading, and Skein crossing change operations",
  tags: [
    "knot",
    "particle",
    "hopf-link",
    "color-tube",
    "skein",
    "exceptional-divisor",
    "operation",
  ],
  uses: [
    "def:knot-particle-generation",
    "prop:skein-generation",
    "rem:color-tube-interpretation",
  ],
});
