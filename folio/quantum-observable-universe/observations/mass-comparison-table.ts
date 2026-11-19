import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:topological-mass-formula",
  label: "rem:mass-comparison-table",
  title: "Mass predictions from knot formulas vs. CODATA/PDG values",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: ["computations/q-pinning-50-digit.witness.json", "computations/codata-masses.witness.json"],
    status: "verified",
  },
  tags: [
    "mass",
    "prediction",
    "CODATA",
    "PDG",
    "comparison",
    "knot",
    "experimental",
  ],
  uses: ["rem:mass-from-generators"],
  authorNotes: [
    {
      kind: "note",
      body: "Supporting witnesses referenced across sections: computations/atomic-mass-via-rho-k.witness.json, computations/m-p-substrate-identity-50dps.witness.json, computations/two-term-qed-isotope-and-nucleon-compute.witness.json, computations/qbeta/qbeta-wedderburn-phase-twoterm-pin.witness.json, computations/q-beta-predicted.witness.json, and certificate-to-mass.witness.json.",
    },
  ],
});
