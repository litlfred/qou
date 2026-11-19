import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-markov-transition",
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
  uses: [],
  computation: {
    engine: "mpmath",
    script: "computations/probes/hecke_markov_transition_probe.py",
    witness: "computations/probes/hecke-markov-transition-probe.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "Item (iv) said the Markov trace of any braid factors as a product of independent vertex volumes. That holds only for words using each generator at most once; for $\\sigma_1\\sigma_2\\sigma_1$ the trace is $h z^2 + z$, not $z^3$. Statement, proof and Lean docstring are scoped. The Lean `MarkovChainFactorization` carried the product formula as a field, so it assumed it. Fixed 2026-11-16: `totalTrace` is now defined as the product of vertex volumes; its identification with the Markov trace of the grouped word is not proved in Lean.",
    },
  ],
});
