import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:per-isotope-binding",
  title: "Per-isotope binding $B(K) = m_e \\cdot \\sum_\\lambda y_\\lambda \\chi^\\lambda \\Delta_\\lambda$",
  uses: [
    "rem:term6-binding-density",
    "thm:knot-mass-formula-unified",
    "alg:markov-trace",
    "prop:linear-chain-bond-count",
    // ²H reeb-flow tier (owner ruling 2026-07-07: kept, NEAR-MATCH label)
    "prop:reeb-pn-magnitude-criticality",
    "conj:reeb-linking-cwf-normalization",
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
