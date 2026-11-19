import { prose } from "../../schema/builders";

export default prose({
  label: "prose:chapter-overview",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/codata-masses.witness.json",
      "computations/q-pinning-50-digit.witness.json",
      "computations/m-p-substrate-identity-50dps.witness.json",
      "computations/canonical-mass-table-extended.witness.json",
      "computations/ame-2020-binding-energies.witness.json",
      "computations/alpha-em-schwinger-ladder.witness.json",
    ],
    status: "verified",
  },
});
