import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-markov-transition",
  proofs: ["prf:hecke-markov-transition"],
  title: "Hecke generator as stochastic transition operator",
  tags: [
    "hecke-algebra",
    "markov-chain",
    "transition-probability",
    "idempotent",
    "memoryless",
  ],
  lean: { ref: "qou:QOU.Braiding.SpectralIdempotentData",
    validation: "not_checked",
  },
  cites: ["diaconis-ram2000", "bufetov2020"],
  uses: ["prop:feynman-categorical-trace"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/hecke_markov_transition_probe.py",
    witness: "computations/probes/hecke-markov-transition-probe.witness.json",
    status: "verified",
  },
});
