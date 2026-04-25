import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-crossing-asymmetry",
  title: "Crossing asymmetry and per-crossing Coulomb correction",
  tags: ["skein", "crossing", "coulomb", "asymmetry", "r-matrix"],
  lean: { ref: "qou:QOU.Braiding.skein_crossing_asymmetry",
    validation: "not_checked",
  },
  uses: ["def:coulomb-charge"],
});
