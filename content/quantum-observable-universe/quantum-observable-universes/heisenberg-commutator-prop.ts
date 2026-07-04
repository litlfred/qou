import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:heisenberg-commutator",
  title: "$q$-deformed Heisenberg commutator from the Reeb fibre",
  tags: ["heisenberg", "uncertainty", "reeb", "commutator"],
  lean: { ref: "qou:QOU.ArchimedeanUniverse.heisenberg_commutator",
    validation: "not_checked",
  },
  uses: ["def:q-deformed-commutator", "def:quantum-planck-constant"],
});
