import { prose } from "../../schema/builders";

export default prose({
  label: "prose:sm-params-gauge-couplings",
  title: "Gauge couplings (3)",
  tags: ["appendix", "standard-model", "parameters", "gauge-couplings", "alpha-em"],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/alpha-em-schwinger-ladder.witness.json",
      "computations/alpha-em-form-ladder.witness.json",
    ],
    status: "verified",
  },
});
