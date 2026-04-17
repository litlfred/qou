import { definition } from "../../schema/builders";

export default definition({
  label: "def:confinement-level",
  title: "Confinement level via shadow-price filtration",
  lean: {
    decl: "QOU.BraidKnot.ConfinementLevel",
    validation: "not_checked",
  },
  uses: [
    "def:knot-operator-energy",
    "def:hecke-normal-form",
    "prop:bw-coefficient-shadow-price",
  ],
  cites: [],
  tags: [
    "confinement",
    "filtration",
    "shadow-price",
    "subalgebra",
    "knot-operator",
  ],
});
