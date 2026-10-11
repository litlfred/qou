import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:integer-stability",
  label: "rem:stability-cubic-plot",
  title:
    "The stability cubic at $q = 1.1100$: lattice points and the nuclear chart",
  tags: [
    "stability-cubic",
    "lattice-points",
    "nuclear-chart",
    "codata",
    "plot",
  ],
  uses: [
    "rem:diophantine-valley",
    "prop:beta-stability",
    "prop:neutron-prediction-comparison",
  ],
  computation: {
    engine: "python",
    script: "computations/observations/stability_cubic_table_from_probe.py",
    witness: "computations/observations/neutron_prediction_comparison_probe.witness.json",
    status: "verified",
  },
});
