import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:hyperelliptic-z5-classification",
  label: "rem:hyperelliptic-z5-classification-interpretation",
  title: "Fixed-point symmetry, tight minimality, and the abstract $\\mathbb{Z}_5$",
  tags: ["hyperelliptic", "z5", "minimal-genus", "bring", "branch-divisor"],
  uses: [
    "thm:hyperelliptic-z5-classification",
    "rem:bring-z5-descent",
  ],
});
