import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:corrected-markov-trace",
  title:
    "Corrected Markov trace of the trefoil braid",
  tags: [
    "markov-trace",
    "correction",
    "trefoil",
    "yang-baxter",
    "adjacent-generators",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.corrected_markov_trace",
    validation: "not_checked",
  },
  uses: [
    "thm:jones-markov-trace",
  ],
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/corrected_markov_trace.py",
    witness: [
      "computations/corrected-markov-trace.witness.json",
    ],
  },
});
