import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:feynman-categorical-trace",
  title: "Feynman transition amplitude as categorical trace",
  tags: ["path-integral", "feynman", "categorical-trace", "markov-trace", "eigenbasis"],
  uses: [
    "prop:knot-eigenbasis-complete",
    "prop:categorical-mass-markov",
    "thm:jones-markov-trace",
  ],
  proofs: ["prf:feynman-categorical-trace"],
});
