import { definition } from "../../schema/builders";

export default definition({
  label: "def:skein-binding-lagrangian",
  title: "Skein binding Lagrangian for multi-nucleon links",
  tags: [
    "lagrangian",
    "binding",
    "skein",
    "nuclear",
    "coulomb",
    "strong-force",
    "pauli",
  ],
  lean: {
    decl: "QOU.Braiding.SkeinBindingLagrangian",
    validation: "not_checked",
  },
  uses: [
    "rem:skein-crossing-asymmetry",
    "def:hadron",
    "def:substrate-parameter",
  ],
});
