import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:deuterium-derived-binding",
  title:
    "Deuterium binding energy from the Markov trace volume integral",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/q-pinning-50-digit.witness.json",
      "computations/gram-matrix-dual.witness.json",
      "computations/binding-endomorphism-deuteron.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "deuterium",
    "binding-energy",
    "markov-trace",
    "derived",
    "zero-parameter",
    "volume-integral",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.deuterium_derived_binding",
    validation: "not_checked",
  },
  uses: ["prop:four-term-pair-nucleon"],
  cites: ["ame2020"],
});
