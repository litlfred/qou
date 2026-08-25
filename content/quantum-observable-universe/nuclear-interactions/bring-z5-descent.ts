import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bring-z5-descent",
  title: "Descent of $\\mathbb{Z}_5 \\subset S_5$ from Bring to $\\mathcal{X}_5$",
  tags: ["descent", "sylow", "bring", "z5", "hyperelliptic"],
  uses: ["prop:x5-z5-automorphism"],
  interprets: "prop:x5-z5-automorphism",
  cites: ["edge1978"],
});
