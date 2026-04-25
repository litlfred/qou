import { definition } from "../../schema/builders";

export default definition({
  label: "def:crossing-energy",
  title: "Crossing energy of a knot composite",
  tags: ["crossing", "energy", "skein", "r-matrix", "stability"],
  lean: { ref: "qou:QOU.Braiding.CrossingEnergy",
    validation: "not_checked",
  },
  uses: [
    "rem:r-matrix-braiding",
    "def:substrate-parameter",
    "def:quantum-observable-universe",
    "prop:braiding-eigenvalue-extraction",
    "prop:nuclear-groebner-reduction",
  ],
});
