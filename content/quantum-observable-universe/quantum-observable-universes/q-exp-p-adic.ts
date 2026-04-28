import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-exponential",
  label: "rem:q-exp-p-adic",
  title: "$p$-adic realisations of $\\exp_q$ ($\\mathbb{Q}_p$ and $\\mathbb{C}_p$)",
  tags: ["q-exponential", "p-adic", "witt-vectors", "c-p", "convergence"],
  uses: ["rem:q-exp-finite-field-obstruction"],
});
