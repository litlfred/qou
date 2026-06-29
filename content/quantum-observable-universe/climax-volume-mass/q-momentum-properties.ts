import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-momentum-properties",
  title: "Additivity, Markov invariance, and parity of $q$-momentum",
  lean: { ref: "qou:QOU.Archimedean.QMomentumProperties",
    validation: "not_checked",
  },
  uses: ["def:q-momentum"],
  tags: [
    "momentum",
    "q-deformed",
    "additivity",
    "markov-invariance",
    "parity",
  ],
});
