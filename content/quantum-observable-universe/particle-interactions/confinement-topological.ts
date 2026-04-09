import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-topological",
  title: "Confinement is topological (LP proof)",
  tags: [
    "confinement",
    "topological",
    "linear-programming",
    "gram-matrix",
    "negative-eigenvalue",
    "borromean",
  ],
  lean: {
    decl: "QOU.Interactions.confinementTopological",
    validation: "not_checked",
  },
  uses: [
    "prop:confinement-lp",
    "prop:frobenius-gram-matrix",
    "prop:confinement-operator-selection",
  ],
});
