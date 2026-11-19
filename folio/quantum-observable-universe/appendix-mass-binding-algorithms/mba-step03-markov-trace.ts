import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:markov-trace",
  title: "Convention-D Markov trace on the Iwahori–Hecke algebra $H_n(q)$",
  uses: [
    "def:hecke-normal-form",
    "prop:markov-trace-axiomatic-closed-form",
    "prop:markov-trace-recursive-reducer",
    "prop:convention-d-kills-antisymmetriser",
    "alg:gs-reduce-to-hecke-nf",
  ],
  tags: [
    "mba",
    "step-3",
    "markov-trace",
    "convention-d",
    "hecke",
    "canonical-chain",
  ],
});
