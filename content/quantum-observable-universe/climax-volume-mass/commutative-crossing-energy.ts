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
  ],
  uses: [
    "rem:sqrt-q-ribbon-structure",
    "rem:archimedean-realisations",
    "prop:categorical-coordinate-ring",
  ],
  interprets: "def:crossing-energy",
});
