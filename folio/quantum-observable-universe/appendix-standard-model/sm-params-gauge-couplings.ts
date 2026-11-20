import { prose } from "../../schema/builders";

export default prose({
  label: "prose:sm-params-gauge-couplings",
  title: "Gauge couplings (3)",
  tags: ["appendix", "standard-model", "parameters", "gauge-couplings", "alpha-em"],
  computation: {
    engine: "python",
    script: "computations/alpha_em_4pi_fixed_point_solve.py",
    witness: ["computations/alpha-em-4pi-fixed-point-solve.witness.json"],
    status: "experimental",
  },
});
