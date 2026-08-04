import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gram-weight-eigenstructure",
  title:
    "Eigenstructure of the Gram weight and the adjoint character",
  tags: [
    "gram-matrix",
    "eigenvalue",
    "frobenius-norm",
    "adjoint-character",
    "wedderburn",
    "jucys-murphy",
  ],
  interprets: "prop:gram-weighted-qvalue",
  uses: ["prop:gram-weighted-qvalue"],
});
