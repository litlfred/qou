import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-factor-frobenius-pairing",
  title:
    "Knot factor as Frobenius self-pairing ratio",
  lean: {
    decl: "QOU.BraidKnot.KnotFactorFrobeniusPairing",
    validation: "not_checked",
  },
  uses: [
    "prop:nuclear-knot-classification",
    "prop:fibre-functor-rigidity",
    "prop:bw-coefficient-shadow-price",
    "def:adjoint-trace",
    "def:q-heat-equation",
    "rem:base-field-independence",
  ],
  tags: [
    "frobenius-pairing",
    "self-duality",
    "knot-factor",
    "rigid-monoidal",
    "categorical-binding",
    "reciprocity",
  ],
});
