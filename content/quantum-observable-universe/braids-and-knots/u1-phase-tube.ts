import { remark } from "../../schema/builders";

export default remark({
  label: "rem:u1-phase-tube",
  title: "Physical interpretation: the single $\\mathrm{U}(1)$ phase tube",
  tags: ["u1", "phase-tube", "color-tube", "commutative-limit", "interpretation"],
  uses: [
    "prop:u1-equivariant-reduction",
    "def:hyperelliptic-quintic",
  ],
  interprets: "prop:u1-equivariant-reduction",
});
