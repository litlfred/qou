import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:markov-trace",
  title: "Markov trace on the Iwahori–Hecke algebra $H_n(q)$",
  uses: [
    "def:hecke-normal-form",
    "prop:markov-trace-axiomatic-closed-form",
    "prop:markov-trace-recursive-reducer",
  ],
  computation: {
    engine: "python+mpmath",
    script: "qou-mass/src/qou_mass/api.py",
    witness: "computations/markov-free-energy-qvalues.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-3",
    "markov-trace",
    "hecke",
    "canonical-chain",
    "alexander-markov",
  ],
});
