import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gram-weighted-qvalue",
  title:
    "Gram-weighted $\\mathcal{Q}_q$-value from Frobenius norm of conversion channels",
  tags: [
    "q-value",
    "gram-matrix",
    "frobenius-norm",
    "beta-decay",
    "garside-element",
    "hecke-algebra",
    "adjoint-character",
  ],
  lean: {
    decl: "QOU.Descartes.gram_weighted_qvalue",
    validation: "not_checked",
  },
  uses: [
    "def:typed-garside-element",
    "prop:frobenius-gram-matrix",
    "prop:nuclear-groebner-reduction",
    "def:transfer-matrix-operator",
  ],
});
