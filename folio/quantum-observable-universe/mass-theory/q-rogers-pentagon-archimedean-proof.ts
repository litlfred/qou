import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-rogers-pentagon-archimedean",
  title: "Proof of q rogers pentagon archimedean",
  uses: ["prop:q-rogers-pentagon-archimedean"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/pentagon-reduction-li2q.witness.json.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/pentagon_reduction_li2q.py",
    witness: [
      "computations/pentagon-reduction-li2q.witness.json",
      "computations/qbeta/qbeta-dladder-fibre-two-action.witness.json",
      "computations/pentagon-multipair-borromean-h4-probe.witness.json",
    ],
    status: "verified",
  },
});
