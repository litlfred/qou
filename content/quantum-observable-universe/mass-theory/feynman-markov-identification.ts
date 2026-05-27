import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:feynman-markov-identification",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.markov_identification",
    validation: "not_checked",
  },
  title: "Markov-weighted eigenbasis sum equals the Markov trace",
  tags: ["markov-trace", "wedderburn", "feynman", "hecke", "identification"],
  uses: ["lem:feynman-eigenbasis-decomposition", "thm:jones-markov-trace"],
  proofs: ["prf:feynman-markov-identification"],
});
