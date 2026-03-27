import { definition } from "../../schema/builders";

export default definition({
  label: "def:transfer-matrix-operator",
  title:
    "Transfer matrix operator on hadrons and Gröbner ideals",
  tags: [
    "transfer-matrix",
    "operator",
    "hecke-algebra",
    "groebner",
    "hadron",
    "knot",
    "crossing",
    "universal",
    "interaction",
  ],
  lean: {
    decl: "QOU.Descartes.TransferMatrixOperator",
    validation: "not_checked",
  },
  uses: [
    "prop:skein-polynomial-transfer-matrix",
    "prop:beta-decay-transfer-matrix",
    "prop:generator-volume-decomposition",
    "def:crossing-energy",
    "rem:building-block-knots",
    "def:hadron",
  ],
});
