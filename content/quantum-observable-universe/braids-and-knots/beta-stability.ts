import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:beta-stability",
  title: "Beta-stability line from the Skein binding Lagrangian",
  tags: [
    "stability",
    "beta-decay",
    "neutron",
    "valley-of-stability",
    "coulomb",
    "lagrangian",
  ],
  lean: { ref: "qou:QOU.Braiding.beta_stability",
    validation: "not_checked",
  },
  uses: ["def:skein-binding-lagrangian"],
});
