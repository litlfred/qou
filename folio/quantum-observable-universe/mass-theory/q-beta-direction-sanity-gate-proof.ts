import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-beta-direction-sanity-gate-argument",
  interprets: "rem:q-beta-direction-sanity-gate",
  title: "Argument for q beta direction sanity gate (not a proof)",
  uses: ["rem:q-beta-direction-sanity-gate"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: qbeta-radius-of-convergence-gate-probe.witness.json.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/qbeta/qbeta_radius_of_convergence_gate_probe.py",
    witness: [
      "computations/qbeta/qbeta-radius-of-convergence-gate-probe.witness.json",
      "computations/qbeta/qbeta-direction-sanity-gate-probe.witness.json",
    ],
    status: "verified",
  },
});
