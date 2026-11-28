import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-mordell-weil",
  lean: {
    ref: "qou:QOU.Observations.AppendixSurreals.CategoricalMordellWeil",
    validation: "not_checked",
  },
  title:
    "Invariant Hom-group, finite-place Euler product, and monoidal localisation kernel",
  uses: [
    "conj:tannaka-krein-isomorphism",
    "prop:descartes-elliptic-curve",
    "def:local-q-zeta-function",
  ],
  tags: [
    "elliptic-curve",
    "l-function",
    "hom-group",
    "localisation-kernel",
    "categorical",
    "fibre-functor",
  ],
  cites: ["tate1974"],
});
