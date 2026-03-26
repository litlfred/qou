import { definition } from "../../schema/builders";

export default definition({
  label: "def:coulomb-charge",
  title: "Coulomb charge of a knot composite",
  tags: ["coulomb", "charge", "crossing", "asymmetry", "skein"],
  lean: {
    decl: "QOU.Braiding.CoulombCharge",
    validation: "not_checked",
  },
  uses: [
    "def:crossing-energy",
    "rem:r-matrix-braiding",
  ],
});
