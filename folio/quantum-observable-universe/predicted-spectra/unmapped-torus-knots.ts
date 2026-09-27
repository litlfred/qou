import { remark } from "../../schema/builders";

export default remark({
  label: "rem:unmapped-torus-knots",
  title: "Unmapped genus-$4$ torus knot generators",
  interprets: "prop:torus-embeddable-complete",
  tags: [
    "torus-knot",
    "genus-4",
    "saturating",
    "unmapped",
    "strong-force",
    "weak-force",
  ],
  uses: [
    "prop:torus-embeddable-complete",
    "rem:knot-formula-table",
  ],
});
