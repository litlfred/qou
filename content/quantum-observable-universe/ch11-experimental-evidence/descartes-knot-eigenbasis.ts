import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:descartes-knot-eigenbasis",
  lean: {
    decl: "QOU.Descartes.descartes_knot_eigenbasis",
    validation: "not_checked",
  },
  title: "Knot eigenbasis completeness for a Descartes universe",
  tags: ["descartes-universe", "knot-invariant", "hecke-algebra", "schur-weyl"],
  uses: [
    "def:descartes-condition",
    "cor:descartes-braid-structure",
    "prop:braid-action-tensor",
    "prop:knot-eigenbasis-complete",
    "def:quantum-su2",
    "rem:r-matrix-braiding",
  ],
});
