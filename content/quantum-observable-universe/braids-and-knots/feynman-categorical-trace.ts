import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:feynman-categorical-trace",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.FeynmanCategoricalTrace",
    validation: "not_checked",
  },
  title: "Feynman transition amplitude as categorical trace",
  tags: ["path-integral", "feynman", "categorical-trace", "markov-trace", "eigenbasis"],
  uses: ["prop:categorical-mass-markov"],
  proofs: ["prf:feynman-categorical-trace"],
});
