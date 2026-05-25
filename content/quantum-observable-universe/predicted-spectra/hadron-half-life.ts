import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hadron-half-life",
  title:
    "Hadron half-life from the $q$-deformed transition amplitude",
  tags: [
    "half-life",
    "beta-decay",
    "hadron",
    "transition-amplitude",
    "substrate-parameter",
    "valley-of-stability",
  ],
  lean: { ref: "qou:QOU.Archimedean.hadron_half_life",
    validation: "not_checked",
  },
  uses: ["prop:integer-stability"],
});
