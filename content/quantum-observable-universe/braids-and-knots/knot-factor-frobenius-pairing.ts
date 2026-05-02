import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:knot-factor-frobenius-pairing",
  title:
    "Knot factor as Frobenius self-pairing ratio",
  lean: { ref: "qou:QOU.BraidKnot.KnotFactorFrobeniusPairing",
    validation: "not_checked",
  },
  uses: [
    "prop:nuclear-knot-classification",
    "rem:fibre-functor-rigidity",
    "prop:bw-coefficient-shadow-price",
    "def:q-casimir",
    "rem:adjoint-trace",
    "def:q-heat-equation",
      ],
  cites: ["yekutieli2015", "kassel1995"],
  tags: [
    "frobenius-pairing",
    "self-duality",
    "knot-factor",
    "rigid-monoidal",
    "categorical-binding",
    "reciprocity",
  ],
});
