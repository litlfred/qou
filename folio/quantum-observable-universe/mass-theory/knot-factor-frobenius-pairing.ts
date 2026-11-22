import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:knot-factor-frobenius-pairing",
  title:
    "Knot factor as Frobenius self-pairing ratio",
  lean: { ref: "qou:QOU.BraidKnot.KnotFactorFrobeniusPairing",
    validation: "not_checked",
  },
  uses: [
    "conj:nuclear-knot-classification",
    "rem:fibre-functor-rigidity",
    "conj:confinement-frobenius-reciprocity",
    "def:q-casimir",
    "rem:adjoint-trace",
    "def:q-heat-equation",
      ],
  cites: ["yekutieli2015", "kassel1995"],
  tags: [
    "tier:keystone",
    "frobenius-pairing",
    "self-duality",
    "knot-factor",
    "rigid-monoidal",
    "categorical-binding",
    "reciprocity",
  ],
});
