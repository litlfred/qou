import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:level-sufficiency",
  proofs: ["prf:level-sufficiency"],
  title:
    "Level sufficiency: Markov trace computable in the coarsest confinement algebra",
  lean: { ref: "qou:QOU.BraidKnot.LevelSufficiency",
    validation: "not_checked",
  },
  tags: [
    "confinement",
    "markov-trace",
    "filtration",
    "hecke-inclusion",
    "computational-minimality",
  ],
});
