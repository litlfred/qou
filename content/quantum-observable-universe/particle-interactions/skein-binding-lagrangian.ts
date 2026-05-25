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
  lean: { ref: "qou:QOU.Braiding.SkeinBindingLagrangian",
    validation: "not_checked",
  },
  uses: ["prop:qou-canonical-action"],
});
