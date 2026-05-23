import { definition } from "../../schema/builders";

export default definition({
  label: "def:stable-nucleus",
  title: "Stable nucleus (Skein energy minimum)",
  tags: [
    "nucleus",
    "stability",
    "hadron",
    "proton",
    "neutron",
    "binding",
    "beta-stability",
    "lagrangian",
  ],
  lean: { ref: "qou:QOU.Torsion.StableNucleus",
    validation: "not_checked",
  },
  uses: ["prop:beta-stability"],
});
