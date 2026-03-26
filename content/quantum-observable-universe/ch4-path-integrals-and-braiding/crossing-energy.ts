import { definition } from "../../schema/builders";

export default definition({
  label: "def:crossing-energy",
  title: "Crossing energy of a knot composite",
  tags: ["crossing", "energy", "skein", "r-matrix", "stability"],
  lean: {
    decl: "QOU.Braiding.CrossingEnergy",
    validation: "not_checked",
  },
  uses: [
    "rem:r-matrix-braiding",
    "def:quantum-su2",
    "def:substrate-parameter",
  ],
});
