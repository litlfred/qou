import { definition } from "../../schema/builders";

export default definition({
  label: "def:spatial-realization-functor",
  lean: {
    decl: "QOU.SpatialRealizationFunctor",
    validation: "not_checked",
  },
  title: "Spatial realization functor",
  tags: ["spectrum", "functor", "contact-geometry"],
  uses: [
    "def:categorical-point",
    "def:frobenius-pairing",
    "def:categorical-reeb",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/spatial-realization-functor-0.svg", blockIndex: 0, hash: "f19d96f655ad" },
  ],

});
