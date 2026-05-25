import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-q-categorical-truncation",
  title: "Brane-tower truncation depth = NF support depth (centre stratification)",
  lean: { ref: "qou:QOU.WedderburnMass.phi_q_categorical_truncation",
    validation: "not_checked",
  },
  uses: [
    "prop:spectral-sequence-collapse",
    "prop:curvature-rank-gb-stratification",
    "prop:categorical-mass-markov",
    "cor:quantum-dilogarithm",
    "def:hecke-normal-form",
    "def:confinement-level",
    "prop:full-pole-structure-mass-trace",
    "cor:habiro-expansion-atomic",
  ],
  proofs: ["prf:phi-q-categorical-truncation"],
  tags: [
    "brane-tower",
    "spectral-sequence",
    "yekutieli",
    "regularization",
    "centre-stratification",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/probe_tritium_k_star.py",
    witness: "folio-assistant/computations/probe-tritium-k-star.witness.json",
    status: "experimental",
  },
});
