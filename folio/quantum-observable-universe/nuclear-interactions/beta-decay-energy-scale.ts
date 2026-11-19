import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:nucleon-nf-observability",
  label: "rem:beta-decay-energy-scale",
  title:
    "Energy scale of the Hecke normal form: from dimensionless debt to MeV",
  tags: [
    "beta-decay",
    "energy-scale",
    "normalization",
    "decay-energy",
    "leptonic-debt",
    "color-tube",
    "hecke-algebra",
    "computational-witness",
  ],
  uses: [
    "rem:nucleon-nf-observability",
    "prop:beta-decay-transfer-matrix",
  ],
  computation: {
    engine: "sympy",
    script: "computations/q_beta_form_a_n1_extension.py",
    witness: [
      "computations/q-beta-form-a-n1-extension.witness.json",
      "computations/confinement-operator-selection.witness.json",
      "computations/probes/nuclear-wave3-periodic-table-synthesis.witness.json",
      "computations/free-neutron-decay.witness.json",
    ],
    status: "experimental",
  },
});
