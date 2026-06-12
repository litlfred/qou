import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:per-isotope-binding",
  title: "Per-isotope binding $B(K) = m_e \\cdot \\sum_\\lambda y_\\lambda \\chi^\\lambda \\Delta_\\lambda$",
  uses: [
    "prop:term6-binding-density",
    "thm:knot-mass-formula-unified",
  ],
  computation: {
    engine: "python",
    script: "qou-mass/src/qou_mass/prediction.py",
    witness: "qou-mass/src/qou_mass/data/isotopes/canonical-isotope-witness-Z*.witness.json",
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
