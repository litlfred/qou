import { prose } from "../../schema/builders";

export default prose({
  label: "prose:sm-params-gauge-couplings",
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): of [the per-observable status dashboard](#rem:per-observable-100x-status-dashboard)" },
  ],
  title: "Gauge couplings (3)",
  tags: ["appendix", "standard-model", "parameters", "gauge-couplings", "alpha-em"],
  computation: {
    engine: "python",
    script: "computations/alpha_em_4pi_fixed_point_solve.py",
    witness: ["computations/alpha-em-4pi-fixed-point-solve.witness.json"],
    status: "experimental",
  },
});
