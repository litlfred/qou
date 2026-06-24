import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:full-pole-structure-mass-trace",
  proofs: ["prf:full-pole-structure-mass-trace"],
  title:
    "Habiro completion of the mass trace",
  lean: {
    ref: "qou:QOU.BraidKnot.HabiroCompletion",
    validation: "not_checked",
  },
  cites: ["habiro2004", "jones1987"],
  tags: [
    "habiro-ring",
    "cyclotomic-completion",
    "markov-trace",
    "root-of-unity",
    "mass",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/markov/markov_substrate_realizer.py",
    witness: [
      "computations/habiro/habiro-interpolate-cross-validation.witness.json",
      "computations/markov/markov-substrate-realization.witness.json",
      "computations/d-from-scratch.witness.json",
      "computations/proton-mass-codata-50dps.witness.json",
    ],
    status: "experimental",
  },
});
