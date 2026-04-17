import { definition } from "../../schema/builders";

export default definition({
  label: "def:atom-knot",
  title: "Atom as a knot via Gröbner normal form",
  lean: {
    decl: "QOU.BraidKnot.AtomKnot",
    validation: "not_checked",
  },
  uses: [
    "def:hecke-normal-form",
    "def:atomic-braid",
    "def:confinement-level",
  ],
  cites: [],
  tags: [
    "atom",
    "knot",
    "groebner-normal-form",
    "block-decomposition",
    "categorical",
  ],
});
