import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:per-isotope-binding",
  title: "Per-isotope binding $B(K) = m_e \\cdot \\sum_\\lambda y_\\lambda \\chi^\\lambda \\Delta_\\lambda$",
  uses: [
    "rem:term6-binding-density",
    "thm:knot-mass-formula-unified",
    "alg:markov-trace",
  ],
  computation: {
    engine: "python+mpmath",
    script: "qou-mass/src/qou_mass/api.py",
    witness: "computations/canonical-mass-table-242ppb.witness.json",
    status: "experimental",
  },
  tags: [
    "mba",
    "step-9b",
    "binding-energy",
    "delta-lambda",
    "per-isotope",
    "canonical-chain",
    "open-gate",
  ],
});
