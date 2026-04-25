import { definition } from "../../schema/builders";

export default definition({
  label: "def:spatial-realization-functor",
  lean: { ref: "qou:QOU.SpatialRealizationFunctor",
    validation: "not_checked",
  },
  title: "Spatial realization functor",
  tags: ["spectrum", "functor", "contact-geometry"],
  uses: [
    "def:categorical-point",
    "def:frobenius-pairing",
    "def:categorical-reeb",
  ],
});
