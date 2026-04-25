import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:heisenberg-commutator",
  title: "$q$-deformed Heisenberg commutator from the Reeb fibre",
  tags: ["heisenberg", "uncertainty", "reeb", "commutator"],
  lean: { ref: "qou:QOU.DescartesUniverse.heisenberg_commutator",
    validation: "not_checked",
  },
  uses: ["def:quantum-planck-constant"],
});
