import { remark } from "../../schema/builders";

export default remark({
  label: "rem:commutative-crossing-energy",
  title:
    "Categorical coordinate of the commutative limit: " +
    "$i$ as $\\sqrt{\\lambda_-}$ and the $\\mathbb{Z}_2 \\hookrightarrow " +
    "\\mathrm{U}(1) \\hookrightarrow \\mathrm{U}_q(1)$ hierarchy",
  tags: [
    "categorical-coordinate",
    "crossing-energy",
    "commutative-limit",
    "complex-structure",
    "u1",
    "phase-tube",
    "branch-phase",
    "isospin",
    "mass-tower",
  ],
  uses: [
    "def:crossing-energy",
    "def:commutative-qou",
    "prop:u1-equivariant-reduction",
    "rem:u1-phase-tube",
    "def:hyperelliptic-quintic",
    "def:exceptional-divisor",
  ],
  interprets: "def:crossing-energy",
});
