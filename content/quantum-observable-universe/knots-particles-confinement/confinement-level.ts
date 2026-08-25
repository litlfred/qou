import { definition } from "../../schema/builders";

export default definition({
  label: "def:confinement-level",
  title: "Confinement level via shadow-price filtration",
  lean: { ref: "qou:QOU.BraidKnot.ConfinementLevel",
    validation: "not_checked",
  },
  uses: [],
  cites: [],
  tags: [
    "confinement",
    "filtration",
    "shadow-price",
    "subalgebra",
    "knot-operator",
  ],
});
