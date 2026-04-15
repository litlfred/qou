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
  rendered: [
    { mime: "image/svg+xml", url: "rendered/gram-weighted-qvalue-0.svg", blockIndex: 0, hash: "52367309cc22" },
    { mime: "image/svg+xml", url: "rendered/gram-weighted-qvalue-1.svg", blockIndex: 1, hash: "40e60ce79281" },
    { mime: "image/svg+xml", url: "rendered/gram-weighted-qvalue-2.svg", blockIndex: 2, hash: "367b6ac8e0a7" },
    { mime: "image/svg+xml", url: "rendered/gram-weighted-qvalue-3.svg", blockIndex: 3, hash: "055666c30e97" },
  ],

});
