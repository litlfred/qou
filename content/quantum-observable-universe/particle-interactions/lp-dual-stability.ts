import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lp-dual-stability",
  title:
    "LP dual stability: confined hadrons have bounded shadow prices",
  tags: [
    "lp-duality",
    "stability",
    "confinement",
    "frobenius",
    "gram-matrix",
    "shadow-price",
    "hadron",
    "quark",
  ],
  uses: [
    "prop:confinement-lp",
    "prop:frobenius-gram-matrix",
    "prop:confinement-topological",
    "rem:confinement-nucleon-unit",
  ],
});
