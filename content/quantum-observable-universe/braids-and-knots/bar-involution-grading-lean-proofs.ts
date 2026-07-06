import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bar-involution-grading-lean-proofs",
  interprets: "def:bar-involution",
  title: "The $\\mathbb{Z}/2\\mathbb{Z}$ bar-grading: Lean $\\leftrightarrow$ paper proof bridge",
  uses: [
    "def:bar-involution",
  ],
  tags: [
    "lean-infrastructure",
    "bar-invariance",
    "bar-grading",
    "categorical-action",
  ],
});
