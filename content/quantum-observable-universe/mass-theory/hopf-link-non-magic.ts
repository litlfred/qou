import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hopf-link-non-magic",
  title:
    "Hopf link as the canonical non-magic knot operator (lowest cohomological degree)",
  interprets: "prop:knot-operator-selection",
  uses: ["prop:torus-knot-shell-binding"],
  tags: [
    "hopf-link",
    "knot-operator",
    "cohomology",
    "non-magic",
    "torus-knot",
    "spectral-sequence",
  ],
});
